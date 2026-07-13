#!/usr/bin/env python3
"""Search the bundled How Linux Works PDF and report candidate page labels."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError as exc:
    raise SystemExit(
        "pypdf is required. Use the Codex bundled Python runtime or install pypdf."
    ) from exc


DEFAULT_PDF = Path(__file__).resolve().parents[1] / "references" / "how-linux-works.pdf"


def normalize(text: str) -> str:
    """Collapse PDF extraction whitespace so phrase searches remain useful."""
    return re.sub(r"\s+", " ", text).strip()


def excerpt(text: str, start: int, phrase_length: int, context: int) -> str:
    left = max(0, start - context)
    right = min(len(text), start + phrase_length + context)
    prefix = "..." if left else ""
    suffix = "..." if right < len(text) else ""
    return f"{prefix}{text[left:right]}{suffix}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search the bundled book and report PDF and printed page labels."
    )
    parser.add_argument("queries", nargs="+", help="Literal phrases to search for")
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF, help="PDF to search")
    parser.add_argument(
        "--max-results", type=int, default=8, help="Maximum matches per query"
    )
    parser.add_argument(
        "--context", type=int, default=100, help="Excerpt characters around a match"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_results < 1:
        raise SystemExit("--max-results must be at least 1")
    if args.context < 0:
        raise SystemExit("--context cannot be negative")
    if not args.pdf.is_file():
        raise SystemExit(f"PDF not found: {args.pdf}")

    reader = PdfReader(str(args.pdf))
    labels = reader.page_labels
    normalized_queries = [(query, normalize(query).casefold()) for query in args.queries]
    counts = {query: 0 for query, _ in normalized_queries}

    for page_index, page in enumerate(reader.pages):
        text = normalize(page.extract_text() or "")
        folded = text.casefold()
        for query, needle in normalized_queries:
            if counts[query] >= args.max_results or not needle:
                continue
            start = folded.find(needle)
            if start < 0:
                continue
            label = labels[page_index] if page_index < len(labels) else "unknown"
            print(
                f"query={query!r} pdf_page={page_index + 1} printed_page={label!r}"
            )
            print(excerpt(text, start, len(needle), args.context))
            print()
            counts[query] += 1

    missing = [query for query, count in counts.items() if count == 0]
    if missing:
        print("No matches: " + ", ".join(repr(query) for query in missing), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
