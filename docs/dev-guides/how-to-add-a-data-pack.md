# How to Add a Data Pack

## Goal

Use this guide when introducing a new sellable or bindable dataset.

## Implementation Steps

1. Add the dataset definition to the database catalog and migrations
2. Add module requirement mappings where appropriate
3. Update the data-pack overview code if new readiness rules are needed
4. Update docs and specs

## Required Tables

Typical touch points:

- `datasets`
- `dataset_releases`
- `module_dataset_requirements`
- `organization_dataset_entitlements`
- `organization_module_datasets`

## Docs and Specs Required

Update:

- `docs/data-packs/data-pack-model.md`
- `specs/data-packs/data-pack-catalog.yaml`

If the data pack materially changes a module contract, also update:

- `docs/feature-system/module-catalog.md`
- `specs/modules/module-catalog.yaml`

## Rule

Do not model a data pack as a top-level module unless it truly becomes a navigable product area instead of a shared dataset product.
