---
name: vpc-version
description: Snapshot the current VPC and bump to v(N+1) as customer feedback refines it. Tracks the diff so the evolution story is auditable. Sets the prior version's status to superseded.
argument-hint: "<segment-slug> [optional: rationale]"
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# vpc-version

Idempotency: bumps the VPC by exactly one version per invocation; refuses if `v<N+1>` already exists. The prior version's `status:` is set to `superseded` and a forward link is added.

Method: Lean Startup validated-learning loop — each turn of build-measure-learn that materially changes the canvas warrants a new versioned snapshot, with the prior version kept as audit trail (Ries, *The Lean Startup*, 2011). See `references.md` and `startups/SOURCES.md`.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Find the latest `03-value-proposition/vpc-<slug>-v*.md`. Halt if
   none exists — route to `value-map-build` first.

## Phase 2: Confirm the bump is warranted

A new VPC version is required when:

- The customer profile changed materially since the last VPC
- A pain reliever / gain creator was added or removed
- The fit relationship changed
- A pivot happened (per `pivot-refine-log`)

Read `02-customer-discovery/segments/<slug>/profile.md` and
`07-validation/pivot-refine-log.md`. If none of the above is true,
warn the user that no bump is needed and confirm.

## Phase 3: Snapshot

1. Copy the previous VPC's content to v(N+1) verbatim.
2. Mark v<N> frontmatter `status: superseded` and add a forward link
   in its `Notes` section.
3. Edit the v<N+1> content to reflect the changes (the user supplies
   the rationale and the specific edits via `AskUserQuestion`).
4. Add a `## Diff from v<N>` section to v<N+1> listing what changed.

## Phase 4: Run fit-check

Auto-invoke `vpc-fit-check` on the new version to compute the new
fit status.

## Phase 5: Log

Append: `## [<today>] vpc-version | <slug> v<N> → v<N+1> (<rationale>)`.

## Important principles

- **Never delete v<N>.** Mark superseded. The chronology is the
  audit trail.
- **Bump for substance, not for typos.** A typo fix doesn't merit a
  new version.
- **Diff section is mandatory.** Future reads should be able to see
  what changed without diffing files manually.

## Edge cases

1. No prior VPC — refuse; route to `value-map-build`.
2. Multiple pivots in same week — one vpc-version per pivot, not one
   batch.
3. v<N+1> already exists — refuse; the user must clean up before
   bumping again.
