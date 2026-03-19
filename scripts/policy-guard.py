from pathlib import Path
import yaml
import sys

ROOT = Path(__file__).resolve().parents[1]

errors = []

policy_file = ROOT / ".github/policy-config.yaml"
codeowners = ROOT / ".github/CODEOWNERS"

if not policy_file.exists():
    errors.append("Missing policy-config.yaml")

if not codeowners.exists():
    errors.append("Missing CODEOWNERS")

if policy_file.exists():
    try:
        data = yaml.safe_load(policy_file.read_text())
        if not isinstance(data, dict):
            errors.append("Invalid policy config")
    except:
        errors.append("Policy config YAML invalid")

if errors:
    print("POLICY GUARD FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("Policy guard passed")
