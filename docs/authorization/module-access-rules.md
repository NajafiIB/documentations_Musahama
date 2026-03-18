# Module Access Rules

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how module visibility is resolved.

Modules control:
- sidebar items
- routes
- page-level access

Modules are not features.

---

## 2. Canonical Module Keys

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

These are the only official top-level modules.

---

## 3. Module Visibility Rule

A module is visible only if all of the following are true:

1. user is authenticated
2. user has active membership in current organization
3. organization is active
4. module exists in catalog
5. module is enabled for the organization
6. role is allowed for the module

---

## 4. Baseline Module Rules

### dashboard
Visible to all active organization members.

### crm_opportunities
Visible to workflow roles.

### mandates
Visible to workflow roles.

### research
Visible to workflow roles.

### results
Visible to workflow roles.

### companies
Visible to workflow roles.

### contacts
Visible to workflow roles.

### integrations
Visible only to platform operator roles.

### billing
Visible only to platform operator roles.

### settings
Subsection-based access.
Do not treat settings as one flat permission.

---

## 5. Settings Subsection Rules

### Personal profile settings
Visible to all signed-in active members.

### Organization settings
Visible to:
- owner
- admin
- developer
- billing_admin where appropriate

### Member management
Visible to:
- owner
- admin
- developer
- manager only if explicitly allowed in limited mode

### Billing/settings subsections
Visible to:
- owner
- billing_admin
- developer

### Integration/provider settings
Visible to:
- owner
- billing_admin
- developer

---

## 6. What Must Not Happen

Do not:
- hardcode sidebar tabs
- make navigation decisions directly inside page files
- infer access from route names alone
- treat hidden modules as secure access control
- mix module visibility and feature availability

---

## 7. Required Runtime Output

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
