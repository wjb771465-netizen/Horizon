"""Tests for digest_mail summary parsers."""

from __future__ import annotations

from pathlib import Path

from scripts.digest_mail import extract_zh_items


def test_extract_zh_items_profile_heading_format(tmp_path: Path) -> None:
    path = tmp_path / "horizon-2026-08-02-zh.md"
    path.write_text(
        """# Horizon 每日速递 - 2026-08-02

**科技新闻**
1. [TOC only](#item-tech-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [KataGo 研究](https://example.com/a) ⭐️ 8.0/10

这是正文第一段，应进入简报摘要。

rss · Simon Willison · 8月1日 20:34

**「背景」** 不应进入 blurb。

---

### [第二条](https://example.com/b) ⭐️ 7.0/10

第二条正文。
""",
        encoding="utf-8",
    )

    items = extract_zh_items(path, limit=6)
    assert len(items) == 2
    assert items[0]["title"] == "KataGo 研究"
    assert items[0]["url"] == "https://example.com/a"
    assert "正文第一段" in items[0]["blurb"]
    assert "背景" not in items[0]["blurb"]
    assert items[1]["title"] == "第二条"


def test_extract_zh_items_legacy_double_hash(tmp_path: Path) -> None:
    path = tmp_path / "horizon-2026-08-01-zh.md"
    path.write_text(
        """# old

## [旧格式标题](https://example.com/old) ⭐️ 9.0/10

旧正文一段。

rss · Author · Aug 1, 20:34

**背景**: 旧背景
""",
        encoding="utf-8",
    )
    items = extract_zh_items(path)
    assert len(items) == 1
    assert items[0]["title"] == "旧格式标题"
    assert "旧正文" in items[0]["blurb"]
