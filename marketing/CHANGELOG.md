# Changelog

## [2.1.2] - 2026-06-20

### Changed
- **Output paths moved to `.project/.marketing-os/seo/`.** All 19 skills now write their artefacts under `.project/.marketing-os/seo/` instead of `.project/marketing/.seo/` (sub-folders `audits/`, `reports/`, `data/`, `scaffolds/`, `plans/`, `briefs/`, `clusters/`, `keywords/`, `serp-analysis/`, `cwv/` preserved). Aligns the SEO toolkit with the shared `.project/.marketing-os/` marketing workspace namespace. The change spans every SKILL.md output directive and in-body path reference, plus the supporting `reference.md`, templates, the `content-strategist` agent, and example outputs. Cross-skill handoffs (keyword-list-developer → keyword-clustering-and-mapping → content-brief-generator / content-gap-analysis / internal-linking-planner) updated in lockstep so they continue to resolve.

## [2.1.1] - 2026-06-03

### Changed
- **Output paths namespaced under `.project/marketing/.seo/`.** All skill artefacts that previously wrote to top-level `.project/{reports,audits,scaffolds,data,plans}/` now write under `.project/marketing/.seo/` (sub-folders preserved). Output artefacts previously under `${CLAUDE_PLUGIN_DATA}` (`keywords/`, `clusters/`, `serp-analysis/`, `cwv/`) also move to `.project/marketing/.seo/`. Credentials (`credentials.json`), the bundled clustering venv, and caches remain in `${CLAUDE_PLUGIN_DATA}` so runtime/auth is unaffected.

## [2.1.0] - 2026-06-03

### Added
- **`keyword-clustering-and-mapping` is now fully self-contained.** The clustering engine is vendored under `skills/keyword-clustering-and-mapping/scripts/keyword_clustering/` and run locally via `scripts/run_clustering.py` — no external `keyword-cluster` CLI or network API. `scripts/setup_env.py` builds a venv from `scripts/requirements.txt` (degrades to tf-idf if `sentence-transformers` is unavailable). Helpers: `scripts/crawl_pages.py`, `scripts/build_dashboard.py`.
- **Page-type & intent-aware page mapping** (`keyword_clustering/page_types.py` + `scoring.map_keywords_to_pages`). Every page is classified (`service/landing/blog/guide/news/tool/nav`) and commercial keywords are steered to service/landing pages and kept off blog/news/tool pages. A commercial cluster with no compatible page now becomes a genuine gap instead of being mis-mapped to whichever article has the richest body text.
- **Structured site-architecture plan** (`keyword_clustering/architecture.py` → `architecture.json`): per-cluster `action` (create/optimise/consolidate/gap/deprioritise), target page type, hub/spoke role, URL slug, volume, and rationale. Narrated into `proposed-architecture.md`.
- **Clustering-mode gate** (`AskUserQuestion`): `optimise_only`, `optimise_expand` (recommended), `greenfield`.
- **Single offline `dashboard.html`** combining every chart (Plotly inlined — opens with no internet) plus rendered reports and data previews. Raw CSV/HTML/brief files are preserved.
- **`keyword-list-developer` focus/exclusion gate**: a structured `AskUserQuestion` capturing services to prioritise/exclude, locale, and intent, persisted to `focus.json` and applied as a hard negative filter — stops off-service keywords (e.g. services the business doesn't offer) entering the list. The clustering skill re-applies `focus.json` via `--focus-file`.

### Fixed
- **Opportunity matrix no longer renders empty.** The engine now aliases `volume→search_volume` and `difficulty→keyword_difficulty`, and `plot_opportunity_matrix` tolerates either column name and shows a placeholder instead of an empty plot when difficulty data is absent.
- Plotly marker sizes clip negative "unknown" sentinels (`-1`) that previously crashed chart generation on real provider data.
- De-duplicated page-brief slugs (`api---integration-api---integration.md` → `api-integration.md`).

## [2.0.1] - 2026-06-03

### Fixed
- **`keyword-clustering-and-mapping` skill now matches the real `keyword-cluster` CLI.** Earlier docs described an interface the package does not have, so runs failed or produced no usable mapping:
  - `--pages` requires `url,page_name` columns (was wrongly documented as `url,title,h1,meta_description,word_count`).
  - Documented the `crawl` / `enrich-pages` subcommand that enriches a pages CSV with `title`/`meta_description`/`h1`/`headings`/`body_excerpt`, which the run folds into page-matching text to sharpen mapping.
  - Cluster count: `--clusters` is an integer only (default 8); automatic selection is `--auto-k silhouette` for kmeans/agglomerative. Removed the invalid `--clusters auto`.
  - Embedding presets corrected to the real `ST_PRESETS` (`tfidf` default, `mini`→all-MiniLM-L6-v2, `mpnet`→all-mpnet-base-v2, `e5-*`, `bge-*`); semantic embeddings require `--similarity semantic|hybrid`. Removed the non-existent `MiniLM`/`multilingual-MiniLM`/`OpenAI` options and the bogus OpenAI-key prerequisite.
- **Corrected output filenames and schemas** across SKILL.md, reference.md, the content-strategist agent, templates, and examples: `page_map.csv`→`keyword_page_map.csv` (per-keyword) and `gap_report.csv`→`content_gap_report.csv` (per-keyword), plus the real columns for `cannibalization_report.csv` and `cluster_summary.csv`, and documented `cluster_quality_report.csv`.
- **`internal-linking-planner` and `keyword-list-developer`** updated to reference the correct output filenames and the `--auto-k silhouette` invocation, so cross-skill handoffs resolve to files that actually exist.

## [2.0.0] - 2026-06-02

### Changed (BREAKING)
- **Credentials are now a single plaintext JSON file.** All providers read from `~/.claude/plugins/data/marketing/credentials.json` (or `$CLAUDE_PLUGIN_DATA/credentials.json`, or `$SEO_CREDENTIALS_FILE`). Per-provider environment variables (`SERPAPI_KEY`, `DATAFORSEO_LOGIN`/`DATAFORSEO_PASSWORD`, `AHREFS_API_KEY`, `MOZ_ACCESS_ID`/`MOZ_SECRET`, `PSI_API_KEY`) still override the file. No encryption, no passphrase, no OAuth, no setup wizard.
- `/marketing:seo-status` now reports which providers are configured (presence only) by reading the credentials file.

### Removed (BREAKING)
- The encrypted Fernet vault (`seo_vault.py`), the `seo_vault_passphrase` `userConfig` option, and the passphrase plumbing.
- OAuth providers **Google Search Console (GSC)** and **Google Analytics 4 (GA4)** — `gsc_client.py`, `ga4_client.py`, `oauth_gsc.py`, `oauth_ga4.py`, and the `gsc-performance-report` skill (skill count 20 → 19).
- The `/marketing:seo-connect` and `/marketing:seo-disconnect` wizard commands, and `token_validator.py`.
- Dependencies `cryptography`, `filelock`, `google-auth`, `google-auth-oauthlib`, `google-api-python-client` (no longer needed).

### Added
- `scripts/lib/credentials.py` — tiny plaintext credential loader (file + env-var fallback).
- `scripts/seo_status.py` and the `/marketing:seo-setup` command to create and inspect the credentials file.
- `credentials.example.json` template at the plugin root.

### Migration
Create `~/.claude/plugins/data/marketing/credentials.json` (run `/marketing:seo-setup`) and paste your API keys in. Any credentials previously stored in the encrypted vault must be re-entered — the old `tokens.enc` is no longer read and can be deleted.

## [1.1.2] - 2026-06-02

### Fixed
- Credentials stored via `/marketing:seo-connect` could not be read back at runtime — every provider reported its key as missing. The vault passphrase was read from `SEO_VAULT_PASSPHRASE`, an environment variable nothing in the skill/command runtime ever set, while the documented `seo_vault_passphrase` plugin option was never declared.

### Added
- `seo_vault_passphrase` is now declared as a `userConfig` option, so Claude Code prompts for it at enable time, stores it in the OS keychain, and injects it into every plugin subprocess as `CLAUDE_PLUGIN_OPTION_SEO_VAULT_PASSPHRASE`.
- `resolve_passphrase()` helper in `seo_vault.py` — single source of truth that reads `CLAUDE_PLUGIN_OPTION_SEO_VAULT_PASSPHRASE`, falling back to `SEO_VAULT_PASSPHRASE` for hooks/tests/CI.

### Changed
- All provider clients (SerpAPI, DataForSEO, Ahrefs, Moz, GSC, GA4) and `token_validator.py` now resolve the passphrase via `resolve_passphrase()` instead of reading `SEO_VAULT_PASSPHRASE` directly.
- `token_validator.py` and the `seo_vault.py` CLI accept an optional `--passphrase` argument; commands now pass the passphrase explicitly rather than relying on environment propagation between processes.

## [1.0.0] - 2026-05-20

### Added
- Initial release. 17 skills covering keyword research + list development + clustering/mapping, SERP analysis, competitor + on-page + technical audits, Core Web Vitals, backlinks, content gap analysis, content briefs, internal-link planning, schema generation, GSC performance reporting, local SEO, redirect mapping, broken-link scanning.
- 3 sub-agents: `seo-auditor`, `serp-analyst`, `content-strategist`.
- 3 slash commands: `/marketing:seo-connect`, `/marketing:seo-status`, `/marketing:seo-disconnect`.
- SessionStart hooks (`ensure-venv.sh`, `check-credentials.sh`) + Stop hook (`suggest-related.sh`).
- Encrypted Fernet vault for SerpAPI, DataForSEO, Ahrefs, Moz, PageSpeed Insights, GSC OAuth, GA4 OAuth credentials.
- `keyword-clustering-and-mapping` skill wraps the external [keyword-clustering](https://github.com/johnoconnor0/keyword-clustering) package.
