#!/usr/bin/env python3
"""Enrich a pages CSV with title/meta/h1/headings/body excerpt for sharper mapping.

Wraps the vendored engine's ``enrich_pages_dataframe`` so the skill never calls an
external CLI. Input needs only a ``url`` column; ``page_name`` is preserved if
present (the clustering run requires ``url,page_name``).

    python crawl_pages.py --pages pages.csv --output pages-enriched.csv [--timeout 20]
"""

from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import pandas as pd  # noqa: E402

from keyword_clustering.integrations import enrich_pages_dataframe  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description="Crawl/enrich a pages CSV (title, meta, h1, headings, body excerpt).")
    ap.add_argument("--pages", required=True, help="Pages CSV with at least a 'url' column.")
    ap.add_argument("--output", default="pages-enriched.csv")
    ap.add_argument("--timeout", type=int, default=20)
    args = ap.parse_args()

    pages = pd.read_csv(args.pages)
    enriched = enrich_pages_dataframe(pages, timeout=args.timeout)
    # Keep page_name (derive from URL slug if the source lacked it).
    if "page_name" not in enriched.columns:
        enriched["page_name"] = (
            enriched["url"].astype(str).str.rstrip("/").str.rsplit("/", n=1).str[-1].replace("", "home")
        )
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    enriched.to_csv(args.output, index=False)
    print(f"Saved enriched pages to {args.output} ({len(enriched)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
