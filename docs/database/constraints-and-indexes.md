# Constraints and Indexes

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Document the important uniqueness, lookup, and performance assumptions in the schema.

---

## 2. Core Uniqueness Rules

### organizations
- slug is unique

### profiles
- email is unique

### organization_members
- unique(organization_id, user_id)

### organization_modules
- unique(organization_id, module_id)

### plan_modules
- unique(plan_id, module_id)

### companies
- unique(organization_id, external_id)

### contacts
- unique(organization_id, external_id)

### company_domains
- unique normalized domain per company
- one primary domain per company

### contact_emails
- unique normalized email per contact
- one primary email per contact

### contact_phones
- unique phone per contact
- one primary phone per contact

### organization_integrations
- unique(org, provider, connection_key)
- one default connection per org/provider

### organization_subscriptions
- unique external subscription reference
- one live org/plan pairing

---

## 3. Core Lookup Indexes

### organizations
- name
- status

### profiles
- id

### organization_members
- organization_id
- user_id
- role
- organization_id, user_id, status
- user_id, organization_id, status

### organization_modules
- organization_id
- module_id
- is_enabled

### modules
- category
- is_active
- sort_order

### organization_subscriptions
- organization_id
- plan_id
- status

### organization_integrations
- organization_id
- provider_id
- status

### organization_credit_ledger
- organization_id
- created_at

### mandates
- organization_id
- created_by_user_id
- status

### research
- organization_id
- mandate_id
- created_by_user_id

### research_results
- organization_id
- research_id
- strategy_id
- company_id
- contact_id

### companies
- organization_id
- name
- status
- created_by_user_id

### contacts
- organization_id
- company_id
- full_name
- status

### evidence
- organization_id
- research_result_id

### dossiers
- organization_id

### psych_profiles
- organization_id
- research_result_id unique

### lmc_fits
- organization_id
- research_result_id unique

---

## 4. Design Rule

Developers must not casually remove or rename indexed ownership and lookup fields.
These indexes support:
- tenancy isolation patterns
- SSR bootstrap queries
- runtime membership checks
- entity resolution
- workflow page performance
