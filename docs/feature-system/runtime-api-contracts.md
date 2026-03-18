# Runtime API Contracts

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the APIs, hooks, and contracts that the rest of the app should use to consume the feature system.

This is the runtime surface that pages and features must depend on.

---

## 2. Rule

Pages and features must ask the feature-system for resolved state.
They must not reconstruct access logic themselves.

---

## 3. Required Runtime APIs

The feature-system should expose contracts like:

- getEnabledModulesForCurrentOrg()
- getModuleState(moduleKey)
- getFeatureState(featureKey)
- getProviderState(capabilityKey)
- explainFeatureDisabled(featureKey)

---

## 4. Recommended Hook Surface

```ts
useModuleState("results")
useFeatureState("results.export.dossier")
useProviderState("contacts.enrich_person")
5. Recommended Resolver Files
src/feature-system/
  catalog/
    module-keys.ts
    feature-keys.ts
    feature-groups.ts
  permissions/
    role-matrix.ts
    module-rules.ts
    feature-rules.ts
  resolver/
    resolve-module-state.ts
    resolve-feature-state.ts
    resolve-provider-state.ts
  runtime/
    use-module-state.ts
    use-feature-state.ts
    use-provider-state.ts
6. Suggested Read Path
module check path

Page or layout
-> module hook
-> module resolver/service
-> Supabase-backed service layer

feature check path

Action or component
-> feature hook
-> feature resolver/service
-> services + runtime dependency checks

provider check path

Action
-> provider hook
-> provider resolver
-> integration/provider service

7. Suggested Server-Side Resolution

Prefer server-side resolution for:

current organization bootstrap

enabled module state

provider-backed feature resolution

billing summary joins

anything involving secrets

anything needed during SSR route gating

8. Response Design Rule

Runtime contracts should return:

stable keys

visible/enabled booleans

explicit reason codes

enough metadata for UI explanation

no raw secret/provider config

9. Anti-Pattern

Do not let a page do this:

read organization_modules directly

read organization_feature_entitlements directly

read organization_integrations directly

infer missing provider from raw rows

guess role behavior in the component

