# Feature System Foundation

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the official runtime capability model for the Musahama platform.

This document is the source of truth for:
- module vs feature boundaries
- provider and entitlement concepts
- runtime capability resolution
- ownership boundaries between feature-system, features, services, and pages

---

## 2. Core Rule

Separate these four concepts and never collapse them into one:

### Modules
Large top-level product areas.

Use for:
- sidebar items
- routes
- page-level access

### Features
Specific capabilities inside modules.

Use for:
- actions
- widgets
- exports
- premium enhancements
- provider-backed capabilities

### Providers
External dependencies only.

Use for:
- integration configuration
- runtime capability support
- provider health/capability checks

### Entitlements
Runtime truth about what an organization is allowed to use.

Use for:
- plan-driven capability access
- org-specific feature enablement
- add-ons
- premium controls

---

## 3. Final Mental Model

- modules = navigation
- features = capabilities
- providers = dependencies
- entitlements = runtime truth

This distinction must remain stable across:
- database
- service layer
- runtime resolver
- UI
- documentation

---

## 4. Why feature-system Exists

The `feature-system/` layer exists to stop the app from scattering access logic across:
- pages
- components
- hooks
- stores
- ad hoc conditionals

Without this layer, the codebase drifts into:
- duplicated role checks
- inconsistent sidebar logic
- broken feature toggling
- provider-coupled UI
- architecture drift

---

## 5. Ownership Boundary

### feature-system/
Owns:
- module visibility
- feature availability
- provider requirement resolution
- role/capability gating
- runtime state
- disabled-state reasons

### features/
Owns:
- domain UI
- module views
- forms
- module-specific components
- visual behavior

### services/
Owns:
- Supabase/backend reads and writes
- query composition
- typed data contracts
- mutation helpers
- server-side data assembly

### pages/routes
Own:
- layout composition
- route params
- choosing views
- calling hooks/services

Pages do not define access truth.

---

## 6. Hard Rules

1. `feature-system/` is the runtime source of truth for capability access
2. `features/` must consume resolved state, not invent permission logic
3. pages must not hardcode role-based access
4. provider names must not become product capability names
5. module access and feature access must stay separate
6. runtime capability logic does not replace RLS
7. RLS remains the final security boundary

---

## 7. What This Layer Must Resolve

The feature-system must answer:

### Module-level questions
- should this module appear in navigation?
- should this route be accessible?
- why is this module unavailable?

### Feature-level questions
- should this action be visible?
- should this action be enabled?
- what dependency is missing?
- is the provider connected and capable?
- is quota sufficient?
- what reason should the UI show?

---

## 8. Output Rule

The rest of the app must consume resolved runtime state rather than reconstructing logic from raw tables.
