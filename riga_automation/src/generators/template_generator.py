"""Template-based problem generator for Project Riga.

Loads YAML template families for each subject and scaffolds new original
problems. Per project rules, the final prompt/solution must be authored and
verified by the human expert; the generator only provides the structural
scaffold, failure-pattern checklist, and variation axes.
"""
from __future__ import annotations

import os
import yaml
import random
from pathlib import Path
from typing import Optional

from ..models.problem import (RigaProblem, SolutionStep, Classification,
                              Subject, Difficulty, ReasoningType)
from ..utils.latex_utils import make_final_step_boxed, wrap_answer


TEMPLATE_DIR = Path(__file__).resolve().parent.parent.parent / "config" / "templates"


class TemplateGenerator:
    def __init__(self, template_dir: Optional[str] = None):
        self.template_dir = Path(template_dir) if template_dir else TEMPLATE_DIR
        self._cache: dict[str, list[dict]] = {}

    # ---------- loading ----------

    def _load(self, subject: str) -> list[dict]:
        if subject in self._cache:
            return self._cache[subject]
        path = self.template_dir / f"{subject}_templates.yaml"
        if not path.exists():
            raise FileNotFoundError(f"No template file: {path}")
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        templates = data.get("templates", []) if isinstance(data, dict) else []
        self._cache[subject] = templates
        return templates

    def list_templates(self, subject: Optional[str] = None) -> list[dict]:
        subjects = [subject] if subject else ["biology", "chemistry", "physics"]
        out = []
        for s in subjects:
            try:
                out.extend(self._load(s))
            except FileNotFoundError:
                continue
        return out

    def get_template(self, template_id: str) -> dict:
        for t in self.list_templates():
            if t.get("id") == template_id:
                return t
        raise KeyError(f"Unknown template id: {template_id}")

    # ---------- generation ----------

    def scaffold(self, template_id: str, difficulty: str = "hard",
                 variation: Optional[dict] = None, seed: Optional[int] = None
                 ) -> RigaProblem:
        """Build a problem scaffold from a template.

        IMPORTANT (guideline): the human expert must replace all
        <AUTHORED:...> placeholders with original, verified content.
        """
        rng = random.Random(seed)
        t = self.get_template(template_id)
        vax = t.get("variability_axes", {})
        # YAML form: list of single-key dicts
        if isinstance(vax, list):
            vax = {k: v for d in vax if isinstance(d, dict) for k, v in d.items()}
        chosen = {k: rng.choice(vs) if isinstance(vs, list) else vs
                  for k, vs in vax.items()}
        if variation:
            chosen.update(variation)

        p = RigaProblem(title=f"{t['name']} (scaffold)")
        p.prompt_latex = t.get("latex_skeleton", "")
        p.author_notes = (
            f"Template: {t['id']} | failure patterns: {t.get('failure_patterns', [])} | "
            f"variation: {chosen}. NOTE: author original content by hand; "
            f"LLM-generated content is NOT permitted in submissions."
        )

        cls = Classification(subject=Subject(t["subject"]))
        cls.difficulty = Difficulty(difficulty) if difficulty in Difficulty._value2member_map_ else Difficulty.HARD
        # map template topic(s) onto the canonical display-cased domain registry
        subj = t["subject"]
        try:
            import sys as _sys
            _cfg = str(Path(__file__).resolve().parent.parent.parent / "config")
            if _cfg not in _sys.path:
                _sys.path.insert(0, _cfg)
            from domain_registry import DOMAIN_REGISTRY
            reg = DOMAIN_REGISTRY.get(subj, {})
        except Exception:
            reg = {}
        topics = t.get("topics", []) + t.get("subtopics", [])

        def _norm(s):
            return s.lower().replace("_", " ").replace("&", "and")

        tnorm = {_norm(x): x for x in topics}
        cls.domain = ""
        for dom in reg:
            if _norm(dom) in tnorm:
                cls.domain = dom
                break
        if not cls.domain and reg:            # best-effort fallback
            cls.domain = next(iter(reg))
        cls.subdomain = ""
        for sub in reg.get(cls.domain, []):
            if _norm(sub) in tnorm:
                cls.subdomain = sub
                break
        cls.domain_explanation = "<AUTHORED: use structure — 'This problem involves X, which are part of <domain>. " \
                                 "The problem also involves Y, which are part of <other>. However, <why less central>.'>"
        cls.problem_type = "<SELECT>"; cls.answer_type = "<SELECT>"
        cls.reasoning_types = []
        for rt in t.get("reasoning_types", []):
            try:
                cls.reasoning_types.append(ReasoningType(rt))
            except ValueError:
                pass
        cls.concepts = t.get("concepts", [])[:5]   # max 5 per rules
        p.classification = cls

        # placeholder steps to be authored (at least 3 required)
        n = max(3, len(t.get("solution_outline", [])) if t.get("solution_outline") else 3)
        for i in range(1, n + 1):
            p.solution_steps.append(SolutionStep(
                number=i,
                content=f"Step {i} <AUTHORED: write Step {i} content here — substantial, verifiable>"))
        # final step format per Answer Formatting Guide
        p.solution_steps[-1].content += "\n" + make_final_step_boxed("AUTHORED_ANSWER")
        p.answer = wrap_answer("AUTHORED_ANSWER")
        return p

    def failure_pattern_checklist(self, template_id: str) -> list[str]:
        t = self.get_template(template_id)
        lines = [f"Failure patterns to exploit for '{t['name']}':"]
        for fp in t.get("failure_patterns", []):
            lines.append(f"  - {fp}")
        if t.get("authoring_pattern"):
            lines.append(f"Authoring pattern: {t['authoring_pattern']}")
        if t.get("literature_anchors"):
            lines.append("Literature anchors (for grounding, NOT to be referenced in prompt):")
            for a in t["literature_anchors"]:
                lines.append(f"  - {a}")
        return lines
