# Module Access Rules

## Purpose

This page defines how access to workspace areas is resolved in the current platform model.

## Current Module Groups

### Platform

- `dashboard`
- `approvals`
- `activity`

### Solutions

- `origination_match`
- `partner_match`
- `negotiator`
- `compliance_guardian`
- `funding_orchestrator`

### Shared Data

- `companies`
- `contacts`
- `integrations`
- `data_packs`

### Admin

- `billing`
- `settings`

### Legacy compatibility

- `crm_opportunities`
- `mandates`
- `research`
- `results`

## Resolution Rule

A module can be used only when all of these are true:

- the user is authenticated
- an active organization is resolved
- the user is an active member of that organization
- the module exists in the catalog
- the module is enabled for the organization
- the user's role is sufficient for the action being attempted

## Legacy Rule

Compatibility routes remain accessible where still enabled, but they should be treated as legacy surfaces under the broader `Origination Match` area rather than as the official long-term module structure.
