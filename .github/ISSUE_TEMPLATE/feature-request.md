---
name: Feature Request
about: Request a new capability or extension to an existing workflow/module
title: "[Feature] "
labels: ["feature-request"]
assignees: []
---

# Summary

Describe the requested feature.

---

## Business Goal

What problem does this feature solve?

---

## User Outcome

What should the user be able to do?

---

## Is This a Module or a Feature?

Choose one:

- [ ] top-level module
- [ ] feature/capability inside an existing module
- [ ] workflow action/subview
- [ ] export
- [ ] settings subsection
- [ ] provider-backed capability
- [ ] unknown

Important:
Do not propose a new top-level module unless truly necessary.

---

## Target Module

Choose the main home for this feature:

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

## Proposed Capability Name

Use capability-first naming.

Examples:
- `results.export.dossier`
- `contacts.enrich_person`
- `crm.sync.import`

Do not use provider-first naming.

---

## Workflow Stage

Where does this fit?

- [ ] CRM Opportunity
- [ ] Mandate
- [ ] Research
- [ ] Strategy
- [ ] Results
- [ ] Canonical Promotion
- [ ] Integration / Billing / Settings
- [ ] Cross-workflow

---

## Proposed Behavior

Explain what the feature should do.

---

## Required Inputs

List required data, context, or dependencies.

Examples:
- active organization
- workflow role
- provider connection
- quota/credits
- canonical company record
- research result selection

---

## Expected Runtime Rules

What should control whether this is available?

- [ ] module enabled
- [ ] role allowed
- [ ] feature entitlement
- [ ] dependency feature
- [ ] provider connected
- [ ] sufficient quota
- [ ] settings subsection access
- [ ] not sure

---

## UI Surface

Where should this appear?

- [ ] sidebar
- [ ] page-level section
- [ ] detail inspector
- [ ] action button
- [ ] export menu
- [ ] modal
- [ ] drawer
- [ ] settings section

---

## Data Source of Truth

What data should the final UI/action use?

- [ ] workflow tables
- [ ] canonical company data
- [ ] canonical contact data
- [ ] analysis tables
- [ ] billing/integration data
- [ ] mixed read model

Specify exact tables if known.

---

## Constraints

What must not happen?

Examples:
- do not create a fake top-level module
- do not build on legacy blobs
- do not bypass feature-system
- do not expose provider secrets
- do not bypass service layer

---

## Acceptance Criteria

List concrete outcomes.

---

## Related Docs to Update

- [ ] docs/auth/
- [ ] docs/authorization/
- [ ] docs/database/
- [ ] docs/feature-system/
- [ ] docs/services/
- [ ] docs/frontend/
- [ ] docs/workflows/
- [ ] docs/dev-guides/
- [ ] none
