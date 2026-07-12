# marketing

17 skills for end-to-end SEO — research, clustering/mapping, audits, content, reporting.

## Skills

| Skill | Purpose |
|---|---|
| `keyword-research` | Seed → expanded keyword set with intent, volume, difficulty |
| `keyword-list-developer` | Build the canonical master keyword CSV ready for clustering |
| `keyword-clustering-and-mapping` | Cluster keywords + map to pages (wraps the `keyword-clustering` package) |
| `serp-analysis` | SERP feature, intent, and competitor breakdown for a query |
| `competitor-seo-audit` | Deep audit of one or more competitor domains |
| `on-page-audit` | Title/meta/heading/internal-link/schema audit of a page or sitemap |
| `technical-seo-audit` | Crawl/render/index/rank pillars audit |
| `core-web-vitals-report` | LCP/INP/CLS + PSI summary for URL list |
| `backlink-audit` | Referring domains, anchor mix, toxic-link flags |
| `content-gap-analysis` | Keywords competitors rank for that we don't |
| `content-brief-generator` | Single-keyword (or cluster-grounded) editorial brief |
| `internal-linking-planner` | Recommend internal links from cluster topology |
| `schema-markup-generator` | JSON-LD for Article/Product/FAQ/HowTo/LocalBusiness etc. |
| `local-seo-audit` | NAP, GBP, citation, review velocity audit |
| `redirect-map-builder` | Build a 301 map between old + new sitemaps |
| `broken-link-scanner` | Crawl + flag 4xx/5xx and orphan pages |

## Setup

1. Install Python deps: `pip install -r requirements.txt` (the `ensure-venv.sh` SessionStart hook does this automatically).
2. Run `/marketing:seo-setup` to create the credentials file, then paste your SerpAPI / DataForSEO / Ahrefs / Moz / PSI keys into `~/.claude/plugins/data/marketing/credentials.json`. It's a plaintext file — no vault, passphrase, or OAuth.
3. Run `/marketing:seo-status` to verify which providers are configured.

See [`docs/credentials.md`](docs/credentials.md), [`docs/data-sources.md`](docs/data-sources.md), and [`docs/quick-start.md`](docs/quick-start.md) for more.

## Agents

- `seo-auditor` — deep technical + on-page audit specialist (opus).
- `serp-analyst` — SERP feature & intent classifier (sonnet).
- `content-strategist` — topic clustering + content gap reasoning; integrates with the `keyword-clustering` package's output schema.

## Licence

MIT — see [LICENSE](LICENSE).
