# Table Reference

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## profiles

Purpose:
- profile extension for authenticated users

Key relationships:
- id -> auth.users.id

Rules:
- one row per auth user
- not a membership table

---

## organizations

Purpose:
- tenant root record

Important fields:
- slug must be unique
- status controls tenant availability

Relationships:
- created_by_user_id -> auth.users.id

---

## organization_members

Purpose:
- user membership in an organization

Important fields:
- organization_id
- user_id
- role
- status
- invited_by_user_id
- joined_at

Important rule:
- one membership row per organization/user pair

---

## organization_invitations

Purpose:
- pending invitation before membership exists

Important rule:
- existing organizations must be joined by invitation, not self-signup

Important constraints:
- unique pending invite per organization/email
- unique token
- expiration enforced

---

## modules

Purpose:
- catalog of top-level modules used for navigation and route-level access

Important fields:
- key
- category
- is_active
- sort_order

Hard rule:
- modules are top-level product areas only
- shortlist, dossiers, CRM sync, discovery are not modules

---

## organization_modules

Purpose:
- module enablement by organization

Important fields:
- organization_id
- module_id
- is_enabled

Hard rule:
- module visibility depends on this table plus role rules

---

## plans

Purpose:
- commercial product plans

---

## plan_modules

Purpose:
- plan-level included modules

Important rule:
- plan_modules alone are not enough for fine-grained capability control

---

## organization_subscriptions

Purpose:
- live org subscription state and billing-provider linkage

---

## integration_providers

Purpose:
- provider catalog

Important fields:
- key
- category
- auth_type
- capabilities
- config_schema
- ui_schema
- status

Hard rule:
- providers are dependencies, not product structure

---

## organization_integrations

Purpose:
- configured provider connections for an organization

Important fields:
- provider_id
- connection_key
- status
- secret_ref
- enabled_capabilities
- is_default
- last_error

Hard rule:
- secret_ref and sensitive provider config are server-only concerns

---

## organization_credit_ledger

Purpose:
- credit/usage ledger per organization

Important fields:
- amount
- entry_type
- status
- balance_after
- module_key

---

## features

Purpose:
- catalog of capability-first feature keys

Examples:
- research.generate_strategies
- results.export.dossier
- contacts.enrich_person

---

## feature_dependencies

Purpose:
- declares prerequisites between features/modules

---

## feature_provider_requirements

Purpose:
- maps a feature to provider/capability requirements

---

## organization_feature_entitlements

Purpose:
- org-specific feature enablement

---

## plan_features

Purpose:
- granular feature inclusion by plan

Status:
- recommended and should be present for long-term control

---

## crm_opportunities

Purpose:
- imported or created business opportunities

---

## mandates

Purpose:
- defined mandate for research

Important fields:
- organization_id
- created_by_user_id
- status

---

## mandate_files

Purpose:
- files linked to mandates

---

## research

Purpose:
- research runs for a mandate

Important fields:
- organization_id
- mandate_id
- created_by_user_id

---

## strategies

Purpose:
- generated search/research strategies

---

## research_results

Purpose:
- candidate outputs from strategies and research

Important rule:
- workflow output, not the final canonical source for entities or normalized analysis

May resolve to:
- company_id
- contact_id

---

## research_constraints

Purpose:
- explicit constraints/exclusions/rules for research execution

---

## companies

Purpose:
- canonical organization records

Important rule:
- final source of truth for company records

---

## company_domains

Purpose:
- normalized company domains

Important rule:
- supports primary-domain uniqueness constraints

---

## contacts

Purpose:
- canonical people records

Important rule:
- final source of truth for contact records

---

## contact_emails

Purpose:
- normalized contact emails

Important rule:
- supports one-primary-per-contact constraint

---

## contact_phones

Purpose:
- normalized contact phone numbers

Important rule:
- supports one-primary-per-contact constraint

---

## evidence

Purpose:
- explainability/source evidence for results and outputs

---

## psych_profiles

Purpose:
- persona/communication insight derived from analysis

---

## lmc_fits

Purpose:
- fit score and justification

---

## dossiers

Purpose:
- export/review package for a result
