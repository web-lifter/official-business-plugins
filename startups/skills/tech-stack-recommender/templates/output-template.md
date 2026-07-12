---
title: Tech stack
slug: tech-stack
type: adr
status: active
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# Tech stack

**Hypothesis class:** {{demand | usability | scale}}
**MVP type:** {{type}}

## Recommended

**{{stack name}}**

### Rationale

- {{why for this hypothesis class}}
- {{connector ecosystem fit}}
- {{team fit}}

## Alternatives considered

| Stack | Speed | Cost | Connectors | Team fit | Total |
|-------|-------|------|-----------|---------|-------|
| {{name}} | {{score}} | {{score}} | {{score}} | {{score}} | {{total}} |

## Decision

Adopting {{stack}}. ADR to follow via `/adr-writer`.

## Connector consequences

- Supabase MCP → schema via `supabase-schema-design`, apply via `migration-plan`
- Cloudflare MCP → deploy plan via `cloudflare-deploy-plan`
- Vercel CLI → deploy plan via `vercel-deploy-plan` (no MCP, plan only)
- Figma MCP → design handoff via `figma-design-handoff` (if installed)
