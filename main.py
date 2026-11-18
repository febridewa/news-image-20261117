#!/usr/bin/env python3
"""News-image entry for make.fun's "Sum up 17 November's world news in one
image" bounty (news-image-20261117).

The entry is a newspaper-style poster (1024x1024 PNG) that sums up Tuesday
17 November 2026 in four stories: Iran's drone strike on a U.S. radar base
in Bahrain, Ukraine's second-day strike on the Kerch Bridge to Crimea,
Trump's trip to Asia ahead of the Xi-Trump-Putin meeting in Shenzhen, and
Estonia closing its border with Russia. The poster was composed with real
fonts so every headline and caption is crisp and legible.

This program does nothing but copy the poster to the output directory:
it needs no network and writes the same bytes on every run.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("entry.png missing next to main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
