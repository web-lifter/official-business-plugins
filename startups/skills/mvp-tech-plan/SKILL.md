---
name: mvp-tech-plan
description: Translate the MVP scope into a tech plan — sequenced delegation to tech-stack-recommender → architecture-design → adr-writer. Thin orchestrator. Outputs reside under 09-mvp/.
argument-hint: [optional: --override-stack=<keyword>]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# mvp-tech-plan

Thin orchestrator over the engineering-bridge skills.

Idempotency: safe to re-run; sub-skills (`/tech-stack-recommender`, `/architecture-design`, `/adr-writer`) each handle their own re-entry semantics. ADRs are append-only.

Delegation chain: `/tech-stack-recommender` → `/architecture-design` → `/adr-writer "tech stack decision"`.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Read `mvp-spec.md`. Halt if missing.
3. Check whether `tech-stack.md` exists; if recent (< 7 days) and no
   override, ask user whether to refresh.

## Phase 2: Sequenced delegation

1. **`/tech-stack-recommender`** (with `--override` if passed) →
   produces `09-mvp/tech-stack.md`.
2. **`/architecture-design`** → produces
   `09-mvp/architecture/architecture-overview.md` plus Mermaid
   diagrams.
3. **`/adr-writer "tech stack decision"`** → produces
   `09-mvp/architecture/ADR-NNN-tech-stack.md`.

After each, read the output, confirm it's well-formed, before
proceeding.

## Phase 3: Cross-check

After the three sub-skills complete:

- Confirm `tech-stack.md` and the architecture overview agree on the
  components.
- Confirm the ADR cites both files.
- Append a summary block to chat: "Tech plan complete:
  - Stack: <name>
  - Architecture: <link>
  - ADR: ADR-NNN
  Next: `/mvp-schema-plan`."

## Phase 4: Log

Append: `## [<today>] mvp-tech-plan | stack <name>`.

## Important principles

- **Thin.** This skill delegates; it doesn't duplicate logic from the
  sub-skills.
- **Re-runnable.** Each sub-skill is re-entrant; the orchestrator can
  re-run safely.
- **Cross-check matters.** Sub-skills run in sequence; the outputs
  must agree.
