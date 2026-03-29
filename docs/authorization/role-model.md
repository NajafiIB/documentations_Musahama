# Role Model

## Core Principle

Roles are organization-scoped.

They are not page-scoped and they are not a substitute for module enablement.

## Current Mental Model

Role resolution answers:

- can the user enter this workspace area?
- can the user create or modify records?
- can the user approve or administer sensitive actions?

It works together with:

- organization membership
- module enablement
- entitlement checks

## Practical Rule

Developers should not hardcode route-specific role rules around legacy pages as if they were still the product model.

Instead:

- reason from the current module groups
- then apply action-level checks inside the owning service or platform flow
