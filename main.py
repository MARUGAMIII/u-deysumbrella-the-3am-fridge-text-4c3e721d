#!/usr/bin/env python3
"""The 3AM Fridge Text -- make.fun entry.

A smart fridge texts its owner at 3am. One line, one joke.

The program writes exactly one text to /output/entry.txt. The gate
requires UTF-8 text of 1 to 140 characters, not only whitespace.
Runs with the standard library only, no network.
"""

import os

ENTRY_TEXT = (
    "It's 3am. 11 visits tonight, 0 snacks eaten. "
    "I've decided we're in a relationship now."
)


def main() -> None:
    text = ENTRY_TEXT.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
