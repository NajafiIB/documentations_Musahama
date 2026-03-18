# Workflow Implementation Rules

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Give developers and AI coding agents strict rules for implementing workflow behavior.

---

## 2. Core Rules

1. build the product around the official workflow sequence
2. keep workflow modules separate from canonical archive modules
3. keep strategies inside research
4. keep shortlist/dossier/export inside results
5. use services for workflow reads and mutations
6. use feature-system for workflow capability access
7. use normalized canonical/analysis tables for final detail views
8. keep all workflow actions organization-scoped

---

## 3. What Developers Must Do

- implement CRM opportunity -> mandate transition explicitly
- implement mandate -> research transition explicitly
- implement research -> results handoff explicitly
- implement result -> canonical promotion through services
- keep workflow status in persistent records
- keep route/module boundaries aligned with docs/frontend/*
- keep capability gates aligned with docs/feature-system/*

---

## 4. What Developers Must Not Do

Do not:
- turn strategies into a top-level module
- turn shortlist into a top-level module
- turn dossiers into a top-level module
- build final company/contact pages from raw result blobs
- hide workflow meaning inside one giant prompt or opaque JSON field
- place workflow orchestration logic directly inside page components
- let one page invent a private workflow model different from the rest of the app

---

## 5. Definition of Done for a Workflow Stage

A workflow stage is not done until:
- the route/module exists
- organization context works
- status is persisted
- service contracts are stable
- runtime capability gating works
- loading/empty/error states exist
- docs are updated
- downstream handoff is defined

---

## 6. AI Coding Agent Rule

Before implementing workflow changes, the agent must read:
- docs/workflows/*
- docs/frontend/*
- docs/services/*
- docs/feature-system/*
- docs/database/source-of-truth-rules.md
- docs/authorization/*

Then it must implement the workflow through correct boundaries instead of patching a single page in isolation.

---

## 7. Final Rule

If a change fixes one screen but breaks the official workflow chain, it is the wrong change.
