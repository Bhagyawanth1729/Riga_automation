#!/usr/bin/env python
"""Create a new problem scaffold interactively.

Usage:
    python scripts/create_problem.py --subject chemistry --difficulty hard
    python scripts/create_problem.py --template chem_tst_tunneling
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.cli.main import main

if __name__ == "__main__":
    # route to 'scaffold' when --template given, else interactive 'list'
    argv = sys.argv[1:]
    if "--template" in argv:
        i = argv.index("--template")
        sys.argv = ["create_problem", "scaffold", argv[i + 1]] + [
            a for a in argv if argv.index(a) != i and argv.index(a) != i + 1]
    else:
        # default: wizard = list templates filtered by flags, then prompt
        subj = None
        diff = "hard"
        for i, a in enumerate(argv):
            if a == "--subject" and i + 1 < len(argv):
                subj = argv[i + 1]
            if a == "--difficulty" and i + 1 < len(argv):
                diff = argv[i + 1]
        from src.generators.template_generator import TemplateGenerator
        gen = TemplateGenerator()
        print("Available templates" + (f" for {subj}:" if subj else ":"))
        for t in gen.list_templates(subj):
            print(f"  [{t['id']}] {t['name']} — difficulty: {t.get('difficulty_range')}")
        print("\nRe-run with --template <id> to scaffold one.")
        sys.exit(0)
    main()
