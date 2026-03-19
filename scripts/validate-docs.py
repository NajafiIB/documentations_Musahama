from pathlib import Path
import sys
import re

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = [
    "README.md",
    "AGENTS.md",
    "docs/auth/authentication-flow.md",
]

REF_RE = re.compile(r"(docs|specs)/[a-zA-Z0-9_\-/.]+\.(md|yaml)")

errors = []

for file in REQUIRED_DOCS:
    if not (ROOT / file).exists():
        errors.append(f"Missing doc: {file}")

for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8", errors="ignore")

    if not text.strip():
        errors.append(f"{md}: empty file")

    first_line = next((l for l in text.splitlines() if l.strip()), "")
    if not first_line.startswith("#"):
        errors.append(f"{md}: must start with heading")

    for ref in REF_RE.findall(text):
        ref_path = ref[0]
        if not (ROOT / ref_path).exists():
            errors.append(f"{md}: broken reference {ref_path}")

if errors:
    print("DOC VALIDATION FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("Doc validation passed")
