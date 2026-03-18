# CRM Opportunities Workflow

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how CRM opportunities enter the system and how they become mandates.

---

## 2. Role in the Product

The CRM Opportunities module is the workflow entry point for externally sourced opportunities.

It supports:
- sync/import from CRM
- manual creation if needed
- review and qualification
- conversion into mandates

It is not the final canonical company/contact archive.

---

## 3. Inputs

An opportunity may come from:

- CRM sync/import
- manual creation by a user
- future integrations through approved service paths

---

## 4. Main Flow

### Step 1 — Opportunity enters system
Create or sync a `crm_opportunities` record.

### Step 2 — Normalize and review
The opportunity is reviewed by a workflow user.

Typical review concerns:
- is it relevant?
- is it complete enough?
- does it need edits before conversion?
- does it belong in this organization workflow?

### Step 3 — Convert to mandate
A user converts the opportunity into a mandate.

This is the key transition.
After this point, active targeting/research work happens in the Mandates and Research modules.

### Step 4 — Preserve linkage
The resulting mandate should retain traceable linkage back to the originating opportunity where applicable.

---

## 5. Expected UI Surface

### Archive/List
- opportunity table/list
- filters
- search
- sync/import trigger
- create manually action if enabled

### Detail
- opportunity summary
- source metadata
- qualification/review status
- convert to mandate action

---

## 6. Allowed Actions

Examples of capability-level actions:
- crm.sync.import
- crm.sync.export
- create opportunity
- update opportunity
- convert to mandate

These actions must still go through:
- services
- feature-system
- RLS

---

## 7. Data Touchpoints

Primary table:
- crm_opportunities

Related tables/services may include:
- organization_integrations
- mandates
- organization_feature_entitlements
- organization_modules

---

## 8. Hard Rules

1. CRM sync is a feature, not a top-level module
2. CRM opportunity records are workflow inputs, not final company/contact records
3. conversion to mandate must use a controlled service action
4. importing from CRM must not bypass organization ownership rules
5. opportunity review state must not be stored only in UI state

---

## 9. Output of This Workflow Stage

The output is:
- a reviewed opportunity record
- or a created mandate

The primary downstream handoff is into the Mandates workflow.
