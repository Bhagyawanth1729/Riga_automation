# riga_automation — Agent Notes

## Purpose
Automation toolkit for **Project Riga (EK_Riga_Production)**: helps Expert Contributors
author original STEM problems (Biology, Chemistry, Physics) in LaTeX that stump frontier
LLMs, with validation, classification, and export.

## ⚠️ Critical rule: no LLM content in submissions
The tools scaffold structure and enforce rules, but **all prompt/solution content must be
written by the human expert**. Templates only provide structural placeholders and
failure-pattern checklists. Per the Code of Conduct: LLM-generated content, plagiarism,
templated/spam submissions, and inappropriate conduct can result in removal. Automated
conduct signals (`conductcheck`) are *review hints*, never automatic rejection.

## Layout
- `config/categories.yaml` — taxonomy (subjects, difficulty, reasoning types, concept levels)
- `config/domain_registry.py` — **canonical** domain/subdomain lists (from Domain Reference)
- `config/llm_failure_patterns.yaml` — stumping patterns library
- `config/code_of_conduct.yaml` — codified conduct rules (spam, plagiarism, LLM-usage, low-AHT, etc.)
- `config/templates/{biology,chemistry,physics}_templates.yaml` — problem template families
- `src/models/problem.py` — `RigaProblem`, `SolutionStep`, `Classification`, `ErrorCategory`
- `src/models/workspace.py` — lifecycle: automated checks → quality review → accepted
- `src/validators/latex_validator.py` — LaTeX + **Appendix formatting** rules
- `src/validators/originality.py` — CoC signals: cross-similarity/spam, corpus plagiarism,
  placeholder residue, LLM boilerplate
- `src/validators/riga_validator.py` — all guideline checks (self-contained, no multi-part,
  no guessable, ≥3 steps, Step #, Final Answer: $\boxed{...}$, Answer exact match, concepts 1–5,
  domain justification, stumps verification)
- `src/validators/llm_tester.py` — frontier-model difficulty testing ("no response ≠ wrong")
- `src/generators/` — template scaffold + variation engine
- `src/exporters/` — LaTeX doc, PDF compile (needs MiKTeX/TeX Live), JSONL/CSV
- `src/cli/main.py` — click CLI (`list`, `scaffold`, `validate`, `export`, `stumptest`,
  `concepts`, `checklist`)
- `scripts/` — direct entry points (create_problem, batch_validate, export_dataset)
- `tests/` — pytest suite including Appendix formatting and full-guideline cases

## Non-negotiable formats (Answer Formatting Guide)
- Final solution step ends with exactly: `Final Answer: $\boxed{...}$
- Answer field: ONLY `$\{answer\}$` — no `\boxed`, no "Final Answer" wording, exact copy of
  the boxed content (spaces/punctuation/order identical)
- Concepts: 1–5 fields, single line each, no bullet/hyphen/number prefixes
- LaTeX: only `$...$` and `$$...$$` (never `\(...\)` / `\[...\]`); no `\item[]`; no `**bold**`;
  mhchem ✅ / chemfig ❌; `\leq` not `<=`; escaped braces `\{1,2,3\}`; polynomials in
  descending exponent order; rounding instructions in prompt when decimals used
- Problem: self-contained (no paper/table/figure references, no single-paper results),
  single question, not guessable, not code-computable, "does not exist" not a valid answer
- Solution: ≥3 substantial steps each starting `Step #`; no micro-steps; assumptions explicit

## Commands
```
pip install -r requirements.txt
python -m src.cli.main list                # templates
python -m src.cli.main list --domains      # domain registry
python scripts/create_problem.py --subject physics
python scripts/create_problem.py --template physics_qo_bayesian_beamsplitters
python scripts/batch_validate.py --input data/problems
python scripts/export_dataset.py --input data/reviewed --format tex,pdf,jsonl
python -m src.cli.main stumptest data/problems/<file>.json --models openai:gpt-4.1 --trials 5
python -m src.cli.main conductcheck data/problems            # anti-spam/plagiarism signals
python -m src.cli.main conductcheck data/problems --corpus data/known_corpus
pytest tests/ -q
```

## Data
- drafts/new: `data/problems/`  •  accepted: `data/reviewed/`  •  exports/reports: `data/exports/`, `data/reports/`
