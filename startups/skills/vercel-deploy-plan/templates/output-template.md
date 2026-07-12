---
title: Vercel deploy plan
slug: deploy-vercel
type: deploy-plan
status: active
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# Vercel deploy plan

**Tech stack:** [tech-stack](../tech-stack.md)
**Architecture:** [architecture](../architecture/architecture-overview.md)

## Project setup

- Repo: {{url}}
- Framework preset: {{Next.js 15}}
- Node version: {{20.x}}
- Build command: {{`next build`}}
- Install command: {{`pnpm install`}}

## Routing strategy

| Route | Mode | Notes |
|-------|------|-------|
| `/` | {{SSR|SSG|ISR}} | {{notes}} |

## Environment variables

| Name | Type | Source |
|------|------|--------|
| {{NAME}} | {{public|secret}} | {{e.g. Supabase project}} |

## Preview deploys

- Per-PR: {{enabled|disabled}}
- Branch protection: production from `main` only

## Observability

- Vercel Analytics: {{enabled|off}}
- Speed Insights: {{enabled|off}}
- External APM: {{Sentry / Datadog / none}}

## Domains

- Production: {{domain}}
- Preview: {{pattern}}

## Image optimisation

- Sources: {{list}}
- Formats: WebP, AVIF
- Sizes: {{preset}}

## CLI commands the user will run

```sh
vercel link
vercel env add {{NAME}} production
vercel --prod
```

**No skill in this marketplace runs these commands.**

## Risks

- {{e.g. ISR + cache invalidation}}
- {{e.g. Edge runtime library incompatibility}}
