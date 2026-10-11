#!/usr/bin/env python3
"""Shared parsing and catalog helpers for Riga task files."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOGS = ROOT / "data" / "catalogs"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
STEP_HEADER_RE = re.compile(r"^##\s+Step\s+(\d+)\s*$", re.M)
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)

FORBIDDEN_PROOF = re.compile(
    r"\b(show that|prove that|prove\b|verify that|demonstrate that)\b",
    re.I,
)
FORBIDDEN_GUESS = re.compile(
    r"\b(true or false|which of the following|multiple choice|select all that apply|"
    r"yes or no)\b",
    re.I,
)
FORBIDDEN_DNE = re.compile(r"\b(does not exist|\bDNE\b)\b", re.I)
FORBIDDEN_DELIMS = re.compile(r"\\\(|\\\)|\\\[|\\\]")
FORBIDDEN_CHEMFIG = re.compile(r"\\chemfig\b")
FORBIDDEN_ITEM = re.compile(r"\\item\b")
FORBIDDEN_MD_BOLD_STEP = re.compile(r"\*\*Step")
KATEX_ONLY = re.compile(r"\\lang\b")
BOXED_IN_ANSWER = re.compile(r"\\boxed")
FINAL_BOXED_RE = re.compile(
    r"Final Answer:\s*\$\\boxed\{.+\}\$\s*$",
    re.S,
)
ANSWER_WRAP_RE = re.compile(r"^\$[\s\S]+\$$")
MULTI_QUESTION = re.compile(
    r"(\?\s+.+\?)|(?:\bpart\s*\([a-z]\)|\([a-z]\)\s)",
    re.I,
)

AI_TELLS = [
    r"\bin this problem,? we (will|shall)\b",
    r"\bit's important to (note|remember|understand)\b",
    r"\bnote that we can simply\b",
    r"\blet's dive (in|into)\b",
    r"\bdelve into\b",
    r"\btapestry\b",
    r"\bshowcase\b",
    r"\brobust(ness)?\b",
    r"\bleverag(e|ing)\b",
    r"\bin the realm of\b",
    r"\ba comprehensive (overview|understanding)\b",
    r"\bas an ai\b",
    r"\bcertainly[!]\b",
    r"\bwithout further ado\b",
    r"\bin conclusion,?\s+we (have|can)\b",
    r"\bthis demonstrates the power of\b",
    r"\bplay(?:s|ed) a (crucial|pivotal|vital) role\b",
    r"\bit is worth noting that\b",
    r"\bwe can clearly see\b",
    r"\bobviously\b",
    r"\btrivially\b",
    r"\bas we all know\b",
    r"\bfirstly\b",
    r"\bsecondly\b",
    r"\bthirdly\b",
    r"\bin today's world\b",
    r"\bcutting-edge\b",
    r"\bstate-of-the-art\b",
    r"\bin this problem we will\b",
    r"\blet us (now |)consider\b",
    r"\bto summarize\b",
    r"\bin summary, we\b",
    r"\bholistic\b",
    r"\bunderscore(s|d)? the (importance|significance)\b",
]


def load_json(name: str) -> Any:
    return json.loads((CATALOGS / name).read_text())


def load_domains() -> dict:
    path = CATALOGS / "domains.json"
    if not path.exists():
        from _build_domains import main as build

        build()
    return json.loads(path.read_text())


def parse_simple_yaml(block: str) -> dict[str, Any]:
    """Minimal YAML subset: scalars, inline lists, and indented string lists."""
    data: dict[str, Any] = {}
    lines = block.splitlines()
    i = 0
    current_key = None
    current_list: list[str] | None = None
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("  - ") and current_list is not None:
            current_list.append(line[4:].strip().strip('"').strip("'"))
            i += 1
            continue
        if current_list is not None:
            data[current_key] = current_list
            current_list = None
            current_key = None
        if ":" not in line:
            i += 1
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val == "":
            current_key = key
            current_list = []
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [
                p.strip().strip('"').strip("'")
                for p in inner.split(",")
                if p.strip()
            ]
        else:
            if val.lower() in {"true", "false"}:
                data[key] = val.lower() == "true"
            else:
                data[key] = val.strip('"').strip("'")
        i += 1
    if current_list is not None and current_key:
        data[current_key] = current_list
    return data


def split_sections(body: str) -> dict[str, str]:
    matches = list(SECTION_RE.finditer(body))
    sections: dict[str, str] = {}
    for idx, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        sections[title] = body[start:end].strip()
    return sections


def parse_task(path: Path) -> dict[str, Any]:
    raw = path.read_text()
    match = FRONTMATTER_RE.match(raw)
    if not match:
        raise ValueError(f"{path} is missing YAML frontmatter delimited by ---")
    meta = parse_simple_yaml(match.group(1))
    sections = split_sections(match.group(2))
    steps = []
    for title, text in sections.items():
        step_match = re.match(r"Step\s+(\d+)$", title)
        if step_match:
            steps.append({"n": int(step_match.group(1)), "title": title, "text": text})
    steps.sort(key=lambda s: s["n"])
    return {
        "path": str(path),
        "meta": meta,
        "sections": sections,
        "problem": sections.get("Problem", ""),
        "domain_explanation": sections.get("Domain Explanation", ""),
        "steps": steps,
        "answer": sections.get("Answer", "").strip(),
        "notes": sections.get("Author Notes", ""),
    }


def find_task_files(target: Path | None = None) -> list[Path]:
    if target is None:
        roots = [
            ROOT / "submissions" / "drafts",
            ROOT / "submissions" / "ready",
            ROOT / "docs" / "examples",
        ]
        files: list[Path] = []
        for root in roots:
            files.extend(root.rglob("task.md"))
        return sorted(files)
    target = Path(target)
    if target.is_file():
        return [target]
    return sorted(target.rglob("task.md"))
