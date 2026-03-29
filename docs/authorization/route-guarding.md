# Route Guarding

## Current Protected Workspace Routes

Primary workspace routes:

- `/dashboard`
- `/approvals`
- `/activity`
- `/origination-match`
- `/partner-match`
- `/negotiator`
- `/compliance-guardian`
- `/funding-orchestrator`
- `/companies`
- `/contacts`
- `/integrations`
- `/data-packs`
- `/billing`
- `/settings`

Compatibility routes that still exist:

- `/mandates`
- `/research`
- `/results`

## Guarding Rule

A route is protected when it requires:

- session resolution
- current organization resolution
- active membership
- module availability where applicable

## Active-Navigation Rule

Compatibility routes should still resolve to the correct active module in the shell.

Most importantly:

- `/mandates`
- `/research`
- `/results`

should activate:

- `Origination Match`
