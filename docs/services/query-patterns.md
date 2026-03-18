# Query Patterns

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the correct read pattern for the application.

---

## 2. Read Path

Use this standard pattern:

Page / Layout / Hook  
→ Service  
→ Supabase

Do not skip the service layer.

---

## 3. Read Categories

### List reads
Examples:
- list mandates
- list research
- list results
- list companies
- list contacts

### Detail reads
Examples:
- get mandate detail
- get research detail
- get result detail
- get company detail
- get contact detail

### Aggregated reads
Examples:
- billing summary
- organization dashboard summary
- result detail with evidence + fit + dossier
- integration status summary

Aggregated reads often need server-side assembly.

---

## 4. Typed DTO Rule

Services should return DTOs tailored to the app, not raw DB rows everywhere.

Examples:
- list item DTO
- detail DTO
- summary DTO
- select option DTO

A page should not need to understand the entire raw DB shape.

---

## 5. Source-of-Truth Rule

Final service reads must prefer normalized source-of-truth tables.

### Use canonical entity tables for final entity reads
- companies
- company_domains
- contacts
- contact_emails
- contact_phones

### Use normalized analysis tables for final analysis reads
- evidence
- psych_profiles
- lmc_fits
- dossiers

### Use workflow tables for orchestration/process reads
- crm_opportunities
- mandates
- mandate_files
- research
- strategies
- research_results
- research_constraints

---

## 6. Transitional Field Rule

Do not build final service reads around these as primary data sources:

- research_results.company_profile
- research_results.psych_profile
- research_results.lmc_fit
- research_results.dossier
- research_results.evidence

They may remain temporarily during migration, but must not be the long-term read model.

---

## 7. Query Composition Rule

Services may join multiple tables if needed for the correct domain read model.

Examples:
- result detail may join:
  - research_results
  - companies
  - contacts
  - evidence
  - psych_profiles
  - lmc_fits
  - dossiers

- company detail may join:
  - companies
  - company_domains
  - related contacts
  - related results

This is acceptable when the service returns a stable domain DTO.

---

## 8. Page Rule

Pages should ask for:
- list DTOs
- detail DTOs
- summary DTOs

Pages should not reconstruct business read models from raw tables.
