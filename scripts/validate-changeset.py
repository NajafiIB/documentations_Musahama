import argparse
import subprocess
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

def changed_files(base: str, head: str) -> list[str]:
    result = subprocess.run(
        ['git', 'diff', '--name-only', '--diff-filter=ACMRTUXB', base, head],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(result.stderr.strip() or 'git diff failed', file=sys.stderr)
        raise SystemExit(1)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]

parser = argparse.ArgumentParser()
parser.add_argument('--base', required=True)
parser.add_argument('--head', required=True)
args = parser.parse_args()

if set(args.base) == {'0'}:
    print('Base SHA is all zeros. Skipping changeset validation.')
    raise SystemExit(0)

files = changed_files(args.base, args.head)
errors = []
for trigger, companions in RULES:
    triggered = any(path.startswith(trigger) for path in files)
    if not triggered:
        continue
    companion_found = any(any(path.startswith(prefix) for prefix in companions) for path in files)
    if not companion_found:
        errors.append(f'changes under {trigger} require companion doc updates under {companions}')

if errors:
    print('CHANGESET VALIDATION FAILED', file=sys.stderr)
    for e in errors:
        print(f'- {e}', file=sys.stderr)
    raise SystemExit(1)
print('Changeset validation passed.')
