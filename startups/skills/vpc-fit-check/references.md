# vpc-fit-check — references

The fit check this skill performs comes from Strategyzer's Value Proposition Canvas. See [`startups/SOURCES.md`](../../../SOURCES.md) for full citations.

## What "fit" means

- **Osterwalder, Alexander; Pigneur, Yves; Bernarda, Greg; Smith, Alan.** *Value Proposition Design.* Wiley, 2014.
  - Fit is the alignment between the value map (left half) and the customer profile (right half) — every prioritised pain has at least one pain reliever; every prioritised gain has at least one gain creator. Strategyzer treats fit as a *necessary condition*, not a sufficient one — a fitted canvas can still fail in the market — but a canvas without fit cannot.

## The high-priority rule

A single unmatched `high`-priority pain or gain blocks fit. This is non-negotiable: high-priority items are the ones the segment cares most about, and a value proposition that does not address them is targeting the wrong segment or is missing a critical element.

## The 70% medium-priority rule

Medium-priority items can be partial. The 70% threshold reflects the trade-off Strategyzer recommends: a canvas that addresses every medium item is over-engineered (and likely cannot be built in a reasonable MVP); a canvas that addresses fewer than 70% is under-cooked.

## Why this skill is read-only on the segment profile

The fit check never modifies jobs/pains/gains — it audits the relievers/creators against them. If the audit reveals that a `medium`-priority pain has no reliever and the team chooses not to add one, the fix is to drop the pain's priority (in `customer-profile-build`) with explicit interview evidence — not to silently delete it. The separation prevents wishful re-prioritisation.
