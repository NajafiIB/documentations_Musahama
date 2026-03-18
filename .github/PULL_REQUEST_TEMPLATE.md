# Pull Request Summary

Describe what changed and why.

---

## Type of Change

- [ ] bug fix
- [ ] structural refactor
- [ ] feature
- [ ] auth/onboarding change
- [ ] authorization change
- [ ] database/schema change
- [ ] feature-system change
- [ ] service-layer change
- [ ] frontend/UI change
- [ ] workflow change
- [ ] docs-only

---

## Related Issue / Change Request

Link the related issue(s) or change request(s).

Examples:
- Closes #123
- Related to #145

---

## What Changed

List the main changes.

- 
- 
- 

---

## Why This Change Was Needed

Explain the actual problem being solved.

---

## Files Intentionally Changed

List the main files or folders that were intentionally modified.

- 
- 
- 

---

## Files Intentionally Not Changed

List important files or layers that were deliberately left untouched.

- 
- 
- 

---

## Layer Ownership Check

Which layer owns the main fix?

- [ ] auth
- [ ] authorization
- [ ] database / RLS
- [ ] feature-system
- [ ] services
- [ ] frontend/features/views
- [ ] workflow orchestration

Explain briefly:

---

## Source-of-Truth Check

Does this change affect final data reads?

- [ ] companies
- [ ] contacts
- [ ] analysis tables
- [ ] workflow-only state
- [ ] not applicable

If yes, explain which tables are now used and why.

---

## Access / Security Check

- [ ] organization scoping preserved
- [ ] role logic stays in the correct layer
- [ ] feature/module gating stays in feature-system
- [ ] no UI-only security assumptions
- [ ] no sensitive provider/billing data exposed
- [ ] RLS assumptions still respected

---

## Workflow Check

If relevant:

- [ ] CRM Opportunity → Mandate preserved
- [ ] Mandate → Research preserved
- [ ] Research → Results preserved
- [ ] Results → Canonical Promotion preserved
- [ ] shortlist/dossier not promoted to top-level modules
- [ ] strategies remain a research subview

---

## Tests

- [ ] unit tests added/updated
- [ ] integration tests added/updated
- [ ] e2e tests added/updated
- [ ] no tests needed

Explain if no tests were needed:

---

## Documentation

- [ ] docs updated
- [ ] docs not required

If updated, list paths:

- 
- 

If not updated, explain why:

---

## Screenshots / Evidence

Add screenshots, logs, or outputs if helpful.

---

## Risks / Known Gaps

List remaining risks, blockers, or follow-up work.

- 
- 

---

## Reviewer Checklist

Reviewer should verify:

- [ ] correct layer owns the change
- [ ] no fake top-level modules introduced
- [ ] no page-level query sprawl added
- [ ] source-of-truth usage is correct
- [ ] service and feature-system boundaries preserved
- [ ] workflow chain still makes sense
- [ ] docs are aligned
