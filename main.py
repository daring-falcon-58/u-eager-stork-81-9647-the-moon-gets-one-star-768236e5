#!/usr/bin/env python3
"""The Moon Gets One Star — entry program (program/v1).

Writes the tournament-winning one-star review of the Moon to
/output/entry.txt (gate: UTF-8 text, 1-120 characters).
"""

import os

ENTRY = "One star. Leaving me at 3.8cm a year. Slowest breakup in history, and it won't even text back."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: the gate refuses anything outside 1-120 chars,
    # so re-check the exact bytes we just wrote before exiting.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the winning line"
    assert 1 <= len(written) <= 120, f"entry is {len(written)} chars, gate needs 1-120"
    print(f"entry.txt OK: {len(written)} characters")


if __name__ == "__main__":
    main()
