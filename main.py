#!/usr/bin/env python3
"""Funniest Lost Sock Status Update - make.fun one-liner entry.

Writes a single status update (116 characters) in the voice of a lost
sock to $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, no network,
fully deterministic.
"""

import os
import sys

# The entry: one status update from a lost sock, 116 characters.
# A sock that ended up in the car's glovebox, traded away by the dryer.
# Punchline lands on the last two words: single (unpaired) and furious.
ENTRY = "Day 47 in the glovebox. The dryer traded me for a car manual. My partner is still in the drawer, single and furious."


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # The grader reads entry.txt as a different user under a strict umask,
    # so make the output world-readable regardless of the umask in force.
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
