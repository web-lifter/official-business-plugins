# vpc-version — references

The validated-learning loop that motivates versioning the VPC comes from Lean Startup. See [`startups/SOURCES.md`](../../../SOURCES.md) for full citations.

## The validated-learning loop

- **Ries, Eric.** *The Lean Startup.* Crown Business, 2011.
  - The build-measure-learn loop produces *validated learning* — evidence that changes what the team believes. When that evidence materially changes the value proposition, the canvas should be re-versioned so the new state is auditable against the prior state. The prior version is never deleted; it is marked `superseded` and forward-linked.

## Why bump for substance, not for typos

A typo fix is not validated learning. The skill refuses to bump for cosmetic changes because version inflation defeats the audit-trail purpose — if every fortnight's polish produces a new version, the version numbers stop meaning anything.

The trigger for a bump is one of:

- The customer profile changed materially since the last VPC.
- A pain reliever or gain creator was added or removed.
- The fit relationship changed.
- A pivot or refine happened (per [`pivot-refine-log`](../../../venture-core/skills/pivot-refine-log/)).

## Why the diff section is mandatory

A future reader should be able to see what changed in the new version without diffing files manually. The `## Diff from v<N>` section gives the *why* alongside the *what* — without it, the version numbers carry no narrative and the audit trail is degraded.

## Append-only chronology

Like the hypothesis register and the pivot/refine log, the VPC chronology is append-only. The discipline is consistent across the venture wiki: a venture's history is part of what makes its current state credible, and erasing history erases credibility.
