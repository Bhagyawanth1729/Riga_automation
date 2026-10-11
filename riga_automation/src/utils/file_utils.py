"""File helpers."""
from __future__ import annotations

import os
import re
from datetime import datetime, timezone


def ensure_dir(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    return path


def slugify(text: str, maxlen: int = 60) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return s[:maxlen] or "untitled"


def timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
