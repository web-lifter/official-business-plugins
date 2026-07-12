"""SEO Toolkit credential status.

Reports which providers have credentials configured in the plaintext
credentials file. Never prints secret values — only presence.

Usage::

    python seo_status.py            # human-readable table
    python seo_status.py --json     # machine-readable
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from lib.credentials import (  # noqa: E402
    canonical_path,
    credentials_path,
    get_credential,
)

# provider -> (label, [(field, env_var), ...])
_PROVIDERS = {
    "serpapi": ("SerpAPI", [("api_key", "SERPAPI_KEY")]),
    "dataforseo": (
        "DataForSEO",
        [("login", "DATAFORSEO_LOGIN"), ("password", "DATAFORSEO_PASSWORD")],
    ),
    "ahrefs": ("Ahrefs", [("api_key", "AHREFS_API_KEY")]),
    "moz": ("Moz", [("access_id", "MOZ_ACCESS_ID"), ("secret", "MOZ_SECRET")]),
    "psi": ("PageSpeed Insights", [("api_key", "PSI_API_KEY")]),
}


def _status() -> dict:
    path = credentials_path()
    providers = {}
    for key, (label, fields) in _PROVIDERS.items():
        present = all(get_credential(key, f, env_var=ev) for f, ev in fields)
        providers[key] = {"label": label, "configured": bool(present)}
    return {
        "credentials_file": str(path) if path else None,
        "canonical_path": str(canonical_path()),
        "providers": providers,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="marketing credential status")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    result = _status()

    if args.json:
        print(json.dumps(result, indent=2))
        return

    if result["credentials_file"]:
        print(f"Credentials file: {result['credentials_file']}\n")
    else:
        print("No credentials file found.")
        print(f"Create one at: {result['canonical_path']}\n")

    print(f"{'Provider':<22} {'Configured'}")
    print(f"{'-' * 22} {'-' * 10}")
    for info in result["providers"].values():
        print(f"{info['label']:<22} {'yes' if info['configured'] else 'no'}")


if __name__ == "__main__":
    main()
