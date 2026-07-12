"""Schema.org structured data validator for marketing.

Extracts JSON-LD blocks from a URL or local HTML file and validates them
against a lookup of common schema.org types. Reports required and recommended
field coverage plus any detected errors.

Supported types: Article, Product, FAQPage, HowTo, LocalBusiness, Recipe,
Event, Organization, Person, BreadcrumbList.

Emitted JSON::

    {
      "url": "https://example.com.au/page/",
      "schemas_found": 2,
      "results": [
        {
          "@type": "Article",
          "status": "valid",
          "score": 0.85,
          "missing_required": [],
          "missing_recommended": ["author", "dateModified"],
          "errors": []
        },
        ...
      ]
    }

Usage::

    python schema_validator.py https://example.com.au/page/
    python schema_validator.py /path/to/local.html
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import httpx
from selectolax.parser import HTMLParser

_USER_AGENT = "marketing-schema-validator/1.0"

# Schema.org type definitions: {type: {required: [...], recommended: [...]}}
_SCHEMA_RULES: dict[str, dict[str, list[str]]] = {
    "Article": {
        "required": ["headline", "datePublished", "image"],
        "recommended": ["author", "dateModified", "description", "publisher"],
    },
    "Product": {
        "required": ["name"],
        "recommended": ["image", "description", "brand", "offers", "aggregateRating", "sku"],
    },
    "FAQPage": {
        "required": ["mainEntity"],
        "recommended": [],
    },
    "HowTo": {
        "required": ["name", "step"],
        "recommended": ["description", "totalTime", "estimatedCost", "image"],
    },
    "LocalBusiness": {
        "required": ["name", "address"],
        "recommended": [
            "telephone", "openingHours", "geo", "url", "image",
            "priceRange", "aggregateRating",
        ],
    },
    "Recipe": {
        "required": ["name", "image", "recipeIngredient", "recipeInstructions"],
        "recommended": [
            "author", "datePublished", "description", "prepTime",
            "cookTime", "totalTime", "recipeYield", "nutrition",
        ],
    },
    "Event": {
        "required": ["name", "startDate", "location"],
        "recommended": ["endDate", "description", "image", "offers", "organizer", "url"],
    },
    "Organization": {
        "required": ["name"],
        "recommended": ["url", "logo", "contactPoint", "sameAs", "address"],
    },
    "Person": {
        "required": ["name"],
        "recommended": ["url", "image", "jobTitle", "worksFor", "sameAs"],
    },
    "BreadcrumbList": {
        "required": ["itemListElement"],
        "recommended": [],
    },
}


def _fetch_html(source: str) -> str:
    """Return HTML from a URL or local file path."""
    if source.startswith("http://") or source.startswith("https://"):
        with httpx.Client(
            timeout=30.0, headers={"User-Agent": _USER_AGENT}, follow_redirects=True
        ) as client:
            response = client.get(source)
            response.raise_for_status()
        return response.text
    else:
        return Path(source).read_text(encoding="utf-8", errors="replace")


def _extract_json_ld(html: str) -> list[dict[str, Any]]:
    """Extract and parse all JSON-LD blocks from *html*."""
    tree = HTMLParser(html)
    schemas: list[dict[str, Any]] = []
    for script in tree.css('script[type="application/ld+json"]'):
        text = script.text(strip=True)
        if not text:
            continue
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            continue
        # Handle both single objects and @graph arrays
        if isinstance(data, list):
            schemas.extend(data)
        elif isinstance(data, dict):
            graph = data.get("@graph")
            if isinstance(graph, list):
                schemas.extend(graph)
            else:
                schemas.append(data)
    return schemas


def _validate_schema(schema: dict[str, Any]) -> dict[str, Any]:
    """Validate a single JSON-LD schema object.

    Returns:
        Validation result dict with ``@type``, ``status``, ``score``,
        ``missing_required``, ``missing_recommended``, and ``errors``.
    """
    schema_type = schema.get("@type", "Unknown")
    # Handle arrays of types — use the first known type
    if isinstance(schema_type, list):
        known = [t for t in schema_type if t in _SCHEMA_RULES]
        schema_type = known[0] if known else schema_type[0]

    rules = _SCHEMA_RULES.get(schema_type)
    if not rules:
        return {
            "@type": schema_type,
            "status": "unknown_type",
            "score": None,
            "missing_required": [],
            "missing_recommended": [],
            "errors": [f"No validation rules for type '{schema_type}'"],
        }

    missing_required = [f for f in rules["required"] if f not in schema]
    missing_recommended = [f for f in rules["recommended"] if f not in schema]
    errors: list[str] = []

    if missing_required:
        errors.append(f"Missing required fields: {', '.join(missing_required)}")

    total_fields = len(rules["required"]) + len(rules["recommended"])
    present = total_fields - len(missing_required) - len(missing_recommended)
    score = round(present / total_fields, 2) if total_fields > 0 else 1.0

    status = "valid" if not missing_required else "invalid"

    return {
        "@type": schema_type,
        "status": status,
        "score": score,
        "missing_required": missing_required,
        "missing_recommended": missing_recommended,
        "errors": errors,
    }


def validate(source: str) -> dict[str, Any]:
    """Extract and validate all JSON-LD schemas from *source*.

    Args:
        source: A URL or local file path.

    Returns:
        Report dict with ``url``, ``schemas_found``, and ``results``.
    """
    html = _fetch_html(source)
    schemas = _extract_json_ld(html)
    results = [_validate_schema(s) for s in schemas]
    return {
        "url": source,
        "schemas_found": len(schemas),
        "results": results,
    }


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: schema_validator.py <url_or_file>", file=sys.stderr)
        sys.exit(1)

    source = sys.argv[1]
    try:
        report = validate(source)
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"error": str(exc)}))
        sys.exit(1)

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
