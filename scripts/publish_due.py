#!/usr/bin/env python3
"""Interval gate for daily-summary CI.

Prints due=true/false for GitHub Actions. Schedule cadence is controlled
only by days since the latest Chinese summary (Asia/Shanghai), not by
calendar cron steps.

Exit 0 always (skip is expressed via due=false).
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
SUMMARIES = ROOT / "data" / "summaries"
DATE_RE = re.compile(r"^horizon-(\d{4}-\d{2}-\d{2})-zh\.md$")
SHANGHAI = ZoneInfo("Asia/Shanghai")
DEFAULT_MIN_GAP_DAYS = 3


def latest_zh_date() -> date | None:
    best: date | None = None
    for path in SUMMARIES.glob("horizon-*-zh.md"):
        m = DATE_RE.match(path.name)
        if not m:
            continue
        d = date.fromisoformat(m.group(1))
        if best is None or d > best:
            best = d
    return best


def is_due(today: date, latest: date | None, min_gap_days: int) -> bool:
    if latest is None:
        return True
    return (today - latest).days >= min_gap_days


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Always due=true (manual workflow_dispatch)",
    )
    parser.add_argument(
        "--min-gap-days",
        type=int,
        default=int(os.environ.get("PUBLISH_MIN_GAP_DAYS", DEFAULT_MIN_GAP_DAYS)),
    )
    parser.add_argument(
        "--today",
        help="Override today as YYYY-MM-DD (tests)",
    )
    args = parser.parse_args(argv)

    today = (
        date.fromisoformat(args.today)
        if args.today
        else datetime.now(SHANGHAI).date()
    )
    latest = latest_zh_date()
    due = True if args.force else is_due(today, latest, args.min_gap_days)

    gap = None if latest is None else (today - latest).days
    print(
        f"today={today.isoformat()} latest={latest} gap={gap} "
        f"min_gap={args.min_gap_days} force={args.force} due={str(due).lower()}"
    )

    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as f:
            f.write(f"due={str(due).lower()}\n")
    else:
        # Local / non-Actions: still emit a machine-readable last line.
        print(f"due={str(due).lower()}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"publish_due failed: {e}", file=sys.stderr)
        sys.exit(1)
