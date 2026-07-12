"""robots.txt parser for marketing.

Fetches a robots.txt file and emits a structured JSON summary including
crawl rules per user-agent and the list of declared sitemaps.

Output JSON::

    {
      "url": "https://example.com.au/robots.txt",
      "user_agents": {
        "*": {"disallow": ["/admin/", "/private/"], "allow": [], "crawl_delay": null},
        "Googlebot": {"disallow": [], "allow": ["/"], "crawl_delay": null}
      },
      "sitemaps": ["https://example.com.au/sitemap.xml"]
    }

Usage::

    python robots_parser.py https://example.com.au/robots.txt
    python robots_parser.py https://example.com.au  # will append /robots.txt
"""

from __future__ import annotations

import json
import sys
from urllib.parse import urljoin, urlparse

import httpx

_USER_AGENT = "marketing-robots-parser/1.0"


def parse_robots(url: str) -> dict:
    """Fetch and parse *url* as a robots.txt file.

    If *url* does not end with ``/robots.txt``, ``/robots.txt`` is appended
    to the scheme+host portion of the URL.

    Args:
        url: URL of the robots.txt file or the site root.

    Returns:
        Dict with ``url``, ``user_agents``, and ``sitemaps`` keys.
    """
    # Normalise URL
    parsed = urlparse(url)
    if not parsed.path.endswith("robots.txt"):
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    else:
        robots_url = url

    with httpx.Client(
        timeout=15.0, headers={"User-Agent": _USER_AGENT}, follow_redirects=True
    ) as client:
        response = client.get(robots_url)
        response.raise_for_status()
        text = response.text

    user_agents: dict[str, dict] = {}
    sitemaps: list[str] = []
    current_agents: list[str] = []

    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        if ":" not in line:
            continue

        directive, _, value = line.partition(":")
        directive = directive.strip().lower()
        value = value.strip()

        if directive == "user-agent":
            current_agents = [value] if value else []
            for agent in current_agents:
                if agent not in user_agents:
                    user_agents[agent] = {"disallow": [], "allow": [], "crawl_delay": None}
        elif directive == "disallow":
            for agent in current_agents:
                if agent in user_agents and value:
                    user_agents[agent]["disallow"].append(value)
        elif directive == "allow":
            for agent in current_agents:
                if agent in user_agents and value:
                    user_agents[agent]["allow"].append(value)
        elif directive == "crawl-delay":
            try:
                delay = float(value)
            except ValueError:
                delay = None
            for agent in current_agents:
                if agent in user_agents:
                    user_agents[agent]["crawl_delay"] = delay
        elif directive == "sitemap":
            if value:
                sitemaps.append(value)

    return {
        "url": robots_url,
        "user_agents": user_agents,
        "sitemaps": sitemaps,
    }


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: robots_parser.py <robots_url_or_site_root>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    try:
        result = parse_robots(url)
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"error": str(exc)}))
        sys.exit(1)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
