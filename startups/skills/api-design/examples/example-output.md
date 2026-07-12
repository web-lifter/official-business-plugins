---
title: API design
slug: api-design
type: adr
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# API design

**Style:** REST (OpenAPI 3.1)
**Tech stack:** [tech-stack](../tech-stack.md) — Next.js 15 App Router + Supabase + Cloudflare Workers
**Architecture:** [architecture-overview](architecture-overview.md)

## Cross-cutting contracts

### Auth
- All `/api/*` routes require a Supabase session cookie set by `@supabase/ssr`.
- Cloudflare Worker endpoints (`/llm/*`) accept a short-lived signed JWT minted by the Next.js layer (RS256, 5 min TTL).
- `/api/admin/*` requires `role = 'owner'` on the user's membership row (RLS-enforced via Postgres function `current_role()`).

### Error contract
RFC 9457 Problem Details for HTTP APIs. Body shape:

```json
{
  "type": "https://contractiq.com.au/errors/upload-too-large",
  "title": "Upload too large",
  "status": 413,
  "detail": "Contract file exceeds the 25 MB MVP limit.",
  "instance": "/api/contracts/upload",
  "trace_id": "01HXY..."
}
```

### Rate limits
| Class | Limit | Applies to |
|-------|-------|-----------|
| `anon-read` | 60 req/min/IP | `GET /api/public/*` |
| `auth-read` | 600 req/min/user | `GET /api/contracts`, etc. |
| `auth-write` | 60 req/min/user | mutating endpoints |
| `llm-classify` | 10 req/min/org | `POST /llm/classify` (expensive) |

Enforced via Cloudflare Workers KV + sliding window.

### Idempotency
`Idempotency-Key` header required on `POST /api/contracts/upload` and `POST /api/redlines`. Keys retained 24 h in KV; replay returns the stored response.

### Versioning
None for MVP. The single deployed version is the contract. Breaking changes after first paying customer trigger an ADR.

## Routes / operations

| Path | Method | Auth | Rate class | Idempotent | Body | Response |
|------|--------|------|------------|-----------|------|----------|
| `/api/contracts` | GET | authn | auth-read | n/a | — | `Contract[]` (RLS-scoped) |
| `/api/contracts/upload` | POST | authn | auth-write | yes | `multipart/form-data` (file ≤ 25 MB) | `{ contract_id, status }` |
| `/api/contracts/{id}` | GET | authn | auth-read | n/a | — | `Contract` |
| `/api/contracts/{id}/findings` | GET | authn | auth-read | n/a | — | `Finding[]` |
| `/api/contracts/{id}/findings/{fid}` | PATCH | authn | auth-write | yes | `{ status: 'accepted'|'rejected', comment? }` | `Finding` |
| `/api/redlines` | POST | authn | auth-write | yes | `{ contract_id }` | `{ redline_id, download_url }` |
| `/llm/classify` | POST | service-jwt | llm-classify | yes | `{ contract_id }` | `{ run_id }` (async; webhook on done) |

## Error catalogue

| Code | Meaning | Body shape |
|------|---------|-----------|
| 400 `validation-failed` | Body fails JSON schema | Problem Details + `errors[]` |
| 401 `not-authenticated` | Missing/expired session | Problem Details |
| 403 `not-authorised` | RLS denial or role mismatch | Problem Details |
| 404 `not-found` | Resource absent or RLS-hidden | Problem Details |
| 409 `idempotency-replay` | Same key, different body | Problem Details |
| 413 `upload-too-large` | File > 25 MB MVP limit | Problem Details |
| 422 `unsupported-format` | Not `.docx` or `.pdf` | Problem Details |
| 429 `rate-limited` | Class limit exceeded | Problem Details + `Retry-After` |
| 503 `llm-unavailable` | Anthropic upstream error | Problem Details |

## OpenAPI / GraphQL schema

```yaml
openapi: 3.1.0
info:
  title: ContractIQ API
  version: 0.1.0
servers:
  - url: https://contractiq.com.au/api
paths:
  /contracts/upload:
    post:
      operationId: uploadContract
      security: [{ supabaseSession: [] }]
      parameters:
        - in: header
          name: Idempotency-Key
          required: true
          schema: { type: string, format: uuid }
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file: { type: string, format: binary }
      responses:
        '202':
          description: Accepted — classifier run queued
          content:
            application/json:
              schema:
                type: object
                properties:
                  contract_id: { type: string, format: uuid }
                  status: { type: string, enum: [queued] }
```

Full spec lives at `09-mvp/architecture/openapi.yaml` and is hand-maintained until route count exceeds ~30.
