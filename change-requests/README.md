# Change Requests

This folder stores the canonical definition of a bug, structural fix, or requested change.

## Purpose
Use a change request to define:
- what is wrong
- what should happen instead
- which layer owns the real fix
- what must not change
- how success will be judged

## Naming
Use `CR-YYYY-NNN.md`.

## Required lifecycle
- draft
- pending-review
- approved
- in-progress
- blocked
- done
- rejected

## Final rule
A change request defines the target before coding starts.

Every non-trivial change request should then be attached to a machine-readable case manifest in `cases/`.
