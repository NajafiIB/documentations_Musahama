# Module Architecture

## Canonical Module Model

Every module in Musahama is described by a manifest-like contract with these fields:

- `key`
- `route`
- `label`
- `kind`
- `navGroup`
- `showInNavigation`
- `defaultEnabled`
- `localNavigation`
- `shortDescription`
- `requiredCapabilities`
- `requiredDatasets`
- `approvalPolicy`
- `legacyAliases`

The implementation lives in:

- `src/platform/modules/types.ts`
- `src/platform/modules/registry.ts`
- `src/platform/modules/utility-manifests.ts`
- `src/modules/*/manifest.ts`

## Module Kinds

### Utility modules

Always-on or shared workspace surfaces:

- `dashboard`
- `approvals`
- `activity`
- `companies`
- `contacts`
- `integrations`
- `data_packs`
- `billing`
- `settings`

Canonical utility routes now include:

- `integrations` -> `/settings/integrations`
- `data_packs` -> `/settings/data-sources`
- `billing` -> `/settings/plan-billing`

### Solution modules

Business workflows packaged as products:

- `origination_match`
- `supplier_development_program`
- `partner_match`
- `negotiator`
- `compliance_guardian`
- `funding_orchestrator`

### Legacy modules

Compatibility routes retained while the product migrates:

- `crm_opportunities`
- `mandates`
- `research`
- `results`

## Default Enablement

Current default enablement matches the implementation:

- enabled by default:
  - `dashboard`
  - `approvals`
  - `activity`
  - `origination_match`
  - `supplier_development_program`
  - `companies`
  - `contacts`
  - `integrations`
  - `data_packs`
  - `billing`
  - `settings`
- present but disabled by default until sold or enabled:
  - `partner_match`
  - `negotiator`
  - `compliance_guardian`
  - `funding_orchestrator`

## Module Boundaries

Modules may read shared entities, but they should not redefine them.

Shared across the platform:

- organizations
- memberships
- subscriptions
- integrations
- companies
- contacts
- approvals
- datasets

Module-scoped runtime state:

- cases
- runs
- run steps
- module artifacts
- action requests
- action executions

## Legacy Alias Rule

The active bridge is:

- `origination_match` owns the business area
- `/mandates`, `/research`, and `/results` remain live compatibility routes
- active navigation still highlights `Origination Match` when a user is on those routes

Developers should treat those legacy routes as compatibility surfaces, not as the future architecture.

## Local Navigation Model

Modules with structured local navigation currently are:

- `origination_match`
- `supplier_development_program`
- `settings`

The platform should document those subroutes explicitly because they are part of the live route structure, not ad hoc tabs hidden inside page code.
