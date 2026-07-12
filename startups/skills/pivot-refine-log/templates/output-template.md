---
title: Pivot/refine log
slug: pivot-refine-log
type: rule
status: active
owner: {{venture-slug}}
created: {{created-date}}
updated: {{today}}
---

# Pivot/refine log — {{venture-name}}

Append-only. Every pivot or refine decision is logged here with the canonical entry shape. Entries are never edited after the fact.

---

## [{{today}}] {{pivot|refine}} | {{one-line summary}}

### Trigger evidence

{{What happened? Links to interviews, learning cards, metrics, or external events. Use relative markdown paths.}}

### Decision

{{What are we doing differently? Be specific.}}

### What changed

- {{cell / page / hypothesis / VPC section updated}} — {{link}}
- {{...}}

### What was kept

- {{model elements that survive — segment, channel, team, brand, etc.}}
- {{...}}

### New version pointers

- BMC: {{link to bmc-v<N>.md or "n/a"}}
- VPC(s): {{links to vpc-<segment>-v<N>.md, one per segment affected}}
- Hypothesis register: {{list of hypothesis IDs whose status changed}}

---

## [{{prior-date}}] {{pivot|refine}} | {{prior summary}}

{{... earlier entries below ...}}
