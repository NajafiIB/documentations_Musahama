# Change Request — Research Feedback Loop and Results Finalization Split

## Status
- done

## Problem

The current research workflow mixes too many responsibilities into one operator surface.

In practice, strategy design, discovery, shortlist handling, due diligence, export, and CRM sync can all appear inside the same workflow. That is operationally useful, but architecturally muddy.

There is also no explicit first-class split between:
- positive learning from shortlisted candidates
- negative learning from rejected candidates

That makes the feedback loop weaker than it should be.

## Expected behavior

The platform must separate concerns more clearly.

### Research must own
- mandate intake
- strategy design
- positive signals
- constraints
- discovery
- operator feedback capture from shortlist/reject decisions

### Results must own
- shortlisted/finalized cases
- final operator review
- evidence-driven detail views
- fit/dossier review
- export and CRM submission

## Required logic

When an operator shortlists or rejects a discovery result, the system may propose a reusable refinement rule if beneficial.

- shortlist may propose a **positive signal**
- reject may propose a **constraint** or exclusion

The operator must be able to:
- approve
- edit
- dismiss

The rule scope must be explicit:
- category-level
- project/global-level

## Required UI direction

The research workspace must describe the process more clearly.

The target research flow is:
1. Strategy
2. Positive Signals
3. Constraints
4. Discovery
5. Results (separate module/page)

The Results page must be dedicated to shortlisted/finalized cases rather than mixed discovery output.

## Affected areas

- `docs/workflows/research-feedback-loop-and-results-finalization.md`
- `docs/frontend/research-workspace-process.md`

## Acceptance criteria

- canonical workflow logic exists for shortlist/reject learning
- positive signals and constraints are defined explicitly
- research/result ownership split is explicit
- frontend process is described from the operator point of view

## Notes

This is a documentation-first architecture change. It does not by itself refactor the implementation.
