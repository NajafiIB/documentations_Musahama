# State, Providers, and Hooks

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the correct role of providers, hooks, and stores in the frontend.

---

## 2. Providers

Recommended provider files:

- auth-provider.tsx
- organization-provider.tsx
- module-provider.tsx
- theme-provider.tsx
- query-provider.tsx

### auth-provider
Owns session/user context wiring only.

### organization-provider
Owns current organization context exposure.

### module-provider
May expose resolved module state for workspace consumers.
It must consume runtime truth rather than inventing it.

### theme-provider
Owns theme and visual mode context.

### query-provider
Owns server-state/query client wiring.

---

## 3. Hooks

Recommended hook groups:

- hooks/auth/
- hooks/organization/
- hooks/permissions/
- hooks/queries/
- hooks/ui/

### auth hooks
User/session convenience hooks.

### organization hooks
Current organization selection/context hooks.

### permissions hooks
Thin wrappers around feature-system runtime APIs.

### query hooks
DTO/data query wrappers.

### ui hooks
Pure UI behavior only.

---

## 4. Store

Recommended stores:
- app-shell.store.ts
- organization.store.ts
- module.store.ts
- ui.store.ts

Use store for:
- local shell open/close state
- selected filters if appropriate
- local UI preferences
- cached local navigation presentation state

Do not use store as the final source of:
- authorization truth
- entitlement truth
- server-backed provider capability truth
- data security decisions

---

## 5. Hard Rules

1. session/org/module state may be exposed through providers and hooks
2. the actual truth must still come from services and feature-system
3. stores must not replace service reads
4. hooks must stay thin and composable
5. provider composition belongs near app root/layout level
