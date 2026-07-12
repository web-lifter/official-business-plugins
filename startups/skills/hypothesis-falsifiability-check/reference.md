# hypothesis-falsifiability-check — reference

## §1. Vagueness patterns

### Falsifier patterns

| Pattern | Why it fails | Salvage |
|---|---|---|
| "Users will love it" | No observation; no measurement | "≥40% of trial users invite a teammate within 7 days" |
| "Many people have this problem" | "Many" is a placeholder | "≥60% of café owners we interview report ≥4h/week on reconciliation" |
| "This will improve" | No baseline, no delta | "Time on task drops from 12 minutes (current) to ≤4 minutes" |
| "Customers prefer X" | No comparison set | "≥60% of segment-A choose X over Y in side-by-side test" |

### Measurement patterns

| Pattern | Why it fails | Salvage |
|---|---|---|
| "We'll know" | Doesn't say how | Name the data source: "PostHog event funnel `signup→activate`" |
| "Survey says" | Survey design matters | "20-question survey, 50 respondents from segment-A panel via X" |
| "Sales numbers" | Which numbers? | "Stripe ARR after 30 days post-launch" |

### Threshold patterns

| Pattern | Why it fails | Salvage |
|---|---|---|
| "High adoption" | Subjective | Specific %: "≥30%" |
| "Good conversion" | Industry-relative | Specific number with citation: "≥3% (industry avg 2.1%)" |
| "Revenue grows" | No baseline | "Monthly ARR ≥ $5k by month 3" |

### Timeframe patterns

| Pattern | Why it fails | Salvage |
|---|---|---|
| Missing | No decision rule | Specific window: "30 days from MVP launch" |
| "Eventually" | Not a timeframe | "Q3 2026" |
| "After enough data" | What's enough? | "After 100 trial users or 60 days, whichever is first" |

## §2. Examples by BMC cell

### Customer Segments

✓ "Café owners with 2-5 staff in inner Sydney spend ≥4h/week
reconciling supplier invoices on paper. Falsifier: same cohort spends
<1h. Measurement: 30-question survey via café-owner network.
Threshold: ≥70% report ≥4h. Timeframe: 30 days from survey launch."

✗ "Cafés need accounting tools." (vague segment, vague claim, no
measurement, no threshold, no timeframe)

### Value Propositions

✓ "Auto-reconciliation reduces weekly reconciliation time by ≥75%
for the segment-A profile. Falsifier: <50% reduction. Measurement:
side-by-side test with 5 paying pilot users, 4 weeks. Threshold:
median reduction ≥75%. Timeframe: 30 days post-pilot start."

✗ "Our auto-reconciliation will save them time." (no quantum, no
sample, no measurement, no threshold, no timeframe)

### Revenue Streams

✓ "Café owners pay AUD $49/mo subscription. Falsifier: <40% conversion
from pilot to paid. Measurement: Stripe checkout from pilot
graduation. Threshold: ≥40% paid conversion. Timeframe: 14 days from
pilot end."

✗ "There's a viable price point." (no number, no test, no rule)
