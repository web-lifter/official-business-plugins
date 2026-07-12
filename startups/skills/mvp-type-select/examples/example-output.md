# MVP type — selection record for ContractIQ

(Appended to `09-mvp/mvp-spec.md` → section "MVP type". Recorded 2026-05-21.)

## Selected: **Partial product**

## Rationale

- **Primary hypothesis:** [H-002 — Usability (median redline < 25 min)](../01-hypotheses/hypothesis-register.md)
- **Hypothesis question answered:** "Will they use a thin slice?" — specifically, will a senior in-house counsel actually finish a redline using the tool, within a defensible time budget.
- **Why this type, not the others:**
  - **Not pre-order.** H-001 (demand) is secondary; pre-order tests willingness-to-pay against a marketing surface, not the workflow. Counsel will say "maybe" to a pre-order, but the H-001 falsifier needs them to anchor on a working demo.
  - **Not audience-building.** ContractIQ is not content-led; the segment is too small (a few thousand in-house counsel in AU/NZ) to support an audience funnel as the primary signal.
  - **Not show-and-tell.** A clickable mock-up wouldn't run the classifier, and H-002's whole point is the stopwatch on a real end-to-end flow.

## Concrete instantiation

A narrow but real product slice:

- Sign-in (Google Workspace + email fallback).
- Upload one `.docx` or `.pdf` (≤ 25 MB) per session.
- Classifier runs on Cloudflare Workers using the AU-tuned 14-category taxonomy.
- Findings list grouped by risk level; accept/reject per finding.
- Tracked-changes `.docx` export.
- No payment, no obligation extraction, no multi-tenant collaboration, no precedent library.

Cohort: 12 in-house counsel from Priya's professional network, one 40-page sample MSA each, week of 2026-05-26.

## Success threshold

Per [mvp-metrics](../mvp-metrics.md):

- **Primary (H-002):** median redline time < 25 minutes across the 12-counsel cohort by 2026-06-13.
- **Refute:** median ≥ 45 minutes OR fewer than 10 of 12 complete a redline at all.
- **Secondary read (H-003):** classifier precision ≥ 85% (refute < 70%) on the held-out 30-document set, measured 2026-06-22.
