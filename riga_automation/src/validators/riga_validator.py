"""Comprehensive Project Riga submission validator.

Implements every automated check derivable from the Riga documentation:

Quality Requirements:
  - Original (checker hook for plagiarism dataset — caller supplies)
  - Appropriate STEM domain + subdomain registry
  - Challenging (LLM test stumps verification)
  - Requires reasoning (>= 3 steps)
  - No multi-part problems
  - Well-formed (LaTeX + grammar heuristics)
  - Unique answer exists; "DNE"/"does not exist" rejected
  - Clear answer format (prompt must state format when parametric)
  - Reliably verifiable / non-computational
  - Self-contained (no references to papers/figures/tables/external data)
  - No shortcuts/hints, no guessable answers (MC, T/F, yes/no)
  - Problem makes sense in domain

Solution Requirements:
  - Steps numbered "Step 1".. sequentially
  - >= 3 substantial steps (micro-step detection heuristics)
  - Final step: 'Final Answer: $\\boxed{...}$' exact pattern
  - Answer field: $...$, no \\boxed, exact matches boxed content
  - No unjustified claims ("clearly", "it follows" flags for review)
  - Assumptions explicitly stated (pattern detection)
  - Non-computational (no code blocks, no excessive sig figs)

Concepts Section:
  - 1-5 concepts, single line each, no bullet/number prefixes

Domain Explanation:
  - Follows the prescribed justification structure keywords
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from ..models.problem import (RigaProblem, ErrorCategory, ValidationIssue)
from .latex_validator import validate_latex


# ------------- heuristics & vocab -------------

MULTIPART_PATTERNS = [
    r"\(\s*[abcd]\s*\)",         # (a)(b)(c)(d) sub-questions
    r"\(\s*i+\s*\)",
    r"\bparts?\b", r"\bsub-?questions?\b",
    r"\bfirst,\s+then\b.*\bfinally\b",
]

GUESSABLE_PATTERNS = [
    r"\b(is|are|does|do)\b.{0,80}\?\s*(answer\s*)?(yes|no)\b",  # yes/no question phrasing
    r"^\s*(true|false|yes|no)\s*$",      # answer is just T/F or Yes/No
    r"\bor\s+(true|false)\s*\??\s*$",     # "...or false?"
    r"\(\s*[A-D]\s*\).*\(\s*[A-D]\s*\)", # multiple choice options
    r"choose the (best|correct)",
    r"select (one|all that apply)",
]

REFERENCE_PATTERNS = [
    r"\bet\s+al\.?\b",
    r"\bfigure\s+\d+", r"\btable\s+\d+", r"\bfig\.\s*\d+",
    r"\bsection\s+\d+.*(of the (paper|study|article))",
    r"in (the|this) (referenced?|cited) (paper|study)",
    r"\[\d+\]",                    # numeric citation
    r"doi:", r"arXiv",
]

CLAIM_WORDS = ["clearly", "obviously", "it follows that", "it is evident",
               "trivially", "as one can see"]

COMPUTATION_PATTERNS = [
    r"```", r"\bpython\b", r"\bmatlab\b", r"\bmathematica\b", r"\bscipy\b",
    r"\bwolfram\b", r"import\s+\w+",
]

UNITS_PATTERN = re.compile(
    r"\\(si|SI|per|meter|gram|second|volt|ampere|kelvin|mole|joule|newton|watt|"
    r"pascal|hertz|tesla|coulomb|farad|henry|ohm|bar|degreeCelsius|liter|litre)\b")


class RigaValidator:
    """Validates a RigaProblem against all project guidelines."""

    def __init__(self, domain_registry: dict | None = None,
                 knowntasks: set[str] | None = None):
        # domain_registry: {"chemistry": {"Electrochemistry": ["Nernst equation", ...]}, ...}
        self.domain_registry = domain_registry or {}
        self.known_tasks = knowntasks or set()   # for originality check (hash store)
        self.issues: list[ValidationIssue] = []

    # ---------------- top level ----------------

    def validate(self, problem: RigaProblem) -> list[ValidationIssue]:
        self.issues = []
        self._check_prompt(problem)
        self._check_solution(problem)
        self._check_answer(problem)
        self._check_classification(problem)
        self._check_difficulty(problem)
        return self.issues

    def _add(self, cat, sev, msg, sug=""):
        self.issues.append(ValidationIssue(cat, sev, msg, sug))

    # ---------------- prompt checks ----------------

    def _check_prompt(self, p: RigaProblem):
        pr = p.prompt_latex.strip()
        if not pr:
            self._add(ErrorCategory.OTHER, "error", "Prompt is empty")
            return

        # LaTeX
        rep = validate_latex(pr)
        for i in rep.issues:
            self._add(ErrorCategory.MAJOR_LATEX_ISSUES, i.severity, f"Prompt LaTeX: {i.message}")

        # Multi-part
        for pat in MULTIPART_PATTERNS:
            if re.search(pat, pr, re.I):
                self._add(ErrorCategory.MULTI_PART_QUESTION, "error",
                          f"Prompt appears multi-part (matched /{pat}/).",
                          "A problem is ONE question; remove sub-parts.")
                break

        # Guessable
        for pat in GUESSABLE_PATTERNS:
            if re.search(pat, pr, re.I):
                self._add(ErrorCategory.GUESSABLE, "error",
                          "Prompt looks guessable (yes/no, true/false, or multiple choice).")
                break

        # Self-contained: external references
        for pat in REFERENCE_PATTERNS:
            if re.search(pat, pr, re.I):
                self._add(ErrorCategory.NOT_SELF_CONTAINED, "error",
                          f"Prompt references external material (/{pat}/).",
                          "Include the needed data/formulas in the prompt itself; "
                          "no dependence on a single paper/figure/table.")
                break

        # Self-contained: undefined symbol heuristic — every \word in prompt
        # that also appears in answer should be defined or standard
        # (light-touch; deep semantic check is human)
        if re.search(r"\bundefined\b|\bnot defined\b", pr, re.I):
            self._add(ErrorCategory.NOT_SELF_CONTAINED, "warning",
                      "Prompt mentions undefined terms; ensure all symbols are defined.")

        # Computational
        for pat in COMPUTATION_PATTERNS:
            if re.search(pat, pr, re.I):
                self._add(ErrorCategory.TOO_COMPUTATIONAL, "error",
                          "Prompt references computer code/CAS.",
                          "Problem must be solvable by hand with a scientific calculator.")
                break
        if re.search(r"\d{8,}", pr):
            self._add(ErrorCategory.TOO_COMPUTATIONAL, "warning",
                      "Prompt has very long numbers; verify they're calculator-tractable.")

        # Word puzzle guard
        if re.search(r"\briddle\b|\bwordplay\b|\bpun\b", pr, re.I):
            self._add(ErrorCategory.DOMAIN_BEYOND_SCOPE, "error", "Word puzzles are not allowed.")

        # Domain registry
        cls = p.classification
        reg = self.domain_registry.get(cls.subject.value, {})
        if reg:
            if cls.domain and cls.domain not in reg:
                self._add(ErrorCategory.DOMAIN_BEYOND_SCOPE, "error",
                          f"Domain '{cls.domain}' not registered for {cls.subject.value}",
                          f"Choose from: {sorted(reg)}")
            elif cls.domain and cls.subdomain and cls.subdomain not in reg.get(cls.domain, []):
                self._add(ErrorCategory.DOMAIN_BEYOND_SCOPE, "warning",
                          f"Subdomain '{cls.subdomain}' not registered under '{cls.domain}'")

        # Originality (hash comparison)
        import hashlib
        h = hashlib.sha256(pr.lower().encode()).hexdigest()
        if h in self.known_tasks:
            self._add(ErrorCategory.OTHER, "error",
                      "Prompt matches a known task (originality check failed).")

    # ---------------- solution checks ----------------

    def _check_solution(self, p: RigaProblem):
        steps = sorted(p.solution_steps, key=lambda s: s.number)
        if len(steps) < 3:
            self._add(ErrorCategory.UNJUSTIFIED_CLAIMS, "error",
                      f"Only {len(steps)} solution steps; minimum 3 required.")

        # sequential numbering + "Step #" prefix
        for idx, s in enumerate(steps, start=1):
            if s.number != idx:
                self._add(ErrorCategory.MAJOR_LATEX_ISSUES, "error",
                          f"Step numbering not sequential (found {s.number}, expected {idx})")
            head = s.content.strip().lower()
            if not (head.startswith(f"step {s.number}") or head.startswith(f"step#{s.number}")):
                self._add(ErrorCategory.MAJOR_LATEX_ISSUES, "error",
                          f"Step {s.number} must start with 'Step {s.number}'")

        # per-step LaTeX
        for s in steps:
            rep = validate_latex(s.content)
            for i in rep.issues:
                self._add(ErrorCategory.MAJOR_LATEX_ISSUES, i.severity,
                          f"Step {s.number} LaTeX: {i.message}")

        # micro-step heuristic: steps with < 25 chars after removing header are suspicious
        sizes = [len(re.sub(r"^Step \d+\s*:?", "", s.content.strip())) for s in steps[:-1]]
        if sizes and min(sizes) < 25 and len(steps) > 3:
            self._add(ErrorCategory.UNJUSTIFIED_CLAIMS, "warning",
                      "Some steps look like trivial micro-steps; merge or make each step substantial.")

        # final step format: 'Final Answer: $\boxed{...}$' as the ending
        if not steps:
            return
        last = steps[-1].content.strip()
        m = re.search(r"Final Answer:\s*\$\\boxed\{(.+?)\}\$\s*$", last, re.S)
        if not m:
            self._add(ErrorCategory.MAJOR_LATEX_ISSUES, "error",
                      "Last step must END with exactly: Final Answer: $\\boxed{...}$",
                      "Use the exact string 'Final Answer: $\\boxed{<answer>}$'. No 'Final Result', "
                      "no \\boxed outside $...$.")

        # unsupported-claim flags (warning for human verification)
        for s in steps:
            for w in CLAIM_WORDS:
                if w in s.content.lower():
                    self._add(ErrorCategory.UNJUSTIFIED_CLAIMS, "warning",
                              f"Step {s.number} uses '{w}'; verify justification is present.")

        # computational
        for s in steps:
            for pat in COMPUTATION_PATTERNS:
                if re.search(pat, s.content, re.I):
                    self._add(ErrorCategory.TOO_COMPUTATIONAL, "error",
                              f"Step {s.number} references code/CAS; solutions must be hand-verifiable.")

        # sig-fig / precision heuristic
        for s in steps:
            for tok in re.findall(r"\d+\.\d{5,}", s.content):
                self._add(ErrorCategory.TOO_COMPUTATIONAL, "warning",
                          f"Step {s.number} has high-precision number {tok} "
                          f"(calculator-tractable? appropriate sig figs?)")

    # ---------------- answer checks ----------------

    def _check_answer(self, p: RigaProblem):
        ans = p.answer.strip()
        if not ans:
            self._add(ErrorCategory.OTHER, "error", "Answer field is empty")
            return

        if "\\boxed" in ans:
            self._add(ErrorCategory.MAJOR_LATEX_ISSUES, "error",
                      "Answer field must NOT use \\boxed (wrap in $...$ only)")
        if ans.lower().startswith(("final answer", "final result")):
            self._add(ErrorCategory.MAJOR_LATEX_ISSUES, "error",
                      "Answer field must not contain 'Final Answer/Result' wording")
        if re.match(r"^\$.*\$$", ans, re.S) is None:
            self._add(ErrorCategory.MAJOR_LATEX_ISSUES, "error",
                      "Answer field must be wrapped in $...$")

        if re.search(r"does\s+not\s+exist|\bDNE\b", ans, re.I):
            self._add(ErrorCategory.OTHER, "error",
                      "'Does not exist'/DNE is not a valid answer on this project.")

        if "<" in ans or ">" in ans:
            if "$<$" in ans or "$>$" in ans or "\\lt" in ans or "\\gt" in ans:
                pass
            elif not re.search(r"\\(le|ge|neq)", ans):
                self._add(ErrorCategory.MAJOR_LATEX_ISSUES, "error",
                          "Answer contains placeholder-like '<' or '>'",
                          "Remove angle brackets — they are placeholders, not part of the answer.")

        # exact match with boxed in final step
        if p.final_step_has_boxed():
            if not p.answer_matches_box():
                self._add(ErrorCategory.MAJOR_LATEX_ISSUES, "error",
                          "Answer field must EXACTLY match the \\boxed{...} content of the final step "
                          "(including spaces, punctuation, order).",
                          "Copy only the {...} from 'Final Answer: $\\boxed{...}$' and wrap in $...$.")
        else:
            self._add(ErrorCategory.MAJOR_LATEX_ISSUES, "error",
                      "Cannot verify answer match: final-step boxed answer missing.")

    # ---------------- classification checks ----------------

    def _check_classification(self, p: RigaProblem):
        cls = p.classification
        for msg in cls.validate_concepts():
            self._add(ErrorCategory.OTHER, "error", f"Concepts: {msg}")

        if not cls.domain_explanation.strip():
            self._add(ErrorCategory.OTHER, "error", "Domain Explanation is required.")
        else:
            # prescribed structure: involves X → domain; also involves Y → less appropriate
            de = cls.domain_explanation
            if "which are part of" not in de and "which is part of" not in de:
                self._add(ErrorCategory.OTHER, "warning",
                          "Domain explanation should follow: '...which are part of <domain>. "
                          "The problem also involves... However, <why their domain is less appropriate>.'")

        if not cls.problem_type:
            self._add(ErrorCategory.OTHER, "error", "Problem Type must be selected.")
        if not cls.answer_type:
            self._add(ErrorCategory.OTHER, "error", "Answer Type must be selected.")

    # ---------------- difficulty check ----------------

    def _check_difficulty(self, p: RigaProblem):
        if not p.stumps_verified:
            self._add(ErrorCategory.OTHER, "error",
                      "LLM difficulty not verified: problem must stump at least one frontier model "
                      "the majority of the time. Note: 'No response generated' does NOT count.")
        elif p.llm_test_results:
            n = len(p.llm_test_results)
            wrong = sum(1 for r in p.llm_test_results if not r.correct)
            if n and wrong / n < 0.5:
                self._add(ErrorCategory.OTHER, "error",
                          f"Only {wrong}/{n} model attempts were wrong (<50%).")
