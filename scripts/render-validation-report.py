import json
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--spec-exit", type=int)
parser.add_argument("--docs-exit", type=int)
parser.add_argument("--cases-exit", type=int)
parser.add_argument("--changeset-exit", type=int)

parser.add_argument("--spec-log", type=Path)
parser.add_argument("--docs-log", type=Path)
parser.add_argument("--cases-log", type=Path)
parser.add_argument("--changeset-log", type=Path)

parser.add_argument("--out-md", type=Path)
parser.add_argument("--out-json", type=Path)

args = parser.parse_args()

def read(p):
    return p.read_text() if p.exists() else ""

report = {
    "spec": args.spec_exit,
    "docs": args.docs_exit,
    "cases": args.cases_exit,
    "changeset": args.changeset_exit,
}

md = [
    "# Validation Report",
    "",
    f"Spec: {'PASS' if args.spec_exit == 0 else 'FAIL'}",
    f"Docs: {'PASS' if args.docs_exit == 0 else 'FAIL'}",
    f"Cases: {'PASS' if args.cases_exit == 0 else 'FAIL'}",
    f"Changeset: {'PASS' if args.changeset_exit == 0 else 'FAIL'}",
    "",
]

md.append("## Logs")
md.append("```")
md.append(read(args.spec_log))
md.append(read(args.docs_log))
md.append(read(args.cases_log))
md.append(read(args.changeset_log))
md.append("```")

args.out_md.write_text("\n".join(md))
args.out_json.write_text(json.dumps(report, indent=2))

print("Report generated")
