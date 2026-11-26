#!/usr/bin/env python3
"""Write one funny line to entry.txt.

Deterministic: the same bytes are written on every run.
Standard library only, no network access.
"""

import os

LINE = "My smartwatch congratulated me on 10,000 steps \u2014 every single one of them between the fridge and the sofa."

MAX_CHARS = 200


def validate(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, over the {MAX_CHARS} limit")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
