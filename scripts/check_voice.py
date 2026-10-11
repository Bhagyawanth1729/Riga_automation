#!/usr/bin/env python3
"""Flag LLM-tell phrasing that reviewers treat as templated / non-expert."""
from __future__ import annotations

import re

from riga_lib import AI_TELLS


def check_voice(task: dict) -> list[str]:
    blobs = [task["problem"], task["domain_explanation"]]
    blobs.extend(step["text"] for step in task["steps"])
    text = "\n".join(blobs)
    errors = []
    for pattern in AI_TELLS:
        hit = re.search(pattern, text, re.I)
        if hit:
            errors.append(
                f"Voice: AI-tell / templated phrasing '{hit.group(0)}' — rewrite as a working scientist would"
            )
    # Repeated sentence openers
    sentences = re.findall(r"^[A-Z][^.?\n]{0,40}", text, re.M)
    if sentences:
        firsts = [s.split()[0] if s.split() else "" for s in sentences]
        for word in {"We", "This", "Thus", "Therefore", "Hence"}:
            if firsts.count(word) >= 4:
                errors.append(
                    f"Voice: '{word}' opens {firsts.count(word)} sentences — vary rhythm"
                )
    # Lecture/tutorial cadence
    if re.search(r"\b(remember that|keep in mind that|as mentioned above)\b", text, re.I):
        errors.append("Voice: tutorial cadence — drop the teaching asides")
    if re.search(r"\b(amazing|fascinating|beautiful result)\b", text, re.I):
        errors.append("Voice: booster adjectives read as generated prose")
    # Over-symmetric three-part lists in the problem
    if len(re.findall(r", and ", task["problem"])) >= 3:
        errors.append(
            "Voice: problem stacks too many ', and' lists — write one concrete setup"
        )
    return errors
