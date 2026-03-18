# Entitlement Resolution

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the official runtime resolution rule for modules and features.

This is the main implementation contract for the resolver layer.

---

## 2. Core Feature Availability Rule

A feature is available only if all of the following pass:

1. module enabled
2. role allowed
3. feature entitlement enabled
4. dependencies satisfied
5. provider requirement satisfied
6. credits/quota sufficient
7. provider/system status healthy

The UI must not guess this logic.

---

## 3. Required Tables

The resolver is expected to use these tables or equivalent service views:

- modules
- organization_modules
- features
- feature_dependencies
- feature_provider_requirements
- organization_feature_entitlements
- plan_features
- organization_integrations
- organization_credit_ledger

---

## 4. Why plan_features Is Needed

`plan_features` is recommended because:
- modules are broad navigation units
- features are granular capabilities
- a plan may include a module without including every premium action inside it

Module access alone is not enough for long-term control.

---

## 5. Resolution Order

### Module resolution
1. verify authenticated user
2. resolve current organization
3. resolve active membership
4. resolve role
5. load module catalog
6. load enabled modules for org
7. evaluate module rule

### Feature resolution
1. resolve module state
2. resolve feature catalog entry
3. evaluate role rule
4. load feature entitlement
5. load feature dependencies
6. resolve provider requirements
7. resolve provider state
8. evaluate credits/quota
9. evaluate system/provider health
10. produce final feature state

---

## 6. Suggested Module Resolver Output

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
7. Suggested Feature Resolver Output
type FeatureStateReason =
  | "ok"
  | "missing_module"
  | "missing_role"
  | "missing_entitlement"
  | "missing_dependency"
  | "missing_provider"
  | "missing_api_key"
  | "insufficient_quota"
  | "provider_unavailable"
  | "system_disabled"

type FeatureState = {
  key: string
  visible: boolean
  enabled: boolean
  reason: FeatureStateReason
}
8. Explainability Rule

The resolver must always produce a reason code when something is unavailable.

Reason codes are required for:

consistent UI behavior

support/debugging

tests

auditability

avoiding magic hidden logic

9. Output Consumption Rule

The rest of the app should consume:

resolved module state

resolved feature state

resolved provider state

It must not reconstruct runtime logic from raw rows in page components.
