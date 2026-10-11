# What actually gets items sent back

Compiled from V1.3 error categories and review-process updates.

| Category | Typical cause | Fix before you submit |
|---|---|---|
| Not Self-Contained | Constant, table, or convention left in your head | Put it in the prompt |
| Non-Unique Answer | Two conventions both legal | Name the convention |
| Too Computational | Series, 8-significant-figure slog, CAS algebra | Redesign so a calculator closes it |
| Multi-Part Question | "Also find" / (a)(b) | One object |
| Guessable | Binary or 4-option shape | Ask for a number or expression |
| Domain Beyond Scope | Math-as-math, CS, engineering design | Stay in Bio / Chem / Phys |
| Wrong Answer | Arithmetic or $n$ / sign error | Recompute hide-the-answer |
| Unjustified Claims | "clearly" with no argument | Write the missing line or delete the claim |
| Unstated Assumption | Ideal gas, infinite bath, 5′→3′, $p^\circ=1\,\mathrm{bar}$ | State it |
| Step Error | Final number luckily right | Reviewer will still bounce it |
| Major LaTeX | `\(`, `\chemfig`, missing `Step N`, `\boxed` in Answer | Run `qa_gate.py` |
| Other | Weak domain justification | Use the three-sentence form |

Reviewer test you should run on your own draft: *If I were mean and only had the text, could I get a different legal answer?* If yes, lock the format.
