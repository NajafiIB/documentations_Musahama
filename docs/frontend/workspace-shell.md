# Workspace Shell

## Purpose

The workspace shell is the permanent frame for the protected application.

Its job is to make the platform feel like one coherent product even though multiple modules share the same workspace.

## Current Shell Areas

The shell contains:

- sidebar navigation
- workspace header
- current-area context
- main content region

The shell should not change shape from module to module.

## Navigation Groups

The sidebar is grouped into:

- `Platform`
- `Solutions`
- `Shared Data`
- `Admin`

That grouping comes from the module registry and should not be duplicated with ad hoc page-level lists.

## Current-Area Clarity

The current sidebar implementation intentionally makes orientation clearer by:

- surfacing the active area near the top
- keeping the active nav group open
- highlighting the active module strongly
- collapsing non-active groups when appropriate

When a developer changes sidebar behavior, the first question should be:

- can a user immediately tell where they are?

## Legacy Route Highlighting

Legacy routes still map visually to the current module model.

Most importantly:

- `/mandates`
- `/research`
- `/results`

must still highlight:

- `Origination Match`

That mapping is implemented from the module registry rather than hardcoded page by page.
