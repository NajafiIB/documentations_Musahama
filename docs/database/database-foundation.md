# Database Foundation

## Purpose

The database supports a multi-layer platform:

- tenancy and memberships
- module and entitlement control
- shared business entities
- retained origination workflow state
- shared module runtime
- data-pack catalog and bindings

## Current Mental Model

Think about the schema in four main parts:

### 1. Control plane

- organizations
- memberships
- plans
- subscriptions
- modules
- organization_modules

### 2. Shared entity plane

- companies
- contacts
- contact_emails
- contact_phones
- evidence
- psych_profiles
- lmc_fits
- dossiers

### 3. Bridge workflow plane

The existing origination workflow still relies on:

- mandates
- research
- strategies
- research_results
- research_run_logs

### 4. Shared runtime and data-pack plane

- module runtime tables
- capabilities
- datasets
- organization dataset bindings
- organization module integration bindings
