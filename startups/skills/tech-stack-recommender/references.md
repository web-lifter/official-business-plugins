# tech-stack-recommender — references

## Framework / platform docs

- **Next.js 15 — App Router.** <https://nextjs.org/docs/app>
- **React 19 release notes.** <https://react.dev/blog/2024/12/05/react-19>
- **Vercel — frameworks.** <https://vercel.com/docs/frameworks>
- **Astro.** <https://docs.astro.build/>
- **SvelteKit.** <https://kit.svelte.dev/docs>
- **Remix.** <https://remix.run/docs/en/main>
- **Expo (React Native).** <https://docs.expo.dev/>

## Backend / data

- **Supabase.** <https://supabase.com/docs>
- **Cloudflare Workers platform.** <https://developers.cloudflare.com/workers/>
- **PostgreSQL.** <https://www.postgresql.org/docs/current/>
- **Fly.io.** <https://fly.io/docs/>

## Methodological grounding

- **Ries, Eric.** *The Lean Startup.* Crown Business, 2011. — Hypothesis-class framing (demand / usability / scale) used to map MVP needs to stack capabilities.
- **Maurya, Ash.** *Running Lean* (3rd ed.). O'Reilly, 2022. — Speed-to-MVP discipline; the "default opinionated stack" rule traces here.

## Rules this skill enforces

1. **Default is opinionated.** The Web Lifter default (Next.js 15 + Supabase + Cloudflare Workers + Vercel + Figma) works for ~80% of MVPs. Override needs a deliberate reason.
2. **Connector ecosystem is a tie-breaker.** Skills downstream depend on the stack choice; an alternative stack costs tooling leverage and that cost must be paid back in scoring.
3. **Hypothesis class drives the recommendation.** Demand vs usability vs scale leads to different "fast enough" trade-offs.
4. **Read-only on the venture.** Writes only `tech-stack.md`. Mutations belong to `/migration-plan` and the deploy plan skills.
5. **No connector calls.** This skill is local-only; the chosen stack determines which MCPs the downstream skills will probe.

See `startups/SOURCES.md` for the broader citation context.
