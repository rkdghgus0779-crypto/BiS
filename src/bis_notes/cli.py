"""Command line interface for BiS note helpers."""

from __future__ import annotations

import argparse
from pathlib import Path

from .summarizer import extract_keywords, summarize_note


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bis-notes",
        description="Summarize study notes and extract beginner-friendly science keywords.",
    )
    parser.add_argument("note_file", type=Path, help="Path to a Markdown or text note")
    parser.add_argument(
        "--sentences",
        type=int,
        default=2,
        help="Number of sentences to include in the summary",
    )
    parser.add_argument(
        "--keywords-only",
        action="store_true",
        help="Print only extracted keywords",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    note = args.note_file.read_text(encoding="utf-8")
    keywords = extract_keywords(note)

    if not args.keywords_only:
        print("Summary:")
        print(summarize_note(note, max_sentences=args.sentences))
        print()

    print("Keywords:")
    print(", ".join(keywords) if keywords else "No known keywords found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
