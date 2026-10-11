"""Riga automation CLI.

Commands:
  scaffold    Create a new problem scaffold from a template
  validate    Validate one or more submission JSON files
  list        List templates / domains / subdomains
  export      Export directory of submissions to LaTeX/PDF/JSONL/CSV
  concepts    Print concepts formatting rules
  stumptest   Run LLM difficulty test for a submission
  checklist   Print the final submission checklist
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from ..models.problem import RigaProblem, ReviewStatus
from ..generators.template_generator import TemplateGenerator
from ..generators.variation_engine import VariationEngine
from ..validators.riga_validator import RigaValidator
from ..validators.llm_tester import LLMTester
from ..validators.originality import OriginalityChecker
from ..exporters.latex_exporter import LatexExporter
from ..exporters.dataset_exporter import DatasetExporter
from ..utils.file_utils import ensure_dir, slugify

console = Console()

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "config"))
from domain_registry import DOMAIN_REGISTRY   # noqa: E402


@click.group()
def cli():
    """Project Riga submission automation toolkit."""
    pass


# ---------------- list ----------------

@cli.command()
@click.option("--subject", type=click.Choice(["biology", "chemistry", "physics"]))
@click.option("--domains", is_flag=True, help="List domains/subdomains instead of templates")
def list(subject, domains):
    """List available templates or domains."""
    if domains:
        subjects = [subject] if subject else DOMAIN_REGISTRY.keys()
        for s in subjects:
            console.rule(f"[bold]{s.upper()}")
            for dom, subs in DOMAIN_REGISTRY.get(s, {}).items():
                console.print(f"[cyan]{dom}[/cyan]: {', '.join(subs)}")
        return
    gen = TemplateGenerator()
    table = Table("id", "subject", "name", "difficulty", "failure patterns")
    for t in gen.list_templates(subject):
        table.add_row(t["id"], t["subject"], t["name"],
                      "/".join(t.get("difficulty_range", [])),
                      ", ".join(t.get("failure_patterns", []))[:80])
    console.print(table)


# ---------------- scaffold ----------------

@cli.command()
@click.argument("template_id")
@click.option("--difficulty", default="hard",
              type=click.Choice(["easy", "medium", "hard", "expert"]))
@click.option("--seed", type=int, default=None)
@click.option("--out", default=str(ROOT / "data" / "problems"))
@click.option("--variations", "-n", type=int, default=1)
def scaffold(template_id, difficulty, seed, out, variations):
    """Create problem scaffold JSON(s) from a template."""
    gen = TemplateGenerator()
    vary = VariationEngine(gen)
    ensure_dir(out)
    specs = vary.sample(template_id, n=variations, seed=seed)
    for i, spec in enumerate(specs):
        p = gen.scaffold(template_id, difficulty=difficulty, variation=spec,
                         seed=None if seed is None else seed + i)
        path = Path(out) / f"{slugify(p.title)}_{p.id}.json"
        p.to_json(str(path))
        console.print(f"[green]Scaffold written:[/green] {path}")
    console.print("\n[bold]Failure-pattern checklist:[/bold]")
    for line in gen.failure_pattern_checklist(template_id):
        console.print(line)
    console.print("\n[yellow]REMINDER:[/yellow] author all content yourself — "
                  "LLM-generated submissions violate project rules.")


# ---------------- validate ----------------

@cli.command()
@click.argument("paths", nargs=-1, type=click.Path(exists=True))
@click.option("--strict/--no-strict", default=False,
              help="Treat warnings as errors")
def validate(paths, strict):
    """Validate submission JSON files against Riga guidelines."""
    validator = RigaValidator(domain_registry=DOMAIN_REGISTRY)
    exit_code = 0
    for fp in paths:
        for f in _expand(fp):
            try:
                p = RigaProblem.from_json(str(f))
            except Exception as e:
                console.print(f"[red]LOAD ERROR[/red] {f}: {e}")
                exit_code = 2
                continue
            issues = validator.validate(p)
            errs = [i for i in issues if i.severity == "error"]
            warns = [i for i in issues if i.severity == "warning"]
            status = "[green]PASS[/green]" if not errs and not (strict and warns) \
                else "[red]FAIL[/red]"
            console.rule(f"{f.name} — {status}")
            for i in issues:
                color = {"error": "red", "warning": "yellow", "note": "blue"}[i.severity]
                console.print(
                    f"  [{color}]{i.severity.upper()}[/{color}] "
                    f"[{i.category.value}] {i.message}"
                    + (f"\n      -> {i.suggestion}" if i.suggestion else ""))
            if errs or (strict and warns):
                exit_code = 1
    sys.exit(exit_code)


def _expand(fp: str):
    p = Path(fp)
    if p.is_dir():
        return sorted(p.glob("*.json"))
    return [p]


# ---------------- export ----------------

@cli.command()
@click.argument("input_dir", type=click.Path(exists=True))
@click.option("--format", "formats", default="tex,jsonl",
              help="comma list: tex,pdf,jsonl,csv")
@click.option("--status", default=None,
              help="comma list filter (e.g. accepted,quality_review)")
@click.option("--out", default=str(ROOT / "data" / "exports"))
@click.option("--no-solutions", is_flag=True)
def export(input_dir, formats, status, out, no_solutions):
    """Export submissions to LaTeX/PDF and dataset formats."""
    problems = []
    for f in sorted(Path(input_dir).glob("*.json")):
        try:
            problems.append(RigaProblem.from_json(str(f)))
        except Exception as e:
            console.print(f"[yellow]Skip {f.name}: {e}[/yellow]")
    console.print(f"Loaded {len(problems)} problem(s)")

    status_filter = [ReviewStatus(s) for s in status.split(",")] if status else None
    written = {}
    for fmt in formats.split(","):
        fmt = fmt.strip()
        if fmt in ("tex", "pdf"):
            written[fmt] = LatexExporter().export(
                problems, out, compile_pdf=(fmt == "pdf"),
                include_solutions=not no_solutions)
        elif fmt == "jsonl":
            written[fmt] = DatasetExporter().export_jsonl(
                problems, out, only_status=status_filter)
        elif fmt == "csv":
            written[fmt] = DatasetExporter().export_csv(
                problems, out)
    for k, v in written.items():
        console.print(f"[green]{k}:[/green] {v}")


# ---------------- stumptest ----------------

@cli.command()
@click.argument("submission", type=click.Path(exists=True))
@click.option("--trials", default=5)
@click.option("--models", default="openai:gpt-4.1", multiple=True,
              help="provider:model entries; requires API keys in env")
def stumptest(submission, trials, models):
    """Run LLM difficulty test against frontier models.

    Per rules: must stump at least ONE model the MAJORITY of the time;
    'no response' does NOT count as failure.
    """
    p = RigaProblem.from_json(submission)
    if not p.prompt_latex or not p.answer:
        console.print("[red]Submission lacks prompt/answer[/red]")
        sys.exit(2)

    tester = LLMTester()
    for spec in models:
        provider, model = spec.split(":", 1)
        fn = _make_provider(provider, model)
        if fn:
            tester.register_provider(model, fn)
        else:
            console.print(f"[yellow]No client configured for {provider}; skipped.[/yellow]")
    if not tester.providers:
        console.print("[red]No providers available[/red]")
        sys.exit(2)

    reference = p.answer.strip().strip("$").strip()
    reports = tester.test(p.prompt_latex, reference, trials=trials)
    any_stumped = False
    for name, r in reports.items():
        console.print(r.summary())
        p.llm_test_results.extend(
            [p.llm_test_results[-1]] if False else [])
        any_stumped = any_stumped or r.stumped
    p.stumps_verified = any_stumped
    p.to_json(submission)
    console.rule("[bold]Result")
    console.print("stumps_verified = " +
                  ("[green]True[/green]" if any_stumped else "[red]False[/red]"))


def _make_provider(provider: str, model: str):
    import os
    if provider == "openai":
        key = os.environ.get("OPENAI_API_KEY")
        if not key:
            return None
        import openai
        client = openai.OpenAI(api_key=key)

        def fn(system, user):
            r = client.chat.completions.create(
                model=model,
                messages=[{"role": "system", "content": system},
                          {"role": "user", "content": user}])
            return r.choices[0].message.content
        return fn
    if provider == "anthropic":
        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            return None
        import anthropic
        client = anthropic.Anthropic(api_key=key)

        def fn(system, user):
            r = client.messages.create(
                model=model, system=system, max_tokens=4000,
                messages=[{"role": "user", "content": user}])
            return "".join(b.text for b in r.content)
        return fn
    if provider == "google":
        key = os.environ.get("GOOGLE_API_KEY")
        if not key:
            return None
        import google.generativeai as genai
        genai.configure(api_key=key)

        def fn(system, user):
            m = genai.GenerativeModel(model, system_instruction=system)
            r = m.generate_content(user)
            return r.text
        return fn
    return None


# ---------------- conductcheck ----------------

@cli.command()
@click.argument("input_dir", type=click.Path(exists=True))
@click.option("--corpus", default=None,
              help="Directory of known external/corpus texts for plagiarism comparison")
@click.option("--threshold", default=0.85, type=float)
def conductcheck(input_dir, corpus, threshold):
    """Code of Conduct signals: near-duplicates (spam/templated),
    corpus match (plagiarism heuristic), template-placeholder residue,
    LLM boilerplate phrases. Results are review signals, not automatic rejection."""
    problems = []
    for f in sorted(Path(input_dir).glob("*.json")):
        try:
            problems.append(RigaProblem.from_json(str(f)))
        except Exception as e:
            console.print(f"[yellow]Skip {f.name}: {e}[/yellow]")
    checker = OriginalityChecker(threshold=threshold)
    rep = checker.check_batch(problems)
    if corpus:
        rep2 = checker.check_against_corpus(problems, corpus)
        rep.corpus_hits.extend(rep2.corpus_hits)

    ok = True
    console.rule("[bold]Conduct signals")
    for hit in rep.cluster_hits:
        ok = False
        console.print(f"[red]SPAM/TEMPLATED[/red] {hit.a} ~ {hit.b} "
                      f"(similarity={hit.similarity:.2f}): {hit.reason}")
    for hit in rep.corpus_hits:
        ok = False
        console.print(f"[red]PLAGIARISM RISK[/red] {hit.a} ~ {hit.b} "
                      f"(similarity={hit.similarity:.2f}): {hit.reason}")
    for pid in rep.placeholder_files:
        ok = False
        console.print(f"[red]UNFINISHED SCAFFOLD[/red] {pid}: placeholder text present")
    for pid in rep.llm_phrase_files:
        ok = False
        console.print(f"[red]LLM BOILERPLATE[/red] {pid}: forbidden AI phrasing detected")
    if ok:
        console.print("[green]No automated conduct signals detected.[/green]")
    sys.exit(0 if ok else 1)


# ---------------- concepts & checklist ----------------

@cli.command()
def concepts():
    """Print the Solution Concepts formatting rules."""
    console.print(
        "Solution Concepts rules:\n"
        "  - List 1 to 5 concepts (five most important if more apply)\n"
        "  - ONE concept per field\n"
        "  - No bullet points, hyphens, em dashes, numbering, or other punctuation prefixes\n"
        "  - Single line per concept, concise text only\n"
        "  - No explanatory details about what the concept means\n")


@cli.command()
def checklist():
    """Print the mandatory final pre-submission checklist."""
    items = [
        "One and only one correct answer (unique; equivalent forms allowed, e.g. valid SMILES variants)",
        "Spelling and grammar checked",
        "Solution steps independently verified (recomputed key equalities/numbers)",
        "Not plagiarized",
        "No LLM-generated content anywhere",
        "LaTeX: $...$ / $$...$$ only (never \\( \\[ ), no \\item[], no **bold**, "
        "mhchem OK / chemfig FORBIDDEN, proper symbols (\\leq not <=), escaped braces \\{...\\}",
        "Final step ends with exactly: Final Answer: $\\boxed{<answer>}$",
        "Answer field: only $...$ wrapped answer, no \\boxed, exact match of boxed content",
        "1-5 concepts, one per field, no punctuation prefixes",
        "Domain + subdomain chosen with justification in the prescribed structure",
        "Problem self-contained: all data/formulas in prompt; no paper/figure/table references",
        "No multi-part questions; not guessable (no yes/no, MCQ, T/F)",
        "Minimum 3 substantial steps; each step starts 'Step #'",
        "Stumps >= 1 frontier model the majority of the time (no-response does NOT count)",
        "Rounding instructions specified in prompt if decimal approximation required",
    ]
    for i, it in enumerate(items, 1):
        console.print(f"[green][OK][/green] {i}. {it}")


def main():
    cli()


if __name__ == "__main__":
    main()
