"""Tests for generators and exporters."""
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.generators.template_generator import TemplateGenerator
from src.generators.variation_engine import VariationEngine
from src.exporters.latex_exporter import LatexExporter
from src.exporters.dataset_exporter import DatasetExporter
from src.models.problem import RigaProblem, SolutionStep, Classification, Subject


def test_templates_load():
    gen = TemplateGenerator()
    all_t = gen.list_templates()
    assert len(all_t) >= 10
    for s in ("biology", "chemistry", "physics"):
        assert gen.list_templates(s), f"no templates for {s}"


def test_scaffold_structure():
    gen = TemplateGenerator()
    some_id = gen.list_templates("physics")[0]["id"]
    p = gen.scaffold(some_id, difficulty="hard", seed=42)
    assert p.prompt_latex
    assert len(p.solution_steps) >= 3
    assert p.classification.subject.value == "physics"
    assert "Final Answer:" in p.solution_steps[-1].content
    assert "\\boxed" in p.solution_steps[-1].content


def test_variation_engine_distinct():
    gen = TemplateGenerator()
    vary = VariationEngine(gen)
    # find a template with axes
    tid = None
    for t in gen.list_templates():
        if t.get("variability_axes") and len(t["variability_axes"]) > 1:
            tid = t["id"]
            break
    if not tid:
        return  # no axes defined anywhere; skip
    picks = vary.sample(tid, n=4, seed=1, min_distinct_keys=1)
    seen = set()
    for spec in picks:
        key = tuple(sorted(spec.items()))
        assert key not in seen
        seen.add(key)


def _demo_problem():
    p = RigaProblem(title="Demo")
    p.prompt_latex = r"Given $V = \SI{1}{\milli\volt}$, compute $\alpha(V)$."
    p.solution_steps = [
        SolutionStep(1, "Step 1\nSet up equation."),
        SolutionStep(2, "Step 2\nSolve."),
        SolutionStep(3, r"Step 3\nSimplify. Final Answer: $\boxed{100 \ \text{s}^{-1}}$"),
    ]
    p.answer = r"$100 \ \text{s}^{-1}$"
    p.classification = Classification(
        subject=Subject.PHYSICS, domain="Classical Mechanics",
        subdomain="Oscillations and waves",
        domain_explanation="This problem involves oscillator rates, which are part of Classical Mechanics.",
        problem_type="Calculation", answer_type="Number with units",
        concepts=["Harmonic oscillator"])
    return p


def test_export_jsonl(tmp_path):
    p = _demo_problem()
    out = DatasetExporter().export_jsonl([p], str(tmp_path), basename="t")
    assert os.path.exists(out)
    lines = Path(out).read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 1
    import json
    rec = json.loads(lines[0])
    assert rec["n_steps"] == 3
    assert rec["answer"] == r"$100 \ \text{s}^{-1}$"


def test_export_tex(tmp_path):
    p = _demo_problem()
    res = LatexExporter().export([p], str(tmp_path), basename="t")
    assert os.path.exists(res["tex"])
    content = Path(res["tex"]).read_text(encoding="utf-8")
    assert "Prompt" in content and "Worked Solution" in content
    assert "Final Answer: $\\boxed{" in content
