# Dashboard Recent Work

## Purpose

The dashboard includes a dynamic `Resume work` section that lets users reopen recent operational surfaces.

This section is not a static empty state. It is driven by user activity recorded from module surfaces.

## Source of Truth

Recent work is stored in:

- `workspace_recent_surfaces`

The table records the organization, user, surface type, target identifiers, title, subtitle, href, and last interaction timestamp.

## Logging Rule

Opening or working inside supported module surfaces records a recent surface.

Examples:

- mandate workspace
- research workspace
- result review
- SDP case
- company or supplier operational detail

The dashboard must only read recent work from the database. It must not infer recent work from local browser state.

## Dashboard Rendering

When records exist, the dashboard shows:

- accurate count
- title
- subtitle/context
- last activity indicator
- resume action

When no records exist, the dashboard shows the empty state.

## Implementation References

Primary implementation files:

- `src/services/activity/recent-surfaces.ts`
- `src/components/activity/recent-surface-visit-tracker.tsx`
- `app/(workspace)/dashboard/page.tsx`

Database setup:

- `supabase/migrations/20260414113000_add_workspace_recent_surfaces.sql`

