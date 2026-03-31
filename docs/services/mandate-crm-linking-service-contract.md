# Mandate CRM Linking Service Contract

## Purpose

Define the service-layer contract for linking an external CRM opportunity to a Musahama mandate without promoting the external opportunity into a canonical internal record.

## Core Rule

The service layer may reference external CRM identifiers and snapshots, but the internal source of truth remains the mandate and its link record.

## Required Capabilities

- fetch available external CRM opportunities through the integration layer
- create or update a mandate-level link record
- prefill mandate fields from the selected external opportunity
- preserve organization scope and audit fields
- support later downstream sync workflows without redefining the external opportunity as an internal module
