# Keyword Research Report — {{business_name}}

**Market / Locale:** {{locale}}
**Primary Intent Target:** {{intent_target}}
**Volume Floor:** {{volume_floor}} searches/month
**Research Date:** {{date_dd_mm_yyyy}}
**Seeds:** {{seed_terms}}
**CSV saved to:** `{{csv_path}}`

---

## Summary

| Metric | Value |
|---|---|
| Total keywords | {{total_keywords}} |
| After deduplication | {{deduplicated_count}} |
| After volume filter | {{post_filter_count}} |
| Parent topics identified | {{parent_topic_count}} |
| API sources used | {{sources_used}} |

### By Intent

| Intent | Count | % of Total |
|---|---|---|
| Informational | {{count_informational}} | {{pct_informational}} |
| Commercial | {{count_commercial}} | {{pct_commercial}} |
| Transactional | {{count_transactional}} | {{pct_transactional}} |
| Navigational | {{count_navigational}} | {{pct_navigational}} |
| Mixed Intent | {{count_mixed}} | {{pct_mixed}} |

### By Difficulty Band

| Band | Score Range | Count |
|---|---|---|
| Easy | 0–30 | {{count_easy}} |
| Medium | 31–60 | {{count_medium}} |
| Hard | 61+ | {{count_hard}} |

---

## Top 20 Keywords by Volume

| # | Keyword | Volume | Difficulty | Band | Intent | Sub-Intent | Parent Topic |
|---|---|---|---|---|---|---|---|
| 1 | {{kw_1}} | {{vol_1}} | {{diff_1}} | {{band_1}} | {{intent_1}} | {{sub_1}} | {{parent_1}} |
| 2 | {{kw_2}} | {{vol_2}} | {{diff_2}} | {{band_2}} | {{intent_2}} | {{sub_2}} | {{parent_2}} |
| … | … | … | … | … | … | … | … |

---

## Quick Wins (Volume ≥ {{volume_floor}}, Difficulty ≤ 30)

| # | Keyword | Volume | Difficulty | Intent | Parent Topic |
|---|---|---|---|---|---|
| 1 | {{qw_kw_1}} | {{qw_vol_1}} | {{qw_diff_1}} | {{qw_intent_1}} | {{qw_parent_1}} |
| … | … | … | … | … | … |

---

## Keyword Clusters by Parent Topic

### {{parent_topic_1}} ({{pt1_volume}} total volume, {{pt1_count}} keywords)

| Keyword | Volume | Difficulty | Band | Intent | Sub-Intent |
|---|---|---|---|---|---|
| {{pt1_kw_1}} | {{pt1_vol_1}} | {{pt1_diff_1}} | {{pt1_band_1}} | {{pt1_intent_1}} | {{pt1_sub_1}} |
| … | … | … | … | … | … |

### {{parent_topic_2}} ({{pt2_volume}} total volume, {{pt2_count}} keywords)

| Keyword | Volume | Difficulty | Band | Intent | Sub-Intent |
|---|---|---|---|---|---|
| {{pt2_kw_1}} | {{pt2_vol_1}} | {{pt2_diff_1}} | {{pt2_band_1}} | {{pt2_intent_1}} | {{pt2_sub_1}} |

_(Repeat section for each parent topic)_

---

## Data Quality Notes

{{#if estimated_metrics}}
**Estimated metrics** (live API data unavailable):
- {{estimated_note_1}}
{{/if}}

{{#if off_topic_exclusions}}
**Off-topic exclusions:** {{off_topic_count}} keywords removed
- {{off_topic_example_1}} — {{off_topic_reason_1}}
{{/if}}

{{#if api_errors}}
**API errors:**
- {{api_error_1}}
{{/if}}

---

## Recommended Next Steps

1. Run **`keyword-list-developer`** with this CSV (`{{csv_path}}`) to expand coverage and enrich with competitor and GSC data.
2. Alternatively, run **`keyword-clustering-and-mapping`** directly if the list is already comprehensive.
3. For high-priority keywords, run **`serp-analysis`** to understand the competitive landscape before committing to content creation.
