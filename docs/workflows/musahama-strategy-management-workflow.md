# Musahama Strategy Management Workflow

## Purpose

Musahama Strategy Management is a solution module for strategy follow-up after a finalized Supplier Development Program report.

It is separate from SDP. SDP produces the report snapshot; Strategy Management owns strategy generation, accepted strategy plans, KPI follow-up, and owner monitoring.

## Canonical Routes

- `/musahama-strategy-management`
- `/musahama-strategy-management/owner`
- `/musahama-strategy-management/launch`
- `/musahama-strategy-management/plan/[planId]`

## Handoff From SDP

The handoff starts from a finalized SDP report snapshot.

The launch route creates or reuses a Strategy Management workspace linked to the SDP report. The handoff must preserve source report identity and should not re-run SDP calculations.

## Runtime Model

Core tables:

- `msm_workspaces`
- `msm_source_reports`
- `msm_kpi_catalog`
- `msm_strategy_runs`
- `msm_strategy_scenarios`
- `msm_strategy_scenario_kpis`
- `msm_strategy_plans`
- `msm_plan_kpis`
- `msm_kpi_measurements`
- `msm_progress_events`
- `msm_alerts`
- `msm_plan_mandates`

## Workflow

1. User finalizes an SDP report.
2. User opens the report in Strategy Management.
3. The module creates a workspace linked to the source report.
4. User generates strategy scenarios.
5. User accepts a scenario into an active plan.
6. User updates plan adjustments and KPI measurements.
7. Owner view monitors participant company progress.

## Credit Behavior

Strategy generation is a credit-charged operation. UI quotes must use the current credit operation key configured by the implementation.

## Implementation References

Primary implementation files:

- `src/services/msm/module.ts`
- `src/services/msm/workspace.ts`
- `src/services/msm/shared.ts`
- `app/(workspace)/musahama-strategy-management/page.tsx`
- `app/(workspace)/musahama-strategy-management/launch/page.tsx`
- `app/(workspace)/musahama-strategy-management/owner/page.tsx`
- `app/(workspace)/musahama-strategy-management/plan/[planId]/page.tsx`

Database setup:

- `supabase/migrations/20260410123000_add_musahama_strategy_management_module.sql`

