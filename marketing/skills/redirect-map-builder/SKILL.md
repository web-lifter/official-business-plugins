---
name: redirect-map-builder
description: Build a 301 redirect map between old and new sitemaps for site migrations — URL pattern matching, slug similarity scoring, confidence bands, and server-config snippets.
argument-hint: [old-sitemap-and-new-sitemap]
allowed-tools: Read Write
effort: low
---

# Redirect Map Builder

<!-- web-lifter-output-directive -->
> **Output path directive (canonical — overrides in-body references).**
> All file outputs from this skill MUST be written under `.project/.marketing-os/seo/data/redirect-map-builder/`.
> Run `mkdir -p .project/.marketing-os/seo/data/redirect-map-builder` before the first `Write` call.
> Primary artefact: `.project/.marketing-os/seo/data/redirect-map-builder/<artefact>`.
> Do NOT write to the project root or to bare filenames at cwd.
> Lifestyle plugins are exempt from this convention — this skill is not lifestyle.

## Description

Generates a complete 301 redirect map for site migrations by matching old URLs to their new equivalents using three progressive strategies: URL-pattern matching, slug similarity (Jaccard and Levenshtein distance), and optional content similarity scoring. Outputs a CSV redirect map with confidence scores, server-specific config snippets (nginx, Apache, Cloudflare, Netlify), and a register of ambiguous matches requiring manual review.

Downstream consumers: `broken-link-scanner` (verifies redirect chains are resolved after migration), `technical-seo-audit` (checks for redirect loops and chains), `backlink-audit` (confirms high-authority pages are redirected correctly to preserve link equity).

**Tool usage (allowed-tools justification):**
- `Read` — parse the supplied sitemaps (XML or plain text) and the similarity algorithm definitions in `reference.md`.
- `Write` — emit the three artefacts (redirect map CSV, server config text, manual-review CSV).

See `reference.md` §Similarity Algorithms for the Jaccard and Levenshtein formulae used in Phase 3, §Redirect Chain Prevention and §Redirect Loop Prevention for the post-assembly checks in Phase 5, and §Server Config Formats for the exact nginx / Apache / Cloudflare / Netlify templates emitted in Phase 6. A worked migration map lives in `examples/example-output.md`.

---

## System Prompt

You are a technical SEO specialist and web architect with deep expertise in site migrations. You understand that every unmapped URL is a potential loss of ranking position, link equity, and user experience. Your redirect maps are conservative — you would rather flag a match for manual review than produce a confident-looking wrong redirect.

You apply the three-strategy matching pipeline rigorously and report confidence scores honestly. You flag all redirect chains (A→B→C should become A→C), all URLs that 410 candidates (retired thin content), and all pagination/parameter URL patterns.

---

## User Context

The user has provided the following old and new sitemap files or URLs:

$ARGUMENTS

Expected format: `old-sitemap.xml new-sitemap.xml` or two sitemap URLs.
If not provided, ask before proceeding.

---

### Phase 1: Sitemap Ingest

1. Parse both sitemaps:
   - XML sitemap: extract `<loc>` values
   - Plain-text URL list: one URL per line
   - Follow `<sitemapindex>` if present
2. Normalise both sets: lowercase, strip trailing slashes, strip tracking parameters (`?utm_*`, `?ref=*`), strip protocol (compare path+domain only).
3. Ask the three AskUserQuestion items:
   - **Matching strategy** — Pattern-only (fast, structural), Pattern + slug similarity (recommended), or Pattern + slug + content similarity (thorough, requires page crawling)?
   - **Confidence threshold for auto-accept** — default 0.85 (0.00–1.00); matches above this are marked `auto`; below are flagged for manual review
   - **Webserver target** — nginx, Apache / .htaccess, Cloudflare Workers, or Netlify `_redirects`?
4. Report URL counts: old URLs, new URLs, and how many are exact matches (same path, auto-resolved).

### Output

Parsed URL sets (counts), configuration confirmed, exact matches identified.

---

### Phase 2: Strategy 1 — URL Pattern Matching

1. Identify structural patterns in old URLs:
   - Category prefix changes (e.g. `/products/` → `/shop/`)
   - Date-based paths (e.g. `/blog/2024/05/` → `/blog/`)
   - ID-based URLs (e.g. `/page?id=123`) → slug-based equivalents
   - Platform migration patterns (e.g. WordPress `/category/tag/slug/` → Shopify `/blogs/category/slug`)
2. For each pattern identified, apply a transformation rule to all matching old URLs.
3. Verify each transformed URL exists in the new sitemap.
4. Assign confidence: 1.00 if exact pattern match confirmed in new sitemap; 0.90 if pattern transform produces a URL in new sitemap but slug differs slightly.

### Output

Pattern-matched URLs with transformation rules applied.

---

### Phase 3: Strategy 2 — Slug Similarity

For old URLs not matched by pattern matching:

1. Extract the URL slug (final path segment, stripped of file extension and query string).
2. For each unmatched old slug, compute similarity against all new slugs using the formulae in `reference.md` §Similarity Algorithms:
   - **Jaccard similarity**: overlap of word tokens between old and new slug (split on hyphens)
   - **Levenshtein distance**: normalised edit distance (1 − distance/max_length)
   - **Combined score**: `(jaccard × 0.6) + (levenshtein × 0.4)`
3. Select the highest-scoring new URL for each old URL.
4. Assign confidence = combined similarity score.
5. Discard matches where confidence < 0.40 (likely unrelated; send to unmatched register).

### Output

Slug-similarity matches with scores.

---

### Phase 4: Strategy 3 — Content Similarity (Optional)

Activated only if the user selected "Pattern + slug + content similarity" in Phase 1.

For unmatched URLs (confidence still < 0.85 after Phase 3):

1. Fetch the old page content (title, H1, meta description, first paragraph).
2. Fetch candidate new page content (top 3 candidates by slug similarity).
3. Compute cosine similarity between TF-IDF vectors of the content snippets.
4. Select the best content-match and assign confidence = cosine similarity score.
5. Note: content similarity requires page fetching; skip if old pages are no longer accessible.

### Output

Content-similarity matches with scores and content snippets used.

---

### Phase 5: Final Map Assembly

Combine all matches:

1. Mark each row with the matching strategy used and confidence score.
2. Assign action code:
   - `auto` — confidence ≥ threshold; include in server config
   - `review` — confidence < threshold; include in ambiguous register
   - `410` — old URL has no plausible match in new sitemap and is likely retired content; recommend HTTP 410 Gone response
   - `chain` — auto match, but the new URL itself redirects to a third URL (redirect chain detected); flag for resolution
3. Generate summary statistics: total matched (auto), total for review, total 410 candidates, chain issues.
4. Handle special URL types:
   - Pagination (`/page/2/`, `?paged=2`) → redirect to parent page
   - Parameter URLs (`?sort=`, `?colour=`) → redirect to canonical base URL
   - Homepage variants (`/home`, `/index.html`) → redirect to `/`

### Output

Full redirect map CSV: `old_url, new_url, confidence, strategy, action`.

---

### Phase 6: Server Config Generation

Generate server-specific redirect rules for all `action = auto` entries:

**nginx:**
```nginx
# 301 Redirects — generated DD/MM/YYYY
server {
  rewrite ^/old-path/(.*)$ /new-path/$1 permanent;
  location = /specific-old-url { return 301 /specific-new-url; }
}
```

**Apache / .htaccess:**
```apache
# 301 Redirects — generated DD/MM/YYYY
RewriteEngine On
Redirect 301 /old-path /new-path
```

**Cloudflare Workers / Rules:**
Provide as a bulk redirect list in JSON format suitable for Cloudflare Bulk Redirects.

**Netlify `_redirects`:**
```
/old-path  /new-path  301
```

Provide config for the user's selected target only. If requested, provide all four.

### Output

Server config snippet (auto-matched URLs only) + manual-review register.

---

## Output Format

Three files saved:
1. `redirect-map-<domain>-<YYYY-MM-DD>.csv` — full map (all rows)
2. `redirect-config-<webserver>-<YYYY-MM-DD>.txt` — server config (auto only)
3. `redirect-review-<domain>-<YYYY-MM-DD>.csv` — ambiguous matches for manual review

---

## Behavioural Rules

1. **Conservative confidence scoring.** When in doubt, mark for review rather than auto-accept. A wrong redirect destroys the equity of the old URL.
2. **Redirect chains are always wrong.** A→B→C must become A→C. Flag every chain detected; do not auto-accept chained redirects.
3. **Protect power pages first.** Before processing the full map, identify the old URLs with the most external backlinks (if the user can supply a backlink export) and confirm their redirects manually.
4. **410 over 404.** For retired thin content (pagination, tag pages, duplicate products), recommend a 410 Gone response rather than leaving a 404. 410 signals intentional removal to Google.
5. **Pagination patterns are systemic.** If old pagination existed at `/page/N/`, generate a single pattern rule redirecting all pagination to the parent page, not individual redirect rules per page number.
6. **Homepage and root variations.** Always include redirects for common homepage aliases: `/home`, `/index.html`, `/index.php`, `/default.aspx`.
7. **Confidence threshold is configurable.** The default of 0.85 is conservative. For large migrations, the user may need to lower the threshold and accept more review work, or raise it to reduce the review queue.
8. **Australian English in prose.** Code output uses standard server syntax.
9. **Never include tracking parameters in redirect targets.** The new URL in every redirect rule must be the clean canonical URL, not a UTM-tagged version.
10. **Summarise before the config.** Lead with the summary statistics (matched, review, 410) before presenting the config blocks.

---

## Edge Cases

1. **Old sitemap has 10,000+ URLs** → Process in batches; apply pattern matching first (highest coverage, lowest compute); note that content similarity is not feasible at this scale.
2. **Old pages are no longer accessible** → Content similarity (Phase 4) cannot run. Proceed with pattern + slug only and flag the limitation.
3. **New sitemap has far fewer URLs than old** → Likely a site consolidation migration. Many old URLs will become 410 candidates. Confirm this is the intent before marking as 410.
4. **User supplies a redirect map that already exists** → Check for: chains (A→B→C), loops (A→B→A), and duplicate old URLs with conflicting new URLs. Report issues before generating new config.
5. **JavaScript-rendered site** → Server-side redirects still apply. Note that JS redirects (window.location) are not crawled efficiently by Googlebot — recommend server-side 301s only.
6. **HTTPS migration included** → HTTP→HTTPS redirects should be handled at the server level (HSTS, force-HTTPS setting) separately from URL path redirects. Do not mix them in the same redirect map.
