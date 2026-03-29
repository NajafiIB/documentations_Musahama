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
- `partner_match` -> `/partner-match`
- `negotiator` -> `/negotiator`
- `compliance_guardian` -> `/compliance-guardian`
- `funding_orchestrator` -> `/funding-orchestrator`

### Shared Data

- `companies` -> `/companies`
- `contacts` -> `/contacts`
- `integrations` -> `/integrations`
- `data_packs` -> `/data-packs`

### Admin

- `billing` -> `/billing`
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

## Default Enablement

Currently default-enabled for organizations:

- `dashboard`
- `approvals`
- `activity`
- `origination_match`
- `companies`
- `contacts`
- `integrations`
- `data_packs`
- `billing`
- `settings`

Currently not default-enabled:

- `partner_match`
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
