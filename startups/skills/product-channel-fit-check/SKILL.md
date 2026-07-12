---
name: product-channel-fit-check
description: Ensure the product type and chosen channel are coherent — SaaS sold via retail is incoherent; mass-market consumer good sold by inside sales is incoherent. Outputs a fit verdict per primary channel.
argument-hint: [no args]
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# product-channel-fit-check

Methodology: product-channel coherence matrix derived from David Skok's SaaS distribution heuristics and the BMC channels cell (Osterwalder & Pigneur, 2010). The matrix lives in `reference.md` §1.

Idempotency: re-running appends a fresh `## Fit report` section to `channel-strategy.md` (dated); prior fit reports are preserved.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `06-relationships-channels/channel-strategy.md`. Halt if
   missing — route to `/channel-select`.
3. Read latest BMC's value-propositions cell to determine product
   type.

## Phase 2: Apply the fit matrix

Match product type to channel type. The matrix is in
`reference.md` §1; the gist:

- **Self-serve SaaS** ↔ direct web, content marketing, freemium
  funnel; ✗ retail, traditional sales
- **Enterprise SaaS** ↔ inside sales, partners, conferences; ✗
  freemium, app store
- **Consumer mobile** ↔ app store, paid social, virality; ✗ inside
  sales
- **Physical product** ↔ direct e-commerce, retail, marketplaces; ✗
  inside sales unless luxury / B2B
- **Service / consulting** ↔ referrals, content, sales; ✗ retail

## Phase 3: Compose verdict

For each primary / secondary / tertiary channel, score:

- 🟢 Coherent — matrix supports
- 🟡 Possible but unconventional — flag what makes it work
- 🔴 Incoherent — recommend rethinking

## Phase 4: Append fit report to channel-strategy

Append a `## Fit report` section to `channel-strategy.md`:

```markdown
## Fit report

Generated <today>.

| Channel | Tier | Verdict | Rationale |
|---|---|---|---|
| <name> | primary | 🟢 | matrix row X |
| <name> | secondary | 🟡 | unconventional but ... |

### Action

- <if any 🔴 — recommend `/channel-select` re-run>
```

## Phase 5: Log

Append: `## [<today>] product-channel-fit | primary <verdict>`.

## Important principles

- **Matrix is explicit.** No hand-waving.
- **🟡 verdicts allowed.** Unconventional channel-product pairs are
  sometimes the wedge — capture *why* it's unconventional.
- **🔴 blocks downstream.** A 🔴 primary channel is a planning bug;
  surface loudly.

## Edge cases

1. Multi-product venture — check fit per product, not aggregated.
2. Pivot just changed the product type — fit-check is now urgent;
   prior verdicts are stale.
