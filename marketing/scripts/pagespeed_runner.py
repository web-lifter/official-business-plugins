"""PageSpeed Insights runner for marketing.

Calls the Google PageSpeed Insights API for a given URL and extracts Core Web
Vitals (LCP, INP, CLS, TTFB) plus the overall Lighthouse performance score.
Emits JSON to stdout for consumption by skills.

PSI API key is read from the credentials file under provider ``psi``, key
``api_key`` (or the ``PSI_API_KEY`` environment variable).

Usage::

    python pagespeed_runner.py https://example.com.au
    python pagespeed_runner.py https://example.com.au --strategy desktop
    python pagespeed_runner.py https://example.com.au --strategy mobile --pretty
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))

import httpx
from lib.credentials import canonical_path, get_credential

_PSI_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"


def _get_api_key() -> str:
    """Read the PSI API key from the credentials file or env var."""
    key = get_credential("psi", "api_key", env_var="PSI_API_KEY")
    if not key:
        raise RuntimeError(
            f"PSI API key not found. Add it to {canonical_path()} as "
            '{"psi": {"api_key": "YOUR_KEY"}} (or set the PSI_API_KEY env var).'
        )
    return key


def _extract_metric(audits: dict, audit_id: str, display_key: str = "displayValue") -> str | None:
    """Safely extract a display value from a Lighthouse audit."""
    audit = audits.get(audit_id, {})
    return audit.get(display_key) or audit.get("numericValue")


def run_psi(url: str, strategy: str = "mobile") -> dict[str, Any]:
    """Call the PSI API and return a normalised metrics dict.

    Args:
        url:      The page URL to analyse.
        strategy: ``"mobile"`` (default) or ``"desktop"``.

    Returns:
        Dict with keys: ``url``, ``strategy``, ``score``, ``lcp``, ``inp``,
        ``cls``, ``ttfb``, ``fcp``, ``speed_index``, ``total_blocking_time``,
        ``field_data`` (CrUX data if available), ``raw`` (full API response).
    """
    api_key = _get_api_key()
    params = {
        "url": url,
        "strategy": strategy,
        "key": api_key,
        "category": "performance",
    }

    with httpx.Client(timeout=60.0) as client:
        response = client.get(_PSI_ENDPOINT, params=params)
        response.raise_for_status()

    data: dict[str, Any] = response.json()

    lighthouse = data.get("lighthouseResult", {})
    audits: dict = lighthouse.get("audits", {})
    categories: dict = lighthouse.get("categories", {})
    score_raw = categories.get("performance", {}).get("score")
    score = round(score_raw * 100) if score_raw is not None else None

    # Lab (Lighthouse) metrics
    lab: dict[str, Any] = {
        "lcp": _extract_metric(audits, "largest-contentful-paint"),
        "inp": _extract_metric(audits, "interaction-to-next-paint"),
        "cls": _extract_metric(audits, "cumulative-layout-shift"),
        "ttfb": _extract_metric(audits, "server-response-time"),
        "fcp": _extract_metric(audits, "first-contentful-paint"),
        "speed_index": _extract_metric(audits, "speed-index"),
        "total_blocking_time": _extract_metric(audits, "total-blocking-time"),
    }

    # Field (CrUX) data
    crux: dict[str, Any] = {}
    loading_exp = data.get("loadingExperience", {})
    for metric_id, metric_data in loading_exp.get("metrics", {}).items():
        crux[metric_id] = {
            "category": metric_data.get("category"),
            "percentile": metric_data.get("percentile"),
        }

    return {
        "url": url,
        "strategy": strategy,
        "score": score,
        **lab,
        "field_data": crux,
    }


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Run PageSpeed Insights for a URL")
    parser.add_argument("url", help="Page URL to analyse")
    parser.add_argument(
        "--strategy",
        choices=["mobile", "desktop"],
        default="mobile",
        help="Analysis strategy (default: mobile)",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    args = parser.parse_args()

    try:
        result = run_psi(args.url, strategy=args.strategy)
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"error": str(exc)}))
        sys.exit(1)

    indent = 2 if args.pretty else None
    print(json.dumps(result, indent=indent))


if __name__ == "__main__":
    main()
