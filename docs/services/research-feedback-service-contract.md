# Research Feedback Service Contract

Owner: Platform Architect
Last Updated: 2026-03-27
Version: 1.0
Status: Approved

## Purpose

Define the canonical service contract for writing and reading research feedback behavior.

This document is the source of truth for:
- service commands that change candidate state
- service commands that resolve proposals
- read models for Research and Results
- service ownership boundaries

## Ownership rule

Research feedback logic belongs in services.

Pages and components may capture user intent, but they must not directly own:
- candidate state transitions
- proposal state transitions
- approved rule persistence
- results case creation

## Write-side commands

### `shortlistCandidate`

Purpose:
- move a candidate from discovery into shortlisted state
- record a shortlist feedback event
- optionally create a positive-signal proposal
- optionally create or upsert a results case

Required inputs:
- `candidateId`
- `actorId`
- `reasonText` (optional)
- `proposalText` (optional)
- `scope` (optional when a proposal is created)

Required outcomes:
- candidate status becomes `shortlisted`
- feedback event with type `shortlist` is recorded
- if a proposal is created, polarity must be `positive_signal`
- candidate becomes eligible for Results reads

### `rejectCandidate`

Purpose:
- move a candidate from discovery into rejected state
- record a reject feedback event
- optionally create a constraint proposal

Required inputs:
- `candidateId`
- `actorId`
- `reasonText` (optional)
- `proposalText` (optional)
- `scope` (optional when a proposal is created)

Required outcomes:
- candidate status becomes `rejected`
- feedback event with type `reject` is recorded
- if a proposal is created, polarity must be `constraint`

### `approveFeedbackProposal`

Purpose:
- accept a suggested proposal as a reusable rule

Required inputs:
- `proposalId`
- `actorId`

Required outcomes:
- proposal state becomes `approved`
- approved rule is created or activated

### `editAndApproveFeedbackProposal`

Purpose:
- approve a proposal after operator changes the text

Required inputs:
- `proposalId`
- `actorId`
- `editedText`
- `scope` (optional if unchanged)

Required outcomes:
- proposal state becomes `edited_approved`
- proposal edited text is preserved
- approved rule is created from the edited text

### `dismissFeedbackProposal`

Purpose:
- reject a suggested proposal without creating a reusable rule

Required inputs:
- `proposalId`
- `actorId`

Required outcomes:
- proposal state becomes `dismissed`
- no approved rule is created

### `finalizeResultsCase`

Purpose:
- mark a shortlisted Results case as finalized

Required inputs:
- `resultsCaseId`
- `actorId`

Required outcomes:
- results case status becomes `finalized`
- candidate may be represented as `finalized` for reporting if needed

## Read-side models

### `getResearchDiscoveryView`

Purpose:
- return the active discovery working set for Research

Must return:
- discovered candidates
- candidate summary counters
- recent shortlist and reject actions if needed for context
- any pending proposals relevant to the active category or project

Must not mix in finalized Results cases as discovery items.

### `getResearchFeedbackPanel`

Purpose:
- return the data needed for the shortlist or reject decision panel

Must return:
- candidate identity summary
- current reason text if present
- suggested proposal text if present
- suggested polarity
- allowed scopes
- current proposal state if one exists

### `getResultsCaseList`

Purpose:
- return shortlisted and finalized cases for the Results module

Must return:
- shortlisted cases
- finalized cases
- stable case summary fields
- links to evidence, fit, and dossier detail DTOs

Must not behave like a raw discovery table.

### `getResultsCaseDetail`

Purpose:
- return the full results detail DTO for one shortlisted or finalized case

Must prefer canonical analysis tables and service-shaped DTOs.

## Boundary rules

### Research services own
- discovery-state candidate transitions
- feedback event recording
- proposal suggestion persistence
- proposal approval and dismissal flows

### Results services own
- shortlisted and finalized case reads
- final detail DTOs
- finalization flow
- export and downstream submission orchestration

### Shared rule
If a service writes both discovery feedback and results-case creation in one operation, the ownership boundary must still stay explicit in the service layer.

## Validation rules

Service logic must guarantee:
- candidate status transitions are valid
- proposal polarity matches the event type
- proposal state is explicit
- scope is explicit for approved rules
- Results list reads only shortlisted and finalized cases
- discovery reads do not show finalized cases as active discovery work

## Final rule

The UI may trigger feedback actions.
Only services may make those actions canonical.
