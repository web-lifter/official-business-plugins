# Redirect Map Builder — Reference Framework

## Redirect Map Best Practice

### Redirect Types

| Code | Name | Use Case |
|---|---|---|
| 301 | Moved Permanently | Standard redirect for site migrations; passes ~95% of link equity |
| 302 | Found (Temporary) | Temporary redirect; do NOT use for migrations — no equity transfer |
| 307 | Temporary Redirect | HTTP/1.1 equivalent of 302; same caveat |
| 308 | Permanent Redirect | Like 301 but preserves HTTP method; rarely needed for SEO |
| 410 | Gone | Content permanently removed; faster de-indexation than 404 |
| 404 | Not Found | Avoid where a redirect is possible; loses all link equity |

**Migration rule:** All URL changes = 301. No exceptions. 302s will be treated as temporary by Google and will not fully transfer equity.

---

## Redirect Chain Prevention

A redirect chain occurs when redirecting A→B where B itself redirects to C.

**Problem:** Each additional hop in a chain reduces the link equity transferred and slows page load time. Google will typically follow up to 5 hops before giving up, but equity degrades at each step.

**Detection:** Before finalising the redirect map, check every `new_url` to confirm it does not itself redirect. If it does, update the old_url's target to the final destination directly.

**Example of a chain to fix:**
```
WRONG:  /old-page → /interim-page → /final-page
RIGHT:  /old-page → /final-page
        /interim-page → /final-page
```

---

## Redirect Loop Prevention

A redirect loop occurs when A→B→A (or any circular chain).

**Detection:** Run a DFS/BFS traversal of the redirect graph after assembly. Any cycle = loop.

**Fix:** Break the loop by identifying which destination URL is canonical and redirecting all others to it.

---

## 1:1 Redirect Preference

Each old URL should map to exactly one new URL. Situations requiring attention:

- **Duplicate old URLs (same new URL):** Multiple old URLs pointing to one new URL is fine (consolidation). Common in category restructures.
- **Same old URL, multiple candidate new URLs:** This is a data error. The old URL can only have one destination. Choose the highest-confidence match and flag the others for review.
- **New URL has no old URL (new content):** No redirect needed. New pages start without equity.

---

## Handling Pagination

Old pagination URLs (`/products/?page=2`, `/blog/page/3/`) should redirect to the base page, not to a new pagination structure.

**Reason:** Pagination pages are thin by definition and have no meaningful link equity. Individual paginated pages should not exist as redirect targets.

**Pattern rule:**
```nginx
location ~ ^/products/page/\d+/?$ {
    return 301 /products/;
}
```

---

## Handling Parametrised URLs

URL parameters (`?sort=price`, `?colour=red`, `?filter=in-stock`) should be stripped and redirected to the canonical base URL.

**Reason:** These are usually faceted navigation or filtered views, not unique content. Redirecting each parameter combination individually is impractical and unnecessary.

**Apache pattern:**
```apache
RewriteCond %{QUERY_STRING} ^(sort|colour|filter|ref)=
RewriteRule ^old-path(.*)$ /new-path? [R=301,L]
```

---

## Similarity Algorithms

### Jaccard Similarity (Token Set)

Slug tokenisation: split on hyphens and underscores.

```
jaccard(A, B) = |tokens(A) ∩ tokens(B)| / |tokens(A) ∪ tokens(B)|
```

Example:
- A slug: `best-hiking-boots-australia` → tokens: {best, hiking, boots, australia}
- B slug: `top-hiking-boots-au` → tokens: {top, hiking, boots, au}
- Intersection: {hiking, boots} = 2
- Union: {best, hiking, boots, australia, top, au} = 6
- Jaccard = 2/6 = 0.333

### Levenshtein Distance (Normalised)

```
levenshtein_norm(A, B) = 1 - (edit_distance(A, B) / max(len(A), len(B)))
```

### Combined Score

```
combined = (jaccard × 0.6) + (levenshtein_norm × 0.4)
```

Jaccard is weighted higher because it captures semantic token overlap better than character-level edit distance for URL slugs.

---

## Server Config Formats

### nginx (location block)

```nginx
# Individual URLs (exact match)
location = /old-url-path { return 301 /new-url-path; }

# Pattern-based (regex)
location ~* ^/old-category/(.+)$ { return 301 /new-category/$1; }
```

### Apache / .htaccess

```apache
RewriteEngine On
# Individual URLs
Redirect 301 /old-url-path /new-url-path

# Pattern-based
RewriteRule ^old-category/(.+)$ /new-category/$1 [R=301,L]
```

### Cloudflare Bulk Redirects (JSON)

```json
[
  {
    "source_url": "https://old-domain.com/old-path",
    "target_url": "https://new-domain.com/new-path",
    "status_code": 301,
    "preserve_query_string": false
  }
]
```

### Netlify `_redirects` file

```
/old-path    /new-path    301
/old-category/*    /new-category/:splat    301
```

---

## Power Pages: Prioritisation

Before processing the full map, identify "power pages" — old URLs with:
- Significant external backlinks (DR/DA signal)
- High historical organic traffic (from analytics or GSC export)
- Known editorial links (cited in press, linked from high-DR domains)

These must be manually reviewed even if the automated confidence is above threshold. The cost of getting one wrong outweighs the value of automation.

---

## Key References

- Google Search Central: Redirects and Google Search
- Screaming Frog: Site migration redirect crawling
- Ahrefs: How 301 redirects affect link equity (empirical tests)
- Moz: Redirect chains and equity leakage
