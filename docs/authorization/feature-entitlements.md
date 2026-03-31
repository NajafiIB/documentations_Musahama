
# Feature Entitlements

Owner: Platform Architect
Last Updated: 2026-03-31
Version: 1.1
Status: Approved

## 1. Purpose

Define how feature-level capability access works.

Features are not modules.
Features are the granular capability layer inside modules.

## 2. Feature Rule

A feature is available only if:

- module enabled
- role allowed
- feature entitlement enabled
- dependencies satisfied
- provider requirement satisfied
- credits or quota are sufficient
- provider and system status are healthy

The UI must not guess this logic.

## 3. Related References

- docs/feature-system/feature-system-foundation.md
- docs/feature-system/entitlement-resolution.md
- docs/authorization/module-access-rules.md

## 3. Feature Categories

### Core features
Mandatory workflow capabilities.

Examples:
- research.generate_strategies
- research.background_processing
- results.generate_fit
- results.generate_dossier

### Add-on features
Optional product enhancements.

Examples:
- results.export.pdf
- results.export.csv
- results.compare_candidates
- companies.local_content_score
- analytics.advanced_dashboards

### Provider-backed features
Capabilities that require external providers.

Examples:
- contacts.enrich_person
- crm.sync.import
- companies.search_external_source

---

## 4. Capability-First Naming Rule

Feature keys must be capability-first.

### Correct
- research.generate_strategies
- contacts.enrich_person
- results.export.dossier
- crm.sync.import

### Incorrect
- contacts.enrich_lusha
- research.generate_strategies_openai

Provider names belong only in:
- provider catalogs
- provider requirements
- integration config
- provider management screens

---

## 5. Required Tables

Use/add these tables:

- features
- feature_dependencies
- feature_provider_requirements
- organization_feature_entitlements
- plan_features

---

## 6. UI Rules

### Module disabled
Hide the entire page/module from sidebar and route access.

### Feature disabled
Keep the page visible if the module is enabled.
Hide or disable only the action, widget, or sub-capability.

### Examples
- shortlist = results feature
- dossier export = results feature
- CRM sync = crm/results feature
- local content score = company/analytics add-on feature

---

## 7. Runtime Feature Resolver

The backend/service layer must resolve feature state for the current:
- organization
- role
- enabled modules
- feature entitlements
- connected integrations
- provider capabilities
- quotas/credits
- system status

Suggested output:

```ts
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
