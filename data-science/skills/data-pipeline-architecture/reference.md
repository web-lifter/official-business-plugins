# Data Pipeline Architecture -- Reference

Supplementary reference material for the data-pipeline-architecture skill. Use alongside SKILL.md for detailed implementation patterns, SQL templates, and decision guides.

---

## Table of Contents

- [Schema Layering Strategy](#schema-layering-strategy)
- [Orchestration Pattern Reference](#orchestration-pattern-reference)
- [Error Handling Patterns](#error-handling-patterns)
- [Monitoring SQL Templates](#monitoring-sql-templates)
- [Source System Integration Patterns](#source-system-integration-patterns)
- [Idempotency Patterns by Pipeline Stage](#idempotency-patterns-by-pipeline-stage)

---

## Schema Layering Strategy

### Raw Layer

The raw layer preserves source data exactly as received. Never transform, filter, or deduplicate here. Every record is sacred.

```sql
-- Raw layer table template
CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE raw.stripe_payments (
  id SERIAL PRIMARY KEY,
  _source_id TEXT NOT NULL,              -- Original record ID from source
  _raw_payload JSONB NOT NULL,           -- Full source payload preserved
  _loaded_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  _source_name TEXT NOT NULL DEFAULT 'stripe',
  _batch_id TEXT,                        -- Groups records from same extraction run
  _valid_from TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  _valid_to TIMESTAMPTZ DEFAULT 'infinity'
);

-- Index for incremental extraction lookups
CREATE INDEX idx_raw_stripe_payments_loaded
  ON raw.stripe_payments (_loaded_at);

CREATE INDEX idx_raw_stripe_payments_source_id
  ON raw.stripe_payments (_source_id);
```

**Raw layer rules:**
- Append-only or soft-delete (never hard-delete)
- Add `_loaded_at`, `_source_id`, `_raw_payload`, `_batch_id` metadata to every table
- Use `JSONB` when source schema varies or is unknown
- No foreign keys in raw -- referential integrity is enforced in staging
- Partitioning by `_loaded_at` for tables exceeding 10M rows

### Staging Layer

Staging cleans, types, deduplicates, and validates raw data. This is where "data as it should be" takes shape.

```sql
CREATE SCHEMA IF NOT EXISTS stg;

-- Staging view: clean and deduplicate stripe payments
CREATE OR REPLACE VIEW stg.stripe_payments AS
WITH ranked AS (
  SELECT
    _source_id AS payment_id,
    (_raw_payload->>'amount')::NUMERIC / 100.0 AS amount,
    (_raw_payload->>'currency')::TEXT AS currency,
    (_raw_payload->>'status')::TEXT AS status,
    (_raw_payload->>'customer')::TEXT AS customer_id,
    TO_TIMESTAMP((_raw_payload->>'created')::BIGINT) AS created_at,
    (_raw_payload->>'description')::TEXT AS description,
    _loaded_at,
    ROW_NUMBER() OVER (
      PARTITION BY _source_id
      ORDER BY _loaded_at DESC
    ) AS rn
  FROM raw.stripe_payments
  WHERE _valid_to = 'infinity'
)
SELECT
  payment_id,
  amount,
  UPPER(currency) AS currency,
  LOWER(status) AS status,
  customer_id,
  created_at,
  NULLIF(TRIM(description), '') AS description,
  _loaded_at
FROM ranked
WHERE rn = 1;
```

**Staging layer rules:**
- Deduplicate using `ROW_NUMBER()` partitioned by source ID, ordered by load time descending
- Cast types explicitly (never rely on implicit casts)
- Normalise casing, trim whitespace, replace sentinel values with NULL
- VIEWs for small datasets; MATERIALIZED VIEWs for large datasets or complex joins
- Add data quality checks as constraints or assertions

### Mart Layer

Marts apply business logic and produce analysis-ready datasets organised by business domain.

```sql
CREATE SCHEMA IF NOT EXISTS mart;

-- Mart table: finance domain revenue analysis
CREATE MATERIALIZED VIEW mart.finance_revenue AS
SELECT
  sp.payment_id,
  sp.amount,
  sp.currency,
  sp.created_at,
  sp.customer_id,
  sc.customer_name,
  sc.customer_email,
  sc.customer_segment,
  DATE_TRUNC('month', sp.created_at) AS revenue_month,
  DATE_TRUNC('week', sp.created_at) AS revenue_week,
  CASE
    WHEN sp.amount >= 10000 THEN 'enterprise'
    WHEN sp.amount >= 1000 THEN 'mid-market'
    ELSE 'smb'
  END AS deal_tier
FROM stg.stripe_payments sp
LEFT JOIN stg.stripe_customers sc ON sp.customer_id = sc.customer_id
WHERE sp.status = 'succeeded'
WITH DATA;

CREATE UNIQUE INDEX idx_mart_revenue_payment
  ON mart.finance_revenue (payment_id);

-- Refresh on schedule
REFRESH MATERIALIZED VIEW CONCURRENTLY mart.finance_revenue;
```

**Mart layer rules:**
- Organised by business domain (finance, marketing, operations), not by source system
- Apply business logic: categorisation, scoring, status mapping
- Denormalise for query performance -- joins are done here, not in reporting
- Use MATERIALIZED VIEWs with `CONCURRENTLY` refresh to avoid locking read queries
- Document every business rule in SQL comments

### Reporting Layer

Reporting provides pre-aggregated views optimised for dashboards and API consumption.

```sql
CREATE SCHEMA IF NOT EXISTS rpt;

-- Reporting view: daily revenue summary
CREATE MATERIALIZED VIEW rpt.daily_revenue_summary AS
SELECT
  DATE(created_at) AS revenue_date,
  currency,
  customer_segment,
  deal_tier,
  COUNT(*) AS transaction_count,
  SUM(amount) AS total_revenue,
  AVG(amount) AS avg_transaction,
  MIN(amount) AS min_transaction,
  MAX(amount) AS max_transaction,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY amount) AS median_transaction
FROM mart.finance_revenue
GROUP BY
  DATE(created_at),
  currency,
  customer_segment,
  deal_tier
WITH DATA;

CREATE INDEX idx_rpt_daily_revenue_date
  ON rpt.daily_revenue_summary (revenue_date);
```

**Reporting layer rules:**
- Pre-aggregate to the grain dashboards need (daily, weekly, monthly)
- Include all dimensions dashboards filter on
- Refresh after mart layer completes
- Keep query complexity minimal -- dashboards should SELECT from these directly

---

## Orchestration Pattern Reference

### Cron-Based Orchestration

Simple time-based scheduling. Each pipeline step runs at a fixed time.

```sql
-- Supabase pg_cron setup
SELECT cron.schedule(
  'extract-stripe-payments',
  '0 6 * * *',  -- Daily at 6:00 AM
  $$SELECT pipeline.extract_stripe_payments()$$
);

SELECT cron.schedule(
  'refresh-staging',
  '30 6 * * *',  -- Daily at 6:30 AM
  $$REFRESH MATERIALIZED VIEW CONCURRENTLY stg.stripe_payments$$
);

SELECT cron.schedule(
  'refresh-mart',
  '0 7 * * *',  -- Daily at 7:00 AM
  $$REFRESH MATERIALIZED VIEW CONCURRENTLY mart.finance_revenue$$
);

SELECT cron.schedule(
  'refresh-reporting',
  '30 7 * * *',  -- Daily at 7:30 AM
  $$REFRESH MATERIALIZED VIEW CONCURRENTLY rpt.daily_revenue_summary$$
);
```

| Aspect | Assessment |
|---|---|
| **Pros** | Simple to set up; no external tooling; works with pg_cron natively; easy to audit schedule |
| **Cons** | No dependency awareness -- if extract runs late, staging runs on stale data; no automatic retry; time gaps wasted if steps finish early |
| **Best for** | Single-source pipelines with predictable runtimes; teams that want minimal infrastructure |
| **Avoid when** | Multiple sources with variable extraction times; steps with hard dependencies |

### Event-Driven Orchestration

Pipeline steps trigger based on events (webhook received, file uploaded, previous step completed).

```sql
-- Trigger-based: refresh staging after raw data load
CREATE OR REPLACE FUNCTION pipeline.on_raw_load_complete()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.status = 'success' AND NEW.pipeline_name LIKE 'extract_%' THEN
    PERFORM pipeline.refresh_staging(NEW.pipeline_name);
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_raw_load_complete
  AFTER INSERT ON pipeline.execution_log
  FOR EACH ROW
  EXECUTE FUNCTION pipeline.on_raw_load_complete();
```

| Aspect | Assessment |
|---|---|
| **Pros** | No wasted time between steps; reacts to actual completion; handles variable runtimes; natural for webhook sources |
| **Cons** | Harder to debug (no linear schedule to inspect); cascading failures can be complex; needs careful error handling at each trigger point |
| **Best for** | Webhook/real-time sources; pipelines where step runtimes vary; multi-source pipelines where sources arrive at different times |
| **Avoid when** | Team needs simple auditability; all sources are batch with predictable timing |

### Dependency-Based Orchestration

A coordinator checks dependencies before running each step. Combines scheduling with dependency awareness.

```sql
-- Dependency-based orchestration function
CREATE OR REPLACE FUNCTION pipeline.run_with_dependencies(
  p_pipeline_name TEXT,
  p_dependencies TEXT[]
) RETURNS VOID AS $$
DECLARE
  v_dep TEXT;
  v_last_success TIMESTAMPTZ;
  v_last_run TIMESTAMPTZ;
BEGIN
  -- Check each dependency completed successfully today
  FOREACH v_dep IN ARRAY p_dependencies
  LOOP
    SELECT MAX(completed_at) INTO v_last_success
    FROM pipeline.execution_log
    WHERE pipeline_name = v_dep
      AND status = 'success'
      AND started_at >= CURRENT_DATE;

    IF v_last_success IS NULL THEN
      RAISE NOTICE 'Dependency % not met for %. Skipping.', v_dep, p_pipeline_name;
      INSERT INTO pipeline.execution_log (pipeline_name, status, error_message)
      VALUES (p_pipeline_name, 'skipped', FORMAT('Dependency %s not met', v_dep));
      RETURN;
    END IF;
  END LOOP;

  -- Check this pipeline has not already succeeded today (idempotency)
  SELECT MAX(completed_at) INTO v_last_run
  FROM pipeline.execution_log
  WHERE pipeline_name = p_pipeline_name
    AND status = 'success'
    AND started_at >= CURRENT_DATE;

  IF v_last_run IS NOT NULL THEN
    RAISE NOTICE '% already completed today. Skipping.', p_pipeline_name;
    RETURN;
  END IF;

  -- Execute the pipeline
  PERFORM pipeline.execute(p_pipeline_name);
END;
$$ LANGUAGE plpgsql;

-- Schedule the coordinator to run frequently; it handles dependency checks
SELECT cron.schedule(
  'orchestrator',
  '*/5 6-8 * * *',  -- Every 5 minutes between 6-8 AM
  $$
    SELECT pipeline.run_with_dependencies('refresh_staging', ARRAY['extract_stripe', 'extract_xero']);
    SELECT pipeline.run_with_dependencies('refresh_mart', ARRAY['refresh_staging']);
    SELECT pipeline.run_with_dependencies('refresh_reporting', ARRAY['refresh_mart']);
  $$
);
```

| Aspect | Assessment |
|---|---|
| **Pros** | Respects dependencies; handles variable timing; idempotent by design; still uses simple scheduling underneath |
| **Cons** | More code to maintain; polling interval adds latency (up to the cron interval); dependency graph must be manually defined |
| **Best for** | Multi-source pipelines with sequential dependencies; teams that want dependency awareness without a full orchestration tool |
| **Avoid when** | Very complex DAGs (use Airflow/Dagster instead); real-time requirements |

---

## Error Handling Patterns

### Dead Letter Queues

Store failed records for manual investigation without blocking the pipeline.

```sql
CREATE TABLE pipeline.dead_letter (
  id SERIAL PRIMARY KEY,
  pipeline_name TEXT NOT NULL,
  step_name TEXT NOT NULL,
  source_record JSONB NOT NULL,
  error_message TEXT NOT NULL,
  error_code TEXT,
  retry_count INT NOT NULL DEFAULT 0,
  max_retries INT NOT NULL DEFAULT 3,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  next_retry_at TIMESTAMPTZ,
  resolved_at TIMESTAMPTZ,
  resolved_by TEXT,
  resolution_notes TEXT
);

CREATE INDEX idx_dead_letter_unresolved
  ON pipeline.dead_letter (pipeline_name, created_at)
  WHERE resolved_at IS NULL;

-- Insert failed record into dead letter queue
CREATE OR REPLACE FUNCTION pipeline.send_to_dead_letter(
  p_pipeline TEXT,
  p_step TEXT,
  p_record JSONB,
  p_error TEXT,
  p_error_code TEXT DEFAULT NULL
) RETURNS VOID AS $$
BEGIN
  INSERT INTO pipeline.dead_letter (
    pipeline_name, step_name, source_record,
    error_message, error_code,
    next_retry_at
  ) VALUES (
    p_pipeline, p_step, p_record,
    p_error, p_error_code,
    NOW() + INTERVAL '1 hour'
  );
END;
$$ LANGUAGE plpgsql;
```

### Retry Strategies — Exponential Backoff

```python
import time
import random
from functools import wraps

def retry_with_backoff(max_retries=3, base_delay=1.0, max_delay=300.0, jitter=True):
    """Decorator for retrying functions with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt == max_retries:
                        raise
                    delay = min(base_delay * (2 ** attempt), max_delay)
                    if jitter:
                        delay = delay * (0.5 + random.random())
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay:.1f}s")
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

# Usage
@retry_with_backoff(max_retries=3, base_delay=2.0)
def extract_from_api(endpoint, params):
    response = requests.get(endpoint, params=params, timeout=30)
    response.raise_for_status()
    return response.json()
```

### Database-Level Retry with Dead Letter Fallback

```sql
CREATE OR REPLACE FUNCTION pipeline.process_with_retry(
  p_pipeline TEXT,
  p_record JSONB,
  p_max_retries INT DEFAULT 3
) RETURNS BOOLEAN AS $$
DECLARE
  v_attempt INT := 0;
  v_success BOOLEAN := FALSE;
  v_delay INTERVAL;
BEGIN
  LOOP
    v_attempt := v_attempt + 1;
    BEGIN
      -- Attempt processing (replace with actual logic)
      PERFORM pipeline.process_record(p_pipeline, p_record);
      v_success := TRUE;
      EXIT;
    EXCEPTION WHEN OTHERS THEN
      IF v_attempt >= p_max_retries THEN
        -- Send to dead letter queue after exhausting retries
        PERFORM pipeline.send_to_dead_letter(
          p_pipeline, 'process', p_record, SQLERRM, SQLSTATE
        );
        EXIT;
      END IF;
      -- Exponential backoff: 1s, 2s, 4s
      v_delay := (POWER(2, v_attempt - 1) || ' seconds')::INTERVAL;
      PERFORM pg_sleep(EXTRACT(EPOCH FROM v_delay));
    END;
  END LOOP;
  RETURN v_success;
END;
$$ LANGUAGE plpgsql;
```

### Circuit Breakers

Prevent cascading failures by stopping extraction when a source is consistently failing.

```sql
CREATE TABLE pipeline.circuit_breaker (
  source_name TEXT PRIMARY KEY,
  state TEXT NOT NULL DEFAULT 'closed',  -- closed (normal), open (blocked), half-open (testing)
  failure_count INT NOT NULL DEFAULT 0,
  failure_threshold INT NOT NULL DEFAULT 5,
  last_failure_at TIMESTAMPTZ,
  opened_at TIMESTAMPTZ,
  cooldown_until TIMESTAMPTZ,
  last_success_at TIMESTAMPTZ
);

CREATE OR REPLACE FUNCTION pipeline.check_circuit(p_source TEXT)
RETURNS BOOLEAN AS $$
DECLARE
  v_state TEXT;
  v_cooldown TIMESTAMPTZ;
BEGIN
  SELECT state, cooldown_until INTO v_state, v_cooldown
  FROM pipeline.circuit_breaker
  WHERE source_name = p_source;

  IF NOT FOUND THEN
    INSERT INTO pipeline.circuit_breaker (source_name)
    VALUES (p_source);
    RETURN TRUE;  -- No record = circuit closed = proceed
  END IF;

  IF v_state = 'closed' THEN
    RETURN TRUE;
  END IF;

  IF v_state = 'open' AND NOW() >= v_cooldown THEN
    -- Transition to half-open: allow one test request
    UPDATE pipeline.circuit_breaker
    SET state = 'half-open'
    WHERE source_name = p_source;
    RETURN TRUE;
  END IF;

  RETURN FALSE;  -- Circuit open, do not proceed
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION pipeline.record_failure(p_source TEXT)
RETURNS VOID AS $$
DECLARE
  v_count INT;
  v_threshold INT;
BEGIN
  UPDATE pipeline.circuit_breaker
  SET failure_count = failure_count + 1,
      last_failure_at = NOW()
  WHERE source_name = p_source
  RETURNING failure_count, failure_threshold INTO v_count, v_threshold;

  IF v_count >= v_threshold THEN
    UPDATE pipeline.circuit_breaker
    SET state = 'open',
        opened_at = NOW(),
        cooldown_until = NOW() + INTERVAL '15 minutes'
    WHERE source_name = p_source;
  END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION pipeline.record_success(p_source TEXT)
RETURNS VOID AS $$
BEGIN
  UPDATE pipeline.circuit_breaker
  SET state = 'closed',
      failure_count = 0,
      last_success_at = NOW()
  WHERE source_name = p_source;
END;
$$ LANGUAGE plpgsql;
```

---

## Monitoring SQL Templates

### Pipeline Health Check

```sql
-- Dashboard: pipeline health overview (last 7 days)
SELECT
  pipeline_name,
  COUNT(*) FILTER (WHERE status = 'success') AS successes,
  COUNT(*) FILTER (WHERE status = 'failed') AS failures,
  COUNT(*) FILTER (WHERE status = 'partial') AS partial,
  ROUND(
    COUNT(*) FILTER (WHERE status = 'success')::NUMERIC /
    NULLIF(COUNT(*), 0) * 100, 1
  ) AS success_rate_pct,
  ROUND(AVG(execution_duration_seconds)::NUMERIC, 1) AS avg_duration_s,
  MAX(execution_duration_seconds) AS max_duration_s
FROM pipeline.execution_log
WHERE started_at > NOW() - INTERVAL '7 days'
GROUP BY pipeline_name
ORDER BY success_rate_pct ASC;
```

### Data Freshness Check

```sql
-- Alert: data freshness violations
-- Configure expected_freshness per table in a control table
CREATE TABLE pipeline.freshness_sla (
  table_schema TEXT NOT NULL,
  table_name TEXT NOT NULL,
  timestamp_column TEXT NOT NULL DEFAULT '_loaded_at',
  max_staleness INTERVAL NOT NULL,
  PRIMARY KEY (table_schema, table_name)
);

-- Seed SLA expectations
INSERT INTO pipeline.freshness_sla VALUES
  ('raw', 'stripe_payments', '_loaded_at', INTERVAL '2 hours'),
  ('raw', 'xero_invoices', '_loaded_at', INTERVAL '25 hours'),
  ('raw', 'ga4_sessions', '_loaded_at', INTERVAL '25 hours');

-- Check freshness (run via pg_cron every 30 minutes)
-- NOTE: Requires dynamic SQL; wrap in a function for production use
SELECT
  sla.table_schema,
  sla.table_name,
  sla.max_staleness,
  NOW() - MAX(r._loaded_at) AS actual_staleness,
  CASE
    WHEN NOW() - MAX(r._loaded_at) > sla.max_staleness THEN 'STALE'
    ELSE 'FRESH'
  END AS status
FROM pipeline.freshness_sla sla
LEFT JOIN raw.stripe_payments r ON sla.table_name = 'stripe_payments'
GROUP BY sla.table_schema, sla.table_name, sla.max_staleness
HAVING NOW() - MAX(r._loaded_at) > sla.max_staleness;
```

### Row Count Validation

```sql
-- Track row counts over time to detect anomalies
CREATE TABLE pipeline.row_count_log (
  id SERIAL PRIMARY KEY,
  table_schema TEXT NOT NULL,
  table_name TEXT NOT NULL,
  row_count BIGINT NOT NULL,
  measured_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Log current counts (run daily)
INSERT INTO pipeline.row_count_log (table_schema, table_name, row_count)
SELECT schemaname, tablename, n_live_tup
FROM pg_stat_user_tables
WHERE schemaname IN ('raw', 'stg', 'mart', 'rpt');

-- Alert on abnormal row count changes
WITH daily_counts AS (
  SELECT
    table_schema,
    table_name,
    row_count,
    measured_at::DATE AS measure_date,
    LAG(row_count) OVER (
      PARTITION BY table_schema, table_name
      ORDER BY measured_at
    ) AS prev_count
  FROM pipeline.row_count_log
)
SELECT
  table_schema,
  table_name,
  prev_count,
  row_count AS current_count,
  row_count - prev_count AS change,
  ROUND(
    (row_count - prev_count)::NUMERIC /
    NULLIF(prev_count, 0) * 100, 1
  ) AS change_pct
FROM daily_counts
WHERE prev_count IS NOT NULL
  AND ABS(row_count - prev_count) >
      GREATEST(prev_count * 0.5, 100)  -- >50% change or >100 rows
ORDER BY ABS(row_count - prev_count) DESC;
```

### Dead Letter Queue Monitor

```sql
-- Unresolved dead letter items by pipeline
SELECT
  pipeline_name,
  step_name,
  COUNT(*) AS unresolved_count,
  MIN(created_at) AS oldest_unresolved,
  MAX(created_at) AS newest_unresolved,
  MAX(retry_count) AS max_retries_hit
FROM pipeline.dead_letter
WHERE resolved_at IS NULL
GROUP BY pipeline_name, step_name
ORDER BY unresolved_count DESC;
```

---

## Source System Integration Patterns

### API Polling

Periodically call a REST API to fetch new or updated records.

```python
import requests
from datetime import datetime, timezone

def extract_api_incremental(
    endpoint: str,
    api_key: str,
    last_sync_at: datetime,
    page_size: int = 100
) -> list[dict]:
    """Generic incremental API extractor with pagination."""
    all_records = []
    page = 1
    has_more = True

    while has_more:
        response = requests.get(
            endpoint,
            headers={"Authorization": f"Bearer {api_key}"},
            params={
                "updated_after": last_sync_at.isoformat(),
                "page": page,
                "per_page": page_size,
                "sort": "updated_at",
                "order": "asc"
            },
            timeout=30
        )
        response.raise_for_status()
        data = response.json()

        records = data.get("data", [])
        all_records.extend(records)

        has_more = len(records) == page_size
        page += 1

    return all_records
```

**When to use:** Source exposes a REST API with filtering by updated_at or cursor-based pagination. Most SaaS tools (Stripe, Xero, HubSpot).

**Watch out for:** Rate limits (implement backoff), API pagination limits, clock skew between systems, records updated during extraction window.

### Webhook Ingestion

Source pushes data to your endpoint when events occur.

```sql
-- Webhook buffer table (raw ingestion point)
CREATE TABLE raw.webhook_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  source TEXT NOT NULL,
  event_type TEXT NOT NULL,
  payload JSONB NOT NULL,
  headers JSONB,
  received_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  processed_at TIMESTAMPTZ,
  processing_status TEXT NOT NULL DEFAULT 'pending'
);

CREATE INDEX idx_webhook_pending
  ON raw.webhook_events (source, received_at)
  WHERE processing_status = 'pending';
```

```typescript
// Supabase Edge Function: webhook receiver
import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

serve(async (req) => {
  const supabase = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!
  );

  const payload = await req.json();
  const source = new URL(req.url).searchParams.get("source") ?? "unknown";
  const eventType = payload.type ?? payload.event ?? "unknown";

  const { error } = await supabase.from("raw.webhook_events").insert({
    source,
    event_type: eventType,
    payload,
    headers: Object.fromEntries(req.headers.entries()),
  });

  if (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
    });
  }

  return new Response(JSON.stringify({ received: true }), { status: 200 });
});
```

**When to use:** Source supports webhooks (Stripe, Shopify, GitHub). Need near-real-time data.

**Watch out for:** Duplicate deliveries (always use idempotency keys), webhook signature verification, burst handling (buffer in table, process asynchronously), missed webhooks (supplement with periodic API polling as backfill).

### File Drop

Process files uploaded to a storage bucket or directory.

```python
import pandas as pd
from pathlib import Path
from datetime import datetime

def process_file_drop(
    file_path: str,
    archive_dir: str,
    error_dir: str
) -> dict:
    """Process a dropped CSV file with error handling and archival."""
    path = Path(file_path)
    result = {"file": path.name, "status": "pending", "rows": 0}

    try:
        # Detect encoding and delimiter
        df = pd.read_csv(path, nrows=5)
        result["columns"] = list(df.columns)

        # Full read with type coercion
        df = pd.read_csv(path, dtype=str)  # Read as string first, cast later
        result["rows"] = len(df)

        # Load to database
        # ... (insert logic here)

        result["status"] = "success"

        # Archive the processed file
        archive_path = Path(archive_dir) / f"{datetime.now():%Y%m%d_%H%M%S}_{path.name}"
        path.rename(archive_path)

    except Exception as e:
        result["status"] = "failed"
        result["error"] = str(e)
        error_path = Path(error_dir) / f"{datetime.now():%Y%m%d_%H%M%S}_{path.name}"
        path.rename(error_path)

    return result
```

**When to use:** Data arrives as CSV/Excel/JSON files (manual exports, SFTP drops, email attachments processed by automation).

**Watch out for:** Encoding issues (always detect, never assume UTF-8), inconsistent column names between drops, partial files (check file size / row counts), processing the same file twice (track processed filenames).

### Change Data Capture (CDC)

Track row-level changes in a source database and replicate them.

```sql
-- Source-side: audit trigger for CDC
CREATE OR REPLACE FUNCTION audit.capture_changes()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO audit.change_log (
    table_name,
    operation,
    old_data,
    new_data,
    changed_at,
    changed_by
  ) VALUES (
    TG_TABLE_NAME,
    TG_OP,
    CASE WHEN TG_OP IN ('UPDATE', 'DELETE') THEN to_jsonb(OLD) ELSE NULL END,
    CASE WHEN TG_OP IN ('INSERT', 'UPDATE') THEN to_jsonb(NEW) ELSE NULL END,
    NOW(),
    current_user
  );
  RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;

-- Apply to tables you want to track
CREATE TRIGGER trg_customers_cdc
  AFTER INSERT OR UPDATE OR DELETE ON public.customers
  FOR EACH ROW EXECUTE FUNCTION audit.capture_changes();
```

**When to use:** Source is a database you control or can add triggers to. Need to track every change (not just current state). Audit trail requirements.

**Watch out for:** Trigger overhead on high-write tables, change log table growth (partition and archive), handling schema changes in the source table, ordering guarantees for replaying changes.

---

## Idempotency Patterns by Pipeline Stage

### Extract Stage

```python
def idempotent_extract(source: str, extraction_date: str, db_conn):
    """Extract is idempotent: re-running for the same date replaces previous extract."""
    # Delete any previous extract for this source + date
    db_conn.execute("""
        DELETE FROM raw.{source}
        WHERE _batch_id = %s
    """.format(source=source), [f"{source}_{extraction_date}"])

    # Run extraction
    records = extract_from_source(source, extraction_date)

    # Load with batch ID
    for record in records:
        db_conn.execute("""
            INSERT INTO raw.{source} (_source_id, _raw_payload, _batch_id)
            VALUES (%s, %s, %s)
        """.format(source=source), [
            record["id"],
            json.dumps(record),
            f"{source}_{extraction_date}"
        ])
```

### Load Stage

```sql
-- Upsert pattern: idempotent load by natural key
INSERT INTO raw.stripe_payments (_source_id, _raw_payload, _loaded_at)
VALUES ($1, $2, NOW())
ON CONFLICT (_source_id)
DO UPDATE SET
  _raw_payload = EXCLUDED._raw_payload,
  _loaded_at = EXCLUDED._loaded_at;

-- Delete-reload pattern: idempotent load by partition
BEGIN;
  DELETE FROM raw.ga4_sessions
  WHERE _loaded_at::DATE = CURRENT_DATE;

  INSERT INTO raw.ga4_sessions (_source_id, _raw_payload, _loaded_at)
  SELECT * FROM tmp_ga4_sessions;
COMMIT;
```

### Transform Stage

```sql
-- Materialized view refresh is inherently idempotent
REFRESH MATERIALIZED VIEW CONCURRENTLY stg.stripe_payments;
REFRESH MATERIALIZED VIEW CONCURRENTLY mart.finance_revenue;

-- Table-based transform: idempotent via truncate-reload
BEGIN;
  TRUNCATE mart.finance_revenue;
  INSERT INTO mart.finance_revenue
  SELECT /* ... transform query ... */;
COMMIT;

-- Incremental transform: idempotent via merge
MERGE INTO mart.customer_summary AS target
USING (
  SELECT customer_id, COUNT(*) AS order_count, SUM(amount) AS total_spent
  FROM stg.stripe_payments
  WHERE created_at >= CURRENT_DATE - INTERVAL '1 day'
  GROUP BY customer_id
) AS source
ON target.customer_id = source.customer_id
WHEN MATCHED THEN
  UPDATE SET
    order_count = source.order_count,
    total_spent = source.total_spent,
    updated_at = NOW()
WHEN NOT MATCHED THEN
  INSERT (customer_id, order_count, total_spent, updated_at)
  VALUES (source.customer_id, source.order_count, source.total_spent, NOW());
```

### Serve / Reporting Stage

```sql
-- Reporting refresh is idempotent by nature (materialized views)
-- For table-based reporting, use the same delete-reload pattern:
BEGIN;
  DELETE FROM rpt.daily_revenue_summary
  WHERE revenue_date = CURRENT_DATE - 1;

  INSERT INTO rpt.daily_revenue_summary
  SELECT /* ... aggregation for yesterday ... */;
COMMIT;
```

**Key principle:** Every stage should produce identical results when run multiple times with the same inputs. Use transactions to make multi-step operations atomic. Use batch IDs or date partitions to scope delete-reload operations.
