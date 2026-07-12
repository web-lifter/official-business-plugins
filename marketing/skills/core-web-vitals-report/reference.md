# Core Web Vitals Report — Reference

## Google CWV Thresholds (Current)

| Metric | Full Name | Measures | Good | Needs Improvement | Poor |
|---|---|---|---|---|---|
| **LCP** | Largest Contentful Paint | Loading performance — time until the largest visible element is rendered | ≤ 2.5s | 2.5s–4.0s | > 4.0s |
| **INP** | Interaction to Next Paint | Responsiveness — time from user interaction to next visual update | ≤ 200ms | 200ms–500ms | > 500ms |
| **CLS** | Cumulative Layout Shift | Visual stability — total unexpected layout shift during page lifecycle | ≤ 0.1 | 0.1–0.25 | > 0.25 |

**Assessment threshold:** Google uses the **75th percentile** of field data (CrUX) for the page experience ranking signal. A page "passes" a metric when 75% of real user sessions achieve "Good" for that metric.

---

## Supporting Metrics (Reported by PSI, Not Core CWV)

| Metric | Description | Good | Notes |
|---|---|---|---|
| **FCP** (First Contentful Paint) | Time to first visible content | ≤ 1.8s | Diagnostic metric; not a ranking signal |
| **TTFB** (Time to First Byte) | Server response time | ≤ 800ms | Diagnostic metric; indirect LCP signal |
| **TBT** (Total Blocking Time) | Main-thread blocking (lab proxy for INP) | ≤ 200ms | Lab-only; correlates with INP |
| **Speed Index** | How quickly visible content fills the viewport | ≤ 3.4s | Composite lab metric |

---

## PSI Performance Score Bands

| Score | Rating | Meaning |
|---|---|---|
| 90–100 | Good | Fast page; prioritise maintenance |
| 50–89 | Needs Improvement | Performance issues affecting UX |
| 0–49 | Poor | Significant performance problems |

---

## Root Cause Diagnosis Quick Reference

### LCP Root Causes

| Root Cause | Signal | Fix |
|---|---|---|
| Render-blocking CSS/JS | `<link rel="stylesheet">` or `<script>` in `<head>` without `async`/`defer`; Lighthouse "Eliminate render-blocking resources" opportunity | Inline critical CSS; defer non-critical CSS; add `async` or `defer` to non-critical scripts |
| Large unoptimised image | LCP element is a JPEG/PNG > 200KB; Lighthouse "Properly size images" opportunity | Convert to WebP/AVIF; use responsive `srcset`; compress |
| No LCP preload / fetchpriority | LCP image loaded without priority hint; discovered late in cascade | Add `<link rel="preload" as="image" href="...">` or `fetchpriority="high"` on LCP `<img>` |
| High TTFB | PSI TTFB > 800ms; server in distant region from users | Add CDN with Australian PoP; enable HTTP/2; server-side caching |
| No CDN / image CDN | Images served from origin server; high latency for AU users | Serve images via CDN (Cloudflare, Fastly, AWS CloudFront with AU edge) |

### INP Root Causes

| Root Cause | Signal | Fix |
|---|---|---|
| Long tasks on main thread | Lighthouse "Avoid long main-thread tasks"; TBT > 200ms | Code-split JS; defer non-critical bundles; use `scheduler.postTask()` for deferred work |
| Third-party scripts | Lighthouse "Reduce the impact of third-party code"; chat widget / tag manager / A/B test tool in top blocking scripts | Lazy-load on first interaction; load after `load` event; use Partytown for tag isolation |
| Heavy framework boot | React/Vue/Angular hydration blocking interaction | Implement partial hydration / islands architecture; reduce JS bundle size |
| DOM size | > 1,500 DOM elements; Lighthouse "Avoid an excessive DOM size" | Virtualise long lists; remove unused DOM nodes; use CSS instead of DOM for decoration |

### CLS Root Causes

| Root Cause | Signal | Fix |
|---|---|---|
| Images without width/height | Lighthouse "Image elements do not have explicit width and height"; layout shift visible in CLS waterfall | Add `width` and `height` attributes to all `<img>` elements; CSS: `img { aspect-ratio: attr(width) / attr(height); }` |
| Injected content above fold | Cookie consent banner, live chat bubble, promotional banner injected into DOM post-render | Use CSS `position: fixed` for overlays; reserve space with CSS; inject below fold content only |
| Font FOUT/FOIT | Text visible shifts when web font loads; Lighthouse "Ensure text remains visible during webfont load" | Add `font-display: swap` to `@font-face`; preload key fonts: `<link rel="preload" as="font">` |
| Dynamic ad slots | Ad containers without reserved height | Reserve ad slot height with CSS `min-height`; use `aspect-ratio` for responsive ads |

---

## CrUX vs Lab Data

| Aspect | CrUX (Field Data) | Lighthouse (Lab Data) |
|---|---|---|
| Source | Real Chrome users visiting the URL (last 28 days) | Simulated load in controlled environment |
| Percentile | 75th percentile of real sessions | Single simulated session |
| Device | Separate mobile and desktop cohorts | Single throttled device profile |
| Availability | Requires ≥ ~500 visits/28 days | Always available |
| Ranking signal | **Yes — CrUX is Google's ranking signal** | No (diagnostic only) |
| Use for | Reporting actual user experience; ranking signal assessment | Diagnosing root causes; testing before deploying to production |

**Key rule:** If CrUX field data is available, it takes precedence for ranking signal assessment. Lab data is used for diagnosis.

---

## pagespeed_runner.py Output Schema

The script outputs a JSON file at the specified `--output` path with this structure:

```json
{
  "generated_at": "ISO8601 timestamp",
  "strategy": "mobile | desktop | both",
  "results": [
    {
      "url": "https://...",
      "strategy": "mobile",
      "field_data_available": true,
      "field": {
        "lcp_p75_ms": 2340,
        "inp_p75_ms": 180,
        "cls_p75": 0.08,
        "fcp_p75_ms": 1200,
        "ttfb_p75_ms": 420
      },
      "lab": {
        "lcp_ms": 2180,
        "tbt_ms": 190,
        "cls": 0.07,
        "fcp_ms": 1100,
        "speed_index_ms": 2800,
        "performance_score": 74
      },
      "opportunities": [
        {"id": "render-blocking-resources", "title": "Eliminate render-blocking resources", "savings_ms": 680},
        {"id": "uses-optimized-images", "title": "Efficiently encode images", "savings_ms": 420}
      ],
      "lcp_element": "img.hero-image"
    }
  ]
}
```

---

## Page Status Classification

Each URL receives a page status per device:

| Status | Condition |
|---|---|
| **Pass** | LCP Good AND INP Good AND CLS Good |
| **Needs Improvement** | Any metric in Needs Improvement range AND no metric in Poor range |
| **Fail** | Any metric in Poor range |

**Overall site status:** Pass if ≥ 75% of URLs have status "Pass" for both mobile and desktop.
