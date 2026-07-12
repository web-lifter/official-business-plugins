---
name: vercel-deploy-plan
description: Vercel deployment plan — project setup, env vars, preview branches, edge-vs-serverless function choice, ISR rules, image optimisation, observability. No Vercel MCP — uses CLI commands and docs. Produces a plan, never deploys.
argument-hint: [no args]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# vercel-deploy-plan

Cites the connector-confirmation idiom in
[`shared/reference/connector-confirmation.md`](../../../../shared/reference/connector-confirmation.md).
**No skill in this marketplace ever runs `vercel ...`.**

Idempotency: side-effect-free planner; rewrites `09-mvp/deploy/vercel.md` in place.

Graceful degrade: there is no Vercel MCP — this skill is always docs-only. The user runs the listed `vercel` CLI commands manually.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `tech-stack.md` and confirm Vercel is the chosen front-end host.
3. Read `architecture-overview.md` for the component layout.
4. Read `mvp-spec.md` for the surfaces to deploy.

## Phase 2: Decide structure

For each runtime decision:

- **Static vs SSR vs ISR vs SSG** per route
- **Edge vs Node serverless** per API route
- **Image optimisation**: which sources, what formats
- **Preview deploys**: per-PR? Branch-per-feature?
- **Env variables**: what's needed (Supabase URL, anon key, secrets)
- **Domains**: production, preview, custom
- **Observability**: Vercel Analytics? Speed Insights? External APM?
- **Error handling**: error boundary structure, 404/500 pages

## Phase 3: Write

Write `09-mvp/deploy/vercel.md`:

```markdown
---
title: Vercel deploy plan
slug: deploy-vercel
type: deploy-plan
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Vercel deploy plan

Tech stack: [tech-stack](../tech-stack.md)
Architecture: [architecture](../architecture/architecture-overview.md)

## Project setup

- Repo: <url>
- Framework preset: Next.js 15
- Node version: 20.x
- Build command: `next build`
- Output directory: `.next`
- Install command: `pnpm install` (or npm / yarn)

## Routing strategy

| Route | Mode | Notes |
|---|---|---|
| `/` | SSR | landing page |
| `/dashboard/*` | SSR | authenticated |
| `/api/webhook/*` | Edge | low-latency third-party callbacks |
| `/api/*` | Node serverless | most API routes |
| `/blog/*` | ISR | revalidate 1h |

## Environment variables

| Name | Type | Source |
|---|---|---|
| NEXT_PUBLIC_SUPABASE_URL | public | Supabase project |
| NEXT_PUBLIC_SUPABASE_ANON_KEY | public | Supabase project |
| SUPABASE_SERVICE_ROLE_KEY | secret | Supabase project |
| ... |

Set via `vercel env add` (the user runs this manually).

## Preview deploys

- Per-PR enabled
- Branch-protection: main / production deploys only from main
- Preview URL pattern: <project>-<branch>-<team>.vercel.app

## Observability

- Vercel Analytics: enabled
- Speed Insights: enabled
- External APM: <Sentry / Datadog / none>

## Domains

- Production: <example.com>
- Preview: <vercel default>

## Image optimisation

- Sources allowed: <list>
- Formats: WebP, AVIF
- Sizes preset: <list>

## CLI commands the user will run

```sh
# Initial link
vercel link

# Add env vars (per environment)
vercel env add NEXT_PUBLIC_SUPABASE_URL production
vercel env add NEXT_PUBLIC_SUPABASE_URL preview
vercel env add NEXT_PUBLIC_SUPABASE_URL development

# Deploy preview from current branch (manual)
vercel

# Deploy production
vercel --prod
```

**No skill in this marketplace runs these commands.** The user runs
them.

## Risks

- <e.g. ISR + Supabase cache invalidation>
- <e.g. Edge runtime incompatibility with some Supabase libs>
```

## Phase 4: Cascade

Pair with `/cloudflare-deploy-plan` if Workers / R2 / KV / D1 are also
in scope.

## Phase 5: Log

Append: `## [<today>] vercel-deploy-plan | written`.

## Important principles

- **Plan, never deploy.** This skill never runs Vercel CLI.
- **Per-route runtime decisions.** Edge vs Node matters for latency
  and lib compatibility.
- **Env vars per environment.** Production / preview / development.
- **Observability up front.** Adding it post-launch is harder than
  designing it in.
