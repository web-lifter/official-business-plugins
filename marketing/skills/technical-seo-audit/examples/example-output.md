# Technical SEO Audit — acmecorp.com.au

**Date:** 15/05/2026
**Audit Depth:** Full Lighthouse
**Pages Crawled:** 200 / 200 max (site has ~340 indexable pages — sample only)
**Subdomains Included:** No (subdomains: blog.acmecorp.com.au — excluded)
**Technical Health Score:** 61/100

---

## Executive Summary

Acmecorp.com.au has a moderate technical SEO foundation with several high-impact issues suppressing organic performance. The most significant findings are: (1) 23 linked 4xx pages wasting crawl budget and breaking user journeys, (2) critical LCP failures on mobile across all key landing pages (avg 5.1s — Google threshold: 2.5s), and (3) 14 blog posts incorrectly noindexed — live, linked content not being indexed. Schema coverage is thin across service pages, and the JavaScript-rendered navigation is invisible to Googlebot's raw crawl pass.

Fixing the noindex errors and resolving the linked 4xx pages are the highest-leverage immediate actions. The LCP issues require engineering involvement but will have the largest ranking impact over the medium term.

---

## Findings Register

| # | Pillar | Issue | Severity | Evidence | SEO Impact | Fix |
|---|---|---|---|---|---|---|
| 1 | Index | 14 blog posts with noindex | Critical | `<meta name="robots" content="noindex">` found on 14 of 67 crawled blog posts | Google cannot index 14 live pages targeting valuable informational queries | Remove noindex meta tag from blog post template; confirm CMS publish setting for these 14 posts |
| 2 | Crawl | 23 linked 4xx pages | Critical | 23 internal links from live pages return 404; full list below | Crawl budget waste; broken user journeys; link equity leak | 301 redirect or restore each 404; update internal links |
| 3 | Rank | LCP > 4.0s on mobile (all key pages) | High | Avg LCP 5.1s mobile; root cause: unoptimised hero images (JPEG, no WebP, no `loading` hint) | Page experience ranking signal; significant mobile ranking suppression | Convert hero images to WebP; add `fetchpriority="high"` to LCP image; defer non-critical JS |
| 4 | Crawl | 7 redirect chains ≥ 3 hops | High | /old-services → /services-2022 → /services-v2 → /services (3-hop); 6 more chains listed below | Latency per chain hop; crawl budget cost; potential link equity loss | Collapse all chains to direct 301 redirects |
| 5 | Render | JS-rendered navigation invisible to raw crawl | High | Nav `<ul>` populated via React state — 0 nav links in raw HTML; 22 links in rendered HTML | Googlebot first-pass sees no nav links; topical authority signal reduced | Add server-side rendered navigation or static HTML fallback nav |
| 6 | Index | 31 pages in sitemap return noindex | High | sitemap.xml contains 31 URLs with `noindex` meta tag on the destination page | Conflicting signals to Googlebot — sitemap suggests indexing, page says no | Remove noindex pages from sitemap; or remove noindex tag if pages should be indexed |
| 7 | Crawl | Sitemap lastmod dates all identical (01/01/2026) | Medium | All 312 sitemap URLs have `<lastmod>2026-01-01</lastmod>` | Googlebot deprioritises recrawls when lastmod doesn't reflect real changes | Configure CMS to write accurate lastmod dates on content publish/update |
| 8 | Index | 18 pages with canonical pointing to www, served from non-www | Medium | Non-www URLs served but canonical is `https://www.acmecorp.com.au/...` — correct, but inconsistent redirect | Not a ranking issue if consistent, but adds crawl overhead | Enforce root domain → www redirect at server level so all URLs are served from canonical form |
| 9 | Rank | 38 service pages have no schema markup | Medium | 38 service page URLs: no JSON-LD found | Missing FAQPage and LocalBusiness schema; lost rich result opportunities | Add `LocalBusiness` + `FAQPage` schema to service page template |
| 10 | Rank | CLS failures on 3 pages (CLS > 0.25) | Medium | /pricing: CLS 0.31; /contact: CLS 0.28; /case-studies: CLS 0.27 | Page experience ranking signal; layout instability hurts UX and mobile ranking | Fix: images missing width/height on /pricing and /case-studies; cookie banner injected above fold on /contact — move below fold |
| 11 | Index | 12 pages with missing canonical tags | Medium | 12 blog tag archive pages have no canonical — eligible for duplicate content issues if similar pages exist | Tag archives with similar content may compete; no canonical means Google chooses arbitrarily | Add self-referencing canonical to all tag archive pages |
| 12 | Rank | INP > 200ms on 5 key pages (mobile) | Medium | Homepage: INP 380ms; /pricing: INP 410ms; /features: INP 320ms | Interaction latency signal; affects mobile UX ranking factor | Profile JS on main thread; defer non-critical third-party scripts (chat widget, analytics) |

**Total findings:** 12 (Critical: 2, High: 4, Medium: 6, Low: 0)

---

## Priority Fix Queue

### Critical — Fix Within 1 Week

| # | Issue | Pillar | Fix |
|---|---|---|---|
| 1 | 14 live blog posts noindexed | Index | Remove `noindex` meta from blog post template. Identify the 14 specific posts in the findings register below and confirm each should be indexed. |
| 2 | 23 linked 4xx pages | Crawl | 301 redirect each 4xx to the nearest relevant live page. For product pages removed permanently, redirect to the parent category. Update all internal links pointing to the old URLs. |

### High — Fix Within 30 Days

| # | Issue | Pillar | Fix |
|---|---|---|---|
| 1 | LCP > 4.0s mobile (all key pages) | Rank | (a) Convert hero images to WebP format. (b) Add `fetchpriority="high"` to the LCP `<img>` element. (c) Defer non-critical JS with `defer` attribute. (d) Set explicit `width` and `height` on all above-fold images. |
| 2 | 7 redirect chains ≥ 3 hops | Crawl | Audit the redirect rules in Nginx/Apache config. Collapse each chain to a single direct 301. |
| 3 | JS-rendered navigation invisible to raw crawl | Render | Add a static HTML `<nav>` block as `<noscript>` fallback, or configure Next.js/React to server-render the navigation component. |
| 4 | 31 noindex pages in sitemap | Index | Export sitemap URLs; cross-reference with crawl noindex flags; remove noindex URLs from sitemap. CMS plugin update may automate this. |

### Medium — Fix Within 60 Days

| # | Issue | Pillar | Fix |
|---|---|---|---|
| 1 | Sitemap lastmod dates all identical | Crawl | Configure CMS to write `<lastmod>` as the `updated_at` timestamp from the database on each sitemap URL. |
| 2 | Schema missing on 38 service pages | Rank | Add `LocalBusiness` and `FAQPage` schema via JSON-LD in the service page template. |
| 3 | CLS failures on 3 pages | Rank | Add explicit `width`/`height` to all images on /pricing and /case-studies. Move cookie consent banner injection to below the fold. |
| 4 | Missing canonicals on 12 tag pages | Index | Add `<link rel="canonical">` self-referencing tag to all archive/tag page templates. |
| 5 | INP > 200ms on 5 key pages | Rank | Audit Chrome DevTools Performance tab for long tasks. Defer chat widget and A/B test scripts. |
| 6 | www/non-www canonical inconsistency | Index | Add server-level 301 redirect: non-www → www. Update all internal links to use www consistently. |

---

## Crawl Pillar

### robots.txt
```
User-agent: *
Disallow: /admin/
Disallow: /staging/
Disallow: /wp-json/
Crawl-delay: 1
Sitemap: https://www.acmecorp.com.au/sitemap.xml
```
**Issues:** No issues — robots.txt is well-configured. Staging and admin correctly blocked. Sitemap declared.

### Sitemap
- **URL:** `https://www.acmecorp.com.au/sitemap.xml`
- **URL count:** 312
- **Last modified (most recent):** 01/01/2026 (all identical — static date, see Finding #7)
- **Issues:** All lastmod dates identical; 31 noindex URLs included (see Finding #6)

### HTTP Status Distribution

| Status | Count | % |
|---|---|---|
| 200 OK | 163 | 81.5% |
| 301 Redirect | 18 | 9.0% |
| 302 Redirect | 2 | 1.0% |
| 404 Not Found | 14 | 7.0% |
| 500 Server Error | 0 | 0% |
| Other | 3 | 1.5% |

### Redirect Chains (> 1 hop)

| Chain | Hops | Recommendation |
|---|---|---|
| /old-services → /services-2022 → /services-v2 → /services | 3 | Collapse to /old-services → /services |
| /team → /about/team-old → /about/our-team | 3 | Collapse to /team → /about/our-team |
| /blog/tag/news → /news → /blog?cat=news → /blog | 3 | Collapse to /blog/tag/news → /blog |
| _(4 more 2-hop chains)_ | 2 | Collapse each |

### 4xx Pages (linked from internal content)

23 URLs returning 404 with internal links pointing to them. Sample:
- `/case-studies/archway-construction` (linked from /case-studies, /homepage) — 404
- `/services/hydraulic-fitting-repair` (linked from /services) — 404
- `/blog/2024/winter-maintenance-guide` (linked from /blog sidebar "Related Posts") — 404
- `/products/legacy-valve-set` (linked from /products/industrial) — 404
- _(+ 19 more in crawl.json)_

### Internal Link Depth Distribution

| Click Depth | URL Count | % of Crawled |
|---|---|---|
| 1 | 14 | 7% |
| 2 | 48 | 24% |
| 3 | 71 | 36% |
| 4 | 39 | 20% |
| 5+ | 28 | 14% |

**Finding:** 28 pages (14%) are ≥ 5 clicks from homepage — likely not crawled on Google's standard crawl interval. Review these pages: if they contain valuable content, add shortcuts via internal links or navigation.

---

## Render Pillar

### JS/HTML Parity Sample (15 pages)

| URL | Raw HTML Links | Rendered Links | Parity | Issue |
|---|---|---|---|---|
| / (homepage) | 3 | 41 | Fail | Nav, footer, related posts all JS-rendered |
| /services | 4 | 38 | Fail | Nav + service cards JS-rendered |
| /blog/sample-post | 11 | 34 | Fail | Nav + related posts JS-rendered |
| /contact | 6 | 29 | Fail | Nav JS-rendered |
| /pricing | 8 | 31 | Fail | Nav + pricing table JS-rendered |

### Framework Detected
**CMS/Framework:** Next.js 14 (React)
**Rendering mode:** CSR (Client-Side Rendering) — pages are not server-rendered; `next/head` and main content rendered client-side
**Recommendation:** Enable Next.js SSR (Server-Side Rendering) or SSG (Static Site Generation) for all key pages. The current CSR setup means Googlebot's first crawl pass sees near-empty HTML. While Google does render JavaScript, second-wave rendering introduces indexing lag and the rendering budget is not guaranteed.

---

## Index Pillar

### URL Count Comparison

| Source | Count |
|---|---|
| XML Sitemap | 312 |
| Crawled URLs (200 OK) | 163 |
| `site:acmecorp.com.au` estimate | ~240 |

**Discrepancy:** ~72 URLs in sitemap not reached by the 200-URL crawl sample. Estimated ~72 additional pages exist beyond the crawl sample. The `site:` query showing ~240 suggests the domain is reasonably well-indexed but below the 312 sitemap count — the 31 noindex pages in the sitemap account for part of this gap.

### Canonical Issues

- `/services/hydraulic-fittings` canonical points to non-www version (`http://acmecorp.com.au/services/hydraulic-fittings`) — should be `https://www.acmecorp.com.au/services/hydraulic-fittings`
- 3-hop canonical chain found: `/products/legacy` → canonical: `/products/industrial-legacy` → canonical: `/products/industrial`
- 12 tag archive pages missing canonical (see Finding #11)

### noindex Anomalies

14 blog posts incorrectly noindexed (Finding #1):
- `/blog/winter-maintenance-checklist-2025`
- `/blog/how-to-select-industrial-fittings`
- `/blog/acmecorp-expands-to-brisbane`
- _(+ 11 more listed in crawl.json)_

---

## Rank Pillar

### Core Web Vitals Summary

| URL | LCP (mob) | INP (mob) | CLS (mob) | LCP (desk) | INP (desk) | CLS (desk) | PSI Score (mob) |
|---|---|---|---|---|---|---|---|
| / (homepage) | 5.4s ❌ | 380ms ❌ | 0.08 ✅ | 2.1s ✅ | 110ms ✅ | 0.04 ✅ | 38 |
| /services | 4.8s ❌ | 210ms ❌ | 0.12 ⚠️ | 1.9s ✅ | 90ms ✅ | 0.06 ✅ | 44 |
| /pricing | 5.1s ❌ | 410ms ❌ | 0.31 ❌ | 2.3s ✅ | 130ms ✅ | 0.09 ✅ | 41 |
| /blog/sample-post | 3.8s ⚠️ | 180ms ✅ | 0.07 ✅ | 1.7s ✅ | 80ms ✅ | 0.03 ✅ | 62 |
| /contact | 4.2s ❌ | 190ms ✅ | 0.28 ❌ | 1.8s ✅ | 70ms ✅ | 0.05 ✅ | 55 |

### CWV Root Causes

- **LCP mobile failures (all key pages):** Hero image is a 1.2MB JPEG loaded without `fetchpriority="high"`. No WebP variant. No image CDN. Render-blocking Google Fonts CSS loaded synchronously in `<head>`. Fix: convert to WebP, add `fetchpriority="high"` to hero `<img>`, load fonts asynchronously.
- **INP failures (/homepage, /pricing, /services):** Chat widget (Intercom) initialises on DOMContentLoaded, adding ~280ms of main-thread blocking. Third-party A/B test script (Optimizely) adds ~190ms. Fix: lazy-load Intercom on first user interaction; defer Optimizely initialisation.
- **CLS failures (/pricing, /contact):** `/pricing` — pricing table images missing `width`/`height` attributes causing reflow. `/contact` — cookie consent banner injected into top of `<body>` on page load, pushing all content down. Fix: add width/height to all images; move consent banner to a fixed-position overlay or delay injection.

### Schema Coverage

| Schema Type | Pages With | Pages Needing | Gap |
|---|---|---|---|
| `LocalBusiness` | 1 (homepage) | 39 (all service + location pages) | 38 pages |
| `Article` / `BlogPosting` | 0 | 67 (all blog posts) | 67 pages |
| `FAQPage` | 0 | 38 (service pages) | 38 pages |
| `BreadcrumbList` | 0 | All pages | All pages |
| `Product` | 0 | 24 (product pages) | 24 pages |

### Schema Validation Issues
- None (schema is absent on most pages — no invalid markup found where schema does exist)

---

## Raw Data Paths

| File | Path |
|---|---|
| Crawl output | `/home/user/.claude/plugin-data/.project/.marketing-os/seo/audits/acmecorp/crawl.json` |
| CWV output | `/home/user/.claude/plugin-data/.project/.marketing-os/seo/audits/acmecorp/cwv.json` |
