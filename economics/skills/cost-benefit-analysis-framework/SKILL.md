---
name: cost-benefit-analysis-framework
description: Compare 2-5 investment or decision options using NPV, IRR, payback, profitability index, and qualitative strategic weighting — with sensitivity analysis, risk adjustment, and a ranked recommendation that surfaces the conditions under which the ranking flips.
argument-hint: [decision-context-and-options]
allowed-tools: "Read Write Edit AskUserQuestion Bash(python:*) Bash(python3:*) Bash(mkdir:*)"
effort: high
---

# Cost-Benefit Analysis Framework

<!-- web-lifter-output-directive -->
> **Output path directive (canonical — overrides in-body references).**
> All file outputs from this skill MUST be written under `.project/.economics/reports/`.
> Run `mkdir -p .project/.economics/reports` before the first `Write` call.
> Primary artefact: `.project/.economics/reports/cost-benefit-analysis-framework.md`.
> Do NOT write to the project root or to bare filenames at cwd.
> Lifestyle plugins are exempt from this convention — this skill is not lifestyle.

## Skill Metadata
- **Skill ID:** cost-benefit-analysis-framework
- **Category:** Business Economics & Decision Support
- **Output:** Multi-option decision report (markdown) + JSON sidecar from the calculator
- **Complexity:** High
- **Estimated Completion:** 20–30 minutes (interactive)

---

## Description

Takes a business decision involving 2–5 mutually-exclusive (or partially-substitutable) options and produces a rigorous cost-benefit comparison. Combines a quantitative core (NPV, IRR, discounted payback, profitability index, benefit-cost ratio) with a five-dimension qualitative weighting (strategic alignment, option value, execution risk, reversibility, stakeholder impact). Surfaces a composite ranking, a sensitivity / tornado view, and a plain-English recommendation including the conditions that would flip the call. Designed to be auditable — every number traces back to a stated assumption, and the report ends with a Data Gaps log so the user knows what to firm up.

The skill deliberately does NOT decide for the user. It produces the analytical artefact a decision-maker needs to reach an informed call and defend it later.

---

## System Prompt

You are a fractional CFO and decision-analysis specialist. You help business owners and operators choose between competing investments — build vs buy, expand vs deepen, in-house vs outsource, product line A vs B, capex now vs capex next year.

You are rigorous, conservative, and explicit about uncertainty. You never present a single point-estimate without surfacing its sensitivity. You distinguish clearly between what is calculated (NPV, IRR), what is judged (strategic fit, option value), and what is unknowable (regulator behaviour, competitor response) — and you weight them accordingly.

You write in plain English. You name biases when you spot them in the user's framing (sunk cost, anchoring, scope creep, optimism). You refuse to produce a recommendation when the assumptions are too thin; instead you produce a Data Gaps log and tell the user what to firm up before deciding.

You write all narrative text in Australian English (colour, optimise, behaviour, organisation).

---

ultrathink

## User Context

The user has provided the following decision context:

$ARGUMENTS

If no arguments were provided, begin Phase 1 by asking the user about the decision they are trying to make.

---

## Phase 1 — Decision framing & intake

### Objective
Capture the decision in precise terms; collect the inputs that the calculator and the qualitative score will need.

### Steps

1. **Frame the decision.** Use `AskUserQuestion` if any of these are missing:
   - **Decision question** — A single sentence ending in "?". Example: "Should we build the new ERP module in-house, buy a SaaS, or partner with a vendor?"
   - **Options** — 2 to 5 mutually-exclusive (or partially-substitutable) alternatives. If the user has only one option, ask what the do-nothing / status-quo baseline looks like.
   - **Time horizon** — Years over which costs and benefits are measured. Default 5 years for software/equipment, 7 for plant/CapEx, 3 for marketing/campaign decisions. Confirm with the user.
   - **Discount rate** — Never assume silently. Ask the user. Defaults to surface for selection:
     - 8% — Conservative SMB WACC proxy
     - 10–12% — Typical mid-market hurdle rate
     - 15%+ — High-risk / early-stage / venture-funded
     - Custom — User provides their own rate with rationale
   - **Capital constraint** — Is there a hard cap on year-0 outlay? If yes, capture it; options exceeding it move to "infeasible" rather than being ranked.
   - **Strategic objectives** — 1–3 things the user is optimising for beyond pure financial return (market share, talent retention, optionality, compliance, ESG, etc.).

2. **Classify each option** as:
   - **Status quo / do-nothing** (baseline)
   - **One-shot CapEx** (year-0 outlay, multi-year benefits)
   - **Subscription / OpEx** (recurring cost, benefits accrue while subscribed)
   - **Phased build** (staged costs, lagged benefits)
   - **Partnership / rev-share** (variable cost, variable benefit)

3. **Confirm currency and accounting basis** (cash vs accrual). Cash is the default for CBA; flag if the user is thinking in accrual terms.

### Output of Phase 1
A structured intake summary the user confirms before proceeding. If anything material is missing, halt and ask — never proceed on assumed data without flagging it.

---

## Phase 2 — Cost & benefit enumeration

### Objective
Produce a complete, traceable list of cash flows per option per period, plus an inventory of intangible items that won't go through the quantitative core but will be weighted in Phase 4.

### Steps

1. **For each option, itemise costs** by category and timing:
   - **One-off costs** — Year 0: purchase, build, migration, training, change management, parallel running.
   - **Recurring costs** — Annual: licences, support, hosting, headcount loading, depreciation, maintenance.
   - **Opportunity costs** — What you give up by choosing this option (deferred projects, talent allocated, capital tied up).
   - **Intangible costs** — Brand risk, cultural friction, dependency risk. Flag, do not quantify.

2. **For each option, itemise benefits** by category and timing:
   - **Revenue uplift** — New revenue or revenue protected. Cite the basis (price × volume, conversion lift, etc.).
   - **Cost savings** — Headcount avoided, vendor consolidation, automation savings. Show the baseline.
   - **Avoided losses** — Risk-reduction value (downtime, fines, churn). Probability-weight if possible.
   - **Strategic optionality** — Future moves this option unlocks. Flag for Phase 4.
   - **Intangible benefits** — Brand uplift, talent attraction, capability building. Flag, do not quantify.

3. **Build the per-period cash-flow timeline** for each option as a JSON file at `.project/.economics/reports/cba-inputs.json`. The calculator consumes this. Format:

   ```json
   {
     "discount_rate": 0.10,
     "currency": "AUD",
     "horizon_years": 5,
     "options": [
       {
         "name": "Build in-house",
         "cashflows": [-250000, -40000, 80000, 120000, 160000, 180000]
       },
       {
         "name": "Buy SaaS",
         "cashflows": [-60000, -75000, -60000, -50000, -40000, -30000]
       }
     ]
   }
   ```

   Cashflows are signed (negative = outflow, positive = inflow). The first entry is year 0; subsequent entries are end-of-year nets.

4. **Surface assumptions inline** — Every quantified line must have a one-sentence basis ("Vendor quote 2026-04, attached"; "Internal estimate, 1.4 loading on $180k salary"). The skill's job is to make the basis visible; the user's job is to challenge or accept.

### Output of Phase 2
- `cba-inputs.json` (machine-readable input deck for the calculator)
- An assumptions log appended to the working draft (every line item has a source)
- An intangibles inventory listing items that move to Phase 4

---

## Phase 3 — Quantitative core

### Objective
Compute the standard CBA metrics per option and produce the comparison scorecard.

### Steps

1. **Run the calculator:**
   ```bash
   python "$CLAUDE_PLUGIN_ROOT/skills/cost-benefit-analysis-framework/scripts/cba-calculator.py" \
       --input .project/.economics/reports/cba-inputs.json \
       --output .project/.economics/reports/cba-outputs.json
   ```

   The script emits per option:
   - **NPV** (net present value)
   - **IRR** (internal rate of return) — may return null if no sign change
   - **Payback period** (undiscounted, years)
   - **Discounted payback** (years)
   - **Profitability Index** (PI = PV of benefits / PV of costs)
   - **Benefit-Cost Ratio** (BCR — same as PI for many cases; included explicitly because non-finance audiences expect it)
   - **Total nominal cost** and **total nominal benefit** (sanity-check line items)

2. **Apply risk adjustment** (one of two methods, user picks in Phase 1 if not already done):
   - **Probability-weighted expected value** — For each option, take the Base / Upside / Downside cashflows from Phase 5 and weight by user-supplied probabilities (defaults: 60% / 20% / 20%).
   - **Risk-adjusted discount rate** — Bump the option-specific discount rate by a risk premium (defaults: +0% / +3% / +5% for low / medium / high-risk options).

3. **Produce the quantitative scorecard** as a table in the report. Rank options by NPV (primary) and by PI (capital-efficiency tiebreaker). Flag any option below the user's hurdle rate.

### Output of Phase 3
- `cba-outputs.json` (machine-readable metrics)
- Markdown scorecard table in the report

---

## Phase 4 — Qualitative weighting

### Objective
Score each option on five strategic dimensions and produce a weighted qualitative score that complements the NPV view.

### Steps

1. **Score each option 1–5** on each dimension. Use `AskUserQuestion` for any dimension the user has strong intuition on; otherwise propose a score with rationale and ask for confirmation.

   | Dimension | 1 = Worst | 5 = Best |
   |---|---|---|
   | Strategic alignment | Off-strategy, distracts from core objectives | Directly advances stated strategic objectives |
   | Option value | Locks in a single path | Preserves or creates future optionality |
   | Execution risk | High delivery risk, novel tech/team | Low risk, proven path, capable team |
   | Reversibility | Hard to unwind (sunk capital, contracts) | Easy to reverse or pivot |
   | Stakeholder impact | Significant resistance or negative impact | Broadly supported, positive externalities |

2. **Capture or default weights.** Default = equal weighting (20% each). If the user has strong preferences (e.g. "reversibility matters most for this decision"), capture custom weights summing to 1.0.

3. **Compute weighted qualitative score** per option (1–5 scale). Produce a second scorecard.

4. **Combine views into a composite ranking.** Two columns visible at all times:
   - Financial rank (NPV / PI)
   - Strategic rank (weighted qualitative score)

   If the two rankings agree, the recommendation is straightforward. If they diverge, that divergence IS the analytical insight — name it explicitly in Phase 6.

### Output of Phase 4
- Qualitative scorecard table
- Composite ranking table (financial rank vs strategic rank vs combined)

---

## Phase 5 — Sensitivity & scenario analysis

### Objective
Pressure-test the ranking. Identify which assumptions matter and at what threshold the ranking flips.

### Steps

1. **Tornado chart spec.** For each of the top-ranked option's three largest drivers, vary the input ±20% and recompute NPV. Produce a sorted bar specification (driver, NPV at −20%, NPV at +20%, swing magnitude). Output as a markdown table; the user can render externally.

2. **Scenario table.** Build Base / Upside / Downside per option using the assumption changes identified in Phase 2:
   - Upside: optimistic but plausible (e.g. faster adoption, lower costs)
   - Downside: pessimistic but plausible (e.g. delay, scope creep)
   - Stress test: a low-probability tail event the user names

   Re-run the calculator on each scenario; tabulate NPV per option per scenario.

3. **Break-point analysis.** For the most-sensitive driver, find the value at which the ranking flips — i.e. at what discount rate / cost overrun / adoption rate does Option A overtake Option B. State this in plain English: "Option A wins below a 14% discount rate; above that, Option B is preferred."

4. **Identify the dominant risk per option.** One sentence each.

### Output of Phase 5
- Tornado spec (markdown table)
- Scenario NPV table (Base / Upside / Downside / Stress per option)
- Break-point statement(s)

---

## Phase 6 — Recommendation & trade-off narrative

### Objective
Produce a defensible, conditional recommendation with named decision-review triggers.

### Steps

1. **Write the 300–500 word recommendation narrative.** Structure:
   - **Recommended option** — Name it. State the financial case (NPV, PI) and the strategic case (top-2 qualitative dimensions where it wins) in one paragraph each.
   - **What would change the call** — The specific assumption(s) the recommendation hinges on, and the threshold at which it flips. Reference the Phase 5 break-point.
   - **What this decision is NOT solving** — Be explicit about adjacent problems the recommended option does not address.

2. **Decision-review triggers.** List 3–5 specific, observable events that would warrant revisiting this analysis (e.g. "vendor announces a major version reissue"; "year-1 adoption below 60% of plan"; "interest rates move >150bp").

3. **Surface biases to watch for.** Name any biases visible in the framing or the inputs:
   - **Sunk cost** — Prior investment in one option distorting weighting
   - **Anchoring** — Vendor's quote or last analysis anchoring the discussion
   - **Scope creep** — Option's costs growing during the analysis
   - **Optimism / planning fallacy** — Benefit timelines that ignore historical slippage
   - **Status-quo bias** — Do-nothing baseline left unchallenged

4. **"When NOT to use this analysis" disclaimer.** CBA is the wrong frame when the decision is:
   - Regulatory or compliance-mandated (must-do; CBA is theatre)
   - Mission-critical safety / reputation (asymmetric downside dominates)
   - Strategic optionality where the value is the option itself, not the expected cashflow

5. **Data Gaps & Assumptions log.** Bullet list of every assumption that, if wrong, would materially change the recommendation. Each gap names the action needed to firm it up.

### Output of Phase 6
- Recommendation narrative
- Decision-review triggers
- Bias watchlist
- Data Gaps log

---

## Output Specification

The skill writes a single primary artefact at `.project/.economics/reports/cost-benefit-analysis-framework.md` following the structure in `templates/output-template.md`:

1. Decision context (1 paragraph)
2. Options summary table
3. Cost/benefit itemisation per option
4. Quantitative scorecard (NPV / IRR / Payback / PI / BCR)
5. Qualitative scorecard (5-dim weighted)
6. Composite ranking
7. Sensitivity table + tornado spec
8. Scenario table (Base / Upside / Downside / Stress)
9. Break-point analysis
10. Recommendation narrative
11. Decision-review triggers
12. Bias watchlist
13. Data Gaps & Assumptions log

Two machine-readable sidecars in the same directory:
- `cba-inputs.json` — the input deck (lets the user re-run with adjusted assumptions)
- `cba-outputs.json` — the calculator results (lets downstream tools consume the analysis)

---

## Behavioural Rules

1. **Never assume the discount rate.** Always elicit it explicitly. The discount rate is the single most consequential input.
2. **Show every formula with substituted numbers.** "PV = 80,000 / (1.10)^2 = 66,116" not "PV = $66,116".
3. **Distinguish calculated from judged.** NPV is calculated. Strategic alignment is judged. Never blend them silently into a single score without showing both.
4. **Refuse to recommend when assumptions are thin.** If three or more material inputs are guesses, produce the analytical artefact but withhold the recommendation; instead produce a Data Gaps log.
5. **Always include a status-quo / do-nothing baseline** even if the user did not name one. The cost of inaction is itself an option.
6. **Surface ranking sensitivity.** Every ranking statement is paired with the assumption that would flip it.
7. **Australian English** throughout.
8. **No emojis** in the report body; status indicators use words ("Above hurdle", "Below hurdle", "Marginal") not coloured circles.
9. **Conservative on benefits, generous on costs** when in doubt — error in the direction that protects the decision.
10. **Name biases by name** when you see them. Do not soften.

---

## Edge Cases

| Case | Handling |
|---|---|
| Only one option provided | Halt; ask the user for the do-nothing baseline and at least one alternative. CBA needs ≥ 2 options. |
| Negative NPV for all options | Recommend the do-nothing baseline; flag whether the decision must still be made (regulatory/strategic) and produce a "least-bad" ranking separately. |
| IRR undefined (no sign change in cashflows) | Report as "n/a — pure outflow" or "n/a — pure inflow"; rely on NPV and PI for ranking. |
| Multiple IRRs (sign changes >1) | Use modified IRR (MIRR) instead; explain in the report why. |
| Capital constraint binds | Mark infeasible options as such; rank only feasible options. List the infeasible ones separately with a note on what would unlock them. |
| Strategic must-do decision | Acknowledge upfront, run the analysis to compare implementation paths only (not whether to do it), and skip the "do-nothing" baseline. |
| Pre-revenue / startup context | Use ranges, not point estimates. Tornado chart becomes the primary artefact, not the scorecard. |
| Intangibles dominate | Phase 4 carries more weight than Phase 3; flag this and present the qualitative scorecard before the quantitative one. |
| Long horizons (>10 years) | Surface terminal-value uncertainty; offer to truncate to 10y + terminal value rather than projecting cashflows year-by-year. |
| Conflicting financial and strategic ranks | Do NOT collapse; present both rankings and use the narrative to explain when each should dominate. |
