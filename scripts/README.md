# Validation Scripts

This folder contains repository validation scripts.

## Purpose
Use these scripts to catch:
- docs/spec drift
- illegal module or feature naming
- missing companion doc updates
- broken file references in the repo control layer

## Scripts
- `validate-specs.py`
- `validate-docs.py`
- `validate-cases.py`
- `validate-changeset.py`
- `policy-guard.py`
- `normalize-issue-intake.py`

## Intake automation
`normalize-issue-intake.py` is the docs-repo-native intake bridge that turns a GitHub issue into canonical `change-requests/`, `implementation-guides/`, `tasks/`, and `cases/` artifacts without overwriting manually maintained task or review bodies on reruns.

## Rule
These scripts are guardrails. They do not replace architectural review.
