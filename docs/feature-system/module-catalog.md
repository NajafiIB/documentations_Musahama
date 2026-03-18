# Module Catalog

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the official top-level module catalog.

Modules are the only valid top-level navigation and page areas.

---

## 2. Canonical Module Keys

The only official top-level modules are:

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

These keys must be used consistently in:
- module catalog
- module resolver
- organization_modules
- role rules
- sidebar rendering
- route/module mapping
- seed data
- tests

---

## 3. Route Mapping

Use this mapping consistently:

- dashboard -> /dashboard
- crm_opportunities -> /crm-opportunities
- mandates -> /mandates
- research -> /research
- results -> /results
- companies -> /companies
- contacts -> /contacts
- integrations -> /integrations
- billing -> /billing
- settings -> /settings

Database names do not need to match route names exactly.

Example:
- module key = results
- route = /results
- workflow table = research_results

---

## 4. What Is Not a Module

The following are not top-level modules:

- discovery
- shortlist
- dossiers
- CRM sync
- analytics

These must be modeled as one of:
- features
- embedded views
- actions
- export actions
- secondary tabs
- widgets
- internal workflow states

### Examples
- shortlist -> results feature or results subview
- dossiers -> results detail section + export feature
- CRM sync -> CRM/results feature
- analytics -> dashboard widget or future add-on only if promoted later
- discovery -> internal workflow stage under research/results

---

## 5. Module Purpose Baseline

### dashboard
Workspace landing area and summary surface.

### crm_opportunities
Opportunity archive and CRM-origin workflow entry.

### mandates
Mandate archive and mandate detail.

### research
Research archive and research detail.

### results
Research results archive and result detail inspector.

### companies
Canonical company archive and detail.

### contacts
Canonical contact archive and detail.

### integrations
Provider configuration and connection health.

### billing
Subscription, credits, and billing controls.

### settings
Organization and personal settings surfaces.

---

## 6. Module Visibility Rule

A module is visible only if all are true:

1. user is authenticated
2. current organization is resolved
3. membership is active
4. organization is active
5. module exists in catalog
6. module is enabled for the organization
7. role is allowed for the module

---

## 7. Baseline Visibility by Role Group

### visible to workflow roles
- dashboard
- crm_opportunities
- mandates
- research
- results
- companies
- contacts

### visible to platform operator roles
- integrations
- billing

### settings
Subsection-based access.
Do not treat settings as a single flat permission.

---

## 8. Suggested Module Catalog Shape

A catalog entry should contain at least:

- key
- route
- label
- icon
- category
- isCore
- defaultEnabled
- allowedRoles
- requiredEntitlementKey (optional)

---

## 9. Required Runtime Contract

The module resolver should return something like:

```ts
type ModuleStateReason =
  | "ok"
  | "not_authenticated"
  | "no_active_org"
  | "not_member"
  | "inactive_membership"
  | "missing_role"
  | "missing_module"
  | "module_disabled"

type ModuleState = {
  key: string
  visible: boolean
  enabled: boolean
  reason: ModuleStateReason
}
---

##10. Hard Rule

Sidebar rendering must always come from resolved module state.
Never from a hardcoded tab list

