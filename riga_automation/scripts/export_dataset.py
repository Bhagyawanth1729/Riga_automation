#!/usr/bin/env python
"""Export submissions to LaTeX/PDF and dataset formats.

Usage:
    python scripts/export_dataset.py --input data/reviewed --format latex,pdf,jsonl
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.models.problem import RigaProblem
from src.exporters.latex_exporter import LatexExporter
from src.exporters.dataset_exporter import DatasetExporter


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default=str(ROOT / "data" / "problems"))
    ap.add_argument("--format", default="tex,jsonl",
                    help="comma list: tex,pdf,jsonl,csv")
    ap.add_argument("--out", default=str(ROOT / "data" / "exports"))
    ap.add_argument("--no-solutions", action="store_true")
    args = ap.parse_args()

    problems = []
    for f in sorted(Path(args.input).glob("*.json")):
        try:
            problems.append(RigaProblem.from_json(str(f)))
        except Exception as e:
            print(f"Skip {f.name}: {e}")
    print(f"Loaded {len(problems)} problem(s)")

    for fmt in args.format.split(","):
        fmt = fmt.strip()
        if fmt in ("tex", "pdf", "latex"):
            res = LatexExporter().export(
                problems, args.out, compile_pdf=(fmt == "pdf"),
                include_solutions=not args.no_solutions)
            print("written:", res)
        elif fmt == "jsonl":
            print("written:", DatasetExporter().export_jsonl(problems, args.out))
        elif fmt == "csv":
            print("written:", DatasetExporter().export_csv(problems, args.out))


if __name__ == "__main__":
    main()
