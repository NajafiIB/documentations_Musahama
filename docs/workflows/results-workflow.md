# Results Workflow

## Status

Compatibility workflow surface under `Origination Match`.

## Current Role

`/results` remains the operational output surface for:

- ranked candidate companies
- result-linked contacts
- evidence views
- one-pagers and related artifacts

It is no longer the official independent top-level product model.

## Current Responsibility

Results currently bridge between:

- workflow-generated candidate data
- shared durable entities
- generated artifacts

## Rule

Do not treat `results` as the final durable archive by default.

Use shared entities and formal artifacts when the data must be reused across modules or treated as long-lived truth.
