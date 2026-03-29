# Start Here

## Goal

This page is for developers joining the Musahama codebase and docs for the first time.

By the end of this short path, you should understand:

- what the live platform is
- how navigation and modules work
- where runtime state lives
- how database changes are synced
- how to add new platform building blocks safely

## Fast Read Path

Read these pages in order:

1. [Architecture overview](../architecture/overview.md)
2. [Module catalog](../feature-system/module-catalog.md)
3. [Runtime plane](../platform-runtime/runtime-plane.md)
4. [Data pack model](../data-packs/data-pack-model.md)
5. [Source-of-truth rules](../database/source-of-truth-rules.md)
6. [Workspace shell](../frontend/workspace-shell.md)
7. [Services foundation](../services/services-foundation.md)
8. [Documentation discipline](documentation-discipline.md)

## Repo Anchors

Useful implementation anchors:

- module registry: `src/platform/modules/registry.ts`
- utility module manifests: `src/platform/modules/utility-manifests.ts`
- solution module manifests: `src/modules/*/manifest.ts`
- runtime/data-pack migration: `supabase/migrations/20260329150000_add_platform_runtime_and_catalog.sql`
- current DB contract: `supabase/schema.sql`
- generated DB types: `src/types/database.types.ts`
- Supabase sync workflow: `database/CONTRACT.md`

## What Not To Assume

Do not assume:

- `mandates`, `research`, and `results` are still the official top-level product model
- hidden navigation means secure access
- datasets should be modeled as modules
- legacy workflow tables are the final source of truth for everything

The live product is now a platform with module and runtime layers, even though `Origination Match` still bridges through legacy workflow pages.
