"""Page-type classification and intent x page-type compatibility.

The base clustering pipeline maps keywords to pages on text-embedding similarity
alone, with no notion of what *kind* of page each URL is. On real sites this sends
buyer-intent (commercial) keywords to whichever page has the richest body text —
typically a blog post, news article, or calculator tool — rather than the service
or landing page that should actually rank.

This module adds two things:

1. ``classify_page_type`` — label every page ``service | landing | blog | guide |
   news | tool | nav | other`` from its URL (and, optionally, title/h1).
2. ``compatibility`` — a 0..1 multiplier for an (intent, page_type) pair. Applied
   to the keyword x page similarity matrix *before* argmax, it steers commercial
   clusters toward service/landing pages and away from news/tool/nav pages, so a
   commercial cluster with no compatible page falls through to a genuine content
   gap instead of being mis-mapped to a blog.

Pure-stdlib; no third-party imports so it is safe to load anywhere in the engine.
"""

from __future__ import annotations

import re
from urllib.parse import urlparse

PAGE_TYPES = ("service", "landing", "blog", "guide", "news", "tool", "nav", "other")

# URL path-segment signals. Order matters: the first matching rule wins.
_URL_RULES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"/(services?|solutions?|products?)/[^/]+"), "service"),
    (re.compile(r"/(tools?|calculators?|checkers?|generators?)\b"), "tool"),
    (re.compile(r"/(news|press|updates?|announcements?)\b"), "news"),
    (re.compile(r"/(guides?|resources?|learn|docs?|knowledge|how-?to|tutorials?)\b"), "guide"),
    (re.compile(r"/(blog|articles?|posts?|insights?|content|library|stories)\b"), "blog"),
    (re.compile(r"/(locations?|areas?|near-me|lp|landing)\b"), "landing"),
    (
        re.compile(
            r"/(about|about-us|contact|contact-us|team|careers?|jobs?|policies|policy|privacy|terms|"
            r"sitemap|cart|checkout|account|login|signin|faq|pricing|portfolio|featured-work|"
            r"case-stud(?:y|ies)|open-source|reviews?|testimonials?)\b"
        ),
        "nav",
    ),
    (re.compile(r"/(services?|solutions?|products?)/?$"), "nav"),  # section index → hub/nav
]

# Title/h1 hints refine an ``other``/``blog`` guess. Lower-cased substring → type.
_TEXT_HINTS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\b(calculator|checker|generator|estimator|tool)\b"), "tool"),
    (re.compile(r"\b(guide|how to|tutorial|checklist|tips|best practices|explained)\b"), "guide"),
    (re.compile(r"\b(news|announce|press release|update:|launches|raises|valuation)\b"), "news"),
    (re.compile(r"\b(services?|agency|company|solutions?)\b"), "service"),
]

# Date-in-slug (e.g. /2026/06/..., /...-2026-06) is a strong news/blog-dated signal.
_DATE_SLUG = re.compile(r"/(19|20)\d{2}([/-]\d{1,2}){0,2}(/|-|$)")


def classify_page_type(url: str, title: str = "", h1: str = "", explicit: str = "") -> str:
    """Return one of :data:`PAGE_TYPES` for a page.

    An explicit, non-empty ``page_type`` (from a user-supplied CSV column) always
    wins so site owners can override the heuristics.
    """
    explicit = (explicit or "").strip().lower()
    if explicit in PAGE_TYPES:
        return explicit

    path = (urlparse(url).path or "/").lower().rstrip("/") or "/"

    # Home page.
    if path == "/":
        return "nav"

    for pattern, ptype in _URL_RULES:
        if pattern.search(path):
            return ptype

    text = f"{title} {h1}".lower()
    if _DATE_SLUG.search(path):
        return "news"
    for pattern, ptype in _TEXT_HINTS:
        if pattern.search(text):
            return ptype

    # A path with no recognised section but a single descriptive slug is most
    # often an article/landing page; treat as blog (informational) by default.
    segments = [s for s in path.split("/") if s]
    if len(segments) == 1:
        return "blog"
    return "other"


# (intent, page_type) -> multiplier in [0, 1]. Missing pairs fall back to 0.5.
# Rows: intent. Cols: page_type. Commercial/transactional/local strongly prefer
# service/landing and are nearly forbidden from news/tool/nav.
_COMPAT: dict[str, dict[str, float]] = {
    "commercial":    {"service": 1.0, "landing": 1.0, "guide": 0.45, "blog": 0.40, "nav": 0.25, "tool": 0.10, "news": 0.05, "other": 0.30},
    "transactional": {"service": 1.0, "landing": 1.0, "guide": 0.35, "blog": 0.30, "nav": 0.30, "tool": 0.15, "news": 0.05, "other": 0.30},
    "local":         {"service": 1.0, "landing": 1.0, "guide": 0.45, "blog": 0.40, "nav": 0.30, "tool": 0.10, "news": 0.05, "other": 0.30},
    "informational": {"service": 0.60, "landing": 0.55, "guide": 1.0, "blog": 1.0, "nav": 0.30, "tool": 0.55, "news": 0.70, "other": 0.50},
    "navigational":  {"service": 0.70, "landing": 0.60, "guide": 0.50, "blog": 0.45, "nav": 1.0, "tool": 0.45, "news": 0.40, "other": 0.50},
    "mixed":         {"service": 0.80, "landing": 0.75, "guide": 0.75, "blog": 0.70, "nav": 0.40, "tool": 0.40, "news": 0.40, "other": 0.50},
}

# Page types that are valid *commercial* targets (used by architecture planning to
# decide whether a commercial cluster has any acceptable existing home).
COMMERCIAL_TARGET_TYPES = frozenset({"service", "landing"})
COMMERCIAL_INTENTS = frozenset({"commercial", "transactional", "local"})


def compatibility(intent: str, page_type: str) -> float:
    """Multiplier for steering an intent toward suitable page types."""
    row = _COMPAT.get((intent or "mixed").strip().lower())
    if row is None:
        row = _COMPAT["mixed"]
    return row.get((page_type or "other").strip().lower(), 0.5)
