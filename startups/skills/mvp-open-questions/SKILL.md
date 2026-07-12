---
name: mvp-open-questions
description: Roll all `?`-tagged items from MVP planning files into 09-mvp/open-questions.md, plus surface them as files under .memex/.open-questions/. Pure aggregation driven by memex hooks — no novel logic.
argument-hint: [no args]
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# mvp-open-questions

Idempotency: safe to re-run; rewrites the aggregate file each time. Promoted `.open-questions/<slug>.md` files are never deleted by a re-run.

## User Context

$ARGUMENTS

## Phase 1: Scan MVP planning files

Read every file under `09-mvp/` and grep for unresolved markers:

- Lines starting with `?` or `TODO:` or `TBD:`
- Sections titled `## Open questions` or `## Risks and unknowns`
- Frontmatter `status: draft` (the artifact itself is unresolved)

## Phase 2: Group and write

Group by source file. Write `09-mvp/open-questions.md`:

```markdown
---
title: MVP open questions
slug: mvp-open-questions
type: open-question
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# MVP open questions

Aggregated from `09-mvp/` files. Each item links to its source.

## From mvp-spec.md
- ...

## From tech-stack.md
- ...

## From schema/migrations-plan.md
- ...

(... per file ...)

## Promoted to .open-questions/

The following items have been promoted to first-class open-question
files for tracking:

- [.open-questions/<slug>.md](../.memex/.open-questions/<slug>.md)
```

## Phase 3: Promote to .open-questions/

For items severe enough to track (regulatory blockers, technical
unknowns, resource constraints), create a corresponding file under
`.memex/.open-questions/<slug>.md` with the full open-question
template (per `claude-memex/templates/profiles/venture/.memex/.open-questions/README.md`).

## Phase 4: Log

Append: `## [<today>] mvp-open-questions | <N> aggregated, <M>
promoted`.

## Important principles

- **Aggregation only.** Don't invent questions; surface what's there.
- **Promote severe items.** A `?` in tech-stack might just be a
  gap; a regulatory `?` is a blocker.
- **Re-runnable.** Each run refreshes the aggregate.
- **Memex hooks handle the rest.** `index-update.py` picks up the
  new files in `.open-questions/`.
