# Codex / AI Studio Review Checklist

Use this checklist before accepting an AI-generated change.

---

## 1. Repo Discipline

- [ ] the change follows the repo docs
- [ ] the change does not invent new architecture casually
- [ ] the change stays scoped to the requested task
- [ ] unrelated files were not modified without reason

---

## 2. Layer Ownership

- [ ] auth logic stayed in auth/services/providers where appropriate
- [ ] authorization logic stayed in feature-system/runtime rules
- [ ] data reads/writes stayed in services
- [ ] domain UI stayed in features
- [ ] reusable layout/view logic stayed in views/components/app
- [ ] page files did not become the source of truth for logic

---

## 3. Module / Feature Discipline

- [ ] no new fake top-level module was introduced
- [ ] modules remain:
  - dashboard
  - crm_opportunities
  - mandates
  - research
  - results
  - companies
  - contacts
  - integrations
  - billing
  - settings
- [ ] shortlist was treated as a results action/subview
- [ ] dossier was treated as a results detail/export behavior
- [ ] strategies stayed inside research
- [ ] provider names were not turned into product structure

---

## 4. Organization and Security

- [ ] organization context is preserved
- [ ] no cross-organization leakage was introduced
- [ ] role checks are not scattered across random UI files
- [ ] the solution does not rely on hidden UI alone as security
- [ ] sensitive provider or billing data is not exposed to the client
- [ ] RLS assumptions still make sense

---

## 5. Source-of-Truth Discipline

- [ ] final company UI uses canonical company tables
- [ ] final contact UI uses canonical contact tables
- [ ] final analysis UI uses normalized analysis tables
- [ ] the change does not build final UI around legacy `research_results` blobs
- [ ] workflow tables are used for workflow state, not mistaken for final truth

---

## 6. Workflow Integrity

- [ ] CRM Opportunity → Mandate flow still works
- [ ] Mandate → Research flow still works
- [ ] Research → Results handoff still works
- [ ] Results → Canonical Promotion remains consistent
- [ ] no page invented a private workflow model

---

## 7. Services Boundary

- [ ] no scattered `.from(...).select(...)` calls were added to pages
- [ ] service functions return stable DTOs where needed
- [ ] sensitive reads remain server-side
- [ ] mutations apply organization/audit fields correctly
- [ ] service contracts remain understandable

---

## 8. Feature-System Boundary

- [ ] module visibility still comes from resolved module state
- [ ] feature availability still comes from runtime feature state
- [ ] disabled states use reason codes
- [ ] provider requirements are resolved underneath the capability layer
- [ ] pages are not reconstructing entitlement logic ad hoc

---

## 9. Frontend Integrity

- [ ] sidebar remains module-driven
- [ ] shell stays stable
- [ ] protected pages still require org context
- [ ] UI uses the expected archive/detail/form patterns
- [ ] result detail stays aligned with normalized data rules

---

## 10. Testing and Docs

- [ ] tests were updated where needed
- [ ] docs were updated where needed
- [ ] README / AGENTS / docs folders remain internally consistent
- [ ] any schema or contract change is reflected in docs

---

## 11. Final Acceptance Question

- [ ] this change solves the problem in the correct layer instead of just hiding the symptom

If this box cannot be checked, the change is not ready.
