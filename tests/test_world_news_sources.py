"""Tests for multi-entry GDELT / Google News source config."""

from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from io import StringIO
from types import SimpleNamespace
from unittest.mock import AsyncMock

from rich.console import Console

from src.models import (
    Config,
    GDELTConfig,
    GoogleNewsConfig,
    SourcesConfig,
)
from src.orchestrator import HorizonOrchestrator
from src.processing.profiles import ProfileRegistry


def test_world_news_profile_loads() -> None:
    registry = ProfileRegistry.load(
        __import__("pathlib").Path("profiles"), "tech-news"
    )
    assert "world-news" in registry.ids
    profile = registry.get("world-news")
    assert "geopolitics" in profile.match_prompt.lower() or "public affairs" in profile.match_prompt.lower()
    assert "9-10" in profile.analysis_prompt


def test_gdelt_google_news_accept_list_and_legacy_object() -> None:
    as_list = SourcesConfig.model_validate(
        {
            "gdelt": [
                {"enabled": True, "query": "a", "profile": "world-news"},
                {"enabled": False, "query": "b", "profile": "world-news"},
            ],
            "google_news": [
                {"enabled": True, "query": "c", "profile": "world-news"},
            ],
        }
    )
    assert len(as_list.gdelt) == 2
    assert len(as_list.google_news) == 1

    legacy = SourcesConfig.model_validate(
        {
            "gdelt": {"enabled": True, "query": "legacy", "profile": "world-news"},
            "google_news": {
                "enabled": True,
                "query": "legacy-gn",
                "profile": "world-news",
            },
        }
    )
    assert len(legacy.gdelt) == 1
    assert legacy.gdelt[0].query == "legacy"
    assert len(legacy.google_news) == 1


def test_fetch_schedules_enabled_news_list_entries(monkeypatch) -> None:
    orchestrator = object.__new__(HorizonOrchestrator)
    orchestrator.console = Console(file=StringIO())
    orchestrator.last_fetch_report = None
    orchestrator.config = SimpleNamespace(  # type: ignore[assignment]
        sources=SimpleNamespace(
            github=[],
            hackernews=SimpleNamespace(enabled=False),
            rss=[],
            reddit=SimpleNamespace(enabled=False),
            telegram=SimpleNamespace(enabled=False),
            twitter=None,
            openbb=None,
            ossinsight=SimpleNamespace(enabled=False),
            gdelt=[
                GDELTConfig(enabled=True, query="geo-a", profile="world-news"),
                GDELTConfig(enabled=False, query="geo-b", profile="world-news"),
            ],
            google_news=[
                GoogleNewsConfig(
                    enabled=True, query="gn-a", profile="world-news"
                ),
                GoogleNewsConfig(
                    enabled=True, query="gn-b", profile="world-news"
                ),
            ],
        ),
        extractors={},
    )

    created: list[str] = []

    class StubScraper:
        def __init__(self, config, client):  # type: ignore[no-untyped-def]
            query = getattr(config, "query", "?")
            created.append(query)

        async def fetch(self, since):  # type: ignore[no-untyped-def]
            return []

    monkeypatch.setattr("src.orchestrator.GDELTScraper", StubScraper)
    monkeypatch.setattr("src.orchestrator.GoogleNewsScraper", StubScraper)

    since = datetime(2026, 1, 1, tzinfo=timezone.utc)
    asyncio.run(orchestrator.fetch_all_sources(since))

    assert created == ["geo-a", "gn-a", "gn-b"]


def test_example_config_includes_world_news() -> None:
    from pathlib import Path

    raw = Path("data/config.example.json").read_text(encoding="utf-8")
    # Expand trivial env placeholders if any — example uses ${LWN_KEY} in one disabled feed
    import os
    import re

    expanded = re.sub(
        r"\$\{([A-Z0-9_]+)\}",
        lambda m: os.environ.get(m.group(1), "placeholder"),
        raw,
    )
    cfg = Config.model_validate_json(expanded)
    assert "world-news" in cfg.processing.profile_settings
    assert "world-news" in cfg.digest.profile_order
    assert any(r.profile == "world-news" for r in cfg.sources.rss)
    assert len(cfg.sources.gdelt) >= 1
    assert len(cfg.sources.google_news) >= 2
    ProfileRegistry.load(
        Path(cfg.processing.profiles_dir), cfg.processing.default_profile
    ).validate_source_references(cfg.sources.model_dump())
