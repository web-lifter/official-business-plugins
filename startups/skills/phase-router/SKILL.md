---
name: phase-router
description: Recommend the next 1–3 actions for the venture based on its current state. Reads the index, hypothesis register, learning cards, and open questions. Outputs a prioritised plan with the skill name to invoke for each action. Read-only.
argument-hint: [optional focus area: discovery|vpc|bmc|competitor|channels|prototype|mvp]
allowed-tools: Read Glob Grep Bash
effort: medium
---

# phase-router

Idempotency: read-only. Running this skill multiple times against unchanged state produces identical recommendations.

Decides what to do next. Encodes Steve Blank's four-step customer-development model (discovery → validation → creation → company building) as a set of inspectable rules in `reference.md` so the routing is auditable, not buried in a prompt. See `startups/SOURCES.md` for citations.

## User Context

$ARGUMENTS

If `$ARGUMENTS` names a focus area, restrict recommendations to that
area; otherwise produce a venture-wide priority list of the next 1-3
actions.

---

## Phase 1: Read the venture state

**Objective:** Understand where we are.

1. Confirm a venture profile is active (same check as `venture-status`).
2. Read these in parallel:
   - `.memex/index.md` head (first 80 lines)
   - `.memex/log.md` tail (last 20 entries)
   - `01-hypotheses/hypothesis-register.md`
   - All filenames under `02-customer-discovery/segments/*/interviews/`
   - All filenames under `02-customer-discovery/{test-cards,learning-cards}/`
   - `07-validation/pivot-refine-log.md` (count of pivots in last 90 days)
   - All filenames in `.memex/.open-questions/` (excluding `README.md`)

---

## Phase 2: Apply the routing rules

**Objective:** Match state to Blank's customer-development loop.

The decision rules live in `reference.md`. Summary:

1. **No vision** → recommend `/vision-sketch`.
2. **Vision but no segments** → recommend `/customer-segment-define`.
3. **Segment defined, < 5 interviews** → recommend
   `/interview-guide-build` (if no guide) or `/interview-log` (if guide
   exists).
4. **≥ 5 interviews per segment, no analysis** → recommend
   `/interview-analyse`.
5. **Customer profile exists, no VPC** → recommend `/value-map-build`.
6. **VPC exists, no fit check** → recommend `/vpc-fit-check`.
7. **No BMC** → recommend `/bmc-build`.
8. **BMC has unflipped hypotheses** → recommend `/test-card-build` for
   the highest-priority hypothesis (use the experimentation plugin's
   `experiment-prioritise` if available).
9. **Open test cards with no learning cards** → recommend
   `/learning-card-build`.
10. **No UVP, ≥ 3 competitors** → recommend `/uvp-statement`.
11. **No channel strategy, BMC channels cell is `hypothesis`** →
    recommend `/channel-select`.
12. **Three or more pivots in last 90 days** → flag instability, suggest
    pausing solution work and revisiting `/customer-discovery-status`.
13. **Customer-discovery-status returns 🟢** → recommend `/mvp-scope` if
    no MVP scope exists.
14. **Mvp-spec exists but no architecture / schema / deploy plan** →
    recommend the matching `/mvp-tech-plan`, `/mvp-schema-plan`,
    `/mvp-deploy-plan`.

When multiple rules match, prioritise by customer-development phase order (lower phase number first), then by the count of *blocked downstream* skills.

---

## Phase 3: Render

**Objective:** Present 1-3 prioritised next actions.

For each recommended action, print:

- **Action**: the skill to invoke (with arguments where obvious).
- **Why**: 1-2 sentences citing what the venture state shows.
- **Evidence**: file paths the recommendation is grounded in.
- **Skips**: any blocking gates this action would bypass (e.g.
  "skipping `customer-discovery-status` would set off
  `prototype-vs-mvp-distinguish` later").

End with one line of metadata: which routing rule(s) matched.

---

## Important principles

- **Decision rules are explicit.** The full table lives in
  `reference.md`. No "the model decides" — every recommendation cites a
  rule number.
- **Read-only.** Never modify state; never append to log.
- **At most three recommendations.** A founder with 12 next-actions has
  no next action.
- **Cite the research.** Each rule references the relevant section of `reference.md` and the underlying source in `startups/SOURCES.md`.
- **Don't override blocking gates.** If `customer-discovery-status` is
  RED, don't recommend `/mvp-scope` even if `--force` would unblock it.
  Recommend the gap-filling action instead.

## Edge cases

1. **Brand-new venture** — recommend `/vision-sketch` and stop.
2. **Multiple segments at different phases** — pick the segment with the
   most interviews and route on that one; mention the others in the
   "also" line.
3. **`$ARGUMENTS` names an unknown focus area** — list valid areas,
   produce a venture-wide plan, and continue.
4. **Hypothesis register has rows but they all lack falsifiers** —
   recommend `/hypothesis-falsifiability-check` first; nothing else
   downstream is meaningful.
5. **Three pivots in 90 days** — explicitly recommend slowing down. The
   point of routing is sometimes "stop adding things; revisit
   discovery."
