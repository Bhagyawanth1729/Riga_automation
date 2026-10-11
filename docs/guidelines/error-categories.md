# Error categories (review)

When sending Needs Revision or Reject, select every category that applies and **name each one** in the notes with a concrete fix.

## Prompt

| Category | Definition |
|---|---|
| Not Self-Contained | Missing definitions, formulas, or context needed to attempt the problem |
| Non-Unique Answer | As written, the prompt would yield multiple valid answers |
| Too Computational | Would require code or machine computation to verify |
| Multi-Part Question | Asks multiple questions or multiple parts of a single question |
| Guessable | Multiple-choice, true-false, or otherwise easily guessed |
| Domain Beyond Project Scope | STEM domain outside Physics, Chemistry, or Biology |

## Answer and solution steps

| Category | Definition |
|---|---|
| Wrong Answer | Wrong answer or flawed, inaccurate reasoning |
| Unjustified or Unsupported Claims | Skips steps or asserts without justification so the work cannot be reproduced |
| Unstated Assumption | An assumption that would change the answer if changed is not stated and justified |
| Step Error | An individual step is wrong but the final answer is still correct |

## Any section

| Category | Definition |
|---|---|
| Major LaTeX or Formatting Issues | Wrong delimiters, unsupported commands, missing project-specific formatting |
| Major Grammar or Language Issues | Unclear phrasing or imprecise scientific language that makes intent ambiguous |
| Other | Wrong domain, closed quota, missing justification, or anything else |

Minor LaTeX/grammar in **solution steps**: fix in review; do not send back for those alone. If you did fix them while sending back for other reasons, note the edits.

Reject only for clear spam, low effort, or completely ignoring project rules.

Machine-readable: `data/catalogs/error_categories.json`.
