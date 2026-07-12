---
name: adr-writer
description: Write an Architecture Decision Record using the standard template — context, decision, consequences, alternatives, status. Used by every other planning skill that lands a decision. Writes 09-mvp/architecture/ADR-NNN-<slug>.md.
argument-hint: "<decision-title> [optional: --status=accepted|proposed|deprecated]"
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# adr-writer

Method: Nygard 2011 ADR template (status / context / decision / consequences / alternatives). See `references.md` and `startups/SOURCES.md`.

Idempotency: safe to re-run; each call writes a new ADR with the next sequence number. Existing ADRs are never overwritten — supersede with a new ADR linking back.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Compute next ADR number: max existing
   `09-mvp/architecture/ADR-*.md` + 1.
3. Slugify the decision title.

## Phase 2: Compose ADR

Use `AskUserQuestion` to gather:

1. **Context** — what's the situation that prompted this decision?
2. **Decision** — what was decided?
3. **Consequences** — what does this make easier? Harder? What's the
   trade-off?
4. **Alternatives considered** — at least 2; note why each lost.
5. **Status** — `proposed` (pre-decision) | `accepted` (committed) |
   `deprecated` (no longer applies) | `superseded by ADR-NNN`.

## Phase 3: Write

Write `09-mvp/architecture/ADR-<NNN>-<slug>.md`:

```markdown
---
title: ADR-<NNN> — <title>
slug: ADR-<NNN>-<slug>
type: adr
status: <status>
owner: <venture name>
created: <today>
updated: <today>
---

# ADR-<NNN> — <title>

## Context

<what's the situation>

## Decision

<what was decided>

## Consequences

### Positive
- ...

### Negative
- ...

### Neutral
- ...

## Alternatives considered

### Alternative 1: <name>
- Why we didn't pick it: ...

### Alternative 2: <name>
- Why we didn't pick it: ...

## Status

`<status>` as of <today>.

## Linked

- Tech stack: [tech-stack](../tech-stack.md)
- MVP spec: [mvp-spec](../mvp-spec.md)
- Related ADRs: <links>
```

## Phase 4: Log

Append: `## [<today>] adr | ADR-<NNN> <title>`.

## Important principles

- **Standard template.** Don't innovate.
- **Alternatives are mandatory.** ≥ 2.
- **Consequences are honest.** Include the negatives.
- **Supersede, don't delete.** Old ADRs get `status: superseded`,
  forward link.
- **Re-runnable.** Each call writes a new ADR.
