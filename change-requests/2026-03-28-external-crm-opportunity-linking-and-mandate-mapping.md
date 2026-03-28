# Change Request — External CRM Opportunity Linking and Mandate Mapping

## Status
- done

## Problem

The repository currently treats `crm_opportunities` as if it were an internal top-level module and an internal workflow table.

That is the wrong model.

External CRM opportunities belong to the client's CRM platform, not to Musahama's internal product structure.

## Expected behavior

The platform must treat CRM opportunities as external records that can be:
- viewed from connected CRM systems
- linked to a mandate
- used to prefill mandate fields
- used later for downstream CRM sync workflows

The platform must not:
- store external CRM opportunities as canonical internal domain records
- expose CRM opportunities as a standalone top-level module or sidebar tab

## Required architecture change

- remove `crm_opportunities` from the official top-level module list
- replace internal CRM opportunity storage with mandate-level link records
- define a canonical `mandate_crm_links` model
- define the mandate-page CRM linking UI as an action/button/drawer, not a tab

## Affected areas

- `README.md`
- `AGENTS.md`
- `docs/frontend/frontend-foundation.md`
- `docs/feature-system/feature-catalog.md`
- `docs/database/source-of-truth-rules.md`
- `docs/workflows/implementation-rules.md`
- `docs/database/mandate-crm-link-model.md`
- `docs/services/mandate-crm-linking-service-contract.md`
- `docs/frontend/mandate-crm-linking-ui.md`

## Acceptance criteria

- `crm_opportunities` is no longer treated as a top-level module
- external CRM opportunities are no longer treated as an internal canonical table
- mandate-level CRM linking is defined canonically
- the mandate-page UI pattern is defined canonically

## Notes

This is a documentation-first architecture correction. It does not by itself refactor the implementation repo.
