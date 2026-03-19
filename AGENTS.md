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