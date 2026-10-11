# Project Riga - Automation System

Automation toolkit for creating STEM problems (Biology, Chemistry, Physics) in LaTeX that challenge frontier LLMs, with built-in validation, classification, and export capabilities.

## Features

- **Problem Generation**: Template-based + adversarial patterns + variation engine
- **LLM Testing**: Automated testing against frontier models to verify difficulty
- **Validation**: LaTeX syntax, reasoning depth (≥3 steps), self-contained check
- **Classification**: Standard taxonomy (subject, difficulty, topic, reasoning_type)
- **Export**: LaTeX + PDF compilation, JSONL dataset format

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Create a new problem interactively
python scripts/create_problem.py --subject physics --difficulty hard

# Validate existing problems
python scripts/batch_validate.py --input data/problems/

# Export to LaTeX + PDF
python scripts/export_dataset.py --format latex,pdf

# Code-of-conduct signals (near-duplicates / plagiarism hints / placeholders)
python -m src.cli.main conductcheck data/problems
```

## Notes
- **Human-authored only.** Scaffolds are starting points — all content is
  written and verified by the expert. LLM-generated content is prohibited
  (attestation per submission; see `config/code_of_conduct.yaml`).
- Final-step format is exactly `Final Answer: $\boxed{...}$`; the Answer field
  is only `$...$` (no `\boxed`), copied verbatim from the boxed content.

## Project Structure

```
riga_automation/
├── config/                 # Configuration files
│   ├── categories.yaml     # Classification taxonomy
│   ├── templates/          # Problem templates by subject
│   └── llm_failure_patterns.yaml  # Known LLM failure modes
├── src/                    # Core source code
│   ├── models/            # Data models
│   ├── generators/        # Problem generation
│   ├── validators/        # Quality validation
│   ├── exporters/         # Export formats
│   └── cli/               # Command-line interface
├── data/                  # Problem storage
│   ├── problems/          # Draft problems
│   ├── reviewed/          # Accepted problems
│   └── exports/           # Exported datasets
└── scripts/               # Entry point scripts
```

## Guidelines Compliance

This system enforces Project Riga requirements:
- ✅ Original, human-authored content (no LLM generation)
- ✅ Minimum 3-step reasoning validation
- ✅ Self-contained, single-part problems
- ✅ Literature-grounded, narrow concepts
- ✅ LLM difficulty verification
- ✅ LaTeX formatting with proper compilation