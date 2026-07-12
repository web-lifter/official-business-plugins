"""Sitemap parser for marketing.

Recursively fetches sitemap index files and sitemaps, emitting one NDJSON
record per URL to stdout. Handles both ``<sitemapindex>`` and ``<urlset>``
document types.

Emitted record::

    {"url": "https://example.com.au/page/", "lastmod": "2026-05-01", "priority": "0.8"}

Usage::

    python sitemap_parser.py https://example.com.au/sitemap.xml
    python sitemap_parser.py https://example.com.au/sitemap_index.xml > urls.ndjson
"""

from __future__ import annotations

import json
import sys
from typing import Iterator
from xml.etree import ElementTree

import httpx

_NS_SITEMAP = "http://www.sitemaps.org/schemas/sitemap/0.9"
_USER_AGENT = "marketing-sitemap-parser/1.0"


def _fetch_xml(url: str) -> ElementTree.Element:
    """Fetch *url* and return the parsed XML root element."""
    with httpx.Client(
        timeout=30.0, headers={"User-Agent": _USER_AGENT}, follow_redirects=True
    ) as client:
        response = client.get(url)
        response.raise_for_status()
    return ElementTree.fromstring(response.text)


def _tag(local: str) -> str:
    """Return a namespace-qualified tag name."""
    return f"{{{_NS_SITEMAP}}}{local}"


def parse_sitemap(url: str, _visited: set[str] | None = None) -> Iterator[dict]:
    """Recursively parse a sitemap or sitemap index at *url*.

    Args:
        url:      The sitemap URL to fetch and parse.
        _visited: Internal set to prevent infinite loops in sitemap indexes.

    Yields:
        Dicts with ``url``, ``lastmod`` (may be empty string), and
        ``priority`` (may be empty string) keys.
    """
    if _visited is None:
        _visited = set()
    if url in _visited:
        return
    _visited.add(url)

    try:
        root = _fetch_xml(url)
    except Exception as exc:  # noqa: BLE001
        # Emit an error record and continue
        yield {"url": url, "error": str(exc), "lastmod": "", "priority": ""}
        return

    # Sitemap index — recurse into each child sitemap
    if root.tag == _tag("sitemapindex"):
        for sitemap_el in root.findall(_tag("sitemap")):
            loc = sitemap_el.findtext(_tag("loc"), "").strip()
            if loc:
                yield from parse_sitemap(loc, _visited=_visited)
        return

    # Regular urlset
    for url_el in root.findall(_tag("url")):
        loc = url_el.findtext(_tag("loc"), "").strip()
        if not loc:
            continue
        lastmod = url_el.findtext(_tag("lastmod"), "").strip()
        priority = url_el.findtext(_tag("priority"), "").strip()
        yield {"url": loc, "lastmod": lastmod, "priority": priority}


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: sitemap_parser.py <sitemap_url>", file=sys.stderr)
        sys.exit(1)

    sitemap_url = sys.argv[1]
    for record in parse_sitemap(sitemap_url):
        print(json.dumps(record), flush=True)


if __name__ == "__main__":
    main()
