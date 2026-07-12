---
name: digital-prototype
description: Drive the digital prototype workflow — delegates to figma-design-handoff for Figma metadata and tokens, captures screenshots, produces a feedback-collection plan. Writes 08-prototype/digital/<slug>/README.md.
argument-hint: "<concept-slug-or-finalist-id> [optional: <figma-file-id>]"
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# digital-prototype

Idempotency: one digital-prototype README per `<slug>`; re-running updates the README in place.

Graceful degrade: if the Figma MCP is not connected, the skill scaffolds the README with a stub component inventory and tokens placeholder, and recommends connecting the MCP before the next pass.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Read the converged finalist matching `$ARGUMENTS`.
3. Read the matching `08-prototype/paper/<slug>.md` if it exists. The
   guidance is paper-first; warn if there's no paper prototype yet.
4. If a Figma file ID is provided, plan to delegate to
   `figma-design-handoff`.

## Phase 2: Decide fidelity

The digital prototype's fidelity should match its purpose:

- **Click-through Figma**: tests usability and aesthetic
- **Coded prototype**: tests interactive behaviours, perf, real data
- **Wizard of Oz**: front-end real, backend manual; tests engagement
  with the experience

For most ventures at this stage, click-through Figma is the right
choice.

## Phase 3: Delegate to figma-design-handoff

If Figma file given, invoke `/figma-design-handoff <file-id>`. The
output lands in `08-prototype/digital/<slug>/`.

If no Figma file yet, scaffold the folder with a stub README and a
recommendation to create one. Surface the reference design tokens
from `tokens.json` if they exist.

## Phase 4: Plan feedback collection

For the digital prototype, plan:

- Test target: how many sessions?
- Tasks: what specific job-to-be-done will participants attempt?
- Probes: open questions during the session
- Hypothesis touch-points: what does each session tell us about which
  hypothesis?

## Phase 5: Write

Append to `08-prototype/digital/<slug>/README.md`:

```markdown
---
title: Digital prototype — <concept>
slug: digital-<slug>
type: prototype
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Digital prototype — <concept>

Tests: H-NN
Source paper prototype: [paper/<slug>](../paper/<slug>.md)
Source Figma: <file-id>

## Fidelity

<click-through Figma | coded | Wizard of Oz>

## Figma handoff

(See [Figma handoff](./README.md) — auto-populated by
figma-design-handoff if MCP available)

## Feedback collection plan

- Sessions: <N>
- Task: <the job-to-be-done>
- Probes: ...
- Hypothesis touch-points: H-NN

Use `/prototype-feedback-collect <slug>` for each session.
```

## Phase 6: Cascade

Recommend running `/prototype-feedback-collect <slug>` for each test
session.

## Phase 7: Log

Append: `## [<today>] digital-prototype | <slug>`.

## Important principles

- **Paper before digital.** Digital is more expensive to be wrong on.
- **Fidelity matches purpose.** Don't code when click-through suffices.
- **Hypothesis-anchored.** Every digital prototype tests at least one
  hypothesis.
- **Use figma-design-handoff for the Figma side.** Don't re-implement
  Figma access here.
- **Prototype-vs-MVP gate applies.** Digital prototypes are still
  prototypes; the gate refuses MVP labels.
