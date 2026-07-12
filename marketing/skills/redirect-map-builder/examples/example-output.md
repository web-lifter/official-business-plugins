# Redirect Map — outdoorhaven.com.au Migration

**Date:** 15/05/2026
**Old sitemap:** old-sitemap.xml (WooCommerce / WordPress)
**New sitemap:** new-sitemap.xml (Shopify)
**Matching strategy:** Pattern + Slug Similarity
**Confidence threshold:** 0.85
**Webserver target:** nginx

---

## Summary Statistics

| Metric | Count |
|---|---|
| Old URLs parsed | 1,247 |
| New URLs parsed | 891 |
| Exact matches (auto) | 312 |
| Pattern-matched (auto) | 418 |
| Slug-similarity matched (auto) | 167 |
| Content-similarity matched (auto) | — (not run) |
| Flagged for review | 112 |
| 410 candidates | 238 |
| Redirect chains detected | 14 |
| Total auto-accepted | 897 (72% of old URLs) |

**Pattern rules identified:**
- `/product/` → `/products/` (WooCommerce → Shopify product URL structure) — 401 URLs
- `/product-category/` → `/collections/` (WooCommerce categories → Shopify collections) — 28 URLs
- `/shop/` → `/collections/all` — 1 URL
- `/wp-content/uploads/` — flagged as 410 (media not served from Shopify)

---

## Redirect Map CSV (Sample — first 20 rows)

```csv
old_url,new_url,confidence,strategy,action
/product/osprey-atmos-65-backpack/,/products/osprey-atmos-65-ag-backpack,0.94,pattern+slug,auto
/product/north-face-thermoball-jacket/,/products/the-north-face-thermoball-eco-jacket,0.87,slug,auto
/product/msr-hubba-hubba-2-tent/,/products/msr-hubba-hubba-nx-2-person-tent,0.91,slug,auto
/product/sea-to-summit-sleeping-bag-liner/,/products/sea-to-summit-reactor-plus-sleeping-bag-liner,0.85,slug,auto
/product/black-diamond-headlamp/,/products/black-diamond-spot-400-headlamp,0.82,slug,review
/product-category/tents/,/collections/tents,1.00,pattern,auto
/product-category/sleeping-bags/,/collections/sleeping-bags,1.00,pattern,auto
/product-category/backpacks/,/collections/backpacks,1.00,pattern,auto
/product-category/clothing/,/collections/outdoor-clothing,0.91,slug,auto
/product-category/footwear/,/collections/hiking-footwear,0.88,slug,auto
/blog/how-to-choose-a-sleeping-bag/,/blogs/guides/choosing-a-sleeping-bag,0.90,slug,auto
/blog/best-hiking-trails-victoria/,/blogs/guides/best-hiking-trails-victoria,0.98,slug,auto
/shop/,/collections/all,1.00,pattern,auto
/page/2/,/collections/all,1.00,pattern-pagination,auto
/page/3/,/collections/all,1.00,pattern-pagination,auto
/about-us/,/pages/about,0.93,slug,auto
/contact/,/pages/contact-us,0.88,slug,auto
/privacy-policy/,/pages/privacy-policy,1.00,exact,auto
/terms-and-conditions/,/pages/terms-of-service,0.86,slug,auto
/cart/,/cart,1.00,exact,auto
```

---

## Server Config — nginx (Sample)

```nginx
# Redirect map for outdoorhaven.com.au → Shopify migration
# Generated 15/05/2026
# Auto-accepted matches only (confidence ≥ 0.85)

server {
    # PATTERN RULES — apply first (most efficient)

    # WooCommerce products → Shopify products
    location ~* ^/product/(.+?)/?$ {
        return 301 /products/$1;
    }

    # WooCommerce categories → Shopify collections
    location ~* ^/product-category/(.+?)/?$ {
        return 301 /collections/$1;
    }

    # Blog path restructure
    location ~* ^/blog/(.+?)/?$ {
        return 301 /blogs/guides/$1;
    }

    # Pagination → parent collection
    location ~* ^/page/\d+/?$ {
        return 301 /collections/all;
    }

    # Shop root
    location = /shop/ { return 301 /collections/all; }

    # INDIVIDUAL URL OVERRIDES (slug-matched; override pattern rules where needed)

    # Category name changes
    location = /product-category/clothing/ { return 301 /collections/outdoor-clothing; }
    location = /product-category/footwear/ { return 301 /collections/hiking-footwear; }

    # Static pages
    location = /about-us/ { return 301 /pages/about; }
    location = /contact/ { return 301 /pages/contact-us; }
    location = /terms-and-conditions/ { return 301 /pages/terms-of-service; }

    # Specific product overrides (slug changed in new site)
    location = /product/north-face-thermoball-jacket/ { return 301 /products/the-north-face-thermoball-eco-jacket; }
    location = /product/msr-hubba-hubba-2-tent/ { return 301 /products/msr-hubba-hubba-nx-2-person-tent; }
    location = /product/sea-to-summit-sleeping-bag-liner/ { return 301 /products/sea-to-summit-reactor-plus-sleeping-bag-liner; }
}
```

---

## Ambiguous Matches — Manual Review Required (Sample)

```csv
old_url,best_candidate_new_url,confidence,strategy,notes
/product/black-diamond-headlamp/,/products/black-diamond-spot-400-headlamp,0.82,slug,Product name changed significantly — verify this is the correct SKU replacement
/product/mont-sleeping-bag-winter/,/products/mont-latitude-0-sleeping-bag,0.71,slug,Mont product line renamed in new catalogue — confirm mapping with product team
/product-category/accessories/,/collections/camping-accessories,0.79,slug,Category renamed — confirm scope matches old category contents
/blog/gear-review-2023-wrap-up/,/blogs/guides/2023-gear-highlights,0.68,slug,Year-end roundup articles rarely have exact equivalents — check if new article covers same content
/about-us/team/,/pages/our-story,0.64,slug,Team page removed in new site? Redirect to about or careers page
/wholesale/,/pages/trade-accounts,0.61,slug,Wholesale programme page — may have changed significantly; manual review
```

**112 rows total in review file. Estimated manual review time: 3–4 hours.**

---

## 410 Candidates (Sample)

| Old URL | Reason | Recommended Action |
|---|---|---|
| /wp-content/uploads/2022/product-images/ | WordPress media path — not migrated | Return 410 Gone |
| /product-tag/sale/ | WooCommerce tag page — no equivalent in Shopify | Return 410 Gone |
| /product-tag/clearance/ | WooCommerce tag page | Return 410 Gone |
| /feed/ | WordPress RSS feed | Return 410 Gone |
| /author/admin/ | WordPress author archive | Return 410 Gone |
| /page/4/ through /page/47/ | Pagination pages | Return 410 Gone (or 301 to /collections/all — already handled by pattern rule above) |
| /product/discontinued-snowshoe-model/ | Product removed from new catalogue | Return 410 Gone |

**238 total 410 candidates. Recommend adding a blanket rule for `/wp-content/` and WordPress-specific paths.**

---

## Redirect Chain Issues

The following 14 redirects must be updated before deployment:

| Old URL | Current Target | Final Destination | Fix Required |
|---|---|---|---|
| /hiking-gear/ | /product-category/hiking/ | /collections/hiking-gear | Update direct: `/hiking-gear/` → `/collections/hiking-gear` |
| /sale-items/ | /product-category/sale/ | /collections/sale | Update direct: `/sale-items/` → `/collections/sale` |
| /outdoor-clothing/ | /product-category/clothing/ | /collections/outdoor-clothing | Update direct |
| /trekking-poles/ | /product/trekking-poles/ | /products/trekking-poles | Update direct |

*(10 additional chain items in full redirect map CSV)*

**Action:** Update the `new_url` field in `redirect-map-outdoorhaven.com.au-2026-05-15.csv` for all 14 chain rows before deploying the nginx config.

---

*Generated by marketing / redirect-map-builder*
