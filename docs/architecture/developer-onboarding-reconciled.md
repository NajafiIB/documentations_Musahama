
# Developer Onboarding (Reconciled)

This is the reconciled onboarding version. It aligns module vocabulary, feature vocabulary, role rules, and source-of-truth guidance.

---

# 1. What This Platform Is

This is an AI-assisted research and discovery platform for organizations.

Clients bring a business need through CRM opportunities.
The platform converts that into mandates, launches research, generates strategies, discovers targets, gathers evidence, scores fit, and produces dossiers and other outputs.

The platform is organization-centric.

---

# 2. Layer Model

There are six layers.

## 2.1 Tenancy Layer
- organizations
- organization_members
- profiles

## 2.2 Platform Layer
- plans
- plan_modules
- organization_subscriptions
- modules
- organization_modules
- integration_providers
- organization_integrations
- organization_credit_ledger

## 2.3 Feature Layer
Features are capabilities inside modules.

Examples:
- research.start
- research.generate_strategies
- results.export.dossier
- contacts.enrich_person

## 2.4 Workflow Layer
- crm_opportunities
- mandates
- mandate_files
- research
- strategies
- research_results
- research_constraints

## 2.5 Canonical Entity Layer
- companies
- company_domains
- contacts
- contact_emails
- contact_phones

## 2.6 Analysis Layer
- evidence
- psych_profiles
- dossiers
- lmc_fits

---

# 3. Canonical Module List

The official top-level modules are:

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

Do not use discovery, shortlist, dossiers, or CRM sync as top-level modules.
Those are features, subviews, or embedded concepts.

---

# 4. Product Workflow

CRM Opportunity  
→ Mandate  
→ Research Run  
→ Strategy Generation  
→ Results  
→ Evidence / Analysis  
→ Fit Scoring  
→ Dossier / Output  
→ CRM Sync / Export

Notes:
- `results` is the module name
- `research_results` is the workflow table name

---

# 5. Ownership Rule

Every business record belongs to an organization.

Source of truth:
- `organization_id` owns the record
- `created_by_user_id` and `updated_by_user_id` are audit actors

Never reintroduce user-owned business data.

---

# 6. Source-of-Truth Rule

Use normalized tables as source of truth.

## Canonical entities
- companies
- company_domains
- contacts
- contact_emails
- contact_phones

## Canonical analysis
- evidence
- psych_profiles
- lmc_fits
- dossiers

## Workflow tables
- crm_opportunities
- mandates
- research
- strategies
- research_results
- research_constraints

Do not build final UI around legacy JSON blobs in `research_results`.

---

# 7. Role Model

## Platform operator roles
- owner
- billing_admin
- developer

These manage:
- integrations
- provider/API configuration
- billing
- platform features

## Workflow roles
- owner
- admin
- manager
- analyst
- member
- developer
- billing_admin (optional broader visibility)

These operate:
- crm opportunities
- mandates
- research
- results
- companies
- contacts

---

# 8. Capability-First Rule

Do not model product behavior around provider names.

Bad:
- Lusha workflow
- OpenAI page

Good:
- enrich person
- generate strategies
- export dossier
- sync CRM

Providers are dependencies behind features.

---

# 9. Frontend Architecture Rule

Use this ownership boundary:

- `features/` = module/domain UI implementation
- `feature-system/` = runtime entitlement logic
- `views/` = reusable inline/detail/form patterns
- `services/` = Supabase/backend access

If you are deciding whether a feature is available, it belongs in `feature-system/`.

---

# 10. Security Rule

Security is enforced in three layers:

1. RLS
2. Feature resolver
3. UI visibility

The UI is never the real security boundary.

---

# 11. First Things Every Developer Must Learn

1. `organization_id` is the owner
2. modules are navigation, features are capabilities
3. providers are dependencies, not product concepts
4. results module maps to `research_results`
5. canonical entities and analysis tables are the source of truth
6. RLS is mandatory
7. `feature-system/` owns entitlement logic

---

# 12. Final Rule

When making changes, always check:

- Does this belong to a module or a feature?
- Is this capability-first or vendor-first?
- Is this reading canonical source-of-truth data?
- Is this organization-scoped?
- Is access enforced in RLS and feature resolution?
