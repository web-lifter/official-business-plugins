# Operational Bottleneck Analysis — {{business_name}}

**Date:** {{date_dd_mm_yyyy}}
**Process domain:** {{process_domain}}
**Data source:** {{data_source_type}}
**Analysis prepared by:** Operational Bottleneck Detector skill

---

## Executive Summary

- {{key_finding_1}}
- {{key_finding_2}}
- {{key_finding_3}}

---

## Process Map

| Stage | Input | Output | Role / System | CT (avg) | WIP | SLA | Value-Added? |
|-------|-------|--------|--------------|---------|-----|-----|-------------|
| {{stage_1}} | {{input}} | {{output}} | {{role}} | {{ct}} | {{wip}} | {{sla}} | Yes / No |
| {{stage_2}} | {{input}} | {{output}} | {{role}} | {{ct}} | {{wip}} | {{sla}} | Yes / No |
| {{stage_3}} | {{input}} | {{output}} | {{role}} | {{ct}} | {{wip}} | {{sla}} | Yes / No |

**Total lead time:** {{total_lead_time}}
**Value-added time:** {{value_added_time}}
**Process efficiency:** {{process_efficiency}}%

---

## Value-Stream Map

```mermaid
flowchart LR
  Input([{{trigger}}])

  subgraph S1["{{stage_1}}"]
    direction TB
    S1CT["CT: {{ct_1}}"]
    S1WIP["WIP: {{wip_1}}"]
  end

  subgraph S2["{{stage_2}} ⚠️ BOTTLENECK"]
    direction TB
    S2CT["CT: {{ct_2}}"]
    S2WIP["WIP: {{wip_2}} HIGH"]
  end

  subgraph S3["{{stage_3}}"]
    direction TB
    S3CT["CT: {{ct_3}}"]
    S3WIP["WIP: {{wip_3}}"]
  end

  Input --> S1
  S1 -->|"Wait: {{wait_1}}"| S2
  S2 -->|"Wait: {{wait_2}}"| S3
  S3 --> Output([{{output_name}}])
```

---

## Throughput Analysis

| Stage | Mean CT | Median CT | P90 CT | Avg WIP | Throughput/day | Little's Law WIP | Consistent? |
|-------|---------|----------|--------|---------|---------------|-----------------|------------|
| {{stage}} | {{mean}} | {{median}} | {{p90}} | {{wip}} | {{tput}} | {{ll_wip}} | Yes / No ⚠️ |

**Overall throughput loss:** {{throughput_loss}}% ({{units_lost}} {{unit_type}} per {{period}} below theoretical capacity)

---

## Bottleneck Register

| # | Location | Root-Cause Category | Severity (1–5) | Evidence | Throughput Loss | Fix Type |
|---|---------|-------------------|---------------|---------|----------------|---------|
| 1 | {{stage}} | People / Process / Systems / Supply | {{severity}} | Data / Interview / Estimate | {{loss}}% | {{fix_type}} |
| 2 | {{stage}} | People / Process / Systems / Supply | {{severity}} | Data / Interview / Estimate | {{loss}}% | {{fix_type}} |

### Bottleneck 1: {{bottleneck_name}}

**Root-cause chain (5 Whys):**
1. Why: {{why_1}}
2. Why: {{why_2}}
3. Why: {{why_3}}
4. Why: {{why_4}}
5. Root cause: {{root_cause}}

---

## Remediation Queue

| Priority | Stage | Fix | Type | Expected Uplift | Effort | Owner | Start |
|---------|-------|-----|------|----------------|--------|-------|-------|
| P1 | {{stage}} | {{fix_description}} | Quick win / Process / System / Structural | {{uplift}}% | Low / Med / High | {{role}} | {{date}} |
| P2 | {{stage}} | {{fix_description}} | Quick win / Process / System / Structural | {{uplift}}% | Low / Med / High | {{role}} | {{date}} |
| P3 | {{stage}} | {{fix_description}} | Quick win / Process / System / Structural | {{uplift}}% | Low / Med / High | {{role}} | {{date}} |

---

## Constraint Cascade Warning

Once the primary constraint ({{primary_bottleneck}}) is resolved, the next binding constraint is likely to be **{{next_bottleneck}}** (currently at {{next_wip}} WIP with {{next_ct}} average cycle time). Monitor this stage immediately after the P1 fix is implemented.

---

## Recommended KPIs to Track Post-Fix

1. {{kpi_1}} — tracks resolution of primary constraint
2. {{kpi_2}} — early warning for cascade constraint
3. {{kpi_3}} — overall throughput health
