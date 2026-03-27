# Analysis Model

Owner: Platform Architect
Last Updated: 2026-03-27
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the canonical analysis model for Musahama.

This document is the source of truth for:
- the meaning of canonical analysis records
- the meaning of `evidence`
- the relationship between `evidence`, `psych_profiles`, `lmc_fits`, and `dossiers`
- the lifecycle from discovery output to canonical analysis tables
- ownership boundaries for workflow, services, frontend, and RLS

---

## 2. Canonical analysis entities

The canonical analysis model consists of:
- `evidence`
- `psych_profiles`
- `lmc_fits`
- `dossiers`

These are the final normalized analysis records used by final detail views.

They are not the same thing as workflow-stage JSON blobs in `research_results`.

---

## 3. Evidence — canonical definition

### What evidence is

Evidence is the canonical record of source-backed intelligence collected for a lead during Discovery & Analysis.

It captures the external signals used to:
- verify a target
- justify why a lead was selected
- support downstream fit analysis
- support psychometric analysis
- support dossier generation

### OSI-aligned wording

In OSI/discovery terms, evidence is made of **Evidence Items**.

Typical evidence items include:
- news
- video
- tweets or social posts
- public-source snippets
- verbal-intent signals

A verbal-intent signal is a directly attributable statement or source-backed signal that helps confirm a target's strategy, investment posture, or relevant public positioning.

### What evidence is not

Evidence is not:
- a transient UI note
- a page-local derived object
- a provider-specific payload treated as final truth
- a legacy `research_results.evidence` blob used as the final analysis model

---

## 4. Minimum evidence record shape

The current documented implementation shape for a canonical evidence record includes fields such as:
- `lead_id`
- `type`
- `title`
- `url`
- `snippet`
- `why_selected`
- `verbal_quote`
- `media_timestamp`
- `matched_terms`
- `created_at`

This shape exists to preserve both:
- the source reference
- the explanation of why the source matters

If the schema changes, this document and the related source-of-truth docs must be updated in the same change cycle.

---

## 5. Relationship to other analysis entities

### `evidence`
Source-backed intelligence and explainability inputs.

### `psych_profiles`
Behavioral and communication interpretation derived from the lead's observable footprint.

### `lmc_fits`
Lead-mandate/company fit analysis explaining why the lead matches or fails to match the opportunity.

### `dossiers`
Decision-ready synthesis for operator review and export.

The intended relationship is:
- evidence supplies source-backed support
- psych profiles interpret behavior/persona
- fit records explain matching logic
- dossiers synthesize the result into review-ready output

---

## 6. Lifecycle

The canonical lifecycle is:

1. discovery/research produces candidate outputs and source signals
2. workflow-stage results may temporarily exist in `research_results`
3. canonical promotion resolves normalized analysis records through services
4. final detail views read canonical analysis tables

For evidence specifically:
1. discovery collects source-backed signals at the lead level
2. those signals are reviewed or resolved through workflow/services
3. canonical evidence records are written to `evidence`
4. final results/detail/export views read canonical evidence records instead of relying on transitional blobs

---

## 7. Ownership boundaries

### Workflows
Own:
- the stage where discovery output is produced
- the handoff from research to results
- canonical promotion triggers through workflow/service boundaries

Workflows do not own the final analysis read model.

### Services
Own:
- evidence read/write paths
- DTO shaping for evidence/detail views
- canonical promotion logic
- joins across analysis entities when building final detail responses

Services are the correct place for evidence aggregation and shaping.

### Frontend
Owns:
- rendering evidence in results/detail/export views
- showing source references and explainability UI
- consuming service-shaped DTOs

The frontend must not invent private evidence logic or treat workflow blobs as canonical truth.

### RLS / secure backend logic
Own:
- final row-level protection for analysis records
- organization/user scoping enforcement

UI hiding is never the security boundary.

---

## 8. Hard rules

1. final detail pages must prefer canonical analysis tables
2. `research_results.evidence` is not the final evidence model
3. evidence must preserve both source reference and reason-for-selection context
4. evidence shaping belongs in services, not in page components
5. discovery terminology may inform evidence meaning, but provider payloads are not canonical truth
6. if evidence schema or lifecycle changes, related database/workflow/service/frontend docs must be updated together

---

## 9. Practical usage rule

If a developer is building:
- a final evidence view -> read `evidence`
- a final result detail view -> read analysis DTOs built from canonical analysis tables
- a workflow progress view -> read workflow tables and only use workflow blobs as process state
- an export/dossier flow -> consume canonical evidence through services

---

## 10. Cross references

Read together with:
- `docs/database/source-of-truth-rules.md`
- `docs/workflows/implementation-rules.md`
- `docs/services/implementation-rules.md`
- `docs/frontend/frontend-foundation.md`
- `docs/authorization/rls-and-runtime-boundary.md`

---

## 11. Final rule

There must be one canonical definition of the analysis model.

All other docs may reference it.
They must not silently replace it with drifting local wording.
