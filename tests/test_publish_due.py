"""Tests for scripts/publish_due.py interval gate."""

from datetime import date
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from publish_due import is_due  # noqa: E402


def test_due_when_no_summary() -> None:
    assert is_due(date(2026, 8, 2), None, 3) is True


def test_skip_when_gap_below_min() -> None:
    today = date(2026, 8, 2)
    assert is_due(today, date(2026, 8, 1), 3) is False  # gap 1
    assert is_due(today, date(2026, 7, 31), 3) is False  # gap 2
    assert is_due(today, date(2026, 8, 2), 3) is False  # gap 0


def test_due_when_gap_reaches_min() -> None:
    today = date(2026, 8, 4)
    assert is_due(today, date(2026, 8, 1), 3) is True  # gap 3
    assert is_due(today, date(2026, 7, 31), 3) is True  # gap 4
