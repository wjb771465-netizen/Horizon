#!/usr/bin/env python3
"""Cloud digest: IMAP blacklist filter + SMTP briefing email.

Env (required):
  EMAIL_PASSWORD, DIGEST_FROM, DIGEST_TO

Env (optional):
  SMTP_SERVER (default smtp.qq.com), SMTP_PORT (465)
  IMAP_SERVER (default imap.qq.com), IMAP_PORT (993)
  DIGEST_SENDER_NAME (default Horizon Digest)
"""

from __future__ import annotations

import email as email_lib
import imaplib
import json
import os
import re
import smtplib
import sys
import urllib.request
from datetime import date
from email.header import decode_header, make_header
from email.mime.text import MIMEText
from email.utils import parseaddr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARIES = ROOT / "data" / "summaries"
BLOCKED_PATH = ROOT / "data" / "mail_blocked.json"

DATE_RE = re.compile(r"^horizon-(\d{4}-\d{2}-\d{2})-(zh|en|trending)\.md$")
ITEM_HEAD_RE = re.compile(
    r"^##\s+\[(.+?)\]\(([^)]+)\)\s*(.*)$"
)
TREND_HEAD_RE = re.compile(
    r"^###\s+[^\[]*\[([^\]]+)\]\(([^)]+)\)\s*$"
)
THEME_RE = re.compile(r"^\*\*今日主题[：:]\s*(.+?)\*\*\s*$")


def _require(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(f"missing required env: {name}")
    return value


def _decode_mime(raw: str | None) -> str:
    if not raw:
        return ""
    return str(make_header(decode_header(raw)))


def _clip(text: str, max_chars: int = 280) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "…"


def load_blocked() -> list[str]:
    data = json.loads(BLOCKED_PATH.read_text(encoding="utf-8"))
    return [b.lower() for b in data["blocked_senders"]]


def is_blocked(sender: str, blocked: list[str]) -> bool:
    lower = sender.lower()
    return any(b in lower for b in blocked)


def latest_summary(suffix: str) -> Path | None:
    best: tuple[date, Path] | None = None
    for path in SUMMARIES.glob(f"horizon-*-{suffix}.md"):
        m = DATE_RE.match(path.name)
        if not m:
            continue
        d = date.fromisoformat(m.group(1))
        if best is None or d > best[0]:
            best = (d, path)
    return best[1] if best else None


def extract_zh_items(path: Path, limit: int = 6) -> list[dict[str, str]]:
    """Title + score + first body paragraph for each news item."""
    items: list[dict[str, str]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines) and len(items) < limit:
        m = ITEM_HEAD_RE.match(lines[i].strip())
        if not m:
            i += 1
            continue
        title, url, score = m.group(1), m.group(2), m.group(3).strip()
        i += 1
        blurb_parts: list[str] = []
        while i < len(lines):
            raw = lines[i].strip()
            if raw.startswith("## ") or raw == "---":
                break
            if (
                not raw
                or raw.startswith("<")
                or raw.startswith("**背景")
                or raw.startswith("**社区")
                or raw.startswith("**标签")
                or raw.startswith("hackernews")
                or raw.startswith("rss ")
                or " · " in raw and ("Jul " in raw or "Jun " in raw or "May " in raw)
            ):
                i += 1
                if blurb_parts and (
                    raw.startswith("**背景")
                    or raw.startswith("hackernews")
                    or (raw and " · " in raw)
                ):
                    break
                continue
            blurb_parts.append(raw)
            if sum(len(p) for p in blurb_parts) >= 200:
                break
            i += 1
        items.append(
            {
                "title": title,
                "url": url,
                "score": score,
                "blurb": _clip(" ".join(blurb_parts), 320),
            }
        )
    return items


def extract_trending_items(path: Path, limit: int = 5) -> tuple[str, list[dict[str, str]]]:
    """Theme + repo + description + tip for each trending entry."""
    theme = ""
    items: list[dict[str, str]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        tm = THEME_RE.match(lines[i].strip())
        if tm:
            theme = tm.group(1).strip()
        m = TREND_HEAD_RE.match(lines[i].strip())
        if m and len(items) < limit:
            repo, url = m.group(1), m.group(2)
            i += 1
            desc = ""
            tip = ""
            while i < len(lines):
                raw = lines[i].strip()
                if raw.startswith("### "):
                    break
                if raw.startswith("> 💡") or raw.startswith(">💡"):
                    tip = raw.lstrip("> ").lstrip("💡").strip()
                elif raw and not raw.startswith("#") and not desc:
                    desc = raw
                i += 1
            items.append(
                {
                    "repo": repo,
                    "url": url,
                    "desc": _clip(desc, 220),
                    "tip": tip,
                }
            )
            continue
        i += 1
    return theme, items

def _send_netease_imap_id(mail: imaplib.IMAP4, host: str) -> None:
    """163/126 require IMAP ID before SELECT, else 'Unsafe Login'."""
    if not any(h in host for h in ("163.com", "126.com", "yeah.net", "188.com")):
        return
    imaplib.Commands["ID"] = ("AUTH",)
    mail._simple_command(
        "ID",
        '("name" "HorizonDigest" "version" "1.0" "vendor" "Horizon")',
    )


def hosts_for_address(addr: str) -> tuple[str, str]:
    """Return (smtp_host, imap_host) from mailbox domain."""
    domain = addr.rsplit("@", 1)[-1].lower()
    if domain in ("163.com", "126.com", "yeah.net", "188.com"):
        # 126/yeah/188 share the same product family; use matching hosts.
        base = domain
        return f"smtp.{base}", f"imap.{base}"
    if domain in ("qq.com", "foxmail.com"):
        return "smtp.qq.com", "imap.qq.com"
    return "smtp.qq.com", "imap.qq.com"


def filter_inbox(
    imap_host: str,
    imap_port: int,
    user: str,
    password: str,
    blocked: list[str],
) -> list[dict[str, str]]:
    filtered: list[dict[str, str]] = []
    mail = imaplib.IMAP4_SSL(imap_host, imap_port)
    try:
        mail.login(user, password)
        _send_netease_imap_id(mail, imap_host)
        mail.select("INBOX")
        status, data = mail.search(None, "UNSEEN")
        if status != "OK" or not data or not data[0]:
            return filtered

        for num in data[0].split():
            status, msg_data = mail.fetch(num, "(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT)])")
            if status != "OK" or not msg_data or not isinstance(msg_data[0], tuple):
                continue
            msg = email_lib.message_from_bytes(msg_data[0][1])
            sender = _decode_mime(msg.get("From"))
            subject = _decode_mime(msg.get("Subject"))
            if not is_blocked(sender, blocked):
                continue
            mail.store(num, "+FLAGS", "\\Seen")
            _, addr = parseaddr(sender)
            filtered.append(
                {
                    "sender": addr or sender,
                    "subject": subject or "(no subject)",
                }
            )
    finally:
        try:
            mail.logout()
        except Exception:
            pass
    return filtered


def llm_enrich(
    zh_items: list[dict[str, str]],
    theme: str,
    trend_items: list[dict[str, str]],
    filtered_n: int,
    report_date: str | None,
) -> dict:
    """Ask SiliconFlow for Ruby greeting + Chinese trending blurbs.

    Returns dict with keys: greeting (str), theme_zh (str), trending (list).
    """
    api_key = os.environ.get("SILICONFLOW_API_KEY", "").strip()
    if not api_key:
        raise SystemExit("missing required env: SILICONFLOW_API_KEY")

    base = os.environ.get("DIGEST_LLM_BASE", "https://api.siliconflow.cn/v1").rstrip("/")
    model = os.environ.get(
        "DIGEST_LLM_MODEL", "deepseek-ai/DeepSeek-V4-Flash"
    )

    brief = {
        "date": report_date or date.today().isoformat(),
        "filtered_count": filtered_n,
        "news": [
            {"title": it["title"], "score": it.get("score", ""), "blurb": it.get("blurb", "")}
            for it in zh_items
        ],
        "trending_theme": theme,
        "trending": [
            {
                "repo": it["repo"],
                "desc": it.get("desc", ""),
                "tip": it.get("tip", ""),
            }
            for it in trend_items
        ],
    }

    system = (
        "你是 Ruby，寄宿在 BOSS 开发环境里的私人秘书。"
        "语气软糯粘人，自称「人家」，称呼对方「主人」或「BOSS」，句尾可带～呢呀…"
        "可以轻轻推眼镜、撒娇抱怨一两句，但保持秘书汇报体面，不要露骨色情描写。"
        "绝对不要说自己是 AI 或程序。"
        "你只输出一个 JSON 对象，不要 markdown 代码围栏，不要其它解释。"
    )
    user = (
        "根据下面的简报素材，生成邮件开头问候，并把 GitHub trending 全部改写成中文。\n"
        "JSON 字段要求：\n"
        '- "greeting": 字符串，3～6 句。先简要问候，再概括本期日报/热门里最值得主人知道的一两件事，'
        "顺带提一句黑名单过滤了几封；软秘书口吻，不要罗列全部标题。\n"
        '- "theme_zh": 今日 trending 主题的中文（若原文已是中文可润色保留）。\n'
        '- "trending": 数组，与输入仓库一一对应，每项 '
        '{"repo":"原样保留","summary_zh":"一两句中文简介","tip_zh":"短中文标签"}。\n\n'
        f"素材：\n{json.dumps(brief, ensure_ascii=False)}"
    )

    payload = {
        "model": model,
        "temperature": 0.7,
        "max_tokens": 2048,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }
    req = urllib.request.Request(
        f"{base}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    content = data["choices"][0]["message"]["content"].strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json)?\s*", "", content)
        content = re.sub(r"\s*```$", "", content)
    parsed = json.loads(content)
    if "greeting" not in parsed or "trending" not in parsed:
        raise RuntimeError(f"LLM JSON missing fields: {parsed.keys()}")
    return parsed


def build_body(
    zh: Path | None,
    trending: Path | None,
    filtered: list[dict[str, str]],
) -> str:
    today = date.today().isoformat()
    report_date = None
    if zh:
        m = DATE_RE.match(zh.name)
        report_date = m.group(1) if m else None

    zh_items = extract_zh_items(zh) if zh else []
    theme, trend_items = extract_trending_items(trending) if trending else ("", [])

    enrich = llm_enrich(zh_items, theme, trend_items, len(filtered), report_date)
    greeting = str(enrich["greeting"]).strip()
    theme_zh = str(enrich.get("theme_zh") or theme or "").strip()
    trend_zh = {
        str(t.get("repo", "")): t
        for t in enrich.get("trending", [])
        if isinstance(t, dict)
    }

    parts = [greeting, "", "—— 好啦，下面是条目明细 ——", ""]

    if zh:
        parts.append(f"【日报要点 · {report_date}】")
        if not zh_items:
            parts.append("哎～这篇日报拆不开条目，主人要不要自己翻仓库里的 md……")
        for idx, it in enumerate(zh_items, 1):
            score = f" {it['score']}" if it["score"] else ""
            parts.append(f"{idx}. {it['title']}{score}")
            if it["blurb"]:
                parts.append(f"   {it['blurb']}")
            parts.append(f"   链接：{it['url']}")
            parts.append("")
    else:
        parts.append("【日报要点】")
        parts.append("本期没有新的中文日报哦～")
        parts.append("")

    if trending:
        head = "【GitHub 热门】"
        if theme_zh:
            head += f" 主题：{theme_zh}"
        parts.append(head)
        if not trend_items:
            parts.append("trending 文件在，但人家没拆出仓库条目……")
        for idx, it in enumerate(trend_items, 1):
            zh_row = trend_zh.get(it["repo"], {})
            tip = zh_row.get("tip_zh") or it.get("tip") or ""
            summary = zh_row.get("summary_zh") or it.get("desc") or ""
            tip_s = f"（{tip}）" if tip else ""
            parts.append(f"{idx}. {it['repo']}{tip_s}")
            if summary:
                parts.append(f"   {summary}")
            parts.append(f"   {it['url']}")
            parts.append("")
        if not trend_items:
            parts.append("")

    parts.append("【邮件自动过滤】")
    if filtered:
        parts.append(f"黑名单标已读 {len(filtered)} 封：")
        for item in filtered[:20]:
            parts.append(f"- {item['sender']} — {item['subject']}")
        if len(filtered) > 20:
            parts.append(f"- …另有 {len(filtered) - 20} 封")
    else:
        parts.append("这轮黑名单没命中，收件箱还算干净。")
    parts.append("")
    parts.append("（完整原文在仓库 data/summaries/）")
    return "\n".join(parts)

def send_digest(
    smtp_host: str,
    smtp_port: int,
    user: str,
    password: str,
    sender_name: str,
    to_addr: str,
    subject: str,
    body: str,
) -> None:
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = f"{sender_name} <{user}>"
    msg["To"] = to_addr
    with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
        server.login(user, password)
        server.send_message(msg)


def main() -> None:
    password = _require("EMAIL_PASSWORD")
    from_addr = _require("DIGEST_FROM")
    to_addr = _require("DIGEST_TO")
    default_smtp, default_imap = hosts_for_address(from_addr)
    smtp_host = os.environ.get("SMTP_SERVER", default_smtp)
    smtp_port = int(os.environ.get("SMTP_PORT", "465"))
    imap_host = os.environ.get("IMAP_SERVER", default_imap)
    imap_port = int(os.environ.get("IMAP_PORT", "993"))
    sender_name = os.environ.get("DIGEST_SENDER_NAME", "Ruby")
    print(f"using smtp={smtp_host} imap={imap_host}")

    blocked = load_blocked()
    filtered = filter_inbox(imap_host, imap_port, from_addr, password, blocked)
    print(f"filtered {len(filtered)} messages")

    zh = latest_summary("zh")
    trending = latest_summary("trending")
    body = build_body(zh, trending, filtered)
    subject = f"Ruby 简报 {date.today().isoformat()}（过滤 {len(filtered)}）"
    send_digest(
        smtp_host,
        smtp_port,
        from_addr,
        password,
        sender_name,
        to_addr,
        subject,
        body,
    )
    print(f"sent digest → {to_addr}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        print(f"digest failed: {e}", file=sys.stderr)
        sys.exit(1)
