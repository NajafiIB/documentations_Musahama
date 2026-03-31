# Musahama Developer Documentation

This documentation set describes the **current implemented Musahama platform**.

Use it to understand how the platform is built today:

- one workspace shell
- one organization-scoped platform kernel
- shared company and contact entities
- reusable capabilities
- solution modules
- paid data packs
- approval-gated external actions

## Start Here

Read in this order:

1. [Architecture overview](architecture/overview.md)
2. [Auth foundation](auth/auth-foundation.md)
3. [Authorization foundation](authorization/authorization-foundation.md)
4. [Module catalog](feature-system/module-catalog.md)
5. [Runtime plane](platform-runtime/runtime-plane.md)
6. [Database source-of-truth rules](database/source-of-truth-rules.md)
7. [Workspace shell](frontend/workspace-shell.md)
8. [Services foundation](services/services-foundation.md)
9. [Developer onboarding](dev-guides/developer-onboarding.md)

## Current Platform Shape

The live platform is organized into four navigation groups:

- `Platform`: `dashboard`, `approvals`, `activity`
- `Solutions`: `origination_match`, `supplier_development_program`, `partner_match`, `negotiator`, `compliance_guardian`, `funding_orchestrator`
- `Shared Data`: `companies`, `contacts`, `integrations`, `data_packs`
- `Admin`: `billing`, `settings`

Canonical routes for the settings-backed utility areas are:

- `integrations` -> `/settings/integrations`
- `data_packs` -> `/settings/data-sources`
- `billing` -> `/settings/plan-billing`

`Settings` also owns:

- `/settings/solutions`
- `/settings/usage`
- `/settings/account`
- internal operator pages under `/settings/view-standard` and `/settings/delivery-orchestrator`

Legacy routes still exist for the bridge from the original workflow product:

- `/crm-opportunities`
- `/mandates`
- `/research`
- `/results`

Those routes are compatibility surfaces, not the official top-level module model anymore.

## Repo Model

The intended long-term home for these docs is the standalone repository:

- `https://github.com/NajafiIB/documentations_Musahama`

This `docs_repo/` directory is the staging copy kept in sync from the implementation repository until the standalone docs repository becomes the canonical published host.
