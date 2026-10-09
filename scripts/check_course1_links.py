#!/usr/bin/env python3
"""Validate local links and image paths in Course 1 lecture Markdown."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path("lectures/00_neural_computing")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def local_targets(path: Path):
    in_fence = False
    tick = chr(96)
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        stripped = line.strip()
        if stripped.startswith(tick * 3) or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK.finditer(line):
            target = match.group(1).strip().split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(
                ("http://", "https://", "mailto:", "#", "data:")
            ):
                continue
            yield line_number, unquote(target)


def main() -> int:
    lectures = sorted(ROOT.glob("*/lecture.md"))
    if len(lectures) != 12:
        print(f"FAIL: expected 12 Course 1 lectures, found {len(lectures)}", file=sys.stderr)
        return 1

    failures = []
    for source in lectures:
        for line_number, target in local_targets(source):
            if target.startswith("/"):
                resolved = Path(target.lstrip("/"))
            else:
                resolved = source.parent / target
            if not resolved.exists():
                failures.append(
                    f"{source}:{line_number}: broken local link {target!r} "
                    f"(resolved as {resolved})"
                )
        if not any(item.startswith(f"{source}:") for item in failures):
            print(f"PASS {source}")

    if failures:
        print("\nBroken Course 1 links:", file=sys.stderr)
        print("\n".join(failures), file=sys.stderr)
        return 1

    print(f"\nPASS: local links and image paths validated in all {len(lectures)} lectures.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
