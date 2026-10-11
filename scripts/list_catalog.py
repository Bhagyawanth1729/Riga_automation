#!/usr/bin/env python3
"""Print domains, subdomains, problem types, or answer types."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from riga_lib import load_domains, load_json


def main() -> int:
    parser = argparse.ArgumentParser(description="List Riga catalogs")
    parser.add_argument("--field", choices=["Biology", "Chemistry", "Physics"])
    parser.add_argument("--domain")
    parser.add_argument("--types", action="store_true", help="print problem and answer types")
    args = parser.parse_args()

    if args.types:
        print("Problem types (all fields):")
        for name in load_json("problem_types.json")["shared_forms"]:
            print(f"  - {name}")
        print()
        answers = load_json("answer_types.json")
        fields = [args.field] if args.field else list(answers)
        for field in fields:
            print(f"Answer types ({field}):")
            for name in answers[field]:
                print(f"  - {name}")
            print()
        return 0

    domains = load_domains()
    platform = {}
    try:
        platform = load_json("platform_domains.json")
    except FileNotFoundError:
        pass

    fields = [args.field] if args.field else list(domains)
    for field in fields:
        live = platform.get(field)
        print(f"## {field}")
        if live:
            print(f"(live dropdown: {len(live)} domains)")
        for domain, subs in domains[field].items():
            marker = ""
            if live and domain not in live:
                marker = "  [PDF only — not on this account's dropdown]"
            if args.domain and domain != args.domain:
                continue
            print(f"\n{domain}{marker}")
            for sub in subs:
                print(f"  - {sub}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
