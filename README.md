# Musahama Platform — Canonical Documentation Repository

This repository is the **source of truth** for the Musahama platform architecture, workflow design, access model, data model, and implementation rules.

It exists to stop development drift.

The rule is simple:

- **GitHub documentation is the source of truth**
- conversations are not the source of truth
- local patches are not the source of truth
- random notes are not the source of truth

If implementation and this repository disagree, the team must resolve that mismatch explicitly.

---

# 1. What this repository is for

This repository defines:

- platform architecture
- auth and onboarding rules
- authorization model
- database source-of-truth rules
- feature-system rules
- service boundaries
- frontend structure
- workflow design
- developer and AI-agent operating rules

This repository is designed for:

- human developers
- Codex
- AI Studio
- architecture review
- implementation planning
- change control

---

# 2. What this repository is not

This repository is **not** the place for uncontrolled “quick fixes”.

Do not use this repo as:
- a scratchpad
- a place to invent architecture during implementation
- a place to patch around bugs without recording the real decision
- a place to store only aspirational docs disconnected from the real system

If a change matters to the platform, it must be reflected here.

---

# 3. Operating model

The platform should be developed using this control model:

- **This repo** = canonical requirements and architecture
- **ChatGPT + Codex** = architecture review, planning, structured implementation, code review
- **AI Studio** = execution agent that implements bounded changes
- **Implementation repo(s)** = production code and migrations

The intended flow is:

1. a bug, change, or feature request appears
2. the change is described here first or checked against the docs here
3. the required architecture and constraints are clarified here
4. Codex or ChatGPT produces an implementation plan from these docs
5. AI Studio or another coding agent executes the change in the implementation repo
6. the output is reviewed against this repo
7. the docs here are updated if the architecture or behavior changed

No serious change should start as “just patch the code”.

---

# 4. Core architecture principles

The Musahama platform follows these principles:

- the platform is **organization-first**
- organizations are the tenant boundary
- Supabase Auth handles identity
- Supabase RLS is the final database security layer
- modules are top-level navigation areas
- features are capabilities inside modules
- providers are dependencies, not product structure
- feature entitlements are runtime truth
- workflow tables are not always the final source of truth
- canonical entity and analysis tables are the final source of truth for final UI reads

Keep these distinctions clean.

---

# 5. Official top-level modules

These are the only official top-level modules:

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

These are **not** top-level modules:

- discovery
- shortlist
- dossiers
- CRM sync
- analytics

Those belong as:
- features
- actions
- subviews
- detail sections
- exports
- widgets

---

# 6. Required read order

Any developer or AI coding agent working on the Musahama platform must read these folders in this order:

1. `docs/auth/`
2. `docs/authorization/`
3. `docs/database/`
4. `docs/feature-system/`
5. `docs/services/`
6. `docs/frontend/`
7. `docs/workflows/`
8. `docs/dev-guides/`

If you skip that order, you will almost certainly implement the wrong thing.

---

# 7. Repository structure

This repository should contain at least:

```text
docs/
  auth/
  authorization/
  database/
  feature-system/
  services/
  frontend/
  workflows/
  dev-guides/
