# Riga

Local authoring desk for Snorkel **Project Riga** — original Physics, Chemistry, and Biology problems that stump frontier models and survive human Quality Review.

Guidelines: V1.3, 16 July 2026 (`docs/guidelines/Riga-Project-Guidelines-V1.3.pdf`).

Draft it here, then paste it into `EK_Riga_Production / Riga Submission`. This repository has never been submitted to Snorkel. I’ve collected all the necessary documentation to train the automation system.
## Start

```bash
python3 scripts/new_task.py --field Chemistry --domain Electrochemistry --subdomain "Nernst equation" --title "working title"
python3 scripts/qa_gate.py submissions/drafts/<folder>/task.md
python3 scripts/preflight.py submissions/drafts/<folder>/task.md
python3 scripts/promote.py submissions/drafts/<folder>/task.md ready
python3 scripts/paste_ready.py submissions/ready/<folder>/task.md
```

Paste `PASTE.md` field-by-field using [`docs/platform/ui-fields.md`](docs/platform/ui-fields.md). Do not paste Author Notes.

## What "accepted" means

An item is accepted only after a Snorkel reviewer marks **Accept**. Local `ready` is not Accept. After that happens, move the folder with `promote.py … accepted`.

Formatting density to match: [`docs/examples/gold-harned-cell/`](docs/examples/gold-harned-cell/). Do not clone its skeleton.

## Agent manual

[`AGENTS.md`](AGENTS.md) — operating contract, acceptance bar, UI map, review mode, CoC.

Folder map: [`docs/FOLDER_MAP.md`](docs/FOLDER_MAP.md).
