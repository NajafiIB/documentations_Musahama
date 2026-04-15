# Automations and Support Intake

## Purpose

Musahama includes a workspace automation runtime and a support bug-report intake path.

Automations are orchestration lines. Integrations are provider connections. A provider connection alone does not imply an automation is running.

## Automation Runtime

Automation definitions contain:

- trigger
- conditions
- ordered steps
- enabled state
- organization scope

Automation runs record execution state and per-step outcomes.

Current automation tables:

- `automation_definitions`
- `automation_definition_conditions`
- `automation_definition_steps`
- `automation_trigger_events`
- `automation_runs`
- `automation_run_steps`
- `automation_in_app_notifications`

Automation operations should call shared service functions rather than duplicating business logic.

## Support Bug Intake

Workspace users can open a report issue flow from the shell. Submitted reports are stored and can dispatch into the documentation-driven delivery/intake process.

Current support table:

- `support_bug_reports`

The report launcher must not close immediately because of sidebar or overlay event propagation. It should behave like a stable workspace slideover/modal action.

## Implementation References

Primary implementation files:

- `src/services/automations/runtime.ts`
- `src/services/automations/operation-handlers.ts`
- `src/services/automations/definitions.ts`
- `app/api/cron/automations/route.ts`
- `src/services/support/bug-reports.ts`
- `src/components/shell/report-bug-launcher.tsx`
- `app/api/support/bug-reports/route.ts`

Database setup:

- `supabase/migrations/20260404163000_add_automation_runtime.sql`
- `supabase/migrations/20260404123000_add_support_bug_reports.sql`

