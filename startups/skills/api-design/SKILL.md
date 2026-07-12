---
name: api-design
description: REST and/or GraphQL API design — route inventory, OpenAPI schema (or GraphQL schema), error contracts, auth and rate-limit decisions, idempotency rules. Writes 09-mvp/architecture/api-design.md.
argument-hint: [optional: --style=rest|graphql|both]
allowed-tools: Read Write Edit Glob Grep
effort: high
---

# api-design

Idempotency: safe to re-run; rewrites `09-mvp/architecture/api-design.md` in place. Treat the file as the current contract — diffs are visible in git history.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `tech-stack.md`, `mvp-spec.md`, latest schema draft if any.
3. Default style is REST unless override.

## Phase 2: Inventory routes

For each user-facing flow in `mvp-spec.md`, list the routes / queries
/ mutations needed:

- Path / operation name
- Method (GET / POST / etc. or query / mutation)
- Auth (public / authenticated / role-restricted)
- Rate limit class
- Idempotency (relevant for POSTs / mutations)
- Body / args
- Response shape
- Error cases

## Phase 3: Define cross-cutting contracts

- **Auth** — bearer JWT? Cookie session? Supabase auth pattern?
- **Error contract** — HTTP status × error body shape; or GraphQL
  errors extension shape
- **Rate limits** — buckets per endpoint class; user / IP / anon
- **Idempotency** — header / key strategy for mutations
- **Versioning** — URL prefix? Header? None for MVP?

## Phase 4: Write

Write `09-mvp/architecture/api-design.md`:

```markdown
---
title: API design
slug: api-design
type: adr
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# API design

Style: REST | GraphQL | both
Tech stack: [tech-stack](../tech-stack.md)

## Cross-cutting contracts

### Auth
...

### Error contract
...

### Rate limits
...

### Idempotency
...

### Versioning
...

## Routes / operations

| Path | Method | Auth | Rate | Idempotent | Body | Response |

## Error catalogue

| Code | Meaning | Body shape |

## OpenAPI / GraphQL schema

(Inline minimal version; full spec hand-written or generated when
implementation begins.)
```

## Phase 5: Log

Append: `## [<today>] api-design | <N> routes`.

## Important principles

- **Auth is per-route.** Don't default everything to "authenticated."
- **Error catalogue is global.** Scattered ad-hoc errors are a known
  bug source.
- **Idempotency for POSTs that matter.** Payment, sign-up, ticket
  create.
- **MVP doesn't need versioning.** Adding it pre-launch is gold-plating.
