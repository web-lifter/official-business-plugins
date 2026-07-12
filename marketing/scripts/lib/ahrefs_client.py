"""Ahrefs API client for marketing (stub).

Provides backlink intelligence via the Ahrefs API v3. Credentials are read
from the encrypted vault under provider ``ahrefs``, key ``api_key``.

Note: Ahrefs API access requires an Ahrefs Enterprise plan. This module is
a functional stub — the endpoint paths and response shapes match the
Ahrefs v3 API documentation; authentication and transport are real.

Usage::

    from scripts.lib.ahrefs_client import referring_domains, backlinks

    domains = referring_domains("https://example.com.au")
    links = backlinks("https://example.com.au", mode="recent")
"""

from __future__ import annotations

from typing import Any

import httpx

from .credentials import canonical_path, get_credential

_AHREFS_BASE = "https://api.ahrefs.com/v3"


def _get_api_key() -> str:
    """Read the Ahrefs API key from the credentials file or env var."""
    key = get_credential("ahrefs", "api_key", env_var="AHREFS_API_KEY")
    if not key:
        raise RuntimeError(
            f"Ahrefs API key not found. Add it to {canonical_path()} as "
            '{"ahrefs": {"api_key": "YOUR_KEY"}} (or set the AHREFS_API_KEY env var).'
        )
    return key


def _get(endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
    """Authenticated GET against the Ahrefs v3 API."""
    api_key = _get_api_key()
    with httpx.Client(timeout=30.0) as client:
        response = client.get(
            f"{_AHREFS_BASE}/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        response.raise_for_status()
    return response.json()


def referring_domains(target: str, limit: int = 100) -> list[dict[str, Any]]:
    """Return referring domains for *target* URL or domain.

    Args:
        target: The target URL or domain (e.g. ``"example.com.au"``).
        limit:  Maximum number of referring domains to return.

    Returns:
        List of dicts with ``domain``, ``domain_rating``, ``backlinks_count``,
        ``linked_domains_count``, and ``first_seen`` fields.
    """
    data = _get(
        "site-explorer/referring-domains",
        {"target": target, "limit": limit, "select": "domain,domain_rating,backlinks,linked_domains,first_seen"},
    )
    return data.get("referring_domains", [])


def backlinks(target: str, mode: str = "recent", limit: int = 100) -> list[dict[str, Any]]:
    """Return backlinks for *target*.

    Args:
        target: The target URL or domain.
        mode:   ``"recent"`` for newest links, ``"best"`` for highest DR links.
        limit:  Maximum number of backlinks to return.

    Returns:
        List of dicts with ``url_from``, ``url_to``, ``anchor``,
        ``domain_rating_source``, ``url_rating_source``, and ``first_seen`` fields.
    """
    order_by = "first_seen:desc" if mode == "recent" else "domain_rating_source:desc"
    data = _get(
        "site-explorer/backlinks",
        {
            "target": target,
            "limit": limit,
            "order_by": order_by,
            "select": "url_from,url_to,anchor,domain_rating_source,url_rating_source,first_seen",
        },
    )
    return data.get("backlinks", [])
