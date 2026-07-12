# Competitor SEO Audit — Reference

## Audit Dimensions

The six dimensions of a full competitor SEO audit:

| # | Dimension | Data Source | Phase |
|---|---|---|---|
| 1 | Indexed Footprint | SerpAPI `site:` query | 2 |
| 2 | Content Topics & Keyword Profile | DataForSEO `keywords_for_site` | 3 |
| 3 | Backlink Profile | DataForSEO `backlinks/summary` | 4 |
| 4 | On-Page Patterns | Direct crawl / sampled pages | 5 |
| 5 | Technical Signals | robots.txt, sitemap, crawl samples | 6 |
| 6 | Comparative Matrix | Aggregate of all dimensions | 6 |

---

## DataForSEO Endpoints Used

| Endpoint | Purpose | Key Response Fields |
|---|---|---|
| `POST /dataforseo_labs/google/keywords_for_site/live` | Top keywords ranking for a domain | `keyword`, `rank_group`, `search_volume`, `keyword_difficulty`, `url` |
| `POST /backlinks/summary/live` | Backlink profile summary | `referring_domains`, `rank`, `backlinks`, `referring_ips`, `referring_subnets` |
| `POST /on_page/task_post` | Crawl a domain or URL list | Site structure, meta tags, schema, headings, word count |
| `GET /on_page/pages` | Retrieve crawl results | `url`, `title`, `meta_description`, `h1`, `word_count`, `schema_types`, `canonical` |

---

## Quick Scan vs Full Audit Scope

| Phase | Quick Scan | Full Audit |
|---|---|---|
| Domain intake & health check | Yes | Yes |
| Indexed footprint | Yes | Yes |
| Content topics & keywords | Yes | Yes |
| Backlink profile | No | Yes |
| On-page patterns | No | Yes |
| Technical signals | No | Yes |
| Comparative matrix | Partial (footprint + keywords) | Full (all 6 dimensions) |

---

## Comparative Matrix Template

All metrics must be sourced and dated. Use "—" for unavailable data, not "0".

| Metric | Source | Baseline | Competitor 1 | Competitor 2 | Competitor 3 |
|---|---|---|---|---|---|
| Indexed pages (est.) | SerpAPI site: | | | | |
| Est. organic traffic/month | DataForSEO | | | | |
| Total referring domains | DataForSEO backlinks | | | | |
| Domain authority score | DataForSEO | | | | |
| XML sitemap present | Direct check | | | | |
| Schema types count | Crawl sample | | | | |
| Top content cluster | DataForSEO keywords | | | | |
| Estimated content pieces | Indexed pages / avg sections | | | | |
| Content gap vs baseline | Keyword overlap analysis | | | | |
| HTTPS | Direct check | | | | |

---

## Backlink Profile Interpretation

| Metric | Weak | Average | Strong |
|---|---|---|---|
| Referring domains | < 50 | 50–500 | 500+ |
| Authority score (DataForSEO) | < 20 | 20–50 | 50+ |
| Branded anchor % | > 80% | 50–80% | < 50% (diverse) |
| Top referring domain DR | < 30 | 30–60 | 60+ |

**Anchor text patterns:**
- **Branded dominant (> 70%):** Natural link profile, common for established brands. Limited keyword value.
- **Keyword-rich dominant (> 30%):** May indicate aggressive link building; potential algorithmic risk.
- **Naked URL dominant:** Common for new sites / directory submissions.

---

## Technical Signal Checklist

Items to verify for each domain during Phase 6:

- [ ] `robots.txt` accessible and no broad disallow rules blocking crawlers
- [ ] `sitemap.xml` accessible at root or declared in robots.txt
- [ ] Sitemap contains < 50,000 URLs (Google limit per sitemap file)
- [ ] Sitemap lastmod dates are reasonably recent (< 90 days for active sites)
- [ ] HTTPS enabled (HTTP → HTTPS redirect active)
- [ ] Viewport meta tag present (mobile-first)
- [ ] Schema markup present on key page types (confirm types via crawl sample)
- [ ] Canonical tags present on sample of pages
- [ ] No broad hreflang errors (if multilingual)
- [ ] Redirect chains ≤ 1 hop on sampled URLs

---

## Schema Type Priority Reference

For a typical Australian service business, these schema types are high-value:

| Schema Type | Page Type | SEO Benefit |
|---|---|---|
| `LocalBusiness` / `ProfessionalService` | Homepage, Contact | Local Pack eligibility |
| `Article` / `BlogPosting` | Blog posts, guides | Top Stories; AI Overview citation |
| `FAQPage` | Service pages, guides | PAA eligibility; expanded snippet |
| `BreadcrumbList` | All pages | Breadcrumb display in SERP snippets |
| `Product` | eCommerce PDPs | Rich snippets with price/availability |
| `Review` / `AggregateRating` | Product pages, service pages | Star rating display |
| `HowTo` | Tutorial pages | How-to rich result |

---

## Content Gap Analysis

When comparing competitor keyword profiles against a baseline domain, use this framework:

**Gap types:**
1. **Unique competitor keywords** — competitor ranks for keywords that the baseline does not appear in top 20 for. High priority if volume > 500/month.
2. **Topic cluster gaps** — baseline has no content in a topic cluster that a competitor covers with multiple pages.
3. **Depth gaps** — baseline has one shallow page on a topic; competitor has a hub page + 5 supporting articles (topical authority gap).

**Prioritisation formula (gap score):**
`gap_score = volume × (1 / difficulty) × intent_weight`

Intent weights: Transactional = 1.5, Commercial = 1.2, Informational = 1.0, Navigational = 0.5
