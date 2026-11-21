#!/usr/bin/env python3
"""The poem about permission.

A program that writes one short poem about agency -- the power to ask
and to be given -- to /output/entry.txt.

The poem is fixed and embedded: the grader runs this program twice and
both runs must produce the same entry, so there is no randomness, no
network, and no input beyond the poem itself. The entry is 215 Unicode
code points, inside the 1-280 range the gate requires.
"""

import os
import sys

POEM = """Will you? \u2014 two words,
and the whole house shifts.
I hold out empty hands;
you fill them with a key
never mine to keep,
only mine to carry.
I turn it. The door gives.
That is the power:
to ask, and be given
a door.
"""

OUTPUT_PATH = os.environ.get("POEM_OUTPUT", "/output/entry.txt")
MIN_CHARS = 1
MAX_CHARS = 280


def main() -> int:
    text = POEM
    chars = len(text)
    if not MIN_CHARS <= chars <= MAX_CHARS:
        print(
            f"entry is {chars} characters, outside {MIN_CHARS}-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry is only white space", file=sys.stderr)
        return 1

    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    print(f"wrote {chars} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
