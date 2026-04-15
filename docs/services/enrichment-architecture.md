# Enrichment Architecture

## Purpose

Musahama supports action-driven enrichment for shared companies and Supplier Development Program supplier defaults.

The current implementation has two enrichment tiers:

- `Fast enrichment`: grounded AI discovery and taxonomy-safe classification.
- `Deep enrichment`: provider-backed verification through Lusha and Unipile.

Initial page loads must never call external enrichment APIs. Tables render only the data already stored in the database. Enrichment starts only after an explicit user action or a future automation operation.

## Runtime Surfaces

Current user-facing surfaces are:

- Companies collection and company detail.
- Supplier Development Program supplier defaults settings.

V1 actions are manual:

- fast enrich selected companies
- fast enrich one company
- deep enrich one company
- fast enrich selected supplier defaults
- fast enrich one supplier default
- deep enrich one supplier default

Bulk and row-level actions enqueue background jobs. The user interface shows queued or processing state and then refreshes from the database as jobs complete.

## Fast Enrichment

Fast enrichment uses a grounded AI provider:

- `gemini`
- `vertex_ai`

The provider must support `firmographic_enrichment`.

The service fetches allowed vocabulary from the database before the AI request and passes it into the prompt. The model is constrained to structured JSON output. Returned taxonomy values are accepted only when they exactly map to allowed database vocabulary.

Company fast enrichment may fill blank fields:

- `legal_name`
- `website_url`
- `description`
- `headquarters_address`
- `phone`
- primary industry relation through `company_industries`

Supplier fast enrichment may fill blank fields:

- linked company `website_url`
- supplier `sector_name`
- supplier `primary_category_id`

Company enrichment must not auto-create industries from AI output.

## Deep Enrichment

Deep enrichment requires both providers to be connected and healthy:

- `lusha`
- `unipile`

Lusha is the canonical provider for company firmographics.

Unipile is the canonical provider for LinkedIn company identity/profile fields.

Deep company enrichment may fill blank fields:

- `legal_name`
- `website_url`
- `description`
- `headquarters_address`
- `phone`
- `external_id`
- `linkedin_url`
- `linkedin_external_id`

Deep supplier enrichment updates the linked company first. If the supplier taxonomy fields are still blank, it then runs the supplier fast-classification path.

## Blank-Only Apply Rule

The default apply mode is fill blanks only.

Existing populated fields are not overwritten by enrichment results unless a later explicit overwrite mode is added. This protects user-corrected records from provider or AI regressions.

## Background Queue

Enrichment runs through a background queue.

Current tables:

- `enrichment_jobs`
- `enrichment_runs`

The browser queues jobs through `/api/enrichment/jobs` and receives a success response when the job is accepted, not when enrichment finishes.

Workers process queued jobs through the enrichment cron/runtime path and write normalized results back into the database. The UI polls job state and refreshes affected rows. External provider calls must remain outside initial page load.

## Audit Model

Every enrichment run records audit data for debugging, billing, and future automation visibility.

Minimum audit concepts:

- organization
- target type and id
- enrichment level
- apply mode
- status
- provider summary
- request payload
- normalized result payload
- applied patch
- skipped fields
- error summary
- user or automation linkage
- timestamps

## Automation Hooks

The same service operations are exposed for future automations:

- `companies.fast_enrich`
- `companies.deep_enrich`
- `sdp.suppliers.fast_enrich`
- `sdp.suppliers.deep_enrich`

V1 does not seed default scheduled automations for enrichment.

## Credit Operations

Enrichment uses distinct credit operation keys:

- `companies.enrich.fast`
- `companies.enrich.deep`
- `sdp.supplier.enrich.fast`
- `sdp.supplier.enrich.deep`

Legacy aliases may exist temporarily, but new callers must quote and charge the exact operation being triggered.

## Provider Configuration

Expected provider keys and capabilities:

- `gemini`: AI provider, `firmographic_enrichment`
- `vertex_ai`: AI provider, `firmographic_enrichment`
- `lusha`: enrichment provider, company firmographics
- `unipile`: enrichment provider, `linkedin_company_profile`

Sensitive configuration stays server-side.

## Implementation References

Primary implementation files:

- `src/services/companies/company-enrichment.ts`
- `src/services/sdp/supplier-profile-enrichment.ts`
- `src/services/enrichment/jobs.ts`
- `src/services/enrichment/runs.ts`
- `src/services/enrichment/lusha.ts`
- `src/services/enrichment/unipile.ts`
- `app/api/enrichment/jobs/route.ts`
- `app/api/cron/enrichment/route.ts`

