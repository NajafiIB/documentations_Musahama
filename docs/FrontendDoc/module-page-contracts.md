---

## `docs/frontend/module-page-contracts.md`

```md
# Module Page Contracts

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the baseline page contract for each top-level module.

This gives the developer a stable target for what each route should do.

---

## 2. Dashboard

Route:
- /dashboard

Purpose:
- overview of the current organization

Typical content:
- summary cards
- workflow status widgets
- recent activity
- quick actions
- optional analytics widgets

---

## 3. CRM Opportunities

Route:
- /crm-opportunities

Purpose:
- archive of imported CRM opportunities
- conversion entry point into mandates

Expected content:
- archive/list
- search/filter
- sync/import entry point
- action to create or convert into mandate

---

## 4. Mandates

Routes:
- /mandates
- /mandates/[id]

Mandates archive:
- archive/list
- filters
- create new mandate

New mandate options:
- add manually
- sync from CRM

Mandate detail:
- summary
- files
- linked research runs
- actions:
  - start research
  - edit
  - archive

---

## 5. Research

Routes:
- /research
- /research/[id]

Research archive:
- archive/list
- filters
- create/start research

Research detail:
- goal
- rules
- exclusions
- strategies
- status/progress

Important rule:
- strategies are a subview of research
- results are a separate module

---

## 6. Results

Routes:
- /results
- /results/[id]

Results archive:
- result list/table
- filters
- selection

Results detail:
- detail inspector
- canonical company/contact summary
- evidence
- psych profile
- fit analysis
- dossier summary
- actions:
  - shortlist
  - export
  - open company
  - open contact

Important rule:
- shortlist is a results action/subview
- dossiers are results detail/export behavior
- neither becomes a top-level module

---

## 7. Companies

Routes:
- /companies
- /companies/[id]

Purpose:
- canonical company archive and detail

Expected content:
- company archive
- company detail
- domains view
- linked contacts
- related results where useful

---

## 8. Contacts

Routes:
- /contacts
- /contacts/[id]

Purpose:
- canonical contact archive and detail

Expected content:
- contact archive
- contact detail
- email list
- phone list
- linked company
- related results where useful

---

## 9. Integrations

Route:
- /integrations

Purpose:
- provider configuration
- integration connection health
- safe status display

Expected content:
- provider list
- connection status
- manage/connect/disconnect actions
- enabled capability visibility
- safe error/health surface

---

## 10. Billing

Route:
- /billing

Purpose:
- subscription and credits management

Expected content:
- current plan
- enabled modules
- credit balance
- credit ledger
- subscription state

---

## 11. Settings

Route:
- /settings

Purpose:
- organization settings
- personal/workspace settings
- membership management
- role-aware subsections

Important rule:
- settings must support subsection-based access
- it is not one flat permission surface
