# Navigation Rendering

## Canonical Source

The workspace navigation must be rendered from the module registry.

Implementation anchors:

- `src/platform/modules/constants.ts`
- `src/platform/modules/types.ts`
- `src/platform/modules/registry.ts`
- `src/platform/modules/utility-manifests.ts`
- `src/modules/*/manifest.ts`

Do not maintain a second manual sidebar catalog in UI code.

## What the Renderer Uses

For each module, navigation rendering depends on:

- `label`
- `route`
- `navGroup`
- `showInNavigation`
- `routeAvailable`
- `legacyAliases`
- runtime enablement for the organization

## Active-State Rules

The renderer should mark a module active when:

- the current pathname matches the module route
- or the pathname matches one of the module's legacy aliases

That is why `Origination Match` still appears active on:

- `/mandates`
- `/research`
- `/results`

## Compatibility Rules

Compatibility routes are still supported, but they should not appear as independent first-class nav items.

Current hidden legacy modules:

- `crm_opportunities`
- `mandates`
- `research`
- `results`

They remain in the catalog for compatibility and gating, not for primary navigation.

Canonical settings-backed utility routes should also preserve their active module state through aliases:

- `/integrations` -> `Integrations`
- `/data-packs` -> `Data Packs`
- `/billing` -> `Billing`

## Developer Rule

If a new module is added:

1. create or update its manifest
2. register it in the shared module registry
3. document it in the docs and specs
4. let the shell render it from that shared contract

Do not patch sidebar links directly as a shortcut.
