---
title: Funnel instrumentation spec
slug: funnel-instrumentation
type: analytics-plan
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Funnel instrumentation spec

**Source funnel:** [funnel-model](../../06-relationships-channels/funnel-model.md)
**Source metrics:** [mvp-metrics](../mvp-metrics.md)
**Tool:** PostHog Cloud (EU region)

## Events per stage

| Stage | Event | When fires | Where | Properties |
|-------|-------|-----------|-------|-----------|
| Awareness | `page_viewed` | route mount on marketing site | client | `{ route, referrer, utm_source, utm_campaign }` |
| Sign-up | `user_signed_up` | server, after `profiles` insert trigger fires | server | `{ source: 'google_oauth'|'email', invited_by_org_id? }` |
| Activation | `contract_uploaded` | server, after `contracts.status='queued'` | server | `{ contract_id, file_kind, page_count }` |
| Value-revealing | `findings_first_viewed` | client, on first mount of `/contracts/{id}` with `status='ready'` | client | `{ contract_id, finding_count, high_risk_count }` |
| Conversion | `redline_export_clicked` | client, on click of "Download redline" | client | `{ contract_id, accepted_count, rejected_count, duration_ms_in_app }` |
| Pricing intent | `pricing_viewed` | `/pricing` mount | client | `{ plan_focus }` |
| Pay | `checkout_completed` | server, Stripe webhook | server | `{ plan, mrr_aud }` |
| Retention W2 | `session_started` | first session in week 2 cohort | client | `{ cohort_week: 2 }` |

All server-side events identify the user via the Supabase session cookie; client-side events identify via PostHog's `distinct_id` aliased to `user.id` on sign-up.

## Threshold queries

### H-002 — activation rate (target ≥ 70% within 7 days of sign-up)
- Funnel: `user_signed_up → contract_uploaded`
- Window: 7 days
- Cohort filter: signup since 2026-05-26.

### H-002 — value-revealing rate (target ≥ 80% of activations within 1 day)
- Funnel: `contract_uploaded → findings_first_viewed`
- Window: 1 day
- Cohort filter: post-activation users.

### H-002 — completion rate (target ≥ 60% of value-revealing within 3 days)
- Funnel: `findings_first_viewed → redline_export_clicked`
- Window: 3 days

### H-001 — sign-up → paid (target ≥ 15% within 30 days)
- Funnel: `user_signed_up → checkout_completed`
- Window: 30 days
- Cohort filter: trial plan only.

### Week-2 retention (target ≥ 50%)
- Cohort: paid users; week 1 = first session post-`checkout_completed`.
- Metric: `session_started` count in week 2 cohort window, deduped by user.

## Dashboards

Source-controlled PostHog dashboard configs at `dashboards/`:

- `dashboards/h-002-redline-funnel.json` — the H-002 four-step funnel + median duration overlay.
- `dashboards/h-001-trial-to-paid.json` — pricing → conversion path.
- `dashboards/retention-cohorts.json` — week-1 / week-2 / week-4 retention curves.

Imported via the PostHog API in CI on every merge to `main`.

## Privacy and PII

- Email never sent — PostHog `$set` excluded; identity is the Supabase user UUID.
- Contract `title` never sent — `contract_id` only.
- IP anonymisation: on.
- Cookie consent: required (PostHog EU region; AU users land on EU pop for residency consistency); banner via `react-cookie-consent`, blocks event firing pre-consent.
