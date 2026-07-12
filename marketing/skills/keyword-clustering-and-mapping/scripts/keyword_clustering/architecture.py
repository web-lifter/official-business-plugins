"""Structured site-architecture planning from a clustered keyword frame.

Turns the per-keyword clustering output into a deterministic, volume-weighted
plan: one record per cluster describing the recommended action (create /
optimise / consolidate / deprioritise), the target page type, a hub/spoke role,
and a URL slug. The skill narrates ``architecture.json`` into a human
``proposed-architecture.md``; keeping the structured layer here makes the plan
reproducible run-to-run rather than free-hand.

Modes
-----
- ``existing_only``  — never propose new pages; clusters with no compatible page
  are reported as gaps (``action='gap'``) but no slug is invented.
- ``optimise_expand`` — optimise compatible existing pages and propose new pages
  for genuine gaps (the default).
- ``greenfield``    — ignore existing pages; design every cluster as a new page.
"""

from __future__ import annotations

import json
import re
from collections import Counter

import pandas as pd

from .page_types import COMMERCIAL_INTENTS, COMMERCIAL_TARGET_TYPES

# A chosen existing page must clear this raw text-similarity bar to count as a
# real match worth optimising (below it the cluster is treated as a gap).
_OPTIMISE_MIN_SIM = 0.45


def slugify(text: str) -> str:
    """Lower-case hyphen slug, de-duplicating repeated tokens.

    Cluster labels are built from top terms and often repeat (e.g.
    'ads / management / ads management'); collapse repeats so slugs read
    'ads-management' rather than 'ads-management-ads-management'.
    """
    seen: set[str] = set()
    tokens: list[str] = []
    for tok in re.split(r"[^a-z0-9]+", str(text).lower()):
        if tok and tok not in seen:
            seen.add(tok)
            tokens.append(tok)
    return "-".join(tokens) or "page"


def _dominant(series: pd.Series, default: str = "mixed") -> str:
    vals = [str(v).strip() for v in series.dropna().tolist() if str(v).strip()]
    if not vals:
        return default
    return Counter(vals).most_common(1)[0][0]


def _target_page_type(intent: str) -> str:
    return "service" if intent in COMMERCIAL_INTENTS else "guide"


def build_architecture(
    df: pd.DataFrame,
    mode: str = "optimise_expand",
    excluded_terms: set[str] | None = None,
) -> list[dict]:
    """Return one architecture record per cluster, volume-ranked.

    ``excluded_terms`` are off-service topic substrings (from ``focus.json``); a
    cluster whose label contains any of them is marked ``deprioritise``.
    """
    excluded_terms = {e.lower().strip() for e in (excluded_terms or set()) if e.strip()}
    if "cluster_id" not in df.columns:
        return []

    vol_col = "search_volume" if "search_volume" in df.columns else None
    records: list[dict] = []

    for cluster_id, group in df.groupby("cluster_id", dropna=False):
        if cluster_id == -1:  # hdbscan noise
            continue
        label = _dominant(group.get("cluster_label", pd.Series(dtype=str)), default=f"cluster-{cluster_id}")
        intent = _dominant(group.get("primary_intent", pd.Series(dtype=str)))
        volume = int(pd.to_numeric(group[vol_col], errors="coerce").fillna(0).sum()) if vol_col else 0
        keyword_count = int(len(group))
        rep = _dominant(group.get("representative_keyword", pd.Series(dtype=str)), default=label)

        # Best existing page this cluster matches (only meaningful outside greenfield).
        existing_page = existing_url = existing_type = ""
        existing_sim = 0.0
        if mode != "greenfield" and "recommended_page" in group.columns:
            best = group.sort_values("page_similarity_score", ascending=False).iloc[0]
            existing_page = str(best.get("recommended_page", "") or "")
            existing_url = str(best.get("recommended_url", "") or "")
            existing_type = str(best.get("recommended_page_type", "") or "")
            existing_sim = round(float(best.get("page_similarity_score", 0.0) or 0.0), 4)

        target_type = _target_page_type(intent)
        is_commercial = intent in COMMERCIAL_INTENTS
        compatible_existing = (
            existing_page
            and existing_sim >= _OPTIMISE_MIN_SIM
            and (
                (is_commercial and existing_type in COMMERCIAL_TARGET_TYPES)
                or (not is_commercial and existing_type in {"blog", "guide", "news"})
            )
        )

        if any(term in label.lower() for term in excluded_terms):
            action, target, rationale = (
                "deprioritise",
                existing_url or "",
                "Off-service topic excluded via focus.json — do not invest unless the offering changes.",
            )
        elif mode == "greenfield":
            action, target, rationale = (
                "create",
                f"/{slugify(label)}",
                f"Greenfield: new {target_type} page for this cluster.",
            )
        elif compatible_existing:
            action, target, rationale = (
                "optimise",
                existing_url,
                f"Compatible {existing_type} page exists (sim {existing_sim}); deepen it to win the cluster.",
            )
        elif mode == "existing_only":
            action, target, rationale = (
                "gap",
                "",
                f"No compatible {target_type} page exists (best match was "
                f"'{existing_page or 'none'}' [{existing_type or 'n/a'}], sim {existing_sim}). "
                "Expansion disabled in existing-only mode.",
            )
        else:  # optimise_expand, genuine gap
            action, target, rationale = (
                "create",
                f"/{'services/' if is_commercial else 'guides/'}{slugify(label)}",
                f"No compatible {target_type} page (best was '{existing_page or 'none'}' "
                f"[{existing_type or 'n/a'}], sim {existing_sim}); create a dedicated {target_type} page.",
            )

        records.append(
            {
                "cluster_id": int(cluster_id) if pd.notna(cluster_id) else -1,
                "cluster_label": label,
                "representative_keyword": rep,
                "primary_intent": intent,
                "keyword_count": keyword_count,
                "search_volume": volume,
                "action": action,
                "target_page_type": target_type,
                "target": target,
                "existing_page": existing_page,
                "existing_url": existing_url,
                "existing_page_type": existing_type,
                "existing_similarity": existing_sim,
                "role": "",  # filled by _assign_hub_spoke
                "parent": "",
                "supporting_cluster_ids": [],
                "rationale": rationale,
            }
        )

    records.sort(key=lambda r: r["search_volume"], reverse=True)
    _assign_hub_spoke(records)
    _flag_consolidation(records)
    return records


def _topic_key(label: str) -> str:
    """Coarse topic grouping: the most salient non-generic token of the label."""
    generic = {"agency", "services", "service", "australia", "near", "me", "best", "top", "company"}
    tokens = [t for t in re.split(r"[^a-z0-9]+", label.lower()) if t and t not in generic]
    return tokens[0] if tokens else label.lower()


def _assign_hub_spoke(records: list[dict]) -> None:
    """Largest-volume commercial cluster per topic = hub; the rest are spokes."""
    groups: dict[str, list[dict]] = {}
    for r in records:
        if r["action"] in {"deprioritise", "gap"}:
            continue
        groups.setdefault(_topic_key(r["cluster_label"]), []).append(r)
    for members in groups.values():
        members.sort(key=lambda r: r["search_volume"], reverse=True)
        hub = members[0]
        hub["role"] = "hub"
        for spoke in members[1:]:
            spoke["role"] = "spoke"
            spoke["parent"] = hub["target"] or hub["cluster_label"]
            hub["supporting_cluster_ids"].append(spoke["cluster_id"])


def _flag_consolidation(records: list[dict]) -> None:
    """If two optimise targets point at the same existing URL, flag consolidation."""
    by_url: dict[str, list[dict]] = {}
    for r in records:
        if r["action"] == "optimise" and r["existing_url"]:
            by_url.setdefault(r["existing_url"], []).append(r)
    for url, rs in by_url.items():
        if len(rs) > 1:
            keep = max(rs, key=lambda r: r["search_volume"])
            for r in rs:
                if r is keep:
                    continue
                r["action"] = "consolidate"
                r["rationale"] = (
                    f"Multiple clusters target {url}; consolidate into the hub cluster "
                    f"'{keep['cluster_label']}' (301/canonical) to avoid cannibalisation."
                )


def write_architecture(records: list[dict], path: str) -> str:
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"clusters": records}, f, indent=2)
    return path
