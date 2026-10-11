"""Submission workspace: manage problem lifecycle and quality tiers.

Workflow:
  draft (data/problems) -> automated checks -> quality review -> accepted (data/reviewed)
Mirror the Snorkel 'Submission Routing' choice (Quality Review vs Automated Checks Only).
"""
from __future__ import annotations

import json
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from ..models.problem import RigaProblem, ReviewStatus, ValidationIssue
from ..validators.riga_validator import RigaValidator
from ..utils.file_utils import ensure_dir, timestamp


@dataclass
class CheckReport:
    problem_id: str
    status: ReviewStatus
    errors: list[ValidationIssue] = field(default_factory=list)
    warnings: list[ValidationIssue] = field(default_factory=list)
    notes: list[ValidationIssue] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def to_markdown(self) -> str:
        lines = [f"# Check report for {self.problem_id}",
                 f"Recommended status: **{self.status.value}**", ""]
        for group, tag in [(self.errors, "ERROR"), (self.warnings, "WARN"),
                            (self.notes, "NOTE")]:
            if group:
                lines.append(f"## {tag}s ({len(group)})")
                for i in group:
                    lines.append(f"- [{i.category.value}] {i.message}")
                    if i.suggestion:
                        lines.append(f"  - Suggestion: {i.suggestion}")
                lines.append("")
        return "\n".join(lines)


class Workspace:
    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.problems_dir = ensure_dir(self.root / "data" / "problems")
        self.review_dir = ensure_dir(self.root / "data" / "reviewed")
        self.exports_dir = ensure_dir(self.root / "data" / "exports")
        self.reports_dir = ensure_dir(self.root / "data" / "reports")

    def automated_check(self, problem_path: str,
                        validator: Optional[RigaValidator] = None,
                        strict: bool = False) -> CheckReport:
        """'Automated Checks Only' routing: check without human review."""
        validator = validator or RigaValidator()
        p = RigaProblem.from_json(problem_path)
        issues = validator.validate(p)
        report = CheckReport(
            problem_id=p.id,
            status=ReviewStatus.NEEDS_REVISION if any(i.severity == "error" for i in issues)
                   else (ReviewStatus.AUTOMATED_CHECKED if not any(i.severity == "warning" for i in issues) or strict
                         else ReviewStatus.AUTOMATED_CHECKED),
            errors=[i for i in issues if i.severity == "error"],
            warnings=[i for i in issues if i.severity == "warning"],
            notes=[i for i in issues if i.severity == "note"],
        )
        # persist p.status as 'automated_checks_only' if passing and not yet submitted
        if report.ok and p.status == ReviewStatus.DRAFT:
            p.status = ReviewStatus.AUTOMATED_CHECKED
            p.to_json(problem_path)
        self._write_report(report)
        return report

    def route_to_quality_review(self, problem_path: str) -> str:
        """Mark a passing submission for human Quality Review review."""
        p = RigaProblem.from_json(problem_path)
        p.status = ReviewStatus.QUALITY_REVIEW
        p.to_json(problem_path)
        return str(problem_path)

    def accept(self, problem_path: str) -> str:
        """Move to accepted library (data/reviewed)."""
        p = RigaProblem.from_json(problem_path)
        p.status = ReviewStatus.ACCEPTED
        p.modified = timestamp()
        dest = self.review_dir / Path(problem_path).name
        p.to_json(str(dest))
        return str(dest)

    def _write_report(self, r: CheckReport):
        path = self.reports_dir / f"{r.problem_id}_{timestamp()}.md"
        path.write_text(r.to_markdown(), encoding="utf-8")

    def dashboard(self) -> dict[str, int]:
        counts = {}
        for d in (self.problems_dir, self.review_dir):
            for f in d.glob("*.json"):
                try:
                    p = RigaProblem.from_json(str(f))
                    counts[p.status.value] = counts.get(p.status.value, 0) + 1
                except Exception:
                    counts["unreadable"] = counts.get("unreadable", 0) + 1
        return counts
