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
Recommended supporting folders:

change-requests/
implementation-guides/
reviews/
specs/
tasks/

Recommended meanings:

docs/ = canonical human-readable architecture and implementation rules

change-requests/ = tracked problem statements and requested changes

implementation-guides/ = file-level execution plans for coding agents

reviews/ = architecture reviews and verification notes

specs/ = optional machine-readable structured definitions

tasks/ = optional atomic task breakdowns

8. Folder meanings
docs/auth/

Identity, onboarding, invitations, session routing, password recovery.

docs/authorization/

Role model, module access rules, feature access, route guarding, RLS/runtime boundaries.

docs/database/

Schema model, table meanings, constraints, indexes, RLS expectations, source-of-truth rules.

docs/feature-system/

Module catalog, feature catalog, provider model, entitlement resolution, runtime contracts.

docs/services/

Service boundaries, Supabase client rules, query/mutation patterns, DTO rules, sensitive-data rules.

docs/frontend/

App Router structure, workspace shell, navigation rendering, view framework, page contracts, design system.

docs/workflows/

CRM opportunity → mandate → research → results → canonical promotion flow.

docs/dev-guides/

Onboarding, coding standards, testing rules, AI-agent rules, change-request process, PR review rules, implementation order.

9. Source-of-truth rules
Final source of truth for companies

companies

company_domains

Final source of truth for contacts

contacts

contact_emails

contact_phones

Final source of truth for analysis

evidence

psych_profiles

lmc_fits

dossiers

Workflow tables

Use these for orchestration and process state:

crm_opportunities

mandates

mandate_files

research

strategies

research_results

research_constraints

Do not build final UI around legacy JSON blobs in research_results.

10. Role of Codex

Codex should be used as:

architecture-aware implementation agent

structured reviewer

file-level planner

bounded code modifier

repo-aware documentation consumer

Codex must follow this repo before making implementation decisions.

Codex should not invent architecture that contradicts this repo.

11. Role of AI Studio

AI Studio should be used as:

execution-focused coding agent

bounded implementer

change applier

task-oriented generator

AI Studio should not be treated as the source of truth for:

architecture

module model

workflow model

role model

data source-of-truth decisions

AI Studio should implement against the requirements defined here.

12. Required development workflow

Use this process for every non-trivial change.

Step 1 — Create or identify the change request

Describe:

the problem

expected behavior

affected module/workflow/layer

constraints

acceptance criteria

Step 2 — Check this repository

Identify which docs apply.

Step 3 — Produce an implementation guide

That guide should define:

files to read

files allowed to change

files that must not change

architecture boundaries

acceptance criteria

Step 4 — Implement in the code repo

Use Codex, AI Studio, or a human developer to implement the change.

Step 5 — Review against this repository

Verify:

correct layer ownership

correct source-of-truth usage

correct module/feature behavior

correct org scoping

correct workflow alignment

Step 6 — Update this repo if the architecture changed

If structure, rules, contracts, or flow changed, update docs in the same change cycle.

13. Required status model

Recommended statuses for change requests and work tracking:

Change request status

draft

pending-review

approved

in-progress

blocked

done

rejected

Documentation status

draft

approved

superseded

archived

Review status

pending

passed

failed

needs-rework

14. Non-negotiable rules

Do not:

invent new top-level modules casually

turn shortlist or dossiers into top-level navigation

hardcode sidebar tabs as architecture truth

scatter direct Supabase queries across page components

use provider names as product concepts

use UI-only hiding as real authorization

build final company/contact pages from result blobs

build final analysis pages from transitional research_results blobs

patch bugs in the wrong layer just because it is faster

15. Definition of done

A change is done only when:

the behavior works

the correct layer owns the change

organization scoping is correct

module/feature boundaries are respected

source-of-truth reads are correct

docs are updated if needed

the workflow chain still makes sense

the codebase is cleaner, not messier

A patch that works but increases structural debt is not done.

16. Recommended root files

This repository should keep these root files current:

README.md

AGENTS.md

Optional later:

CONTRIBUTING.md

.github/PULL_REQUEST_TEMPLATE.md

.github/ISSUE_TEMPLATE/*

17. How to use this repo in practice
If you are a human developer

Read the relevant docs before changing implementation.

If you are Codex

Read AGENTS.md, then follow the required read order, then implement only through the correct boundary.

If you are AI Studio

Treat this repo as the architecture contract. Do not improvise around it.

If you are reviewing code

Review the implementation against the rules in this repo, not only against whether the screen appears to work.

18. Final rule

This repository exists to prevent development drift.

If implementation and documentation diverge, resolve the divergence explicitly.
Do not let both versions continue in parallel.
