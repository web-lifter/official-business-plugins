"""Account-isolated GET cache. Never cache POST operations or raw credentials."""
from __future__ import annotations
import hashlib
import json
import math
import os
import tempfile
import time
from pathlib import Path
from typing import Any
import httpx


def _cache_dir() -> Path:
    data = os.environ.get("PLUGIN_DATA") or os.environ.get("CLAUDE_PLUGIN_DATA")
    cache = Path(data or Path.home() / ".claude/plugins/data/marketing") / "cache"
    cache.mkdir(parents=True, exist_ok=True, mode=0o700)
    return cache


def _cache_key(url: str, params: dict[str, Any] | None, headers: dict[str, str] | None = None) -> str:
    canonical = json.dumps([url, params or {}, {k.lower(): v for k, v in (headers or {}).items()}],
                           sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(canonical.encode()).hexdigest()


def cached_get(url: str, params: dict[str, Any] | None = None, ttl_hours: float = 24,
               headers: dict[str, str] | None = None) -> dict[str, Any]:
    if not math.isfinite(ttl_hours) or ttl_hours < 0:
        raise ValueError("cache TTL must be finite and non-negative")
    try:
        path = _cache_dir() / (_cache_key(url, params, headers) + ".json") if ttl_hours else None
    except OSError:
        path = None
    if path:
        try:
            age = time.time() - path.stat().st_mtime
            if 0 <= age < ttl_hours * 3600:
                cached = json.loads(path.read_text(encoding="utf-8"))
                if isinstance(cached, dict):
                    return cached
        except (OSError, ValueError):
            pass  # Corrupt, expired or concurrently replaced entries are cache misses.
    with httpx.Client(timeout=30.0) as client:
        response = client.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
    if not isinstance(data, dict):
        raise ValueError("expected a JSON object response")
    if path:
        tmp = None
        try:
            with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, encoding="utf-8", delete=False) as f:
                tmp = Path(f.name)  # tempfile creates owner-only files on POSIX.
                json.dump(data, f, ensure_ascii=False, allow_nan=False)
            os.replace(tmp, path)
        except OSError:
            pass  # A cache write failure must not invalidate a successful API response.
        finally:
            if tmp:
                try:
                    tmp.unlink(missing_ok=True)
                except OSError:
                    pass
    return data
