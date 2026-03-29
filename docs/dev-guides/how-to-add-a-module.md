# How to Add a Module

## Goal

Use this guide when adding a new top-level module or solution module.

## Implementation Steps

1. Add the module key to `src/platform/modules/constants.ts`
2. Create or update a manifest in:
   - `src/platform/modules/utility-manifests.ts` for utility modules
   - `src/modules/<module-key>/manifest.ts` for solution modules
3. Register the manifest in `src/platform/modules/registry.ts`
4. Add the route entry under `app/(workspace)/`
5. Ensure the workspace shell can render the module from the registry
6. Add or seed the module in the database catalog if required
7. Update docs and specs

## Docs and Specs Required

Update at minimum:

- `docs/feature-system/module-catalog.md`
- `specs/modules/module-catalog.yaml`
- `specs/routes/route-map.yaml`

If the module introduces runtime behavior or datasets, also update:

- `docs/platform-runtime/runtime-plane.md`
- `docs/data-packs/data-pack-model.md`
- `specs/platform/runtime-plane.yaml`
- `specs/data-packs/data-pack-catalog.yaml`

## Rule

Do not add a sidebar link directly without first defining the module in the shared registry and docs.
