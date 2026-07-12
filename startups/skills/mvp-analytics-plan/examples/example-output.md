---
title: Events spec
slug: events-spec
type: analytics-plan
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Events spec

**Tool:** PostHog Cloud (EU region — `eu.posthog.com`)
**Source metrics:** [mvp-metrics](../mvp-metrics.md)

## Identity model

- Anonymous visitor: `distinct_id` assigned client-side at first marketing-site visit.
- Sign-up: server-side `alias(distinct_id → user.id)` immediately after the `profiles` row is inserted.
- Post-membership load: `posthog.group('org', org_id)` so org-level analytics work.
- Sign-out: `posthog.reset()` clears the identified state.

## Global super-properties

| Property | Type | When to set |
|----------|------|-----------|
| `app_version` | string | session start (from `process.env.NEXT_PUBLIC_GIT_SHA`) |
| `auth_state` | `'anon' | 'authed'` | every event |
| `org_id` | uuid | post-membership-load |
| `org_plan` | `'trial'|'starter'|'growth'` | post-membership-load |
| `route` | string | every page view |
| `feature_flags` | string[] | session start, refreshed every 10 min |

## Events

### `page_viewed`
- **Where:** client, all marketing routes + app routes.
- **Properties:** `{ route, referrer, utm_source?, utm_medium?, utm_campaign? }`
- **Maps to metric:** awareness funnel top.

### `user_signed_up`
- **Where:** server, in the post-sign-up route handler.
- **Properties:** `{ source: 'google_oauth'|'email', invited_by_org_id? }`
- **Maps to metric:** H-001 trial-to-paid funnel start.

### `org_created`
- **Where:** server, when first org row is inserted.
- **Properties:** `{ org_id, plan }`

### `contract_uploaded`
- **Where:** server, after `contracts.status='queued'`.
- **Properties:** `{ contract_id, file_kind, page_count }`
- **Maps to metric:** H-002 activation rate.

### `classifier_run_completed`
- **Where:** server (CF Worker → Vercel webhook).
- **Properties:** `{ contract_id, duration_ms, finding_count, high_risk_count, model }`
- **Maps to metric:** H-003 precision (manual labelling against this sample).

### `findings_first_viewed`
- **Where:** client, on first mount of `/contracts/{id}` with `status='ready'`.
- **Properties:** `{ contract_id, finding_count }`

### `finding_decided`
- **Where:** client, on accept/reject click.
- **Properties:** `{ contract_id, finding_id, category_id, decision: 'accepted'|'rejected', risk_level }`

### `redline_export_clicked`
- **Where:** client.
- **Properties:** `{ contract_id, accepted_count, rejected_count, duration_ms_in_app }`
- **Maps to metric:** H-002 completion rate; primary success event for the redline funnel.

### `pricing_viewed`
- **Where:** client.
- **Properties:** `{ plan_focus }`

### `checkout_completed`
- **Where:** server, Stripe webhook handler.
- **Properties:** `{ plan, mrr_aud }`
- **Maps to metric:** H-001 conversion.

### `session_started`
- **Where:** client, debounced once per 30 minutes idle.
- **Properties:** inherited globals only.

## Configuration

```ts
// app/_components/PosthogProvider.tsx
import posthog from 'posthog-js';

if (typeof window !== 'undefined' && process.env.NEXT_PUBLIC_POSTHOG_KEY) {
  posthog.init(process.env.NEXT_PUBLIC_POSTHOG_KEY, {
    api_host: 'https://eu.posthog.com',
    autocapture: false,
    capture_pageview: false,        // we fire page_viewed manually with route metadata
    capture_pageleave: true,
    person_profiles: 'identified_only',
    bootstrap: { distinctID: cookies().get('ph_did')?.value },
  });
}
```

Server-side events use `@posthog/node` with the same project key + EU host, identifying by Supabase user UUID.

## Privacy

- **PII excluded.** Email, full name, contract title, clause text, document body — never sent. We send `contract_id` and `finding_id` only.
- **IP anonymisation:** on.
- **Cookie consent:** required for AU + EU users; banner via `react-cookie-consent` gates client-side init.
- **Data residency:** PostHog EU region selected so AU customer data lands in Frankfurt, consistent with Privacy Act 1988 schedule 1 (APP 8.1 disclosure).
- **Retention:** PostHog default (7 years for events). Reduce when a paying customer requires it.

## Hand-off

Next: `/funnel-instrumentation-spec` translates these events into the funnel-model thresholds, and `/experiment-data-collection-plan TC-007` wires the H-002 test card to the `redline_export_clicked` event.
