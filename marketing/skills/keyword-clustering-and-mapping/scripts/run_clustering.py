#!/usr/bin/env python3
"""Self-contained clustering runner for the keyword-clustering-and-mapping skill.

Replaces the external ``keyword-cluster`` CLI. Imports the engine vendored under
``scripts/keyword_clustering/`` and adds the skill-specific behaviour:

- **--mode** {optimise_only, optimise_expand, greenfield} — drives the structured
  architecture plan (``architecture.json``). ``existing_only`` is accepted as an
  alias for ``optimise_only``.
- **--focus-file** focus.json — exclude off-service topics before clustering and
  carry them into the architecture plan as ``deprioritise``.
- Page-type & intent-aware mapping (engine), opportunity-matrix fix (engine), and
  a single offline ``dashboard.html`` (via build_dashboard.py).

Everything runs locally with Python — no CLI, no network API.

Example:
    python run_clustering.py \
        --keywords master.csv --pages pages-enriched.csv \
        --output ./output --method kmeans --auto-k silhouette \
        --similarity semantic --embedding-model mpnet \
        --mode optimise_expand --focus-file focus.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

# Make the vendored package importable regardless of CWD.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import pandas as pd  # noqa: E402

from keyword_clustering.architecture import build_architecture, write_architecture  # noqa: E402
from keyword_clustering.cli import _config_from_args, _load_serp, build_parser  # noqa: E402
from keyword_clustering.export import build_interactive_report, save_all_outputs  # noqa: E402
from keyword_clustering.pipeline import run_keyword_clustering  # noqa: E402
from keyword_clustering.visualization import save_all_charts  # noqa: E402

_MODE_ALIASES = {
    "existing_only": "optimise_only",
    "existing": "optimise_only",
    "optimise-only": "optimise_only",
    "optimise_only": "optimise_only",
    "optimise-expand": "optimise_expand",
    "optimise_expand": "optimise_expand",
    "expand": "optimise_expand",
    "greenfield": "greenfield",
    "scratch": "greenfield",
}


def _load_exclusions(focus_file: str | None) -> list[str]:
    if not focus_file or not os.path.exists(focus_file):
        return []
    try:
        with open(focus_file, encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return []
    terms = data.get("exclude") or data.get("exclusions") or []
    return [str(t).strip().lower() for t in terms if str(t).strip()]


def _apply_exclusions(df: pd.DataFrame, terms: list[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    if not terms:
        return df, df.iloc[0:0]
    kw = df["keyword"].astype(str).str.lower()
    mask = pd.Series(False, index=df.index)
    for t in terms:
        mask = mask | kw.str.contains(rf"\b{re.escape(t)}\b", regex=True, na=False)
    return df[~mask].copy(), df[mask].copy()


def _ensure_pages(pages_df: pd.DataFrame | None) -> pd.DataFrame | None:
    if pages_df is None:
        return None
    if "url" not in pages_df.columns:
        raise SystemExit("Pages CSV must include a 'url' column.")
    if "page_name" not in pages_df.columns:
        # Derive a human label from the URL's last path segment.
        pages_df = pages_df.copy()
        pages_df["page_name"] = (
            pages_df["url"].astype(str).str.rstrip("/").str.rsplit("/", n=1).str[-1].replace("", "home")
        )
    return pages_df


def _semantic_available() -> bool:
    try:
        import sentence_transformers  # noqa: F401

        return True
    except Exception:  # noqa: BLE001
        return False


def _build_engine_args(ns: argparse.Namespace) -> argparse.Namespace:
    """Parse a minimal argv through the engine's own parser to inherit all defaults."""
    argv = ["run", "--keywords", ns.keywords, "--output", ns.output, "--method", ns.method,
            "--similarity", ns.similarity, "--embedding-model", ns.embedding_model]
    if ns.pages:
        argv += ["--pages", ns.pages]
    if ns.topics:
        argv += ["--topics", ns.topics]
    if ns.serp_file:
        argv += ["--serp-file", ns.serp_file]
    if ns.auto_k:
        argv += ["--auto-k", ns.auto_k]
    if ns.clusters is not None:
        argv += ["--clusters", str(ns.clusters)]
    return build_parser().parse_args(argv)


def main() -> None:
    p = argparse.ArgumentParser(description="Self-contained keyword clustering + page mapping + architecture.")
    p.add_argument("--keywords", required=True, help="Master keyword CSV (needs a 'keyword' column).")
    p.add_argument("--pages", default=None, help="Pages CSV (url + page_name; enriched is better).")
    p.add_argument("--topics", default=None)
    p.add_argument("--serp-file", dest="serp_file", default=None)
    p.add_argument("--output", required=True, help="Output directory.")
    p.add_argument("--method", default="kmeans", choices=["kmeans", "agglomerative", "hdbscan", "graph"])
    p.add_argument("--clusters", type=int, default=None)
    p.add_argument("--auto-k", dest="auto_k", default="silhouette", choices=["none", "silhouette"])
    p.add_argument("--similarity", default="semantic", choices=["semantic", "tfidf", "hybrid"])
    p.add_argument("--embedding-model", dest="embedding_model", default="mpnet")
    p.add_argument("--mode", default="optimise_expand", help="optimise_only | optimise_expand | greenfield")
    p.add_argument("--focus-file", dest="focus_file", default=None, help="focus.json with an 'exclude' list.")
    p.add_argument("--no-dashboard", dest="no_dashboard", action="store_true")
    ns = p.parse_args()

    mode = _MODE_ALIASES.get(str(ns.mode).strip().lower(), "optimise_expand")
    os.makedirs(ns.output, exist_ok=True)

    # Degrade gracefully if semantic deps are unavailable.
    if (ns.similarity in {"semantic", "hybrid"} or ns.embedding_model != "tfidf") and not _semantic_available():
        print("WARNING: sentence-transformers not available — falling back to tf-idf.", file=sys.stderr)
        ns.similarity = "tfidf"
        ns.embedding_model = "tfidf"

    args = _build_engine_args(ns)

    df = _load_serp(pd.read_csv(ns.keywords), ns.serp_file)
    exclude_terms = _load_exclusions(ns.focus_file)
    df, dropped = _apply_exclusions(df, exclude_terms)
    if len(dropped):
        dropped_path = os.path.join(ns.output, "excluded_keywords.csv")
        dropped.to_csv(dropped_path, index=False)
        print(f"Excluded {len(dropped)} off-service keyword(s) -> {dropped_path}")

    pages_df = _ensure_pages(pd.read_csv(ns.pages)) if ns.pages else None
    topics_df = pd.read_csv(ns.topics) if ns.topics else None

    config = _config_from_args(args)
    result = run_keyword_clustering(df, pages_df, topics_df, config)

    saved = save_all_outputs(result.df, ns.output, keyword_vectors=result.keyword_vectors, run_dir=result.run_dir)
    topic_labels = (
        topics_df["topic"].dropna().astype(str).tolist()
        if topics_df is not None and "topic" in topics_df.columns
        else None
    )
    save_all_charts(result.df, result.keyword_vectors, result.coords, ns.output,
                    topic_vectors=result.topic_vectors, topic_labels=topic_labels)
    report_path = build_interactive_report(ns.output)

    arch_path = ""
    if mode in {"optimise_expand", "greenfield", "optimise_only"}:
        records = build_architecture(result.df, mode=mode, excluded_terms=set(exclude_terms))
        arch_path = write_architecture(records, os.path.join(ns.output, "architecture.json"))

    dashboard_path = ""
    if not ns.no_dashboard:
        try:
            from build_dashboard import build_dashboard

            dashboard_path = build_dashboard(ns.output, result=result, mode=mode, topic_labels=topic_labels)
        except Exception as exc:  # noqa: BLE001 — dashboard is best-effort
            print(f"WARNING: dashboard build failed ({exc}).", file=sys.stderr)

    print("Done. Summary:")
    print(f"  Mode: {mode}")
    print(f"  Keywords: {result.metrics['n_keywords']}  Clusters: {result.metrics['n_clusters']}")
    for label, path in saved.items():
        print(f"  {label}: {path}")
    print(f"  interactive_report: {report_path}")
    if arch_path:
        print(f"  architecture: {arch_path}")
    if dashboard_path:
        print(f"  dashboard: {dashboard_path}")


if __name__ == "__main__":
    main()
