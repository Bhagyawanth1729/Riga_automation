"""Core data model for a Project Riga problem submission.

Mirrors the required fields from the Snorkel submission UI:
- Problem (Prompt): LaTeX, single self-contained question
- Domain / Sub-domain + Domain Explanation
- Step-by-Step Worked Solution (>= 3 steps, each "Step #", ends with Final Answer: $\\boxed{...}$)
- Answer field (exact match of boxed content, wrapped in $...$, no \\boxed)
- Problem Type, Answer Type, Concepts (1-5, one per field, no punctuation prefixes)
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()
from enum import Enum
from typing import Optional
import uuid
import json


class Subject(str, Enum):
    BIOLOGY = "biology"
    CHEMISTRY = "chemistry"
    PHYSICS = "physics"


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    EXPERT = "expert"


class ReasoningType(str, Enum):
    MULTI_STEP_DEDUCTION = "multi_step_deduction"
    QUANTITATIVE_REASONING = "quantitative_reasoning"
    CONCEPTUAL_SYNTHESIS = "conceptual_synthesis"
    COUNTERFACTUAL_REASONING = "counterfactual_reasoning"
    EXPERIMENTAL_DESIGN = "experimental_design"
    DIMENSIONAL_ANALYSIS = "dimensional_analysis"
    LIMITING_CASE_ANALYSIS = "limiting_case_analysis"
    ORDER_OF_MAGNITUDE = "order_of_magnitude"
    SYMBOLIC_MANIPULATION = "symbolic_manipulation"
    GRAPH_INTERPRETATION = "graph_interpretation"
    LITERATURE_GROUNDED = "literature_grounded"


class ReviewStatus(str, Enum):
    DRAFT = "draft"
    AUTOMATED_CHECKED = "automated_checks_only"
    QUALITY_REVIEW = "quality_review"
    ACCEPTED = "accepted"
    NEEDS_REVISION = "needs_revision"
    REJECTED = "rejected"


class ErrorCategory(str, Enum):
    """Error categories from the Riga documentation."""
    NOT_SELF_CONTAINED = "not_self_contained"
    NON_UNIQUE_ANSWER = "non_unique_answer"
    TOO_COMPUTATIONAL = "too_computational"
    MULTI_PART_QUESTION = "multi_part_question"
    GUESSABLE = "guessable"
    DOMAIN_BEYOND_SCOPE = "domain_beyond_project_scope"
    WRONG_ANSWER = "wrong_answer"
    UNJUSTIFIED_CLAIMS = "unjustified_or_unsupported_claims"
    UNSTATED_ASSUMPTION = "unstated_assumption"
    STEP_ERROR = "step_error"
    MAJOR_LATEX_ISSUES = "major_latex_or_formatting_issues"
    MAJOR_GRAMMAR_ISSUES = "major_grammar_or_language_issues"
    OTHER = "other"


@dataclass
class SolutionStep:
    """A single step in the worked solution."""
    number: int
    content: str  # LaTeX content, must start with "Step {number}"
    key_results: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)

    def render(self) -> str:
        return f"Step {self.number}\n{self.content}"


@dataclass
class Classification:
    subject: Subject
    domain: str = ""               # e.g. "Electrochemistry"
    subdomain: str = ""            # e.g. "Nernst equation"
    domain_explanation: str = ""   # Why this domain beats the next-best
    difficulty: Difficulty = Difficulty.MEDIUM
    reasoning_types: list[ReasoningType] = field(default_factory=list)
    problem_type: str = ""         # from platform's Problem Types list
    answer_type: str = ""          # from platform's Answer Types list
    concepts: list[str] = field(default_factory=list)  # 1-5 items

    def validate_concepts(self) -> list[str]:
        errors = []
        if not (1 <= len(self.concepts) <= 5):
            errors.append(f"Concepts count must be 1-5, got {len(self.concepts)}")
        for c in self.concepts:
            stripped = c.strip()
            if not stripped:
                errors.append("Empty concept entry")
            if any(stripped.startswith(p) for p in ("-", "*", "•", "1.", "2.")):
                errors.append(f"Concept '{c}' uses punctuation/numbering prefix (not allowed)")
            if "\n" in stripped:
                errors.append(f"Concept '{c}' spans multiple lines (must be single line)")
        return errors


@dataclass
class LLMTestResult:
    """Result of testing the problem against a frontier model."""
    model_name: str
    model_answer: str
    correct: bool
    timestamp: str = field(default_factory=_utcnow)


@dataclass
class ValidationIssue:
    category: ErrorCategory
    severity: str  # "error" | "warning" | "note"
    message: str
    suggestion: str = ""


@dataclass
class RigaProblem:
    """The full submission package."""
    title: str = ""
    prompt_latex: str = ""
    solution_steps: list[SolutionStep] = field(default_factory=list)
    answer: str = ""               # $...$ wrapped, matches boxed in final step
    classification: Classification = field(default_factory=lambda: Classification(
        subject=Subject.PHYSICS, domain="", subdomain="", domain_explanation=""))
    author_notes: str = ""
    status: ReviewStatus = ReviewStatus.DRAFT
    llm_test_results: list[LLMTestResult] = field(default_factory=list)
    stumps_verified: bool = False  # at least one model wrong majority of the time
    id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    created: str = field(default_factory=_utcnow)
    modified: str = field(default_factory=_utcnow)
    version: int = 1

    # ---------- helpers ----------

    def final_step_has_boxed(self) -> bool:
        if not self.solution_steps:
            return False
        last = max(self.solution_steps, key=lambda s: s.number)
        return "Final Answer:" in last.content and "\\boxed" in last.content

    def extract_boxed_answer(self) -> Optional[str]:
        """Extract content inside \\boxed{...} of the final step."""
        import re
        if not self.solution_steps:
            return None
        last = max(self.solution_steps, key=lambda s: s.number).content
        m = re.search(r"Final Answer:\s*\$\\boxed\{(.*)\}\$\s*$", last.strip(), re.S)
        return m.group(1) if m else None

    def answer_matches_box(self, normalize_ws: bool = False) -> bool:
        boxed = self.extract_boxed_answer()
        if boxed is None:
            return False
        ans = self.answer.strip()
        if ans.startswith("$") and ans.endswith("$"):
            ans = ans[1:-1]
        if normalize_ws:
            return " ".join(boxed.split()) == " ".join(ans.split())
        return boxed == ans   # exact match (spacing/punctuation must match per guide)

    def to_json(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(asdict(self), f, indent=2, ensure_ascii=False, default=str)

    @classmethod
    def from_json(cls, path: str) -> "RigaProblem":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        data["solution_steps"] = [SolutionStep(**s) for s in data.get("solution_steps", [])]
        data["classification"] = Classification(
            subject=Subject(data["classification"]["subject"]),
            difficulty=Difficulty(data["classification"].get("difficulty", "medium")),
            reasoning_types=[ReasoningType(r) for r in data["classification"].get("reasoning_types", [])],
            **{k: v for k, v in data["classification"].items()
               if k not in ("subject", "difficulty", "reasoning_types")},
        )
        data["llm_test_results"] = [LLMTestResult(**r) for r in data.get("llm_test_results", [])]
        data["status"] = ReviewStatus(data.get("status", "draft"))
        return cls(**data)
