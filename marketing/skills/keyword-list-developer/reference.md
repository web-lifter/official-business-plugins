# Keyword List Developer — Reference

## Master CSV Output Schema

The `keyword-list-developer` output CSV is the **canonical input** for the `keyword-clustering` package. The schema is fixed — the clustering CLI (`keyword-cluster run --keywords <file>`) expects these exact column names in this exact order.

### Column Definitions

| Column | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Normalised keyword (lowercase, trimmed) |
| `volume` | integer or -1 | Yes | Monthly search volume (12-month average). Use `-1` if estimated/unavailable |
| `difficulty` | integer 0–100 | Yes | Keyword difficulty score. Use `-1` if unavailable |
| `intent` | string | Yes | `Informational` / `Navigational` / `Commercial` / `Transactional` |
| `parent_topic` | string | Yes | Broadest parent keyword satisfying the same need |
| `source` | string | Yes | Data origin — see source codes below |
| `current_url` | string or empty | Yes | Existing page on the client domain ranking in top 20 for this keyword. Empty string if none |
| `serp_features` | string | Yes | Pipe-delimited list of SERP features present for this keyword. Empty string if unknown |

**Column order in CSV must be exactly:** `keyword,volume,difficulty,intent,parent_topic,source,current_url,serp_features`

### Source Code Reference

| Source Code | Origin |
|---|---|
| `serpapi-related` | SerpAPI related_searches array |
| `serpapi-paa` | SerpAPI people_also_ask array |
| `dataforseo-suggest` | DataForSEO keywords_for_keywords endpoint |
| `dataforseo-volume` | DataForSEO search_volume endpoint (keyword was already in list, enriched with volume) |
| `dataforseo-site` | DataForSEO keywords_for_site endpoint |
| `gsc-top-queries` | Google Search Console top queries export |
| `competitor-{domain}` | DataForSEO keywords_for_site for a competitor domain (replace {domain} with root domain) |
| `llm-semantic` | LLM-generated semantic expansion |

### SERP Features List

Valid values for the `serp_features` column (pipe-delimited, e.g. `Featured Snippet|PAA|AI Overview`):

- `Featured Snippet`
- `PAA` (People Also Ask)
- `Local Pack`
- `Image Pack`
- `Video Pack`
- `Knowledge Panel`
- `Shopping`
- `Top Stories`
- `Reviews`
- `Sitelinks`
- `AI Overview`

---

## Downstream Package: keyword-clustering

**Package location:** `<keyword-clustering-dir>` (set to your local clone path)
**Install command:** `pip install "keyword-clustering[app,semantic,advanced] @ file:///<keyword-clustering-dir>"`
**CLI entrypoint:** `keyword-cluster`

The master CSV produced by `keyword-list-developer` is passed to the package via:

```bash
keyword-cluster run \
  --keywords .project/.marketing-os/seo/keywords/<slug>-master.csv \
  --pages <pages.csv> \
  --topics <topics.csv> \
  --method <kmeans|agglomerative|hdbscan|graph> \
  --clusters <N> \
  --output .project/.marketing-os/seo/clusters/<slug>/
```

The `--pages` CSV has columns: `url,title,h1,meta_description,word_count`.
The `--topics` CSV has columns: `topic,description` (optional — for seeding cluster labels).

---

## Search Intent Reference (Backlinko Matrix — Abbreviated)

See `keyword-research/reference.md` for the full matrix. Key mappings relevant to master list building:

| Intent | Common Signals | Typical Business Value |
|---|---|---|
| Informational | "how to", "what is", "guide", question phrasing | Top-funnel; brand building; featured snippet opportunity |
| Commercial | "best", "vs", "review", "top", "compare" | Mid-funnel; high purchase intent; comparison content |
| Transactional | "buy", "hire", "near me", "book", "price", "cost" | Bottom-funnel; direct conversion opportunity |
| Navigational | Brand names, "login", "contact" | Retention/direct; minimal content opportunity for non-owners |

---

## Volume Floor Guidelines

| Programme Maturity | Recommended Floor |
|---|---|
| New site / pre-launch | 50–100/month — include long-tails with acquisition potential |
| Established site (< 50K sessions/month) | 100–200/month |
| High-traffic site (> 50K sessions/month) | 200–500/month — focus on competitive terms |
| Niche / specialist market | 20–50/month — low-volume markets often have high intent |

---

## Deduplication Rules

1. **Exact match:** Keep higher-quality source. Priority: dataforseo-volume > dataforseo-suggest > dataforseo-site > serpapi-* > gsc > competitor-* > llm-semantic.
2. **Singular/plural:** Keep the higher-volume form. E.g. "running shoe" vs "running shoes" — keep "running shoes" (2,400 vol).
3. **Hyphenation:** "e-commerce" = "ecommerce" — keep the form with higher volume.
4. **Common misspellings:** Remove misspelling; keep canonical. Log the misspelling in exclusion notes.
5. **Stop-word variants:** "best running shoes for australia" ≈ "best running shoes australia" — keep the shorter canonical form if volumes are within 20%.

---

## List Size Guidelines

| Use Case | Recommended Final Size |
|---|---|
| Single product/service page | 30–80 keywords |
| Single content cluster | 50–150 keywords |
| Full site / content programme | 200–1,000 keywords |
| Enterprise / multi-vertical | 1,000–5,000 keywords (split by vertical) |

The `keyword-clustering` package works best with 100–500 keywords per clustering run. For larger lists, split by intent or parent topic before clustering.
