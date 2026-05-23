"""CLI entry point for Horizon."""

import argparse
import asyncio
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

from .storage.manager import ConfigError, StorageManager
from .orchestrator import HorizonOrchestrator


console = Console()


def print_banner():
    """Print the application banner."""
    banner = r"""
[bold blue]
  _    _            _
 | |  | |          (_)
 | |__| | ___  _ __ _ ___  ___  _ __
 |  __  |/ _ \| '__| |_  / / _ \| '_ \
 | |  | | (_) | |  | |/ / | (_) | | | |
 |_|  |_|\___/|_|  |_/___| \___/|_| |_|
[/bold blue]
[cyan]  AI-Driven Information Aggregation System[/cyan]
    """
    console.print(banner)


def main():
    """Main CLI entry point."""

    parser = argparse.ArgumentParser(description="Horizon - AI-Driven Information Aggregation System")
    parser.add_argument("--hours", type=int, help="Force fetch from last N hours")
    parser.add_argument("--trending", action="store_true", help="Enable OSS Insight trending repos in this run")
    parser.add_argument("--output", type=str, default=None, help="Output directory for reports (default: data/summaries/)")
    parser.add_argument("--quiet", action="store_true", help="Suppress banner and progress output")
    args = parser.parse_args()

    if not args.quiet:
        print_banner()

    try:
        load_dotenv()

        data_dir = Path("data")
        storage = StorageManager(data_dir=str(data_dir))

        try:
            config = storage.load_config()
        except FileNotFoundError:
            console.print("[bold red]❌ Configuration file not found![/bold red]\n")
            console.print(
                "Run [bold cyan]uv run horizon-wizard[/bold cyan] to launch the interactive setup wizard,\n"
                "or create [cyan]data/config.json[/cyan] manually based on the template:\n"
            )
            print_config_template()
            sys.exit(1)
        except ConfigError as e:
            console.print(f"[bold red]❌ Error loading configuration: {e}[/bold red]")
            sys.exit(1)
        except Exception as e:
            console.print(f"[bold red]❌ Error loading configuration: {e}[/bold red]")
            sys.exit(1)

        # Enable OSS Insight trending if --trending flag is set
        if args.trending:
            config.sources.ossinsight.enabled = True

        orchestrator = HorizonOrchestrator(config, storage, output_dir=args.output, quiet=args.quiet)
        asyncio.run(orchestrator.run(force_hours=args.hours))

    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Interrupted by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]❌ Fatal error: {e}[/bold red]")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def print_config_template():
    """Print configuration template."""
    template = """
{
  "version": "1.0",
  "ai": {
    "provider": "anthropic",
    "model": "claude-sonnet-4.5-20250929",
    "api_key_env": "ANTHROPIC_API_KEY",
    "temperature": 0.3,
    "max_tokens": 4096
  },
  "sources": {
    "github": [
      {
        "type": "user_events",
        "username": "torvalds",
        "enabled": true
      }
    ],
    "hackernews": {
      "enabled": true,
      "fetch_top_stories": 30,
      "min_score": 100
    },
    "rss": [
      {
        "name": "Example Blog",
        "url": "https://example.com/feed.xml",
        "enabled": true,
        "category": "software-engineering"
      }
    ]
  },
  "filtering": {
    "ai_score_threshold": 7.0,
    "time_window_hours": 24
  }
}

Also create a .env file with:
ANTHROPIC_API_KEY=your_api_key_here
GITHUB_TOKEN=your_github_token_here (optional but recommended)
"""
    console.print(template)


if __name__ == "__main__":
    main()
