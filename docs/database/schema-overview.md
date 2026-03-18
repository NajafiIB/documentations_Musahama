# Schema Overview

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Give developers a practical map of the schema by business layer.

---

## 2. Tenancy Layer

### profiles
Purpose:
- application-facing extension of auth.users

Core fields:
- id
- email
- full_name or split name fields depending on migration state
- created_at

Notes:
- id matches auth.users.id
- profile is not organization membership

### organizations
Purpose:
- tenant record

Core fields:
- id
- slug
- name
- legal_name
- billing_email
- status
- settings
- created_by_user_id
- created_at
- updated_at

### organization_members
Purpose:
- attaches users to organizations

Core fields:
- id
- organization_id
- user_id
- role
- status
- invited_by_user_id
- joined_at
- created_at
- updated_at

Official roles:
- owner
- admin
- manager
- analyst
- member
- billing_admin
- developer

Status values:
- invited
- active
- suspended
- removed

### organization_invitations
Purpose:
- required for controlled existing-organization join flow

Notes:
- this table is required even if not yet present in the old schema
- self-join into an existing organization is not allowed

Recommended fields:
- id
- organization_id
- email
- role
- token
- status
- expires_at
- created_by_user_id
- accepted_by_user_id
- accepted_at
- created_at
- updated_at

---

## 3. Platform Layer

### plans
Defines commercial plans.

### plan_modules
Maps plans to modules.

### organization_subscriptions
Tracks live organization plan/subscription state.

### modules
Canonical top-level product areas.

Official module keys:
- dashboard
- crm_opportunities
- mandates
- research
- results
- companies
- contacts
- integrations
- billing
- settings

### organization_modules
Stores module enablement per organization.

### integration_providers
Catalog of supported external providers.

### organization_integrations
Stores organization-level configured provider connections.

### organization_credit_ledger
Tracks purchased/used/admin-granted credit balances.

---

## 4. Feature Layer

### features
Catalog of feature keys.

### feature_dependencies
Declares prerequisite features/modules.

### feature_provider_requirements
Maps capabilities to required provider capabilities.

### organization_feature_entitlements
Stores org-level feature availability.

### plan_features
Recommended for granular plan-to-feature control.

---

## 5. Workflow Layer

### crm_opportunities
Initial imported business opportunities.

### mandates
Business search mandates derived from opportunities.

### mandate_files
Files attached to mandates.

### research
Research runs for mandates.

### strategies
Generated research/search strategies.

### research_results
Candidate outputs from strategies and workflows.

### research_constraints
Explicit research constraints and exclusions.

---

## 6. Canonical Entity Layer

### companies
Canonical discovered/resolved organizations.

### company_domains
Normalized company web domains.

### contacts
Canonical people records.

### contact_emails
Normalized contact emails.

### contact_phones
Normalized contact phones.

---

## 7. Analysis Layer

### evidence
Structured evidence/source snippets.

### psych_profiles
Psychology/communication fit interpretation.

### lmc_fits
Fit scoring and justification.

### dossiers
Summarized analysis package for review/export.

---

## 8. Global/System Tables

### global_config
System-level configuration.
This is not organization-owned.

Hard rule:
- do not store active secrets here in the final model
- move secret-like values to proper secret infrastructure
