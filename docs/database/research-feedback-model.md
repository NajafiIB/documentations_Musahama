# Research Feedback Model

Owner: Platform Architect
Last Updated: 2026-03-27
Version: 1.0
Status: Approved

## Purpose

Define the canonical data model for operator feedback in the Research workflow and the handoff into Results.

This document is the source of truth for:
- candidate lifecycle state
- feedback event shape
- proposal state
- rule polarity
- rule scope
- linkage from discovery candidate to results case

## Core entities

The canonical feedback model consists of these concepts:
- candidate
- feedback event
- feedback proposal
- approved rule
- results case

## Candidate

A candidate is a discovery-stage target under review.

Minimum canonical fields:
- `candidate_id`
- `category_id`
- `project_id`
- `status`
- `created_at`
- `updated_at`

### Candidate status
Allowed canonical values:
- `discovered`
- `shortlisted`
- `rejected`
- `finalized`

### Status meaning
- `discovered` = active discovery working set
- `shortlisted` = accepted from discovery and now eligible for Results
- `rejected` = removed from active discovery set
- `finalized` = completed shortlisted case under Results ownership

## Feedback event

A feedback event records an operator decision on a candidate.

Minimum canonical fields:
- `feedback_event_id`
- `candidate_id`
- `event_type`
- `reason_text`
- `actor_id`
- `created_at`

### Event type
Allowed canonical values:
- `shortlist`
- `reject`

## Feedback proposal

A feedback proposal is a candidate reusable rule suggested after a feedback event.

Minimum canonical fields:
- `feedback_proposal_id`
- `feedback_event_id`
- `candidate_id`
- `proposal_state`
- `rule_polarity`
- `scope`
- `suggested_text`
- `edited_text`
- `created_at`
- `resolved_at`

### Proposal state
Allowed canonical values:
- `suggested`
- `approved`
- `dismissed`
- `edited_approved`

### Rule polarity
Allowed canonical values:
- `positive_signal`
- `constraint`

### Scope
Allowed canonical values:
- `category`
- `global`

## Approved rule

An approved rule is the reusable refinement that affects future search behavior.

Minimum canonical fields:
- `rule_id`
- `rule_polarity`
- `scope`
- `text`
- `source_feedback_proposal_id`
- `project_id`
- `category_id` (nullable when scope is global)
- `is_active`
- `created_at`

## Results case

A results case is the shortlisted or finalized record that belongs to the Results module.

Minimum canonical fields:
- `results_case_id`
- `candidate_id`
- `project_id`
- `case_status`
- `created_at`
- `updated_at`

### Results case status
Allowed canonical values:
- `shortlisted`
- `finalized`

## Lifecycle rules

### Shortlist path
1. candidate status changes from `discovered` to `shortlisted`
2. feedback event is recorded as `shortlist`
3. system may create a feedback proposal with polarity `positive_signal`
4. operator may approve, edit and approve, or dismiss the proposal
5. if approved, an approved rule is created
6. a results case may be created for the candidate

### Reject path
1. candidate status changes from `discovered` to `rejected`
2. feedback event is recorded as `reject`
3. system may create a feedback proposal with polarity `constraint`
4. operator may approve, edit and approve, or dismiss the proposal
5. if approved, an approved rule is created

### Finalization path
1. a shortlisted candidate moves under Results ownership
2. results case status changes from `shortlisted` to `finalized` when review is complete
3. candidate status may also be represented as `finalized` for cross-module reporting if needed

## Hard rules

1. shortlist and reject are feedback events, not only button clicks
2. proposal state must be explicit
3. rule polarity must be explicit
4. scope must be explicit
5. shortlisted candidates must be representable in Results without mixing them back into discovery lists
6. a reusable rule is not canonical until operator approval is recorded

## Practical mapping rule

Existing implementation may map older fields or structures into this model.

For example:
- existing refinement rule structures may map into approved rules
- discovery-stage lead status fields may map into candidate status
- shortlist tables or results tables may map into results case

The implementation may differ, but the canonical meanings above must be preserved.

## Final rule

The feedback model must keep discovery learning explicit.

If shortlist and reject decisions are not represented canonically, the workflow will drift and the Research-to-Results split will not hold.
