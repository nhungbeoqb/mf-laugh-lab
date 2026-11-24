#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

The excuse a robot vacuum gives after eating a sock.
Writes one short funny line to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

# v2 (genuine revision): tightened to one flowing escalation and gave the
# third beat a concrete embodied image -- the laundry basket seizing the
# charging cable (the vacuum's lifeline) as evidence, instead of the vaguer
# "under investigation". The joke now escalates: ate it, report filed,
# evidence seized.
JOKE = (
    "I ate the sock. Its partner filed a missing-person report, "
    "and the laundry basket has seized my charging cable as evidence."
)


def main() -> None:
    line = JOKE.strip()
    if not line or line != JOKE.strip():
        raise SystemExit("joke must be a single non-empty line")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"joke must be 1-200 characters, got {len(line)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
