# Broken Link Scanner — Reference Framework

## HTTP Status Taxonomy

### 4xx Client Errors

| Code | Name | SEO Implication | Recommended Action |
|---|---|---|---|
| 400 | Bad Request | Malformed URL — usually a site bug | Fix the URL in the source page's link |
| 401 | Unauthorised | Content behind login; not indexable | Expected for private pages; check if accidentally linked from public pages |
| 403 | Forbidden | Access denied; not indexable | Expected for admin paths; check if accidentally linked from public pages |
| 404 | Not Found | Page does not exist; loses all link equity | Redirect to most relevant existing page (301) or return 410 if content is gone |
| 410 | Gone | Explicitly removed; faster de-indexation than 404 | Confirm content is intentionally retired; use for removed products, discontinued services |
| 451 | Unavailable for Legal Reasons | Rare; content removed on legal grounds | Handle case-by-case; do not redirect without legal review |

### 5xx Server Errors

| Code | Name | SEO Implication | Recommended Action |
|---|---|---|---|
| 500 | Internal Server Error | Server-side bug; Google will retry but may de-prioritise crawling | Investigate and fix immediately; these are developer issues, not SEO issues |
| 502 | Bad Gateway | Upstream server error (common in proxy/CDN setups) | Check CDN/proxy configuration; usually transient |
| 503 | Service Unavailable | Server temporarily overloaded or in maintenance | Add `Retry-After` header for planned maintenance; investigate if persistent |
| 504 | Gateway Timeout | Upstream server too slow to respond | Investigate server performance; may indicate a crawl budget drain |

### Key Distinction: 404 vs 410

- **404**: Google treats this as "maybe temporary" and will re-crawl the page for weeks before removing it from the index
- **410**: Google treats this as "deliberately gone" and de-indexes the page faster
- **When to use 410:** Discontinued products, deleted blog posts, removed service pages
- **When to use 404:** Accidentally broken links that will be fixed; pages that may return

---

## Orphan-Page Definition

### Sitemap Orphan
A URL that is:
- Present in the XML sitemap (crawlable and indexable)
- BUT receives zero internal links from other pages on the site

**Problem:** Google discovers the page via the sitemap but has no context signals about its importance. Internal links carry PageRank and topical context — without them, the page is isolated.

**How to detect:** `sitemap_urls − internally_linked_urls = sitemap_orphans`

### Navigation Orphan
A URL that:
- Is reachable via internal links (present in the crawl)
- BUT is NOT included in the XML sitemap

**Problem:** May or may not be indexed depending on crawl depth. If it has valuable content, it should be in the sitemap.

**How to detect:** `internally_linked_urls − sitemap_urls = nav_orphans`

### Orphan Severity Tiers

| Tier | Condition | Action |
|---|---|---|
| Critical | Sitemap orphan + has external backlinks | Connect to nearest cluster hub immediately |
| High | Sitemap orphan + conversion/transactional value | Add to nearest hub as spoke |
| Medium | Sitemap orphan + informational content | Evaluate: connect or 410 if thin |
| Low | Sitemap orphan + thin/duplicate content | Remove from sitemap + 410 or redirect |
| Watch | Nav orphan + substantial content | Add to sitemap |
| Ignore | Nav orphan + utility/admin page | Add noindex if not already |

---

## Soft-404 Detection Heuristics

A soft-404 is a page that returns a 200 HTTP status code but serves content that is functionally a "not found" or error state.

### Detection Signals (apply any 1 = candidate)

| Signal | Heuristic | Threshold |
|---|---|---|
| Error title | Title or H1 contains: "not found", "404", "error", "oops", "doesn't exist", "can't find", "coming soon", "under construction" | Exact string match (case-insensitive) |
| Thin content | Response body word count (excluding navigation/footer boilerplate) | < 200 words |
| Template response | Response body is identical or near-identical to another URL already in the crawl | > 90% cosine similarity |
| Redirect-equivalent | Page contains a meta refresh redirect or a JavaScript redirect in the body | Presence of `<meta http-equiv="refresh">` or `window.location` |
| Empty search results | Page appears to be a search results page returning zero results | URL contains `?s=`, `?q=`, or `?search=` and body contains "0 results" or "no results found" |

### False Positive Risk

Short-form pages that are intentionally thin:
- Contact pages (form only)
- Thank-you pages (post-conversion)
- Single-product pages with short descriptions
- Calendars or booking widgets

Flag these as candidates for human review, not for automatic action.

---

## Link-Rot Remediation Playbook

### Priority 1 — Broken Internal Links on High-Equity Pages

1. Identify the source page (found-on) and the broken target.
2. Determine why the target is broken:
   - Accidental deletion → restore the page or redirect to the closest equivalent
   - URL structure change → add a 301 redirect
   - Content retired → replace the link with a link to related content, or remove the link
3. Fix within 24–48 hours if the source page has external backlinks.

### Priority 2 — Orphan Pages with External Links

1. Identify the orphan's topic cluster using its content/URL.
2. Add an internal link from the nearest hub or related spoke.
3. Ensure the orphan links back to its hub (spoke→hub link).
4. Verify the URL is in the sitemap.

### Priority 3 — Broken External Links

1. Check if the external URL still exists at a different address (has it been moved?).
2. If moved: update the link on the source page.
3. If gone permanently: remove the citation or replace with an alternative source.
4. If the external page was cited as evidence for a claim: find an updated or alternative source.

### Priority 4 — Soft-404s

1. Review each candidate manually.
2. If the page genuinely has no content value: remove from sitemap, add noindex, or return 410.
3. If the page has content value but thin content: expand the content.
4. If the page is a template returning empty results: fix the template or disallow the URL pattern in robots.txt.

---

## Crawl Budget Implications

Google allocates a crawl budget to each site. Broken links and orphan pages consume crawl budget without contributing to indexation:

- Each 404 response Google encounters wastes a crawl budget allocation
- Soft-404s waste crawl budget AND may result in poor-quality content being indexed
- Large numbers of orphan pages may indicate to Google that the site's navigation is poor (low "site quality" signal)

**Rule of thumb:** Sites with < 1,000 pages typically have unlimited crawl budget and do not need to worry about crawl budget optimisation. Sites > 10,000 pages should actively manage crawl budget by minimising broken URLs, removing thin pages, and using disallow rules for truly utility/admin paths.

---

## Key References

- Google Search Central: HTTP status codes for SEO
- Google Search Central: Site crawl management
- Screaming Frog SEO Spider: Crawl data export documentation
- Moz: Orphan pages and internal link auditing
