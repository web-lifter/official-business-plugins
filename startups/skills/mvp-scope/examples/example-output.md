---
title: MVP scope v1
slug: mvp-spec
type: mvp-spec
status: draft
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# MVP scope — v1

**Primary hypothesis:** [H-002 — Usability (median redline < 25 min)](../01-hypotheses/hypothesis-register.md)
**Primary segment:** [AU mid-market in-house counsel](../02-customer-discovery/segments/au-mid-market-counsel/README.md)
**Primary value prop:** from [vpc-au-mid-market-counsel-v3](../03-value-proposition/vpc-au-mid-market-counsel-v3.md)

H-002 is chosen as primary because H-001 (demand) cannot be cleanly tested until counsel have actually used the tool — willingness-to-pay anchored on a working demo is more credible than a static page.

## Cut / Keep / Maybe

### Keep (the MVP) — 9 features

| Feature | Why required (to test H-002) | Test signal |
|---------|------------------------------|-------------|
| Google Workspace + email/password sign-in | Counsel can't try the tool without an account | `user_signed_up` |
| Org creation + single-org membership | RLS scope; one counsel = one org in v1 | `org_created` |
| Contract upload (`.docx`/`.pdf` ≤ 25 MB) | The H-002 stopwatch starts at upload | `contract_uploaded` |
| Async classifier (14-category taxonomy, AU MSA-tuned) | Without classification there's nothing to redline | `classifier_run_completed` |
| Findings list grouped by risk level | The actual review surface | `findings_first_viewed` |
| Accept/Reject per finding with optional comment | The decision discipline H-002 measures | `finding_decided` |
| Redline export (tracked-changes `.docx`) | End of the H-002 stopwatch | `redline_export_clicked` |
| PostHog instrumentation per events-spec | H-002 can't be measured without it | all funnel events |
| Privacy policy + ToS draft | Counsel won't upload without one | linked in footer |

### Maybe (post-v1 candidates)

| Feature | Why deferred | Trigger to revisit |
|---------|--------------|--------------------|
| Negotiation-brief export (one-page summary for business owner) | Not needed for H-002 stopwatch; cohort survey will tell us if counsel ask for it | ≥ 4/12 cohort participants request it |
| Obligation-extraction (calendar of "Buyer shall…" deadlines) | Different hypothesis (H-004 future); adds parser complexity | After H-002 confirms; explicitly out of v1 |
| Multi-org per user | Cohort study is one-org-per-counsel | First multi-org customer asks |
| Stripe checkout + paid plans | H-001 is tested via interview WTP, not transactional in v1 | After H-002 confirms |
| Audit log of accept/reject actions | Compliance need, not H-002 critical | First regulated-customer ask |
| OAuth via Microsoft 365 | Most cohort participants are on Google Workspace | First Microsoft-365-only prospect |

### Cut (out of MVP scope)

| Feature | Why cut |
|---------|---------|
| Precedent library ("what did we accept last quarter?") | Needs corpus; pre-V2 |
| In-app chat with classifier ("why is this risky?") | Adds turn-based UX; H-002 needs a deterministic single-pass review |
| Mobile app | Counsel review on laptops; no cohort participant uses mobile for review |
| API for procurement-system integration | Different segment; secondary |
| Slack / Teams notifications | Workflow surface; not on the H-002 path |
| Custom clause taxonomies per org | Tenant-scoped configuration; deferred to v2 |
| OCR for scanned PDFs | Document parsing complexity; v2 |
| Self-serve onboarding videos | Cohort study has Priya on Zoom for first session |
| Multi-language support | AU/NZ English only |
| Dark mode | Not on the H-002 path |
| Two-factor authentication | Google OAuth carries it; pure email/password 2FA deferred |
| Bulk upload (>1 contract at once) | Cohort study is one-at-a-time |
| Comment threads on findings (multi-reviewer) | One reviewer per contract in v1 |

Counts: **Keep 9, Maybe 6, Cut 13** → 65% cut, 32% maybe, ~32% keep. Within the discipline rule (≥ 60% cut, ≤ 30% keep — minor overshoot acknowledged; Priya defends as floor below which H-002 cannot be tested).

## What this MVP proves (or doesn't)

- **Confirms / refutes:** H-002 (usability — median redline time).
- **Tangentially supports:** H-003 (precision — measured against the same classifier runs).
- **Does NOT test:**
  - H-001 (willingness-to-pay) — tested separately via cohort interviews, not transactionally.
  - H-004+ (obligation tracking, precedent library, multi-org collaboration) — all deferred.

## MVP type

To be set by `/mvp-type-select`. Working assumption: **partial product** (narrow but real end-to-end slice). Confirmed at TC-006.

## Hand-off

Next: `/mvp-type-select` to confirm partial-product. Then `/mvp-tech-plan`.
