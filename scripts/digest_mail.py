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
from datetime import date
from email.header import decode_header, make_header
from email.mime.text import MIMEText
from email.utils import parseaddr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARIES = ROOT / "data" / "summaries"
BLOCKED_PATH = ROOT / "data" / "mail_blocked.json"

TOC_RE = re.compile(r"^\d+\.\s+\[(.+?)\]\([^)]*\)(.*)$")
DATE_RE = re.compile(r"^horizon-(\d{4}-\d{2}-\d{2})-(zh|en|trending)\.md$")


def _require(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(f"missing required env: {name}")
    return value


def _decode_mime(raw: str | None) -> str:
    if not raw:
        return ""
    return str(make_header(decode_header(raw)))


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


def extract_toc(path: Path, limit: int = 8) -> list[str]:
    lines: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = TOC_RE.match(line.strip())
        if not m:
            if lines:
                break
            continue
        title, rest = m.group(1), m.group(2).strip()
        lines.append(f"- {title}{(' ' + rest) if rest else ''}")
        if len(lines) >= limit:
            break
    return lines


def extract_trending_top(path: Path, limit: int = 5) -> list[str]:
    lines: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("### ") and any(ch.isdigit() for ch in line[:8]):
            # e.g. ### 1️⃣ [repo](url)
            title = re.sub(r"^###\s+", "", line)
            title = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", title)
            lines.append(f"- {title.strip()}")
            if len(lines) >= limit:
                break
    return lines


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


def build_body(
    zh: Path | None,
    trending: Path | None,
    filtered: list[dict[str, str]],
) -> str:
    today = date.today().isoformat()
    parts = [
        f"你好，这是 Horizon 三天简报（{today}）。",
        "",
    ]

    if zh:
        m = DATE_RE.match(zh.name)
        report_date = m.group(1) if m else zh.name
        parts.append(f"## 日报要点（{report_date}）")
        toc = extract_toc(zh)
        parts.extend(toc if toc else ["（未能从日报提取目录）"])
        parts.append("")
    else:
        parts.append("## 日报要点")
        parts.append("本期没有新的中文日报。")
        parts.append("")

    if trending:
        parts.append("## GitHub Trending")
        tops = extract_trending_top(trending)
        parts.extend(tops if tops else ["（未能提取 trending 条目）"])
        parts.append("")

    parts.append("## 邮件自动过滤")
    parts.append(f"本期按黑名单标已读：{len(filtered)} 封。")
    for item in filtered[:20]:
        parts.append(f"- {item['sender']} — {item['subject']}")
    if len(filtered) > 20:
        parts.append(f"- …另有 {len(filtered) - 20} 封")
    parts.append("")
    parts.append("详情见仓库 data/summaries/。需要操作邮件或待办时再叫 Ruby。")
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
    smtp_host = os.environ.get("SMTP_SERVER", "smtp.qq.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "465"))
    imap_host = os.environ.get("IMAP_SERVER", "imap.qq.com")
    imap_port = int(os.environ.get("IMAP_PORT", "993"))
    sender_name = os.environ.get("DIGEST_SENDER_NAME", "Horizon Digest")

    blocked = load_blocked()
    filtered = filter_inbox(imap_host, imap_port, from_addr, password, blocked)
    print(f"filtered {len(filtered)} messages")

    zh = latest_summary("zh")
    trending = latest_summary("trending")
    body = build_body(zh, trending, filtered)
    subject = f"Horizon 简报 {date.today().isoformat()}（过滤 {len(filtered)}）"
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
