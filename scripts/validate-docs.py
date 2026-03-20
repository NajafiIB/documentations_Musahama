#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT_FILES = [
    "README.md",
    "AGENTS.md",
]

REQUIRED_PROCESS_FILES = [
    "change-requests/README.md",
    "change-requests/CR-template.md",
    "implementation-guides/README.md",
    "implementation-guides/IMP-template.md",
    "reviews/README.md",
    "reviews/RV-template.md",
    "tasks/README.md",
    "tasks/TASK-template.md",
    "scripts/README.md",
]

REQUIRED_FOUNDATION_DOCS = [
    "docs/auth/authentication-flow.md",
    "docs/authorization/authorization-foundation.md",
    "docs/database/database-foundation.md",
    "docs/feature-system/feature-system-foundation.md",
    "docs/services/services-foundation.md",
    "docs/frontend/frontend-foundation.md",
    "docs/workflows/workflows-foundation.md",
    "docs/dev-guides/developer-onboarding.md",
]

REFERENCE_RE = re.compile(
    r"(?P<path>(docs|specs|change-requests|implementation-guides|reviews|tasks|scripts|\.github)/[A-Za-z0-9._/\-\[\]]+\.(md|ya?ml|py))"
)

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def ensure(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def validate_required_files() -> None:
    for relative_path in REQUIRED_ROOT_FILES + REQUIRED_PROCESS_FILES + REQUIRED_FOUNDATION_DOCS:
        ensure((ROOT / relative_path).exists(), f"Missing required file: {relative_path}")


def first_non_empty_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ""


def validate_markdown_file(path: Path) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        fail(f"{path.as_posix()}: failed to read file: {exc}")
        return

    ensure(text.strip() != "", f"{path.as_posix()}: file is empty")

    first_line = first_non_empty_line(text)
    ensure(first_line.startswith("# "), f"{path.as_posix()}: first non-empty line must be a markdown H1 heading")

    for match in REFERENCE_RE.finditer(text):
        relative_ref = match.group("path")
        ensure((ROOT / relative_ref).exists(), f"{path.as_posix()}: referenced file does not exist: {relative_ref}")


def main() -> int:
    validate_required_files()

    for markdown_path in ROOT.rglob("*.md"):
        if ".git" in markdown_path.parts:
            continue
        validate_markdown_file(markdown_path)

    if errors:
        print("DOC VALIDATION FAILED", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        return 1

    print("Doc validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
