---
name: mvp-feasibility
description: Surface technical, regulatory, and resource feasibility risks. Reads outputs of mvp-tech-plan, mvp-schema-plan, mvp-deploy-plan plus optional Supabase/Cloudflare MCP quota probes. Writes 09-mvp/feasibility.md.
argument-hint: [no args]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# mvp-feasibility

Idempotency: side-effect-free planner; rewrites `09-mvp/feasibility.md` in place.

Graceful degrade: without the Supabase / Cloudflare MCPs the advisory section is omitted and the verdict is flagged "advisory data unavailable".

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `mvp-spec.md`, `tech-stack.md`, `architecture-overview.md`,
   `schema/migrations-plan.md`, `deploy/vercel.md`,
   `deploy/cloudflare.md`, `analytics/events-spec.md`.
3. If Supabase MCP available, probe `get_advisors` for
   security/performance advisories on the project (read-only).
4. If Cloudflare MCP available, check account state for resource
   ceilings (workers per script, KV namespace count, etc.).

## Phase 2: Walk feasibility categories

For each category, surface risks:

### Technical
- Components that haven't been used together before (compatibility)
- Connectors with known limits we approach (Worker CPU time, Edge
  runtime constraints, Postgres connection limits, etc.)
- Missing pieces (e.g. no caching layer when funnel implies high
  read volume)

### Regulatory / legal
- Privacy: PII handling, GDPR / CCPA / Australian Privacy Act
- Industry-specific: financial / health / education
- Accessibility: WCAG compliance for the segment

### Resource
- Team capacity vs estimate from `build-plan.md` (if exists)
- Budget vs cost from `revenue-cost-sketch.md` and deploy plans
- Timeline vs market window

### Open questions
- Pull existing `.open-questions/<slug>.md` files; check which would
  block MVP build

## Phase 3: Score and verdict

For each risk, score `low / medium / high`. Verdict:

- 🟢 — no high risks; medium risks have mitigations
- 🟡 — some high risks, with plausible mitigations
- 🔴 — high risk(s) without mitigation; MVP build is risky

## Phase 4: Write

Write `09-mvp/feasibility.md`:

```markdown
---
title: MVP feasibility
slug: feasibility
type: mvp-spec
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# MVP feasibility

Verdict: 🟢 | 🟡 | 🔴

## Technical risks

| Risk | Severity | Mitigation |

## Regulatory risks

| Risk | Severity | Mitigation |

## Resource risks

| Risk | Severity | Mitigation |

## Open questions blocking

- [<slug>](../.open-questions/<slug>.md): <severity>

## Connector advisories (if probed)

### Supabase advisors
- ...

### Cloudflare account state
- ...

## Recommendation

<Proceed | proceed with these mitigations | revisit before build>
```

## Phase 5: Cascade

If 🟢 → recommend `/mvp-build-plan`.
If 🟡 → list the mitigations needed before building.
If 🔴 → recommend revisiting the offending sub-plan.

## Phase 6: Log

Append: `## [<today>] mvp-feasibility | <verdict>`.

## Important principles

- **All four categories.** Skipping regulatory is a known failure
  mode.
- **Risks have mitigations.** Empty mitigation column promotes risk
  severity.
- **Connector probes are read-only.** No mutations.
- **Honest verdict.** 🔴 isn't a sign the venture is bad — it's a sign
  to address risk before building.
