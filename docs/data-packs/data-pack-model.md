# Data Pack Model

## Purpose

Data packs are purchasable datasets exposed through the platform. They are not top-level modules.

They exist so the platform can sell:

- shared data products
- premium data readiness
- module-specific enhancement packs

without turning every dataset into a separate application area.

## Current Tables

The current data-pack plane is backed by:

- `datasets`
- `dataset_releases`
- `module_dataset_requirements`
- `organization_dataset_entitlements`
- `organization_module_datasets`
- `organization_module_integrations`

## Current Dataset Keys

Seeded dataset keys:

- `company_intelligence`
- `contact_intelligence`
- `market_signals`
- `procurement_intelligence`
- `local_content_reference`
- `funding_programs`

## How Data Packs Work

### 1. Dataset definition

`datasets` defines the product and commercial identity of a data pack.

### 2. Release tracking

`dataset_releases` lets the platform describe available versions or release labels.

### 3. Module requirements

`module_dataset_requirements` defines whether a dataset is:

- `required`
- `optional`
- `enhancer`

for a given module.

### 4. Organization entitlement

`organization_dataset_entitlements` records whether an organization can use a dataset at all.

### 5. Module binding

`organization_module_datasets` records whether a dataset is actively bound to a module for a specific organization.

## Module Examples

Current seeded expectations:

- `origination_match`
  - `company_intelligence`
  - `contact_intelligence`
- `musahama_strategy_management`
  - `local_content_reference`
  - `market_signals`
- `negotiator`
  - `contact_intelligence`
- `compliance_guardian`
  - `procurement_intelligence`
  - `local_content_reference`
- `funding_orchestrator`
  - `funding_programs`

## Developer Rule

When adding a new data pack:

- add it to the catalog tables and specs
- define its module requirement relationships
- document how readiness is shown in the UI
- do not model it as a top-level module unless it is truly a product surface, not just data
