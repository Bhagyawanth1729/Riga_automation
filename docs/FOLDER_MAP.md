# Riga local desk — folder map

Source of truth: `docs/guidelines/Riga-Project-Guidelines-V1.3.pdf` (Snorkel V1.3, 16 July 2026).

```
Riga/
├── AGENTS.md                      # operating manual (agent + you)
├── README.md
├── .cursor/
│   ├── hooks.json                 # sessionStart / afterFileEdit / stop QA
│   ├── hooks/
│   │   ├── session-start.py
│   │   ├── after-edit-validate.py
│   │   └── stop-qa.py
│   └── rules/                     # always-on + field-specific
│       ├── 00-riga-core.mdc
│       ├── 10-acceptance-bar.mdc
│       ├── 15-originality-and-stump.mdc
│       ├── 20-human-expert-voice.mdc
│       ├── 25-answer-formatting.mdc
│       ├── 30-latex-and-fields.mdc
│       ├── 40-physics.mdc
│       ├── 41-chemistry.mdc
│       ├── 42-biology.mdc
│       ├── 50-review-mode.mdc
│       └── 60-code-of-conduct.mdc
├── docs/
│   ├── FOLDER_MAP.md              # this file
│   ├── guidelines/
│   │   ├── Riga-Project-Guidelines-V1.3.pdf
│   │   ├── quality-bar.md
│   │   ├── answer-formatting.md
│   │   ├── latex.md
│   │   ├── error-categories.md
│   │   ├── code-of-conduct.md
│   │   └── accepted-examples.md   # PDF examples: inspiration only
│   ├── platform/
│   │   ├── ui-fields.md           # every Snorkel input, paste order
│   │   ├── workflow.md
│   │   └── screenshots/
│   ├── domains/                   # how to pick domain vs runner-up
│   ├── voice/expert-voice.md
│   └── examples/gold-harned-cell/ # formatting density, not a clone source
├── data/catalogs/
│   ├── domains.json               # full PDF tree
│   ├── platform_domains.json      # live Biology dropdown on this account
│   ├── problem_types.json
│   ├── answer_types.json
│   └── error_categories.json
├── knowledge/
│   ├── model-stump-patterns.md
│   ├── rejection-avoidance.md
│   └── accepted-checklist.md
├── schemas/submission.schema.json
├── scripts/
│   ├── new_task.py
│   ├── qa_gate.py
│   ├── preflight.py
│   ├── paste_ready.py
│   ├── promote.py
│   ├── list_catalog.py
│   ├── check_voice.py
│   ├── check_latex.py
│   ├── validate_submission.py
│   └── riga_lib.py
├── templates/
│   ├── task.md
│   ├── scratch.md
│   └── review.md
├── submissions/
│   ├── drafts/ → ready/ → submitted/ → accepted | needs_revision | rejected
│   └── each item: task.md + scratch.md + PASTE.md
└── reviews/                       # when you are the reviewer, not the OA
```

## Paste order on Snorkel (matches platform UI)

1. Left: `Enter your prompt here` → run both hard models (need consistent miss; ≤88% success on ≥1 model for official check)
2. Right: Problem (Prompt) via **Paste from Prompt**
3. Field / Domain / Sub-domain (Biology: use `platform_domains.json`; Genetics and Genomics is **not** on this account)
4. Domain Explanation (three sentences: This problem involves / The problem also involves / However)
5. Worked Solution boxes: each body starts `Step N:` ; last ends `Final Answer: $\boxed{...}$`
6. Answer: `$...$` only, no `\boxed`
7. **Check Accuracy of LaTeX** (mandatory)
8. Problem Type, Answer Type, Concepts (1–5)
9. **Automated Checks Only** first; Quality Review only after green difficulty

## Commands

```bash
python3 scripts/new_task.py --field Biology --domain "Biochemistry and Metabolism" --subdomain "Enzyme kinetics" --title "short title"
python3 scripts/qa_gate.py submissions/drafts/<id>/task.md
python3 scripts/preflight.py submissions/drafts/<id>/task.md
python3 scripts/promote.py submissions/drafts/<id>/task.md ready
python3 scripts/paste_ready.py submissions/ready/<id>/task.md
python3 scripts/list_catalog.py --field Chemistry
```

Never paste `## Author Notes` into Snorkel.
