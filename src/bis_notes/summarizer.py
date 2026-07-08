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
    in_code_block = False
    for line in note.splitlines():
        stripped = line.strip()

        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
            continue

        if in_code_block or not stripped:
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            level, heading_text = heading.groups()
            if len(level) == 1:
                continue
            stripped = heading_text.strip()
            if stripped and stripped[-1] not in ".!?":
                stripped = f"{stripped}."

        stripped = re.sub(r"^[-*+]\s+\[[ xX]\]\s+", "", stripped)
        if stripped.startswith(("- ", "* ", "+ ")):
            stripped = stripped[2:].strip()
        stripped = re.sub(r"^\d+[.)]\s+", "", stripped)
        stripped = re.sub(r"^>\s*", "", stripped)
        stripped = re.sub(r"`([^`]+)`", r"\1", stripped)
        stripped = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", stripped)

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
