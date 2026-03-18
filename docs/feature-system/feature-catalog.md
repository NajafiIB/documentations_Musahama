
---

## `docs/feature-system/feature-catalog.md`

```md
# Feature Catalog

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how features are named, grouped, and documented.

A feature is a capability.
It is not a page, route, table, or provider name.

---

## 2. Capability-First Naming Rule

Feature keys must be capability-first.

### Correct examples
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
- billing.manage_subscription

### Incorrect examples
- contacts.enrich_lusha
- research.generate_strategies_openai
- openai.strategy_button
- lusha.enrich_contact

Provider names belong only in:
- provider catalogs
- provider requirements
- integration configuration
- provider management screens

---

## 3. Feature Categories

### Core features
Mandatory workflow capabilities.

Examples:
- research.generate_strategies
- research.background_processing
- results.generate_fit
- results.generate_dossier

### Add-on features
Optional premium or plan-dependent enhancements.

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

## 4. Module-to-Feature Relationship

A feature must belong to a module context.

Examples:
- research.generate_strategies -> research
- results.export.dossier -> results
- results.shortlist -> results
- contacts.enrich_person -> contacts
- crm.sync.import -> crm_opportunities
- billing.manage_subscription -> billing

A feature may depend on another module being enabled, but its primary home must still be explicit.

---

## 5. Suggested Feature Catalog Metadata

Each feature definition should include at least:

- key
- label
- moduleKey
- category
- description
- visibilityMode
- requiredRoles
- providerBacked
- providerCapabilityRequirements
- dependencyKeys
- entitlementKey
- optionalPlanKeys
- quotaMeterKey (optional)

---

## 6. Visibility vs Enablement

### visible
Whether the user should see the feature at all.

### enabled
Whether the user can currently execute the feature.

Examples:
- a visible but disabled export button
- a visible but disabled enrichment action
- a hidden feature if the organization lacks the module entirely

---

## 7. Baseline Example Catalog

### research
- research.start
- research.generate_strategies
- research.background_processing

### results
- results.generate_fit
- results.generate_dossier
- results.shortlist
- results.export.csv
- results.export.dossier
- results.export.pdf
- results.compare_candidates

### companies
- companies.find_similar
- companies.local_content_score
- companies.search_external_source

### contacts
- contacts.enrich_person
- contacts.export.contact

### crm_opportunities
- crm.sync.import
- crm.sync.export

### billing
- billing.manage_subscription
- billing.view_credit_usage

---

## 8. Hard Rule

Do not create product structure from provider names.
The user should see capability-driven actions, not vendor-driven actions.
