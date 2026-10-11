#!/usr/bin/env python3
"""Acceptance-bar checks aligned to Riga STEM Guidelines V1.3."""
from __future__ import annotations

import re

from check_latex import check_latex
from check_voice import check_voice
from riga_lib import (
    FORBIDDEN_DNE,
    FORBIDDEN_GUESS,
    FORBIDDEN_PROOF,
    MULTI_QUESTION,
    load_domains,
    load_json,
)

DOMAIN_JUSTIFICATION = [
    r"This problem involves",
    r"The problem also involves",
    r"However,",
]


def check_acceptance(task: dict) -> list[str]:
    errors: list[str] = []
    meta = task["meta"]
    domains = load_domains()
    problem_types = load_json("problem_types.json")["shared_forms"]
    answer_types = load_json("answer_types.json")

    field = meta.get("field")
    domain = meta.get("domain")
    subdomain = meta.get("subdomain")
    if field not in domains:
        errors.append(f"field must be Biology, Chemistry, or Physics (got {field!r})")
    else:
        try:
            platform = load_json("platform_domains.json")
        except FileNotFoundError:
            platform = {}
        live = platform.get(field)
        if live and domain not in live:
            errors.append(
                f"domain {domain!r} is not on the live {field} dropdown. Use one of: "
                + ", ".join(live)
            )
        elif domain not in domains[field]:
            errors.append(f"domain {domain!r} is not a {field} domain")
        elif subdomain not in domains[field].get(domain, []):
            errors.append(
                f"subdomain {subdomain!r} is not under {field} / {domain}"
            )

    ptype = meta.get("problem_type")
    if ptype not in problem_types:
        errors.append(f"problem_type {ptype!r} is not an allowed form")
    atype = meta.get("answer_type")
    if field in answer_types and atype not in answer_types[field]:
        errors.append(f"answer_type {atype!r} is not valid for {field}")

    concepts = meta.get("concepts") or []
    if not isinstance(concepts, list) or not (1 <= len(concepts) <= 5):
        errors.append("concepts must be a list of 1 to 5 items")
    else:
        for c in concepts:
            if not isinstance(c, str) or not c.strip() or len(c.split()) > 8:
                errors.append(
                    f"concept {c!r} should be a short noun phrase (not a sentence)"
                )
            if re.search(r"replace-me|TODO|TBD|xxx", str(c), re.I):
                errors.append(f"concept {c!r} is still a placeholder")

    blob = "\n".join(
        [
            task["problem"],
            task["domain_explanation"],
            task["answer"],
            *(s["text"] for s in task["steps"]),
        ]
    )
    if re.search(
        r"\{\{|REPLACE|<key elements>|<domain and subdomain>|replace-me|"
        r"Write one self-contained question here",
        blob,
    ):
        errors.append("Draft still contains template placeholders — finish the science")

    problem = task["problem"]
    if not problem or len(problem) < 80:
        errors.append("Problem is too short to be self-contained and original")
    if FORBIDDEN_PROOF.search(problem):
        errors.append("Prompt looks like a proof ('show that' / 'prove' / 'verify')")
    if FORBIDDEN_GUESS.search(problem):
        errors.append("Prompt looks guessable (MC / T-F / yes-no)")
    if FORBIDDEN_DNE.search(problem) or FORBIDDEN_DNE.search(task["answer"]):
        errors.append("DNE / 'does not exist' is not a valid Riga answer")
    if MULTI_QUESTION.search(problem):
        errors.append("Prompt appears to ask more than one question")
    if problem.count("?") > 2:
        errors.append("Too many question marks — keep a single closed question")
    if not re.search(
        r"(report|give|find|compute|evaluate|determine|express|write|identify)",
        problem,
        re.I,
    ):
        errors.append(
            "Problem should explicitly ask for one checkable object (find/compute/report/...)"
        )
    if not re.search(
        r"(express|report|give|round|significant|decimal|in terms of|exact|units?)",
        problem,
        re.I,
    ):
        errors.append(
            "Clear answer format is missing — state exact form, rounding, variables, or units"
        )

    expl = task["domain_explanation"]
    for needle in DOMAIN_JUSTIFICATION:
        if needle not in expl:
            errors.append(
                f"Domain Explanation must include the required sentence starting '{needle}'"
            )

    steps = task["steps"]
    if len(steps) < 3:
        errors.append("Worked solution needs at least 3 substantial steps")
    expected = list(range(1, len(steps) + 1))
    got = [s["n"] for s in steps]
    if got != expected:
        errors.append(f"Steps must be numbered 1..n in order (got {got})")
    for step in steps:
        if len(step["text"]) < 40:
            errors.append(f"{step['title']} looks like a micro-step (too short)")
        if re.search(r"\b(Step \d+\.[a-z]|substep|Part [A-Z])\b", step["text"], re.I):
            errors.append(f"{step['title']} contains a step-within-a-step")
        if re.search(r"\b(clearly|it follows|note that)\b", step["text"], re.I):
            if len(step["text"]) < 160:
                errors.append(
                    f"{step['title']}: 'clearly/note that/it follows' needs an actual argument"
                )

    answer = task["answer"]
    if FORBIDDEN_DNE.search(answer):
        errors.append("Answer cannot be DNE")
    # Units: if problem omits units and answer is numeric, units should appear
    numeric_answer = bool(re.search(r"[0-9]", answer))
    problem_asks_units = bool(re.search(r"\\mathrm\{|\\text\{|units?", problem, re.I))
    dimensionless = bool(
        re.search(
            r"\b(frequency|probabilit|proportion|fraction|decimal|dimensionless)\b",
            problem,
            re.I,
        )
    )
    answer_has_units = bool(
        re.search(r"\\mathrm\{|\\text\{|\\,\\mathrm|\\,\s*\\text", answer)
    )
    if numeric_answer and not problem_asks_units and not answer_has_units and not dimensionless:
        if meta.get("answer_type") in {
            "Quantity with units",
            "Concentration or quantity with units",
            "Physical quantity with units",
        }:
            errors.append(
                "Numeric answer needs units in the Answer field when the prompt does not specify them"
            )

    if meta.get("status") == "ready" and meta.get("independently_verified") is not True:
        errors.append(
            "status=ready requires independently_verified: true after you recomputed every equality"
        )

    errors.extend(check_latex(task))
    errors.extend(check_voice(task))
    return errors


def format_report(task: dict, errors: list[str]) -> str:
    name = task["meta"].get("id", task["path"])
    if not errors:
        return f"PASS  {name}"
    lines = [f"FAIL  {name}  ({len(errors)} issue(s))"]
    for err in errors:
        lines.append(f"  - {err}")
    return "\n".join(lines)
