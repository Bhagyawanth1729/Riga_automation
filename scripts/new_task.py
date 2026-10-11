#!/usr/bin/env python3
"""Scaffold a new Riga submission folder under submissions/drafts/."""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from riga_lib import ROOT, load_domains

TEMPLATE = ROOT / "templates" / "task.md"


def slug(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return text[:48] or "task"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Riga draft task")
    parser.add_argument("--field", required=True, choices=["Biology", "Chemistry", "Physics"])
    parser.add_argument("--domain", required=True)
    parser.add_argument("--subdomain", required=True)
    parser.add_argument("--title", required=True, help="short working title, not the prompt")
    args = parser.parse_args()

    domains = load_domains()
    if args.domain not in domains[args.field]:
        print(f"Unknown domain {args.domain!r} for {args.field}")
        print("Options:", ", ".join(domains[args.field]))
        return 2
    if args.subdomain not in domains[args.field][args.domain]:
        print(f"Unknown subdomain {args.subdomain!r}")
        print("Options:", ", ".join(domains[args.field][args.domain]))
        return 2

    today = dt.date.today().isoformat()
    folder = ROOT / "submissions" / "drafts" / f"{today}-{slug(args.field)}-{slug(args.title)}"
    folder.mkdir(parents=True, exist_ok=False)
    task_id = folder.name
    text = TEMPLATE.read_text()
    replacements = {
        "{{ID}}": task_id,
        "{{FIELD}}": args.field,
        "{{DOMAIN}}": args.domain,
        "{{SUBDOMAIN}}": args.subdomain,
        "{{TITLE}}": args.title,
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    (folder / "task.md").write_text(text)
    scratch = (ROOT / "templates" / "scratch.md").read_text().replace("{{TITLE}}", args.title)
    (folder / "scratch.md").write_text(scratch)
    print(folder / "task.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
