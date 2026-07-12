---
name: prototype-feedback-collect
description: Standardised template for capturing prototype-test feedback sessions. Writes one file per session under 08-prototype/feedback/<prototype-slug>-<NNN>.md. Append-only — sessions are immutable once filed.
argument-hint: "<prototype-slug> [optional: --participant=<id>]"
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# prototype-feedback-collect

Idempotency: append-only. Session number auto-increments; once filed, a session file is immutable.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Confirm a prototype exists at
   `08-prototype/paper/<slug>.md` or `08-prototype/digital/<slug>/`.
3. Compute next session number: max existing
   `08-prototype/feedback/<slug>-*.md` + 1.

## Phase 2: Capture

Use `AskUserQuestion`:

- **Date and duration**
- **Participant** (name / pseudonym, segment fit)
- **Setup** — paper / digital / Wizard of Oz / hybrid
- **Task completion** — did they complete? Where did they get stuck?
- **What surprised them**
- **What they'd want changed**
- **Quotes** — verbatim where possible
- **Hypothesis touch-points** — for the hypothesis the prototype
  tests, did this session confirm / refute / leave ambiguous?
- **Follow-up?**

## Phase 3: Write

Write `08-prototype/feedback/<slug>-<NNN>.md`:

```markdown
---
title: Feedback — <prototype> session <NNN>
slug: feedback-<slug>-<NNN>
type: feedback
status: active
owner: <venture name>
created: <date>
updated: <date>
---

# Feedback — <prototype> session <NNN>

Prototype: [<slug>](../paper/<slug>.md) (or digital)
Tests: H-NN

- Date: <YYYY-MM-DD>
- Duration: <minutes>
- Participant: <id>, <segment>, <fit>
- Setup: paper | digital | Wizard of Oz | hybrid

## Task

<the job-to-be-done they were asked to complete>

## Walkthrough

### Step-by-step observations
<bullets>

### Where they got stuck
- ...

### Surprises
- ...

## Quotes

> "<verbatim>"

## Hypothesis touch-points

| Hypothesis | Outcome | Evidence |
|---|---|---|
| H-NN | confirm | "<quote>" |

## Follow-ups

- <referrals, agreed-upon next contact, design changes proposed>
```

## Phase 4: Log

Append:
`## [<today>] prototype-feedback | <slug> session <NNN>`.

## Important principles

- **Append-only.** Once filed, never edited. Corrections are filed
  separately.
- **Hypothesis touch-points are the link.** The feedback only matters
  if it speaks to a hypothesis.
- **Quotes preserved.** Verbatim where possible.
- **Aggregation comes later.** Multiple sessions feed
  `interview-analyse`-style aggregation; this skill captures one.
