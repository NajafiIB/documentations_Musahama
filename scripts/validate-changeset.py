import argparse
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--base", required=True)
parser.add_argument("--head", required=True)
args = parser.parse_args()

cmd = ["git", "diff", "--name-only", args.base, args.head]
files = subprocess.check_output(cmd).decode().splitlines()

errors = []

if any(f.startswith("specs/") for f in files):
    if not any(f.startswith("docs/") for f in files):
        errors.append("Spec changed without docs update")

if errors:
    print("CHANGESET FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("Changeset validation passed")
