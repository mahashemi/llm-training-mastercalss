#!/usr/bin/env python3
"""Validate math delimiters and renderer compatibility in Course 1 lectures and labs.

This is a rendering/syntax guard, not a proof that every equation is mathematically
correct. Worked calculations and model implementations still need independent review.
"""

from __future__ import annotations

import json
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


def check_text(label: str, text: str) -> list[str]:
    errors: list[str] = []
    in_fence = False
    in_display = False
    display_open_line = 0
    tick = chr(96)

    for line_number, original in enumerate(text.splitlines(), start=1):
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

        # Check renderer-incompatible commands inside and outside display math.
        for macro in UNSUPPORTED_MACROS:
            if macro in line:
                errors.append(
                    f"{label}:{line_number}: renderer-incompatible math macro {macro}; "
                    r"use a supported upright-text form such as \mathrm{...}"
                )

        if in_display:
            continue

        if any(token in line for token in LEGACY_DELIMITERS):
            errors.append(
                f"{label}:{line_number}: use $...$ / $$...$$ instead of "
                r"\(...\) or \[...\]"
            )

        if stripped == "$":
            errors.append(
                f"{label}:{line_number}: stray single-dollar display delimiter"
            )
            continue

        display_tokens = DISPLAY_DOLLAR.findall(line)
        if len(display_tokens) % 2:
            errors.append(
                f"{label}:{line_number}: unpaired same-line $$ display delimiter"
            )
            continue

        line_without_display = DISPLAY_DOLLAR.sub("", line)
        inline_tokens = INLINE_DOLLAR.findall(line_without_display)
        if len(inline_tokens) % 2:
            errors.append(
                f"{label}:{line_number}: unmatched inline $ delimiter"
            )

    if in_display:
        errors.append(
            f"{label}:{display_open_line}: display-math block opened but never closed"
        )
    if in_fence:
        errors.append(f"{label}: unclosed fenced code block")

    return errors


def check_file(path: Path) -> list[str]:
    return check_text(str(path), path.read_text(encoding="utf-8"))


def check_notebook(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid notebook JSON: {exc}"]

    for index, cell in enumerate(notebook.get("cells", [])):
        if cell.get("cell_type") != "markdown":
            continue
        source = cell.get("source", "")
        if isinstance(source, list):
            source = "".join(source)
        errors.extend(check_text(f"{path}:markdown cell {index}", source))
    return errors


def main() -> int:
    lectures = sorted(ROOT.glob("*/lecture.md"))
    notebooks = sorted(ROOT.glob("*/lab.ipynb"))
    if len(lectures) != EXPECTED_CHAPTERS:
        print(
            f"FAIL: expected {EXPECTED_CHAPTERS} Course 1 lecture files, "
            f"found {len(lectures)}",
            file=sys.stderr,
        )
        return 1
    if len(notebooks) != EXPECTED_CHAPTERS:
        print(
            f"FAIL: expected {EXPECTED_CHAPTERS} Course 1 lab notebooks, "
            f"found {len(notebooks)}",
            file=sys.stderr,
        )
        return 1

    failures: list[str] = []
    for path in lectures:
        errors = check_file(path)
        if errors:
            failures.extend(errors)
        else:
            print(f"PASS math: {path}")

    for path in notebooks:
        errors = check_notebook(path)
        if errors:
            failures.extend(errors)
        else:
            print(f"PASS math: {path}")

    if failures:
        print("\nCourse 1 math validation failed:", file=sys.stderr)
        print("\n".join(failures), file=sys.stderr)
        return 1

    print(
        f"\nPASS: checked math delimiters and renderer compatibility in all "
        f"{len(lectures)} lectures and {len(notebooks)} lab notebooks. "
        "This is a rendering check, not a semantic proof."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
