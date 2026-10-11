"""Tests for the full Riga submission validator."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "config"))

from src.models.problem import (RigaProblem, SolutionStep, Classification,
                                Subject, ErrorCategory)
from src.validators.riga_validator import RigaValidator

GOOD_PROMPT = (
    r"A voltage-gated channel has opening rate $\alpha(V) = \alpha_0 e^{zFV/RT}$ "
    r"with $\alpha_0 = 100 \ \text{s}^{-1}$, $z = 2$, $F = 96485 \ \text{C/mol}$, "
    r"$R = 8.314 \ \text{J/(mol K)}$, $T = 298 \ \text{K}$. "
    r"Derive the voltage at which the dwell-time variance equals the mean dwell time "
    r"squared, and compute its numerical value. Express the answer in mV.")


def _make_problem(**kw):
    p = RigaProblem(title="t")
    p.prompt_latex = kw.get("prompt", GOOD_PROMPT)
    steps = [
        "Step 1\nWrite the master equation for the two-state channel and solve the steady state.",
        "Step 2\nCompute the mean and variance of dwell time from the rate $\\alpha(V)$.",
        "Step 3\nSet variance = mean squared and solve for $V$; substitute the given constants.",
        "Step 4\nConvert to mV.\n\nFinal Answer: $\\boxed{25.7 \\ \\text{mV}}$",
    ]
    p.solution_steps = [SolutionStep(number=i + 1, content=c)
                        for i, c in enumerate(steps)]
    p.answer = r"$25.7 \ \text{mV}$"
    p.classification = Classification(
        subject=Subject.BIOLOGY, domain="Cell Biology",
        subdomain="Membrane structure and transport",
        domain_explanation=(
            "This problem involves ion-channel kinetics, which are part of Cell Biology, "
            "Membrane structure and transport. The problem also involves stochastic "
            "processes, which are part of Biophysics. However, the core quantity is a "
            "cellular membrane property, not a physical measurement setup."),
        problem_type="Derive and compute",
        answer_type="Numeric value with units",
        concepts=["Two-state kinetics", "Dwell-time distribution", "Steady state"],
    )
    p.stumps_verified = kw.get("stumps", True)
    return p


def test_good_problem_passes():
    p = _make_problem()
    v = RigaValidator(domain_registry={"biology": {
        "Cell Biology": ["Membrane structure and transport"]}})
    issues = [i for i in v.validate(p) if i.severity == "error"]
    assert issues == [], [i.message for i in issues]


def test_too_few_steps():
    p = _make_problem()
    p.solution_steps = p.solution_steps[:2]
    p.answer = r"$x$"
    v = RigaValidator()
    issues = v.validate(p)
    assert any("minimum 3" in i.message for i in issues)


def test_answer_mismatch():
    p = _make_problem()
    p.answer = r"$25.6 \ \text{mV}$"   # does not match boxed
    v = RigaValidator()
    issues = v.validate(p)
    assert any("EXACTLY match" in i.message for i in issues)


def test_answer_with_boxed():
    p = _make_problem()
    p.answer = r"$\boxed{25.7 \ \text{mV}}$"
    v = RigaValidator()
    issues = v.validate(p)
    assert any("must NOT use" in i.message for i in issues)


def test_multipart_detected():
    p = _make_problem(prompt=GOOD_PROMPT + r" (a) First part. (b) Second part.")
    v = RigaValidator()
    issues = v.validate(p)
    assert any(i.category == ErrorCategory.MULTI_PART_QUESTION for i in issues)


def test_guessable_detected():
    p = _make_problem(prompt="Is the rate positive? yes")
    v = RigaValidator()
    issues = v.validate(p)
    assert any(i.category == ErrorCategory.GUESSABLE for i in issues)


def test_not_self_contained_reference():
    p = _make_problem(prompt="Using the data in Table 3 of Smith et al., compute X.")
    v = RigaValidator()
    issues = v.validate(p)
    assert any(i.category == ErrorCategory.NOT_SELF_CONTAINED for i in issues)


def test_dne_answer_rejected():
    p = _make_problem()
    p.answer = r"$\text{does not exist}$"
    v = RigaValidator()
    issues = v.validate(p)
    assert any("not a valid answer" in i.message for i in issues)


def test_concepts_format():
    p = _make_problem()
    p.classification.concepts = ["- Bullet concept", "Fine"]
    v = RigaValidator()
    issues = v.validate(p)
    assert any("punctuation/numbering" in i.message for i in issues)
    p.classification.concepts = ["a", "b", "c", "d", "e", "f"]
    issues = v.validate(p)
    assert any("1-5" in i.message for i in issues)


def test_final_step_wrong_markup():
    p = _make_problem()
    p.solution_steps[-1].content = "Step 4\nConvert. Result: \\boxed{25 mV}"
    v = RigaValidator()
    issues = v.validate(p)
    assert any("Final Answer: $\\boxed{...}$" in i.message for i in issues)


def test_stumps_required():
    p = _make_problem(stumps=False)
    v = RigaValidator()
    issues = v.validate(p)
    assert any("stump at least one frontier model" in i.message for i in issues)
