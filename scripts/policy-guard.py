from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
policy_path = ROOT / '.github' / 'policy-config.yaml'
codeowners_path = ROOT / '.github' / 'CODEOWNERS'
errors = []

if not policy_path.exists():
    errors.append('missing .github/policy-config.yaml')
else:
    try:
        data = yaml.safe_load(policy_path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'policy-config.yaml invalid YAML: {exc}')
        data = {}
    if not isinstance(data, dict):
        errors.append('policy-config.yaml root must be a mapping')
    else:
        for key in ('schema_version', 'last_updated', 'owner', 'status', 'canonical_modules'):
            if not data.get(key):
                errors.append(f'policy-config.yaml missing field {key}')

if not codeowners_path.exists():
    errors.append('missing .github/CODEOWNERS')

if errors:
    print('POLICY GUARD FAILED', file=sys.stderr)
    for err in errors:
        print(f'- {err}', file=sys.stderr)
    raise SystemExit(1)

print('Policy guard passed.')
