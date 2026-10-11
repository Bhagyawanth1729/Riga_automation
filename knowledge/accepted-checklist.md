# What an Accept looks like

An item is **accepted** only after a human Quality Reviewer on Snorkel marks Accept. Local `status: ready` is not Accept. Do not invent files in `submissions/accepted/` until that happens.

## Author-side bar (must all be true)

1. Original closed question; unique checkable answer; format stated.
2. Self-contained; no contest clone; no Harned-cell skeleton clone.
3. ≥3 substantial steps; last line `Final Answer: $\boxed{...}$`; Answer `$...$`.
4. Every displayed equality recomputed; `independently_verified: true`.
5. `qa_gate.py` PASS; In-App LaTeX check run.
6. At least one hard model misses consistently; official difficulty ≤88% on ≥1 model.
7. Domain/subdomain are the subject; three-sentence justification names a runner-up.
8. Voice reads as a working scientist, not a chatbot.

## Reviewer-side bar (when you review)

1. You solved it yourself; steps survive with the boxed line hidden.
2. Labels are not obviously wrong.
3. Difficulty is assumed sufficient unless blatantly trivial or a wording trick.
4. Decision is Accept / Needs Revision / Reject, with error categories named on send-back.

Local gold for *formatting density*: `docs/examples/gold-harned-cell/`.
