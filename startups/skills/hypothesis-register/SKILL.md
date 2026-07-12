---
name: hypothesis-register
description: Maintain the canonical list of venture hypotheses — id, BMC cell, statement, status (open/accepted/refuted/superseded), falsifier, measurement, threshold, timeframe, evidence. Add, update, flip status. Single source of truth for what we believe.
argument-hint: "[add|update|flip] [hypothesis-id-or-slug]"
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# hypothesis-register

Idempotency: `add` and `update` modes are deterministic on identical inputs. `flip` writes one row change plus one log entry per invocation.

Method: hypothesis-status conventions from Blank (`open` / `accepted` / `refuted` / `superseded`) and Maurya's *Running Lean* hypothesis tracking. See `references.md` and `startups/SOURCES.md`.

The hypothesis register is the venture's master list of every guess
we're testing. Every test card references it; every learning card
flips a row's status; every BMC version reflects the current snapshot.

## User Context

$ARGUMENTS

Modes:

- `add` — append a new hypothesis (default if `$ARGUMENTS` is empty or a
  free-form statement)
- `update` — edit an existing hypothesis's statement, falsifier,
  measurement, threshold, timeframe, or owner
- `flip` — change a hypothesis's status (`open` → `accepted` /
  `refuted` / `superseded`)

---

## Phase 1: Confirm and read

**Objective:** Don't run on the wrong directory; load the current
register.

1. Verify the venture profile (same check as `venture-status`).
2. Read `01-hypotheses/hypothesis-register.md`. If missing, scaffold it
   with the table header and a frontmatter block. (`venture-init` does
   this; this skill is also tolerant.)

---

## Phase 2: Branch on mode

### 2a — Add

1. If `$ARGUMENTS` contains a free-form statement, use it as the
   hypothesis statement; otherwise prompt via `AskUserQuestion`.
2. Use `AskUserQuestion` to gather:
   - **BMC cell** (one of the 9 — pick from a list)
   - **Falsifier** ("we are wrong if ...")
   - **Measurement** (where the data comes from)
   - **Threshold** (pass / fail line)
   - **Timeframe** (when we decide)
3. Validate the statement via the falsifiability heuristic in
   `reference.md` §1. If any of falsifier / measurement / threshold /
   timeframe is missing or vague, refuse and offer to call
   `/hypothesis-falsifiability-check`.
4. Compute the next `H-<NN>` ID by scanning the register.
5. Append a row to the table with `status: open`, today's `updated:`
   date, empty `evidence:`.
6. Bump the row's `status` field in the page-level frontmatter is *not*
   needed — the register itself is one document; per-row status lives in
   the table. (See note in `reference.md` §2.)

### 2b — Update

1. `$ARGUMENTS` must contain a hypothesis ID or slug; if not, list all
   hypotheses and prompt.
2. Use `Edit` (not `Write`) to modify only the matching row. Refuse if
   the change would erase evidence — preserve audit trail.
3. Bump `updated:` on the modified row.

### 2c — Flip

1. `$ARGUMENTS` must contain `<id> <new-status>` (e.g. `H-03 accepted`).
2. Validate the new status is in the enum.
3. Validate that the user has linked at least one piece of evidence
   (interview, learning card, external) — if none, prompt for a link
   before flipping.
4. Use `Edit` to change the row's `status` and `updated`. Append a line
   to the row's `evidence:` field with the supplied link.
5. **Cascade.** When a flip happens:
   - Append an entry to `.memex/log.md`:
     `## [<today>] hypothesis-flip | H-<NN> <old> → <new>`
   - Surface to the user: "BMC update needed — recommend running
     `/bmc-update H-<NN>` to bump to v(N+1)"
   - If the new status is `refuted` or `superseded` and there are pages
     under `03-value-proposition/` or `05-business-model/` that cite
     this hypothesis, list them so the user knows what's now stale.
   - The actual stale-page detection delegates to memex's
     `stop-stale-check.py` hook on session end.

---

## Phase 3: Write back and log

**Objective:** Persist the register and chronicle the change.

1. Write the updated register file.
2. Append a log entry per the entry shape above.
3. Print a short success message stating the operation, the hypothesis
   ID, and the current status.

---

## Important principles

- **Single source of truth.** Every other artifact references this
  register by ID. Do not duplicate hypothesis statements in the BMC, the
  VPC, the test cards, or anywhere else — link.
- **Never delete.** Set status to `deprecated` or `superseded` and link
  forward. The chronology matters.
- **Falsifier is mandatory.** A hypothesis without a falsifier is a
  belief, not a hypothesis. Refuse to add it.
- **Evidence required for flips.** A status change without evidence is a
  guess. Refuse to flip without a linked artifact.
- **Re-entrant.** Adding the same hypothesis twice should detect the
  duplicate (by statement similarity) and offer to merge or leave both.

## Edge cases

1. **Duplicate hypothesis statement** — detect by Levenshtein distance
   on the normalised statement; if > 80% similar, ask the user.
2. **Flip without an attached learning card** — strongly discouraged but
   allowed if the user supplies an external citation (research paper,
   public dataset). Log the deviation.
3. **Pivot in progress** — when `pivot-refine-log` is being written
   simultaneously, append the hypothesis flips to the pivot entry's
   "What changed" section automatically.
4. **Register file > 500 rows** — we're not optimising for that yet.
   Performance is fine; readability isn't. Surface a warning at 100
   rows: consider splitting by phase.
