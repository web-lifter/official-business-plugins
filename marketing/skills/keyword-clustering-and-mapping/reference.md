# Keyword Clustering and Mapping — Reference

## Bundled engine

The clustering engine is **vendored** under `scripts/keyword_clustering/` and run via `scripts/run_clustering.py` — there is no external `keyword-cluster` CLI. `scripts/setup_env.py` builds a venv from `scripts/requirements.txt`. Helpers: `scripts/crawl_pages.py` (page enrichment) and `scripts/build_dashboard.py` (the offline dashboard). Skill-specific additions over the base engine: page-type classification (`keyword_clustering/page_types.py`), intent×page-type-aware mapping (`scoring.map_keywords_to_pages`), and the structured architecture plan (`keyword_clustering/architecture.py` → `architecture.json`).

## Engine Inputs

`run_clustering.py` takes these inputs:

| Flag | Required | Schema | Notes |
|---|---|---|---|
| `--keywords` | Yes | CSV with at least a `keyword` column | Extra columns (`search_volume`, `keyword_difficulty`, `current_url`, `serp_urls`, …) are used for scoring/summaries when present. |
| `--pages` | No | CSV requiring **`url,page_name`** | `page_name` is a short human label/slug. Page-matching text is composed from `page_name + title + h1 + meta_description + headings + body_excerpt`. Without `--pages`, page-mapping is empty. |
| `--topics` | No | CSV with a `topic` column | Seed labels to guide cluster naming. |
| `--serp-file` | No | CSV (`keyword,position,url,title`) | Enables SERP-overlap similarity / cannibalisation signals. |

**Enriching the pages CSV:** `python scripts/crawl_pages.py --pages <in>.csv --output <out>.csv` fetches each `url` and appends `title`, `meta_description`, `h1`, `headings`, `body_excerpt`, `canonical_url`, `word_count`, `status_code`. The input needs only a `url` column; `page_name` is preserved/derived so the enriched output still satisfies `--pages`. The run folds these fields into the page text **and** uses URL/title to classify each page's type (`service/landing/blog/guide/news/tool/nav`); a `page_type` column in the CSV overrides the heuristic.

**Mode (`--mode`)**: `optimise_only` (map to existing pages, propose nothing), `optimise_expand` (existing + propose new pages and architecture), `greenfield` (design from scratch). `--focus-file focus.json` drops off-service keywords (its `exclude` list) before clustering and marks matching clusters `deprioritise`.

**Architecture output**: `architecture.json` → `{clusters: [{cluster_id, cluster_label, primary_intent, action (create|optimise|consolidate|gap|deprioritise), target_page_type, target, role (hub|spoke), parent, search_volume, supporting_cluster_ids, rationale}]}`. The skill narrates this into `proposed-architecture.md`. `dashboard.html` combines every chart (Plotly inlined, offline) + rendered reports.

---

## Engine Output Schema

The package writes the following files into the `--output` directory. **Filenames are exact** — earlier drafts of this skill used `page_map.csv` / `gap_report.csv`, which the package does **not** produce.

---

### clustered_keywords.csv

The full enriched keyword frame — every input keyword plus the columns the pipeline adds. Common columns:

| Column | Type | Description |
|---|---|---|
| `keyword` | string | The input keyword (unchanged) |
| `cluster_id` | integer | Numeric cluster ID (0-based; `-1` = noise under hdbscan) |
| `cluster_label` | string | Human-readable label inferred from top keywords |
| `primary_intent` | string | Classified intent |
| `recommended_page` / `recommended_url` | string | Best-matching existing page label / URL (when `--pages` supplied) |
| `page_similarity_score` | float | Similarity of keyword to its best page (0–1) |
| `match_confidence` | string/float | Mapping confidence band |
| `content_gap` | bool | True when no page meets the match threshold |
| `search_volume` | integer | From input CSV (if provided) |
| `keyword_difficulty` | float | From input CSV (if provided) |
| `opportunity_score` | float | Composite score computed by the pipeline |

---

### keyword_page_map.csv

One row **per keyword** with its best-matching existing page. (Not per-cluster — aggregate by `cluster_label` for a cluster-level view.)

| Column | Type | Description |
|---|---|---|
| `keyword` | string | The keyword |
| `recommended_page` | string | `page_name` of the best-matching page. Empty if none. |
| `recommended_url` | string | URL of the best-matching page |
| `page_similarity_score` | float | Similarity of keyword to that page (0–1) |
| `match_confidence` | string/float | Confidence band for the match |
| `cluster_label` | string | The keyword's cluster label |
| `primary_intent` | string | Classified intent |

**Similarity interpretation (rule of thumb):**
- **≥ 0.7** — Strong match. The page explicitly targets this keyword/cluster. Action: optimise.
- **0.4–0.69** — Weak match. The page incidentally covers it. Action: optimise or create a dedicated page.
- **< 0.4** — No match / GAP (surfaces in `content_gap_report.csv`). Action: create.

---

### content_gap_report.csv

Keywords flagged as content gaps (no existing page meets the match threshold) — content-creation opportunities. One row **per keyword**; roll up by `cluster_label` and sum `search_volume` to prioritise.

| Column | Type | Description |
|---|---|---|
| `keyword` | string | The gap keyword |
| `cluster_label` | string | Its cluster label |
| `primary_intent` | string | Classified intent |
| `search_volume` | integer | Monthly volume (if provided in input) |
| `keyword_difficulty` | float | Difficulty (if provided in input) |
| `opportunity_score` | float | Composite opportunity score |
| `page_similarity_score` | float | Similarity to the closest existing page (low ⇒ genuine gap) |

---

### cannibalization_report.csv

Clusters where multiple existing pages compete, risking ranking dilution. One row **per detected conflict**.

| Column | Type | Description |
|---|---|---|
| `cluster_id` | integer | Cluster ID where the conflict was detected |
| `cluster_label` | string | Cluster label |
| `cannibalization_type` | string | `ranking_cannibalization` (multiple `current_url`s) or `mapping_conflict` (multiple `recommended_page`s) |
| `detail` | string | Comma-separated competing URLs, optionally suffixed with `\| avg_serp_overlap=<score>` |
| `keyword_count` | integer | Keywords in the affected cluster |

---

### cluster_summary.csv

One row per cluster with aggregate statistics. Columns are generated from the aggregation, so exact names depend on which input columns were present:

| Column | Type | Description |
|---|---|---|
| `cluster_id` | integer | Cluster ID |
| `cluster_label` | string | Human-readable label |
| `keyword_count` | integer | Keywords in cluster (`keyword_count`) |
| `top_keywords` | string | Comma-separated top 5 keywords |
| `search_volume_sum` | integer | Total monthly volume (present if `search_volume` was in input) |
| `search_volume_mean` | float | Mean volume (present if `search_volume` was in input) |
| `keyword_difficulty_mean` | float | Mean difficulty (present if `keyword_difficulty` was in input) |
| `opportunity_score_mean` | float | Mean opportunity score (present if `opportunity_score` was computed) |

---

### cluster_quality_report.csv

Per-cluster quality diagnostics (silhouette and intra-cluster similarity, sizes, outliers). Surface these metrics when a run looks degenerate (1–2 clusters, many singletons) — never fabricate quality numbers.

---

### recommendations.md

Free-text markdown generated by the package: per-cluster recommended page, primary intent, top keywords, and an opportunity rationale. Always incorporate this file's content into the Web Lifter report rather than replacing it.

---

## Clustering Method Selection Guide

| Method | Best For | Requires Cluster Count? | Speed | Notes |
|---|---|---|---|---|
| `kmeans` | General-purpose; balanced clusters | `--clusters N`, or `--auto-k silhouette` | Fast | Default method. Sensitive to initialisation. `--clusters` is an integer only. |
| `agglomerative` | Hierarchical exploration; dendrogram analysis | `--clusters N`, or `--auto-k silhouette` | Medium | Better for understanding sub-clusters. Higher memory use. |
| `hdbscan` | Unknown cluster count; noise-tolerant | Auto (tune `--min-cluster-size`) | Medium | Assigns outlier keywords to noise cluster (-1). `--clusters` ignored. Best for messy lists. |
| `graph` | SERP-overlap-based clustering | Auto (community detection) | Slow | Most accurate for commercial intent; requires SerpAPI. `--clusters` ignored. |

> `--auto-k silhouette` searches `--k-min`..`--k-max` (default 4–40) and picks the best silhouette. There is no `--clusters auto`.

---

## Embedding Model Selection

Embeddings only apply when `--similarity` is `semantic` or `hybrid` (the default is `tfidf`, which uses no embedding model). `--embedding-model` (alias `--embedding`) accepts these **presets** (from `ST_PRESETS`); any other value is treated as a literal Hugging Face model id and will be downloaded on first use:

| Preset | Resolves to | Download | Quality | Best For |
|---|---|---|---|---|
| `tfidf` (default) | — (lexical) | No | Baseline | Fast lexical runs; no model needed |
| `mini` | `all-MiniLM-L6-v2` | First use | Good | Small/fast English semantic runs |
| `mpnet` | `all-mpnet-base-v2` | First use | Better | **Recommended** semantic default — higher quality |
| `e5-small` / `e5-base` | `intfloat/e5-small-v2` / `e5-base-v2` | First use | Good–Better | Retrieval-style embeddings |
| `bge-small` / `bge-base` | `BAAI/bge-small-en-v1.5` / `bge-base-en-v1.5` | First use | Good–Better | Alternative English embeddings |

There is **no OpenAI embedding option**. Passing an unrecognised name like `MiniLM` (note the casing — the preset is `mini`) is forwarded as an invalid HF id and fails when offline. Example semantic invocation: `--similarity semantic --embedding-model mpnet`.

---

## Handoff.json Schema

Written to `.project/.marketing-os/seo/clusters/<slug>/handoff.json`.

```json
{
  "slug": "string — URL-safe identifier derived from business/campaign name",
  "method": "string — kmeans | agglomerative | hdbscan | graph",
  "cluster_count": "integer — actual clusters produced (may differ from requested N)",
  "csv_paths": {
    "keywords": "absolute path to input keywords CSV",
    "clustered_keywords": "absolute path to clustered_keywords.csv",
    "keyword_page_map": "absolute path to keyword_page_map.csv",
    "content_gap_report": "absolute path to content_gap_report.csv",
    "cannibalization_report": "absolute path to cannibalization_report.csv",
    "cluster_summary": "absolute path to cluster_summary.csv"
  },
  "generated_at": "ISO 8601 datetime string"
}
```

Consumed by: `content-brief-generator`, `internal-linking-planner`, `content-gap-analysis`.

---

## Content Action Decision Matrix

| Page Map Status | Recommended Action | Priority |
|---|---|---|
| Strong match (≥ 0.7), page performing well | Monitor — no action needed | Low |
| Strong match (≥ 0.7), page underperforming | Optimise on-page: title, headings, content depth | High |
| Weak match (0.4–0.69) | Create a dedicated page or significantly expand existing | Medium |
| No match / GAP | Create new content targeting the cluster | Based on volume |
| Multiple pages matched | Investigate cannibalisation; consolidate or differentiate | High (if confirmed) |
