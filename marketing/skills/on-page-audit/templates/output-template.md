# On-Page Audit Report — {{site_name}}

**Date:** {{date_dd_mm_yyyy}}
**Mode:** {{mode}} | **URLs Audited:** {{urls_audited}} | **Primary Keyword:** {{primary_keyword_or_none}}

---

## Aggregate Summary

| Severity | Issue Count | URLs Affected |
|---|---|---|
| Critical | {{critical_count}} | {{critical_urls}} |
| High | {{high_count}} | {{high_urls}} |
| Medium | {{medium_count}} | {{medium_urls}} |
| Low | {{low_count}} | {{low_urls}} |

---

## Issue Frequency

| Check | Pass Rate | Systemic? |
|---|---|---|
| Title tag exists | {{pct_title_exists}} | {{systemic_title}} |
| Title length (50–60 chars) | {{pct_title_length}} | {{systemic_title_len}} |
| Meta description exists | {{pct_meta_exists}} | {{systemic_meta}} |
| Meta description length | {{pct_meta_length}} | {{systemic_meta_len}} |
| Single H1 | {{pct_h1}} | {{systemic_h1}} |
| Heading hierarchy | {{pct_headings}} | {{systemic_headings}} |
| Internal link density | {{pct_internal_links}} | {{systemic_links}} |
| Alt text ≥ 90% | {{pct_alt_text}} | {{systemic_alt}} |
| Canonical present | {{pct_canonical}} | {{systemic_canonical}} |
| Schema present | {{pct_schema}} | {{systemic_schema}} |
| OG tags complete | {{pct_og}} | {{systemic_og}} |
| Not noindex | {{pct_noindex}} | {{systemic_noindex}} |

---

## Critical and High Issues

| URL | Issue | Found | Expected | Severity |
|---|---|---|---|---|
| {{url_1}} | {{issue_1}} | {{found_1}} | {{expected_1}} | {{severity_1}} |
| {{url_2}} | {{issue_2}} | {{found_2}} | {{expected_2}} | {{severity_2}} |
| … | … | … | … | … |

---

## Quick Wins (Easy fix, ≥ 30% of pages affected)

| Issue | Pages Affected | Fix |
|---|---|---|
| {{qw_issue_1}} | {{qw_count_1}} | {{qw_fix_1}} |
| {{qw_issue_2}} | {{qw_count_2}} | {{qw_fix_2}} |

---

## Top 10 Worst Pages (by issue score)

| # | URL | Critical | High | Medium | Low | Score |
|---|---|---|---|---|---|---|
| 1 | {{worst_url_1}} | {{w1_crit}} | {{w1_high}} | {{w1_med}} | {{w1_low}} | {{w1_score}} |
| 2 | {{worst_url_2}} | {{w2_crit}} | {{w2_high}} | {{w2_med}} | {{w2_low}} | {{w2_score}} |
| … | … | … | … | … | … | … |

---

## Prioritised Fix List

| Priority | Fix | Severity | Pages Affected | Effort |
|---|---|---|---|---|
| 1 | {{fix_1}} | {{fix_1_sev}} | {{fix_1_pages}} | {{fix_1_effort}} |
| 2 | {{fix_2}} | {{fix_2_sev}} | {{fix_2_pages}} | {{fix_2_effort}} |
| … | … | … | … | … |

---

## Per-URL Scorecards

### {{url_1}}

| Check | Result | Found | Expected | Severity |
|---|---|---|---|---|
| Title tag | {{u1_title_result}} | {{u1_title_found}} | 50–60 chars | {{u1_title_sev}} |
| Meta description | {{u1_meta_result}} | {{u1_meta_found}} | 150–160 chars | {{u1_meta_sev}} |
| H1 count | {{u1_h1_result}} | {{u1_h1_found}} | Exactly 1 | {{u1_h1_sev}} |
| Heading hierarchy | {{u1_headings_result}} | {{u1_headings_found}} | No skipped levels | {{u1_headings_sev}} |
| Internal links | {{u1_links_result}} | {{u1_links_found}} | ≥ 2 per 500 words | {{u1_links_sev}} |
| Alt text coverage | {{u1_alt_result}} | {{u1_alt_found}} | ≥ 90% | {{u1_alt_sev}} |
| Word count | {{u1_wc_result}} | {{u1_wc_found}} | {{u1_wc_expected}} | {{u1_wc_sev}} |
| Canonical | {{u1_can_result}} | {{u1_can_found}} | Self-referencing | {{u1_can_sev}} |
| Schema | {{u1_schema_result}} | {{u1_schema_found}} | ≥ 1 type | {{u1_schema_sev}} |
| OG tags | {{u1_og_result}} | {{u1_og_found}} | All 3 present | {{u1_og_sev}} |
| Twitter card | {{u1_tw_result}} | {{u1_tw_found}} | Present | {{u1_tw_sev}} |
| robots meta | {{u1_robots_result}} | {{u1_robots_found}} | Not noindex | {{u1_robots_sev}} |

_(Repeat scorecard for each URL)_
