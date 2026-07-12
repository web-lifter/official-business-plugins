# On-Page Audit — Reference

## On-Page Checklist with Thresholds

Based on Yoast SEO, SurferSEO, and Google Search Essentials guidelines.

| # | Check | Pass Criteria | Warning | Fail / Severity |
|---|---|---|---|---|
| 1 | Title tag exists | Present | — | Missing → **Critical** |
| 2 | Title length | 50–60 characters | 45–49 or 61–65 chars → Medium | < 45 or > 65 chars → **High** |
| 3 | Keyword in title | Primary keyword appears in title (front-weighted preferred) | Keyword present but at end → Low | Keyword absent → **High** (only if keyword provided) |
| 4 | Meta description exists | Present | — | Missing → **High** |
| 5 | Meta description length | 150–160 characters | 130–149 or 161–175 chars → Low | < 130 or > 175 chars → **Medium** |
| 6 | H1 count | Exactly one H1 | — | Zero H1s → **Critical**; Multiple H1s → **High** |
| 7 | Keyword in H1 | Primary keyword (or close variant) in H1 | — | Absent → **Medium** (only if keyword provided) |
| 8 | Heading hierarchy | H2 before H3, H3 before H4; no level skipped | Single skip (H2 → H4) → Low | Multiple skips → **Medium** |
| 9 | Internal link density | ≥ 2 internal links per 500 words of body content | 1 per 500 words → Low | 0 internal links → **High** |
| 10 | Alt text coverage | ≥ 90% of images have non-empty alt attribute | 75–89% → Medium | < 75% → **High** |
| 11 | Word count | Within 80–150% of the SERP median for the primary keyword | 70–79% of median → Low | < 70% of median → **Medium** (only if keyword + median provided) |
| 12 | Canonical tag | Present; self-referencing URL (or intentional non-self) | Non-self canonical → Warning (confirm intent) | Missing → **Medium**; Malformed → **High** |
| 13 | Schema markup | At least one schema type present and valid | Schema present but no type appropriate for page → Low | No schema → **Medium** |
| 14 | OG: title | og:title meta tag present | — | Missing → **Medium** |
| 15 | OG: description | og:description meta tag present | — | Missing → **Medium** |
| 16 | OG: image | og:image meta tag present | — | Missing → **Medium** |
| 17 | Twitter card | twitter:card meta tag present | — | Missing → **Low** |
| 18 | robots meta | Not noindex (or explicitly allowed to index) | noindex AND nofollow on same page → confirm intent | noindex → **Critical** |

---

## Severity Definitions

| Severity | Definition | Action |
|---|---|---|
| **Critical** | Will prevent the page from being indexed or ranked. Must be fixed immediately. | Fix before publishing / first in queue |
| **High** | Significantly reduces ranking potential or click-through rate. High-priority fix. | Fix this sprint |
| **Medium** | Reduces ranking potential or CTR; less immediate but important. | Fix in next sprint |
| **Low** | Minor improvement opportunity. Worth fixing if effort is low. | Batch fix or leave |

---

## Internal Link Density Formula

`Internal link density = (number of internal links) / (word count / 500)`

Example: A 1,500-word page with 3 internal links = 3 / (1500/500) = 1.0 links per 500 words. Target: ≥ 2.

Exclude navigation and footer links from the count — count only contextual in-content links.

---

## SERP Median Word Count Reference

Approximate SERP median word counts by query type (use as a reference when primary keyword + intent is known):

| Query / Intent | SERP Median Word Count |
|---|---|
| Informational / How-to | 1,800–2,500 |
| Informational / Definition | 800–1,400 |
| Commercial / Best | 2,000–3,500 |
| Commercial / Compare | 1,500–2,500 |
| Transactional / Service page | 600–1,200 |
| Transactional / Product page | 300–800 |
| Local landing page | 600–1,200 |

These are approximate. Actual SERP medians should be validated by examining top-10 results for the specific query.

---

## Schema Type Recommendations by Page Type

| Page Type | Recommended Schema |
|---|---|
| Homepage | `Organization`, `WebSite`, `LocalBusiness` (if local) |
| Service page | `Service`, `LocalBusiness`, `FAQPage` |
| Blog post / article | `Article`, `BlogPosting`, `BreadcrumbList` |
| How-to guide | `HowTo`, `FAQPage`, `Article` |
| Product page | `Product`, `Offer`, `AggregateRating` |
| Location/contact page | `LocalBusiness`, `PostalAddress` |
| Author bio page | `Person` |

---

## OG Tag Reference

Required OG tags for correct social sharing:

| Tag | Purpose | Recommended Length |
|---|---|---|
| `og:title` | Title displayed when shared | 60–90 characters |
| `og:description` | Description displayed when shared | 100–155 characters |
| `og:image` | Preview image | 1200 × 630 px recommended; min 600 × 314 px |
| `og:url` | Canonical URL for the shared page | Exact canonical URL |
| `og:type` | Content type | `website` for homepage; `article` for blog posts |

---

## Scoring Formula (Aggregate)

For ranking pages by issue severity in the aggregate report:

`page_score = (Critical × 10) + (High × 5) + (Medium × 2) + (Low × 1)`

Sort descending — highest score = worst page = fix first.

---

## Yoast/SurferSEO On-Page Principles Referenced

- **Yoast SEO**: Focus keyphrase in SEO title, meta description, first paragraph, subheadings, URL, image alt text. Outbound links to authoritative sources. Text length appropriate to content type.
- **SurferSEO**: Content score based on keyword density, NLP terms, heading structure, word count vs top-10 competitors, internal links, and image use.
- **Google Search Essentials**: Unique, helpful, reliable content. Accurate title and meta. Proper canonical. Schema markup for enhanced appearance.
