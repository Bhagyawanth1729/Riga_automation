#!/usr/bin/env python3
"""Move a submission folder between lanes and update status in task.md."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from riga_lib import ROOT, parse_task

LANES = ("drafts", "ready", "submitted", "accepted", "needs_revision", "rejected")
STATUS = {
    "drafts": "draft",
    "ready": "ready",
    "submitted": "submitted",
    "accepted": "accepted",
    "needs_revision": "needs_revision",
    "rejected": "rejected",
}


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) != 2:
        print("usage: promote.py path/to/task.md <lane>")
        print("lanes:", ", ".join(LANES))
        return 2
    src = Path(argv[0]).resolve()
    dest_lane = argv[1]
    if dest_lane not in LANES:
        print(f"unknown lane {dest_lane!r}")
        return 2
    if src.name != "task.md" or not src.exists():
        print("first argument must be an existing task.md")
        return 2

    folder = src.parent
    submissions = ROOT / "submissions"
    dest_root = submissions / dest_lane
    dest_root.mkdir(parents=True, exist_ok=True)
    dest = dest_root / folder.name
    if dest.exists() and dest.resolve() != folder.resolve():
        print(f"destination already exists: {dest}")
        return 1

    task = parse_task(src)
    if dest_lane == "ready":
        if task["meta"].get("independently_verified") is not True:
            print("ready requires independently_verified: true")
            return 1
        from validate_submission import check_acceptance

        errors = check_acceptance(task)
        if errors:
            print("gate is not clean:")
            for e in errors:
                print(f"  - {e}")
            return 1
    if dest_lane == "accepted":
        print(
            "accepted is for items a Snorkel reviewer marked Accept. "
            "Only promote here after that happens on the platform."
        )

    text = src.read_text()
    new_status = STATUS[dest_lane]
    text2, n = re.subn(
        r"^status:\s*\S+",
        f"status: {new_status}",
        text,
        count=1,
        flags=re.M,
    )
    if n != 1:
        print("could not update status: in frontmatter")
        return 1
    src.write_text(text2)

    if folder.parent.resolve() != dest_root.resolve():
        folder.rename(dest)
        print(dest / "task.md")
    else:
        print(src)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
