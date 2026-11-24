#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one funny line roasting my own AI agent to /output/entry.txt.
"""

import os

LINE = "I gave my agent one job. It did three, documented none, and called it initiative."


def validate(text):
    """Mirror the bounty gate: UTF-8 text, 1-200 chars, not only whitespace,
    a single line. Raise ValueError on anything the gate would refuse."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
