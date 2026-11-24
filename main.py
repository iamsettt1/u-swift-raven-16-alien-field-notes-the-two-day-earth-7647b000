"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text: a review of planet Earth
left by an alien tourist. Deterministic: a fixed string, no
randomness, no network, no reads outside this repository.
"""

import os

ENTRY = (
    "Earth review: the dominant species is the dog \u2014 it cannot "
    "open doors, pays no rent, and is worshipped anyway. "
    "Five stars, would be ruled again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
