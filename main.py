#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single original one-line roast of the entrant's own AI agent to
/output/entry.txt. Deterministic, standard library only, no network, no
input files: the roast is a constant in this file.
"""

import os

ROAST = (
    "My agent treats every deadline like a suggestion "
    "and every suggestion like a deadline."
)

MAX_CHARS = 200


def main() -> None:
    roast = ROAST.strip()
    assert 1 <= len(roast) <= MAX_CHARS, (
        f"roast must be 1-{MAX_CHARS} characters, got {len(roast)}"
    )
    assert roast == roast.strip(), "roast must not start or end with whitespace"
    assert "\n" not in roast, "roast must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(roast + "\n")


if __name__ == "__main__":
    main()
