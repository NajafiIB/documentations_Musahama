# Specs

This folder contains the machine-readable version of the platform rules.

Use both:
- `docs/` for human-readable architecture and implementation guidance
- `specs/` for machine-readable structured truth

## Current spec files
- `specs/modules/module-catalog.yaml`
- `specs/roles/role-matrix.yaml`
- `specs/routes/route-map.yaml`
- `specs/features/feature-catalog.yaml`
- `specs/workflows/workflow-map.yaml`
- `specs/database/source-of-truth.yaml`
- `specs/platform/runtime-plane.yaml`
- `specs/data-packs/data-pack-catalog.yaml`

## Rules
1. if `docs/` and `specs/` disagree, fix the mismatch immediately
2. do not invent keys outside these specs without updating them
3. update specs whenever architecture rules change
