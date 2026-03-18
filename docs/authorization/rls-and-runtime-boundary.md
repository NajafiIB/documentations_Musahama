
---

## `docs/authorization/rls-and-runtime-boundary.md`

```md
# RLS and Runtime Boundary

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Clarify the difference between RLS, runtime authorization, and UI access behavior.

This boundary must stay clean.

---

## 2. RLS Responsibilities

RLS is responsible for:
- organization isolation
- row-level data access
- final database enforcement

RLS is the final source of truth for data protection.

---

## 3. Runtime Responsibilities

Runtime authorization is responsible for:
- module visibility
- route access decisions
- feature availability
- provider/dependency checks
- explanation of unavailable states

Runtime authorization does not replace RLS.
It sits above it.

---

## 4. UI Responsibilities

The UI is responsible for:
- rendering the resolved module list
- showing/hiding actions
- disabling buttons
- explaining why something is unavailable

The UI must not act as the real security boundary.

---

## 5. Correct Example

### Integrations page
- Runtime decides whether the module is visible for this role/org
- UI renders the page only if runtime allows it
- RLS still protects underlying data access

### Results export action
- Runtime decides whether `results.export.dossier` is enabled
- UI disables or hides export action
- RLS/service validation still protects the underlying operation

---

## 6. Incorrect Example

- Sidebar hides Billing so developer assumes Billing is secure
- Page has no server/runtime guard
- Service call has no role/module validation
- RLS is incomplete

This is not acceptable.

---

## 7. Final Rule

Authorization is valid only when:
- RLS is correct
- runtime resolution is correct
- UI consumes runtime truth correctly
