"""DataForSEO client for marketing.

Provides keyword suggestions and search volume lookups via the DataForSEO
Keywords Data API. Credentials (login + password) are read from the plaintext credentials file or environment under provider ``dataforseo``.

Location code 2036 = Australia.

Usage::

    from scripts.lib.dataforseo_client import keyword_suggestions, keyword_volume

    suggestions = keyword_suggestions("accounting software", location_code=2036)
    volumes = keyword_volume(["accounting software", "bookkeeping app"], location_code=2036)
"""

from __future__ import annotations

import base64
from typing import Any

import httpx

from .credentials import canonical_path, get_credential

_DFS_BASE = "https://api.dataforseo.com/v3"


def _get_auth_header() -> str:
    """Return Basic Auth header value derived from the credentials file."""
    login = get_credential("dataforseo", "login", env_var="DATAFORSEO_LOGIN") or ""
    password = get_credential("dataforseo", "password", env_var="DATAFORSEO_PASSWORD") or ""
    if not login or not password:
        raise RuntimeError(
            f"DataForSEO credentials not found. Add them to {canonical_path()} as "
            '{"dataforseo": {"login": "...", "password": "..."}} '
            "(or set DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD env vars)."
        )
    token = base64.b64encode(f"{login}:{password}".encode()).decode()
    return f"Basic {token}"


def _post(endpoint: str, payload: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """POST *payload* to DataForSEO *endpoint*, returning the ``tasks`` list."""
    auth = _get_auth_header()
    with httpx.Client(timeout=60.0) as client:
        response = client.post(
            f"{_DFS_BASE}/{endpoint}",
            json=payload,
            headers={"Authorization": auth, "Content-Type": "application/json"},
        )
        response.raise_for_status()
    body: dict[str, Any] = response.json()
    if not isinstance(body, dict) or body.get("status_code") != 20000:
        raise RuntimeError("DataForSEO request failed; check status code and account configuration")
    tasks = body.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        raise RuntimeError("DataForSEO returned no task results")
    for task in tasks:
        if not isinstance(task, dict) or task.get("status_code") != 20000:
            raise RuntimeError("DataForSEO task failed; do not treat this as zero search volume")
        if task.get("result") is not None and not isinstance(task["result"], list):
            raise RuntimeError("DataForSEO returned an unexpected result shape")
    return tasks


def keyword_suggestions(
    seed: str,
    location_code: int = 2036,
    language_code: str = "en",
    limit: int = 100,
) -> list[dict[str, Any]]:
    """Return keyword suggestions related to *seed*.

    Args:
        seed:          Seed keyword to expand.
        location_code: DataForSEO location code (2036 = Australia).
        language_code: Language code (default: ``"en"``).
        limit:         Maximum number of suggestions to return.

    Returns:
        List of keyword dicts with ``keyword``, ``search_volume``,
        ``competition``, ``cpc`` fields where returned by the API.
    """
    if not isinstance(seed, str) or not seed.strip() or isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise ValueError("seed must be non-empty and limit a positive integer")
    payload = [
        {
            "keywords": [seed],
            "location_code": location_code,
            "language_code": language_code,
        }
    ]
    tasks = _post("keywords_data/google_ads/keywords_for_keywords/live", payload)
    results: list[dict[str, Any]] = []
    for task in tasks:
        results.extend(task.get("result") or [])
    return results[:limit]


def keyword_volume(
    keywords: list[str],
    location_code: int = 2036,
    language_code: str = "en",
) -> list[dict[str, Any]]:
    """Return search volume data for a list of exact keywords.

    Args:
        keywords:      List of keywords to look up (max 700 per call).
        location_code: DataForSEO location code (2036 = Australia).
        language_code: Language code (default: ``"en"``).

    Returns:
        List of dicts with ``keyword``, ``search_volume``, ``competition``,
        ``cpc`` fields where returned by the API.
    """
    if not keywords:
        return []
    if len(keywords) > 700 or any(not isinstance(k, str) or not k.strip() for k in keywords):
        raise ValueError("provide 1-700 non-empty keywords (the local client batch limit)")
    payload = [
        {
            "keywords": keywords,
            "location_code": location_code,
            "language_code": language_code,
        }
    ]
    tasks = _post("keywords_data/google_ads/search_volume/live", payload)
    results: list[dict[str, Any]] = []
    for task in tasks:
        results.extend(task.get("result") or [])
    return results
