# Broken Link Scan — cloudtech.com.au

**Date:** 15/05/2026
**Crawl seed:** https://cloudtech.com.au/sitemap.xml
**Pages crawled:** 198 of 214 (93% coverage)
**Internal-only:** No (external links checked via HEAD request)
**Soft-404 check:** Yes

---

## Executive Summary

- **Broken links found:** 8 (Critical: 2, High: 3, Medium: 2, Low: 1)
- **Orphan pages found:** 3 (Sitemap orphans: 2, Nav orphans: 1)
- **Soft-404 candidates:** 2
- **Priority action:** Fix the two critical 404 pages — `/resources/saas-pricing-guide/` and `/case-studies/acme-corp/` — both have significant external backlinks and are returning 404 since the recent CMS migration. These should be redirected to their new URLs immediately.

---

## Broken-Link Register

| Priority | Broken URL | Status | Found On | Anchor Text | Type |
|---|---|---|---|---|---|
| Critical | /resources/saas-pricing-guide/ | 404 | /resources/, /blog/choosing-cloud-software/ | "SaaS Pricing Guide", "pricing guide" | Internal |
| Critical | /case-studies/acme-corp/ | 404 | /case-studies/, /solutions/enterprise/ | "Acme Corp case study", "see how Acme saved 40%" | Internal |
| High | /blog/cloud-migration-checklist/ | 404 | /blog/, /services/migration/ | "migration checklist", "free checklist" | Internal |
| High | /integrations/xero-connector/ | 404 | /integrations/, /features/ | "Xero integration", "connect Xero" | Internal |
| High | /careers/ | 404 | Main navigation header (sitewide) | "Careers" | Internal |
| Medium | /docs/api-reference/ | 404 | /developers/ | "API Reference documentation" | Internal |
| Medium | https://aaa.org.au/cloud-computing-standards | 404 | /blog/security-compliance-guide/ | "industry standard" | External |
| Low | https://oldpartnersite.com.au/joint-announcement | 404 | /about/partners/ | "joint press release" | External |

**Total broken links:** 8
**Notes:**
- The `/careers/` 404 is in the site-wide navigation header — it appears as a broken link on every page. Crawl flagged this on every page but it is one root cause (missing `/careers/` page).
- External link to `aaa.org.au` may have moved — check for a redirect or updated URL before removing the citation.

---

## Orphan Pages Register

| URL | Type | External Links | Conversion Value | Recommended Action |
|---|---|---|---|---|
| /resources/cloud-cost-calculator/ | Sitemap orphan | 3 external links | High (interactive tool; high conversion intent) | Add internal links from /resources/ hub page and /pricing/ page immediately |
| /whitepapers/multi-cloud-strategy-2025/ | Sitemap orphan | 1 external link | Medium (gated content; lead generation) | Add internal link from /resources/ and from a relevant blog post |
| /old-site-archive/ | Nav orphan | 0 | None (appears to be a legacy archive page) | Add noindex meta tag; remove from sitemap if not there already; or 410 |

---

## Soft-404 Candidates

| URL | Trigger | Snippet | Recommended Action |
|---|---|---|---|
| /search/?q=cloudbackup | Thin content (42 words); empty search results | "Your search for 'cloudbackup' returned no results. Try a different search term…" | Noindex search result pages via `robots.txt` (`Disallow: /search/`) or canonical; do not leave empty search pages indexed |
| /tags/deprecated/ | Thin content (12 words); title contains "no posts" | "No posts found in this category." | Remove from sitemap; add noindex; or return 410 — this is a blog tag with no remaining posts |

---

## Remediation Priorities

1. **Restore or redirect `/careers/`** — This is in the sitewide navigation and affects every page on the site as a source of the 404. If the careers page was accidentally deleted during migration, restore it. If careers are now handled via a third-party platform (e.g. Seek, LinkedIn), create a `/careers/` page that redirects to or embeds the external listing. Estimated effort: 1 hour.

2. **Redirect `/resources/saas-pricing-guide/` and `/case-studies/acme-corp/`** — Both pages have external backlinks pointing to them (confirmed via Ahrefs). The link equity is currently flowing to a 404. Find the new URLs in the current site and add 301 redirects from the old URLs. If these pages no longer exist in the new site, recreate or redirect to the closest equivalent. Estimated effort: 30–60 minutes.

3. **Connect `/resources/cloud-cost-calculator/` (orphan)** — This tool has 3 external backlinks and is a high-conversion asset. It is completely invisible to internal PageRank flow. Add a prominent link from the /resources/ hub page and from /pricing/. Estimated effort: 20 minutes.

4. **Fix `/blog/cloud-migration-checklist/` and `/integrations/xero-connector/`** — Both are referenced in the site's own content (internal links on /services/migration/ and /features/). Find the new URLs and update the links or add redirects. Estimated effort: 30 minutes.

5. **Noindex empty search pages** — Add `Disallow: /search/` to robots.txt or add a `<meta name="robots" content="noindex">` to all search result pages. Empty search pages indexed waste crawl budget and may be flagged as thin content. Estimated effort: 15 minutes (developer change).

6. **Handle `/tags/deprecated/` and `/old-site-archive/`** — Both are serving thin/empty content. Return 410 for the deprecated tag page; add noindex to the archive or 410 it if it has no retention value. Estimated effort: 15 minutes.

7. **Update or remove the broken external citation on `/blog/security-compliance-guide/`** — The link to `aaa.org.au/cloud-computing-standards` is returning a 404. Check whether the page has moved (check for a redirect at the root domain). If the standard is cited as evidence, find an updated version or replace with an equivalent authoritative source. Estimated effort: 20 minutes.

---

*Generated by marketing / broken-link-scanner*
