"""Tests for LaTeX validation rules (incl. Appendix conventions)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.validators.latex_validator import validate_latex


def has_error(rep, needle):
    return any(i.severity == "error" and needle in i.message for i in rep.issues)


def test_inline_math_ok():
    rep = validate_latex(r"The rate is $k = 10 \ \text{s}^{-1}$.")
    assert not has_error(rep, "$...$")


def test_display_math_ok():
    rep = validate_latex(r"$$E = mc^2$$")
    assert rep.ok


def test_parenthesis_delimiters_forbidden():
    rep = validate_latex(r"Compute \( x^2 \).")
    assert has_error(rep, "NOT allowed")


def test_bracket_delimiters_forbidden():
    rep = validate_latex(r"\[ x^2 \]")
    # balance check counts \[ \] — also gives unbalanced; appendix error is what we check
    assert has_error(rep, "NOT allowed")


def test_chemfig_forbidden():
    rep = validate_latex(r"\usepackage{chemfig}\ce{H2O}")
    assert any("chemfig" in i.message for i in rep.issues)


def test_mhchem_allowed():
    rep = validate_latex(r"\usepackage[version=4]{mhchem} \ce{H2O}")
    assert not any("chemfig" in i.message for i in rep.issues)


def test_leq_not_allowed():
    rep = validate_latex(r"$a <= b$")
    assert any("\\leq" in i.message for i in rep.issues)


def test_item_bracket_forbidden():
    rep = validate_latex(r"\begin{itemize}\item[] x \end{itemize}")
    assert any("\\item[]" in i.message or "item" in i.message.lower() for i in rep.issues)


def test_markdown_bold_forbidden():
    rep = validate_latex(r"**Step 1** do something")
    assert any("**" in i.message for i in rep.issues)


def test_unbalanced_dollars():
    rep = validate_latex(r"$x^2 + y")
    assert has_error(rep, "Unbalanced")


def test_kaTex_command():
    rep = validate_latex(r"$\lang x \rang$")
    assert any("ang" in i.message for i in rep.issues)
