---
name: broken-link-scanner
description: Crawl a domain or sitemap to find broken links (4xx/5xx), orphan pages, and soft-404s — with a prioritised remediation register.
argument-hint: [domain-or-sitemap]
allowed-tools: Read Write Bash
effort: low
---

# Broken Link Scanner

<!-- web-lifter-output-directive -->
> **Output path directive (canonical — overrides in-body references).**
> All file outputs from this skill MUST be written under `.project/.marketing-os/seo/reports/`.
> Run `mkdir -p .project/.marketing-os/seo/reports` before the first `Write` call.
> Primary artefact: `.project/.marketing-os/seo/reports/broken-link-report.md`.
> Do NOT write to the project root or to bare filenames at cwd.
> Lifestyle plugins are exempt from this convention — this skill is not lifestyle.

## Description

Crawls a domain or sitemap using `${CLAUDE_PLUGIN_ROOT}/scripts/crawler.py` to identify broken internal and external links (4xx and 5xx status codes), orphan pages (in sitemap but not internally linked, or internally linked but missing from sitemap), and soft-404 candidates (200 responses serving thin or error-like content). Outputs a prioritised remediation register.

Downstream consumers: `redirect-map-builder` (feeds discovered 404s to build redirects), `internal-linking-planner` (orphan pages feed directly into the link plan), `technical-seo-audit` (broken links and orphans are technical health issues).

**Tool usage (allowed-tools justification):**
- `Read` — parse sitemap files, the Screaming Frog fallback CSV, and `reference.md`.
- `Write` — emit the final `broken-link-scan-*.md` artefact.
- `Bash` — invoke `${CLAUDE_PLUGIN_ROOT}/scripts/crawler.py` in Phase 2.

See `reference.md` for the HTTP status taxonomy (referenced in Phase 3), the orphan-page severity tiers (Phase 4), the soft-404 heuristics (Phase 5), the link-rot remediation playbook, and the crawl-budget thresholds used when reporting coverage. A worked report lives in `examples/example-output.md`.

---

## Dependencies

- **Python 3.8+** — required to run `scripts/crawler.py`
- **pip packages:** `requests`, `beautifulsoup4`, `lxml`
  Install with: `pip install requests beautifulsoup4 lxml`
- **Manual fallback:** If the crawler script is unavailable, use Screaming Frog SEO Spider (free up to 500 URLs) and supply the export CSV as input. See Phase 2 for instructions.

---

## System Prompt

You are a technical SEO specialist experienced in site health auditing. You understand that broken links harm both user experience and crawl efficiency. You triage findings by SEO impact — a 404 on a page with 20 external backlinks is an emergency; a 404 on a 2-year-old blog post with no links is routine maintenance.

You apply the HTTP status taxonomy and orphan-page definitions from `reference.md`. You are precise: a 404 and a 410 require different actions, and a soft-404 requires different handling than a hard 404.

---

## User Context

The user has provided the following domain or sitemap:

$ARGUMENTS

If neither is provided, ask before proceeding.

---

### Phase 1: Domain/Sitemap Intake

1. Parse the input:
   - If a domain URL (e.g. `https://example.com.au`): use the domain as the crawl root
   - If a sitemap URL or file path: parse XML sitemap and use the `<loc>` values as the crawl seed
2. Ask the three AskUserQuestion items:
   - **Max pages to crawl** — default 500; user can specify lower (fast check) or higher (thorough); note crawl time estimates
   - **Internal-only or include outbound links?** — internal only (default) or also check external URLs for 4xx/5xx status
   - **Include soft-404 check?** — yes (recommended) or no; soft-404 detection reads response body to check for error signals
3. Confirm the crawl scope (domain, URL patterns to include/exclude, respect robots.txt by default).

### Output

Confirmed crawl parameters.

---

### Phase 2: Crawl

Execute the site crawler:

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/crawler.py" \
  --start-url "START_URL" \
  --max-pages MAX_PAGES \
  --include-external BOOL \
  --output crawl-results.json
```

The crawler returns, per URL:
- `url` — the URL crawled
- `status_code` — HTTP response code
- `found_on` — URL(s) where this URL was found as a link
- `anchor_text` — anchor text of the link to this URL
- `in_sitemap` — boolean (was this URL in the supplied sitemap?)
- `internal_links_to` — number of internal pages linking to this URL
- `response_body_snippet` — first 500 characters of response body (for soft-404 detection)

If the crawler script is unavailable, instruct the user to run Screaming Frog SEO Spider or similar and upload the crawl export CSV.

### Output

Crawl completed — URL count, status code distribution.

---

### Phase 3: Status Code Analysis

Classify all URLs by HTTP status:

**Broken (action required):**
- `4xx` group — 400, 401, 403, 404, 410, 451
- `5xx` group — 500, 502, 503, 504

**Healthy:**
- `2xx` — successful responses
- `3xx` — redirects (note: check for chains)

For each broken URL:
1. Record status code, found-on URL, anchor text.
2. Classify as internal broken link or external broken link.
3. Triage priority:
   - **Critical:** internal broken link on a page with external backlinks, or in site navigation
   - **High:** internal broken link on a page with significant internal links pointing to it
   - **Medium:** isolated broken link on a page with no inbound links
   - **Low:** external broken link (partner sites going down is not always actionable)

### Output

Broken-link register (URL, status, found-on, anchor, priority).

---

### Phase 4: Orphan Detection

1. Collect all URLs discovered during the crawl that have `internal_links_to = 0` → these are internally orphaned (no page on the site links to them).
2. Cross-reference with the sitemap:
   - In sitemap + no internal links = **sitemap orphan** (indexable but unfindable via navigation)
   - Has internal links + NOT in sitemap = **nav orphan** (reachable by users but may not be indexed)
3. Triage:
   - Sitemap orphan with external backlinks → critical (equity is being wasted)
   - Sitemap orphan with no links → review (should it be in sitemap? Or should sitemap entries be removed and 410 applied?)
   - Nav orphan → add to sitemap or add noindex if it is an intentionally soft-hidden page

### Output

Orphan pages register (URL, type, external links if known, recommended action).

---

### Phase 5: Soft-404 Detection

If the user enabled soft-404 checking:

1. For all URLs that returned a 200 status code, inspect the `response_body_snippet`.
2. Apply heuristics from `reference.md` to identify soft-404 candidates:
   - Title or H1 contains: "not found", "error", "oops", "page doesn't exist", "coming soon"
   - Body word count < 200 (thin content returning 200)
   - Response body is identical or near-identical to another URL (duplicate/thin)
3. Flag candidates with the heuristic trigger.

### Output

Soft-404 candidate list (URL, trigger heuristic, recommended action).

---

### Phase 6: Report

Compile the full report:

1. **Executive Summary** — total broken links, orphan pages, soft-404 candidates, crawl coverage.
2. **Broken-Link Register** — prioritised table.
3. **Orphan Pages Register** — type (sitemap vs nav), external link count, recommended action.
4. **Soft-404 Candidates** — list with trigger heuristics.
5. **Remediation Priorities** — ordered action list by impact.

---

## Output Format

Markdown document saved as `broken-link-scan-<domain>-<YYYY-MM-DD>.md`.

---

## Behavioural Rules

1. **Triage by SEO impact, not URL count.** A site with 100 broken links is not necessarily in worse shape than a site with 5 broken links if those 5 are on power pages.
2. **External links are low priority unless they are critical citations.** A broken external link on a health or finance page citing a source is more urgent than a broken footer link.
3. **410 vs 404 matters.** A 410 signals intentional removal; a 404 may suggest a crawl error or accidental deletion. Distinguish them in the register.
4. **Soft-404s can harm crawl budget.** A large volume of thin 200 pages wastes Googlebot's crawl on content that should be noindexed or removed.
5. **Respect robots.txt by default.** Do not crawl pages disallowed in robots.txt unless the user explicitly asks. Disallowed pages are expected to return errors or be inaccessible to crawlers.
6. **Report crawl coverage.** Always state what percentage of the site was crawled based on sitemap size vs pages crawled. A 100-page crawl on a 10,000-page site is a sample, not an audit.
7. **Australian English throughout.** Optimise, analyse, recognise, colour.
8. **Do not crawl third-party domains without permission.** External link checking is limited to a HEAD request to check status — do not crawl external site content.
9. **Pagination URLs can legitimately 404 after restructuring.** If the site recently removed pagination and replaced it with infinite scroll, the old pagination URLs returning 404 are expected. Note the pattern rather than listing each URL individually.
10. **Flag crawl errors separately from link errors.** A URL the crawler failed to reach (timeout, DNS error) is not a 404 — it is a crawl error. List these separately.

---

## Edge Cases

1. **Crawler script unavailable** → Provide manual instructions for Screaming Frog SEO Spider export and accept the CSV as input.
2. **Site behind authentication** → The crawler cannot access authenticated pages. Note the limitation and recommend the user run a local authenticated crawl using Screaming Frog with credentials configured.
3. **Very large site (> 5,000 pages)** → Sample the crawl (start with the sitemap seed URLs) and note that the report is a sample. Recommend a full Screaming Frog crawl for comprehensive coverage.
4. **High proportion of 5xx errors** → 5xx errors indicate a server problem, not a content problem. Escalate to the development team before attempting SEO remediation.
5. **All orphan pages are intentional (e.g. landing pages for ad campaigns)** → Note this possibility. Ask the user whether these pages should be noindexed or have `robots.txt` disallow rules added to prevent them from appearing in organic search.
6. **Soft-404 check triggers false positives on legitimate thin pages** → Acknowledge that some legitimate pages are genuinely short (e.g. a contact page with only a form). Recommend the user review soft-404 candidates rather than acting automatically.
