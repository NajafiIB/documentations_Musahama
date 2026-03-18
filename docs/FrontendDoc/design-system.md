# Design System

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the UI tone and design system rules for the platform.

---

## 2. Desired Product Feel

The UI should feel:
- professional
- premium
- calm
- highly readable
- modular
- expandable

Do not build a noisy or overly playful UI.

---

## 3. Design Foundation

Use:
- shadcn/ui as the base component system
- Tailwind CSS for styling
- Lucide for icons
- TanStack Table for dense data tables
- React Hook Form + Zod for forms
- Recharts for charts

---

## 4. Brand Colors

### Primary
- #0F766E
- hover: #115E59
- soft: #CCFBF1
- border accent: #5EEAD4

### Accent
- #D97706
- hover: #B45309
- soft: #FEF3C7

Use teal as the primary action color.
Use the yellow accent sparingly.
Keep the rest of the system neutral and readable.

---

## 5. Shell UI Rules

Header, sidebar, and footer should feel consistent across the workspace.
Do not redesign chrome per page.

---

## 6. Capability UI Rule

UI labels should be capability-first.

Correct:
- Enrich Contact
- Generate Strategy
- Export Dossier
- Sync CRM

Incorrect:
- Lusha Action
- OpenAI Strategy Button

Provider requirements are resolved underneath by the runtime layer.

---

## 7. Data-Dense UI Rule

For archive-heavy modules:
- use consistent tables
- keep filters predictable
- keep actions discoverable
- avoid excessive custom layouts when a standard list/detail pattern works

---

## 8. Form Rule

Forms should:
- use shared form primitives
- validate through schema-backed flows
- look consistent across modules
- preserve the same action placement and error style

---

## 9. Feedback Rule

Use shared feedback surfaces for:
- loading
- empty states
- validation errors
- system errors
- unavailable capability explanations

These should not be redesigned differently on every page.

---

## 10. Final Rule

The UI should feel like one expandable workspace, not ten unrelated mini-products.
