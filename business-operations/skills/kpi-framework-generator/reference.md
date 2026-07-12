# KPI Framework Generator — Reference Material

## Table of Contents

- [Sean Ellis North-Star Framework](#sean-ellis-north-star-framework)
- [AARRR Pirate Metrics (Dave McClure)](#aarrr-pirate-metrics-dave-mcclure)
- [Doerr OKR Model](#doerr-okr-model)
- [DuPont Financial Decomposition](#dupont-financial-decomposition)
- [Industry KPI Benchmarks (Australian SMB context, 2024–2026)](#industry-kpi-benchmarks-australian-smb-context-20242026)
- [Functional KPI Libraries](#functional-kpi-libraries)
- [Mermaid Mindmap Template](#mermaid-mindmap-template)

---

## Sean Ellis North-Star Framework

The North-Star Metric (NSM) is the single metric that best captures the core value your product delivers to customers. It sits above all other metrics in the hierarchy.

### Criteria for a Good North-Star
1. **Reflects customer value received** — not company revenue (revenue is a lagging consequence)
2. **Predicts long-term growth** — moves before revenue moves
3. **Understandable by the whole team** — every function can see how they contribute
4. **Measurable** — a number the team can actually track

### North-Star Anti-Patterns
- Revenue (lagging — tells you what happened, not why)
- Number of users (vanity — active users matter, raw signups don't)
- NPS (sentiment proxy — useful but not a North-Star)
- "Engagement" without definition (meaningless)

---

## AARRR Pirate Metrics (Dave McClure)

Framework for mapping the customer journey. Use to identify which stage of the funnel to prioritise.

| Stage | Measures | Example Metrics |
|-------|---------|-----------------|
| **Acquisition** | How do users find you? | CAC, CPL, organic sessions, paid impressions |
| **Activation** | Do users have a good first experience? | Trial → paid conversion, onboarding completion, time-to-value |
| **Retention** | Do users come back? | Day-7/30 retention, churn rate, renewal rate |
| **Referral** | Do users tell others? | NPS, referral rate, viral coefficient |
| **Revenue** | Do users pay? | MRR, ARPU, LTV, gross margin |

For most SMBs, the highest-leverage stage is **Retention** — reducing churn compounds faster than increasing acquisition.

---

## Doerr OKR Model

**Objective**: Qualitative, inspiring direction. "What do we want to achieve?"
**Key Result**: Quantitative, measurable outcome. "How will we know we got there?"

### Rules
- 3–5 objectives per quarter
- 2–5 key results per objective
- Key results are outcomes (results), not activities (tasks)
- Stretch: 70% achievement of a well-set OKR is considered success

### OKR → KPI Mapping
| OKR Element | KPI Role |
|------------|---------|
| Objective | Strategic theme — no single KPI |
| Key Result | Primary KPI with target |
| Initiative | Leading indicator KPI |

---

## DuPont Financial Decomposition

DuPont breaks Return on Equity (ROE) into three drivers — useful for identifying where financial performance is being lost.

```
ROE = Net Profit Margin × Asset Turnover × Equity Multiplier
    = (Net Income / Revenue) × (Revenue / Assets) × (Assets / Equity)
```

For SMBs without public equity, use the operating version:
```
EBITDA Margin = Gross Margin − Operating Expense Ratio
```

### Key Finance KPIs by Stage

| Stage | Priority KPIs |
|-------|--------------|
| Pre-revenue | Cash runway (months), burn rate (AUD/month) |
| Early traction | Gross margin %, CAC payback period |
| Growth | LTV:CAC, net revenue retention, EBITDA margin |
| Mature | ROIC, cash conversion cycle, DSO |

---

## Industry KPI Benchmarks (Australian SMB context, 2024–2026)

### SaaS

| KPI | Good | Excellent |
|-----|------|-----------|
| Monthly churn rate | < 2% | < 0.5% |
| Net Revenue Retention | > 100% | > 120% |
| CAC payback period | < 18 months | < 12 months |
| Gross margin | > 65% | > 80% |
| Trial-to-paid conversion | > 10% | > 25% |

### eCommerce

| KPI | Good | Excellent |
|-----|------|-----------|
| Repeat purchase rate (12-month) | > 25% | > 45% |
| Customer LTV (12-month) | 3× CAC | 5× CAC |
| Average order value | Context-dependent | +20% YoY |
| Cart abandonment rate | < 65% | < 50% |
| Email open rate | > 20% | > 35% |

### Professional Services

| KPI | Good | Excellent |
|-----|------|-----------|
| Client retention rate | > 70% | > 85% |
| Revenue per engagement | Trending up YoY | +15% YoY |
| Utilisation rate | > 65% | > 80% |
| NPS | > 30 | > 60 |
| Proposal win rate | > 35% | > 55% |

### Marketplace

| KPI | Good | Excellent |
|-----|------|-----------|
| Gross take rate | 10–20% | 20–30% |
| Buyer repeat rate | > 30% | > 50% |
| Liquidity (fill rate) | > 50% | > 80% |
| GMV growth MoM | > 10% | > 20% |

---

## Functional KPI Libraries

### Sales
- Pipeline velocity: (# opportunities × avg deal size × win rate) / sales cycle length
- Win rate: closed-won / total opportunities closed
- Average deal size: total closed-won revenue / # deals closed
- Sales cycle length: average days from first contact to close
- Quota attainment: closed-won revenue / quota × 100%

### Marketing
- CAC: total marketing spend / new customers acquired
- MQL → SQL conversion: SQLs / MQLs × 100%
- Cost per lead (CPL): spend / leads by channel
- Brand share of voice: brand mentions / total category mentions
- Content conversion rate: content-attributed leads / content sessions

### Operations
- Cycle time: average time from order/request to delivery/resolution
- On-time delivery rate: on-time completions / total completions
- Defect / error rate: defects / total units produced
- SLA compliance: requests resolved within SLA / total requests
- Unit cost: total variable costs / units produced or delivered

### Product
- Feature adoption rate: users using feature / eligible users × 100%
- Time-to-value: average days from sign-up to first core value action
- CSAT: average satisfaction score (1–5 or 1–10)
- Release cadence: deployments or feature releases per month
- Bug resolution time: average days from report to fix

### Finance
- Gross margin %: (revenue − COGS) / revenue × 100%
- Operating expense ratio: total opex / revenue × 100%
- EBITDA margin: EBITDA / revenue × 100%
- Cash conversion cycle: DSO + DIO − DPO (days)
- Days sales outstanding (DSO): (AR / revenue) × days in period

### Customer Experience
- First response time: average hours to first response
- Resolution rate: resolved tickets / total tickets × 100%
- NPS: % promoters − % detractors (−100 to +100)
- Churn rate: churned customers / beginning-of-period customers × 100%
- Expansion revenue %: expansion MRR / beginning MRR × 100%

---

## Mermaid Mindmap Template

```
mindmap
  root((North-Star Metric))
    Input Metric 1
      KPI 1A
      KPI 1B
    Input Metric 2
      KPI 2A
      KPI 2B
    Input Metric 3
      KPI 3A
      KPI 3B
```
