from pathlib import Path
import datetime as dt
import re
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
ALLOWED_STATUS = {'draft', 'approved', 'superseded', 'archived'}
FEATURE_KEY_RE = re.compile(r'^[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)+$')
CANONICAL_MODULES = {'dashboard','crm_opportunities','mandates','research','results','companies','contacts','integrations','billing','settings'}
CANONICAL_ROLES = {'owner','admin','manager','analyst','member','billing_admin','developer'}
PROVIDER_TOKENS = {'openai','lusha','crm_connector','search_provider'}
errors = []

def err(msg):
    errors.append(msg)

specs = {}
for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists():
        err(f'missing required spec file: {rel}')
        continue
    try:
        data = yaml.safe_load(path.read_text(encoding='utf-8'))
    except Exception as exc:
        err(f'{rel}: invalid YAML: {exc}')
        continue
    if not isinstance(data, dict):
        err(f'{rel}: root must be a mapping')
        continue
    specs[rel] = data
    for key in ('schema_version','last_updated','owner','status'):
        if not data.get(key):
            err(f'{rel}: missing metadata field {key}')
    if data.get('last_updated'):
        try:
            dt.date.fromisoformat(str(data['last_updated']))
        except ValueError:
            err(f'{rel}: last_updated must be YYYY-MM-DD')
    if data.get('status') and data['status'] not in ALLOWED_STATUS:
        err(f"{rel}: invalid status {data['status']}")
    refs = data.get('references', {})
    if isinstance(refs, dict):
        for doc in refs.get('docs', []) if isinstance(refs.get('docs', []), list) else []:
            if isinstance(doc, str) and not (ROOT / doc).exists():
                err(f'{rel}: referenced doc does not exist: {doc}')

modules = specs.get('specs/modules/module-catalog.yaml', {}).get('canonical_modules', [])
module_keys = {m.get('key') for m in modules if isinstance(m, dict) and m.get('key')}
if module_keys != CANONICAL_MODULES:
    err(f'canonical module keys mismatch: {sorted(module_keys)}')

roles = specs.get('specs/roles/role-matrix.yaml', {}).get('roles', [])
role_keys = {r.get('key') for r in roles if isinstance(r, dict) and r.get('key')}
if role_keys != CANONICAL_ROLES:
    err(f'canonical role keys mismatch: {sorted(role_keys)}')

route_groups = specs.get('specs/routes/route-map.yaml', {}).get('route_groups', {})
public_routes = route_groups.get('public', {}).get('routes', []) if isinstance(route_groups, dict) else []
protected_routes = route_groups.get('protected_workspace', {}).get('routes', []) if isinstance(route_groups, dict) else []
public_paths = {r.get('path') for r in public_routes if isinstance(r, dict) and r.get('path')}
for needed in {'/login','/register','/forgot-password','/invite/[token]','/auth/callback'}:
    if needed not in public_paths:
        err(f'missing public auth route: {needed}')
protected_modules = {r.get('module_key') for r in protected_routes if isinstance(r, dict) and r.get('module_key')}
if not CANONICAL_MODULES.issubset(protected_modules):
    err('not all canonical modules appear in protected routes')

features = specs.get('specs/features/feature-catalog.yaml', {}).get('features', [])
feature_keys = set()
for feat in features:
    if not isinstance(feat, dict):
        continue
    key = feat.get('key')
    module_key = feat.get('module_key')
    if key:
        if FEATURE_KEY_RE.fullmatch(key) is None:
            err(f'invalid feature key syntax: {key}')
        for token in PROVIDER_TOKENS:
            if token in key:
                err(f'provider token {token} must not appear in feature key {key}')
        feature_keys.add(key)
    if module_key and module_key not in CANONICAL_MODULES:
        err(f'feature references unknown module key: {module_key}')

provider_map = specs.get('specs/providers/provider-capabilities.yaml', {}).get('feature_to_capability_map', {})
if isinstance(provider_map, dict):
    for feature_key in provider_map.keys():
        if feature_key not in feature_keys:
            err(f'provider capability map references unknown feature: {feature_key}')

if errors:
    print('SPEC VALIDATION FAILED', file=sys.stderr)
    for e in errors:
        print(f'- {e}', file=sys.stderr)
    raise SystemExit(1)
print('Spec validation passed.')
