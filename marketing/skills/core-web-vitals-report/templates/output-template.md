# Core Web Vitals Report — {{site_name}}

**Date:** {{date_dd_mm_yyyy}}
**URLs Tested:** {{url_count}}
**Device:** {{device}}
**Data Source:** PSI / CrUX (field) + Lighthouse (lab)
**Raw data:** `{{cwv_json_path}}`

---

## Summary

| Metric | URLs Passing | URLs NI | URLs Failing | Pass Rate |
|---|---|---|---|---|
| LCP | {{lcp_pass}} | {{lcp_ni}} | {{lcp_fail}} | {{lcp_pass_rate}} |
| INP | {{inp_pass}} | {{inp_ni}} | {{inp_fail}} | {{inp_pass_rate}} |
| CLS | {{cls_pass}} | {{cls_ni}} | {{cls_fail}} | {{cls_pass_rate}} |
| **All metrics pass** | {{all_pass}} | — | {{any_fail}} | **{{overall_pass_rate}}** |

**CrUX field data available for:** {{field_data_count}} of {{url_count}} URLs ({{field_data_pct}})

---

## Worst Offenders

| URL | LCP (mob) | INP (mob) | CLS (mob) | PSI Score | Issues |
|---|---|---|---|---|---|
| {{worst_1}} | {{w1_lcp}} | {{w1_inp}} | {{w1_cls}} | {{w1_psi}} | {{w1_issues}} |
| {{worst_2}} | {{w2_lcp}} | {{w2_inp}} | {{w2_cls}} | {{w2_psi}} | {{w2_issues}} |
| {{worst_3}} | {{w3_lcp}} | {{w3_inp}} | {{w3_cls}} | {{w3_psi}} | {{w3_issues}} |
| {{worst_4}} | {{w4_lcp}} | {{w4_inp}} | {{w4_cls}} | {{w4_psi}} | {{w4_issues}} |
| {{worst_5}} | {{w5_lcp}} | {{w5_inp}} | {{w5_cls}} | {{w5_psi}} | {{w5_issues}} |

---

## Full Scorecard — Mobile

| URL | LCP | INP | CLS | PSI | Status | Field Data |
|---|---|---|---|---|---|---|
| {{url_1}} | {{m_lcp_1}} | {{m_inp_1}} | {{m_cls_1}} | {{m_psi_1}} | {{m_status_1}} | {{m_field_1}} |
| {{url_2}} | {{m_lcp_2}} | {{m_inp_2}} | {{m_cls_2}} | {{m_psi_2}} | {{m_status_2}} | {{m_field_2}} |
| … | … | … | … | … | … | … |

{{#if desktop}}
## Full Scorecard — Desktop

| URL | LCP | INP | CLS | PSI | Status | Field Data |
|---|---|---|---|---|---|---|
| {{url_1}} | {{d_lcp_1}} | {{d_inp_1}} | {{d_cls_1}} | {{d_psi_1}} | {{d_status_1}} | {{d_field_1}} |
| … | … | … | … | … | … | … |
{{/if}}

---

## Remediation Recommendations

### {{root_cause_1}} (affects {{rc1_url_count}} URLs — {{rc1_metric}})

**Root cause:** {{rc1_description}}

**Affected URLs:**
- {{rc1_url_1}}
- {{rc1_url_2}}

**Fix:**
{{rc1_fix}}

**Impact:** {{rc1_impact}} | **Effort:** {{rc1_effort}}

---

### {{root_cause_2}} (affects {{rc2_url_count}} URLs — {{rc2_metric}})

**Root cause:** {{rc2_description}}

**Affected URLs:**
- {{rc2_url_1}}

**Fix:**
{{rc2_fix}}

**Impact:** {{rc2_impact}} | **Effort:** {{rc2_effort}}

---

_(Repeat recommendation section for each distinct root cause)_

---

## Data Quality Notes

{{#if missing_field_data}}
**URLs without CrUX field data (low traffic):** {{missing_field_data_count}} URLs — lab data only for these pages.
{{/if}}

{{#if api_rate_limited}}
**PSI rate limiting:** {{rate_limit_note}}
{{/if}}
