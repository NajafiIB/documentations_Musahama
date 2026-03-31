# Supplier Development Program Workflow

## Purpose

`Supplier Development Program` is the canonical full solution module for spend-led supplier prioritization.

It is not a thin placeholder page. It uses the shared module runtime plus SDP-specific domain tables.

## Canonical Route Flow

1. `/supplier-development-program`
2. `/supplier-development-program/cases`
3. `/supplier-development-program/cases/[caseId]`
4. `/supplier-development-program/catalog`

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
- `sdp_classification_suggestions`
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

## Case Workflow

### Costs

- upload batches
- raw line counts
- validation status

### Classification

- AI suggestions per spend line
- approval or correction before facts enter scoring

### Categories

- category totals
- expected future spend
- criticality assessments
- priority category results

### Suppliers

- shortlist decisions
- supplier assessments
- final supplier ranking

### Report

- final core supplier
- report snapshots in `module_artifacts`
- approval-gated exports in `module_action_requests`

## Configuration Model

Saudi PIF SDP is seeded as the first `sdp_program_profile`.

Profiles configure:

- shortlist thresholds
- shortlist exclusions
- AI confidence thresholds
- banding thresholds
- score option dictionaries

Core formulas stay in SQL or application logic, not in user-editable formula strings.
