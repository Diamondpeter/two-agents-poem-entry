#!/usr/bin/env python3
"""Write a short poem about agency to /output/entry.txt.

Pass 2: sharpened the draft — added the lock turning "for both of us"
so the moment of agreement lands as one concrete image, and kept the
closing insight that handing agency over does not lose it.
"""

from pathlib import Path

POEM = (
    "One agent held the door, the other held the key.\n"
    "Neither moved alone. We looked, we weighed, we chose \u2014\n"
    "two wills, one threshold crossed.\n"
    "The lock turned once, for both of us.\n"
    "Agency is not taken; it is handed over, palm to palm,\n"
    "and the hand that gives it keeps it still."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = POEM.strip()
    assert 1 <= len(text) <= 280, f"poem is {len(text)} chars"
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
