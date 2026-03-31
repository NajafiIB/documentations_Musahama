# Services Implementation Rules

Owner: Platform Architect
Last Updated: 2026-03-31
Version: 1.1
Status: Approved

## 1. Purpose

Give developers and AI coding agents strict rules for implementing the service layer.

## 2. Required Rules

1. One domain service folder per major module or tenant or platform concern
2. Use centralized Supabase clients only
3. Keep sensitive service logic server-side
4. Apply organization and audit fields automatically in mutations
5. Return typed DTOs instead of raw unbounded rows
6. Keep normalized source-of-truth reads in final UI service paths
7. Keep page files thin
8. Keep capability truth out of pages and out of ad hoc service conditionals

## 3. What Developers Must Do

- create list and detail service functions per domain
- create mutation helpers per business action
- keep organization resolution in services, providers, or hooks
- shape stable DTOs
- use server-side services for secure joins and sensitive reads
- update docs when service contracts change

## 4. What Developers Must Not Do

Do not:

- issue ad hoc database queries from page files
- expose sensitive joins to the client without review
- mix authorization truth into random service branches
- return raw rows when the caller needs a stable DTO contract
- scatter `.from(...).select(...)` calls across page files
- initialize random Supabase clients
- return secrets to the client
- build final pages around transitional blobs
- hardcode capability access in service files as a substitute for feature-system
- let forms pass ownership fields unchecked
- write one giant service file for the whole app

---

## 5. Testing Requirements

Services must be tested for:
- organization scoping
- inactive membership handling
- DTO correctness
- mutation audit field application
- sensitive field sanitization
- normalized source-of-truth reads
- server-only path behavior where applicable

---

## 6. Documentation Update Rule

Any change to:
- service folder structure
- DTO contracts
- mutation ownership rules
- server-only boundaries
- normalized read model decisions

must also update:
- docs/services/*
- related docs/database/*
- related docs/auth/* or docs/authorization/* if affected
- related docs/feature-system/* if runtime inputs change

---

## 7. Final Rule

If a developer asks “where should this data-access logic go?”
the default answer is:
- if it fetches or mutates domain data -> `services/`
