"""LaTeX helper utilities."""
from __future__ import annotations

import re


def strip_comments(text: str) -> str:
    """Remove % comments (respecting escaped \\%)."""
    out_lines = []
    for line in text.splitlines():
        # find first un-escaped %
        idx = None
        for i, ch in enumerate(line):
            if ch == "%" and (i == 0 or line[i - 1] != "\\"):
                idx = i
                break
        out_lines.append(line if idx is None else line[:idx])
    return "\n".join(out_lines)


def count_math_items(text: str) -> dict:
    """Rough complexity metrics for a LaTeX string."""
    text = strip_comments(text)
    return {
        "inline_math": len(re.findall(r"(?<!\\)\$[^$]+$", text, re.M)),
        "display_math": text.count("$$") // 2,
        "equations": len(re.findall(r"\\begin\{equation", strip_comments(text))),
        "braces_depth": _max_brace_depth(text),
        "length": len(text),
    }


def _max_brace_depth(text: str) -> int:
    depth = max_depth = 0
    for i, ch in enumerate(text):
        if ch == "{" and (i == 0 or text[i - 1] != "\\"):
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == "}" and (i == 0 or text[i - 1] != "\\"):
            depth -= 1
    return max_depth


def extract_symbols(text: str) -> set[str]:
    """All \\command tokens used (for undefined-notation checks)."""
    return set(re.findall(r"\\([a-zA-Z]+)", strip_comments(text)))


def wrap_answer(answer_core: str) -> str:
    """Wrap bare answer core in $...$ exactly once (Answer field format)."""
    core = answer_core.strip()
    core = core.strip("$").strip()
    if "\\boxed" in core:
        core = core.replace("\\boxed", "")
        core = core.strip("{}")
    return f"${core}$"


def make_final_step_boxed(answer_core: str) -> str:
    """Exact required final phrase per the Answer Formatting Guide."""
    core = answer_core.strip().strip("$").strip()
    return f"Final Answer: $\\boxed{{{core}}}$"
