---
name: Bug / Change Request
about: Report a bug or request a structural fix/change
title: "[CR] "
labels: ["change-request"]
assignees: []
---

# Summary

Describe the bug or requested change clearly.

---

## Problem

What is wrong right now?

Be specific:
- what the user sees
- what the system does
- what part of the workflow breaks
- what structural concern exists

---

## Expected Behavior

What should happen instead?

---

## Affected Area

Select all that apply:

- [ ] auth
- [ ] authorization
- [ ] database
- [ ] feature-system
- [ ] services
- [ ] frontend
- [ ] workflow
- [ ] integrations
- [ ] billing
- [ ] settings

---

## Affected Module(s)

Select any relevant module(s):

- [ ] dashboard
- [ ] crm_opportunities
- [ ] mandates
- [ ] research
- [ ] results
- [ ] companies
- [ ] contacts
- [ ] integrations
- [ ] billing
- [ ] settings

---

## Affected Workflow Stage

- [ ] CRM Opportunity
- [ ] Mandate
- [ ] Research
- [ ] Strategy
- [ ] Results
- [ ] Canonical Promotion
- [ ] Export / Shortlist / Sync

---

## Current Behavior Details

Include:
- route(s)
- component(s)
- service(s)
- table(s)
- role(s)
- organization context
- provider/integration state if relevant

Example:
- route: `/results/[id]`
- role: `member`
- organization: active
- current issue: page reads legacy `research_results.dossier` blob instead of normalized `dossiers`

---

## Suspected Layer Owning the Fix

Pick the one that should own the real fix:

- [ ] auth
- [ ] authorization
- [ ] feature-system
- [ ] services
- [ ] frontend views/components
- [ ] database / RLS
- [ ] workflow orchestration
- [ ] unknown

---

## Constraints

What must not change?

Examples:
- do not add a new top-level module
- do not hardcode role logic in UI
- do not bypass services
- do not use provider names as product structure
- do not build final views from legacy result blobs

---

## Source-of-Truth Rule

Does this issue touch final data reads?

- [ ] company source of truth
- [ ] contact source of truth
- [ ] analysis source of truth
- [ ] workflow-only state
- [ ] not applicable

If yes, specify the correct source of truth.

---

## Acceptance Criteria

Write clear acceptance criteria.

Example:
- sidebar renders only modules allowed by resolved module state
- `/integrations` is not accessible to `admin`
- results detail reads normalized `dossiers` and `evidence`
- service layer owns the required reads
- docs updated if architecture changed

---

## Screenshots / Evidence

Add screenshots, logs, errors, or links if available.

---

## Related Docs

List docs that must be checked before implementation:

- docs/auth/
- docs/authorization/
- docs/database/
- docs/feature-system/
- docs/services/
- docs/frontend/
- docs/workflows/
- docs/dev-guides/

Be more specific if known.

---

## Suggested Status

- [ ] draft
- [ ] pending-review
- [ ] approved
- [ ] blocked
