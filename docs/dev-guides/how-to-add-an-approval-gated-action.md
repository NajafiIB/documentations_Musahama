# How to Add an Approval-Gated Action

## Goal

Use this guide when adding a new outbound or side-effectful action that should be reviewed before execution.

## Implementation Steps

1. Define the action inside the owning module or platform flow
2. Write the action request into `module_action_requests`
3. Record the final execution in `module_action_executions`
4. Ensure the `Approvals` inbox can render the new request shape
5. Update docs and specs if the runtime vocabulary changes

## Expected Runtime Model

Use:

- action request for pending review
- approval status transitions for decision state
- action execution for the actual outbound step

Do not skip directly to execution for an action that is supposed to be approval-gated.

## Docs and Specs Required

Update:

- `docs/platform-runtime/runtime-plane.md`
- `specs/platform/runtime-plane.yaml`

If the action changes module behavior materially, also update:

- `docs/feature-system/module-catalog.md`
- `specs/modules/module-catalog.yaml`
