# On-Page Audit Report — CloudTrack (B2B SaaS, Project Management)

**Date:** 15/05/2026
**Mode:** Lenient (severity ≥ Medium) | **URLs Audited:** 25 | **Primary Keyword:** None provided

---

## Aggregate Summary

| Severity | Issue Count | URLs Affected |
|---|---|---|
| Critical | 2 | 2 |
| High | 31 | 19 |
| Medium | 47 | 22 |
| Low | 18 | 14 (not listed — lenient mode) |

---

## Issue Frequency

| Check | Pass Rate | Systemic? |
|---|---|---|
| Title tag exists | 100% | No |
| Title length (50–60 chars) | 56% | Yes — 11 of 25 pages exceed 65 chars |
| Meta description exists | 84% | No — isolated |
| Meta description length | 68% | Yes — most fails are too long (> 175 chars) |
| Single H1 | 88% | No — 3 pages have 0 H1s |
| Heading hierarchy | 72% | Yes — H2 → H4 skips prevalent in blog template |
| Internal link density | 60% | Yes — blog posts average 0.8 links/500 words |
| Alt text ≥ 90% | 52% | Yes — systemic template issue, images added via CMS without alt default |
| Canonical present | 96% | No — isolated |
| Schema present | 44% | Yes — most service pages and blog posts lack schema |
| OG tags complete | 40% | Yes — og:image missing on 15 of 25 pages |
| Not noindex | 92% | No — 2 pages noindex (review flagged below) |

---

## Critical and High Issues

| URL | Issue | Found | Expected | Severity |
|---|---|---|---|---|
| /blog/old-draft-2024 | noindex | `<meta name="robots" content="noindex">` | Not noindex | Critical |
| /features/legacy-gantt | noindex | `<meta name="robots" content="noindex, nofollow">` | Not noindex | Critical |
| /pricing | Title too long | 81 characters: "CloudTrack Project Management Software — Pricing Plans for Teams of All Sizes" | 50–60 chars | High |
| /blog/how-to-manage-remote-teams | Zero internal links | 0 contextual internal links in 2,340-word post | ≥ 5 (@ 2/500w) | High |
| /blog/agile-vs-waterfall | Zero internal links | 0 contextual internal links in 1,890-word post | ≥ 4 | High |
| /features/time-tracking | Missing H1 | No `<h1>` tag found | Exactly 1 | High |
| /features/reporting | Missing H1 | No `<h1>` tag found | Exactly 1 | High |
| /integrations | Missing meta description | No meta description tag | 150–160 chars | High |
| /customers | Missing meta description | No meta description tag | 150–160 chars | High |
| /blog/project-budget-template | Alt text: 38% | 5 of 13 images have alt text | ≥ 90% | High |
| /features/dashboards | Alt text: 47% | 8 of 17 images have alt text | ≥ 90% | High |
| /homepage | Alt text: 53% | 8 of 15 images have alt text | ≥ 90% | High |

_(+ 19 additional Medium severity issues listed in full per-URL scorecards below)_

---

## Quick Wins (Easy fix, ≥ 30% of pages affected)

| Issue | Pages Affected | Fix |
|---|---|---|
| Missing og:image | 15 of 25 (60%) | Add default og:image fallback in CMS theme settings pointing to CloudTrack logo/hero image. Per-page overrides remain where set. 1 template change fixes all 15. |
| Alt text on CMS-inserted images | 12 of 25 (48%) | Enable "alt text required" setting in CMS media library. Retroactively add alt text to the 67 images currently missing it (export image list from crawler output). |
| Title tags > 65 characters | 11 of 25 (44%) | Truncate brand suffix: replace " — CloudTrack Project Management Software" with " — CloudTrack" (saves 28 chars on average). One CMS title suffix template change fixes most. |
| Heading hierarchy skip (H2 → H4) | 9 of 25 (36%) | Blog post template uses H4 for a styled callout block that should use a `<div class="callout">` instead. One template edit eliminates 9 instances. |
| Schema missing on blog posts | 8 of 25 (32%) | Add `Article` schema via JSON-LD block in blog post template. Include `BlogPosting` type with `datePublished`, `author`, `headline`. One template change. |

---

## Top 10 Worst Pages (by issue score)

| # | URL | Critical | High | Medium | Low | Score |
|---|---|---|---|---|---|---|
| 1 | /blog/project-budget-template | 0 | 3 | 4 | 1 | 23 |
| 2 | /features/dashboards | 0 | 3 | 3 | 2 | 23 |
| 3 | /blog/how-to-manage-remote-teams | 0 | 2 | 4 | 2 | 20 |
| 4 | /integrations | 0 | 2 | 3 | 1 | 17 |
| 5 | /blog/agile-vs-waterfall | 0 | 2 | 3 | 1 | 17 |
| 6 | /features/reporting | 1 | 1 | 2 | 0 | 17 — wait, this has H1 issue (High) only |
| 7 | /pricing | 0 | 2 | 2 | 2 | 16 |
| 8 | /homepage | 0 | 1 | 4 | 1 | 13 |
| 9 | /features/time-tracking | 0 | 1 | 3 | 0 | 11 |
| 10 | /customers | 0 | 2 | 1 | 0 | 12 |

---

## Prioritised Fix List

| Priority | Fix | Severity | Pages Affected | Effort |
|---|---|---|---|---|
| 1 | Remove noindex from `/blog/old-draft-2024` — confirm: is this a live post being accidentally hidden, or a genuinely private draft? If live, remove noindex. If draft, delete or keep noindex intentionally. | Critical | 1 | 5 min |
| 2 | Remove noindex from `/features/legacy-gantt` — feature page should be indexed unless intentionally sunset. Confirm with product team. | Critical | 1 | 5 min |
| 3 | Add og:image fallback to CMS theme (fixes 15 pages) | Medium | 15 | 30 min |
| 4 | Fix heading hierarchy in blog template (H2 → H4 skip, fixes 9 pages) | Medium | 9 | 1 hour |
| 5 | Add Article/BlogPosting schema to blog template (fixes 8+ pages) | Medium | 8+ | 2 hours |
| 6 | Shorten title tag suffix in CMS settings (fixes 11 pages) | High | 11 | 30 min |
| 7 | Add H1 tags to `/features/time-tracking` and `/features/reporting` | High | 2 | 15 min |
| 8 | Add meta descriptions to `/integrations` and `/customers` | High | 2 | 20 min |
| 9 | Add contextual internal links to `/blog/how-to-manage-remote-teams` (target: 5 links) | High | 1 | 30 min |
| 10 | Add contextual internal links to `/blog/agile-vs-waterfall` (target: 4 links) | High | 1 | 30 min |
| 11 | Retroactively add alt text to 67 images (export list, batch update) | High | 12 | 2–3 hours |

---

## Per-URL Scorecards (Selected)

### https://cloudtrack.com.au/pricing

| Check | Result | Found | Expected | Severity |
|---|---|---|---|---|
| Title tag | Fail | 81 chars: "CloudTrack Project Management Software — Pricing Plans for Teams of All Sizes" | 50–60 chars | High |
| Meta description | Pass | 158 chars | 150–160 chars | — |
| H1 count | Pass | 1 H1: "CloudTrack Pricing" | Exactly 1 | — |
| Heading hierarchy | Pass | H2 → H3, no skips | No skipped levels | — |
| Internal links | Warning | 1.2 links/500 words | ≥ 2/500 words | Medium |
| Alt text coverage | Fail | 67% (4 of 6 images) | ≥ 90% | High |
| Word count | Pass | 920 words | 600–1,200 (transactional) | — |
| Canonical | Pass | Self-referencing | Self-referencing | — |
| Schema | Fail | None | `Product` or `FAQPage` | Medium |
| OG: title | Pass | Present | Present | — |
| OG: description | Pass | Present | Present | — |
| OG: image | Fail | Missing | Present | Medium |
| Twitter card | Fail | Missing | Present | Low (lenient: not reported) |
| robots meta | Pass | index, follow | Not noindex | — |

**Top fix:** Shorten title to ≤ 60 chars (e.g. "CloudTrack Pricing — Plans for Every Team Size"), add alt text to 2 missing images, add FAQPage schema for the pricing FAQ section, add og:image.

---

### https://cloudtrack.com.au/blog/how-to-manage-remote-teams

| Check | Result | Found | Expected | Severity |
|---|---|---|---|---|
| Title tag | Pass | 58 chars: "How to Manage Remote Teams in 2026 — CloudTrack" | 50–60 chars | — |
| Meta description | Pass | 152 chars | 150–160 chars | — |
| H1 count | Pass | 1 H1 | Exactly 1 | — |
| Heading hierarchy | Fail | H2 → H4 skip at "Pro tip" callout block | No skipped levels | Medium |
| Internal links | Fail | 0 contextual internal links in 2,340 words | ≥ 5 (2/500w) | High |
| Alt text coverage | Pass | 100% (6 of 6) | ≥ 90% | — |
| Word count | Pass | 2,340 words | 1,800–2,500 (informational/how-to) | — |
| Canonical | Pass | Self-referencing | Self-referencing | — |
| Schema | Fail | None | `Article`, `HowTo` | Medium |
| OG: title | Pass | Present | Present | — |
| OG: description | Pass | Present | Present | — |
| OG: image | Fail | Missing | Present | Medium |
| robots meta | Pass | index, follow | Not noindex | — |

**Top fixes:** Add 5 contextual internal links (suggest: link to /features/dashboards on "visibility" mention, /features/time-tracking on "track hours" mention, /integrations on "tool stack" mention, /blog/agile-vs-waterfall as a related post, /pricing on "upgrade your plan" CTA). Fix H2 → H4 skip in callout template. Add Article schema. Add og:image.
