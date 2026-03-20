# Organization Context Services

Owner: Platform Architect
Last Updated: 2026-03-20
Version: 1.0
Status: Approved

## Purpose

Define how current organization context is resolved in the service layer.

## Responsibilities

The service layer must support:
- current user resolution
- active membership lookup
- current organization selection
- multi-organization handling
- no-organization onboarding routing

## Core rules

- organization context is resolved before protected workspace rendering
- profile is not the same as membership
- inactive memberships must not act as active context
- organization context must not be guessed from route alone

## Suggested outputs

A resolver should return one of:
- no_session
- no_membership
- single_organization
- multi_organization

## Related documents

- docs/auth/authentication-flow.md
- docs/services/services-foundation.md
- docs/frontend/workspace-shell.md
