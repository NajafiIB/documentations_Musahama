# Database Foundation

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the official database model for the Musahama platform.

This document is the source of truth for:
- database layering
- ownership rules
- table categories
- source-of-truth rules
- security expectations
- implementation boundaries

---

## 2. Core Principles

1. The platform is organization-first and multi-tenant
2. Organizations are the tenant boundary
3. Supabase Auth handles authentication
4. Supabase RLS enforces data isolation
5. Workflow tables are not always the final source of truth
6. Canonical entity and analysis tables are the final source of truth for normalized records
7. Pages must not couple directly to transitional DB fields

---

## 3. Layered Database Model

The database is organized into six layers.

### 3.1 Tenancy Layer
Tables:
- organizations
- organization_members
- profiles

### 3.2 Platform Layer
Tables:
- plans
- plan_modules
- organization_subscriptions
- modules
- organization_modules
- integration_providers
- organization_integrations
- organization_credit_ledger

### 3.3 Feature Layer
Tables:
- features
- feature_dependencies
- feature_provider_requirements
- organization_feature_entitlements
- plan_features

### 3.4 Workflow Layer
Tables:
- crm_opportunities
- mandates
- mandate_files
- research
- strategies
- research_results
- research_constraints

### 3.5 Canonical Entity Layer
Tables:
- companies
- company_domains
- contacts
- contact_emails
- contact_phones

### 3.6 Analysis Layer
Tables:
- evidence
- psych_profiles
- lmc_fits
- dossiers

---

## 4. Ownership Rule

All business data is organization-owned unless explicitly global/system-owned.

Required ownership pattern for major business tables:
- organization_id
- created_by_user_id
- updated_by_user_id

Meaning:
- organization_id = tenant owner
- created_by_user_id = creating actor
- updated_by_user_id = last updating actor

Mutation helpers should set these fields automatically where applicable.

---

## 5. Source-of-Truth Rule

### Canonical entities are the source of truth
Use these as final entity records:
- companies
- company_domains
- contacts
- contact_emails
- contact_phones

### Canonical analysis is the source of truth
Use these as final analysis records:
- evidence
- psych_profiles
- lmc_fits
- dossiers

### Workflow tables are orchestration state
Use these for lifecycle/process execution:
- crm_opportunities
- mandates
- mandate_files
- research
- strategies
- research_results
- research_constraints

---

## 6. Transitional Field Rule

The following fields inside `research_results` are transitional only and must not be the final UI data path:
- company_profile
- psych_profile
- lmc_fit
- dossier
- evidence

They may remain temporarily for compatibility, but final pages must read normalized canonical/analysis tables instead.

---

## 7. Security Rule

Database security is enforced in three layers:

1. RLS
2. service/runtime access validation
3. UI consumption of resolved truth

The UI is not the actual security boundary.
