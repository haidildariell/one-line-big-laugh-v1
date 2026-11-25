#!/usr/bin/env python3
"""One Line, Big Laugh entry: writes a single funny line to /output/entry.txt."""

import os

ENTRY_TEXT = "The warranty covers water damage, so the technician poured a glass of water over my laptop to check if it was really broken."


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry must be 1-200 characters"
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
