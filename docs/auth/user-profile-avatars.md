# User Profile Avatars

## Purpose

Users can personalize their profile avatar without changing workspace membership or organization data.

Avatar state is personal to the authenticated user and applies across all workspaces.

## Supported Sources

Rendering precedence is:

1. uploaded photo
2. preset avatar
3. initials monogram

The avatar appears in:

- account settings profile tab
- top-right header user menu trigger

## Metadata Model

Avatar state is stored in Supabase auth user metadata only.

Canonical metadata keys:

```json
{
  "avatar_source": "initials | preset | upload",
  "avatar_preset_key": "string | null",
  "avatar_url": "string | null"
}
```

No `profiles` table column is required for avatar state.

Malformed or missing avatar metadata must fall back to initials.

## Upload Storage

Uploaded photos are stored in the public Supabase storage bucket:

- `user_avatars`

Object path format:

```text
{user.id}/{timestamp}-{random}.png
```

Uploaded output is normalized client-side to a square `512x512` PNG.

Accepted source formats:

- JPG
- PNG

Maximum file size:

- 5 MB

When replacing or removing an uploaded avatar, the old object is deleted best-effort only when it belongs to the same user path.

## UI Flow

The account profile section shows a `96px` circular avatar preview and an always-visible `Update picture` action.

On hover-capable devices the avatar shows a dark overlay with a camera affordance.

Editing opens a centered modal with:

- upload and crop section
- 12 built-in abstract preset avatars
- use initials action
- cancel and save picture footer

The save action is disabled until a pending change exists.

## Implementation References

Primary implementation files:

- `src/services/auth/user-avatar.ts`
- `src/components/avatar/user-avatar.tsx`
- `src/components/avatar/user-avatar-presets.tsx`
- `src/components/avatar/avatar-edit-modal.tsx`
- `src/components/avatar/account-avatar-section.tsx`
- `src/components/shell/header-user-menu.tsx`

Storage setup:

- `supabase/migrations/20260414203000_add_user_avatar_bucket.sql`

