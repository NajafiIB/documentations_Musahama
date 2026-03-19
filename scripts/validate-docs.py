from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md',
    'AGENTS.md',
    'docs/auth/authentication-flow.md',
    'docs/authorization/authorization-foundation.md',
    'docs/database/database-foundation.md',
    'docs/feature-system/feature-system-foundation.md',
    'docs/services/services-foundation.md',
    'docs/frontend/frontend-foundation.md',
    'docs/workflows/workflows-foundation.md',
    'docs/dev-guides/developer-onboarding.md',
]
REF_RE = re.compile(r'(docs|specs|change-requests|implementation-guides|reviews|tasks)/[A-Za-z0-9._/\-\[\]]+\.(md|ya?ml)')
errors = []

for rel in REQUIRED:
    if not (ROOT / rel).exists():
        errors.append(f'missing required file: {rel}')

for path in ROOT.rglob('*.md'):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8', errors='replace')
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        errors.append(f'{path.relative_to(ROOT)}: file is empty')
        continue
    if not lines[0].startswith('# '):
        errors.append(f'{path.relative_to(ROOT)}: first non-empty line must be a markdown H1 heading')
    for match in REF_RE.finditer(text):
        rel = match.group(0)
        if not (ROOT / rel).exists():
            errors.append(f'{path.relative_to(ROOT)}: referenced file does not exist: {rel}')

if errors:
    print('DOC VALIDATION FAILED', file=sys.stderr)
    for err in errors:
        print(f'- {err}', file=sys.stderr)
    raise SystemExit(1)

print('Doc validation passed.')
