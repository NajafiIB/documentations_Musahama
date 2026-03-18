# Services Foundation

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the official responsibility of the `services/` layer in the Musahama platform.

This document is the source of truth for:
- what belongs in services
- what must not belong in services
- how services interact with feature-system, pages, and views
- how data should be fetched and mutated
- where server-only logic belongs

---

## 2. Core Rule

Pages must not scatter direct Supabase queries.

Use:
- `services/` for data access and mutations
- `feature-system/` for capability/runtime access truth
- `features/` for UI/domain rendering
- `views/` for reusable layout/view primitives

---

## 3. Services Layer Responsibility

`services/` owns:
- data fetching
- mutations
- query composition
- write helpers
- typed data contracts
- server-side data assembly
- normalized DTO shaping
- audit field application
- secure backend/Supabase access boundaries

---

## 4. Services Layer Does Not Own

`services/` does not own:
- sidebar/module visibility decisions
- feature enablement truth
- page layout composition
- ad hoc UI button visibility rules
- provider-first product structure
- final database security enforcement

Those belong to:
- `feature-system/`
- `features/`
- `views/`
- RLS

---

## 5. Relationship to Other Layers

### feature-system/
Owns:
- module visibility
- feature availability
- provider requirement resolution
- capability reason codes

### features/
Owns:
- domain UI
- forms
- components
- visual behavior

### pages/routes
Own:
- route params
- layout composition
- choosing what view to render

### services/
Own:
- all meaningful backend/Supabase reads and writes
- shaping domain-safe return objects
- secure server-side data assembly

---

## 6. Non-Negotiable Rules

1. No ad hoc Supabase queries inside page components
2. No direct page-level writes to organization-owned tables
3. No raw secret exposure in client-readable service responses
4. No capability/entitlement truth hardcoded in services as a UI substitute
5. No final UI built around transitional blobs in `research_results`
6. No mutation path that depends on forms remembering ownership fields manually

---

## 7. Final Mental Model

- if code fetches or mutates domain data -> `services/`
- if code decides whether a capability is available -> `feature-system/`
- if code renders how a module looks -> `features/`
- if code renders reusable layouts -> `views/`
- if code protects rows -> RLS
