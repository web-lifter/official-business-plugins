"""SerpAPI client for marketing.

Provides a thin wrapper around the SerpAPI Google Search endpoint, with
results cached via ``http_cache.cached_get``.

Credentials are read from the plaintext credentials file under provider
``serpapi``, key ``api_key`` (or the ``SERPAPI_KEY`` environment variable).

Usage::

    from scripts.lib.serpapi_client import search

    results = search("best accounting software Australia", location="Australia", num=10)
    organic = results.get("organic_results", [])
"""

from __future__ import annotations

from typing import Any

from .credentials import canonical_path, get_credential
from .http_cache import cached_get

_SERPAPI_ENDPOINT = "https://serpapi.com/search"


def _get_api_key() -> str:
    """Read the SerpAPI key from the credentials file or env var."""
    key = get_credential("serpapi", "api_key", env_var="SERPAPI_KEY")
    if key:
        return key
    raise RuntimeError(
        f"SerpAPI key not found. Add it to {canonical_path()} as "
        '{"serpapi": {"api_key": "YOUR_KEY"}} (or set the SERPAPI_KEY env var).'
    )


def search(
    query: str,
    location: str = "Australia",
    num: int = 10,
    gl: str = "au",
    hl: str = "en",
    ttl_hours: float = 24,
) -> dict[str, Any]:
    """Execute a Google search via SerpAPI.

    Args:
        query:     The search query string.
        location:  Target location for localised results.
        num:       Number of organic results to request (max 100).
        gl:        Country code for Google (default: ``"au"``).
        hl:        Language code for Google (default: ``"en"``).
        ttl_hours: Cache TTL for results. Use 0 to bypass cache.

    Returns:
        Full SerpAPI response dict including ``organic_results``,
        ``answer_box``, ``related_questions``, ``knowledge_graph``, etc.
    """
    api_key = _get_api_key()
    params: dict[str, Any] = {
        "engine": "google",
        "q": query,
        "location": location,
        "num": num,
        "gl": gl,
        "hl": hl,
        "api_key": api_key,
    }
    return cached_get(_SERPAPI_ENDPOINT, params=params, ttl_hours=ttl_hours)
