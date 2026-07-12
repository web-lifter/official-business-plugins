## Unit Economics Model — [Business Name]

### 1. Business Model Classification

- **Model Type:** {{SaaS / Service / E-commerce / Marketplace / Freelancer}}
- **Revenue Model:** {{subscription / project / retainer / transaction / hourly}}
- **Team Size:** {{solo / small team / mid-size}}
- **Currency:** {{AUD / USD}}
- **Analysis Period:** {{e.g. trailing 12 months}}

---

### 2. Core Metrics

**Customer Acquisition:**

| Metric | Value | Formula | Status |
|--------|-------|---------|--------|
| CAC (fully loaded) | ${{X}} | Total acquisition cost / New customers | {{assessment}} |
| CAC (marketing only) | ${{X}} | Ad spend + tools / New customers | {{assessment}} |
| CAC Payback Period | {{X}} months | CAC / Monthly gross margin per customer | {{assessment}} |

<!-- Fully loaded CAC includes: ad spend, BD salaries, proposal time, tools, trial/onboarding costs. -->
<!-- If only ad spend is provided, flag as partial CAC and estimate the gap. -->

**Customer Lifetime Value:**

| Metric | Value | Formula | Status |
|--------|-------|---------|--------|
| Average Revenue per Customer | ${{X}}/{{period}} | Total revenue / Active customers | |
| Gross Margin | {{X}}% | (Revenue - COGS) / Revenue | {{assessment}} |
| Customer Lifespan | {{X}} months | 1 / Monthly churn rate | |
| LTV (revenue) | ${{X}} | ARPC x Lifespan | |
| LTV (margin-adjusted) | ${{X}} | ARPC x Margin x Lifespan | {{assessment}} |

<!-- LTV should be margin-adjusted, not raw revenue. A $10K project at 30% margin = $3K LTV contribution. -->

**Health Ratios:**

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| LTV:CAC Ratio | {{X}}:1 | > 3:1 healthy | {{status_emoji}} {{assessment}} |
| CAC Payback | {{X}} months | < 12 months | {{status_emoji}} {{assessment}} |
| Gross Margin | {{X}}% | {{industry benchmark}} | {{status_emoji}} {{assessment}} |
| Net Margin | {{X}}% | {{industry benchmark}} | {{status_emoji}} {{assessment}} |
| Monthly Churn | {{X}}% | < 5% (SMB SaaS) | {{status_emoji}} {{assessment}} |

<!-- Never present a single number without context. Every metric needs a benchmark and interpretation. -->

---

### 3. Health Assessment

| Metric | Value | Benchmark | Status | Interpretation |
|--------|-------|-----------|--------|---------------|
| LTV:CAC | {{X}}:1 | > 3:1 | Green / Yellow / Red | {{plain-language meaning}} |
| Payback Period | {{X}} mo | < 12 mo | Green / Yellow / Red | {{plain-language meaning}} |
| Gross Margin | {{X}}% | > {{X}}% | Green / Yellow / Red | {{plain-language meaning}} |
| Churn Rate | {{X}}% | < {{X}}% | Green / Yellow / Red | {{plain-language meaning}} |
| Utilisation | {{X}}% | > 70% | Green / Yellow / Red | {{plain-language meaning — service businesses}} |

**Overall Health:** {{Healthy / Needs attention / Unsustainable}}

<!-- For service businesses, utilisation is the hidden multiplier. A 10% improvement in utilisation often has a larger profit impact than 10% revenue growth. -->

---

### 4. Scenario Analysis

**Base Case:**

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| Customers | {{X}} | {{X}} | {{X}} | {{X}} |
| Monthly Revenue | ${{X}} | ${{X}} | ${{X}} | ${{X}} |
| Monthly Costs | ${{X}} | ${{X}} | ${{X}} | ${{X}} |
| Net Margin | ${{X}} | ${{X}} | ${{X}} | ${{X}} |
| Cumulative Profit | ${{X}} | ${{X}} | ${{X}} | ${{X}} |

**Upside Case:** {{key assumption change — e.g. 20% lower churn}}

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| {{same structure as base case}} |

**Downside Case:** {{key assumption change — e.g. CAC doubles}}

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| {{same structure as base case}} |

**Sensitivity Table (Top Variable: {{variable_name}}):**

| {{Variable}} Value | LTV:CAC | Payback | Net Margin |
|-------------------|---------|---------|-----------|
| {{low}} | {{X}}:1 | {{X}} mo | {{X}}% |
| {{base}} | {{X}}:1 | {{X}} mo | {{X}}% |
| {{high}} | {{X}}:1 | {{X}} mo | {{X}}% |

---

### 5. Strategic Narrative

{{2-3 paragraph plain-language summary covering:}}
- {{Current state of the business economics}}
- {{The single biggest lever for improvement}}
- {{Whether the model is viable for scaling or needs fixing first}}

<!-- If unit economics are broken, growing faster just burns cash faster. -->
<!-- "Fix your margins before you scale" is often the right answer. -->

---

### 6. Key Levers

| # | Lever | Current | Target | Impact on LTV:CAC | Difficulty |
|---|-------|---------|--------|-------------------|-----------|
| 1 | {{e.g. Reduce churn by 2%}} | {{current}} | {{target}} | +{{X}} | Low / Med / High |
| 2 | {{e.g. Increase ARPU by $50}} | {{current}} | {{target}} | +{{X}} | Low / Med / High |
| 3 | {{e.g. Lower CAC via referrals}} | {{current}} | {{target}} | +{{X}} | Low / Med / High |

<!-- Segment where possible. Blended averages hide problems. -->
<!-- Show your working: every formula with actual numbers substituted in. -->

---

### 7. Action Items

**Immediate (next 30 days):**
1. {{specific action with expected impact}}

**Short-term (next 90 days):**
1. {{specific action with expected impact}}

**Data Gaps to Fill:**
- [ ] {{missing input that would improve the model — e.g. channel-level CAC}}
- [ ] {{missing input — e.g. actual churn data vs estimated}}

**Metric Tracking Checklist (monthly):**

| Metric | Definition | How to Measure | Target |
|--------|-----------|---------------|--------|
| {{metric}} | {{precise definition}} | {{measurement method}} | {{target value}} |

<!-- Track these monthly. Unit economics are a living model, not a one-time calculation. -->
