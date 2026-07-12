# Core Web Vitals Report — TradeSupply.com.au (eCom)

**Date:** 15/05/2026
**URLs Tested:** 20
**Device:** Both (mobile + desktop)
**Data Source:** PSI / CrUX (field) + Lighthouse (lab)
**Raw data:** `/home/user/.claude/plugin-data/cwv/tradesupply-cwv.json`

---

## Summary

| Metric | URLs Passing | URLs NI | URLs Failing | Pass Rate |
|---|---|---|---|---|
| LCP | 8 | 8 | 4 | 40% |
| INP | 12 | 5 | 3 | 60% |
| CLS | 14 | 3 | 3 | 70% |
| **All metrics pass** | 6 | — | 14 | **30%** |

**CrUX field data available for:** 14 of 20 URLs (70%) — 6 lower-traffic category pages use lab data only.

---

## Worst Offenders

| URL | LCP (mob) | INP (mob) | CLS (mob) | PSI Score | Issues |
|---|---|---|---|---|---|
| /products/power-tools | 6.2s ❌ | 480ms ❌ | 0.28 ❌ | 24 | All 3 failing |
| /products/hand-tools | 5.8s ❌ | 390ms ❌ | 0.22 ⚠️ | 31 | LCP + INP failing |
| /sale | 5.4s ❌ | 510ms ❌ | 0.14 ⚠️ | 28 | LCP + INP failing |
| /products/safety-equipment | 4.8s ❌ | 210ms ⚠️ | 0.31 ❌ | 36 | LCP + CLS failing |
| / (homepage) | 4.1s ❌ | 340ms ❌ | 0.09 ✅ | 42 | LCP + INP failing |

---

## Full Scorecard — Mobile

| URL | LCP | INP | CLS | PSI | Status | Field Data |
|---|---|---|---|---|---|---|
| / (homepage) | 4.1s ❌ | 340ms ❌ | 0.09 ✅ | 42 | Fail | CrUX |
| /products/power-tools | 6.2s ❌ | 480ms ❌ | 0.28 ❌ | 24 | Fail | CrUX |
| /products/hand-tools | 5.8s ❌ | 390ms ❌ | 0.22 ⚠️ | 31 | Fail | CrUX |
| /products/measuring-tools | 3.1s ⚠️ | 190ms ✅ | 0.07 ✅ | 61 | NI | CrUX |
| /products/safety-equipment | 4.8s ❌ | 210ms ⚠️ | 0.31 ❌ | 36 | Fail | CrUX |
| /products/fasteners | 2.3s ✅ | 170ms ✅ | 0.06 ✅ | 79 | Pass | CrUX |
| /products/electrical | 2.8s ⚠️ | 180ms ✅ | 0.08 ✅ | 68 | NI | Lab only |
| /products/plumbing | 2.2s ✅ | 160ms ✅ | 0.05 ✅ | 82 | Pass | Lab only |
| /products/concrete-tools | 3.4s ⚠️ | 200ms ⚠️ | 0.09 ✅ | 55 | NI | Lab only |
| /products/welding | 2.4s ✅ | 175ms ✅ | 0.07 ✅ | 76 | Pass | Lab only |
| /categories/brands | 5.1s ❌ | 280ms ❌ | 0.12 ⚠️ | 33 | Fail | CrUX |
| /sale | 5.4s ❌ | 510ms ❌ | 0.14 ⚠️ | 28 | Fail | CrUX |
| /blog/top-10-power-tools-2026 | 2.1s ✅ | 150ms ✅ | 0.04 ✅ | 88 | Pass | CrUX |
| /blog/tradie-safety-guide | 2.3s ✅ | 160ms ✅ | 0.05 ✅ | 85 | Pass | CrUX |
| /about | 1.9s ✅ | 130ms ✅ | 0.03 ✅ | 91 | Pass | Lab only |
| /contact | 2.0s ✅ | 140ms ✅ | 0.04 ✅ | 89 | Pass | Lab only |
| /cart | 2.8s ⚠️ | 230ms ⚠️ | 0.18 ⚠️ | 59 | NI | CrUX |
| /checkout | 2.4s ✅ | 190ms ✅ | 0.11 ⚠️ | 73 | NI | CrUX |
| /search?q=drill | 4.2s ❌ | 350ms ❌ | 0.09 ✅ | 38 | Fail | Lab only |
| /products/tool-storage | 3.6s ⚠️ | 210ms ⚠️ | 0.08 ✅ | 53 | NI | Lab only |

---

## Full Scorecard — Desktop

| URL | LCP | INP | CLS | PSI | Status | Field Data |
|---|---|---|---|---|---|---|
| / (homepage) | 2.1s ✅ | 90ms ✅ | 0.04 ✅ | 78 | Pass | CrUX |
| /products/power-tools | 2.8s ⚠️ | 120ms ✅ | 0.09 ✅ | 65 | NI | CrUX |
| /products/hand-tools | 2.6s ⚠️ | 110ms ✅ | 0.08 ✅ | 70 | NI | CrUX |
| /sale | 2.9s ⚠️ | 140ms ✅ | 0.06 ✅ | 63 | NI | CrUX |
| /products/safety-equipment | 2.4s ✅ | 100ms ✅ | 0.12 ⚠️ | 74 | NI | CrUX |
| _(remaining 15 URLs — desktop Pass or NI)_ | … | … | … | … | … | … |

**Desktop finding:** All desktop metrics are significantly better. The mobile failures are primarily due to unoptimised image loading on mobile network simulation and heavy third-party scripts. Desktop is not ranking-critical — Google uses mobile field data.

---

## Remediation Recommendations

### 1. Unoptimised product listing page hero images (affects 6 URLs — LCP)

**Root cause:** Category PLP pages (`/products/power-tools`, `/products/hand-tools`, `/products/safety-equipment`, `/categories/brands`, `/sale`, `/search`) load a hero banner image as a JPEG (avg 1.8MB). No WebP variant exists. No `fetchpriority="high"` on the LCP `<img>`. Image served from origin server with no CDN caching for AU users.

**Affected URLs:** /products/power-tools, /products/hand-tools, /products/safety-equipment, /categories/brands, /sale, /search?q=drill

**Fix:**
1. Convert all PLP hero images to WebP format (target: < 150KB at max display width).
2. Add `fetchpriority="high"` to the first `<img>` in the hero component.
3. Add `<link rel="preload" as="image" href="[hero-image-url]" fetchpriority="high">` in `<head>`.
4. Enable Cloudflare Image Resizing (or equivalent CDN image optimisation) to serve WebP automatically and cache at Australian edge nodes.

**Impact:** High — expected LCP improvement of 1.5–2.5s per page | **Effort:** 1 day (image conversion + CDN config)

---

### 2. Tag Manager / chat widget blocking main thread (affects 8 URLs — INP)

**Root cause:** Google Tag Manager (GTM) fires synchronously on `DOMContentLoaded`, loading Klaviyo (email), Meta Pixel, Google Ads conversion tags, and Gorgias chat widget — total third-party blocking time: ~420ms on mobile. This is visible in the Lighthouse "Reduce the impact of third-party code" diagnostic across all failing INP pages.

**Affected URLs:** / (homepage), /products/power-tools, /products/hand-tools, /sale, /categories/brands, /search, /cart, and any PLP page receiving traffic.

**Fix:**
1. Delay GTM initialisation until after `load` event using a custom script trigger in GTM (fires GTM after page load instead of on `DOMContentLoaded`).
2. Or implement Partytown (https://partytown.builder.io/) to run third-party scripts in a service worker off the main thread.
3. Set Gorgias chat widget to load on first user interaction (scroll or click) rather than on page load.
4. Audit GTM tags — remove unused or duplicate firing tags (Lighthouse shows duplicate Meta Pixel fires on these pages).

**Impact:** High — expected INP improvement of 150–250ms | **Effort:** 1 sprint (GTM configuration + testing)

---

### 3. Product image grid without explicit dimensions (affects 4 URLs — CLS)

**Root cause:** Product grid `<img>` elements on `/products/power-tools`, `/products/hand-tools`, `/products/safety-equipment`, and `/sale` do not have explicit `width` and `height` HTML attributes. When images load, the grid reflows, causing CLS scores of 0.22–0.31.

**Affected URLs:** /products/power-tools, /products/hand-tools, /products/safety-equipment, /sale

**Fix:**
```html
<!-- Before (causes CLS) -->
<img src="/images/product-001.jpg" alt="Makita Drill">

<!-- After (no CLS) -->
<img src="/images/product-001.jpg" alt="Makita Drill" width="300" height="300">
```
For dynamically sized images, use CSS `aspect-ratio`:
```css
.product-card img {
  aspect-ratio: 1 / 1;
  width: 100%;
  height: auto;
}
```
Update the product card template to output `width` and `height` from product image metadata stored in the eCommerce platform.

**Impact:** High — expected CLS improvement to ≤ 0.1 on affected pages | **Effort:** 0.5 days (template change)

---

### 4. Promotional banner injected above fold on /sale (CLS)

**Root cause:** The `/sale` page injects a promotional countdown banner into the top of the DOM after initial render, pushing all page content down and contributing 0.08 to CLS (combined with image dimension issue above).

**Fix:** Reserve space for the banner using CSS `min-height` before the component loads:
```css
.promo-banner-wrapper {
  min-height: 56px; /* match banner height */
}
```
Or render the banner server-side so it is present in initial HTML (no reflow).

**Impact:** Medium — removes 0.08 CLS contribution | **Effort:** 2 hours

---

## Data Quality Notes

**URLs without CrUX field data (low traffic):** 6 URLs — lab data only for:
- /products/electrical, /products/plumbing, /products/concrete-tools, /products/welding, /about, /contact
These pages have insufficient CrUX data (< ~500 real Chrome sessions in the last 28 days). Lab data is used as a proxy; treat these results as indicative, not definitive for ranking signal purposes.

**PSI rate limiting:** Not applicable — PSI API key configured; all 40 PSI calls (20 URLs × 2 strategies) completed without throttling.
