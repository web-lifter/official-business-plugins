---
name: vision-sketch
description: Capture the venture's initial vision as a sketch (not a spec). Forces answers to three questions — top customer problems, how the idea helps, day-in-the-life before vs after — and writes them to 00-vision/vision-sketch.md and day-in-life.md.
argument-hint: [optional one-line venture description]
allowed-tools: Read Write Bash Glob
effort: low
---

# vision-sketch

Idempotency: re-running refreshes the sketch in place, archives the previous version under `00-vision/.archive/`, and bumps `updated:`.

Method: lightweight vision capture before any hypothesis testing. The output is *intentionally* a sketch. No roadmap, no feature list, no
tech stack. Those come later, when hypotheses get tested.

## User Context

$ARGUMENTS

If `$ARGUMENTS` is a one-line description of the venture, use it as a
seed for the vision questions; otherwise prompt the user via
`AskUserQuestion`.

---

## Phase 1: Confirm we're inside a venture

**Objective:** Don't run on the wrong directory.

1. Verify `memex.config.json#/profile == "venture"`. If not, halt with
   the message `not a venture workspace — run /venture-init first`.
2. Read the existing `00-vision/vision-sketch.md` if any. If it has
   `status: active` and the user did not pass `--update`, ask via
   `AskUserQuestion` whether to refresh it (which bumps to v2 and
   archives v1) or abort.

---

## Phase 2: Elicit the three answers

**Objective:** Get specific, tangible answers — not slogans.

Use `AskUserQuestion` with three sequential questions (or one
multi-question call):

1. **Top problems.** "What are the top 1-3 problems your customers face
   today? Be specific. Each problem should be observable — something we
   could see them doing if we shadowed them for an hour." Reject answers
   that are abstract ("inefficiency", "lack of trust") and ask the user
   to ground each in an observable behaviour.
2. **How the idea helps.** "How does your idea help solve them? One
   sentence per problem from question 1. The form is: 'When X happens,
   our idea Y, so the customer Z.'"
3. **Day-in-the-life: before vs after.** "Walk me through what a typical
   customer's day looks like *before* using your idea, then *after*. ≤
   200 words each. Include who they're talking to, what tools they're
   using, and what's frustrating."

If the user stalls, prompt with: "I'd rather get a thin answer now than
a polished one later — we'll refine after the first interview."

---

## Phase 3: Write the files

**Objective:** Write or refresh `00-vision/vision-sketch.md` and
`00-vision/day-in-life.md` with full frontmatter.

1. `00-vision/vision-sketch.md` — three `## ` sections matching the
   three questions, plus a closing `## What we are NOT testing yet`
   section that explicitly lists 2-3 things we're *not* claiming. The
   honest "not yet" list keeps the sketch from feeling like a spec.
2. `00-vision/day-in-life.md` — two `## ` sections (Before / After)
   each ≤ 200 words.
3. Frontmatter on both:
   ```yaml
   ---
   title: <Vision sketch | Day in the life>
   slug: <vision-sketch | day-in-life>
   type: vision
   status: active
   owner: <venture name>
   created: <today>
   updated: <today>
   ---
   ```
4. Append a log entry:
   `## [<today>] vision | sketch written/refreshed`.

---

## Phase 4: Seed the hypothesis register

**Objective:** Each problem from Phase 2 becomes an `open` hypothesis.

For each top problem from Phase 2, append a row to
`01-hypotheses/hypothesis-register.md` with:

- ID: `H-<NN>` (auto-increment)
- Cell: `Customer Segments` (or `Value Propositions` for the "how the
  idea helps" answers — see the cell-mapping table in
  `reference.md`)
- Statement: derived from the answer
- Status: `open`
- Falsifier / Measurement / Threshold / Timeframe: empty (the user fills
  these in via `hypothesis-register` later)

The `hypothesis-falsifiability-check` will flag these next time it runs
— that's the point. Vision-sketch hypotheses are not falsifiable yet;
they get hardened before any testing.

---

## Important principles

- **Sketch, not spec.** No features, no roadmap, no tech.
- **Observable problems only.** "Inefficiency" is not a problem. "Spends
  4 hours every Friday reconciling invoices" is.
- **The 'NOT testing' section is required.** Forces the user to admit
  what they're skipping. Cuts down on surprise pivots later.
- **Hypotheses start as guesses.** This skill seeds the register without
  filling in falsifiers. That's intentional.
- **Re-runnable.** A second invocation refreshes the sketch and bumps
  the file's `updated:` field. Old sketches are archived to
  `00-vision/.archive/<YYYY-MM-DD>-vision-sketch.md`.

## Edge cases

1. **User insists on listing features in the vision** — push back once,
   then accept and add a note: "Features listed in the vision are
   guesses about what the value proposition cell should contain. They
   stay here only until BMC v1 absorbs them."
2. **Empty argument and no input from `AskUserQuestion`** — halt without
   writing.
3. **Re-run on a venture with `00-vision/.archive/`** — append to the
   archive, never overwrite an archive file.
