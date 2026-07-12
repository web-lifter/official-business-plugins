# Technical SEO Audit — {{domain}}

**Date:** {{date_dd_mm_yyyy}}
**Audit Depth:** {{audit_depth}}
**Pages Crawled:** {{pages_crawled}} / {{max_pages}} max
**Subdomains Included:** {{subdomains}}
**Technical Health Score:** {{health_score}}/100

---

## Executive Summary

{{executive_summary}}

---

## Findings Register

| # | Pillar | Issue | Severity | Evidence | SEO Impact | Fix |
|---|---|---|---|---|---|---|
| 1 | {{pillar_1}} | {{issue_1}} | {{severity_1}} | {{evidence_1}} | {{impact_1}} | {{fix_1}} |
| 2 | {{pillar_2}} | {{issue_2}} | {{severity_2}} | {{evidence_2}} | {{impact_2}} | {{fix_2}} |
| … | … | … | … | … | … | … |

**Total findings:** {{total_findings}} (Critical: {{crit_count}}, High: {{high_count}}, Medium: {{med_count}}, Low: {{low_count}})

---

## Priority Fix Queue

### Critical — Fix Within 1 Week

| # | Issue | Pillar | Fix |
|---|---|---|---|
| 1 | {{crit_issue_1}} | {{crit_pillar_1}} | {{crit_fix_1}} |

### High — Fix Within 30 Days

| # | Issue | Pillar | Fix |
|---|---|---|---|
| 1 | {{high_issue_1}} | {{high_pillar_1}} | {{high_fix_1}} |

### Medium — Fix Within 60 Days

| # | Issue | Pillar | Fix |
|---|---|---|---|
| 1 | {{med_issue_1}} | {{med_pillar_1}} | {{med_fix_1}} |

---

## Crawl Pillar

### robots.txt
```
{{robots_txt_summary}}
```
**Issues:** {{robots_issues_or_none}}

### Sitemap
- **URL:** `{{sitemap_url}}`
- **URL count:** {{sitemap_url_count}}
- **Last modified (most recent):** {{sitemap_lastmod}}
- **Issues:** {{sitemap_issues_or_none}}

### HTTP Status Distribution

| Status | Count | % |
|---|---|---|
| 200 OK | {{count_200}} | {{pct_200}} |
| 301 Redirect | {{count_301}} | {{pct_301}} |
| 302 Redirect | {{count_302}} | {{pct_302}} |
| 404 Not Found | {{count_404}} | {{pct_404}} |
| 500 Server Error | {{count_500}} | {{pct_500}} |
| Other | {{count_other}} | {{pct_other}} |

### Redirect Chains (> 1 hop)
{{redirect_chains_or_none}}

### 4xx Pages (linked from internal content)
{{linked_404_list_or_none}}

### Internal Link Depth Distribution

| Click Depth | URL Count | % of Crawled |
|---|---|---|
| 1 | {{depth_1}} | {{depth_1_pct}} |
| 2 | {{depth_2}} | {{depth_2_pct}} |
| 3 | {{depth_3}} | {{depth_3_pct}} |
| 4 | {{depth_4}} | {{depth_4_pct}} |
| 5+ | {{depth_5plus}} | {{depth_5plus_pct}} |

---

## Render Pillar

{{#if render_phase_run}}
### JS/HTML Parity Sample ({{render_sample_size}} pages)

| URL | Raw HTML Links | Rendered Links | Parity | Issue |
|---|---|---|---|---|
| {{r_url_1}} | {{r_raw_1}} | {{r_rendered_1}} | {{r_parity_1}} | {{r_issue_1}} |

### Framework Detected
**CMS/Framework:** {{framework}}
**Rendering mode:** {{rendering_mode}} (SSR / CSR / SSG / ISR)
**Recommendation:** {{render_recommendation}}
{{else}}
_Render phase skipped (depth: Crawl-only)._
{{/if}}

---

## Index Pillar

### URL Count Comparison

| Source | Count |
|---|---|
| XML Sitemap | {{sitemap_count}} |
| Crawled URLs (200 OK) | {{crawled_200}} |
| `site:{{domain}}` estimate | {{site_query_count}} |

**Discrepancy:** {{index_discrepancy_notes}}

### Canonical Issues
{{canonical_issues_or_none}}

### noindex Anomalies
{{noindex_anomalies_or_none}}

### Hreflang (if applicable)
{{hreflang_findings_or_none}}

---

## Rank Pillar

### Core Web Vitals Summary

| URL | LCP (mob) | INP (mob) | CLS (mob) | LCP (desk) | INP (desk) | CLS (desk) | PSI Score (mob) |
|---|---|---|---|---|---|---|---|
| {{cwv_url_1}} | {{cwv_lcp_m_1}} | {{cwv_inp_m_1}} | {{cwv_cls_m_1}} | {{cwv_lcp_d_1}} | {{cwv_inp_d_1}} | {{cwv_cls_d_1}} | {{cwv_psi_1}} |
| … | … | … | … | … | … | … | … |

### CWV Root Causes
{{cwv_root_causes}}

### Schema Coverage

| Schema Type | Pages With | Pages Needing | Gap |
|---|---|---|---|
| {{schema_type_1}} | {{schema_with_1}} | {{schema_need_1}} | {{schema_gap_1}} |

### Schema Validation Issues
{{schema_validation_issues_or_none}}

---

## Raw Data Paths

| File | Path |
|---|---|
| Crawl output | `{{crawl_json_path}}` |
| CWV output | `{{cwv_json_path}}` |
