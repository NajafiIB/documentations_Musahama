import argparse
import json
from pathlib import Path

MARKER = '<!-- validation-report -->'


def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8', errors='replace') if path.exists() else ''


def parse_failures(text: str) -> list[str]:
    return [line[2:].strip() for line in text.splitlines() if line.strip().startswith('- ')]


def excerpt(text: str, max_lines: int = 40) -> str:
    lines = [line.rstrip() for line in text.splitlines() if line.strip()]
    if not lines:
        return '_no output_'
    return '\n'.join(lines[:max_lines] + ([] if len(lines) <= max_lines else ['…']))


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument('--spec-exit', type=int, required=True)
    p.add_argument('--docs-exit', type=int, required=True)
    p.add_argument('--changeset-exit', type=int, required=True)
    p.add_argument('--spec-log', type=Path, required=True)
    p.add_argument('--docs-log', type=Path, required=True)
    p.add_argument('--changeset-log', type=Path, required=True)
    p.add_argument('--out-md', type=Path, required=True)
    p.add_argument('--out-json', type=Path, required=True)
    args = p.parse_args()

    spec_log = read_text(args.spec_log)
    docs_log = read_text(args.docs_log)
    changeset_log = read_text(args.changeset_log)
    overall_ok = args.spec_exit == 0 and args.docs_exit == 0 and args.changeset_exit == 0

    report = {
        'overall_ok': overall_ok,
        'checks': {
            'specs': {'exit_code': args.spec_exit, 'failures': parse_failures(spec_log)},
            'docs': {'exit_code': args.docs_exit, 'failures': parse_failures(docs_log)},
            'changeset': {'exit_code': args.changeset_exit, 'failures': parse_failures(changeset_log)},
        },
    }

    md = [MARKER, '# Repo validation report', '', f"**Overall:** {'✅ PASS' if overall_ok else '❌ FAIL'}", '']
    md += ['| Check | Result |', '|---|---|']
    md += [f"| Spec validation | {'PASS' if args.spec_exit == 0 else 'FAIL'} |"]
    md += [f"| Doc validation | {'PASS' if args.docs_exit == 0 else 'FAIL'} |"]
    md += [f"| Changeset validation | {'PASS' if args.changeset_exit == 0 else 'FAIL'} |", '']
    for title, code, log in [('Spec validation', args.spec_exit, spec_log), ('Doc validation', args.docs_exit, docs_log), ('Changeset validation', args.changeset_exit, changeset_log)]:
        md += [f'## {title}', '']
        if code == 0:
            md += ['- no issues detected', '']
            continue
        failures = parse_failures(log)
        md += ['### Failure summary', '']
        md += [f'- {f}' for f in failures[:20]] or ['- no parsed failure lines']
        md += ['', '<details>', f'<summary>Show raw {title.lower()} output</summary>', '', '```text', excerpt(log), '```', '</details>', '']
    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.write_text('\n'.join(md), encoding='utf-8')
    args.out_json.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(f'Wrote markdown report to {args.out_md}')
    print(f'Wrote JSON report to {args.out_json}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
