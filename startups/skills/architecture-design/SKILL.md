---
name: architecture-design
description: Produce a system-architecture document — Mermaid component diagram, data-flow diagram, integration surface, sync/async boundaries. One file per architectural decision under 09-mvp/architecture/.
argument-hint: [optional: --topic=<focus-area>]
allowed-tools: Read Write Edit Glob Grep
effort: high
---

# architecture-design

Idempotency: side-effect-free planner; rewrites `09-mvp/architecture/architecture-overview.md` in place. Never touches infra. Re-runs that materially change topology should be paired with a fresh ADR via `/adr-writer`.

Delegation chain: `/mvp-tech-plan` calls `/tech-stack-recommender` then this skill, then `/adr-writer` to formalise major decisions.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `09-mvp/tech-stack.md`. Halt if missing.
3. Read `mvp-spec.md`, `mvp-metrics.md` for what needs to be built.

## Phase 2: Generate diagrams

Compose:

- **Component diagram** — Mermaid `graph TB`. Browser → CDN → app
  layer → DB / cache / queue / blob store. Annotate each component
  with its provider (Vercel, Cloudflare Worker, Supabase, etc.).
- **Data flow diagram** — Mermaid `sequenceDiagram`. The primary
  user flow from sign-up to value-revealing event.
- **Integration surface** — list of external services and the call
  pattern (sync / async / webhook).
- **Sync/async boundaries** — for each integration, why is it
  sync/async? Cost, latency, failure mode.

## Phase 3: Write

Write `09-mvp/architecture/architecture-overview.md`:

```markdown
---
title: Architecture overview
slug: architecture-overview
type: adr
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Architecture overview

Tech stack: [tech-stack](../tech-stack.md)
MVP spec: [mvp-spec](../mvp-spec.md)

## Component diagram

\`\`\`mermaid
graph TB
  Browser[Browser] --> CDN[Cloudflare CDN]
  CDN --> Vercel[Vercel - Next.js 15]
  Vercel --> Supabase[(Supabase Postgres)]
  Vercel --> Workers[Cloudflare Workers]
  Workers --> Supabase
\`\`\`

## Primary user flow

\`\`\`mermaid
sequenceDiagram
  Browser->>Vercel: GET /
  Vercel->>Browser: Server-rendered landing page
  Browser->>Vercel: POST /signup
  Vercel->>Supabase: insert user
  Supabase-->>Vercel: user
  Vercel->>Browser: 302 /dashboard
\`\`\`

## Integration surface

| Service | Pattern | Why this pattern |

## Sync / async boundaries

| Boundary | Mode | Reason |

## Risks and unknowns

- <component>: <risk> — <mitigation> or open question
```

## Phase 4: Cascade

Recommend `/adr-writer` for each major decision the architecture
implies (e.g. "Use Workers for X, Vercel functions for Y").

## Phase 5: Log

Append: `## [<today>] architecture | overview written`.

## Important principles

- **Mermaid, always.** Source-controlled diagrams.
- **Annotate components with providers.** "App" is useless;
  "Vercel — Next.js 15 SSR" is informative.
- **Sync/async called out.** Most architectural bugs live at these
  boundaries.
- **Don't over-design.** MVP architecture is allowed to be naive.
- **No connector calls.** Local-only.
