---
title: Hypothesis register
slug: hypothesis-register
type: hypothesis
status: active
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# Hypothesis register

> Canonical list of every hypothesis the venture is testing. Single
> source of truth. Other artifacts reference rows by ID; never duplicate
> the statement. Falsifier / measurement / threshold / timeframe are
> mandatory before any test card can be built.

## Conventions

- IDs are zero-padded to 2 digits (`H-01`) until > 99, then 3 digits
  (`H-100`).
- `Cell` uses the canonical 9 BMC cell names; `cross-cutting` if a
  hypothesis spans cells.
- `Status` values: `open` / `accepted` / `refuted` / `superseded` /
  `deprecated`.
- `Evidence` is a `;`-separated list of relative markdown links.

## Register

| ID | Cell | Statement | Status | Falsifier | Measurement | Threshold | Timeframe | Evidence | Updated |
|----|------|-----------|--------|-----------|-------------|-----------|-----------|----------|---------|
| H-{{NN}} | {{Cell}} | {{Statement}} | open | {{What observation refutes}} | {{Source/instrument}} | {{Pass/fail line}} | {{Decision window}} | — | {{YYYY-MM-DD}} |

## Cascade reminders

When flipping a row's status:

- `accepted` → recommend `/bmc-update H-{{NN}}` to flip the cell to `fact`.
- `refuted` → flag pages under `03-value-proposition/` and
  `05-business-model/` that cite this hypothesis as stale.
- `superseded` → link forward to the replacing ID in the row's
  `Statement` field; never delete.
