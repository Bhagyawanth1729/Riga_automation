#!/usr/bin/env python3
"""LaTeX and Riga formatting checks for a parsed task."""
from __future__ import annotations

import re

from riga_lib import (
    ANSWER_WRAP_RE,
    BOXED_IN_ANSWER,
    FINAL_BOXED_RE,
    FORBIDDEN_CHEMFIG,
    FORBIDDEN_DELIMS,
    FORBIDDEN_ITEM,
    FORBIDDEN_MD_BOLD_STEP,
    KATEX_ONLY,
)


def _scan(label: str, text: str) -> list[str]:
    errors = []
    if FORBIDDEN_DELIMS.search(text):
        errors.append(f"{label}: use $...$ or $$...$$, never \\( \\) or \\[ \\]")
    if FORBIDDEN_CHEMFIG.search(text):
        errors.append(f"{label}: \\chemfig is not supported")
    if FORBIDDEN_ITEM.search(text):
        errors.append(f"{label}: do not use \\item for lists")
    if FORBIDDEN_MD_BOLD_STEP.search(text):
        errors.append(f"{label}: do not bold steps with **...**")
    if KATEX_ONLY.search(text):
        errors.append(f"{label}: KaTeX-only commands (e.g. \\lang) are forbidden; use \\langle")
    if re.search(r"<=|>=", text) and not re.search(r"\\leq|\\geq|\\le|\\ge", text):
        errors.append(f"{label}: use \\leq / \\geq instead of <= / >=")
    if re.search(r"(?<!\\)\{[0-9,\s]+\}", text) and "\\{" not in text:
        # only flag obvious unescaped set braces like {1, 2, 3}
        if re.search(r"\{[0-9]", text) and not re.search(r"\\boxed|\\frac|\\sqrt", text):
            errors.append(f"{label}: escape visible set braces as \\{{ ... \\}}")
    return errors


def check_latex(task: dict) -> list[str]:
    errors: list[str] = []
    errors.extend(_scan("Problem", task["problem"]))
    errors.extend(_scan("Domain Explanation", task["domain_explanation"]))
    for step in task["steps"]:
        errors.extend(_scan(step["title"], step["text"]))
        if not re.match(rf"Step {step['n']}\b", step["text"]) and not step["text"].startswith(
            f"Step {step['n']}"
        ):
            # Platform requires each step to start with "Step #"
            if not step["text"].lstrip().startswith(f"Step {step['n']}"):
                errors.append(
                    f"{step['title']}: step body must start with 'Step {step['n']}'"
                )
    if task["steps"]:
        last = task["steps"][-1]["text"].rstrip()
        if not FINAL_BOXED_RE.search(last):
            errors.append(
                "Last step must end with exactly: Final Answer: $\\boxed{...}$"
            )
    answer = task["answer"].strip()
    if BOXED_IN_ANSWER.search(answer):
        errors.append("Answer field must not contain \\boxed")
    if not ANSWER_WRAP_RE.match(answer):
        errors.append("Answer field must be wrapped in $...$ only")
    if "\\ce{" not in task["problem"] + "".join(s["text"] for s in task["steps"]):
        pass  # mhchem is allowed, not required
    return errors
