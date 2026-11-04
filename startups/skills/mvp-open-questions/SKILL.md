---
name: mvp-open-questions
description: "Aggregate unresolved MVP planning items with source references. Refresh the report explicitly without requiring external hooks."
argument-hint: "[venture or supplied MVP files]"
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# mvp-open-questions

## Runtime preflight

Read [the runtime guide](../../RUNTIME.md) before this workflow.

## User Context

$ARGUMENTS

## Phase 1: Inspect

Resolve the venture root. Read Markdown planning files under `09-mvp/`, excluding `open-questions.md` itself and generated copies/archives. Never recursively ingest the previous aggregate. With large inputs, report the files covered and any uninspected files rather than claiming complete coverage.

Find lines beginning `?`, `TODO:` or `TBD:`, and unresolved items in `Open questions` or `Risks and unknowns` sections. A draft file is a review task, not proof that every statement is unresolved. Ignore explicitly resolved items and illustrative placeholders in templates. Capture source path, heading or line, exact question, severity and current status.

## Phase 2: Refresh the aggregate

Deduplicate by source path plus normalised question. Reconcile against the existing report so owner, decision and resolution annotations are preserved. Write `09-mvp/open-questions.md` using the [template](templates/output-template.md). Link each item to its real source relative to the output file. Do not invent questions or infer that disappearance from an input proves resolution.

## Phase 3: Promote only when useful

For material blockers, create a non-destructive `.open-questions/<slug>.md` record containing title, source, question, evidence needed, owner (or unassigned), status and review date. Preserve existing promoted records and link them from the aggregate. No external template or index-update hook is required.

## Phase 4: Report actual changes

Update index links and append a log entry only when a file changed. Report unresolved blockers and any incomplete coverage. Do not log a no-op rerun. In hosted chat, return the report and explicitly distinguish it from persisted venture state.
