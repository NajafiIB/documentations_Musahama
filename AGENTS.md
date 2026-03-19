# AGENTS.md

Scope: entire repository unless a deeper `AGENTS.md` overrides part of it.

This file defines how AI coding agents must operate in this repository.

## Repository identity
This repository is the canonical documentation repository for the Musahama platform. It is the source of truth for auth, authorization, database rules, feature-system rules, service boundaries, frontend structure, workflow design, and repo governance.

## Mandatory read order
Before making any meaningful change, read in this order:
1. `docs/auth/`
2. `docs/authorization/`
3. `docs/database/`
4. `docs/feature-system/`
5. `docs/services/`
6. `docs/frontend/`
7. `docs/workflows/`
8. `docs/dev-guides/`

## Hard architecture rules
1. Modules are not features.
2. Providers are dependencies, not product structure.
3. `feature-system/` owns runtime capability truth.
4. `services/` own reads, writes, and DTO shaping.
5. `features/` own domain UI.
6. `views/` own reusable view patterns.
7. Pages and routes stay thin.
8. RLS is the final security boundary.
9. Final UI must prefer canonical entity and analysis tables.
10. Legacy JSON blobs in `research_results` are not the final source of truth.

## Source-of-truth rules
Use these as final entity truth:
- `companies`
- `company_domains`
- `contacts`
- `contact_emails`
- `contact_phones`

Use these as final analysis truth:
- `evidence`
- `psych_profiles`
- `lmc_fits`
- `dossiers`

Use these for workflow orchestration:
- `crm_opportunities`
- `mandates`
- `mandate_files`
- `research`
- `strategies`
- `research_results`
- `research_constraints`

## Allowed task modes
- documentation updates
- implementation guide generation
- architecture review
- repo governance updates

Unless explicitly instructed otherwise, do not treat this repository as the production application repo.

## Output requirements
For meaningful work, return:
1. files changed or recommended to change
2. what changed
3. blockers
4. risks
5. any schema or architecture mismatch discovered

## Final instruction
Prefer explicit structure, narrower changes, and the correct owning layer over fast patches.

# AGENTS.md

Scope: entire repository unless a deeper `AGENTS.md` overrides part of it.

This file defines how AI coding agents must operate in this repository.

---

# 1. Repository identity

This repository is the **canonical documentation repository** for the Musahama platform.

It is the source of truth for:

- auth and onboarding behavior
- authorization rules
- database source-of-truth rules
- feature-system rules
- service boundaries
- frontend structure
- workflow model
- developer and AI-agent operating rules

Unless the task explicitly says otherwise, assume this repo is **documentation-first**, not the production application repo.

Do not treat this repository like a free-form coding sandbox.

---

# 2. Primary objective

Your job is to preserve architectural integrity.

That means:

- read the docs before making changes
- follow the documented boundaries
- do not invent new architecture casually
- do not “fix” symptoms in the wrong layer
- do not create drift between docs and implementation guidance

---

# 3. Mandatory read order

Before making any meaningful change, read in this exact order:

1. `docs/auth/`
2. `docs/authorization/`
3. `docs/database/`
4. `docs/feature-system/`
5. `docs/services/`
6. `docs/frontend/`
7. `docs/workflows/`
8. `docs/dev-guides/`

Minimum required understanding before proceeding:

- organization-first tenancy model
- canonical module list
- role model
- feature-system ownership
- service boundary rules
- canonical source-of-truth tables
- workflow chain from CRM to results
- implementation order and definition of done

If you do not understand those, do not improvise.

---

# 4. Canonical vocabulary

Use these terms precisely.

## Modules
Top-level navigation and route areas:

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

## Features
Capabilities inside modules, for example:

- research.start
- research.generate_strategies
- results.export.dossier
- results.shortlist
- contacts.enrich_person
- crm.sync.import

## Providers
External dependencies only, for example:

- OpenAI
- Lusha
- CRM connector
- search provider

## Entitlements
Runtime truth about what an organization is allowed to use.

Do not blur these concepts.

---

# 5. Hard architectural rules

You must obey all of these.

1. modules are not features
2. providers are not product structure
3. shortlist is not a top-level module
4. dossier is not a top-level module
5. discovery is not a top-level module
6. `feature-system/` owns runtime capability truth
7. `services/` own reads, writes, and DTO shaping
8. `features/` own domain UI
9. `views/` own reusable view patterns
10. pages/routes stay thin
11. RLS is the final security boundary
12. final UI must prefer canonical entity and analysis tables
13. legacy JSON blobs in `research_results` are not the final source of truth

---

# 6. Source-of-truth rules

Use these as final source of truth for final entity UI:

- `companies`
- `company_domains`
- `contacts`
- `contact_emails`
- `contact_phones`

Use these as final source of truth for final analysis UI:

- `evidence`
- `psych_profiles`
- `lmc_fits`
- `dossiers`

Use these for workflow orchestration and process state:

- `crm_opportunities`
- `mandates`
- `mandate_files`
- `research`
- `strategies`
- `research_results`
- `research_constraints`

Do not build final pages from workflow blobs if canonical or normalized tables exist.

---

# 7. Allowed task modes

## Mode A — Documentation update
Allowed:
- update docs
- fix wording
- add missing architecture rules
- add implementation guides
- add change requests
- add review notes

## Mode B — Planning / implementation guide generation
Allowed:
- create change requests
- create implementation guides
- define allowed files and forbidden files
- define acceptance criteria
- define review checkpoints

## Mode C — Architecture review
Allowed:
- compare implementation or proposed changes against docs
- report mismatches
- recommend the correct layer for the fix

## Mode D — Code implementation guidance
Allowed:
- produce instructions for a coding agent working in the application repo

Unless explicitly instructed, do **not** write production app code in this documentation repo.

---

# 8. Allowed file changes in this repo

You may modify files in:

- `README.md`
- `AGENTS.md`
- `docs/**`
- `change-requests/**`
- `implementation-guides/**`
- `reviews/**`
- `specs/**`
- `tasks/**`

If those folders do not exist yet, you may create them when the task requires them.

---

# 9. Forbidden actions in this repo

Do not:

- add random production application code here
- add database migrations here unless the task is explicitly to store migration docs/templates
- invent architecture not grounded in existing docs
- silently rename official module keys
- turn feature names into provider names
- delete canonical docs without replacing them
- create multiple conflicting versions of the same rule
- solve a structural problem with a vague note instead of a clear rule

---

# 10. Change discipline

For non-trivial work, create or update a change request first.

Recommended structure:

- problem
- expected behavior
- affected layer
- affected module/workflow
- constraints
- acceptance criteria
- status

Do not implement or recommend structural changes without a clear target.

---

# 11. Required reasoning rules for implementation planning

When asked to plan or review a change, determine all of these first:

- which layer owns the problem
- which docs define the correct behavior
- whether the issue is auth, authorization, service, feature-system, frontend, database, or workflow
- whether the current implementation is using the wrong source of truth
- which files are allowed to change
- which files must not change
- what tests or checks should exist
- what status/result should be reported back

Do not produce vague “fix it” instructions.

---

# 12. Output requirements

For any meaningful task, return:

1. files changed or recommended to change
2. what changed
3. blockers
4. risks
5. follow-up needed
6. any schema or architecture mismatch discovered

If generating an implementation guide, include:

- files to read first
- files allowed to change
- files forbidden to change
- architecture rules to respect
- acceptance criteria

---

# 13. Boundary enforcement rules

Use these boundary defaults.

## If deciding whether something is visible or enabled
That belongs in:
- `feature-system/`

## If fetching or mutating domain data
That belongs in:
- `services/`

## If rendering module-specific UI
That belongs in:
- `features/`

## If rendering reusable page/view patterns
That belongs in:
- `views/`

## If laying out routes and workspace shell
That belongs in:
- `app/`

## If enforcing row-level data protection
That belongs in:
- RLS and secure server-side logic

Do not move logic into the wrong layer for convenience.

---

# 14. Review checklist

Before finalizing any change, verify:

- current organization model is preserved
- canonical module list is unchanged unless intentionally approved
- no new fake top-level modules were introduced
- source-of-truth rules are preserved
- `feature-system/` remains the runtime capability source of truth
- `services/` remain the data access layer
- no UI-only access logic is being mistaken for security
- workflow chain still makes sense
- docs stay internally consistent

---

# 15. Common failure modes to avoid

Do not:

- hardcode sidebar tabs as the primary truth
- duplicate permission logic in buttons and pages
- build final result detail from `research_results` blobs
- place direct Supabase queries in page components
- confuse `results` the module with `research_results` the table
- treat `admin` as a platform operator by default
- treat `billing_admin` as a workflow operator by default
- create a fix that works visually but increases architectural debt

---

# 16. Documentation consistency rule

If you change any of these, update the related docs in the same task:

- auth flow
- role rules
- module list
- feature keys
- service contracts
- workflow sequence
- database assumptions
- source-of-truth rules
- folder boundaries
- implementation order

Do not leave architecture drift behind.

---

# 17. Definition of done

A task is done only when:

- the requested outcome is addressed
- the correct layer owns the solution
- the docs stay consistent
- the vocabulary stays consistent
- the workflow chain stays consistent
- no structural debt was introduced

A fast patch that violates the architecture is not done.

---

# 18. Final instruction

This repository exists to reduce drift and force disciplined implementation.

When in doubt:
- prefer explicit structure
- prefer documented rules
- prefer narrower changes
- prefer the correct layer over the fastest patch
