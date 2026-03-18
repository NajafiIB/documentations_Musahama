# Service Directory Map

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the official structure of the `services/` folder.

The goal is:
- one service area per major domain
- predictable file placement
- no random service sprawl
- AI-friendly implementation

---

## 2. Canonical Folder Structure

```text
src/
  services/
    supabase/
      client.ts
      server.ts
      middleware.ts

    organizations/
      resolve-current-organization.ts
      get-active-memberships.ts
      list-organizations.ts
      get-organization-settings.ts
      update-organization-settings.ts
      invite-member.ts
      accept-invitation.ts

    crm-opportunities/
      list-opportunities.ts
      get-opportunity-detail.ts
      create-opportunity.ts
      update-opportunity.ts

    mandates/
      list-mandates.ts
      get-mandate-detail.ts
      create-mandate.ts
      update-mandate.ts
      list-mandate-files.ts
      attach-mandate-file.ts

    research/
      list-research.ts
      get-research-detail.ts
      create-research.ts
      update-research.ts
      list-strategies.ts
      create-research-constraint.ts

    results/
      list-results.ts
      get-result-detail.ts
      shortlist-result.ts
      export-result-dossier.ts
      export-result-csv.ts

    companies/
      list-companies.ts
      get-company-detail.ts
      upsert-company.ts
      list-company-domains.ts

    contacts/
      list-contacts.ts
      get-contact-detail.ts
      upsert-contact.ts
      list-contact-emails.ts
      list-contact-phones.ts

    integrations/
      list-integrations.ts
      get-integration-detail.ts
      connect-integration.ts
      disconnect-integration.ts
      get-provider-status.ts

    billing/
      get-billing-summary.ts
      get-credit-ledger.ts
      get-current-plan.ts
      create-checkout-session.ts
3. Canonical Minimum Folders

These folders are required in the reconciled structure:

supabase

organizations

crm-opportunities

mandates

research

results

companies

contacts

integrations

billing

4. Optional Support Folders

These may exist if needed, but must stay disciplined:

auth

files

analytics

shared

Use optional folders only when the concern does not belong cleanly to one domain module.

5. Folder Responsibility Rule

Each domain folder should own:

list loaders

detail loaders

create/update/delete helpers

domain DTO shaping

domain-specific server reads

mutation helpers

Do not put cross-domain architecture rules here.
Those belong in:

docs

feature-system

shared typed contracts

server APIs if truly needed

6. Naming Rule

Use:

kebab-case filenames

verb-first or intent-first file names

singular purpose per file

Correct:

get-result-detail.ts

list-companies.ts

connect-integration.ts

Incorrect:

results.ts

companyStuff.ts

doEverything.ts

7. Final Rule

A service folder is organized by domain boundary, not by SQL table count.
One domain may read multiple tables if that is the correct business read model.


---
