"""Utilities for simple scientific note summarization."""

from __future__ import annotations

import re
from collections.abc import Iterable

DEFAULT_KEYWORDS = (
    "biology",
    "neuroscience",
    "bioinformatics",
    "data",
    "machine learning",
    "brain",
    "computational biology",
    "single-cell",
    "single-cell rna-seq",
    "fibrosis",
    "immune response",
    "macrophage",
    "fibroblast",
    "myofibroblast",
    "extracellular matrix",
    "organoid",
    "biomedical ai",
    "genomics",
    "protein",
    "cell",
)


def _plain_text(note: str) -> str:
    lines = []
    for line in note.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith(("- ", "* ")):
            stripped = stripped[2:].strip()
        lines.append(stripped)
    return " ".join(lines)


def _split_sentences(note: str) -> list[str]:
    return [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", _plain_text(note))
        if sentence.strip()
    ]


def summarize_note(note: str, max_sentences: int = 2) -> str:
    """Return the first meaningful sentences from a study note."""

    if max_sentences < 1:
        raise ValueError("max_sentences must be at least 1")

    sentences = _split_sentences(note)
    if not sentences:
        return ""

    return " ".join(sentences[:max_sentences])


def extract_keywords(
    note: str,
    keywords: Iterable[str] = DEFAULT_KEYWORDS,
) -> list[str]:
    """Find known scientific keywords in a note, preserving keyword order."""

    lower_note = note.lower()
    found_keywords = []

    for keyword in keywords:
        normalized_keyword = keyword.lower()
        pattern = re.escape(normalized_keyword).replace(r"\ ", r"\s+")
        if " " not in normalized_keyword and not normalized_keyword.endswith("s"):
            pattern = f"{pattern}s?"
        if re.search(rf"(?<![a-z0-9-]){pattern}(?![a-z0-9-])", lower_note):
            found_keywords.append(keyword)

    return found_keywords
