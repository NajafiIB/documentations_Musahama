#!/usr/bin/env python3

from pathlib import Path
import datetime as dt
import yaml
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "specs/modules/module-catalog.yaml",
    "specs/roles/role-matrix.yaml",
    "specs/routes/route-map.yaml",
    "specs/features/feature-catalog.yaml",
    "specs/workflows/workflow-map.yaml",
    "specs/database/source-of-truth.yaml",
    "specs/providers/provider-capabilities.yaml",
]

errors = []

def fail(msg):
    errors.append(msg)

for file in REQUIRED_FILES:
    path = ROOT / file
    if not path.exists():
        fail(f"Missing spec file: {file}")
        continue

    try:
        data = yaml.safe_load(path.read_text())
    except Exception as e:
        fail(f"{file}: invalid YAML → {e}")
        continue

    if not isinstance(data, dict):
        fail(f"{file}: root must be dict")
        continue

    for key in ["schema_version", "last_updated", "owner", "status"]:
        if key not in data:
            fail(f"{file}: missing {key}")

    try:
        dt.date.fromisoformat(str(data["last_updated"]))
    except:
        fail(f"{file}: invalid date format")

if errors:
    print("SPEC VALIDATION FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("Spec validation passed")
