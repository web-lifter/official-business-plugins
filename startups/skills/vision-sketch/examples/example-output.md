---
title: Vision sketch
slug: vision-sketch
type: vision
status: active
owner: contractiq
created: 2026-04-02
updated: 2026-04-09
---

# Vision sketch — ContractIQ

## Customers' top problems

1. Sole in-house counsel at AU/NZ mid-market companies (50–500 staff) sit down at 9pm on a Thursday to review a 40-page commercial MSA so the business can sign on Friday morning. Observable: calendars show after-hours blocks on contract days; counsel arrive Friday tired with marked-up Word docs.
2. The same counsel get blamed 12–18 months later for an auto-renewal clause that auto-billed the company AU$50k–AU$200k. Observable: incident reports, finance-team escalations naming a specific contract clause that was "missed in review".
3. Once a contract is signed, no system tracks the obligations it created. Observable: counsel maintain personal Excel sheets of "buyer shall…" clauses; obligations are surfaced only when finance or operations stumbles on them.

## How our idea helps

1. When a 40-page MSA hits the inbox, ContractIQ classifies every clause against the 14 highest-risk AU/NZ categories and produces a redline + one-page negotiation brief, so the counsel spends 20 minutes reviewing instead of 3 hours.
2. When a clause is auto-renewing, uncapped, or has a non-standard governing-law surprise, ContractIQ flags it before signature with a plain-English explanation, so the counsel doesn't miss it under deadline pressure.
3. When a contract is signed, ContractIQ extracts every "buyer shall…" obligation into a calendar plus dependency graph, so the team has a defensible obligation tracker without anyone re-typing the contract.

## Day-in-the-life: before vs after

**Before ContractIQ.** Priya's counterpart at a 180-staff Sydney health-tech is the only lawyer in the business. On Thursday afternoon the head of partnerships drops a 38-page reseller MSA from a US vendor into Slack and asks for sign-off "by tomorrow morning ideally". She opens it in Word, makes a coffee, and starts reading. By 8pm she's marked up clauses 1–22 and is tired. She emails the partnerships lead at 11:14pm with redlines on the indemnity, liability cap, and termination-for-convenience clauses but misses an auto-renewal in clause 31 because she's skimming. The contract is signed Friday. 14 months later the vendor invoices AU$78,000 for the next auto-renewed year; the partnerships lead, finance, and Priya's counterpart spend a fortnight trying to extract the company from it. The CFO is annoyed.

**After ContractIQ.** Thursday 4pm she uploads the same MSA. By 4:08pm ContractIQ has flagged 11 issues: 2 critical (uncapped liability, 36-month auto-renewal in clause 31), 4 high (indemnity, governing-law, audit rights, modern-slavery reporting), and 5 medium. She walks through the critical and high findings, accepts 9 and rejects 2 (the auto-renewal is acceptable to the business in this case, but she wants a notice clause added). She produces a tracked-changes redline plus a one-page negotiation brief by 5:20pm. Friday morning she's in front of the business owner at 9am with answers, not questions. The obligations tracker auto-populates after signature; finance sees the auto-renewal trigger 60 days before it fires.

## What we are NOT testing yet

1. We are not yet claiming the AU/NZ-specific clause classifier generalises to litigation or employment contracts; the corpus is commercial MSAs only.
2. We are not yet claiming a self-serve free tier; pricing assumes a seat-based subscription with a paid pilot path.
3. We are not yet claiming an enterprise CLM integration; ContractIQ is a pre-execution review tool, not a contract lifecycle manager.
