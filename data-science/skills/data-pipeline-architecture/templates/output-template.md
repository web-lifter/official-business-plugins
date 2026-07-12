## Data Pipeline Architecture — [Business Name]

### 1. Architecture Overview

- **Purpose:** {{what this pipeline does and what business outcome it enables}}
- **Pattern:** ELT / ETL / Streaming / Hybrid
- **Source Systems:** {{count}} sources
- **Destination:** {{e.g. Supabase PostgreSQL, BigQuery}}
- **Refresh Frequency:** {{e.g. hourly incremental, daily full}}
- **Estimated Data Volume:** {{rows/day or GB/day}}

<!-- Summarise the full pipeline in 2-3 sentences before diving into detail. -->

---

### 2. Data Flow Diagram

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Source A    │────>│  Raw Layer   │────>│  Staging     │────>│  Mart/       │
│  ({{type}}) │     │  (exact copy)│     │  (cleaned)   │     │  Reporting   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                           │
┌─────────────┐            │
│  Source B    │────────────┘
│  ({{type}}) │
└─────────────┘
```

<!-- Show all sources, intermediate layers, and final destinations. -->
<!-- Include branch points, fan-out, and any feedback loops. -->

---

### 3. Source System Integration

For each source:

**Source: {{source_name}}**
- **Type:** API / Database / File / Webhook
- **Connection:** {{connection method and credentials reference}}
- **Schema:** {{key tables or endpoints}}
- **Volume:** {{estimated rows or records per sync}}
- **Freshness Requirement:** {{how stale the data can be}}
- **Change Detection:** {{timestamp column / CDC / full scan}}
- **Extract SQL/Code:**
```sql
-- Incremental extract for {{source_name}}
SELECT *
FROM {{source_table}}
WHERE updated_at > '{{last_sync_timestamp}}'
```

<!-- Repeat for each source system. -->

---

### 4. Transformation Specifications

**Layer Architecture:**

| Layer | Purpose | Naming Convention | Example |
|-------|---------|-------------------|---------|
| Raw | Exact copy of source data | `raw_{{source}}_{{table}}` | `raw_stripe_charges` |
| Staging | Cleaned, typed, deduplicated | `stg_{{source}}_{{table}}` | `stg_stripe_charges` |
| Mart | Business logic applied | `mart_{{domain}}_{{entity}}` | `mart_finance_revenue` |
| Reporting | Aggregated for dashboards | `rpt_{{domain}}_{{view}}` | `rpt_finance_monthly` |

**Transformation: {{transform_name}}**
```sql
-- Purpose: {{what this transform does}}
-- Input: {{source table(s)}}
-- Output: {{target table}}

CREATE TABLE IF NOT EXISTS {{target_table}} AS
SELECT
  {{transformed columns}}
FROM {{source_table}}
WHERE {{filter conditions}};
```

<!-- Repeat for each major transformation. Include DDL for target tables. -->

---

### 5. Orchestration Design

- **Orchestration Tool:** {{pg_cron / n8n / Cloudflare Worker / Airflow}}
- **Schedule:** {{cron expression and human-readable description}}
- **Dependency Chain:**
  1. Extract from Source A
  2. Extract from Source B
  3. Load raw data
  4. Run staging transforms
  5. Run mart transforms
  6. Update reporting views
- **Concurrency:** {{parallel extracts? sequential transforms?}}
- **Trigger Mechanism:** {{cron / webhook / event-driven}}

```sql
-- Example pg_cron schedule
SELECT cron.schedule('pipeline_daily', '0 2 * * *', $$
  SELECT run_pipeline();
$$);
```

---

### 6. Error Handling Strategy

- **Retry Policy:** {{max retries, backoff strategy}}
- **Dead Letter Handling:** {{where failed records go}}
- **Idempotency:** {{how re-runs produce the same result — upsert, merge, truncate-and-reload}}
- **Partial Failure:** {{what happens if one source fails — continue or abort?}}
- **Schema Drift Detection:** {{how to detect when source schemas change}}

```sql
-- Error logging table
CREATE TABLE IF NOT EXISTS pipeline_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  pipeline_name TEXT NOT NULL,
  status TEXT NOT NULL,  -- 'started', 'completed', 'failed'
  rows_processed INTEGER,
  error_message TEXT,
  started_at TIMESTAMPTZ NOT NULL,
  completed_at TIMESTAMPTZ
);
```

---

### 7. Monitoring & Alerting

| Check | Frequency | Condition | Alert Channel |
|-------|-----------|-----------|---------------|
| Pipeline completion | After each run | status != 'completed' | {{Slack / email}} |
| Data freshness | Hourly | last_load > {{threshold}} | {{Slack / email}} |
| Row count anomaly | Daily | deviation > {{%}} from average | {{Slack / email}} |
| Schema change | On each extract | column mismatch detected | {{Slack / email}} |

<!-- Silent failures are the worst failures. Every run must be logged and monitored. -->

---

### 8. Implementation Roadmap

| Phase | Tasks | Duration | Dependencies |
|-------|-------|----------|-------------|
| 1. Foundation | Set up raw layer, logging, error handling | {{timeframe}} | Database access |
| 2. Extract | Build extractors for each source | {{timeframe}} | Source credentials |
| 3. Transform | Build staging and mart layer SQL | {{timeframe}} | Phase 1-2 complete |
| 4. Orchestrate | Configure scheduling and dependencies | {{timeframe}} | Phase 3 complete |
| 5. Monitor | Set up alerting and dashboards | {{timeframe}} | Phase 4 complete |
| 6. Harden | Test with production data, add edge case handling | {{timeframe}} | Phase 5 complete |

**Maintenance Schedule:**
- **Monthly:** Review error logs, check pipeline performance
- **Quarterly:** Assess data volume growth, optimise slow transforms
- **Ad-hoc:** Handle schema changes in source systems
