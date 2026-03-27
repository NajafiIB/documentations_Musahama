# Change Request — Centralize Analysis Model and Evidence Definition

## Status
- done

## Problem

The repository already identifies `evidence`, `psych_profiles`, `lmc_fits`, and `dossiers` as canonical analysis sources of truth, but it does not define their shared analysis model in one canonical place.

The meaning of `evidence` is especially at risk of drift because OSI/discovery wording, workflow wording, service wording, and UI wording can diverge.

## Expected behavior

The repository must contain one canonical document that defines:

- the analysis model
- the meaning of `evidence`
- the OSI-aligned wording for evidence items
- the lifecycle from discovery output to canonical analysis record
- the ownership boundaries for workflow, services, frontend, and RLS

## Affected layer

- documentation
- database model clarification
- workflow/service/frontend cross-reference clarification

## Affected areas

- `docs/database/analysis-model.md`
- `docs/database/source-of-truth-rules.md`
- `docs/workflows/implementation-rules.md`
- `docs/services/implementation-rules.md`
- `docs/frontend/frontend-foundation.md`

## Constraints

- keep one canonical definition instead of duplicating explanations in multiple places
- keep OSI/discovery vocabulary aligned with current ResearchTool wording
- keep final source-of-truth rules unchanged
- keep pages thin and service boundaries intact

## Acceptance criteria

- `docs/database/analysis-model.md` exists
- the evidence definition is canonical and OSI-aligned
- related docs reference the canonical analysis model instead of drifting definitions
- final-page guidance still points to normalized analysis tables, not `research_results` blobs

## Notes

This change is documentation-only. It does not alter the production data model by itself.
