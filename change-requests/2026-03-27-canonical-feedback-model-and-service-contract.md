# Change Request — Canonical Feedback Model and Service Contract

## Status
- done

## Problem

The repository now defines the workflow split between Research and Results, and it defines the UI idea of positive signals, constraints, shortlist actions, and reject actions.

What is still missing is the canonical model for how feedback is represented and the canonical service contract for how feedback is written and consumed.

Without that, the UI can look correct while the data model and service behavior drift.

## Expected behavior

The repository must define:
- the canonical feedback data model
- the canonical statuses for candidates and proposals
- the relationship between feedback, rules, and results cases
- the service contract for shortlist, reject, proposal approval, proposal dismissal, and finalization flows

## Affected areas

- `docs/database/research-feedback-model.md`
- `docs/services/research-feedback-service-contract.md`

## Acceptance criteria

- candidate state is defined canonically
- feedback event shape is defined canonically
- proposal state is defined canonically
- rule polarity and scope are defined canonically
- service commands and read models are defined canonically

## Notes

This is documentation-only. It does not by itself change the production schema or implementation.
