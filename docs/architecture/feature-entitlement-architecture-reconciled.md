
# Feature Entitlement Architecture (Reconciled)

This document defines the reconciled architecture for modular, expandable platform features.

It resolves the earlier tension between:
- module navigation
- feature capabilities
- provider dependencies
- entitlement/runtime state

---

# 1. Core Rule

Separate these four concepts:

## Modules
Large user-facing sections of the product.

Canonical module keys:
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

## Features
Specific capabilities/actions/widgets inside modules.

Examples:
- research.start
- research.generate_strategies
- research.background_processing
- results.export.csv
- results.export.dossier
- results.shortlist
- contacts.enrich_person
- companies.find_similar
- crm.sync.import
- crm.sync.export

## Providers
External dependencies only.

Examples:
- OpenAI
- Lusha
- CRM connector
- search provider

Providers are never the product concept.

## Entitlements
Runtime truth about what an organization is allowed to use.

A feature is available only if the entitlement logic passes.

---

# 2. Capability-First Rule

Feature keys must be capability-first, not vendor-first.

## Correct
- research.generate_strategies
- contacts.enrich_person
- results.export.dossier
- crm.sync.import

## Incorrect
- contacts.enrich_lusha
- research.generate_strategies_openai

Provider selection belongs in:
- `feature_provider_requirements`
- integration configuration
- runtime resolver state

---

# 3. Feature Categories

## Core features
Mandatory workflow capabilities.

Examples:
- research.generate_strategies
- research.background_processing
- results.generate_fit
- results.generate_dossier

## Add-on features
Optional product enhancements.

Examples:
- results.export.pdf
- results.export.csv
- results.compare_candidates
- companies.local_content_score
- analytics.advanced_dashboards

## Provider-backed features
Capabilities that require external providers.

Examples:
- contacts.enrich_person
- crm.sync.import
- companies.search_external_source

The provider is configured separately.

---

# 4. Runtime Availability Rule

A feature is available only if:

module enabled
AND role allowed
AND feature entitlement enabled
AND dependencies satisfied
AND provider requirement satisfied (if any)
AND credits/quota sufficient (if needed)
AND provider/system status healthy

The UI must not guess this logic.

---

# 5. Required Tables

Add/use these tables:

- features
- feature_dependencies
- feature_provider_requirements
- organization_feature_entitlements
- plan_features (recommended)

## Recommendation
Add `plan_features`.

Why:
- modules are large navigation units
- features are granular capabilities
- a plan may include a module but not every premium action inside it

---

# 6. Provider Requirement Rule

Provider requirements belong in `feature_provider_requirements`.

Example:

Feature:
- contacts.enrich_person

Possible provider requirements:
- provider = Lusha, capability = person_enrichment
- provider = another enrichment provider, capability = person_enrichment

The feature stays the same even if the provider changes.

---

# 7. Runtime Feature Resolver

The backend/service layer should resolve feature state for the current:
- organization
- role
- enabled modules
- feature entitlements
- connected integrations
- provider capabilities
- quotas/credits
- system status

Example output:

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
```

---

# 8. Frontend Ownership Boundary

This resolves the earlier structure conflict.

## features/
UI/domain implementation.

## feature-system/
Runtime capability truth.

Recommended folder:

```text
src/
  feature-system/
    catalog/
    resolver/
    permissions/
    runtime/
```

### Rule
`feature-system/` is authoritative for capability access.
`features/` consumes that runtime truth.

---

# 9. Role Rules

## Platform operator roles
- owner
- billing_admin
- developer

Can manage:
- integrations
- APIs
- billing
- platform features

## Workflow roles
- owner
- admin
- manager
- analyst
- member
- developer
- billing_admin (optional broader visibility)

Can use:
- crm_opportunities
- mandates
- research
- results
- companies
- contacts

---

# 10. UI Rules

## Module disabled
Hide the entire page/module from sidebar.

## Feature disabled
Keep the page visible if the module is enabled.
Hide or disable only the action/widget.

## Examples
- shortlist -> results feature
- dossier export -> results feature
- CRM sync -> crm/results feature
- local content score -> company/analytics feature or separate add-on module if promoted later

---

# 11. Final Recommendation

Use:
- modules for navigation
- features for capabilities
- providers for dependencies
- entitlements for runtime truth

This is the model with the highest chance of long-term expandability and the lowest chance of rebuilding architectural debt later.
