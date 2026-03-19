import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES = [
    ('specs/modules/', ['docs/feature-system/', 'docs/frontend/', 'docs/authorization/']),
    ('specs/roles/', ['docs/authorization/', 'docs/feature-system/']),
    ('specs/routes/', ['docs/frontend/', 'docs/auth/', 'docs/authorization/']),
    ('specs/features/', ['docs/feature-system/', 'docs/authorization/', 'docs/services/']),
    ('specs/workflows/', ['docs/workflows/', 'docs/services/', 'docs/frontend/']),
    ('specs/database/', ['docs/database/', 'docs/services/', 'docs/workflows/']),
    ('specs/providers/', ['docs/feature-system/', 'docs/services/']),
]

parser = argparse.ArgumentParser()
parser.add_argument('--base', required=True)
parser.add_argument('--head', required=True)
args = parser.parse_args()

if set(args.base) == {'0'}:
    print('Base SHA is all zeros. Skipping changeset validation.')
    raise SystemExit(0)

cmd = f"cd '{ROOT}' && git diff --name-only --diff-filter=ACMRTUXB {args.base} {args.head}"
output = os.popen(cmd).read()
files = [line.strip() for line in output.splitlines() if line.strip()]
errors = []
for trigger, companions in RULES:
    if not any(path.startswith(trigger) for path in files):
        continue
    if not any(any(path.startswith(prefix) for prefix in companions) for path in files):
        errors.append(f'changes under {trigger} require companion doc updates under {companions}')

if errors:
    print('CHANGESET VALIDATION FAILED', file=sys.stderr)
    for err in errors:
        print(f'- {err}', file=sys.stderr)
    raise SystemExit(1)
print('Changeset validation passed.')
