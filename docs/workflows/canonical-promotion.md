# Canonical Promotion

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how workflow outputs are turned into canonical entity and analysis records.

This is the bridge between:
- workflow tables
and
- final source-of-truth tables

---

## 2. Core Rule

Workflow output is not automatically the final source of truth.

Candidate outputs from `research_results` must be resolved or promoted into normalized records where applicable.

---

## 3. Entity Promotion Targets

### Company promotion
Promote or resolve into:
- companies
- company_domains

### Contact promotion
Promote or resolve into:
- contacts
- contact_emails
- contact_phones

### Analysis promotion
Persist normalized analysis into:
- evidence
- psych_profiles
- lmc_fits
- dossiers

---

## 4. Linkage Rule

Where a result has been resolved to canonical records, keep linkage from workflow result to canonical records.

Examples:
- research_results.company_id
- research_results.contact_id

This preserves traceability between:
- workflow output
- final entity/archive records

---

## 5. Promotion Flow

### Step 1 — Candidate result exists
A `research_results` row contains candidate output.

### Step 2 — Resolve or create canonical entities
Upsert or link company/contact records as needed.

### Step 3 — Persist normalized analysis
Write evidence, fit, dossier, and related analysis to their dedicated tables.

### Step 4 — Maintain traceability
Store the resulting canonical IDs back on the workflow result where applicable.

### Step 5 — Use canonical reads in final UI
Final pages and detail views should prefer canonical and normalized analysis reads.

---

## 6. Hard Rules

1. no final company page should be powered by a result blob alone
2. no final contact page should be powered by a result blob alone
3. analysis must not remain permanently trapped inside `research_results`
4. promotion logic belongs in services/server workflows, not in page components
5. promotion must remain organization-scoped

---

## 7. Upsert Rule

Promotion may require upserts for:
- companies
- contacts
- domains
- emails
- phones

Use disciplined natural keys and service-level validation.
Do not do vague “save whatever is present” writes from the UI.

---

## 8. Final Rule

Results are review/action surfaces.
Companies, contacts, and analysis tables are the final structured records.
