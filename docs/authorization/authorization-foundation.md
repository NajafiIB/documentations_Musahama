# Authorization Foundation

## Purpose

Authorization decides whether a user can access an organization, a module, and eventually an action.

The current system must understand the platform as a grouped module workspace, not as a flat list of old workflow pages.

## Core Runtime Inputs

Authorization depends on:

- authenticated user
- resolved current organization
- active membership
- membership role
- organization status
- module enablement
- feature or dataset entitlement where relevant
- RLS for final data enforcement

## Current Module Model

Primary top-level areas now include:

- `dashboard`
- `approvals`
- `activity`
- solution modules
- shared-data utilities
- admin areas

Legacy workflow routes remain valid, but they are compatibility surfaces.

## Important Rule

Hidden navigation is not authorization.

Real enforcement must still come from:

- server-side checks
- runtime state resolution
- RLS
