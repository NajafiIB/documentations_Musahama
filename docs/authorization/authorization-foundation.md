# Authorization Foundation

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how authorization works in the Musahama platform.

This document is the source of truth for:
- role interpretation
- module visibility
- feature availability
- route access
- separation between auth, authorization, RLS, and UI

---

## 2. Core Rule

Authorization is not one thing. It has three layers:

1. Database security
2. Server/runtime access resolution
3. UI rendering

### 2.1 Database security
Supabase RLS is the final security boundary.

### 2.2 Runtime access resolution
The backend/service layer and `feature-system/` resolve:
- which modules are visible
- which features are enabled
- why something is unavailable

### 2.3 UI rendering
The UI consumes resolved access state.
The UI is not the source of truth for security.

---

## 3. Non-Negotiable Rules

1. Never trust frontend role checks alone
2. Never hardcode permissions directly in page components
3. Modules control navigation and route visibility
4. Features control actions, exports, widgets, and enhancements
5. Providers are dependencies, not product concepts
6. `feature-system/` is the source of truth for runtime capability access
7. RLS remains the final protection layer

---

## 4. Concepts

### 4.1 Modules
Modules are large top-level application sections.

They control:
- sidebar visibility
- route visibility
- page-level availability

Canonical modules:
- dashboard
- crm_opportunities
- mandates
- research
- results
- companies
- contacts
- integrations
- billing
- settings

### 4.2 Features
Features are capabilities inside modules.

They control:
- actions
- exports
- buttons
- widgets
- provider-backed actions
- premium enhancements

Examples:
- research.start
- research.generate_strategies
- results.export.csv
- results.export.dossier
- results.shortlist
- contacts.enrich_person
- companies.find_similar
- crm.sync.import
- billing.manage_subscription

### 4.3 Providers
Providers are external dependencies only.

Examples:
- OpenAI
- Lusha
- CRM connector
- search providers

Providers must never define product structure.

### 4.4 Entitlements
Entitlements are runtime truth about what an organization is allowed to use.

---

## 5. Authorization Layers

### Layer 1 — RLS
Protects organization isolation and data access.

### Layer 2 — Feature Resolver
Resolves:
- module visibility
- feature availability
- dependency requirements
- provider requirements
- quota/credit status

### Layer 3 — UI
Shows, hides, disables, or explains unavailable areas.

---

## 6. Scope of Authorization

Authorization determines:

- whether a module appears in sidebar
- whether a route is accessible
- whether a page section is visible
- whether a button/action is enabled
- whether a provider-backed capability can run
- whether an admin/configuration page can be used

Authorization does NOT determine:
- authentication/session validity
- password/login logic
- organization onboarding flow

Those belong to auth and tenancy.

---

## 7. Ownership Boundary

### `feature-system/`
Owns:
- role/capability gating
- module-to-feature resolution
- runtime access state
- reasons for disabled state

### `features/`
Owns:
- UI/domain implementation
- forms
- module components
- views

### `services/`
Owns:
- backend access
- Supabase reads/writes
- query composition

### UI rule
`features/` must consume access truth from `feature-system/`.
It must not invent access logic.

---

## 8. Final Mental Model

- Modules = navigation
- Features = capabilities
- Providers = dependencies
- Entitlements = runtime truth
- UI = consumer of runtime truth
- RLS = final security boundary
