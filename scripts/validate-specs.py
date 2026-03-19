from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'specs/modules/module-catalog.yaml',
    'specs/roles/role-matrix.yaml',
    'specs/routes/route-map.yaml',
    'specs/features/feature-catalog.yaml',
    'specs/workflows/workflow-map.yaml',
    'specs/database/source-of-truth.yaml',
    'specs/providers/provider-capabilities.yaml',
]
errors = []
for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists():
        errors.append(f'missing required spec file: {rel}')
        continue
    try:
        data = yaml.safe_load(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{rel}: invalid YAML: {exc}')
        continue
    if not isinstance(data, dict):
        errors.append(f'{rel}: root must be a mapping')
        continue
    for key in ('schema_version', 'last_updated', 'owner', 'status'):
        if not data.get(key):
            errors.append(f'{rel}: missing metadata field {key}')
if errors:
    print('SPEC VALIDATION FAILED', file=sys.stderr)
    for e in errors:
        print(f'- {e}', file=sys.stderr)
    raise SystemExit(1)
print('Spec validation passed.')
