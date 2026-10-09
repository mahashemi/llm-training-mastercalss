#!/usr/bin/env python3
"""Check Course 1 Markdown math delimiters.

This catches common rendering mistakes; it does not prove that equations are
mathematically correct. Worked calculations still require independent review.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path("lectures/00_neural_computing")
EXPECTED_CHAPTERS = 12
INLINE_DOLLAR = re.compile(r"(?<!\\)\$(?!\$)")
DISPLAY_DOLLAR = re.compile(r"(?<!\\)\$\$")
LEGACY_DELIMITERS = (r"\(", r"\)", r"\[", r"\]")
UNSUPPORTED_MACROS = (r"\operatorname", r"\DeclareMathOperator", r"\newcommand")


def strip_inline_code(line: str) -> str:
    """Ignore math-like characters inside Markdown inline-code spans."""
    tick = chr(96)
    return re.sub(tick + r"[^" + tick + r"]*" + tick, "", line)


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    in_fence = False
    in_display = False
    display_open_line = 0
    tick = chr(96)

    for line_number, original in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        stripped = original.strip()

        if stripped.startswith(tick * 3) or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        line = strip_inline_code(original)

        if stripped == "$$":
            in_display = not in_display
            if in_display:
                display_open_line = line_number
            continue

        if in_display:
            continue

        for macro in UNSUPPORTED_MACROS:
            if macro in line:
                errors.append(
                    f"{path}:{line_number}: renderer-incompatible math macro {macro}; "
                    "use a supported upright-text form such as \\mathrm{...}"
                )

        if any(token in line for token in LEGACY_DELIMITERS):
            errors.append(
                f"{path}:{line_number}: use $...$ / $$...$$ instead of "
                r"\(...\) or \[...\]"
            )

        if stripped == "$":
            errors.append(
                f"{path}:{line_number}: stray single-dollar display delimiter"
            )
            continue

        # Inline display math written on one line must have opening and closing
        # $$ markers. Standard standalone $$ lines are handled above.
        display_tokens = DISPLAY_DOLLAR.findall(line)
        if len(display_tokens) % 2:
            errors.append(
                f"{path}:{line_number}: unpaired same-line $$ display delimiter"
            )
            continue

        line_without_display = DISPLAY_DOLLAR.sub("", line)
        inline_tokens = INLINE_DOLLAR.findall(line_without_display)
        if len(inline_tokens) % 2:
            errors.append(
                f"{path}:{line_number}: unmatched inline $ delimiter"
            )

    if in_display:
        errors.append(
            f"{path}:{display_open_line}: display-math block opened but never closed"
        )
    if in_fence:
        errors.append(f"{path}: unclosed fenced code block")

    return errors


def main() -> int:
    lectures = sorted(ROOT.glob("*/lecture.md"))
    if len(lectures) != EXPECTED_CHAPTERS:
        print(
            f"FAIL: expected {EXPECTED_CHAPTERS} Course 1 lecture files, "
            f"found {len(lectures)}",
            file=sys.stderr,
        )
        return 1

    failures: list[str] = []
    for path in lectures:
        errors = check_file(path)
        if errors:
            failures.extend(errors)
        else:
            print(f"PASS {path}")

    if failures:
        print("\nMath delimiter validation failed:", file=sys.stderr)
        print("\n".join(failures), file=sys.stderr)
        return 1

    print(
        f"\nPASS: checked math delimiter consistency in all {len(lectures)} "
        "Course 1 lectures. This is a rendering check, not a semantic proof."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
