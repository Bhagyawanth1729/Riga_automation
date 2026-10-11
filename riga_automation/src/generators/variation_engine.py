"""Variation engine: generate N distinct parameter variations of a scaffold.

Produces variation specs so the human author can produce multiple distinct,
non-templated original problems from the same structural idea (avoiding the
'spam/repetitive/templated' rejection reason by requiring manual authoring).
"""
from __future__ import annotations

import itertools
import random
from typing import Any

from .template_generator import TemplateGenerator


class VariationEngine:
    def __init__(self, template_generator: TemplateGenerator | None = None):
        self.gen = template_generator or TemplateGenerator()

    def expand_axes(self, template_id: str) -> list[dict[str, Any]]:
        """Cartesian product of variability axes for a template."""
        t = self.gen.get_template(template_id)
        axes = t.get("variability_axes", {})
        if isinstance(axes, list):
            axes = {k: v for d in axes if isinstance(d, dict) for k, v in d.items()}
        if not axes:
            return [{}]
        keys = list(axes.keys())
        values = [axes[k] if isinstance(axes[k], list) else [axes[k]] for k in keys]
        return [dict(zip(keys, combo)) for combo in itertools.product(*values)]

    def sample(self, template_id: str, n: int = 5, seed: int | None = None,
               min_distinct_keys: int = 1) -> list[dict[str, Any]]:
        """Sample n distinct variation specs, ensuring minimal distinctness."""
        rng = random.Random(seed)
        combos = self.expand_axes(template_id)
        rng.shuffle(combos)
        picks: list[dict[str, Any]] = []
        for c in combos:
            if len(picks) >= n:
                break
            if self._sufficiently_distinct(c, picks, min_distinct_keys):
                picks.append(c)
        return picks

    @staticmethod
    def _sufficiently_distinct(cand, existing, min_keys) -> bool:
        for e in existing:
            diff = sum(1 for k, v in cand.items() if e.get(k) != v)
            if diff < min_keys:
                return False
        return True
