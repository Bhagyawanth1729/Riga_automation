# Give me a task

Read this file first, then `AGENTS.md`, then `.cursor/rules/`. When the user says "give me a task" (or anything close), do the work below. Do not ask them to restate the rules.

## What you produce

One original Physics, Chemistry, or Biology problem that a working PhD could have set for a qualifying exam, written so a frontier model misses for a real scientific reason.

Official difficulty target: at most 88% success on at least one of the two hard models. Design the miss first. The model should drop a real applicability condition. It should not lose because the English is foggy.

Allowed pressure (pick one, and make the science new):

- activity or fugacity given, then dropped from \(Q\)
- wrong electron count \(n\)
- small-\(x\) used when \(x\) is not small
- identical-particle sign (fermion vs boson)
- a stated non-default standard state (\(1\,\mathrm{m}\) vs \(1\,\mathrm{M}\) vs \(1\,\mathrm{bar}\))
- which operator is actually measured
- reading frame after a stated splice
- a neglected junction, coincidence, or generation condition

Forbidden: ambiguous wording, hidden definitions, riddles, multiple choice, true/false, yes/no, proof language (`show that`, `prove`, `verify that`), contest problems with the numbers swapped, and clones of `docs/examples/gold-harned-cell/` or of any earlier draft.

Rotate the scientific object. If the last problem opened with a cell diagram, the next one must not. Use a rate law, a Hamiltonian, a pedigree, a sequence plus a code table, a circuit with element values, or enzyme numbers.

## How to write it

Follow `AGENTS.md` exactly.

1. Pick one field, domain, and subdomain from `data/catalogs/domains.json`. If `data/catalogs/platform_domains.json` lists that field, the domain must be on that list.
2. Design the answer first in `scratch.md`. One closed, unique, hand-checkable object.
3. Write the prompt so a competent human can solve it from the text plus ordinary graduate knowledge. Put every constant, table row, and convention in the prompt.
4. At least three substantial `Step N` steps. Last step ends with `Final Answer: $\boxed{...}$`. The answer field is `$...$` with no `\boxed`.
5. Domain justification is exactly three sentences: This problem involves / The problem also involves / However.
6. Voice: a specific working scientist, not a chatbot. Open on the physical system and the given data. If `scripts/check_voice.py` flags a phrase, rewrite that sentence from scratch.
7. After any `task.md` edit, run `python3 scripts/qa_gate.py` on that file and fix every failure. Recompute every equality yourself before setting `independently_verified: true`.

Do not paste `Author Notes` into the platform. Do not submit to Snorkel. The user pastes.

## Files in this kit

- `AGENTS.md` — operating contract
- `.cursor/rules/` — acceptance bar, originality, voice, LaTeX, field rules, review mode
- `docs/guidelines/` — V1.3 guidelines and the extracted text
- `docs/platform/ui-fields.md` — paste order
- `knowledge/model-stump-patterns.md` — legal miss modes
- `data/catalogs/` — domains, problem types, answer types
- `templates/` — `task.md`, `scratch.md`
- `scripts/` — `new_task.py`, `qa_gate.py`, `preflight.py`, `promote.py`, `paste_ready.py`

Finished problems are not in this kit. Write a new one. Do not reconstruct one from memory of another expert's item.
