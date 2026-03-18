# Source of Truth Rules

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
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
- crm_opportunities
- mandates
- mandate_files
- research
- strategies
- research_results
- research_constraints

Use these for execution state and process tracking.

---

## 3. Practical Rule

If the developer is building:
- a final company view -> read canonical company tables
- a final contact view -> read canonical contact tables
- a final dossier/fit/evidence view -> read analysis tables
- a process dashboard -> read workflow tables
- a capability/access decision -> read modules/features/entitlements/integrations through services and feature-system

---

## 4. Hard Rule

No final page should depend primarily on:
- research_results.company_profile
- research_results.psych_profile
- research_results.lmc_fit
- research_results.dossier
- research_results.evidence
