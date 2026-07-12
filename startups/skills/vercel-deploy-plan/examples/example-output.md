---
title: Vercel deploy plan
slug: deploy-vercel
type: deploy-plan
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Vercel deploy plan

**Tech stack:** [tech-stack](../tech-stack.md)
**Architecture:** [architecture](../architecture/architecture-overview.md)

## Project setup

- Repo: `https://github.com/contractiq/web` (private)
- Framework preset: Next.js 15 (App Router)
- Node version: 20.x
- Build command: `pnpm build`
- Install command: `pnpm install --frozen-lockfile`
- Output directory: `.next` (Vercel-managed)

## Routing strategy

| Route | Mode | Notes |
|-------|------|-------|
| `/` | SSG | Marketing landing page — fully static |
| `/pricing` | SSG | Static for MVP; promote to ISR when content team takes over |
| `/login`, `/signup` | SSR | Server-rendered with CSRF tokens |
| `/(app)/contracts` | SSR | Authenticated; RLS-scoped read at render |
| `/(app)/contracts/[id]` | SSR | Authenticated; polls Supabase Realtime client-side |
| `/api/contracts/*` | Node serverless | Most API routes; needs Node-API for `@supabase/ssr` cookie handling |
| `/api/webhooks/classifier-done` | Node serverless | Verifies `VERCEL_WEBHOOK_SECRET` HMAC from CF Worker |
| `/api/webhooks/stripe` | Node serverless | Deferred until post-H-002; route stub returns 501 |
| `/_health` | Edge | Status only — fast, runs everywhere |

Edge runtime intentionally avoided for `/api/contracts/*` because `@supabase/ssr` and the docx library have Node-API dependencies that don't run on Vercel Edge.

## Environment variables

| Name | Type | Source |
|------|------|--------|
| `NEXT_PUBLIC_SUPABASE_URL` | public | Supabase project (`xkqj…7w2a`) |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | public | Supabase project |
| `SUPABASE_SERVICE_ROLE_KEY` | secret | Supabase project — server routes only |
| `SUPABASE_URL` | secret | Supabase project — server routes |
| `VERCEL_WEBHOOK_SECRET` | secret | random 32-byte hex; shared with CF Workers |
| `NEXT_PUBLIC_POSTHOG_KEY` | public | PostHog EU project |
| `POSTHOG_API_KEY` | secret | PostHog EU (server events) |
| `SENTRY_DSN` | secret | Sentry `contractiq-web` project |
| `NEXT_PUBLIC_GIT_SHA` | public | injected at build time by Vercel `$VERCEL_GIT_COMMIT_SHA` |

Each set per environment (`production`, `preview`, `development`) via `vercel env add`. Tom runs the CLI manually.

## Preview deploys

- Per-PR: enabled.
- Branch protection: production deploys only from `main` (Vercel "Production Branch" = `main`).
- Preview URL pattern: `contractiq-git-<branch>-contractiq.vercel.app`.
- Preview deployments use the preview Supabase project (`contractiq-preview`), so cohort testing on PR previews is safe.

## Observability

- **Vercel Analytics:** enabled (free tier — pageviews only).
- **Speed Insights:** enabled (free tier — Core Web Vitals).
- **Sentry:** initialised via `@sentry/nextjs`; release tagged with `$VERCEL_GIT_COMMIT_SHA`; source maps uploaded in `vercel-build` step.
- **PostHog** handles all product analytics — no double-counting against Vercel Analytics.

## Domains

- Production: `contractiq.com.au` (apex + `www.` redirect to apex).
- `api.contractiq.com.au` aliased to the same Vercel project.
- Preview: Vercel default pattern (above).
- DNS: Cloudflare authoritative, A records to Vercel anycast; SSL via Vercel.

## Image optimisation

- Sources allowed: `vercel.app` previews, `contractiq.com.au`, `supabase-storage` (signed URLs for cohort-uploaded sample MSAs only, never end-user contracts).
- Formats: WebP, AVIF.
- Sizes: default Next.js `deviceSizes` preset.
- Cohort screenshots and marketing imagery only — never contract content.

## CLI commands the user will run

```sh
# One-time
vercel link

# Env vars (per environment, repeat for production / preview / development)
vercel env add NEXT_PUBLIC_SUPABASE_URL production
vercel env add NEXT_PUBLIC_SUPABASE_ANON_KEY production
vercel env add SUPABASE_SERVICE_ROLE_KEY production
vercel env add SUPABASE_URL production
vercel env add VERCEL_WEBHOOK_SECRET production
vercel env add NEXT_PUBLIC_POSTHOG_KEY production
vercel env add POSTHOG_API_KEY production
vercel env add SENTRY_DSN production

# Deploy
vercel              # preview
vercel --prod       # production (only from main, via CI typically)
```

**No skill in this marketplace runs these commands.** Tom runs them locally.

## Risks

- **ISR + Supabase cache invalidation on `/pricing`** — only matters once `/pricing` becomes dynamic post-MVP; tracked as future work.
- **Vercel Edge runtime gaps** — caused the decision to keep `/api/contracts/*` on Node serverless. Revisit if `@supabase/ssr` ships full Edge support.
- **Vercel function execution timeout (Pro: 60s)** — `/api/contracts/upload` accepts up to 25 MB; multipart parse + Storage upload measured ~6 s in prototype; comfortable.
- **Cold starts on infrequent `/api/webhooks/classifier-done`** — accepted; webhook is async from the user's POV.
