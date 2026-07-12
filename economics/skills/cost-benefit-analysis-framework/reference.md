# Cost-Benefit Analysis — Reference Material

Dense reference content extracted from SKILL.md to keep it under the 500-line cap. Cite specific sections by anchor when invoking from the main skill body.

---

## 1. Discount Rate Theory

The discount rate translates future cashflows into present-value terms. It carries two jobs at once: **time preference** (a dollar now is worth more than a dollar later) and **risk compensation** (riskier cashflows are discounted more heavily). Conflating the two is the most common source of CBA error.

### Choosing a rate

| Context | Rate range | Rationale |
|---|---|---|
| Government / public sector | 3–7% | Long horizon, low default risk; usually a published Treasury rate |
| Large stable corporate | 7–10% | WACC reflects mixed debt/equity at investment-grade credit |
| Mid-market SMB | 10–15% | Higher cost of debt + equity holders' opportunity cost |
| Early-stage / startup | 20–35% | Equity capital is expensive; embeds high failure probability |
| Personal / household | Inflation + 2–4% | Real return on safe assets plus modest premium |

### WACC formula (refresher)

```
WACC = (E/V) × Re + (D/V) × Rd × (1 − T)
```

Where:
- E = equity value
- D = debt value
- V = E + D
- Re = cost of equity (CAPM: Rf + β × ERP)
- Rd = cost of debt (pretax)
- T = marginal tax rate

For SMBs without listed comparables, default to a hurdle rate set by the owner — typically the next-best use of the same capital. Document the rationale; do not derive WACC from textbooks for unlisted businesses.

### Real vs nominal

If cashflows are in nominal currency (inclusive of expected inflation), use a nominal discount rate. If cashflows are in real (constant) currency, use a real discount rate. Mixing the two is a silent error that overstates or understates NPV by the expected inflation rate per year — compounding badly over long horizons.

---

## 2. Metric Definitions

### NPV — Net Present Value
Sum of discounted cashflows. Decision rule: accept if NPV > 0; among mutually-exclusive options, pick the highest NPV.

```
NPV = Σ CF_t / (1 + r)^t   for t = 0 to T
```

### IRR — Internal Rate of Return
The discount rate at which NPV = 0. Decision rule: accept if IRR > hurdle rate.

**Pitfalls:**
- Undefined when all cashflows have the same sign.
- Multiple roots when cashflows change sign more than once.
- Reinvestment assumption: IRR implicitly assumes intermediate cashflows are reinvested at the IRR itself, which overstates returns for high-IRR projects. Use MIRR for those.

### MIRR — Modified IRR
Reinvests positive cashflows at a specified reinvestment rate (usually the cost of capital). More realistic for projects with strongly positive IRRs.

### Payback Period
Years until cumulative undiscounted cashflows turn positive. Decision rule: accept if payback < user-defined threshold (commonly 3 years for software, 5 for plant).

**Pitfalls:**
- Ignores cashflows after payback.
- Ignores time value of money.
- Useful as a liquidity proxy, not a returns metric.

### Discounted Payback
Years until cumulative DISCOUNTED cashflows turn positive. Fixes the time-value issue but still ignores post-payback cashflows.

### Profitability Index (PI) / Benefit-Cost Ratio (BCR)
Ratio of PV of benefits to PV of costs. Decision rule: PI > 1 means project creates value.

```
PI = PV(positive cashflows) / PV(negative cashflows)
```

PI is the right metric when capital is constrained — it ranks options by value-per-dollar-invested rather than absolute NPV.

### Equivalent Annual Cost / Annuity (EAC / EAA)
Useful for comparing options with different horizons. Convert the NPV into an equivalent annuity over each option's life and compare on an annualised basis.

---

## 3. Real Options Primer

Standard CBA undervalues flexibility because it assumes the decision is binary and final. Real options recognises that many investments carry embedded options:

- **Option to defer** — Waiting reveals information (vendor pricing, regulation, demand). The option to wait has value above and beyond the static NPV.
- **Option to expand** — A small pilot creates the right (not the obligation) to scale up if it succeeds. Value the option, not just the pilot's standalone NPV.
- **Option to abandon** — Salvage value or cancellation clauses limit downside; their existence increases option value.
- **Option to switch** — Mid-course pivots between technologies, suppliers, or markets.

**Heuristic, not formula.** Black-Scholes for real options is rarely tractable in SMB contexts. Instead, in Phase 4 score "option value" 1–5 on:

- Does the option create future right-to-act without obligation?
- Is the underlying uncertainty resolvable in the time horizon?
- Is the embedded option contingent on this investment, or independent?

---

## 4. Risk Adjustment Methods

### Method A — Probability-weighted expected value
Build Base / Upside / Downside cashflow streams. Run NPV on each. Weighted NPV = ΣP_i × NPV_i. Sensible defaults: 60/20/20 if user has no strong view; flag explicitly that this is a guess.

### Method B — Risk-adjusted discount rate
Add a premium to the base discount rate per option:
- Low risk (proven, internal): +0%
- Medium (new tech, known team): +2–3%
- High (novel domain, new team): +5%+

**Pitfall:** Double-counting risk by both probability-weighting AND raising the discount rate. Pick one method per analysis.

### Method C — Certainty-equivalent
Convert risky cashflows to "certainty-equivalent" amounts (what the decision-maker would accept with certainty), then discount at the risk-free rate. Cleanest theoretically; hardest to elicit in practice.

---

## 5. Common Biases in CBA

| Bias | How it shows up | Counter |
|---|---|---|
| Sunk cost | "We've already spent $500k on Option A, we may as well finish." | Frame all options from today forward; prior spend is irrelevant. |
| Anchoring | First quote received dominates the comparison. | Solicit independent estimates per option before showing prior quotes. |
| Scope creep | One option's costs grow as analysis proceeds. | Freeze scope at Phase 2; new requirements trigger a new analysis. |
| Optimism / planning fallacy | Year-1 benefits assume on-time delivery. | Apply historical slippage rates (typical: +30% on duration, +20% on cost). |
| Status-quo bias | Do-nothing baseline is treated as risk-free. | Explicitly model the cost of inaction (lost share, deferred decisions, etc.). |
| Confirmation bias | Inputs selected to favour a pre-existing preferred option. | Have a sceptic review the assumption table before running the model. |
| Salience / availability | Recent vivid events overweight risk on one side. | Use historical base rates where available; flag when relying on a single anecdote. |

---

## 6. When CBA Is the Wrong Frame

CBA assumes:
1. Costs and benefits are commensurable (convertible to a common metric, usually money)
2. Cashflows are reasonably predictable
3. The decision is reversible enough that getting it wrong is recoverable
4. Risk can be priced

When any of these break, CBA produces precise nonsense. Specifically:

- **Regulatory / compliance-mandated decisions** — Must-do; the only CBA question is implementation path, not whether to do it.
- **Safety / reputation decisions with asymmetric downside** — A 0.1% chance of catastrophic loss can dominate any expected-value calculation. Use scenario analysis with explicit tail-risk pricing, not NPV.
- **Identity / strategic-fit decisions** — "Is this the kind of business we want to be?" doesn't translate to cashflow.
- **Pure optionality plays** — When the value IS the option (e.g. holding a parcel of land, retaining a key hire), the cashflow lens misses the point.
- **Decisions with strong network effects or learning curves** — Static cashflow projections miss the dynamics that matter most.

When CBA is the wrong frame, the skill should still produce the analytical artefact (it remains useful as input to a broader judgement) but the recommendation section should explicitly defer.

---

## 7. Worked Example — Sensitivity / Break-point

Setup: Two options with year-0 cost and 5-year cashflows.

- **Option A:** [-100, 30, 30, 30, 30, 30]   → NPV at 10% = 13.7
- **Option B:** [-150, 40, 40, 40, 50, 60]   → NPV at 10% = 19.8

At 10% discount rate, Option B wins by 6.1.

Sweep the discount rate from 5% to 20%:

| Rate | NPV(A) | NPV(B) | Winner |
|---:|---:|---:|---|
| 5% | 29.9 | 45.0 | B |
| 10% | 13.7 | 19.8 | B |
| 13% | 5.5 | 7.4 | B (margin shrinks) |
| 14% | 3.0 | 3.6 | B (within noise) |
| 15% | 0.6 | 0.0 | A (just barely) |
| 18% | −6.2 | −9.6 | A (both negative; A less bad) |
| 20% | −10.3 | −15.0 | A |

**Break-point:** ~14.5% discount rate. Below that, B is preferred; above, A is preferred (or do-nothing if both are negative).

The skill's job in Phase 5 is to surface this break-point in plain English so the user understands what the recommendation hinges on.

---

## 8. Glossary

- **NPV** — Net Present Value
- **IRR** — Internal Rate of Return
- **MIRR** — Modified IRR (with explicit reinvestment rate)
- **PI** — Profitability Index (PV benefits / PV costs)
- **BCR** — Benefit-Cost Ratio (equivalent to PI in our decomposition)
- **WACC** — Weighted Average Cost of Capital
- **CapEx** — Capital expenditure (one-off, capitalised on balance sheet)
- **OpEx** — Operating expenditure (recurring, expensed in P&L)
- **Hurdle rate** — Minimum acceptable rate of return for a project
- **Terminal value** — Value assigned to cashflows beyond the explicit horizon
- **Optionality** — The right (not obligation) to take future action
