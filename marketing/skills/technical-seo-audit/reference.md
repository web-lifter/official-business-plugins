# Technical SEO Audit — Reference

## Google Search Pillars: Crawl–Render–Index–Rank

All technical SEO issues map to one of four pillars. This framework helps route fixes to the correct team and prioritise by impact.

| Pillar | Question Google is Asking | Key Signals |
|---|---|---|
| **Crawl** | Can Googlebot discover and fetch the page? | robots.txt, crawl budget, server response codes, redirect chains, internal linking depth |
| **Render** | Can Googlebot see the content after JavaScript executes? | JS-rendered content, lazy loading, `<noscript>` fallbacks, SSR vs CSR |
| **Index** | Should Google store this page in its index? | noindex, canonical tags, duplicate content, thin content, hreflang |
| **Rank** | Does the page deserve to rank for the query? | Core Web Vitals, schema, content quality, backlinks, on-page signals |

A page must pass all four pillars to rank. Failures are cumulative.

---

## robots.txt Interpretation

```
User-agent: *           # Applies to all crawlers
Disallow: /admin/       # Blocks /admin/ and all sub-paths
Disallow: /search?      # Blocks faceted search result pages
Allow: /blog/           # Explicitly allows (overrides broader Disallow above)
Crawl-delay: 2          # Ask crawlers to wait 2 seconds between requests
Sitemap: https://example.com/sitemap.xml  # Declares sitemap location
```

**Common issues:**
- `Disallow: /` — blocks everything. Critical if applied to Googlebot.
- Disallowing CSS or JS files — may prevent rendering; see Render pillar.
- `Crawl-delay` > 5 — may slow indexing on smaller sites unnecessarily.
- Missing `Sitemap:` declaration — not an error, but helpful for crawlers.

---

## Sitemap Quality Checklist

- [ ] Sitemap accessible at root `/sitemap.xml` or declared in robots.txt
- [ ] Sitemap is valid XML (`<urlset>` or `<sitemapindex>` namespace correct)
- [ ] Each `<url>` contains `<loc>` (required) and `<lastmod>` (recommended)
- [ ] `<lastmod>` values are accurate (not all the same date — indicates auto-generated without real modification tracking)
- [ ] No URLs return 4xx/5xx when fetched
- [ ] No URLs that are noindex are included (noindex URLs in sitemap create conflicting signals)
- [ ] URL count ≤ 50,000 per file (Google hard limit)
- [ ] Non-canonical URLs excluded (only include the canonical version of each page)
- [ ] Sitemap index used if > 1 sitemap file

---

## Canonical Tag Rules

```html
<link rel="canonical" href="https://example.com/page/" />
```

**Rules:**
1. Every indexable page should have a self-referencing canonical.
2. Canonical URL must use the correct protocol (https), subdomain (www or non-www, consistent), and trailing slash convention.
3. Paginated pages: canonical should point to the paginated URL itself (not page 1) unless the content is truly a subset.
4. Syndicated content: canonical points to the original source.
5. Canonical chains (A → B → B points to C) — Google resolves but it wastes crawl budget and can cause misattribution.

**Canonical issues severity:**
- Missing canonical → Medium
- Canonical to wrong domain/protocol → High
- Canonical chain > 1 hop → Medium
- noindex page in sitemap with canonical → High (conflicting signals)

---

## Hreflang Rules

Used for multilingual / multi-regional sites. Each page's hreflang set must be consistent:

1. **Reciprocal tags required** — if page A links to page B via hreflang, page B must link back to page A.
2. **Self-referencing** — each page must include its own URL in the hreflang set.
3. **x-default** — include `hreflang="x-default"` for the fallback URL (usually the English/global version).
4. **URLs must be indexable** — hreflang pointing to noindex or 404 URLs is invalid.
5. **Language codes** — use ISO 639-1 language codes + optional ISO 3166-1 country codes: `en`, `en-AU`, `en-US`, `fr-FR`.

---

## Core Web Vitals Thresholds

| Metric | Good | Needs Improvement | Poor |
|---|---|---|---|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 2.5–4.0s | > 4.0s |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 200–500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 0.1–0.25 | > 0.25 |

**Root cause diagnosis:**

| Metric | Common Root Causes |
|---|---|
| **LCP** | Render-blocking CSS/JS, large unoptimised hero image, slow TTFB (server), no resource preloading, third-party script blocking |
| **INP** | Heavy JavaScript on main thread, long tasks (> 50ms), unoptimised event handlers, third-party tag manager scripts |
| **CLS** | Images without explicit `width`/`height` attributes, dynamically injected content above the fold (ads, banners, cookie notices), font-swap without `font-display: swap` |

---

## Mobile-First Indexing Checklist

Google primarily uses the mobile version of content for indexing and ranking:

- [ ] Viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] Same content on mobile and desktop HTML (do not hide content on mobile that is on desktop)
- [ ] Mobile page speed is acceptable (use PSI mobile strategy)
- [ ] Tap targets are adequately sized (minimum 48x48px)
- [ ] No interstitials blocking main content on mobile

---

## Redirect Chain Rules

| Chain Length | Status | Action |
|---|---|---|
| 0 (direct 200) | Ideal | None |
| 1 hop (301/302 → 200) | Acceptable | None (1-hop redirects are normal) |
| 2 hops (A → B → 200) | Warning | Collapse to direct redirect where possible |
| 3+ hops | Issue | Fix — each hop adds latency and crawl budget cost |
| Circular (A → B → A) | Critical | Fix immediately — crawler loop |

**301 vs 302:** Use 301 for permanent redirects (passes link equity). Use 302 for temporary redirects. Incorrect use of 302 for permanent moves means link equity may not pass.

---

## Internal Link Depth Targets

| Page Type | Target Click Depth from Homepage |
|---|---|
| Top service/product pages | ≤ 2 clicks |
| Key blog posts / guides | ≤ 3 clicks |
| Supporting content | ≤ 4 clicks |
| Archive / tag pages | ≤ 5 clicks (accept deeper) |
| Pages > 5 clicks | Flag — may not be crawled regularly |

---

## Technical Health Score Deduction Table

| Severity | Deduction Per Finding |
|---|---|
| Critical | 10 points |
| High | 5 points |
| Medium | 2 points |
| Low | 1 point |

Score starts at 100. Minimum reported score: 0.

| Score Range | Interpretation |
|---|---|
| 90–100 | Strong technical foundation |
| 75–89 | Good, with addressable issues |
| 60–74 | Moderate — technical debt limiting ranking potential |
| 45–59 | Poor — significant issues suppressing organic performance |
| < 45 | Critical — fundamental technical problems, immediate action required |
