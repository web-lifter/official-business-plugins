# Moat Strength Audit — Reference Material

## Hamilton Helmer's 7 Powers (detailed criteria)

### 1. Scale Economies

- **Definition:** Cost per unit decreases with scale; competitor at smaller size has higher costs
- **Score 9–10:** Cost advantage is structural and very large (e.g. Walmart, Amazon AWS)
- **Score 6–7:** Meaningful per-unit cost advantage (10–25% lower)
- **Score 3–4:** Small advantage; can be eroded with focus
- **Score 0–1:** No scale economies (most pure SaaS at startup phase)

### 2. Network Effects

- **Definition:** Value to each user increases as users grow
- **Score 9–10:** Two-sided with very high cross-side dependency (eBay, Tinder, DoorDash at scale)
- **Score 7–8:** Strong same-side or moderate cross-side (Facebook, LinkedIn)
- **Score 4–5:** Some network effect but not core to value (Slack — useful for me even without my network)
- **Score 0–2:** No network effect; isolated value to each user

### 3. Counter-Positioning

- **Definition:** Incumbent can't copy without cannibalising existing business
- **Score 9–10:** Structural conflict (e.g. Costco's no-margin retail model — Walmart literally cannot adopt without destroying gross margin)
- **Score 5–6:** Some structural conflict
- **Score 0–2:** No structural conflict; incumbent can easily copy

### 4. Switching Costs

- **Definition:** Cost (real or perceived) for buyer to switch
- **Score 9–10:** Massive switching cost — re-training, re-integration, lost data (enterprise ERP)
- **Score 6–7:** Significant but achievable (Slack, CRM)
- **Score 3–4:** Moderate; some friction
- **Score 0–1:** No friction; trivial switching

### 5. Branding

- **Definition:** Buyers will pay more for the brand at equal performance
- **Score 9–10:** Strong premium pricing power; cultural touchstone (Apple, Hermès)
- **Score 6–7:** Some premium (Lululemon, Bunnings in AU)
- **Score 3–4:** Recognised but not premium-priced
- **Score 0–1:** Indistinguishable from alternatives

### 6. Cornered Resource

- **Definition:** Exclusive access to something (talent, IP, contract, raw material)
- **Score 9–10:** Truly unique and durable (Disney IP, Saudi Aramco oil reserves)
- **Score 6–7:** Hard to replicate but not impossible (key talent or unique data)
- **Score 3–4:** Some exclusivity, can be replicated with investment
- **Score 0–1:** Nothing exclusive

### 7. Process Power

- **Definition:** Execution capability competitors can't replicate quickly
- **Score 9–10:** Multi-decade learning curve embedded in organisation (Toyota Production System, In-N-Out)
- **Score 5–6:** Strong process but replicable in 24+ months
- **Score 0–2:** Generic execution; replicable with hire + 12 months

---

## Scoring Calibration — Real-World Examples

| Company | Likely 7 Powers Score (out of 70) | Pattern |
|---------|----------------------------------|---------|
| Apple (consumer hardware) | ~45 | Brand 10 + Scale 8 + Switching 8 + Process 8 |
| Costco | ~40 | Counter-positioning 10 + Scale 8 + Switching 5 + Brand 7 |
| Amazon Retail | ~38 | Scale 10 + Network 6 + Process 7 |
| Xero (AU SMB accounting) | ~35 | Network 6 (accountant channel) + Switching 7 + Brand 6 + Scale 5 |
| Coles + Woolies (each, AU retail) | ~32 | Scale 8 + Brand 5 + Counter-position 4 + Cornered 5 (locations) |
| Stripe | ~38 | Scale 9 + Switching 7 + Network 5 + Process 6 |
| Average B2B SaaS unicorn | ~25–30 | Mix |
| Most startups (Series A) | ~10–15 | Mostly weak; betting on building moats |

---

## Decay-Rate Heuristics

| Moat type | Default decay rate |
|----------|-------------------|
| Network effects | Strengthens with scale; defaults to flat-up |
| Switching costs | Decays as data-portability standards mature (1–2 points/decade) |
| Scale | Slowly improves with growth; can decay if a more efficient scale axis emerges |
| Brand | Slow to build, slow to decay; vulnerable to scandals + missed transitions |
| IP/cornered resource | Hard cliffs at patent expiry, contract renewal, key person departure |
| Process power | Decays as talent leaves; replicable with sustained investment |
| Regulatory | Cliff at regulatory change; usually slow but episodic |

---

## Worked Examples (Concise Patterns)

### Strong moat: Costco
- Counter-positioning (10): membership-fee + no-margin retail is structurally incompatible with traditional retailers
- Scale (8): SKU efficiency + buying power
- Switching (5): annual membership + warehouse familiarity
- Brand (7): cult-status loyalty
- Total: ~40 — very strong

### Moderate moat: Xero (AU accounting)
- Network via accountants (6): firms refer clients to Xero
- Switching (7): years of bookkeeping data + workflows
- Brand (6): strong in AU
- Scale (5): some advantage; Xero's hosting per-customer is lower
- Process (5): banking integration breadth
- Total: ~30 — solid moat, well-defended

### Weak moat: New B2B SaaS startup
- Scale (1): no advantage
- Network (1): single-sided product
- Switching (3): some data lock-in
- Brand (1): unknown
- Cornered (1): nothing exclusive
- Process (2): good team but generic
- Total: ~9 — weak; must build a moat before competitors catch up
