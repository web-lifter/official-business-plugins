"""Plaintext credential loader for marketing.

Dead simple: read provider API keys from a JSON file. No encryption, no
passphrase, no OAuth, no setup wizard. You edit one file, every skill reads it.

File location (first match wins):

    1. $SEO_CREDENTIALS_FILE                              (explicit override)
    2. $CLAUDE_PLUGIN_DATA/credentials.json               (installed plugin data dir)
    3. ~/.claude/plugins/data/marketing/credentials.json  (canonical default)

File shape::

    {
      "serpapi":    { "api_key": "..." },
      "dataforseo": { "login": "...", "password": "..." },
      "ahrefs":     { "api_key": "..." },
      "moz":        { "access_id": "...", "secret": "..." },
      "psi":        { "api_key": "..." }
    }

Per-credential environment variables still override the file (handy for CI):
``SERPAPI_KEY``, ``DATAFORSEO_LOGIN`` / ``DATAFORSEO_PASSWORD``,
``AHREFS_API_KEY``, ``MOZ_ACCESS_ID`` / ``MOZ_SECRET``, ``PSI_API_KEY``.

Public API::

    credentials_path() -> Path | None     # the file that will be read, if any
    canonical_path() -> Path               # where to create the file
    load_credentials() -> dict             # parsed file, or {} if absent
    get_credential(provider, key, env_var=None) -> str | None
"""

from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Any


def canonical_path() -> Path:
    """Return the documented default location for the credentials file."""
    return (
        Path(os.path.expanduser("~"))
        / ".claude"
        / "plugins"
        / "data"
        / "marketing"
        / "credentials.json"
    )


def _candidate_paths() -> list[Path]:
    """Return candidate credential file paths, in priority order."""
    paths: list[Path] = []
    override = os.environ.get("SEO_CREDENTIALS_FILE")
    if override:
        paths.append(Path(override))
    plugin_data = os.environ.get("CLAUDE_PLUGIN_DATA")
    if plugin_data:
        paths.append(Path(plugin_data) / "credentials.json")
    paths.append(canonical_path())
    return paths


def credentials_path() -> Path | None:
    """Return the first credentials file that exists, or ``None``."""
    for p in _candidate_paths():
        if p.is_file():
            return p
    return None


@lru_cache(maxsize=1)
def load_credentials() -> dict[str, Any]:
    """Load and parse the credentials file.

    Returns an empty dict if no file is found. Raises ``ValueError`` with a
    clear message if a file exists but is not valid JSON.
    """
    path = credentials_path()
    if path is None:
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"marketing: {path} is not valid JSON ({exc}). "
            "Fix the file or delete it and re-create it."
        ) from exc


def get_credential(provider: str, key: str, env_var: str | None = None) -> str | None:
    """Resolve a single credential value.

    Args:
        provider: Top-level provider key in the JSON file (e.g. ``"serpapi"``).
        key:      Field within the provider (e.g. ``"api_key"``).
        env_var:  Optional environment variable that overrides the file value.

    Returns:
        The credential string, or ``None`` if neither the env var nor the file
        provides it.
    """
    if env_var:
        val = os.environ.get(env_var)
        if val:
            return val
    return load_credentials().get(provider, {}).get(key) or None
