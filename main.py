#!/usr/bin/env python3
"""Make the Judge Laugh in One Line - entry program (pure stdlib).

Writes the chosen one-liner to /output/entry.txt.
"""

from pathlib import Path

LINE = "My grandfather warned me never to trust a man with two first names. His name was James James."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Self-check against the gate: 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
