# Frontend Implementation Rules

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Give developers and AI coding agents strict rules for implementing the frontend.

---

## 2. Core Rules

1. Build the product as one stable workspace
2. Keep the shell permanent
3. Use canonical module keys and routes only
4. Keep module-driven navigation
5. Use the shared view framework
6. Keep pages thin
7. Keep data access in services
8. Keep capability truth in feature-system
9. Keep final UI on normalized source-of-truth tables
10. Keep secret or sensitive reads server-side

---

## 3. What Developers Must Do

- use the official route map
- use the official folder structure
- use one feature folder per module
- use one service folder per domain
- use feature-system for capability checks
- use the same archive/detail/form patterns across modules
- resolve organization context before protected page rendering
- render sidebar from module state rather than static tabs
- update docs when structure changes

---

## 4. What Developers Must Not Do

Do not:
- hardcode sidebar tabs
- introduce new top-level modules casually
- treat discovery/shortlist/dossiers as top-level nav items
- scatter Supabase queries through pages
- put security or entitlement truth in the store
- rebuild permission logic in buttons and page components
- build final result detail on legacy JSON blobs
- expose sensitive provider data to the client

---

## 5. Vertical Slice Order

Build frontend slices in this order:

1. shell and tenancy
2. CRM opportunities and mandates
3. research
4. results
5. companies and contacts
6. integrations, billing, settings
7. cleanup

Do not try to build every page at once.

---

## 6. Definition of Done for a Frontend Slice

A slice is not done until:
- the route exists
- current organization context works
- module visibility is correct
- feature-gated actions behave correctly
- services are used instead of scattered queries
- loading/empty/error states exist
- view framework patterns are used
- no ad hoc role logic is scattered in UI
- docs are updated

---

## 7. AI Coding Agent Rule

Before changing frontend structure, the agent must read:
- docs/frontend/*
- docs/auth/*
- docs/authorization/*
- docs/feature-system/*
- docs/services/*
- docs/database/source-of-truth-rules.md

The agent must then implement changes through the correct boundary instead of patching random components.

---

## 8. Final Rule

If a change solves the immediate bug but breaks the frontend ownership boundary, it is the wrong change.
