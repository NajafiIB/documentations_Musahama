# Architecture Overview

## Platform Summary

Musahama is no longer a single workflow app organized around `crm_opportunities`, `mandates`, `research`, and `results` as first-class top-level modules.

The current platform is a unified workspace with:

- a platform kernel
- shared business entities
- reusable capabilities
- solution modules
- paid data packs
- approval-gated external execution

## Core Layers

### 1. Platform kernel

The kernel owns:

- organizations and memberships
- subscriptions and module enablement
- integrations
- approvals
- notifications
- billing and usage
- workspace shell behavior

### 2. Shared entities

The shared entity layer owns canonical data reused across modules:

- companies
- contacts
- evidence
- analysis outputs

This is the long-lived data layer that outlives individual workflow runs.

### 3. Reusable capabilities

Capabilities are execution primitives reused by multiple modules, such as:

- `research_discovery`
- `evidence_enrichment`
- `report_generation`
- `crm_sync`
- `outreach_execution`
- `calendar_booking`
- `negotiation_briefing`
- `compliance_scoring`
- `funding_matching`

### 4. Solution modules

Solution modules package capabilities, data packs, and UX around a business problem:

- `origination_match`
- `supplier_development_program`
- `partner_match`
- `negotiator`
- `compliance_guardian`
- `funding_orchestrator`

### 5. Data packs

Data packs are purchasable datasets bound to modules through entitlements and module-dataset bindings.

Current dataset keys include:

- `company_intelligence`
- `contact_intelligence`
- `market_signals`
- `procurement_intelligence`
- `local_content_reference`
- `funding_programs`

## Current Navigation Model

The workspace shell groups modules into:

- `Platform`
- `Solutions`
- `Shared Data`
- `Admin`

This grouped navigation is the official product structure.

Current grouped ownership is:

- `Platform`: `dashboard`, `approvals`, `activity`
- `Solutions`: `origination_match`, `supplier_development_program`, `partner_match`, `negotiator`, `compliance_guardian`, `funding_orchestrator`
- `Shared Data`: `companies`, `contacts`, `integrations`, `data_packs`
- `Admin`: `billing`, `settings`

Settings-backed utility routes are canonical for:

- `integrations` -> `/settings/integrations`
- `data_packs` -> `/settings/data-sources`
- `billing` -> `/settings/plan-billing`

## Bridge From the Legacy Workflow Product

The original workflow surfaces still exist, but now serve as a bridge:

- `/mandates`
- `/research`
- `/results`
- `/crm-opportunities`

The official solution-module home for that workflow family is:

- `/origination-match`

`Origination Match` is the first solution module, and its current implementation still relies on the existing mandate, research, and result flows while the shared runtime plane is layered in behind it.

## Implementation Rule

When adding or changing platform functionality:

- keep shared concerns in the platform kernel
- keep reusable execution logic in capabilities
- keep long-lived business records in shared entities
- keep workflow-specific UX in modules
- keep dataset packaging separate from modules

Do not reintroduce the old workflow-first top-level architecture in new work.
