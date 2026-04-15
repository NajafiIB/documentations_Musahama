# Module Catalog

## Purpose

This document describes the current canonical module catalog for Musahama.

It must match the implementation registry in:

- `src/platform/modules/registry.ts`
- `src/platform/modules/utility-manifests.ts`
- `src/modules/*/manifest.ts`

## Official Navigable Modules

### Platform

- `dashboard` -> `/dashboard`
- `approvals` -> `/approvals`
- `activity` -> `/activity`

### Solutions

- `origination_match` -> `/origination-match`
- `supplier_development_program` -> `/supplier-development-program`
- `musahama_strategy_management` -> `/musahama-strategy-management`
- `negotiator` -> `/negotiator`
- `compliance_guardian` -> `/compliance-guardian`
- `funding_orchestrator` -> `/funding-orchestrator`

### Shared Data

- `companies` -> `/companies`
- `contacts` -> `/contacts`
- `integrations` -> `/settings/integrations` with legacy alias `/integrations`
- `data_packs` -> `/settings/data-sources` with legacy alias `/data-packs`

### Admin

- `billing` -> `/settings/plan-billing` with legacy alias `/billing`
- `settings` -> `/settings`

## Hidden Legacy Compatibility Modules

These remain in the catalog for compatibility and gating, but not primary navigation:

- `crm_opportunities` -> `/crm-opportunities`
- `mandates` -> `/mandates`
- `research` -> `/research`
- `results` -> `/results`

`crm_opportunities` is currently a hidden legacy catalog entry rather than an active workspace route.

## Legacy Alias Rule

`Origination Match` owns these legacy aliases:

- `/mandates`
- `/research`
- `/results`

That means the user is still considered inside the `Origination Match` solution area when browsing those routes.

## Local Navigation Structure

`Origination Match` owns these canonical subroutes:

- `/origination-match/mandates`
- `/origination-match/research`
- `/origination-match/results`
- `/origination-match` as the report home

`Supplier Development Program` owns these canonical subroutes:

- `/supplier-development-program/cases`
- `/supplier-development-program/catalog`
- `/supplier-development-program/settings`
- `/supplier-development-program/owner`
- `/supplier-development-program` as the report home

`Musahama Strategy Management` owns these canonical subroutes:

- `/musahama-strategy-management`
- `/musahama-strategy-management/owner`
- `/musahama-strategy-management/launch`
- `/musahama-strategy-management/plan/[planId]`

`Settings` owns these canonical subroutes:

- `/settings`
- `/settings/workspace`
- `/settings/solutions`
- `/settings/integrations`
- `/settings/automations`
- `/settings/data-sources`
- `/settings/usage`
- `/settings/plan-billing`
- `/settings/account`

Internal operator tools also exist under settings:

- `/settings/view-standard`
- `/settings/delivery-orchestrator`

## Default Enablement

Currently default-enabled for organizations:

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

Currently not default-enabled:

- `musahama_strategy_management`
- `negotiator`
- `compliance_guardian`
- `funding_orchestrator`

## What Is Not a Module

These are not top-level modules:

- discovery
- shortlist
- dossiers
- one-pagers
- CRM sync as a product area
- dataset releases

Those should remain:

- features
- artifacts
- subviews
- actions
- outputs

## Rule

Any change to the module list must be updated in:

- docs
- specs
- the shared module registry
- the workspace shell
