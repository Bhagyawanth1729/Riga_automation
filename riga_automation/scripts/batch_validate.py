#!/usr/bin/env python
"""Batch-validate all submissions in a directory.

Usage:
    python scripts/batch_validate.py --input data/problems/
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "config"))

from src.validators.riga_validator import RigaValidator
from src.models.problem import RigaProblem
from domain_registry import DOMAIN_REGISTRY


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default=str(ROOT / "data" / "problems"))
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    validator = RigaValidator(domain_registry=DOMAIN_REGISTRY)
    in_dir = Path(args.input)
    files = sorted(in_dir.glob("*.json"))
    if not files:
        print(f"No .json submissions found in {in_dir}")
        return 0

    total_err = total_warn = 0
    for f in files:
        try:
            p = RigaProblem.from_json(str(f))
        except Exception as e:
            print(f"[LOAD ERROR] {f.name}: {e}")
            total_err += 1
            continue
        issues = validator.validate(p)
        errs = [i for i in issues if i.severity == "error"]
        warns = [i for i in issues if i.severity == "warning"]
        total_err += len(errs)
        total_warn += len(warns)
        print(f"\n{f.name}: {len(errs)} error(s), {len(warns)} warning(s)")
        for i in issues:
            print(f"  [{i.severity}] {i.category.value}: {i.message}")
            if i.suggestion:
                print(f"       -> {i.suggestion}")

    print(f"\n{'=' * 60}")
    print(f"TOTAL: {len(files)} file(s), {total_err} error(s), {total_warn} warning(s)")
    return 2 if total_err else (1 if args.strict and total_warn else 0)


if __name__ == "__main__":
    sys.exit(main())
