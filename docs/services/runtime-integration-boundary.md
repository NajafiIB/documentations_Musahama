# Runtime Integration Boundary

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Clarify the boundary between `services/` and `feature-system/`.

This is where teams usually make a mess.

---

## 2. Services vs Feature-System

### services/
Own:
- fetching domain data
- mutating domain data
- reading modules/features/integrations/credits as raw runtime inputs
- returning stable DTOs

### feature-system/
Owns:
- module visibility truth
- feature availability truth
- provider requirement evaluation
- reason codes for unavailable capability states

---

## 3. Correct Relationship

Services provide runtime inputs.
Feature-system resolves runtime capability truth.

Example:
- services fetch enabled modules, feature entitlements, provider states, credit summary
- feature-system decides whether `results.export.dossier` is visible/enabled and why

---

## 4. Correct Pattern

### module check path
Page or layout
→ feature-system runtime hook
→ module resolver
→ service
→ Supabase

### feature check path
Action or component
→ feature-system runtime hook
→ feature resolver
→ service(s)
→ Supabase

### provider check path
Action
→ feature-system runtime hook
→ provider resolver
→ integrations service
→ Supabase

---

## 5. What Services Must Not Do

Services must not become the UI capability source of truth.

Do not scatter inside services:
- button visibility rules
- ad hoc page-specific role logic
- sidebar composition rules
- arbitrary hidden/disabled UI decisions

---

## 6. What Feature-System Must Not Do

Feature-system must not become a replacement data access layer for all domain reads.

Do not make feature-system responsible for:
- company detail loading
- contact archive loading
- mandate CRUD
- general results list loading

Those stay in services.

---

## 7. Final Rule

Services supply data.
Feature-system resolves capability.
UI consumes both.
