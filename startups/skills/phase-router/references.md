# phase-router — references

The routing rules encoded in this skill match the four-step customer-development model. See [`startups/SOURCES.md`](../../../SOURCES.md) for the underlying citations.

## The four-step model

- **Blank, Steve.** *The Four Steps to the Epiphany.* K&S Ranch, 2005.
  - Customer discovery → customer validation → customer creation → company building. Each step has gating questions; the phase-router rules in [`reference.md`](reference.md) translate those gates into file-system checks against the venture's `.memex/` tree.
- **Blank, Steve & Dorf, Bob.** *The Startup Owner's Manual.* K&S Ranch, 2012.
  - Practical playbook for the four-step model. Rules 1–6 of [`reference.md`](reference.md) (vision, segment, interviews, profile, VPC, fit) operationalise discovery. Rules 7–11 (BMC, test cards, learning cards, UVP, channels) operationalise validation. Rules 13–14 (`customer-discovery-status` 🟢, MVP scope) gate creation work.

## Prioritisation discipline

When multiple rules match, the router prioritises by customer-development phase order — i.e. close the gap at the earliest unfinished step. This reflects Blank's central claim that out-of-order work (e.g. building an MVP before finding a real problem in a real segment) is the dominant cause of startup failure.

## Read-only by design

The router never mutates state. Every recommendation cites a numbered rule in [`reference.md`](reference.md) and the file paths the rule fired against, so any disagreement with the recommendation can be relitigated against the rule itself rather than the model's judgement.
