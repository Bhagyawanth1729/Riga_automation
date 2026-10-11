#!/usr/bin/env python3
"""Human + gate preflight before Quality Review."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from riga_lib import parse_task
from validate_submission import check_acceptance, format_report

CHECKS = [
    "One closed question; unique answer; format stated in the prompt",
    "Every constant, table, and convention is in the prompt",
    "Hid the boxed line and recomputed every displayed equality",
    "Last step ends Final Answer: $\\boxed{...}$; Answer is $...$ with the same payload",
    "Domain is the subject; three-sentence justification names a runner-up",
    "Voice does not read as templated; skeleton differs from the last draft",
    "Both hard models will be run; 'No Response' will be re-run, not counted as a miss",
    "In-App LaTeX check will be run; Automated Checks Only before Quality Review",
]


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print("usage: preflight.py path/to/task.md")
        return 2
    path = Path(argv[0])
    task = parse_task(path)
    errors = check_acceptance(task)
    print(format_report(task, errors))
    print()
    print("Author checklist (confirm before paste):")
    for i, line in enumerate(CHECKS, 1):
        print(f"  [{i}] {line}")
    meta = task["meta"]
    print()
    print(f"status={meta.get('status')}  independently_verified={meta.get('independently_verified')}")
    if errors:
        print("\nGate failed. Do not paste.")
        return 1
    if meta.get("independently_verified") is not True:
        print("\nSet independently_verified: true only after you recomputed.")
        return 1
    print("\nLocal gate is clean. Promote to ready, emit PASTE.md, then run the platform models.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
