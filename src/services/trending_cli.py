"""CLI entry point for GitHub trending report."""

import asyncio
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

from .trending import run_trending, print_trending, DEFAULT_KEYWORDS, DEFAULT_LANGUAGES

console = Console()


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="GitHub trending repos report — AI-powered daily summary"
    )
    parser.add_argument(
        "--keywords", nargs="*", default=None,
        help="Filter keywords (space-separated). Default: AI-related keywords.",
    )
    parser.add_argument(
        "--languages", nargs="*", default=None,
        help="Programming languages to track. Default: All Python TypeScript Rust.",
    )
    parser.add_argument(
        "--max-repos", type=int, default=15,
        help="Max repos to send to AI (default: 15).",
    )
    parser.add_argument(
        "--print", action="store_true", dest="print_only",
        help="Print to console only, don't save.",
    )
    args = parser.parse_args()

    try:
        load_dotenv(Path(__file__).parent.parent.parent / ".env")
        report = asyncio.run(
            run_trending(
                data_dir="data",
                keywords=args.keywords,
                languages=args.languages,
                max_repos=args.max_repos,
            )
        )
        if args.print_only:
            print(report)
        else:
            print_trending(report)
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
