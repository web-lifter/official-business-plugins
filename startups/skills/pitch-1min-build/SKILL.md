---
name: pitch-1min-build
description: Generate a 1-minute pitch from the current BMC + UVP + MVP scope. Outputs a script (~150 words) plus a slide-skeleton outline. Suitable for pitch competitions, investor coffee chats, customer cold-opens.
argument-hint: [optional: --audience=investor|customer|partner]
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# pitch-1min-build

Idempotency: safe to re-run; each `--audience` writes a distinct file (`pitch-1min-investor.md`, `pitch-1min-customer.md`, etc.) so variants coexist.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `04-competitors/uvp.md`, latest `bmc-v*.md`,
   `09-mvp/mvp-spec.md`, primary segment profile, latest VPC.

## Phase 2: Compose script

A 1-minute pitch (≈ 150 words) has 5 beats:

1. **Problem** — who hurts and how (15s)
2. **Insight** — what we learned that others missed (10s)
3. **Solution** — what we built (15s)
4. **Traction / why now** — evidence (10s)
5. **Ask** — what we want from this conversation (10s)

Adjust beats by audience:

- **Investor**: emphasise traction and market size
- **Customer**: emphasise problem and solution; light on metrics
- **Partner**: emphasise where they fit in the model

## Phase 3: Write

Write `pitch-1min.md` in the venture root:

```markdown
---
title: 1-minute pitch
slug: pitch-1min
type: vision
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# 1-minute pitch

Audience: <investor|customer|partner>
Generated: <today>

## Script (≈150 words)

### Problem (~15s)
<2-3 sentences>

### Insight (~10s)
<1-2 sentences>

### Solution (~15s)
<2 sentences referencing UVP>

### Traction / why now (~10s)
<concrete numbers from learning cards / pre-orders / interviews>

### Ask (~10s)
<one specific request>

## Slide outline

1. Title slide — name + tagline
2. Problem — one number, one quote
3. Solution — UVP + diagram
4. Traction — three metrics
5. Ask — what we want

## Source

- UVP: [uvp](04-competitors/uvp.md)
- BMC: [latest](05-business-model/bmc-vN.md)
- MVP scope: [mvp-spec](09-mvp/mvp-spec.md)
```

## Phase 4: Log

Append: `## [<today>] pitch-1min | <audience>`.

## Important principles

- **150 words.** Hard cap.
- **One specific ask.** Not "feedback"; "would you intro me to two
  café owners?"
- **Traction is concrete.** Numbers from the venture's actual
  learning cards.
- **Re-runnable.** Audience-specific variants live as separate runs;
  use `--audience` to differentiate.
