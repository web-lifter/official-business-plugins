# Cost-Benefit Analysis — {{decision_title}}

**Date:** {{YYYY-MM-DD}}
**Decision-maker:** {{name / role}}
**Time horizon:** {{N}} years
**Discount rate:** {{X}}% ({{rationale — WACC proxy, hurdle rate, etc.}})
**Capital constraint:** {{$X year-0 cap, or "none"}}
**Strategic objectives:** {{objective 1; objective 2; objective 3}}

---

## 1. Decision Context

{{One paragraph stating the decision question, why it is being asked now, and what is at stake. Name the trigger (vendor renewal, market shift, capacity wall) so future readers understand the framing.}}

---

## 2. Options

| # | Option | Classification | Year-0 outlay | Description |
|---|--------|----------------|--------------:|-------------|
| 1 | {{Option A}} | {{CapEx / OpEx / Phased / Partnership / Do-nothing}} | ${{X}} | {{1-sentence}} |
| 2 | {{Option B}} | … | ${{X}} | {{1-sentence}} |
| 3 | {{Option C}} | … | ${{X}} | {{1-sentence}} |
| 0 | Do-nothing baseline | Status quo | $0 | {{what continues if no action is taken}} |

---

## 3. Cost & Benefit Itemisation

### Option 1 — {{name}}

**Costs:**

| Category | Year 0 | Year 1 | Year 2 | … | Basis |
|---|---:|---:|---:|---|---|
| One-off | ${{X}} | | | | {{quote / estimate source}} |
| Recurring | | ${{X}} | ${{X}} | … | {{basis}} |
| Opportunity | | ${{X}} | ${{X}} | … | {{deferred project NPV}} |

**Benefits:**

| Category | Year 0 | Year 1 | Year 2 | … | Basis |
|---|---:|---:|---:|---|---|
| Revenue uplift | | ${{X}} | ${{X}} | … | {{price × volume basis}} |
| Cost savings | | ${{X}} | ${{X}} | … | {{baseline → new state}} |
| Avoided losses | | ${{X}} | ${{X}} | … | {{probability × impact}} |

**Intangibles (flagged for Phase 4):**
- {{e.g. capability building — improves future hiring}}
- {{e.g. dependency on single vendor}}

_(Repeat for each option.)_

---

## 4. Quantitative Scorecard

| Option | NPV (${{currency}}) | IRR | Payback (yrs) | Disc. Payback (yrs) | PI | BCR | Above hurdle? |
|---|---:|---:|---:|---:|---:|---:|---|
| {{A}} | {{X}} | {{X%}} | {{X}} | {{X}} | {{X}} | {{X}} | {{Yes/No/Marginal}} |
| {{B}} | … | … | … | … | … | … | … |
| Do-nothing | 0 | n/a | n/a | n/a | n/a | n/a | n/a |

**Financial rank (by NPV):** 1) {{Option}}  2) {{Option}}  3) {{Option}}

---

## 5. Qualitative Scorecard (1–5, higher = better)

| Dimension | Weight | {{A}} | {{B}} | {{C}} |
|---|---:|---:|---:|---:|
| Strategic alignment | {{X}} | {{n}} | {{n}} | {{n}} |
| Option value | {{X}} | {{n}} | {{n}} | {{n}} |
| Execution risk (inverted) | {{X}} | {{n}} | {{n}} | {{n}} |
| Reversibility | {{X}} | {{n}} | {{n}} | {{n}} |
| Stakeholder impact | {{X}} | {{n}} | {{n}} | {{n}} |
| **Weighted total** | 1.0 | **{{X}}** | **{{X}}** | **{{X}}** |

**Strategic rank:** 1) {{Option}}  2) {{Option}}  3) {{Option}}

---

## 6. Composite Ranking

| Option | Financial rank | Strategic rank | Composite |
|---|---:|---:|---|
| {{A}} | {{1}} | {{2}} | {{1.5 — leading}} |
| {{B}} | {{2}} | {{1}} | {{1.5 — tied}} |
| {{C}} | {{3}} | {{3}} | {{3}} |

{{One sentence on whether the two rankings agree or diverge, and what the divergence means.}}

---

## 7. Sensitivity (Tornado Spec)

Top-3 drivers for {{top-ranked option}}; NPV at ±20% of each input:

| Driver | NPV at −20% | Base NPV | NPV at +20% | Swing |
|---|---:|---:|---:|---:|
| {{Driver 1}} | ${{X}} | ${{X}} | ${{X}} | ${{X}} |
| {{Driver 2}} | ${{X}} | ${{X}} | ${{X}} | ${{X}} |
| {{Driver 3}} | ${{X}} | ${{X}} | ${{X}} | ${{X}} |

---

## 8. Scenario Table

| Option | Base NPV | Upside NPV | Downside NPV | Stress NPV |
|---|---:|---:|---:|---:|
| {{A}} | ${{X}} | ${{X}} | ${{X}} | ${{X}} |
| {{B}} | ${{X}} | ${{X}} | ${{X}} | ${{X}} |

**Assumption changes:**
- **Upside:** {{e.g. adoption +25%, costs −10%}}
- **Downside:** {{e.g. delay 6 months, costs +20%}}
- **Stress:** {{user-named tail event}}

---

## 9. Break-point Analysis

{{Plain-English statement: "Option A is preferred while the discount rate stays below 14%; above 14%, Option B overtakes." Repeat for each material driver that flips the ranking.}}

---

## 10. Recommendation

{{300–500 word narrative. Recommended option. Financial case (NPV / PI). Strategic case (top 2 qualitative dimensions). What would change the call. What this decision is NOT solving.}}

---

## 11. Decision-Review Triggers

Revisit this analysis if any of the following occur:
- {{Trigger 1}}
- {{Trigger 2}}
- {{Trigger 3}}

---

## 12. Biases to Watch

- **Sunk cost** — {{specific instance in the framing, or "not detected"}}
- **Anchoring** — {{e.g. vendor's quote dominated the comparison}}
- **Scope creep** — {{which option's costs grew during analysis}}
- **Optimism / planning fallacy** — {{benefit timelines vs historical slippage}}
- **Status-quo bias** — {{did the do-nothing baseline get a fair examination}}

---

## 13. Data Gaps & Assumptions Log

| Gap / Assumption | Material? | Action to firm up | Owner |
|---|---|---|---|
| {{e.g. Year-3 adoption rate is a guess}} | Yes — flips ranking at 60% | {{customer interviews; pilot data}} | {{name}} |
| {{e.g. Discount rate not formally set}} | Yes | {{CFO sign-off on 10% hurdle}} | {{name}} |

---

## When NOT to Use This Analysis

CBA is the wrong frame when the decision is:
- Regulatory / compliance-mandated (must-do; CBA is theatre)
- Mission-critical safety / reputation (asymmetric downside dominates)
- Pure optionality plays where the value IS the option itself

If any of these apply, treat this report as supporting analysis only.
