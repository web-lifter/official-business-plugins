# Data Pipeline Architecture: Marketing Data Stack

**Client:** BrightPath Education (Australian online learning platform)
**Sources:** Google Ads API, Meta Ads API
**Destination:** Supabase (PostgreSQL)
**Orchestration:** Supabase Edge Functions + pg_cron
**Reporting:** Metabase connected to Supabase read replica

---

## Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐
│   Google Ads    │    │    Meta Ads     │
│      API        │    │   Marketing     │
└────────┬────────┘    └────────┬────────┘
         │  REST/JSON           │  REST/JSON
         ▼                      ▼
┌─────────────────────────────────────────┐
│       Supabase Edge Functions           │
│  ┌──────────────┐  ┌─────────────────┐  │
│  │ google-ads-  │  │ meta-ads-       │  │
│  │ ingestion    │  │ ingestion       │  │
│  └──────┬───────┘  └───────┬─────────┘  │
│         │                  │            │
│         ▼                  ▼            │
│  ┌──────────────────────────────────┐   │
│  │     raw_google_ads / raw_meta    │   │  Supabase
│  │         (staging tables)         │   │  PostgreSQL
│  └──────────────┬───────────────────┘   │
│                 │                       │
│         ┌───────▼───────────┐           │
│         │  pg_cron job      │           │
│         │  transform_ads()  │           │
│         └───────┬───────────┘           │
│                 │                       │
│  ┌──────────────▼───────────────────┐   │
│  │   unified_ad_performance         │   │
│  │   (clean, deduplicated, AUD)     │   │
│  └──────────────┬───────────────────┘   │
│                 │                       │
└─────────────────┼───────────────────────┘
                  │
                  ▼
         ┌────────────────┐
         │    Metabase    │
         │   Dashboards   │
         └────────────────┘
```

---

## Data Flow

### Phase 1: Ingestion (Edge Functions, daily at 05:00 AEST)

**Google Ads ingestion** (`google-ads-ingestion`):
- Calls Google Ads API v17 `/customers/{id}/googleAds:searchStream`
- Pulls campaign, ad group, and keyword performance for the previous day
- Writes raw JSON rows into `raw_google_ads`

```sql
CREATE TABLE public.raw_google_ads (
  id              BIGSERIAL PRIMARY KEY,
  ingested_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  report_date     DATE NOT NULL,
  campaign_id     TEXT NOT NULL,
  campaign_name   TEXT,
  ad_group_id     TEXT,
  ad_group_name   TEXT,
  impressions     INTEGER,
  clicks          INTEGER,
  cost_micros     BIGINT,
  conversions     NUMERIC(10,2),
  conversion_value_micros BIGINT,
  raw_payload     JSONB NOT NULL
);
```

**Meta Ads ingestion** (`meta-ads-ingestion`):
- Calls Meta Marketing API v21.0 `/act_{ad_account_id}/insights`
- Pulls campaign-level spend, impressions, clicks, and purchase conversions
- Writes raw rows into `raw_meta_ads`

```sql
CREATE TABLE public.raw_meta_ads (
  id              BIGSERIAL PRIMARY KEY,
  ingested_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  report_date     DATE NOT NULL,
  campaign_id     TEXT NOT NULL,
  campaign_name   TEXT,
  adset_id        TEXT,
  adset_name      TEXT,
  impressions     INTEGER,
  clicks          INTEGER,
  spend           NUMERIC(12,2),
  currency        TEXT DEFAULT 'AUD',
  purchases       INTEGER,
  purchase_value  NUMERIC(12,2),
  raw_payload     JSONB NOT NULL
);
```

### Phase 2: Transformation (pg_cron, daily at 05:30 AEST)

A PostgreSQL function merges both sources into a unified view with consistent column names, AUD currency, and deduplication.

```sql
CREATE OR REPLACE FUNCTION transform_ads() RETURNS void AS $$
BEGIN
  -- Clear today's transformed rows (idempotent re-runs)
  DELETE FROM public.unified_ad_performance
  WHERE report_date = CURRENT_DATE - INTERVAL '1 day';

  -- Google Ads
  INSERT INTO public.unified_ad_performance
    (report_date, source, campaign_id, campaign_name, impressions, clicks, spend_aud, conversions, revenue_aud)
  SELECT
    report_date,
    'google_ads',
    campaign_id,
    campaign_name,
    SUM(impressions),
    SUM(clicks),
    SUM(cost_micros) / 1000000.0,
    SUM(conversions),
    SUM(conversion_value_micros) / 1000000.0
  FROM public.raw_google_ads
  WHERE report_date = CURRENT_DATE - INTERVAL '1 day'
  GROUP BY report_date, campaign_id, campaign_name;

  -- Meta Ads
  INSERT INTO public.unified_ad_performance
    (report_date, source, campaign_id, campaign_name, impressions, clicks, spend_aud, conversions, revenue_aud)
  SELECT
    report_date,
    'meta_ads',
    campaign_id,
    campaign_name,
    SUM(impressions),
    SUM(clicks),
    SUM(spend),
    SUM(purchases),
    SUM(purchase_value)
  FROM public.raw_meta_ads
  WHERE report_date = CURRENT_DATE - INTERVAL '1 day'
  GROUP BY report_date, campaign_id, campaign_name;
END;
$$ LANGUAGE plpgsql;
```

**Unified output table:**

```sql
CREATE TABLE public.unified_ad_performance (
  id            BIGSERIAL PRIMARY KEY,
  report_date   DATE NOT NULL,
  source        TEXT NOT NULL CHECK (source IN ('google_ads', 'meta_ads')),
  campaign_id   TEXT NOT NULL,
  campaign_name TEXT,
  impressions   INTEGER NOT NULL DEFAULT 0,
  clicks        INTEGER NOT NULL DEFAULT 0,
  spend_aud     NUMERIC(12,2) NOT NULL DEFAULT 0,
  conversions   NUMERIC(10,2) NOT NULL DEFAULT 0,
  revenue_aud   NUMERIC(12,2) NOT NULL DEFAULT 0,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (report_date, source, campaign_id)
);

CREATE INDEX idx_unified_perf_date ON public.unified_ad_performance(report_date);
```

### Phase 3: Serving (Metabase)

Metabase connects to the Supabase read replica and queries `unified_ad_performance` for:
- Daily spend vs. revenue by channel
- ROAS (Return on Ad Spend) trending
- Campaign-level CPA (Cost per Acquisition) breakdown
- Week-over-week comparison dashboards

---

## Scheduling

```sql
-- pg_cron schedule (configured via Supabase dashboard)
SELECT cron.schedule('ingest-google-ads', '0 19 * * *', $$ SELECT net.http_post('https://xyzproject.supabase.co/functions/v1/google-ads-ingestion', '{}', '{"Authorization": "Bearer <service_role_key>"}') $$);
SELECT cron.schedule('ingest-meta-ads', '5 19 * * *', $$ SELECT net.http_post('https://xyzproject.supabase.co/functions/v1/meta-ads-ingestion', '{}', '{"Authorization": "Bearer <service_role_key>"}') $$);
SELECT cron.schedule('transform-ads', '30 19 * * *', $$ SELECT transform_ads() $$);
-- Note: 19:00 UTC = 05:00 AEST (next day)
```

---

## Error Handling Strategy

| Failure Mode | Detection | Response | Recovery |
|---|---|---|---|
| API rate limit (429) | HTTP status in Edge Function | Exponential backoff: 1s, 2s, 4s, max 3 retries | Auto-retry; alert after 3 failures |
| API auth expired | 401 response | Log error, send Slack alert to #data-ops | Manual token refresh in Supabase secrets |
| Partial data (API timeout) | Row count check: `raw_*` < 80% of prior day | Flag `pipeline_runs` row as `partial` | Re-trigger ingestion via manual Edge Function call |
| Transform failure | pg_cron job error in `cron.job_run_details` | Slack alert via pg_net webhook | Fix SQL, re-run `SELECT transform_ads()` |
| Duplicate ingestion | UNIQUE constraint on unified table | ON CONFLICT DO NOTHING (idempotent) | No action needed |

**Pipeline health check (runs at 06:00 AEST):**

```sql
SELECT
  source,
  MAX(report_date) AS latest_date,
  CASE
    WHEN MAX(report_date) < CURRENT_DATE - 1 THEN 'STALE'
    ELSE 'OK'
  END AS status
FROM public.unified_ad_performance
GROUP BY source;
```
