# UI Consumption Rules

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how the UI must consume resolved module and feature state.

The UI is a consumer of runtime truth.
It is not the source of truth.

---

## 2. Module UI Rule

If a module is unavailable:
- hide it from sidebar
- block direct route access separately
- do not rely only on sidebar hiding

If a module is available:
- show it in navigation
- allow route-level rendering
- resolve feature states inside the page

---

## 3. Feature UI Rule

If a feature is unavailable but the module is available:
- hide or disable only the action/widget/sub-capability
- keep the page itself accessible

Examples:
- results page visible
- dossier export button disabled
- contact detail visible
- enrich contact action disabled

---

## 4. Capability-First UI Rule

UI labels should be capability-first.

Correct:
- Enrich Contact
- Generate Strategy
- Export Dossier
- Sync CRM

Incorrect:
- Lusha Action
- OpenAI Strategy Button
- CRM Vendor Sync Button

Provider requirements are resolved underneath through the runtime layer.

---

## 5. Disabled State Rule

The UI should be able to explain disabled states using reason codes.

Examples:
- missing entitlement
- provider not connected
- insufficient quota
- missing dependency
- module disabled

---

## 6. Consistency Rule

The same feature key must produce the same state wherever it appears.

Example:
`results.export.dossier` must not be:
- enabled in one component
- disabled in another
- hidden in a third

unless a documented scope/substate explains the difference.

---

## 7. Results Page Rule

Concepts like shortlist and dossier generation must appear as:
- result actions
- result detail sections
- export controls
- subviews

They must not be promoted into fake top-level modules.

---

## 8. Final Data Rule

Final result detail UI should read normalized canonical and analysis data, not transitional workflow blobs.

Use:
- companies
- contacts
- evidence
- psych_profiles
- lmc_fits
- dossiers

Do not make final UI depend on legacy JSON fields in `research_results`.

---

## 9. Hard Rule

The UI must consume resolved state from the feature-system.
Do not add ad hoc role checks in each button.
