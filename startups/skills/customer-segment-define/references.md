# customer-segment-define — references

The user-vs-paying-customer distinction this skill enforces comes from Steve Blank's customer-development model. See [`startups/SOURCES.md`](../../../SOURCES.md) for full citations.

## User ≠ paying customer

- **Blank, Steve.** *The Four Steps to the Epiphany.* K&S Ranch, 2005.
  - Blank is explicit that the *user* (who actually operates the product) and the *paying customer* (who signs the cheque) are often different people, especially in B2B. Treating them as one role leads to demos that delight users and lose deals at procurement.
- **Blank, Steve & Dorf, Bob.** *The Startup Owner's Manual.* K&S Ranch, 2012.
  - Practical guidance on modelling both roles. If they sit in the same function (e.g. a marketing manager who buys and uses an analytics tool), use sub-folders `<slug>-user` and `<slug>-buyer`. If they sit in different functions (e.g. in-house counsel uses, procurement buys), model them as separate peer segments.

## Why observable problems, not abstractions

Blank's discipline is to ground a segment in *observable behaviour* — what we could see them doing if we shadowed them for an hour. "Small business owners struggle with efficiency" is a market trope; "Owners of independent cafés in inner Sydney spend 4+ hours each Friday reconciling supplier invoices on paper" is a customer-development hypothesis.

This skill refuses abstract problems for the same reason `hypothesis-register` refuses statements without falsifiers: a segment that cannot be observed cannot be tested.

## One folder per segment

Blank treats segmentation as the unit of focus. Two segments in one folder is a sign the team has not yet committed to one. The skill enforces this by failing on slug collision and recommending a more specific slug instead.
