# Entity Disambiguation: Customer Merge

**Scenario:** Merging customer records between CRM (HubSpot) and billing system (Stripe) for an Australian B2B SaaS company
**Source A:** HubSpot Contacts (1,247 records)
**Source B:** Stripe Customers (983 records)
**Goal:** Produce a canonical customer list with `sameAs` mappings

---

## Match Scoring Rules

Each candidate pair receives a composite score (0-100) based on weighted field comparisons.

| Field | Weight | Match Logic |
|-------|--------|-------------|
| Email (primary) | 35 | Exact match (case-insensitive) |
| Company name | 20 | Jaro-Winkler similarity >= 0.88 |
| Phone | 15 | Normalised digits match (strip +61, spaces, dashes) |
| Full name | 15 | Jaro-Winkler similarity >= 0.85 |
| ABN | 10 | Exact 11-digit match |
| Domain | 5 | Extracted domain from email, exact match |

**Decision thresholds:**
- **>= 80:** Auto-merge (high confidence)
- **60-79:** Flag for manual review
- **< 60:** No match

---

## Match Results Summary

| Category | Pairs | % of Source B |
|----------|-------|---------------|
| Auto-merge (>= 80) | 814 | 82.8% |
| Manual review (60-79) | 47 | 4.8% |
| No match found | 122 | 12.4% |

---

## Sample Canonical Records

### Auto-Merge Example (Score: 95)

| Field | HubSpot (Source A) | Stripe (Source B) | Canonical Value |
|-------|-------------------|-------------------|-----------------|
| **Name** | Sarah O'Brien | Sarah O'Brien | Sarah O'Brien |
| **Email** | sarah@brightpath.com.au | sarah@brightpath.com.au | sarah@brightpath.com.au |
| **Company** | BrightPath Education Pty Ltd | BrightPath Education | BrightPath Education Pty Ltd |
| **Phone** | +61 412 345 678 | 0412345678 | +61 412 345 678 |
| **ABN** | 51 824 753 556 | -- | 51 824 753 556 |

```json
{
  "canonical_id": "cust_00814",
  "source_ids": {
    "hubspot": "hs_contact_29481",
    "stripe": "cus_R8kPqL2vN5mXzJ"
  },
  "match_score": 95,
  "match_breakdown": {
    "email": 35,
    "company_name": 18,
    "phone": 15,
    "full_name": 15,
    "abn": 10,
    "domain": 5
  },
  "decision": "auto_merge",
  "canonical_record": {
    "full_name": "Sarah O'Brien",
    "email": "sarah@brightpath.com.au",
    "company": "BrightPath Education Pty Ltd",
    "phone": "+61 412 345 678",
    "abn": "51824753556"
  }
}
```

### Manual Review Example (Score: 68)

| Field | HubSpot (Source A) | Stripe (Source B) | Notes |
|-------|-------------------|-------------------|-------|
| **Name** | James Nguyen | J. Nguyen | Partial first name match |
| **Email** | james.n@outlook.com | jnguyen@acmecorp.com.au | Different emails |
| **Company** | Acme Corp | ACME Corporation Pty Ltd | Similar but not exact |
| **Phone** | 0433 221 987 | +61 433 221 987 | Match after normalisation |
| **ABN** | -- | 12 345 678 901 | Only in one source |

```json
{
  "candidate_id": "review_00023",
  "source_ids": {
    "hubspot": "hs_contact_10332",
    "stripe": "cus_M4nTqX9wK2pYaB"
  },
  "match_score": 68,
  "match_breakdown": {
    "email": 0,
    "company_name": 17,
    "phone": 15,
    "full_name": 11,
    "abn": 0,
    "domain": 0
  },
  "decision": "manual_review",
  "review_reason": "Phone matches but emails differ; company names are similar but not definitive. Likely same person using personal vs. corporate email.",
  "suggested_action": "MERGE -- confirm with sales team that James Nguyen at Acme Corp uses both email addresses."
}
```

---

## sameAs Mapping Table

Output format for the resolved canonical mapping (stored in Supabase).

```sql
CREATE TABLE public.customer_identity_map (
  canonical_id    TEXT PRIMARY KEY,
  hubspot_id      TEXT,
  stripe_id       TEXT,
  match_score     INTEGER NOT NULL,
  decision        TEXT NOT NULL CHECK (decision IN ('auto_merge', 'manual_merge', 'no_match')),
  reviewed_by     TEXT,
  reviewed_at     TIMESTAMPTZ,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Sample rows
INSERT INTO public.customer_identity_map (canonical_id, hubspot_id, stripe_id, match_score, decision) VALUES
  ('cust_00001', 'hs_contact_10201', 'cus_A1bC2dE3fG4hI5', 92, 'auto_merge'),
  ('cust_00002', 'hs_contact_10202', 'cus_J6kL7mN8oP9qR0', 88, 'auto_merge'),
  ('cust_00023', 'hs_contact_10332', 'cus_M4nTqX9wK2pYaB', 68, 'manual_merge'),
  ('cust_00814', 'hs_contact_29481', 'cus_R8kPqL2vN5mXzJ', 95, 'auto_merge'),
  ('cust_00900', 'hs_contact_30102', NULL,                   0,  'no_match'),
  ('cust_00901', NULL,               'cus_T3uV4wX5yZ6aB7', 0,  'no_match');
```

---

## Confidence Distribution

```
Score Range   Count   Decision
90-100        612     Auto-merge
80-89         202     Auto-merge
70-79          31     Manual review
60-69          16     Manual review
<60 / None    122     No match (orphan records)
─────────────────────────────────
Total         983
```

---

## Merge Precedence Rules

When field values conflict between sources, apply these precedence rules:

| Field | Preferred Source | Reason |
|-------|-----------------|--------|
| Full name | HubSpot | Sales team maintains accurate contact names |
| Email | Keep both; flag primary | Users may have personal + corporate emails |
| Company name | HubSpot | Includes Pty Ltd suffix from ABN lookup |
| Phone | Either (normalised) | Both sources equally reliable |
| ABN | Either (non-null wins) | Only one source typically has it |
| Billing address | Stripe | Verified via payment processing |
| Lifecycle stage | HubSpot | CRM is source of truth for sales pipeline |

---

## Orphan Records

**122 Stripe customers with no HubSpot match** -- these are likely:
- Self-serve sign-ups that bypassed the sales team (89 records, based on plan = "starter")
- Legacy customers from before HubSpot adoption (28 records, signup before 2023-01)
- Test/internal accounts (5 records, email domain matches company domain)

**Recommended action:** Import the 89 self-serve customers into HubSpot as "Product-Led" lifecycle stage. Archive the 5 test accounts. Review the 28 legacy records manually.
