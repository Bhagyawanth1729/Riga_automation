#!/usr/bin/env python3
"""Run the full Riga acceptance gate on one task or a folder."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from riga_lib import find_task_files, parse_task
from validate_submission import check_acceptance, format_report


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    target = Path(argv[0]) if argv else None
    files = find_task_files(target)
    if not files:
        print("No task.md files found.")
        return 2
    failed = 0
    for path in files:
        try:
            task = parse_task(path)
            errors = check_acceptance(task)
        except Exception as exc:  # noqa: BLE001 — report parse failures as gate fails
            print(f"FAIL  {path}  (parse error)")
            print(f"  - {exc}")
            failed += 1
            continue
        print(format_report(task, errors))
        if errors:
            failed += 1
    print(f"\n{len(files) - failed}/{len(files)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
