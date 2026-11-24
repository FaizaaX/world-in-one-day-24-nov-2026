#!/usr/bin/env python3
"""Entrypoint for 'The World in One Day' - 24 November 2026.

Writes the front-page image for Tuesday 24 November 2026 to
/output/entry.png. The image (news.png) was drawn in this session by
draw_news.py; this program only copies it. Standard library only,
no network, deterministic: two runs write identical bytes.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "news.png"
TARGET = Path("/output/entry.png")


def main() -> None:
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(IMAGE, TARGET)
    print(f"wrote {TARGET} ({TARGET.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
