# Auth Foundation

## Identity
Supabase Auth

## Tenancy
Organizations are the tenant boundary.

## Required tables
- profiles
- organizations
- organization_members
- organization_invitations

## Routing
- no session -> /login
- session + no org -> /onboarding
- session + one org -> /dashboard
- session + many orgs -> /select-organization

## Rules
- no protected workspace without active org membership
- no self-join into an existing organization
- invitation required for existing org join
