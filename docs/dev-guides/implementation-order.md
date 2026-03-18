# Implementation Order

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the official build order for the platform.

This keeps the team from building random pages before the shell, tenancy, and core workflow are stable.

---

## 2. Core Rule

Do not build every page at once.

Build vertical slices in the correct order.

---

## 3. Official Order

### Milestone 1 — Shell and Tenancy
Deliver:
- auth flow
- current user resolution
- current organization resolution
- role resolution
- enabled module loading
- header
- sidebar
- footer
- module-driven navigation
- view framework scaffolding

Success means:
- user can sign in
- user can switch organizations
- protected pages require org context
- sidebar updates by enabled modules

---

### Milestone 2 — CRM Opportunities + Mandates
Deliver:
- opportunities archive
- search/filter
- sync/import entry point
- mandates archive
- mandate detail
- create mandate manually
- create mandate from CRM opportunity
- mandate file upload

Success means:
- opportunity can become mandate
- mandate archive/detail work
- file attachment flow works

---

### Milestone 3 — Research
Deliver:
- research archive
- create/start research
- research detail
- strategies subview
- research constraints UI
- progress/status display

Success means:
- mandate can create research runs
- research run shows strategies
- org/role access is correct

---

### Milestone 4 — Results
Deliver:
- results archive/table
- result detail inspector
- evidence rendering
- psych profile rendering
- fit analysis rendering
- dossier rendering
- shortlist
- export action stubs

Success means:
- results list/detail work
- analysis renders from normalized data
- actions are feature-gated correctly

---

### Milestone 5 — Companies + Contacts
Deliver:
- company archive/detail
- company domains
- contact archive/detail
- email and phone views
- links to related results

Success means:
- canonical entities are visible and editable
- developers stop treating research_results as final source of truth

---

### Milestone 6 — Integrations + Billing + Settings
Deliver:
- integrations overview and management
- provider/capability state visibility
- safe status surfaces
- billing summary
- credit ledger
- plan visibility
- settings sections
- membership management

Success means:
- platform operator roles can access technical/admin areas
- workflow roles cannot access restricted areas incorrectly

---

### Milestone 7 — Cleanup
Deliver:
- remove transitional UI dependence on result blobs
- clean legacy naming
- polish route guards and permission wrappers
- reduce technical debt

Success means:
- transitional compatibility hacks are no longer the main path
- structure remains aligned with docs

---

## 4. Final Rule

Do not move to the next milestone until the previous slice works end-to-end.
