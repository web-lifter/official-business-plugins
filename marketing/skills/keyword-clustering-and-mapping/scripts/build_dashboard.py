#!/usr/bin/env python3
"""Combine every clustering output into one offline ``dashboard.html``.

Plotly.js is inlined exactly once so the dashboard opens with no internet. Charts
are regenerated from the run (when called in-process with the live result) or
from the saved CSVs/HTML (disk fallback). Markdown reports are rendered inline;
CSVs get scrollable previews. The raw files are left untouched as source data.

Usage (disk fallback):
    python build_dashboard.py <output_dir> [--mode optimise_expand]
In-process (preferred), from run_clustering.py:
    build_dashboard(output_dir, result=result, mode=..., topic_labels=...)
"""

from __future__ import annotations

import argparse
import html
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import pandas as pd  # noqa: E402

try:
    import markdown as _markdown
except Exception:  # noqa: BLE001
    _markdown = None

ACCENT = "#2f5bea"
_ACTION_ORDER = ["create", "optimise", "consolidate", "gap", "deprioritise"]
_ACTION_BADGE = {
    "create": "#16a34a", "optimise": "#2563eb", "consolidate": "#d97706",
    "gap": "#9333ea", "deprioritise": "#6b7280",
}


# --------------------------------------------------------------------------- #
# Fragment helpers
# --------------------------------------------------------------------------- #
def _fig_div(fig, *, first: bool) -> str:
    """Render a Plotly figure as an embeddable div; inline plotly.js on the first only."""
    return fig.to_html(
        full_html=False,
        include_plotlyjs=True if first else False,
        config={"responsive": True, "displaylogo": False},
    )


def _render_markdown(path: str) -> str:
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if _markdown is not None:
        return _markdown.markdown(text, extensions=["tables", "fenced_code", "toc"])
    return f"<pre>{html.escape(text)}</pre>"


def _csv_preview(path: str, max_rows: int = 60) -> str:
    if not os.path.exists(path):
        return ""
    try:
        df = pd.read_csv(path)
    except Exception:  # noqa: BLE001
        return ""
    note = f"<p class='muted'>{len(df)} rows · showing first {min(max_rows, len(df))}</p>"
    return note + df.head(max_rows).to_html(index=False, border=0, classes="data")


def _architecture_html(output_dir: str) -> str:
    path = os.path.join(output_dir, "architecture.json")
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        records = json.load(f).get("clusters", [])
    if not records:
        return ""
    records = sorted(
        records,
        key=lambda r: (_ACTION_ORDER.index(r["action"]) if r["action"] in _ACTION_ORDER else 99, -r.get("search_volume", 0)),
    )
    rows = []
    for r in records:
        badge = _ACTION_BADGE.get(r["action"], "#6b7280")
        rows.append(
            "<tr>"
            f"<td><span class='badge' style='background:{badge}'>{html.escape(r['action'])}</span></td>"
            f"<td>{html.escape(str(r['cluster_label']))}</td>"
            f"<td>{html.escape(str(r.get('role','')))}</td>"
            f"<td>{html.escape(str(r['primary_intent']))}</td>"
            f"<td>{html.escape(str(r['target_page_type']))}</td>"
            f"<td><code>{html.escape(str(r['target']))}</code></td>"
            f"<td style='text-align:right'>{int(r.get('search_volume',0)):,}</td>"
            f"<td>{int(r.get('keyword_count',0))}</td>"
            f"<td>{html.escape(str(r['rationale']))}</td>"
            "</tr>"
        )
    return (
        "<table class='data'><thead><tr>"
        "<th>Action</th><th>Cluster</th><th>Role</th><th>Intent</th><th>Page type</th>"
        "<th>Target</th><th>Volume</th><th>Kw</th><th>Rationale</th>"
        "</tr></thead><tbody>" + "".join(rows) + "</tbody></table>"
    )


def _metrics_html(df: pd.DataFrame, output_dir: str) -> str:
    n_kw = len(df)
    n_clusters = int(df["cluster_id"].nunique()) if "cluster_id" in df.columns else 0
    vol = int(pd.to_numeric(df.get("search_volume", df.get("volume", pd.Series(dtype=float))), errors="coerce").fillna(0).sum())
    gaps = int(df["content_gap"].sum()) if "content_gap" in df.columns else 0
    cards = [
        ("Keywords", f"{n_kw:,}"),
        ("Clusters", f"{n_clusters}"),
        ("Addressable volume / mo", f"{vol:,}"),
        ("Content gaps", f"{gaps:,}"),
    ]
    return "".join(f"<div class='card'><div class='num'>{v}</div><div class='lbl'>{k}</div></div>" for k, v in cards)


# --------------------------------------------------------------------------- #
# Assembly
# --------------------------------------------------------------------------- #
def _tab(tab_id: str, label: str, body: str, active: bool = False) -> tuple[str, str]:
    btn = f"<button class='tab{' active' if active else ''}' onclick=\"showTab('{tab_id}')\">{label}</button>"
    panel = f"<section id='{tab_id}' class='panel{' active' if active else ''}'>{body}</section>"
    return btn, panel


def build_dashboard(output_dir: str, *, result=None, mode: str = "optimise_expand", topic_labels=None) -> str:
    """Write ``<output_dir>/dashboard.html`` and return its path."""
    from keyword_clustering import visualization as viz

    if result is not None:
        df = result.df
    else:
        ck = os.path.join(output_dir, "clustered_keywords.csv")
        df = pd.read_csv(ck) if os.path.exists(ck) else pd.DataFrame()

    figures: list[tuple[str, str, object]] = []  # (tab_id, label, fig)
    if not df.empty:
        figures.append(("opportunity", "Opportunity Matrix", viz.plot_opportunity_matrix(df)))
        figures.append(("treemap", "Treemap", viz.plot_treemap(df)))
        figures.append(("sankey", "Cluster → Page", viz.plot_sankey(df)))
        if result is not None and getattr(result, "coords", None) is not None:
            coords = result.coords
            figures.append(("map2d", "Cluster Map 2D", viz.plot_2d_clusters(df, coords[:, :2])))
            figures.append(("map3d", "Cluster Map 3D", viz.plot_3d_clusters(df, coords)))
            figures.append(("network", "Keyword Network", viz.plot_network_graph(df, result.keyword_vectors)))

    # Build chart fragments, inlining plotly.js on the first chart only.
    chart_btns, chart_panels = [], []
    first = True
    for tab_id, label, fig in figures:
        try:
            body = f"<div class='chartwrap'>{_fig_div(fig, first=first)}</div>"
            first = False
        except Exception as exc:  # noqa: BLE001
            body = f"<p class='muted'>Chart unavailable: {html.escape(str(exc))}</p>"
        btn, panel = _tab(tab_id, label, body, active=not chart_btns)
        chart_btns.append(btn)
        chart_panels.append(panel)

    # Reports + architecture + data tabs.
    parent = os.path.dirname(output_dir.rstrip("/\\"))
    report_sources = [
        ("Strategy report", os.path.join(parent, "cluster-strategy-report.md")),
        ("Proposed architecture", os.path.join(output_dir, "proposed-architecture.md")),
        ("Engine recommendations", os.path.join(output_dir, "recommendations.md")),
    ]
    report_html = ""
    for label, path in report_sources:
        rendered = _render_markdown(path)
        if rendered:
            report_html += f"<h2>{label}</h2><div class='report'>{rendered}</div>"
    arch_html = _architecture_html(output_dir)
    if arch_html:
        report_html = f"<h2>Architecture plan</h2>{arch_html}" + report_html

    data_html = ""
    for label, fname in [
        ("Cluster summary", "cluster_summary.csv"),
        ("Content gaps", "content_gap_report.csv"),
        ("Keyword → page map", "keyword_page_map.csv"),
        ("Cannibalisation", "cannibalization_report.csv"),
        ("Cluster quality", "cluster_quality_report.csv"),
        ("Excluded (off-service)", "excluded_keywords.csv"),
    ]:
        preview = _csv_preview(os.path.join(output_dir, fname))
        if preview:
            data_html += f"<h2>{label} <span class='muted'>({fname})</span></h2>{preview}"

    btns, panels = [], []
    overview = f"<div class='cards'>{_metrics_html(df, output_dir)}</div>" if not df.empty else "<p>No data.</p>"
    overview += f"<p class='muted'>Mode: <strong>{html.escape(mode)}</strong>. Raw files are preserved in this folder.</p>"
    b, p = _tab("overview", "Overview", overview, active=True)
    btns.append(b)
    panels.append(p)
    # charts (none active since overview is active)
    btns += chart_btns
    panels += chart_panels
    if report_html:
        b, p = _tab("reports", "Reports & Plan", report_html)
        btns.append(b)
        panels.append(p)
    if data_html:
        b, p = _tab("data", "Data", data_html)
        btns.append(b)
        panels.append(p)

    doc = _PAGE.format(accent=ACCENT, tabs="".join(btns), panels="".join(panels))
    out_path = os.path.join(output_dir, "dashboard.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    return out_path


_PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Keyword Clustering Dashboard — Web Lifter SEO Toolkit</title>
<style>
  :root {{ --accent: {accent}; }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif; color:#1f2937; background:#f3f4f6; }}
  header {{ background:var(--accent); color:#fff; padding:18px 24px; }}
  header h1 {{ margin:0; font-size:20px; }}
  header p {{ margin:4px 0 0; opacity:.85; font-size:13px; }}
  nav {{ position:sticky; top:0; background:#fff; border-bottom:1px solid #e5e7eb; padding:0 12px; display:flex; flex-wrap:wrap; z-index:5; }}
  .tab {{ border:0; background:none; padding:14px 16px; font-size:14px; cursor:pointer; color:#6b7280; border-bottom:3px solid transparent; }}
  .tab.active {{ color:var(--accent); border-bottom-color:var(--accent); font-weight:600; }}
  .panel {{ display:none; padding:24px; max-width:1200px; margin:0 auto; }}
  .panel.active {{ display:block; }}
  .cards {{ display:flex; gap:16px; flex-wrap:wrap; margin-bottom:16px; }}
  .card {{ background:#fff; border:1px solid #e5e7eb; border-radius:10px; padding:18px 22px; min-width:170px; }}
  .card .num {{ font-size:26px; font-weight:700; color:var(--accent); }}
  .card .lbl {{ font-size:12px; color:#6b7280; text-transform:uppercase; letter-spacing:.04em; }}
  .chartwrap {{ background:#fff; border:1px solid #e5e7eb; border-radius:10px; padding:8px; }}
  table.data {{ border-collapse:collapse; width:100%; background:#fff; font-size:13px; }}
  table.data th, table.data td {{ border:1px solid #e5e7eb; padding:6px 9px; text-align:left; vertical-align:top; }}
  table.data th {{ background:#f9fafb; position:sticky; top:0; }}
  .badge {{ color:#fff; padding:2px 8px; border-radius:99px; font-size:11px; text-transform:uppercase; letter-spacing:.03em; }}
  .report {{ background:#fff; border:1px solid #e5e7eb; border-radius:10px; padding:8px 22px; margin-bottom:20px; }}
  .report table {{ border-collapse:collapse; }} .report th,.report td {{ border:1px solid #e5e7eb; padding:5px 8px; }}
  .muted {{ color:#6b7280; font-size:12px; }}
  h2 {{ font-size:16px; margin-top:26px; }}
</style></head>
<body>
<header><h1>Keyword Clustering &amp; Content Strategy</h1><p>Web Lifter SEO Toolkit · self-contained dashboard</p></header>
<nav>{tabs}</nav>
{panels}
<script>
  function showTab(id) {{
    document.querySelectorAll('.panel').forEach(function(p){{p.classList.remove('active');}});
    document.querySelectorAll('.tab').forEach(function(t){{t.classList.remove('active');}});
    var panel = document.getElementById(id); if (panel) panel.classList.add('active');
    var btn = [].slice.call(document.querySelectorAll('.tab')).find(function(t){{return t.getAttribute('onclick').indexOf("'"+id+"'")>-1;}});
    if (btn) btn.classList.add('active');
    window.dispatchEvent(new Event('resize'));
  }}
</script>
</body></html>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Combine clustering outputs into one offline dashboard.html")
    ap.add_argument("output_dir")
    ap.add_argument("--mode", default="optimise_expand")
    args = ap.parse_args()
    path = build_dashboard(args.output_dir, mode=args.mode)
    print(f"dashboard: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
