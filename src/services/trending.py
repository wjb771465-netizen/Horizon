"""GitHub trending daily report — standalone Horizon service.

Fetches trending repos from OSS Insight, filters by AI keywords, and uses
the configured AI provider to generate a curated daily summary.

Integrated as: horizon-trending CLI command.
"""

import asyncio
import html as html_mod
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import List
from zoneinfo import ZoneInfo

import httpx
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

from ..ai.client import create_ai_client
from ..storage.manager import StorageManager

console = Console()

TRENDING_URL = "https://github.com/trending"

DEFAULT_KEYWORDS = [
    "llm", "gpt", "rag", "agent", "inference", "cuda", "triton",
    "vector", "diffusion", "transformer", "embedding", "vllm", "sglang",
    "langchain", "llama", "mistral", "claude", "openai", "mcp",
]

DEFAULT_LANGUAGES = ["All", "Python", "TypeScript", "Rust"]

SYSTEM_PROMPT = """你是一个技术新闻编辑，擅长从 GitHub 热门仓库中发现技术趋势。

从用户提供的仓库列表中，用一句中文概括今日主题，并选出最值得关注的 Top 5 仓库。

严格按以下 JSON 格式输出，不要 markdown 包裹，不要输出其他内容：
{
  "theme": "今日主题（15字以内中文）",
  "top5": [
    {
      "rank": 1,
      "name": "owner/repo（必须填写，从列表中复制完整仓库名）",
      "url": "https://github.com/owner/repo",
      "desc": "中文简介（一两句，不要英文原文）",
      "reason": "中文推荐理由（20字以内）"
    }
  ]
}"""


def _match_keywords(repo: dict, keywords: List[str]) -> bool:
    text = (
        f"{repo.get('repo_name', '')} "
        f"{repo.get('description', '')} "
        f"{repo.get('collection_names', '')}"
    )
    text_lower = text.lower()
    return any(kw in text_lower for kw in keywords)


def _clean_html(s: str) -> str:
    s = re.sub(r"<svg.*?</svg>", "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    return html_mod.unescape(s).strip()


def _parse_trending_html(html: str) -> List[dict]:
    """Parse github.com/trending page into repo dicts."""
    repos = []
    for row in html.split('class="Box-row"')[1:]:
        m = re.search(r'<h2[^>]*>\s*<a[^>]*href="/([^"]+)"', row)
        if not m:
            continue
        name = m.group(1).rstrip("/")
        d = re.search(r'<p class="col-9[^"]*">\s*(.*?)\s*</p>', row, re.S)
        desc = _clean_html(d.group(1)) if d else ""
        lang_m = re.search(r'itemprop="programmingLanguage">([^<]+)<', row)
        lang = lang_m.group(1) if lang_m else ""
        today_m = re.search(r"([\d,]+)\s*stars (?:today|this week|this month)", row)
        stars_today = int(today_m.group(1).replace(",", "")) if today_m else 0
        repos.append({
            "repo_id": name,
            "repo_name": name,
            "description": desc,
            "primary_language": lang,
            "stars": stars_today,
        })
    return repos


async def fetch_trending(since: str = "daily") -> List[dict]:
    async with httpx.AsyncClient(
        timeout=30, headers={"User-Agent": "Horizon-Aggregator"}, follow_redirects=True
    ) as client:
        resp = await client.get(TRENDING_URL, params={"since": since})
        resp.raise_for_status()
        repos = _parse_trending_html(resp.text)
    repos.sort(key=lambda r: r.get("stars", 0), reverse=True)
    return repos


def build_prompt(repos: List[dict], max_repos: int) -> str:
    filtered = [r for r in repos if _match_keywords(r, DEFAULT_KEYWORDS)][:max_repos]
    if not filtered:
        return ""

    lines = []
    for i, r in enumerate(filtered, 1):
        name = r.get("repo_name", "?")
        desc = r.get("description", "") or "无描述"
        lang = r.get("primary_language", "?")
        stars = r.get("stars", "?")
        lines.append(f"[{i}] {name} ({lang}) +{stars}⭐/今日\n    {desc}")

    today = datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d")
    return f"以下是 {today} GitHub 上 AI 相关的热门仓库：\n\n" + "\n\n".join(lines)


async def run_trending(
    data_dir: str = "data",
    keywords: List[str] | None = None,
    since: str = "daily",
    max_repos: int = 15,
) -> str:
    if keywords is not None:
        global DEFAULT_KEYWORDS
        DEFAULT_KEYWORDS = keywords

    # Load config for AI settings
    storage = StorageManager(data_dir=str(Path(data_dir)))
    config = storage.load_config()

    # Fetch
    console.print("[bold cyan]📊 Fetching GitHub trending repos...[/bold cyan]")
    repos = await fetch_trending(since)
    console.print(f"   {len(repos)} repos from github.com/trending ({since})")

    # Filter
    filtered = [r for r in repos if _match_keywords(r, DEFAULT_KEYWORDS)]
    console.print(f"   {len(filtered)} AI-related repos after keyword filter")

    if not filtered:
        console.print("[yellow]   No AI-related repos today — keeping previous report untouched.[/yellow]")
        return "今日暂无 AI 相关热门仓库。"

    # AI summary
    console.print("[bold cyan]🤖 Generating trending summary...[/bold cyan]")
    ai_client = create_ai_client(config.ai)
    response = await ai_client.complete(
        system=SYSTEM_PROMPT,
        user=build_prompt(repos, max_repos),
    )

    # Parse & render
    import json

    try:
        data = json.loads(response)
    except json.JSONDecodeError:
        console.print("[red]AI response parse failed, raw output:[/red]")
        return response

    today = datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d")
    theme = data.get("theme", "AI 编程生态活跃")
    top5 = data.get("top5", [])

    lines = [
        f"# GitHub 今日热门 — {today}",
        "",
        f"**今日主题：{theme}**",
        "",
        "## 🏆 Top 5",
        "",
    ]
    for item in top5[:5]:
        rank = item.get("rank", "?")
        name = item.get("name", "")
        url = item.get("url", "")
        # Fallback: extract owner/repo from URL if name is missing
        if not name and url:
            name = url.replace("https://github.com/", "").rstrip("/")
        if not name:
            name = "?"
        desc = item.get("desc", "")
        reason = item.get("reason", "")
        lines.append(f"### {rank}️⃣ [{name}]({url})")
        lines.append(f"{desc}")
        lines.append(f"> 💡 {reason}")
        lines.append("")

    # Save alongside daily summaries
    report = "\n".join(lines)
    summary_path = storage.save_daily_summary(today, report, language="trending")
    console.print(f"\n[green]💾 Saved to: {summary_path}[/green]")

    return report


def print_trending(report: str) -> None:
    console.print(Panel(report, title="GitHub Trending", border_style="blue"))
