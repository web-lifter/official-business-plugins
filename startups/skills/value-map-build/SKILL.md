---
name: value-map-build
description: Build the left half of the VPC for one segment — products & services, pain relievers, gain creators. Maps each reliever to a prioritised pain and each creator to a prioritised gain. Writes 03-value-proposition/vpc-<segment>-vN.md.
argument-hint: "<segment-slug> [optional: --version=N]"
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# value-map-build

Idempotency: each run produces `vpc-<segment>-v<N>.md` where N is `(latest + 1)` unless `--version=N` overrides. Re-running with an existing version refuses unless overridden.

Method: the value-map half of the Value Proposition Canvas — products & services, pain relievers, gain creators — per Osterwalder, Pigneur, Bernarda & Smith, *Value Proposition Design* (Wiley, 2014). See `references.md` and `startups/SOURCES.md`.

## User Context

$ARGUMENTS

`<segment-slug>` is required.

## Phase 1: Pre-flight

1. Verify the venture profile.
2. Verify `02-customer-discovery/segments/<slug>/profile.md` exists with
   `status: active`. Refuse if profile is `draft` — the right half
   of the VPC must be sharp before designing the left half.
3. Find the existing VPC version for this segment, if any. Default
   target version is `(latest + 1)` unless `--version=N` is passed.

## Phase 2: Elicit the value map

Use `AskUserQuestion`:

1. **Products & services** — what are we offering? List concrete
   things (a feature, a service, a deliverable). Tag each as
   `physical | digital | service | financial`.
2. **Pain relievers** — for each prioritised pain on the segment's
   profile, what specifically reduces or removes it? Reject "we make
   it easy" — require an observable mechanism ("auto-reconciles
   transactions from the bank feed in real time").
3. **Gain creators** — for each prioritised gain, what specifically
   produces it?

Each pain reliever must reference at least one pain ID. Each gain
creator must reference at least one gain ID. Surface unmatched items.

## Phase 3: Write the VPC

Write `03-value-proposition/vpc-<segment>-vN.md`:

```markdown
---
title: VPC — <segment label> v<N>
slug: vpc-<segment>-v<N>
type: vpc
status: draft
owner: <venture name>
created: <today>
updated: <today>
---

# Value Proposition Canvas — <segment label> v<N>

Source segment: [<segment>](../02-customer-discovery/segments/<slug>/README.md)
Source profile: [profile.md](../02-customer-discovery/segments/<slug>/profile.md)

## Customer profile (right half)

(Imported from segment profile; not duplicated here. See profile.md.)

## Value map (left half)

### Products & services

| Product / service | Type |
|---|---|
| <name> | physical|digital|service|financial |

### Pain relievers

| Reliever | Mechanism | Maps to pain |
|---|---|---|
| <name> | <observable how> | <pain row from profile> |

### Gain creators

| Creator | Mechanism | Maps to gain |
|---|---|---|
| <name> | <observable how> | <gain row from profile> |

## Notes

- Created from <interview-summary | hypothesis update | pivot>
- Successor relationship: <link to v<N-1> if any>
```

## Phase 4: Log

Append: `## [<today>] vpc | <segment> v<N> built`.

## Important principles

- **Every pain reliever maps to a prioritised pain.** Unmapped
  relievers are vanity features.
- **Mechanisms must be observable.** "Easier" / "faster" / "better"
  are not mechanisms.
- **VPC is per-segment.** Multi-segment ventures have one VPC per
  segment.
- **Re-runnable.** Increments the version number on each run unless
  `--version=N` overrides.

## Edge cases

1. Multiple high-priority pains with no candidate reliever — list as
   open questions.
2. Pain is reliever-rich but the gain side is empty — fine; product is
   pain-driven.
3. Re-run after a pivot — bump version; old version stays as
   `superseded`.
