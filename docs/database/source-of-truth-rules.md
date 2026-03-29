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
