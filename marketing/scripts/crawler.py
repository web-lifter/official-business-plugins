"""Lightweight async web crawler for marketing.

Crawls a website starting from *start_url*, respects ``robots.txt``, and emits
NDJSON to stdout — one record per page. Intended for use by ``on-page-audit``,
``technical-seo-audit``, ``internal-linking-planner``, and
``broken-link-scanner`` skills.

Each emitted record::

    {
      "url": "https://example.com.au/page/",
      "status": 200,
      "title": "Page Title",
      "meta_description": "...",
      "h1": "Main Heading",
      "internal_links": ["https://example.com.au/other/", ...],
      "external_links": ["https://partner.com/", ...],
      "content_length": 42314,
      "canonical": "https://example.com.au/page/",
      "noindex": false,
      "error": null
    }

Usage::

    python crawler.py https://example.com.au
    python crawler.py https://example.com.au --max-pages 200 --same-host
    python crawler.py https://example.com.au --max-pages 50 > pages.ndjson
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from collections import deque
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser

import httpx
from selectolax.parser import HTMLParser


_USER_AGENT = "marketing-crawler/1.0 (+https://github.com/web-lifter/official-claude-plugins)"
_CONCURRENCY = 5


def _parse_robots(base_url: str) -> RobotFileParser:
    """Fetch and parse robots.txt for *base_url*."""
    robots_url = urljoin(base_url, "/robots.txt")
    rp = RobotFileParser(robots_url)
    try:
        rp.read()
    except Exception:  # noqa: BLE001
        pass  # If robots.txt is unreachable, allow everything
    return rp


def _extract_text(node) -> str:
    """Return stripped inner text of a selectolax node, or empty string."""
    if node is None:
        return ""
    return node.text(strip=True) or ""


def _extract_links(
    tree: HTMLParser, base_url: str, same_host: bool, host: str
) -> tuple[list[str], list[str]]:
    """Return (internal_links, external_links) for all <a href> elements."""
    internal: list[str] = []
    external: list[str] = []
    for node in tree.css("a[href]"):
        href = node.attributes.get("href", "")
        if not href or href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
            continue
        full_url = urljoin(base_url, href)
        parsed = urlparse(full_url)
        # Strip fragment
        clean = parsed._replace(fragment="").geturl()
        if parsed.netloc == host:
            internal.append(clean)
        else:
            if not same_host:
                external.append(clean)
    return internal, external


async def crawl(
    start_url: str,
    max_pages: int = 100,
    same_host: bool = True,
) -> None:
    """Crawl *start_url* and emit NDJSON records to stdout.

    Args:
        start_url: The URL to begin crawling from.
        max_pages: Maximum number of pages to crawl.
        same_host: If True, only follow links on the same hostname.
    """
    parsed_start = urlparse(start_url)
    host = parsed_start.netloc
    base_url = f"{parsed_start.scheme}://{host}"

    robots = _parse_robots(base_url)
    visited: set[str] = set()
    queue: deque[str] = deque([start_url])
    sem = asyncio.Semaphore(_CONCURRENCY)

    async def fetch_page(client: httpx.AsyncClient, url: str) -> None:
        if not robots.can_fetch(_USER_AGENT, url):
            record = {
                "url": url, "status": None, "title": None, "meta_description": None,
                "h1": None, "internal_links": [], "external_links": [],
                "content_length": 0, "canonical": None, "noindex": False,
                "error": "disallowed by robots.txt",
            }
            print(json.dumps(record), flush=True)
            return

        async with sem:
            try:
                response = await client.get(url, follow_redirects=True)
                final_url = str(response.url)
                content = response.text
                status = response.status_code
            except Exception as exc:  # noqa: BLE001
                record = {
                    "url": url, "status": None, "title": None, "meta_description": None,
                    "h1": None, "internal_links": [], "external_links": [],
                    "content_length": 0, "canonical": None, "noindex": False,
                    "error": str(exc),
                }
                print(json.dumps(record), flush=True)
                return

        tree = HTMLParser(content)

        title_node = tree.css_first("title")
        title = _extract_text(title_node)

        meta_desc_node = tree.css_first('meta[name="description"]')
        meta_desc = (meta_desc_node.attributes.get("content", "") or "") if meta_desc_node else ""

        h1_node = tree.css_first("h1")
        h1 = _extract_text(h1_node)

        canonical_node = tree.css_first('link[rel="canonical"]')
        canonical = (canonical_node.attributes.get("href", "") or "") if canonical_node else ""

        robots_meta = tree.css_first('meta[name="robots"]')
        noindex = False
        if robots_meta:
            content_attr = robots_meta.attributes.get("content", "").lower()
            noindex = "noindex" in content_attr

        internal_links, external_links = _extract_links(tree, final_url, same_host, host)

        # Enqueue unvisited internal links
        for link in internal_links:
            if link not in visited and len(visited) + len(queue) < max_pages:
                queue.append(link)

        record = {
            "url": final_url,
            "status": status,
            "title": title,
            "meta_description": meta_desc,
            "h1": h1,
            "internal_links": list(set(internal_links)),
            "external_links": list(set(external_links)),
            "content_length": len(content),
            "canonical": canonical or None,
            "noindex": noindex,
            "error": None,
        }
        print(json.dumps(record), flush=True)

    async with httpx.AsyncClient(
        headers={"User-Agent": _USER_AGENT},
        timeout=30.0,
        limits=httpx.Limits(max_connections=_CONCURRENCY),
    ) as client:
        while queue and len(visited) < max_pages:
            url = queue.popleft()
            if url in visited:
                continue
            visited.add(url)
            await fetch_page(client, url)


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Crawl a website and emit NDJSON")
    parser.add_argument("start_url", help="URL to begin crawling from")
    parser.add_argument(
        "--max-pages", type=int, default=100, help="Maximum pages to crawl (default: 100)"
    )
    parser.add_argument(
        "--same-host",
        action="store_true",
        default=True,
        help="Only follow links on the same hostname (default: true)",
    )
    args = parser.parse_args()
    asyncio.run(crawl(args.start_url, max_pages=args.max_pages, same_host=args.same_host))


if __name__ == "__main__":
    main()
