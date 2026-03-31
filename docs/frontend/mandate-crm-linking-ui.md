# Mandate CRM Linking UI

## Purpose

Define the approved UI pattern for linking an external CRM opportunity to a mandate.

## Approved Pattern

The CRM opportunity link must appear as a mandate-scoped action, not as a standalone top-level module.

Recommended interaction:

- an `Attach CRM opportunity` action on the mandate surface
- a drawer, modal, or bounded panel to search/select the external record
- a read-only linked-record summary once attached
- explicit sync or refresh controls only where the integration capability allows them

## Disallowed Pattern

Do not expose external CRM opportunities as a first-class internal product page or canonical entity table.
