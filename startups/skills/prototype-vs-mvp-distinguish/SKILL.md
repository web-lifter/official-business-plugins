---
name: prototype-vs-mvp-distinguish
description: Classify an artifact against the 5-dimension prototype-vs-MVP rubric (audience, fidelity, scope, environment, what-it-proves). Refuses to label a prototype as an MVP. Blocking — `--force` overrides, override is logged.
argument-hint: <artifact-path-or-slug>
allowed-tools: Read Edit Glob Grep
effort: low
---

# prototype-vs-mvp-distinguish

Methodology: Lean Startup MVP definition (Ries, 2011) — "the version of a new product that allows a team to collect the maximum amount of validated learning about customers with the least effort." Combined with the Strategyzer testing literature (test card / learning card discipline). See `references.md`.

**Blocking** — the gate refuses to flip an artifact's `type:` to `mvp-spec` if any of the five dimensions fails. Override with `--force`; the override is logged loudly in the venture's running log so the audit trail catches it. All five dimensions are conjunctive: a single failure halts the type change.

Idempotency: re-running on the same artifact re-evaluates and re-writes the verdict; the prior verdict is overwritten (the log entry preserves history).

## User Context

$ARGUMENTS

`<artifact-path-or-slug>` is required. The artifact is typically
`09-mvp/mvp-spec.md` (when checking on creation) or any prototype
file the user is considering relabelling.

## Phase 1: Pre-flight

1. Verify venture profile.
2. Read the artifact and any spec it references.

## Phase 2: Apply the five dimensions

For each dimension, evaluate:

1. **Audience** — is the audience the segment's earlyvangelists
   (named, with contact details)? Not internal team, not friendlies.
2. **Fidelity** — is the shipped slice production-quality? Not
   click-through, not paper.
3. **Scope** — is the scope the smallest end-to-end thing that tests
   the *primary* hypothesis? Not nice-to-haves, not adjacent
   features.
4. **Environment** — is it live? Real auth, real data, real billing
   if billing is in the hypothesis. Not sandboxed.
5. **What it proves** — does the artifact state which hypothesis it
   tests, with what threshold, in what timeframe?

## Phase 3: Verdict

- All five pass → MVP. Allow the type flip; recommend the user run
  `/mvp-metrics` if metrics aren't yet defined.
- One or more fail → prototype. Refuse to set `type: mvp-spec`.
  Surface the failures with specific actions.

## Phase 4: Write or block

If pass:

- (Optional) update the artifact's `type:` to `mvp-spec` if the user
  asked.
- Append log: `## [<today>] mvp-gate | <slug> passes 5-dim check`.

If fail without `--force`:

- Refuse, surface the failure list, do not modify the artifact.

If fail with `--force`:

- Allow the type change; append log:
  `## [<today>] gate-override | prototype-vs-mvp-distinguish bypassed
  for <slug> (failed: <list>)`.

## Important principles

- **All five must pass.** Conjunctive, not majority.
- **Specific failure messages.** "Fidelity fail" is useless;
  "Fidelity fail — prototype is a Figma click-through; an MVP needs a
  shipped product slice."
- **--force is logged loudly.** The user is making a judgement call;
  the audit trail catches it.
- **Read-only on every other artifact.** This skill only edits the
  one artifact's `type:` field, and only with `--force` or after a
  pass.

## Edge cases

1. Hybrid (Wizard of Oz, Concierge) — usually MVP-class if the
   audience is real customers and they paid, even though fidelity is
   manual. The "fidelity" check accepts manual delivery as production
   for service-class products.
2. Pre-order page with hard commitment — usually MVP (audience-
   building or pre-order type per Ch. 6 menu).
3. Demo-only landing page with no commitment — prototype, not MVP.
