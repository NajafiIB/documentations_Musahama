# Source of Truth Rules

Owner: Platform Architect
Last Updated: 2026-03-28
Version: 1.1
Status: Approved

---

## 1. Purpose

Stop developers from reading the wrong table or building pages on transitional fields.

---

## 2. Final Sources of Truth

### Companies
Use:
- companies
- company_domains

Do not treat result JSON blobs as the final company record.

### Contacts
Use:
- contacts
- contact_emails
- contact_phones

Do not treat workflow result blobs as the final contact record.

### Analysis
Use:
- evidence
- psych_profiles
- lmc_fits
- dossiers

Do not treat legacy JSON fields in `research_results` as the final analysis model.

### Workflow state
Use:
- mandates
- mandate_crm_links
- mandate_files
- research
- strategies
- research_results
- research_constraints

Use these for execution state and process tracking.

### External CRM opportunity data
Do not persist external CRM opportunities as canonical internal records.

If an opportunity title, description, or mapped values are imported from an external CRM, those values become part of the mandate workflow state.
They do not create a separate internal `crm_opportunities` source-of-truth table.

Use `mandate_crm_links` only to store the relationship between an internal mandate and the external CRM entity identifier/provider reference.

---

## 3. Practical Rule

If the developer is building:
- a final company view -> read canonical company tables
- a final contact view -> read canonical contact tables
- a final dossier/fit/evidence view -> read analysis tables
- a process dashboard -> read workflow tables
- a capability/access decision -> read modules/features/entitlements/integrations through services and feature-system
- a mandate CRM-link action -> read the mandate and its `mandate_crm_links` record, not a cached internal CRM opportunity object

---

## 4. Hard Rule

No final page should depend primarily on:
- research_results.company_profile
- research_results.psych_profile
- research_results.lmc_fit
- research_results.dossier
- research_results.evidence

Do not introduce a separate internal `crm_opportunities` workflow table as a substitute for external CRM linking.
