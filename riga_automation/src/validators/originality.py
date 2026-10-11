"""Originality & anti-spam checks (Code of Conduct enforcement helpers).

Implements the automatable signals from config/code_of_conduct.yaml:
- cross-submission similarity (shingle Jaccard) -> spam/templated clusters
- known-corpus hash & similarity match -> plagiarism heuristic
- template placeholder residue -> unfinished scaffold submitted as work
- authoring-time heuristic -> low-AHT flag (informational)

NOTE: These are *signals for human review*, not automatic grounds for
rejection — consistent with the project's guidance.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from ..models.problem import RigaProblem


_AUTHOR_PHRASES = re.compile(r"[\s_\-\*#•]*AUTHORED[\s_:/A-Za-z]*", re.I)
_LLM_BOILERPLATE = [
    r"as an ai language model", r"i cannot help with that",
    r"as a large language model", r"i'm just an ai", r"certainly! here's",
    r"sure! here is", r"great question!",
]


def _norm_text(p: RigaProblem) -> str:
    parts = [p.prompt_latex, p.answer] + [s.content for s in p.solution_steps]
    parts += p.classification.concepts
    raw = " ".join(parts).lower()
    raw = re.sub(r"\s+", " ", raw)
    return raw


def _shingles(text: str, n: int = 5) -> set[tuple[str, ...]]:
    toks = re.findall(r"\w+|[^\w\s]", text)
    if len(toks) < n:
        return {tuple(toks)}
    return {tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


@dataclass
class SimilarityHit:
    a: str
    b: str
    similarity: float
    reason: str


@dataclass
class OriginalityReport:
    cluster_hits: list[SimilarityHit] = field(default_factory=list)     # within batch
    corpus_hits: list[SimilarityHit] = field(default_factory=list)      # vs known corpus
    placeholder_files: list[str] = field(default_factory=list)
    llm_phrase_files: list[str] = field(default_factory=list)
    low_aht_files: list[tuple[str, float]] = field(default_factory=list)  # (file, minutes)

    @property
    def ok(self) -> bool:
        return not (self.cluster_hits or self.corpus_hits or self.placeholder_files)


class OriginalityChecker:
    def __init__(self, threshold: float = 0.85,
                 placeholder_pattern: str = r"<AUTHORED|AUTHORED_ANSWER|<SELECT>",
                 min_active_minutes: float = 5.0):
        self.threshold = threshold
        self.placeholder_re = re.compile(placeholder_pattern, re.I)
        self.min_active_minutes = min_active_minutes

    # ---------- public ----------

    def check_batch(self, problems: list[RigaProblem]) -> OriginalityReport:
        rep = OriginalityReport()
        texts = [(_norm_text(p), p.id) for p in problems]

        # cross-similarity cluster (spam/templated signal)
        shingles = [(set(_shingles(t)), pid) for t, pid in texts]
        for i in range(len(shingles)):
            for j in range(i + 1, len(shingles)):
                sim = jaccard(shingles[i][0], shingles[j][0])
                if sim >= self.threshold:
                    rep.cluster_hits.append(SimilarityHit(
                        shingles[i][1], shingles[j][1], sim,
                        "near-duplicate submission (possible templating/spam)"))

        for text, pid in texts:
            if self.placeholder_re.search(text):
                rep.placeholder_files.append(pid)
            for pat in _LLM_BOILERPLATE:
                if re.search(pat, text):
                    rep.llm_phrase_files.append(pid)
                    break
        return rep

    def check_against_corpus(self, problems: list[RigaProblem],
                             corpus_dir: str | Path,
                             hash_match: bool = True) -> OriginalityReport:
        """Compare to an external corpus of known texts (one .txt/.json per file)."""
        rep = OriginalityReport()
        cdir = Path(corpus_dir)
        if not cdir.exists():
            return rep
        c_files = list(cdir.glob("*.txt")) + list(cdir.glob("*.json"))
        corpus = []
        for f in c_files:
            txt = f.read_text(encoding="utf-8", errors="ignore").lower()
            txt = re.sub(r"\s+", " ", txt)
            corpus.append((txt, f.name))
        corpus_shingles = [(_shingles(t), name) for t, name in corpus]
        corpus_hashes = {hashlib.sha256(t.encode()).hexdigest(): name
                         for t, name in corpus}

        for p in problems:
            txt = _norm_text(p)
            if hash_match:
                h = hashlib.sha256(txt.encode()).hexdigest()
                if h in corpus_hashes:
                    rep.corpus_hits.append(SimilarityHit(
                        p.id, corpus_hashes[h], 1.0, "exact hash match to known corpus"))
                    continue
            s = set(_shingles(txt))
            best_sim, best_name = 0.0, None
            for cs, name in corpus_shingles:
                sim = jaccard(s, cs)
                if sim > best_sim:
                    best_sim, best_name = sim, name
            if best_sim >= self.threshold and best_name is not None:
                rep.corpus_hits.append(SimilarityHit(
                    p.id, best_name, best_sim, "high similarity to known corpus text"))
        return rep
