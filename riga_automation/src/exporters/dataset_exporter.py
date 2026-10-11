"""Dataset exporter: JSONL / CSV of accepted Riga submissions.

Schema (one JSON object per line):
  id, title, subject, domain, subdomain, difficulty, reasoning_types,
  prompt_latex, solution_steps (list of 'Step N: ...'), final_step_boxed,
  answer, problem_type, answer_type, concepts, domain_explanation,
  stumps_verified, llm_failure_rate, status, created
"""
from __future__ import annotations

import csv
import json
import os
from dataclasses import asdict

from ..models.problem import RigaProblem, ReviewStatus
from ..utils.file_utils import ensure_dir, timestamp


class DatasetExporter:
    def to_record(self, p: RigaProblem) -> dict:
        cls = p.classification
        steps = sorted(p.solution_steps, key=lambda s: s.number)
        failed = [r for r in p.llm_test_results if not r.correct]
        rate = len(failed) / len(p.llm_test_results) if p.llm_test_results else None
        return {
            "id": p.id,
            "title": p.title,
            "subject": cls.subject.value,
            "domain": cls.domain,
            "subdomain": cls.subdomain,
            "domain_explanation": cls.domain_explanation,
            "difficulty": cls.difficulty.value,
            "reasoning_types": [r.value for r in cls.reasoning_types],
            "problem_type": cls.problem_type,
            "answer_type": cls.answer_type,
            "concepts": cls.concepts,
            "prompt_latex": p.prompt_latex,
            "solution_steps": [s.content for s in steps],
            "n_steps": len(steps),
            "final_step_boxed": p.extract_boxed_answer(),
            "answer": p.answer,
            "stumps_verified": p.stumps_verified,
            "llm_failure_rate": rate,
            "status": p.status.value,
            "created": p.created,
            "version": p.version,
        }

    def export_jsonl(self, problems: list[RigaProblem], out_dir: str,
                     only_status: list[ReviewStatus] | None = None,
                     basename: str | None = None) -> str:
        ensure_dir(out_dir)
        recs = [p for p in problems
                if only_status is None or p.status in only_status]
        path = os.path.join(out_dir,
                            (basename or f"riga_dataset_{timestamp()}") + ".jsonl")
        with open(path, "w", encoding="utf-8") as f:
            for p in recs:
                f.write(json.dumps(self.to_record(p), ensure_ascii=False) + "\n")
        return path

    def export_csv(self, problems: list[RigaProblem], out_dir: str,
                   basename: str | None = None) -> str:
        ensure_dir(out_dir)
        recs = [self.to_record(p) for p in problems]
        path = os.path.join(out_dir,
                            (basename or f"riga_dataset_{timestamp()}") + ".csv")
        if not recs:
            open(path, "w").close()
            return path
        flat = []
        for r in recs:
            r2 = dict(r)
            r2["reasoning_types"] = "; ".join(r2["reasoning_types"])
            r2["concepts"] = "; ".join(r2["concepts"])
            r2["solution_steps"] = "\n\n".join(r2["solution_steps"])
            flat.append(r2)
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(flat[0].keys()))
            w.writeheader()
            w.writerows(flat)
        return path
