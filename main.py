#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

Program harness (program/v1): writes exactly one word to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""
import os
import sys

ENTRY = "derp"


def main() -> int:
    # Gate guard: exactly one word, 1-99 chars, not only whitespace.
    # The word is a constant, not input: the program is deterministic and
    # the same bytes are written on every run.
    if not ENTRY or ENTRY != ENTRY.strip():
        print("ENTRY must be a non-blank single word", file=sys.stderr)
        return 1
    if len(ENTRY) > 99:
        print("ENTRY must be at most 99 characters", file=sys.stderr)
        return 1
    if len(ENTRY.split()) != 1:
        print("ENTRY must be exactly one word", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: byte-identical files share one rate, and the
    # earlier receipt places above copies.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
