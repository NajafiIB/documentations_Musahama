# Coding Standards

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the implementation standards for code written by humans and AI agents.

---

## 2. Core Principles

1. Respect architecture boundaries
2. Keep code explicit
3. Prefer stable DTOs over raw row sprawl
4. Keep pages thin
5. Keep runtime access logic centralized
6. Keep naming consistent
7. Prefer predictable structure over clever shortcuts

---

## 3. Boundary Rules

### services/
Use for:
- reads
- writes
- DTO shaping
- organization-scoped data access
- secure server-side assembly

### feature-system/
Use for:
- module state
- feature state
- provider requirement resolution
- reason codes

### features/
Use for:
- domain UI
- forms
- module components
- view composition

### views/
Use for:
- reusable inline/detail/form patterns

### app/
Use for:
- layout
- routing
- composition entry points

---

## 4. Naming Rules

### Routes
Use kebab-case.
Examples:
- /crm-opportunities
- /results

### Module keys
Use snake_case.
Examples:
- crm_opportunities
- results

### Feature keys
Use dot-separated capability names.
Examples:
- results.export.dossier
- contacts.enrich_person

### Filenames
Use kebab-case and one clear purpose per file.
Examples:
- get-result-detail.ts
- resolve-feature-state.ts
- use-current-organization.ts

Do not use vague filenames like:
- utils.ts
- stuff.ts
- service.ts
- helper.ts

---

## 5. Service Rules

- pages must not scatter `.from(...).select(...)` calls
- services should return stable DTOs
- sensitive or privileged reads must stay server-side
- mutations must apply organization and audit fields automatically
- final UI reads should prefer canonical entity and analysis tables

---

## 6. UI Rules

- sidebar is module-driven
- module access comes from runtime module state
- feature actions come from runtime feature state
- disabled states must use explicit reason codes
- do not duplicate role checks across buttons and pages

---

## 7. Feature Rules

Do:
- name features by capability
- keep provider names underneath the capability layer
- keep feature gating in `feature-system/`

Do not:
- create vendor-first feature keys
- evaluate feature access ad hoc in page components
- blur module access and feature access

---

## 8. Data Rules

Use canonical data for final pages:
- companies
- company_domains
- contacts
- contact_emails
- contact_phones
- evidence
- psych_profiles
- lmc_fits
- dossiers

Do not use `research_results` blobs as the long-term final read model.

---

## 9. Component Rules

Shared components must stay generic.

Do not place module-specific business logic inside:
- components/ui
- components/shell
- components/navigation

Domain logic belongs in `features/`.

---

## 10. Comments Rule

Write comments only when needed for:
- non-obvious business logic
- resolver reasoning
- important security or ownership caveats
- tricky transformation logic

Do not write noisy comments explaining obvious syntax.

---

## 11. Error Handling Rule

Every service should return predictable failures.
Every runtime resolver should return predictable reason codes.

Do not hide errors behind silent fallbacks unless the fallback is explicitly required.

---

## 12. Final Rule

A quick patch that violates the architecture is not acceptable code.
