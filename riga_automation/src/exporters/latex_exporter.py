"""LaTeX document exporter with PDF compilation."""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from ..models.problem import RigaProblem
from ..utils.file_utils import ensure_dir, slugify, timestamp


DOCUMENT_PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage{amsmath, amssymb, amsfonts}
\usepackage[version=4]{mhchem}
\usepackage{siunitx}
\usepackage[margin=2.5cm]{geometry}
\setlength{\parskip}{6pt}
\begin{document}
"""

DOCUMENT_POSTAMBLE = r"\end{document}"


class LatexExporter:
    """Export submissions to compilable LaTeX documents and PDFs."""

    def render_document(self, problems: list[RigaProblem],
                        include_solutions: bool = True) -> str:
        parts = [DOCUMENT_PREAMBLE]
        for i, p in enumerate(problems, 1):
            cls = p.classification
            parts.append(f"\\section*{{Problem {i}: {p.title or p.id}}}")
            parts.append(f"\\textit{{{cls.subject.value.title()} / {cls.domain} / {cls.subdomain}}}\n")
            parts.append("--- Prompt ---\n")
            parts.append(p.prompt_latex)
            if include_solutions:
                parts.append("\n--- Worked Solution ---\n")
                for step in sorted(p.solution_steps, key=lambda s: s.number):
                    parts.append(step.content)
                parts.append(f"\nAnswer: {p.answer}")
            parts.append(f"\nConcepts: {', '.join(cls.concepts)}\n")
            parts.append("\\clearpage\n")
        parts.append(DOCUMENT_POSTAMBLE)
        return "\n\n".join(parts)

    def export(self, problems: list[RigaProblem], out_dir: str,
               basename: str | None = None, compile_pdf: bool = False,
               include_solutions: bool = True) -> dict[str, str]:
        ensure_dir(out_dir)
        basename = basename or f"riga_export_{timestamp()}"
        tex_path = os.path.join(out_dir, slugify(basename) + ".tex")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(self.render_document(problems, include_solutions))
        result = {"tex": tex_path}
        if compile_pdf:
            pdf = self.compile_pdf(tex_path)
            if pdf:
                result["pdf"] = pdf
        return result

    @staticmethod
    def compile_pdf(tex_path: str, engine: str = "pdflatex") -> str | None:
        """Compile with pdflatex (Twice for refs). Requires TeX distribution."""
        if not shutil.which(engine):
            raise RuntimeError(
                f"'{engine}' not found on PATH. Install MiKTeX/TeX Live.")
        work = Path(tex_path).parent
        job = Path(tex_path).stem
        for _ in range(2):
            proc = subprocess.run(
                [engine, "-interaction=nonstopmode", f"-jobname={job}", tex_path],
                cwd=work, capture_output=True, text=True, timeout=300)
            if proc.returncode != 0:
                return None
        pdf = work / f"{job}.pdf"
        return str(pdf) if pdf.exists() else None
