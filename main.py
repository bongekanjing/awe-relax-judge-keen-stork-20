#!/usr/bin/env python3
"""Write the competition entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The text is a module-level constant and nothing in the program reads the
clock, a random source, or the locale, so repeated runs are byte-identical.
Only the output directory comes from the environment, defaulting to /output.
"""

import os
from pathlib import Path

TEXT = (
    "Off Greenland, in the year 1000, a mass of cold water sank out of the "
    "wind and began to travel south under the Atlantic, in the dark, over a "
    "floor of pale mud; it is due back at the surface near the Azores around "
    "the year 2500, and the winter it sank with is still in it."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
