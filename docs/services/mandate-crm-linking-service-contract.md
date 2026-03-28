# Mandate CRM Linking Service Contract

Owner: Platform Architect
Last Updated: 2026-03-28
Version: 1.0
Status: Approved

## Purpose

Define the canonical service contract for linking a mandate to an external CRM opportunity and importing selected CRM values.

This document is the source of truth for:
- mandate CRM linking commands
- CRM preview/read models
- import behavior
- ownership boundaries

## Ownership rule

CRM opportunity linking belongs in services.

Pages may initiate the action, but they must not directly own:
- external CRM entity lookup
- mandate-to-CRM link persistence
- field import mapping
- downstream CRM sync preparation

## Write-side commands

### `linkMandateToCrmEntity`

Purpose:
- create or update the relationship between a mandate and an external CRM entity

Required inputs:
- `mandateId`
- `providerKey`
- `externalEntityType`
- `externalEntityId`
- `externalEntityLabel` (optional)

Required outcomes:
- create or update a `mandate_crm_links` record
- do not create an internal `crm_opportunities` domain record

### `unlinkMandateFromCrmEntity`

Purpose:
- remove the relationship between a mandate and an external CRM entity

Required inputs:
- `mandateId`
- `providerKey`
- `externalEntityId`

Required outcomes:
- remove or deactivate the relevant `mandate_crm_links` record

### `importCrmFieldsIntoMandate`

Purpose:
- copy selected external CRM values into mandate fields

Required inputs:
- `mandateId`
- `providerKey`
- `externalEntityId`
- `fieldMapping`

Required outcomes:
- selected external CRM values are written into mandate fields
- `last_imported_at` on `mandate_crm_links` may be updated
- no standalone internal CRM opportunity object is created

## Read-side models

### `listAvailableCrmEntities`

Purpose:
- return a filterable list of external CRM opportunities or equivalent entities for operator selection

Must return:
- external entity id
- provider key
- title or label if available
- summary preview fields if available

### `getCrmEntityPreview`

Purpose:
- return previewable source values from the external CRM entity before link/import

Must return:
- provider key
- external entity id
- title
- description
- any other fields needed for operator mapping

### `getMandateCrmLink`

Purpose:
- return the CRM link record for a mandate

Must return:
- mandate id
- provider key
- external entity type
- external entity id
- optional label
- last imported timestamp if available

## Boundary rules

### Services own
- CRM connector calls
- external entity preview
- mandate link persistence
- field import mapping execution

### Frontend owns
- opening the link/import UI
- letting the operator select the CRM entity
- letting the operator choose which fields to import
- displaying current linked values

### Hard rule
The UI must not treat previewed CRM values as canonical internal records until the import command writes the selected values into the mandate.

## Final rule

The service layer links mandates to external CRM records.
It does not create a separate internal CRM opportunities module.
