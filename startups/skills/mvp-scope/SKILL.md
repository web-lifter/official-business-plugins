---
name: mvp-scope
description: Define the smallest feature set that lets us test the *primary* hypothesis. Forces a cut/keep/maybe classification of every candidate feature. Blocking — refuses without a green customer-discovery-status (override with --force, logged).
argument-hint: [optional: --primary-hypothesis=<H-NN>]
allowed-tools: Read Write Edit Glob Grep
effort: high
---

# mvp-scope

Method: smallest-testable-feature-set discipline from Ries 2011 (*The Lean Startup*) and Maurya 2022 (*Running Lean*) — see `startups/SOURCES.md`.

Idempotency: safe to re-run; v1 stays as written. A re-run that materially changes scope writes `mvp-spec-v2.md` rather than overwriting v1.

**Blocking** — refuses unless `customer-discovery-status` returns 🟢
on the primary segment. Override with `--force`; logged.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Run `customer-discovery-status` (read-only). If not 🟢 and no
   `--force`, refuse with the gap list.
3. If `--primary-hypothesis` not given, identify the most-blocked
   open hypothesis from the register.
4. Read converged finalists from `08-prototype/converged-*.md` to
   ground feature candidates.

## Phase 2: Generate candidate features

For each top finalist, list the features it implies:

- Authentication / accounts (if needed)
- Core value-revealing flow
- Onboarding
- Data persistence
- Payments / billing (if revenue is in the hypothesis)
- Notifications / lifecycle
- Admin / observability
- Support / feedback channel

Don't assume "all of the above"; some will be `cut`.

## Phase 3: Apply cut/keep/maybe filter

For each candidate feature:

- **Keep** — needed to test the *primary* hypothesis end-to-end. If
  cut, the hypothesis can't be tested.
- **Maybe** — adjacent; useful but not strictly required. Defaults to
  cut for v1; revisit after v1 evidence.
- **Cut** — not needed to test the primary hypothesis.

Force ratios:

- ≥ 60% of candidates should be `cut` for early MVPs
- ≤ 30% `keep`
- ≤ 30% `maybe`

If the user has > 30% `keep`, push back and ask which features could
move to `maybe`.

## Phase 4: Write

Write `09-mvp/mvp-spec.md`:

```markdown
---
title: MVP scope v1
slug: mvp-spec
type: mvp-spec
status: draft
owner: <venture name>
created: <today>
updated: <today>
---

# MVP scope — v1

Primary hypothesis: [H-NN](../01-hypotheses/hypothesis-register.md)
Primary segment: [<slug>](../02-customer-discovery/segments/<slug>/README.md)
Primary value prop: from [vpc-<slug>-vN](../03-value-proposition/vpc-<slug>-vN.md)

## Cut / keep / maybe

### Keep (the MVP)
| Feature | Why it's required | Test signal |

### Maybe (post-v1 candidates)
| Feature | Why it's deferred | Trigger to revisit |

### Cut (out of MVP scope)
| Feature | Why it's cut |

## What this MVP proves (or doesn't)

- Confirms / refutes: H-NN
- Does NOT test: <list of hypotheses out of scope for v1>

## MVP type (selected via `/mvp-type-select`)

To be set by `mvp-type-select`. Pre-order, audience-building,
show-and-tell, or partial product.
```

## Phase 5: Cascade and log

1. Recommend `/mvp-type-select` next.
2. Recommend `/prototype-vs-mvp-distinguish 09-mvp/mvp-spec.md` once
   `mvp-type-select` lands.
3. Append log: `## [<today>] mvp-scope | v1 (<keep-count> keep,
   <maybe-count> maybe, <cut-count> cut)`.

## Important principles

- **Primary hypothesis only.** Secondary hypotheses get tested in
  later versions.
- **Defaults are aggressive cut.** Founder optimism inflates `keep`
  counts; force trade-offs.
- **What it does NOT prove is required.** Honest about scope.
- **Re-runnable.** v1 stays; v2 is a new version when the team
  decides to expand.

## Edge cases

1. Multiple hypotheses with similar priority — pick one as primary;
   others move to next-version.
2. Founder insists "we have to ship X feature" — push back; if
   they refuse, log the override and accept.
3. No converged finalists — refuse; route to `/converge-ideas`.
