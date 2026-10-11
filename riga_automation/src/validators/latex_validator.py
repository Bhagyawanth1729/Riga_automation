"""LaTeX syntax validation for Project Riga submissions.

Checks balance of math delimiters/environments, supported packages
(mhchem allowed, chemfig NOT supported), and common delimiter errors.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field


FORBIDDEN_PACKAGES = ["chemfig"]
KNOWN_PACKAGES = ["mhchem", "amsmath", "amssymb", "siunitx", "physics", "graphicx"]

ENVIRONMENTS = [
    "equation", "equation*", "align", "align*", "gather", "gather*",
    "multline", "multline*", "cases", "pmatrix", "bmatrix", "matrix",
    "enumerate", "itemize", "figure", "table", "document",
]


@dataclass
class LatexIssue:
    severity: str              # error | warning | note
    message: str
    line: int = 0
    position: int = 0


@dataclass
class LatexReport:
    ok: bool = True
    issues: list[LatexIssue] = field(default_factory=list)

    def add(self, severity: str, message: str, line: int = 0):
        self.issues.append(LatexIssue(severity, message, line))
        if severity == "error":
            self.ok = False


def check_balance(text: str) -> LatexReport:
    """Check braces, math delimiters, environments."""
    report = LatexReport()

    # brace balance (ignore escaped \{ \})
    depth = 0
    for i, ch in enumerate(text):
        if ch in "{}" and (i == 0 or text[i - 1] != "\\"):
            depth += 1 if ch == "{" else -1
            if depth < 0:
                report.add("error", "Unbalanced closing '}'", position=i)
                depth = 0
    if depth != 0:
        report.add("error", f"Unbalanced braces: {depth} unclosed '{{'")

    # $...$ balance (ignore \$)
    dollars = re.findall(r"(?<!\\)\$", text)
    if len(dollars) % 2 != 0:
        report.add("error", "Unbalanced inline math delimiters $...$ (odd count of $)")

    # $$ $$ and display math
    for open_tok, close_tok in [(r"$$", r"$$"), (r"\[", r"\]"), (r"\(", r"\)")]:
        if open_tok in ("$$",):
            n = text.count("$$")
            if n % 2 != 0:
                report.add("error", "Unbalanced display math $$...$$")
        else:
            n_open = len(re.findall(re.escape(open_tok), text))
            n_close = len(re.findall(re.escape(close_tok), text))
            if n_open != n_close:
                report.add("error", f"Unbalanced {open_tok}...{close_tok} ({n_open} vs {n_close})")

    # environments
    begins = re.findall(r"\\begin\{([^}]+)\}", text)
    ends = re.findall(r"\\end\{([^}]+)\}", text)
    from collections import Counter
    for env, n in (Counter(begins) - Counter(ends)).items():
        report.add("error", f"Environment '{env}' has \\begin without matching \\end")
    for env, n in (Counter(ends) - Counter(begins)).items():
        report.add("error", f"Environment '{env}' has \\end without matching \\begin")

    return report


def check_packages(text: str) -> LatexReport:
    report = LatexReport()
    for pkg in FORBIDDEN_PACKAGES:
        if re.search(rf"\\usepackage(?:\[[^\]]*\])?\{{{pkg}\}}", text) or re.search(rf"\\{pkg}", text):
            report.add("error",
                       f"Package '{pkg}' is NOT supported on the Snorkel platform "
                       f"(mhchem IS supported; remove chemfig usage)")
    return report


# ---- Appendix: LaTeX Formatting rules (Project conventions) ----

FORBIDDEN_DELIMITERS = [
    (r"\\\(", r"\\\)", "\\(...\\) is NOT allowed; use $...$"),
    (r"\\\[", r"\\\]", "\\[...\\] is NOT allowed; use $$...$$"),
]

KATEX_ONLY_COMMANDS = ["\\lang", "\\rang"]  # invalid; prefer \\langle / \\rangle

ASCII_OPERATOR_MAP = [
    (r"(?<!\\)(?<![<>=!<>])<=", "use \\leq instead of <="),
    (r"(?<![<>=!>])>=", "use \\geq instead of >="),
    (r"(?<![<>=!])!=(?![<>=!])", "use \\neq instead of !="),
    (r"\|\|", "absolute/norm: use \\lvert ... \\rvert or \\lVert ... \\rVert"),
]


def check_project_appendix(text: str) -> LatexReport:
    """Appendix: LaTeX Formatting requirements."""
    report = LatexReport()

    # Forbidden delimiters \(...\) and \[...\]
    for open_re, close_re, msg in FORBIDDEN_DELIMITERS:
        if re.search(open_re, text) or re.search(close_re, text):
            report.add("error", msg)

    # No \item[] usage
    if re.search(r"\\item\s*\[", text):
        report.add("error", "No use of \\item[] in lists")

    # No markdown bold **...**
    if re.search(r"\*\*[^*]+\*\*", text):
        report.add("error", "No use of **...** to bold steps or titles")

    # KaTeX-only commands: \lang / \rang (but NOT \langle / \rangle)
    for cmd in KATEX_ONLY_COMMANDS:
        if re.search(re.escape(cmd) + r"(?![a-zA-Z])", text):
            report.add("error", f"{cmd} is KaTeX-only/invalid; use "
                                f"\\langle / \\rangle instead")

    # ASCII operators
    for pat, fix in ASCII_OPERATOR_MAP:
        if re.search(pat, text):
            report.add("error", f"ASCII operator found (/{pat}/): {fix}")

    # Visible braces must be escaped: \{1,2,3\}
    # crude check: '=' followed by {space or not} digit/list pattern inside math
    if re.search(r"=\\?\s*\{?\d,\d", text) and "\\{" not in text:
        report.add("warning",
                   "Set-braces may be unescaped; use \\{1,2,3\\} when braces must render")

    # Polynomial descending order heuristic (e.g., 1 + x + x^2 flagged; x^2 + x + 1 ok)
    poly_m = re.findall(r"(1\s*\+\s*[a-zA-Z]\s*\+\s*[a-zA-Z]\^\{?2)", text)
    if poly_m:
        report.add("warning",
                   "Polynomial terms should be in descending order of exponents")

    # Unnecessary braces that don't render: {\frac{3}{4}}
    # (\boxed{\frac{...}} and similar legitimate grouping are excluded)
    if re.search(r"(?<!boxed)\{\\(frac|dfrac|tfrac)", text):
        report.add("warning",
                   "Avoid unnecessary braces that don't render (e.g., remove in {\\frac{3}{4}})")

    # Plaintext trig/log that should be commands: sin(, log(, ln(, sqrt(, tan( outside commands
    for fn, fix in [("sin\\(", "\\sin("), ("cos\\(", "\\cos("), ("tan\\(", "\\tan("),
                    ("ln\\(", "\\ln("), ("log", "\\log"), ("sqrt", "\\sqrt"),
                    ("\\bexp\\(", "\\exp(")]:
        bad = re.findall(rf"(?<!\\){fn}", text)
        if bad:
            report.add("warning", f"Plaintext function '{fn[:-2] if fn.endswith('(') else fn}' found; use {fix}")

    # Rounding instructions: decimal approx in answer/prompt without 'round' keyword
    return report


def check_constants_format(text: str) -> LatexReport:
    """e, pi, i, phi symbol conventions from the Appendix."""
    report = LatexReport()
    if re.search(r"(?<!\\)\bpi\b", text):
        report.add("warning", "Use \\pi instead of plaintext 'pi'")
    if re.search(r"(?<!\\)\binfinity\b|∞", text):
        report.add("error", "Use \\infty instead of 'infinity' or ∞")
    return report


def check_common_errors(text: str) -> LatexReport:
    report = LatexReport()
    # \ce without mhchem declared (soft check)
    if "\\ce{" in text and "mhchem" not in text:
        report.add("warning", "Uses \\ce{...} but mhchem may not be declared")
    # forbidden unicode arrows
    for bad, fix in [("→", "\\to"), ("–", "--"), ("−", "-"), ("×", "\\times"),
                     ("ε", "\\varepsilon or \\epsilon"), ("’", "'")]:
        if bad in text:
            report.add("warning", f"Unicode '{bad}' found; prefer LaTeX '{fix}'")
    # image references
    if re.search(r"\\includegraphics|\\begin\{figure\}\s*\\", text):
        report.add("warning", "Prompt contains figures/images; problems must be text-only")
    return report


def validate_latex(text: str) -> LatexReport:
    """Full LaTeX validation pipeline (fast checks only, no compile)."""
    combined = LatexReport()
    for r in (check_balance(text), check_packages(text), check_common_errors(text),
              check_project_appendix(text), check_constants_format(text)):
        combined.issues.extend(r.issues)
    combined.ok = not any(i.severity == "error" for i in combined.issues)
    return combined
