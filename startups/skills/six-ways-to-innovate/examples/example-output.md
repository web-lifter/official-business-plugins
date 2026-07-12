---
title: Six ways candidates — AU/NZ mid-market in-house counsel
slug: six-ways-au-midmarket-inhouse-counsel-2026-05-21
type: vpc
status: draft
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# Six ways candidates — AU/NZ mid-market in-house counsel

Each item below is a *candidate* — a hypothesis worth considering, not a fact. Generated against [`profile.md`](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/profile.md) and [`vpc-au-midmarket-inhouse-counsel-v1.md`](vpc-au-midmarket-inhouse-counsel-v1.md). Deduplicated against the current hypothesis register.

## 1. Customer needs

- **Adjacent need: NDA-only review mode.** 3/7 interviewees mentioned NDAs as a separate, higher-volume workflow than MSAs. A simpler, lighter NDA-only mode might unlock weekly use even when MSA volume is low.
- **Adjacent need: employment contract review.** 2/7 mentioned "the same problems exist for employment contracts but the corpus is totally different". Worth probing whether a sister classifier is in-scope for v2.

## 2. Value (price, performance, customisation)

- **Performance trade-off: synchronous vs batch.** Sub-60-second classifier latency is engineering-expensive. A "batch overnight" mode at half the price might fit asynchronous reviewers and reduce infrastructure cost.
- **Price: per-contract vs per-seat.** Some interviewees process few high-value contracts; per-contract pricing could capture buyers who don't think in "seats".

## 3. The product itself

- **Form factor: MS Word add-in.** 2/7 strongly preferred a Word add-in over a web app (Spellbook frame). Adding a Word add-in alongside the web app may unlock buyers we lose to Spellbook.
- **Depth: just-the-flags vs full-redline.** A "flags only, you redline" tier at lower price might match counsel who don't trust automated redlines yet.

## 4. The experience (onboarding, packaging, brand)

- **Onboarding: "run it on your last 6 MSAs".** P3 articulated the trust threshold explicitly. An onboarding flow that runs the classifier over a customer-supplied back-catalogue and presents a side-by-side ("we caught what you caught, plus these you didn't") may collapse evaluation time from weeks to a single session.
- **Brand: AU/NZ-first positioning.** Lean into the AU/NZ specificity hard — the audit-defensible PPSA/Privacy/Modern-Slavery story is a wedge against Spellbook that we under-state today.

## 5. The relationship (self-serve, concierge, community)

- **Concierge for first 10 customers.** Founder-led design-partner relationship (Priya runs onboarding personally for the first cohort) may compress the evidence collection needed to clear `customer-discovery-status` Q4.
- **Community: ACC Australia mid-market chat.** P3 offered to post in this chat. A modest community presence (monthly clause-trap newsletter) may produce a higher-quality inbound channel than LinkedIn outbound.

## 6. The channel (direct, indirect, partner)

- **Partner: AU mid-market law firms doing fractional GC work.** Several mid-market firms supply fractional in-house counsel to companies in our band; partnering rather than competing may unlock distribution.
- **Partner: AU corporate-secretary platforms (e.g. BoardPro).** Adjacent buyer; obligation tracking is also their problem. Worth a 60-minute conversation.

## To register

For each candidate the user wants to test:

- Convert to a hypothesis via `/hypothesis-register add` — supply falsifier, measurement, threshold, timeframe.

### Suggested first three to test (Priya's pick)

1. **Word add-in form factor (lens 3)** — falsify by offering a Word-add-in beta and measuring conversion vs the web app at parity feature set.
2. **"Run it on your last 6 MSAs" onboarding (lens 4)** — falsify by A/B-ing the back-catalogue onboarding against a fresh-contract demo and measuring time-to-trust.
3. **Mid-market law firm partner channel (lens 6)** — falsify by booking 3 mid-market AU firm conversations and measuring whether any commit to a co-promotion arrangement within 60 days.
