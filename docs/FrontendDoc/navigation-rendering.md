# Navigation Rendering

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how the sidebar and other primary navigation surfaces are rendered.

---

## 2. Canonical Module List

The only official top-level navigation items are:

- dashboard
- crm_opportunities
- mandates
- research
- results
- companies
- contacts
- integrations
- billing
- settings

---

## 3. Navigation Rule

Navigation must be module-driven.

This means:
- module catalog provides the allowed module keys
- feature-system/runtime provides resolved module visibility
- sidebar renders only visible modules

The sidebar must not be hardcoded as a static tab array divorced from runtime state.

---

## 4. Render Sequence

Navigation rendering should follow this sequence:

1. resolve current organization
2. resolve current role
3. resolve enabled module state
4. filter visible modules
5. map visible modules to labels/icons/routes
6. render navigation

---

## 5. Recommended Nav Item Shape

A navigation item should effectively carry:
- module key
- route
- label
- icon
- visible
- enabled
- active

The navigation component should consume this prepared shape.
It should not invent the rules itself.

---

## 6. What Must Not Be Top-Level Nav

Do not create top-level nav items for:
- discovery
- shortlist
- dossiers
- CRM sync
- analytics

These are not modules.

They belong inside:
- results
- research
- dashboard widgets
- secondary tabs
- actions
- detail sections

---

## 7. Access and Route Rule

Hiding a sidebar item is not enough.

Every protected route must also be guarded separately.

Navigation rendering is a UI concern.
Actual access must still be checked by:
- auth/bootstrap logic
- runtime module resolution
- server-side route/layout checks

---

## 8. Settings Rule

Settings appears as one top-level module in navigation, but it must support subsection-based access internally.

Do not treat every settings section as having the same access level.

---

## 9. Final Rule

If the sidebar differs from runtime module truth, the sidebar is wrong.
