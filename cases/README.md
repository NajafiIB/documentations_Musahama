# Cases

This folder stores the machine-readable delivery state for the Musahama documentation process.

## Purpose

Use a case manifest to tie together:

- the source issue
- the parent change request
- the parent implementation guide
- the ordered task list
- review history
- implementation evidence
- QA evidence
- closure evidence

## Format Rule

Case manifests use **JSON-compatible YAML** so they remain easy for humans to inspect and deterministic for agents and scripts to read and write.

That means:

- the file extension remains `.yaml`
- the content must still parse as valid JSON
- comments should not be added inside the manifest body

## Naming

Use `CASE-YYYY-NNN.yaml`.

## Lifecycle Rules

1. each case must reference one canonical source issue
2. each case must reference one change request and one implementation guide
3. each task listed in the case must map to a real task document
4. only one task may be `active` within a case in v1
5. only one case may be `in_implementation` or `ready_for_qa` across the queue in v1
6. a case may not close until docs, implementation, and QA evidence all agree
