---
id: {{ID}}
status: draft
field: {{FIELD}}
domain: {{DOMAIN}}
subdomain: {{SUBDOMAIN}}
problem_type: Exact computation
answer_type: Exact scalar
concepts:
  - replace-me
  - replace-me
routing: Automated Checks Only
independently_verified: false
working_title: {{TITLE}}
---

## Problem

Write one self-contained question here. State the answer format (exact expression, units, rounding). Do not ask a second question.

## Domain Explanation

This problem involves <key elements>, which are part of <domain and subdomain>.
The problem also involves <additional elements>, which are part of <next-best domain and/or subdomain>.
However, <why those are not core, or less advanced than the chosen pair>.

## Step 1

Step 1
Set the governing relation and name every symbol. Justify any assumption that would change the answer if dropped.

## Step 2

Step 2
Do the main reduction. Recompute every displayed equality. If you write "from Step 1", say Step 1.

## Step 3

Step 3
Close the algebra or arithmetic and report the object the prompt asked for.

Final Answer: $\boxed{REPLACE}$

## Answer

$REPLACE$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [ ] Hid the boxed line and recomputed every displayed equality
- [ ] `python3 scripts/qa_gate.py` PASS
- [ ] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- 
