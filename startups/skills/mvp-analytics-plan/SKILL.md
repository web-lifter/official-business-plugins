---
name: mvp-analytics-plan
description: Translate mvp-metrics into an analytics implementation — event taxonomy, properties, identity model, tool selection (PostHog / GA4 / Plausible / Mixpanel). Writes 09-mvp/analytics/events-spec.md.
argument-hint: [optional: --tool=posthog|ga4|plausible|mixpanel]
allowed-tools: Read Write Edit Glob Grep
effort: high
---

# mvp-analytics-plan

Idempotency: side-effect-free planner; rewrites `09-mvp/analytics/events-spec.md` in place.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `mvp-metrics.md`. Halt if missing.
3. Read `mvp-spec.md` for the user flows to instrument.
4. Read `funnel-model.md` if it exists.

## Phase 2: Tool selection

Match metric needs to tool:

| Need | Best fit |
|---|---|
| Generalist + product analytics + session replay | PostHog |
| Web analytics, marketing | GA4 |
| Privacy-friendly, simple | Plausible |
| Product analytics, cohorts | Mixpanel |

Default for the Web Lifter stack: PostHog (self-host or cloud).

## Phase 3: Event taxonomy

Define events in `verb_object` form:

- `user_signed_up`
- `pricing_viewed`
- `checkout_started`
- `checkout_completed`
- `feature_x_activated`

For each event:

- Where it fires (route / component / server)
- Properties (user / event-specific)
- Sample rate (1.0 by default)

## Phase 4: Identity model

- Anonymous user → assigned `distinct_id` on first visit
- On sign-up → `alias` to user UUID
- On sign-out → reset to new anonymous ID

## Phase 5: Property dictionary

Per-event properties + global super-properties:

- `app_version`
- `auth_state` (anon / user)
- `tenant_id` (for SaaS pattern)
- `route`

## Phase 6: Write

Write `09-mvp/analytics/events-spec.md`:

```markdown
---
title: Events spec
slug: events-spec
type: analytics-plan
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Events spec

Tool: <PostHog | GA4 | Plausible | Mixpanel>
Source metrics: [mvp-metrics](../mvp-metrics.md)

## Identity model

- Anonymous: assigned distinct_id at first visit
- Signed-in: aliased to user UUID
- Signed-out: reset to new anonymous distinct_id

## Global properties (super-properties)

| Property | Type | When to set |

## Events

### user_signed_up
- Where: server, after profile insert
- Properties: { source, plan, referrer }
- Maps to metric: H-NN signup conversion

### pricing_viewed
- Where: client, on `/pricing` mount
- Properties: { plan_focus }

(... more events ...)

## Configuration

\`\`\`ts
// posthog.init({ api_host: ..., autocapture: false })
\`\`\`

## Privacy

- PII never sent to analytics: emails, names, addresses excluded
- IP anonymisation: on
- Cookie consent: required for EU; banner via X
```

## Phase 7: Cascade

Recommend `/funnel-instrumentation-spec` to translate the
funnel-model into events.

Recommend `/experiment-data-collection-plan` for each open test card
that needs data capture.

## Phase 8: Log

Append: `## [<today>] mvp-analytics-plan | <tool>; <N> events`.

## Important principles

- **No PII in analytics.** Email, name, address never sent.
- **Verb-object event names.** Consistent.
- **Global properties keep events clean.** Don't repeat per event.
- **Tool defaults.** PostHog for the Web Lifter stack unless reason to
  override.
- **No connector calls.** Analytics tools have their own MCPs not
  used here.
