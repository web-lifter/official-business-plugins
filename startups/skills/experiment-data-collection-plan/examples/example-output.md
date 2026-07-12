# Data collection plan — TC-007

(Appended to the test card at `02-customer-discovery/test-cards/TC-007.md`.)

**Test card:** TC-007 — Median redline time on the prototype, 12-counsel cohort.
**Hypothesis:** H-002 — A senior in-house counsel can produce a redline in < 25 minutes (median) using the tool, vs. > 90 minutes manual.
**Owner:** Priya Natarajan
**Window:** 2026-05-26 → 2026-06-13 (15 working days).

## Source

Mixed:
- **Supabase SQL** for in-tool timing (`classifier_runs.started_at`, `findings.reviewed_at`).
- **PostHog** for `redline_export_clicked` event (marks the counsel's perceived end of the review).
- **Out-of-band survey** for the manual baseline self-report (one row per participant, captured at intake).

## Schema

### Supabase
- `contracts(id, uploaded_by, created_at, status)`
- `classifier_runs(contract_id, finished_at)` — proxy for "ready for review" start.
- `findings(contract_id, reviewed_at)` — last reviewed finding ≈ end of review.

### PostHog
- `redline_export_clicked` event with properties: `{ contract_id, distinct_id, duration_ms_in_app }`.

### Survey (Tally → Supabase via webhook → `interview_intakes` table)
- `manual_baseline_minutes` — self-reported median time for a comparable 40-page MSA.

## Pre-test checks

- [x] `redline_export_clicked` event firing — verified in PostHog live events 2026-05-22.
- [x] `findings.reviewed_at` populated — verified by Tom in the staging DB.
- [x] Sample size: 12 counsel × 1 contract each = 12 paired observations. Sufficient for a sign test at α=0.05.
- [x] Threshold computable: median over the 12 samples.

All checks green — experiment can run.

## Query

```sql
-- Median time-to-redline per participant, in-tool measurement
with review_windows as (
  select
    c.uploaded_by                                   as participant_id,
    c.id                                            as contract_id,
    cr.finished_at                                  as review_started_at,
    max(f.reviewed_at)                              as review_ended_at,
    extract(epoch from (max(f.reviewed_at) - cr.finished_at)) / 60.0 as duration_min
  from public.contracts c
  join public.classifier_runs cr on cr.contract_id = c.id and cr.status = 'succeeded'
  join public.findings f on f.contract_id = c.id and f.status in ('accepted','rejected')
  where c.created_at >= '2026-05-26' and c.created_at < '2026-06-14'
    and c.org_id = '<study-org-uuid>'
  group by c.uploaded_by, c.id, cr.finished_at
)
select
  percentile_cont(0.5) within group (order by duration_min) as median_minutes,
  count(*)                                                   as n,
  min(duration_min)                                          as fastest,
  max(duration_min)                                          as slowest
from review_windows;
```

PostHog confirmation query (sanity check on the export event):

```
funnel "Redline completion"
  step 1: contract_uploaded
  step 2: redline_export_clicked (within 4 hours)
filter: org_id = "<study-org-uuid>" and timestamp >= 2026-05-26
```

## Decision rule

At 2026-06-13 17:00 AEST:
- If `median_minutes < 25` and `n >= 10` → **confirm** H-002. Move to H-001 pricing experiment (TC-008).
- If `25 <= median_minutes < 45` → **refine.** Identify the slowest 3 sessions, instrument cause (likely PDF parsing latency on 50+ page contracts), iterate, rerun.
- If `median_minutes >= 45` or `n < 10` → **refute** H-002. Build learning card LC-007, decide pivot on UX (e.g. structured review wizard vs free-form).

Manual-baseline comparison (`manual_baseline_minutes` self-reported median) is a secondary readout, not the falsifier — small-sample self-report cannot carry the decision alone.

## Linked

- Test card: [TC-007](TC-007.md)
- Hypothesis: [H-002](../../01-hypotheses/hypothesis-register.md)
- Events spec: [events-spec](../../09-mvp/analytics/events-spec.md)
- Funnel instrumentation: [funnel-instrumentation](../../09-mvp/analytics/funnel-instrumentation.md)
