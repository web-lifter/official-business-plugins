---
title: API design
slug: api-design
type: adr
status: active
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# API design

**Style:** {{REST | GraphQL | both}}
**Tech stack:** [tech-stack](../tech-stack.md)
**Architecture:** [architecture-overview](architecture-overview.md)

## Cross-cutting contracts

### Auth
{{Bearer JWT? Cookie session via @supabase/ssr? Service-role for internal endpoints?}}

### Error contract
{{HTTP status x error body shape. Cite RFC 9457 (Problem Details) if used.}}

### Rate limits
{{Per-endpoint class, per-user, per-IP, anonymous.}}

### Idempotency
{{Idempotency-Key header strategy for mutating POSTs.}}

### Versioning
{{URL prefix? Header? None for MVP?}}

## Routes / operations

| Path | Method | Auth | Rate class | Idempotent | Body | Response |
|------|--------|------|------------|-----------|------|----------|
| {{/path}} | {{GET}} | {{public|authn|role:X}} | {{class}} | {{yes|no}} | {{schema}} | {{schema}} |

## Error catalogue

| Code | Meaning | Body shape |
|------|---------|-----------|
| {{HTTP+app code}} | {{when raised}} | {{Problem Details fields}} |

## OpenAPI / GraphQL schema

```yaml
# Inline minimal version (full spec generated when implementation begins).
```
