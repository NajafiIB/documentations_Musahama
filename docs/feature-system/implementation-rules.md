# Feature System Implementation Rules

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Give developers and AI coding agents strict implementation rules for the feature-system layer.

---

## 2. Required Folder Structure

```text
src/
  feature-system/
    catalog/
    permissions/
    resolver/
    runtime/
Recommended files:

feature-system/
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
3. File Responsibility Rules
catalog/

Define:

canonical module keys

canonical feature keys

feature grouping metadata

permissions/

Define:

official role matrix

module role rules

feature role rules

resolver/

Implement:

module state resolution

feature state resolution

provider state resolution

runtime/

Expose:

hooks

runtime consumers

explanation helpers

4. What Developers Must Do

centralize module keys

centralize feature keys

centralize role rules

use the resolver layer for all capability decisions

keep provider logic below the capability layer

reuse reason codes consistently

keep page components thin

keep services responsible for database reads and mutations

5. What Developers Must Not Do

Do not:

hardcode sidebar tabs

spread if role === logic through components

make a page the source of entitlement logic

name features after providers

read raw provider secrets on the client

reconstruct feature availability from random table reads

bypass module checks because the page is visible

treat feature-system as optional

6. Testing Requirements

Tests must cover:

module visibility per role

feature availability per role

module enabled vs disabled

missing entitlement

missing dependency

missing provider

insufficient quota

provider unavailable

optional billing_admin visibility

settings subsection rules

7. Review Rule

Any PR that changes:

module keys

feature keys

role rules

provider requirement rules

resolver behavior

must also update:

docs/feature-system/*

related docs/authorization/*

related docs/database/* when schema affected

8. AI Implementation Rule

AI coding agents must:

read docs/feature-system/*

read docs/authorization/*

read related docs/database/*

implement only through feature-system + services boundaries

avoid page-level patching as a substitute for runtime design


---

## `docs/feature-system/references.md`

```md
# Feature System References

Use these documents together:

- docs/feature-system/feature-system-foundation.md
- docs/feature-system/module-catalog.md
- docs/feature-system/feature-catalog.md
- docs/feature-system/provider-model.md
- docs/feature-system/entitlement-resolution.md
- docs/feature-system/permissions-and-rules.md
- docs/feature-system/runtime-api-contracts.md
- docs/feature-system/ui-consumption-rules.md
- docs/feature-system/implementation-rules.md

Related documents:
- docs/auth/authentication-flow.md
- docs/authorization/authorization-foundation.md
- docs/authorization/module-access-rules.md
- docs/authorization/feature-entitlements.md
- docs/database/database-foundation.md
- docs/database/source-of-truth-rules.md
The three rules your developer must not violate

feature-system/ must stay the runtime source of truth, the app must keep modules separate from features and providers, and pages must consume resolved state through services/runtime hooks instead of rebuilding logic inline. That is the whole reason this layer exists.
