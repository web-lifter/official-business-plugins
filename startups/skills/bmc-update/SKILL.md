---
name: bmc-update
description: Apply changes from the hypothesis register to the BMC — when a hypothesis flips to accepted/refuted, update the relevant cell and bump to v(N+1). Tracks the diff in a changelog. Marks the prior version superseded.
argument-hint: [optional: hypothesis-id-or-comma-list]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# bmc-update

Applies hypothesis-register flips to the BMC, bumping it to v(N+1). The "BMC as hypothesis sheet" pattern (Osterwalder & Pigneur, *Business Model Generation*, 2010) is the underlying discipline. See `references.md`.

**Idempotency:** a second run with no further flips since the last version is a no-op.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Find the latest BMC. Halt if none — route to `/bmc-build`.
3. Read hypothesis register; find hypotheses whose `Updated` date is
   newer than the latest BMC's `updated` and whose status is
   `accepted` or `refuted`. Optional `$ARGUMENTS` filters to specific
   IDs.
4. If nothing has flipped since the last version, halt with a no-op
   message.

## Phase 2: Compute cell changes

For each flipped hypothesis:

- Look up its BMC cell (from the hypothesis register's `Cell` column).
- Determine the change:
  - `accepted` → cell entry tag flips from `hypothesis` to `fact`;
    add evidence link
  - `refuted` → cell entry is removed (or re-stated as a different
    hypothesis if the user has a replacement)

If the flip is a refutation that invalidates a whole cell entry, ask
the user via `AskUserQuestion`: "Replace with new entry, leave empty,
or keep with note?"

## Phase 3: Write the new version

1. Copy the prior BMC verbatim to a new file `bmc-v<N+1>.md`.
2. Apply the cell changes.
3. Add a `## Changelog` section listing what changed and the
   hypothesis IDs that drove the change.
4. Mark the prior BMC `status: superseded` and add a forward link.
5. Bump frontmatter `updated:` on both files.

## Phase 4: Cascade

Surface to the user:

- Pages that cite the prior BMC — typically VPCs, channel strategy,
  pivot/refine log entries. Recommend running the relevant
  `version` skill on each.
- If a pivot is implied by the changes (≥ 2 cells touched), recommend
  `/pivot-refine-log pivot`.

## Phase 5: Log

Append:
`## [<today>] bmc-update | v<N> → v<N+1> (<flips list>)`.

## Important principles

- **Every cell change traces to a hypothesis ID.** No silent edits.
- **`fact` requires evidence link.** No bare assertions.
- **Major changes (≥ 2 cells, or any segment change) imply a pivot.**
  Surface the pivot-refine-log recommendation; don't auto-log.
- **Re-runnable.** A second run after no further flips is a no-op.

## Edge cases

1. Hypothesis flipped but its `Cell` is "cross-cutting" — surface for
   user to map to a cell explicitly before updating.
2. Cell becomes empty after refutation — leave empty with a note;
   don't delete the cell.
3. Concurrent flips imply contradictory updates — refuse; ask the user
   to resolve in the register first.
