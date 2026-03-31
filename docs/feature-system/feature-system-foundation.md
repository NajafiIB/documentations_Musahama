# Feature System Foundation

## Purpose

The feature system governs what an organization can access at runtime.

In the current platform, that means keeping these concepts separate:

- modules
- capabilities
- data packs
- entitlements
- integrations

## Current Product Structure

The platform is grouped into:

- utility modules
- solution modules
- hidden legacy compatibility modules

It is not provider-first and it is not shaped around a single old workflow chain anymore.

## Runtime Truth

Runtime access should be derived from:

- the module registry
- `organization_modules`
- organization memberships and roles
- feature or dataset entitlements
- integration readiness where needed

## Important Rule

Datasets and data packs are not modules.

Capabilities are not modules either.

The structure is:

- module = product area
- capability = reusable execution behavior
- dataset = purchasable or bindable data product

## Current Module Direction

The canonical module catalog now includes:

- `dashboard`
- `approvals`
- `activity`
- `origination_match`
- `supplier_development_program`
- `partner_match`
- `negotiator`
- `compliance_guardian`
- `funding_orchestrator`
- `companies`
- `contacts`
- `integrations`
- `data_packs`
- `billing`
- `settings`

Canonical utility route ownership is:

- `integrations` -> `/settings/integrations`
- `data_packs` -> `/settings/data-sources`
- `billing` -> `/settings/plan-billing`

Legacy compatibility surfaces remain hidden from primary navigation:

- `crm_opportunities`
- `mandates`
- `research`
- `results`
