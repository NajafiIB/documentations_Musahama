# Mandate CRM Link Model

Owner: Platform Architect
Last Updated: 2026-03-28
Version: 1.0
Status: Approved

## Purpose

Define the canonical model for linking an internal mandate to an external CRM opportunity or equivalent external CRM entity.

This document is the source of truth for:
- what is and is not stored internally
- the meaning of `mandate_crm_links`
- how imported CRM values relate to the mandate record

## Core rule

External CRM opportunities are not canonical Musahama records.

They remain records in the client's CRM system.
Musahama may reference them, preview them, and import selected values from them.
Musahama must not persist them as a standalone internal `crm_opportunities` domain table.

## Canonical internal model

The canonical internal workflow record is:
- `mandates`

The canonical internal CRM-link record is:
- `mandate_crm_links`

## `mandate_crm_links`

Purpose:
Store the relationship between an internal mandate and an external CRM entity.

Minimum canonical fields:
- `mandate_crm_link_id`
- `mandate_id`
- `provider_key`
- `external_entity_type`
- `external_entity_id`
- `external_entity_label` (optional)
- `last_imported_at` (optional)
- `created_at`
- `updated_at`

## Field meaning

### `mandate_id`
The internal mandate being linked.

### `provider_key`
The external CRM platform key or integration key.

Examples:
- salesforce
- hubspot
- dynamics

### `external_entity_type`
The external record type.

Examples:
- opportunity
- deal
- account_opportunity

### `external_entity_id`
The external CRM entity identifier.

### `external_entity_label`
Optional human-readable label for operator convenience.
It is not the canonical source of truth for the external record.

## Imported values rule

If the operator imports title, description, or selected fields from the external CRM opportunity, those values become mandate data.

They do not create a separate internal CRM opportunity record.

## What must not be stored as canonical internal domain state

Do not create an internal table whose purpose is to mirror the external CRM opportunity as if it were a native Musahama module.

Do not treat external CRM opportunity title or description as a separate internal domain object once those values have been copied into the mandate.

## Practical rule

Use:
- `mandates` for internal mandate workflow state
- `mandate_crm_links` for the external CRM relationship

Do not use:
- an internal `crm_opportunities` module table
- a standalone internal CRM opportunity object as a source of truth

## Final rule

Mandates are internal workflow records.
CRM opportunities are external records.
The internal platform stores the link, not a duplicate product module.
