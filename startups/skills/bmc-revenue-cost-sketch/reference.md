# bmc-revenue-cost-sketch — reference

## §1. Revenue model archetypes

| Archetype | When it fits | Examples |
|---|---|---|
| **Subscription** | Recurring value, sticky usage | SaaS, streaming, gym |
| **Transaction** | Per-event value | Ride share, payment processing, e-commerce |
| **Usage-based** | Variable consumption | Cloud compute, API calls, electricity |
| **Licence** | Software / IP per seat or install | Enterprise software, fonts, stock photos |
| **Freemium** | Wide funnel; paid tier for power users | Slack, Notion, Spotify |
| **Marketplace fee** | Two-sided; revenue from each transaction | Airbnb, Etsy, Uber |
| **Ad-supported** | Free to user; advertisers pay for attention | Search, social, news |
| **Services / consulting** | High customisation, low repeat | Agencies, professional services |
| **Hybrid** | Mix of any of the above | SaaS + setup fees, freemium + marketplace, etc. |

## §2. Cost categories — quick prompts

### Fixed
- Salaries (founders, employees, contractors)
- Infrastructure (cloud baseline, office, tools)
- Licences (software, content, regulatory)
- Insurance, accounting, legal retainers

### Variable
- Per-customer compute (GPU, model APIs, bandwidth)
- Per-customer support (response time × cost-per-minute)
- Payment processing fees (2.9% + $0.30 baseline)
- Per-transaction COGS (physical goods, vendor margin)

### One-time
- Build (engineering effort to ship MVP)
- Launch (marketing, PR, content)
- IP (trade marks, patents, content licences)
- Legal (entity formation, contracts, terms of service)
- Onboarding partners (integration work, deal closing)

## §3. Willingness-to-pay heuristics

Use customer profile to gauge:

- **High**: pain is operational and recurring; budget exists; customer
  has paid for substitutes
- **Medium**: pain is real but workaround is acceptable; budget exists
  but is contested
- **Low**: pain is occasional / non-urgent; no obvious budget; price
  sensitivity high

Ask the segment's earlyvangelists during interviews — see
`/interview-guide-build` "What did it cost you" question.

## §4. When to escalate to unit-economics

The sketch is enough until:

- Real revenue numbers (≥ 1 paid pilot)
- Real cost numbers (≥ 1 month of infra bills, ≥ 1 month of support
  load)
- A meaningful go-to-market plan that needs CAC / LTV math

When all three are true, run `business-economics/unit-economics` and
link its output back to the sketch.
