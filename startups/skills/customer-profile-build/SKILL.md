---
name: customer-profile-build
description: Build the right half of the Value Proposition Canvas for one segment — customer jobs, pains, gains. Each item tagged functional/social/emotional and prioritised high/medium/low. Updates segments/<slug>/profile.md.
argument-hint: <segment-slug>
allowed-tools: Read Write Edit Bash Glob
effort: medium
---

# customer-profile-build

Idempotency: re-running on the same segment refreshes the table in place; pass `--archive` to keep the prior version as `profile.md.archive-<YYYY-MM-DD>`.

Method: the customer profile (right half of the Value Proposition Canvas) per Osterwalder et al., *Value Proposition Design* (Wiley, 2014). Jobs are tagged functional/social/emotional per Christensen's jobs-to-be-done lens (*Competing Against Luck*). See `references.md` and `startups/SOURCES.md`.

This skill produces the right side of the VPC. The left side
(products/services, pain relievers, gain creators) is built later by
`value-proposition/value-map-build`.

## User Context

$ARGUMENTS

`<segment-slug>` is required.

---

## Phase 1: Pre-flight

1. Verify the venture profile.
2. Verify `02-customer-discovery/segments/<slug>/` exists (run
   `customer-segment-define` first if not).
3. Read `02-customer-discovery/segments/<slug>/README.md` for the
   segment definition and `00-vision/vision-sketch.md` for the
   pre-existing problem statements. Pre-fill candidate jobs/pains/gains
   from these where possible.

---

## Phase 2: Elicit jobs, pains, gains

**Objective:** Produce specific, prioritised items in three categories.

For each of the three categories, use `AskUserQuestion` to gather 3-7
items:

### Jobs

The tasks the customer is trying to get done. Tag each as:

- **functional** — a specific outcome (reconcile invoices, find a
  supplier, post a job ad)
- **social** — how they want to be perceived (look professional, fit in
  with peers, gain status)
- **emotional** — how they want to feel (confident, in control, not
  guilty)

### Pains

Obstacles, undesired outcomes, risks, costs, frustrations. Tag each as:

- **functional** — friction in the task itself
- **social** — embarrassment, loss of face
- **emotional** — anxiety, frustration, shame

### Gains

Required, expected, desired, unexpected outcomes the customer would
appreciate. Use the four sub-types:

- **required** — without this, the solution doesn't work
- **expected** — basic features customers anticipate
- **desired** — what they'd ask for if asked
- **unexpected** — beyond what they'd think to request

For each item across all three sections, prioritise **high / medium /
low**. The skill refuses to accept a profile where every item is
"high" — force prioritisation.

---

## Phase 3: Write the profile

**Objective:** Persist to `profile.md` with the structured table.

Replace the contents of
`02-customer-discovery/segments/<slug>/profile.md` (preserving its
frontmatter, bumping `updated:`):

```markdown
---
<existing frontmatter, updated bumped>
type: profile
status: active        # was draft until first run
---

# Customer profile — <segment label>

## Jobs

| Job | Type | Priority |
|---|---|---|
| <job statement> | functional|social|emotional | high|medium|low |

## Pains

| Pain | Type | Priority |
|---|---|---|
| <pain statement> | functional|social|emotional | high|medium|low |

## Gains

| Gain | Type | Priority |
|---|---|---|
| <gain statement> | required|expected|desired|unexpected | high|medium|low |

## Sources

- Vision sketch: [vision-sketch](../../../00-vision/vision-sketch.md)
- Interviews informing this profile: <empty until interviews are logged>
```

If interviews exist for this segment, populate the Sources section
with their relative links automatically.

---

## Phase 4: Update the hypothesis register

**Objective:** Materially-prioritised pains and gains often correspond
to hypotheses worth testing. Surface them for the user.

For each `high`-priority pain or gain that does not already match an
existing hypothesis (by similarity), prompt the user:

> "This pain looks like a testable hypothesis — should we add it to the
> register? Statement: <derived from pain>. Cell: <Customer Segments or
> Value Propositions>."

If yes, append to `01-hypotheses/hypothesis-register.md` via the
`hypothesis-register` skill's add mode. The user will need to fill in
the falsifier / measurement / threshold / timeframe in a follow-up
step (the falsifiability check will prompt for these).

---

## Phase 5: Log

Append:
`## [<today>] profile | <slug> jobs/pains/gains documented`.

---

## Important principles

- **Observable items only.** "Frustrated by paperwork" is not specific
  enough; "Spends 4 hours every Friday on reconciliation" is.
- **Force prioritisation.** Reject profiles where everything is high
  priority.
- **Tag rigorously.** A "functional" pain miscategorised as "emotional"
  changes the value-map design later. The pain "I'm worried about
  fraud" is emotional even if its root cause is functional.
- **Re-runnable.** Re-running on the same segment refreshes the table;
  archive the prior to `profile.md.archive-<YYYY-MM-DD>` if the user
  passed `--archive`. Otherwise overwrite.

## Edge cases

1. **No interviews logged yet** — that's fine; the profile is the
   starting point. The first round of interviews will refine it.
2. **Segment has user / paying-customer split** — run the skill twice,
   once per sub-segment.
3. **More than 7 items in any category** — surface a warning: too many
   priorities means none. Suggest splitting the segment.
4. **All items emotional** — flag — usually indicates the user hasn't
   identified the underlying functional friction. Prompt for at least 1
   functional item per section.
