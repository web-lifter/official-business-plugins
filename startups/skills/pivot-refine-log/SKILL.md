---
name: pivot-refine-log
description: Append a pivot or refine entry to 07-validation/pivot-refine-log.md. Forces the canonical entry shape — trigger evidence, decision, what changed, what was kept, new version pointers. Surfaces stale pages that need follow-up.
argument-hint: "[pivot|refine] [one-line summary]"
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# pivot-refine-log

Idempotency: append-only. Each invocation produces a new dated entry; existing entries are never modified.

Records every pivot or refine decision so the customer-development loop
is auditable. Append-only — entries never get edited after the fact.

Method: Steve Blank's verify / pivot / refine discipline from the customer-development model (*The Four Steps to the Epiphany*; *The Startup Owner's Manual*). See `startups/SOURCES.md`.

## User Context

$ARGUMENTS

`$ARGUMENTS` should contain `pivot` or `refine` followed by a one-line
summary. If absent, prompt via `AskUserQuestion`.

---

## Phase 1: Confirm and check

**Objective:** Validate the entry type and confirm we have something
substantive to log.

1. Verify the venture profile.
2. Verify the user explicitly chose `pivot` or `refine`. If they're not
   sure, surface the rule from
   `claude-memex/templates/profiles/venture/.memex/.rules/pivot-refine-rules.md`:
   pivot = change a core element of the model, keep another. Refine =
   tweak the same model. If they can't tell, it's almost certainly a
   refine.
3. Look at the last 90 days of `pivot-refine-log.md` entries:
   - If this would be the **third pivot in 90 days**, warn the user
     before logging. Three pivots in a quarter is an instability signal
     — the rule says slow down on solution work, revisit discovery.
     Logging is still allowed; the warning is informational.

---

## Phase 2: Gather the entry content

**Objective:** Build the canonical entry shape.

Use `AskUserQuestion` to gather (one question per concept, or a single
multi-question block):

1. **Trigger evidence.** What happened? Link to interviews, learning
   cards, metrics, or external events. Use markdown links (relative
   paths inside the venture).
2. **Decision.** What are we doing differently? Be specific.
3. **What changed.** Cells / pages / hypotheses / VPC sections that
   were updated. Markdown links.
4. **What was kept.** Explicit list of model elements that survive.
   This is the "don't throw away learning" rule.
5. **New version pointers.** BMC version (link), VPC version(s) (link),
   hypothesis IDs whose status changed.

Refuse to proceed if "What was kept" is empty — even a major pivot
keeps something (the segment, the channel, the team, the brand). If the
user really has thrown everything away, that's a re-start, not a pivot.
Suggest archiving the venture and starting fresh.

---

## Phase 3: Append the entry

**Objective:** Write the entry in the canonical shape; never edit
existing entries.

Append to `07-validation/pivot-refine-log.md` after the last existing
entry:

```markdown
## [<today>] <pivot|refine> | <one-line summary>

### Trigger evidence
<the answer from Phase 2.1>

### Decision
<the answer from Phase 2.2>

### What changed
<the answer from Phase 2.3>

### What was kept
<the answer from Phase 2.4>

### New version pointers
- BMC: <link>
- VPC(s): <links>
- Hypothesis register: <list of hypothesis IDs>
```

Frontmatter on the file (set once, never modified):

```yaml
---
title: Pivot/refine log
slug: pivot-refine-log
type: rule
status: active
owner: <venture name>
created: <date of file creation>
updated: <today>
---
```

---

## Phase 4: Cascade

**Objective:** Surface the work this pivot/refine creates.

1. For each hypothesis ID in "New version pointers", check the register.
   If the status hasn't been updated to match the pivot, recommend
   `/hypothesis-register flip <id> <status>`.
2. For each VPC link in "New version pointers", check that a new
   `vpc-<segment>-vN.md` exists with `N` greater than the prior. If
   not, recommend `/vpc-version`.
3. For the BMC pointer, check that a new `bmc-vN.md` exists. If not,
   recommend `/bmc-update`.
4. Memex's `stop-stale-check.py` hook will catch other stale pages on
   session end.
5. Append a log entry:
   `## [<today>] pivot-refine | <pivot|refine> — <one-line summary>`.

---

## Important principles

- **Append-only.** Never edit a logged entry. If the entry is wrong,
  log a correction with a new heading.
- **What was kept is mandatory.** Empty answers are refused.
- **Three pivots in 90 days = warning.** Doesn't block; informs.
- **Evidence is required.** A pivot without a trigger is a whim. Refuse
  to log.
- **Re-entrant.** Running this skill twice with the same arguments
  produces two log entries — that's the right behaviour, since the
  user might genuinely be logging two related decisions.

## Edge cases

1. **The pivot is a re-segmentation.** Recommend adding the new segment
   first via `/customer-segment-define`, then logging the pivot with the
   new segment's path in "What changed."
2. **The user types "I'm not sure if this is a pivot or refine"** —
   show the rule, then prompt again.
3. **Major pivots that flip ≥ 5 hypotheses at once** — log normally;
   the cascade in Phase 4 will produce a long list of recommendations.
   That's fine.
4. **First entry on a fresh venture** — file has only the frontmatter
   and a header; append below the frontmatter.
