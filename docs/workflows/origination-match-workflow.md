# Origination Match Workflow

## Purpose

`Origination Match` is the first fully realized solution module in the current platform.

It packages the existing origination flow inside the new workspace shell and module model.

## Current Route Surface

Module home:

- `/origination-match`

Compatibility routes still in active use:

- `/mandates`
- `/research`
- `/results`

## Current Workflow Shape

1. define a mandate or targeting scope
2. run research against that scope
3. generate strategies, candidate companies, and result-level contact suggestions
4. review results, one-pagers, and linked evidence
5. promote durable outputs into shared entities where appropriate

## Current Data Shape

Operational depth still comes from the legacy workflow tables:

- `mandates`
- `research`
- `strategies`
- `research_results`
- `research_result_contacts`
- `research_run_logs`

Shared runtime bridging now also exists through:

- `module_cases`
- `module_runs`
- bridge fields on `research` and `research_run_logs`

## Developer Rule

When changing origination behavior:

- keep current routes working unless intentionally removed
- treat `Origination Match` as the owning solution module
- prefer new shared runtime concepts for new cross-module behavior
- do not rebuild new product areas as additional first-class legacy workflow modules
