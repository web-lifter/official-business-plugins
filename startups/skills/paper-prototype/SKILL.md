---
name: paper-prototype
description: Generate a paper-prototype script — the screens / states / interactions sketched as text or pen-and-paper, and a guided run-through script. Cheaper to be wrong on paper. Writes 08-prototype/paper/<slug>.md.
argument-hint: <concept-slug-or-finalist-id>
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# paper-prototype

Methodology: "paper before pixels" — low-fidelity sketches are cheaper to be wrong on than digital prototypes.

Idempotency: one paper-prototype file per `<slug>`; re-running overwrites with a new draft (status flips back to `draft` if the prior was `active`).

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read the converged finalists; find the one matching `$ARGUMENTS`.
3. Read segment profile and VPC for context.

## Phase 2: Sketch screens / states

For the concept, list:

- The 3-7 screens / states the prototype needs (e.g. landing,
  sign-up, first-run wizard, value-revealing screen, paywall, success)
- For each, the rough layout (text description, ASCII sketch, or a
  prompt for the user to draw on paper)
- The transitions between screens (what triggers each)

Keep it minimal. A paper prototype with 12 screens is a digital
prototype trying to escape.

## Phase 3: Compose the run-through script

Write a script for guiding a participant through the prototype:

1. **Setup** — what we tell the participant before starting
2. **Task** — the specific job-to-be-done we ask them to complete
3. **Probes** — open questions to ask along the way ("What did you
   expect to happen?")
4. **Close** — the four interview closers (why, why not, who else,
   can we follow up)

## Phase 4: Write

Write `08-prototype/paper/<slug>.md`:

```markdown
---
title: Paper prototype — <concept>
slug: paper-<slug>
type: prototype
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Paper prototype — <concept>

Tests: H-NN (<hypothesis>)
Segment: <slug>

## Screens / states

### Screen 1: <name>
<layout description / ASCII sketch>

### Transition 1 → 2
<trigger>

### Screen 2: ...
...

## Run-through script

### Setup
"Thanks for trying this out. It's a paper prototype — rough sketches.
Don't worry about polish; tell me what you'd do at each step."

### Task
"<the job-to-be-done>"

### Probes (use as relevant)
- "What did you expect to happen?"
- "What were you hoping to find?"
- "If this were a real tool, would you use it?" → "Why / why not?"

### Close
- "Why does this matter to you?"
- "Who else should try this?"
- "Can we follow up after a few sessions?"

## Recording

Use `/prototype-feedback-collect <slug>` to log each session.
```

## Phase 5: Log

Append: `## [<today>] paper-prototype | <slug> drafted`.

## Important principles

- **Minimal screens.** ≤ 7. More is digital prototype territory.
- **Run-through script is the artifact.** Without it, the prototype
  isn't testable.
- **Hypothesis-anchored.** State which hypothesis the prototype tests.
- **Use as part of `prototype-vs-mvp-distinguish`.** Paper prototypes
  are unambiguously prototypes; the gate refuses to mark them as MVPs.

## Edge cases

1. Concept needs persistence (an account, saved state) — paper
   prototype can fake it (cards on a table); flag the limitation.
2. Voice / non-visual interface — script the dialogue, not screens.
3. Multi-actor concept — script per actor; run with a paired
   participant.
