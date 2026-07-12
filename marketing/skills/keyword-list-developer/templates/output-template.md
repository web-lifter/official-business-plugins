# Keyword Master List — {{business_name}}

**Market / Locale:** {{locale}}
**Volume Floor:** {{volume_floor}} searches/month
**Maximum List Size:** {{max_list_size}}
**Include Branded:** {{include_branded}}
**Research Date:** {{date_dd_mm_yyyy}}
**CSV saved to:** `{{csv_path}}`

---

## Summary

| Metric | Value |
|---|---|
| Total keywords in master list | {{total_keywords}} |
| Raw candidates (pre-filter) | {{raw_count}} |
| Removed (volume < floor) | {{removed_volume}} |
| Removed (off-topic) | {{removed_offtopic}} |
| Removed (duplicates) | {{removed_duplicates}} |
| Sources used | {{sources_list}} |

### By Intent

| Intent | Count | % of Total |
|---|---|---|
| Informational | {{count_informational}} | {{pct_informational}} |
| Commercial | {{count_commercial}} | {{pct_commercial}} |
| Transactional | {{count_transactional}} | {{pct_transactional}} |
| Navigational (incl. branded) | {{count_navigational}} | {{pct_navigational}} |

### By Difficulty Band

| Band | Count |
|---|---|
| Easy (0–30) | {{count_easy}} |
| Medium (31–60) | {{count_medium}} |
| Hard (61+) | {{count_hard}} |
| Unknown / Estimated | {{count_estimated}} |

---

## Top 10 by Volume

| # | Keyword | Volume | Difficulty | Intent | Parent Topic | Current URL |
|---|---|---|---|---|---|---|
| 1 | {{kw_1}} | {{vol_1}} | {{diff_1}} | {{intent_1}} | {{parent_1}} | {{url_1}} |
| 2 | {{kw_2}} | {{vol_2}} | {{diff_2}} | {{intent_2}} | {{parent_2}} | {{url_2}} |
| … | … | … | … | … | … | … |

---

## Top 10 Quick Wins (Volume ≥ {{volume_floor}}, Difficulty ≤ 30)

| # | Keyword | Volume | Difficulty | Intent | Parent Topic |
|---|---|---|---|---|---|
| 1 | {{qw_1}} | {{qw_vol_1}} | {{qw_diff_1}} | {{qw_intent_1}} | {{qw_parent_1}} |
| … | … | … | … | … | … |

---

## Data Quality Notes

**Estimated volume records:** {{estimated_count}} keywords (volume retrieved via LLM/estimation — marked with `-1` in CSV)

**Off-topic exclusions:** {{offtopic_count}} removed
- {{offtopic_example_1}} — {{offtopic_reason_1}}

**Missing difficulty:** {{missing_diff_count}} keywords (marked `-1` in CSV)

**Missing SERP features:** {{missing_serp_count}} keywords (sampled top 50 by volume only)

**GSC data:** {{gsc_status}}

**Competitor extraction:** {{competitor_status}}

---

## Handoff Note

Master list ready. Run `keyword-clustering-and-mapping` with:

```bash
keyword-cluster run \
  --keywords {{csv_path}} \
  --pages <pages.csv> \
  --method kmeans \
  --auto-k silhouette \
  --output .project/.marketing-os/seo/clusters/{{slug}}/
```

Or use the `keyword-clustering-and-mapping` skill which will handle method selection interactively.
