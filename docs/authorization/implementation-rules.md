# Authorization Implementation Rules

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Give developers a strict implementation contract for authorization.

---

## 2. Folder Ownership

### `feature-system/`
Use for:
- role matrix
- module rules
- feature rules
- runtime resolvers
- capability hooks

### `features/`
Use for:
- page/module UI
- module-specific components
- forms
- views

### `services/`
Use for:
- Supabase access
- membership reads
- module reads
- feature entitlement reads
- provider/integration reads

### `views/`
Use for reusable presentation layouts only.

---

## 3. Required Frontend Structure

```text
src/
  feature-system/
    catalog/
    permissions/
    resolver/
    runtime/


Recommended contents:

feature-system/
  catalog/
    module-keys.ts
    feature-keys.ts
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
---

##4. What Developers Must Do

centralize role rules

centralize module rules

centralize feature rules

resolve module state before rendering navigation

resolve feature state before enabling actions

keep service queries out of presentational components

keep authorization logic out of page-level hacks

##5. What Developers Must Not Do

Do not:

hardcode tabs in shell/sidebar

write if role === ... throughout components

make page components the source of permission rules

treat provider configuration as product capability naming

build separate permission logic in multiple hooks/stores

bypass RLS assumptions

##6. Minimum Resolver Inputs

Module resolver must consider:

authenticated user

current organization

active membership

role

enabled modules

Feature resolver must consider:

current organization

role

enabled module

feature entitlement

dependencies

provider requirement

credits/quota

provider/system health

##7. Testing Requirements

Authorization tests must cover:

platform roles

workflow roles

module enabled/disabled states

feature enabled/disabled states

route guard outcomes

membership inactive/suspended cases

billing_admin optional visibility cases

##8. Final Rule

If code decides whether a capability is available, it belongs in feature-system/.
If code renders how a module looks, it belongs in features/.
If code talks to Supabase/backend, it belongs in services/.
