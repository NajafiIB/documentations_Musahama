# Source of Truth Rules

## Core Rule

Not every workflow table is the final source of truth for final UI or downstream reuse.

The current platform distinguishes between:

- shared durable entities
- module-scoped runtime state
- bridge workflow state
- transitional or generated artifacts

## Shared Durable Sources

Use these as final long-lived read models where appropriate:

- `companies`
- `industries`
- `company_industries`
- `contacts`
- `contact_emails`
- `contact_phones`
- `evidence`
- `psych_profiles`
- `lmc_fits`
- `dossiers`

## Runtime Sources

Use the shared runtime plane for cross-module execution state:

- `module_cases`
- `module_runs`
- `module_run_steps`
- `module_artifacts`
- `module_action_requests`
- `module_action_executions`
- `workspace_recent_surfaces`
- `enrichment_jobs`
- `enrichment_runs`

## Billing Source Rule

Current credit balance is organization-scoped and ledger-backed.

Do not use user profile fields as canonical billing balance.

Use:

- organization credit wallet records
- `organization_credit_ledger`
- billing purchase records
- operation cost model rules

for billing state and runtime credit charging.

## Enrichment Source Rule

Enrichment outputs are proposed normalized data plus an audit trail.

The final durable source remains the target entity table after blank-only patches are applied:

- `companies`
- `company_industries`
- `sdp_supplier_profiles`

Use `enrichment_runs` and `enrichment_jobs` for operational audit, debugging, credits, and future automation visibility.

## SDP Source Rule

SDP report calculations use approved facts for the relevant case/reporting scope.

The report must not calculate from only the first uploaded batch or first category when more approved facts exist.

## Origination Bridge Rule

The origination flow still uses:

- `mandates`
- `mandate_crm_links`
- `research`
- `strategies`
- `research_results`
- `research_run_logs`

Those remain operationally important, but they should not automatically be treated as the final source of truth for all downstream UI.

## External CRM Link Rule

External CRM opportunity data should remain an external-link concern, not a new internal canonical entity layer.

Use:

- `mandate_crm_links`

for linkage to external CRM objects where applicable.

## Transitional Fields

Generated or transitional payload fields should be treated carefully.

That includes older result-linked generated content and newly added result-level operational enrichments until they are promoted into shared durable records or formal artifacts.
