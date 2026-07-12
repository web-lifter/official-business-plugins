# vercel-deploy-plan — references

## Canonical product docs

- **Vercel — Project configuration (`vercel.json`).** <https://vercel.com/docs/projects/project-configuration>
- **Vercel — Frameworks: Next.js.** <https://vercel.com/docs/frameworks/nextjs>
- **Vercel — Function runtimes (Edge vs Node).** <https://vercel.com/docs/functions/runtimes>
- **Vercel — Environment variables.** <https://vercel.com/docs/projects/environment-variables>
- **Vercel — Preview deployments.** <https://vercel.com/docs/deployments/preview-deployments>
- **Vercel — Domains and DNS.** <https://vercel.com/docs/projects/domains>
- **Vercel — Image optimisation.** <https://vercel.com/docs/image-optimization>
- **Vercel — Analytics and Speed Insights.** <https://vercel.com/docs/analytics>

## Next.js

- **Next.js 15 — App Router.** <https://nextjs.org/docs/app>
- **Next.js — Rendering modes (SSG / SSR / ISR).** <https://nextjs.org/docs/app/building-your-application/rendering>
- **`@supabase/ssr` — Next.js App Router pattern.** <https://supabase.com/docs/guides/auth/server-side/nextjs>

## Observability

- **Sentry for Next.js.** <https://docs.sentry.io/platforms/javascript/guides/nextjs/>

## Rules this skill enforces

1. **Plan, never deploy.** This skill never runs `vercel` CLI commands. The user runs them.
2. **Per-route runtime decision.** Edge vs Node serverless matters for cold-start, library compatibility, and latency — chose per route, not per project.
3. **Env vars per environment.** Production / preview / development sets are distinct; `vercel env add` is repeated per environment.
4. **Observability designed in.** Sentry, Vercel Analytics, Speed Insights all up front — adding them post-launch is harder than wiring them at project init.
5. **No PII through Vercel logs.** Avoid logging request bodies on routes that handle contract uploads.
6. **Production deploys only from `main`.** Preview deploys cover everything else.

## Graceful degrade

There is no Vercel MCP. This skill is always docs-only; account-state introspection is replaced with explicit "Tom will verify in the Vercel dashboard before deploy" notes.

See `startups/SOURCES.md` for the broader citation context.
