# Current Workspace UI Rules

## Purpose

This page records current workspace UI behavior that is more specific than the general frontend foundation.

## Sidebar Layout

The workspace sidebar uses a strict three-zone layout:

1. top fixed zone
2. dynamic middle zone
3. bottom anchored zone

The whole sidebar is pinned to viewport height and does not scroll as one long list.

The middle zone is the only area that scrolls when contextual navigation is long.

Bottom links stay anchored:

- Companies
- Contacts
- Settings

Settings submenus and solution submenus populate the middle zone. They must not expand under the bottom links.

## Sidebar Tokenization

Sidebar colors, hover states, active states, indicator dots, scrollbars, and transitions must use global theme tokens.

Do not hardcode provider colors, blues, greys, fonts, or transition durations in sidebar components.

## Data-Heavy Workbenches

Data-table and workbench pages should use a fluid layout rather than a boxed max-width layout.

Rules:

- use full available width with standard side padding
- do not constrain tables to narrow card widths
- set sensible min-widths for long text columns
- right-align numeric and monetary columns
- allow horizontal table scroll only when viewport width is too small

## Read-Only Data vs Inputs

Read-only metrics and labels must not look like editable form fields.

Use label/value presentation, muted empty states, and subtle dividers. Reserve filled grey boxes for real form inputs.

## Favicons and Identity Badges

Company and integration identity badges should prefer website favicons through Google's public favicon endpoint when a website URL exists.

Fallback order:

1. website favicon
2. configured local logo or monogram
3. generic icon

Use plain image elements for arbitrary external favicon URLs to avoid framework remote-image configuration coupling.

## Implementation References

Primary implementation files:

- `src/components/shell/sidebar.tsx`
- `app/(workspace)/companies/company-identity-badge.tsx`
- `app/(workspace)/integrations/integration-provider-logo.tsx`
- `app/globals.css`

