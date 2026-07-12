---
title: MVP deploy plan
slug: mvp-deploy-plan
type: deploy-plan
status: active
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# MVP deploy plan

**Tech stack:** [tech-stack](../tech-stack.md)
**Architecture:** [architecture](../architecture/architecture-overview.md)

## Sub-plans

- [{{x|space}}] Vercel — see [deploy/vercel.md](vercel.md)
- [{{x|space}}] Cloudflare — see [deploy/cloudflare.md](cloudflare.md)
- [{{x|space}}] Other ({{e.g. Fly.io, Render}})

## Cross-check

### Env vars

| Var | Vercel | Cloudflare | Match? |
|-----|--------|-----------|--------|
| {{NAME}} | {{yes|no}} | {{yes|no}} | {{ok|drift}} |

### DNS / domains

- Production: {{domain}} → {{primary host}}
- Apex routing: {{provider}}
- Preview: {{pattern}}

### Observability

- Errors: {{Sentry / Datadog}}
- Analytics: {{PostHog / GA4}}
- No double-instrumentation

## Open issues from sub-plans

- {{summary}}

## Recommendation

{{Proceed | proceed with mitigations | revisit}}
