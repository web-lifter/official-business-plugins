"""Simple filesystem-backed HTTP GET cache for marketing scripts.

Caches JSON responses from GET requests to ``${CLAUDE_PLUGIN_DATA}/cache/``
keyed by a SHA-256 hash of the URL and parameters. Default TTL is 24 hours.

This prevents hammering paid APIs (SerpAPI, DataForSEO) when the same query
is made multiple times within a session or across sessions on the same day.

Usage::

    from scripts.lib.http_cache import cached_get

    data = cached_get(
        "https://serpapi.com/search",
        params={"q": "keyword research tools", "api_key": "..."},
        ttl_hours=24,
    )
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path
from typing import Any

import httpx


def _cache_dir() -> Path:
    """Return the cache directory, creating it if needed."""
    data_dir = os.environ.get(
        "CLAUDE_PLUGIN_DATA",
        os.path.join(os.path.expanduser("~"), ".claude", "plugins", "data", "marketing"),
    )
    cache = Path(data_dir) / "cache"
    cache.mkdir(parents=True, exist_ok=True)
    return cache


def _cache_key(url: str, params: dict[str, Any] | None) -> str:
    """Return the SHA-256 hex digest of *url* + sorted *params* as the cache key."""
    canonical = url
    if params:
        sorted_params = "&".join(f"{k}={v}" for k, v in sorted(params.items()))
        canonical = f"{url}?{sorted_params}"
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def cached_get(
    url: str,
    params: dict[str, Any] | None = None,
    ttl_hours: float = 24,
    headers: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Perform a GET request, returning a cached response if available and fresh.

    Args:
        url:       The full URL to fetch.
        params:    Query parameters as a dict.
        ttl_hours: Cache TTL in hours. Set to 0 to bypass the cache.
        headers:   Optional request headers (e.g. ``Authorization``).

    Returns:
        Parsed JSON response as a dict.

    Raises:
        httpx.HTTPStatusError: On non-2xx responses.
        json.JSONDecodeError:  If the response body is not valid JSON.
    """
    cache_path: Path | None = None
    ttl_seconds = ttl_hours * 3600

    if ttl_hours > 0:
        key = _cache_key(url, params)
        cache_path = _cache_dir() / f"{key}.json"

        if cache_path.exists():
            mtime = cache_path.stat().st_mtime
            if time.time() - mtime < ttl_seconds:
                return json.loads(cache_path.read_text(encoding="utf-8"))

    # Cache miss or bypass — make the real request
    with httpx.Client(timeout=30.0) as client:
        response = client.get(url, params=params, headers=headers)
        response.raise_for_status()
        data: dict[str, Any] = response.json()

    if cache_path is not None:
        cache_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    return data
