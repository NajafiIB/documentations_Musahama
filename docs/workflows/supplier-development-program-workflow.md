# Supplier Development Program Workflow

## Purpose

`Supplier Development Program` is the canonical solution module for spend-led supplier prioritization, local-content improvement, and report handoff into strategy follow-up.

It uses the shared module runtime plus SDP-specific domain tables. It is not a placeholder route.

## Canonical Routes

- `/supplier-development-program`
- `/supplier-development-program/cases`
- `/supplier-development-program/cases/new`
- `/supplier-development-program/cases/[caseId]`
- `/supplier-development-program/cases/[caseId]/preview`
- `/supplier-development-program/catalog`
- `/supplier-development-program/settings`
- `/supplier-development-program/owner`
- `/supplier-development-program/owner/participants/[organizationId]`

Direct access to protected SDP routes must redirect logged-out users to login with a return path.

## Runtime Model

The shared runtime plane stores:

- `module_cases`
- `module_runs`
- `module_artifacts`
- `module_action_requests`

The SDP domain model stores:

- `sdp_cases`
- `sdp_program_profiles`
- `sdp_upload_batches`
- `sdp_raw_cost_lines`
- `sdp_batch_supplier_mappings`
- `sdp_classification_suggestions`
- `sdp_supplier_profiles`
- `sdp_supplier_master`
- `sdp_spend_categories`
- `sdp_spend_subcategories`
- `sdp_approved_spend_facts`
- `sdp_score_options`
- `sdp_category_assessments`
- `sdp_supplier_assessments`
- `sdp_category_priority_results`
- `sdp_supplier_shortlist_results`
- `sdp_supplier_priority_results`
- `sdp_category_major_cost_types`
- `sdp_supplier_resolution_memory`
- `sdp_cost_classification_memory`
- `company_lc_score_history`
- `sdp_sector_lc_benchmarks`

## Case Workflow

### 1. Create Case

A case belongs to one organization and one active SDP program profile. Duplicate reporting periods are prechecked before creation.

### 2. Upload Costs

Users can upload CSV or paste data. Header detection must tolerate common copy-paste artifacts such as trailing semicolons, blank lines, and whitespace.

Cost upload mapping is saved before ingestion. Workbench table pages use a fluid layout so long cost, category, and subcategory fields are readable.

### 3. Map Suppliers

Supplier mapping resolves uploaded supplier names to canonical company records.

Rules:

- supplier company identity should dedupe within an organization
- shared company records should dedupe across reusable supplier defaults
- same-country or jurisdiction-aware candidates rank higher when available
- users can create or select the linked company during review

### 4. Map Costs

Cost mapping assigns approved cost facts to the selected category and subcategory.

Category and subcategory dropdowns use the active program/category setup for the current workspace.

### 5. Autopilot Review

AI autopilot can suggest classifications and supplier resolutions, but approved facts are still the source for downstream calculations.

Memory tables retain prior supplier and cost classification decisions.

### 6. Category and Supplier Inputs

Users review category priority inputs, supplier shortlist decisions, supplier assessments, LC values, and sector benchmarks.

Supplier defaults are editable after creation. Users can edit jurisdiction, sector, primary category, LC score, national status, and sector average LC without recreating the supplier profile.

### 7. Run and Report

The report calculation must use all relevant approved spend facts for the case, not only the first category or first uploaded batch.

Report snapshots are generated from the case's relevant approved facts and persisted in runtime artifacts. The report stage displays totals, supplier counts, rankings, and chart colors from the current design tokens including the secondary burnt-yellow chart color.

### 8. Strategy Handoff

Finalized SDP reports can open in Musahama Strategy Management. The handoff creates or reuses a strategy workspace linked to the report snapshot.

## Supplier Defaults

Supplier defaults are reusable supplier profiles attached to companies. They can be bulk uploaded, enriched, edited line-by-line, and deleted for future reuse.

Supplier defaults may include:

- company
- jurisdiction
- sector
- primary category
- LC score
- national status
- sector average LC

Supplier defaults share the company identity model with the Companies module.

## Enrichment

SDP supplier defaults support:

- fast enrichment
- deep enrichment

Fast enrichment fills blank linked-company website and supplier taxonomy fields using grounded AI with strict allowed sector/category vocabularies.

Deep enrichment requires Lusha and Unipile, updates the linked company first, then runs taxonomy-safe supplier classification if needed.

See `docs/services/enrichment-architecture.md`.

## Configuration Model

Program profiles configure:

- shortlist thresholds
- shortlist exclusions
- AI confidence thresholds
- banding thresholds
- score option dictionaries
- spend categories and subcategories
- sector and LC references

Core formulas stay in SQL or application logic, not in user-editable formula strings.

## Implementation References

Primary implementation files:

- `src/services/sdp/workflow.ts`
- `src/services/sdp/upload-ingestion.ts`
- `src/services/sdp/save-sdp-upload-mapping.ts`
- `src/services/sdp/review-sdp-classifications.ts`
- `src/services/sdp/run-sdp-case.ts`
- `src/services/sdp/report-snapshot.ts`
- `src/services/sdp/batch-scope.ts`
- `src/services/sdp/manage-sdp-supplier-profiles.ts`
- `src/services/sdp/update-sdp-supplier-profile.ts`
- `src/services/sdp/supplier-profile-enrichment.ts`
- `src/services/sdp/autopilot.ts`
