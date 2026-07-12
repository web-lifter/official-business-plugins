---
title: Funnel instrumentation spec
slug: funnel-instrumentation
type: analytics-plan
status: active
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# Funnel instrumentation spec

**Source funnel:** [funnel-model](../../06-relationships-channels/funnel-model.md)
**Source metrics:** [mvp-metrics](../mvp-metrics.md)
**Tool:** {{PostHog | GA4 | Plausible | Mixpanel}}

## Events per stage

| Stage | Event | When fires | Where (client/server) | Properties |
|-------|-------|-----------|----------------------|-----------|
| Awareness | `page_viewed` | route mount | client | `{ route, referrer, utm_* }` |
| Sign-up | `user_signed_up` | post-profile-insert | server | `{ source, plan }` |
| Activation | `{{value_revealing_event}}` | {{when}} | {{where}} | {{props}} |
| Conversion | `{{conversion_event}}` | {{when}} | {{where}} | {{props}} |
| Retention W{{N}} | `session_started` | session resume | client | `{ cohort }` |

## Threshold queries

### {{metric name}} (target {{≥ X%}})
- Funnel: `{{event_a}} → {{event_b}}`
- Window: {{N days}}
- Cohort filter: {{filter}}

## Dashboards

- {{One per primary metric — source-controlled config under `dashboards/`}}
