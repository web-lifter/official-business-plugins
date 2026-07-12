---
name: mvp-type-select
description: Choose between pre-order, audience-building, show-and-tell, or partial-product MVP types. Each is a real MVP; they test different things. Updates 09-mvp/mvp-spec.md.
argument-hint: [no args]
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# mvp-type-select

Method: the four MVP archetypes (pre-order / audience-building / show-and-tell / partial product) sit alongside the build-measure-learn loop in Ries 2011 — see `startups/SOURCES.md`.

Idempotency: safe to re-run; updates the "MVP type" section of `mvp-spec.md` in place. Rationale history captured in `.memex/log.md`.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Read `09-mvp/mvp-spec.md`. Halt if missing — route to `/mvp-scope`.
3. Read primary hypothesis (linked from spec).

## Phase 2: Apply selection matrix

Match the primary hypothesis question to MVP type:

| Question | Best MVP type |
|---|---|
| "Will they pay?" | Pre-order |
| "Are they engaged?" | Audience-building |
| "Do they want it?" | Show-and-tell |
| "Will they use a thin slice?" | Partial product |

If the hypothesis is multi-faceted, prefer the type that addresses
the most expensive uncertainty.

## Phase 3: Confirm

Use `AskUserQuestion` to confirm the recommendation; user can override.

## Phase 4: Update spec

Update `09-mvp/mvp-spec.md`'s "MVP type" section with:

- Selected type
- Rationale (which question it answers)
- Concrete instantiation (e.g. "Pre-order: Stripe checkout link, hard
  promise to deliver in 90 days, refund-if-not-launched policy")
- Success threshold

## Phase 5: Log

Append: `## [<today>] mvp-type | <type> selected`.

## Important principles

- **Each type is a real MVP if executed correctly.** A pre-order page
  with no commitment ask is a prototype, not an MVP — see
  `prototype-vs-mvp-distinguish`.
- **Type drives instrumentation.** Pre-order needs payment events;
  audience-building needs subscribe-then-open events. Hands off to
  `mvp-analytics-plan`.
- **Re-runnable.** Type can be re-selected; the rationale change is
  recorded.
