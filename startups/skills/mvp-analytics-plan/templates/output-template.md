---
title: Events spec
slug: events-spec
type: analytics-plan
status: active
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# Events spec

**Tool:** {{PostHog | GA4 | Plausible | Mixpanel}}
**Source metrics:** [mvp-metrics](../mvp-metrics.md)

## Identity model

- Anonymous: `distinct_id` assigned at first visit
- Signed-in: aliased to user UUID via `posthog.alias()`
- Signed-out: reset to new anonymous `distinct_id`

## Global super-properties

| Property | Type | When to set |
|----------|------|-----------|
| `app_version` | string | session start |
| `auth_state` | enum | every event |
| `tenant_id` | uuid | post-membership-load |
| `route` | string | every page view |

## Events

### {{event_name}}
- **Where:** {{client|server}}, {{component|route}}
- **Properties:** `{ {{property names}} }`
- **Maps to metric:** {{H-NN}} {{metric}}

## Configuration

```ts
posthog.init(KEY, {
  api_host: '{{eu|us}}.posthog.com',
  autocapture: false,
  capture_pageview: false,
  person_profiles: 'identified_only',
});
```

## Privacy

- PII excluded: email, full name, free-form text
- IP anonymisation: on
- Consent: required for {{regions}}; banner blocks pre-consent
