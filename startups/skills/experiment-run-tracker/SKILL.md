---
name: experiment-run-tracker
description: Log experiment execution against an open test card — dates, who was contacted, raw data observations, current status. Distinct from interview-log (raw notes per session); this tracks the experiment as a unit. Append-only.
argument-hint: "<test-card-id> [optional: status update note]"
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# experiment-run-tracker

Append-only log of an experiment's execution against an open test card — distinct from per-interview notes. Tracks the experiment as a unit.

**Idempotency:** strictly append-only; never edits prior run-log entries. Status transitions are explicit, never silent.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Read the test card. Halt if status is `concluded` — route to
   `/learning-card-build`.

## Phase 2: Append a run-tracker entry

Use `AskUserQuestion` to gather:

1. Date of the update
2. What happened today (1-3 sentences)
3. Who was contacted / interviewed / messaged (if applicable)
4. Sample size to date
5. Status: `recruiting`, `running`, `analysis`, `paused`, `aborted`,
   or `ready-for-conclusion`

## Phase 3: Update the test card

Append a `## Run log` entry to the test card:

```markdown
## Run log

### <date>
- Status: <status>
- What happened: ...
- Sample to date: <n>
- Notes: ...
```

If `ready-for-conclusion`, surface: "Run /learning-card-build TC-<NNN>
to close."

If `aborted`, set test card status to `concluded` with a `## Aborted`
section, and recommend filing an open question for what blocked the
test.

## Phase 4: Log

Append: `## [<today>] experiment-run | TC-<NNN> <status>`.

## Important principles

- **Append-only run log.** Never edit prior entries.
- **Status transitions are explicit.** No silent moves to
  `concluded`.
- **Aborted ≠ failed.** Aborted means the test stopped; failed is a
  refutation, captured in the learning card.
