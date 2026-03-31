# Definition of Done

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define what “done” means for a feature, bug fix, or workflow slice.

---

## 2. Core Rule

A task is not done when the screen merely renders.
It is done when the architecture, data, access rules, and workflow handoff are correct.

---

## 3. General Definition of Done

A change is done only when all are true:

- route or UI surface works
- correct organization context is enforced
- correct role/module/feature gating exists
- services are used instead of scattered queries
- source-of-truth reads are correct
- loading/empty/error states exist
- tests were updated where needed
- docs were updated where needed
- canonical case state and evidence were updated where needed
- no structural debt was introduced in the wrong layer

---

## 4. For UI Work

UI work is not done until:
- shell/layout rules are respected
- module-driven navigation still works
- disabled states use runtime reason codes
- no ad hoc access logic was added to random components
- detail pages use expected DTOs

---

## 5. For Service Work

Service work is not done until:
- organization scope is enforced
- DTOs are stable
- sensitive data is sanitized
- canonical source-of-truth reads are preserved
- mutation ownership/audit fields are correct

---

## 6. For Runtime Access Work

Runtime access work is not done until:
- module visibility works by role and org
- feature availability works by entitlement/dependency/provider state
- reason codes are stable
- route-level protection remains aligned

---

## 7. For Workflow Work

Workflow work is not done until:
- the state transition is persisted
- the downstream handoff is defined
- the change does not break the official workflow sequence
- the module boundary remains correct

---

## 8. Final Rule

A change is not done if it merely hides the problem instead of solving it in the right layer.
