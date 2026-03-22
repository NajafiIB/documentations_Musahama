# Supabase Confirmation URL Setup (Current Deployment)

## Purpose
Ensure email confirmation links from Supabase point to the currently deployed Musahama URL.

## Current target URL
Use this deployment base URL for production:

`https://musahama-platform-998539683150.us-west1.run.app`

## Supabase dashboard updates
In Supabase project dashboard:

1. Go to **Authentication -> URL Configuration**.
2. Set **Site URL** to:
   - `https://musahama-platform-998539683150.us-west1.run.app`
3. Add **Additional Redirect URLs** (recommended):
   - `https://musahama-platform-998539683150.us-west1.run.app/**`
   - local/dev URLs you actually use (for example `http://localhost:3000/**`).

## Email template check
In **Authentication -> Email Templates**, make sure confirmation template behavior matches your app routing:

- If you rely on `redirectTo`, use `{{ .RedirectTo }}` in links.
- If you rely on project default site URL, links can use `{{ .SiteURL }}`.

Recommended confirmation link pattern:

`{{ .RedirectTo }}/auth/confirm?token_hash={{ .TokenHash }}&type=email`

## Application-side check
When signing up, pass `emailRedirectTo`/`redirectTo` to your deployed URL callback path, for example:

`https://musahama-platform-998539683150.us-west1.run.app/auth/confirm`

Important:
- The callback URL must be included in Supabase redirect URLs.
- Keep callback route stable across deployments.

## Quick verification
1. Create a new user signup.
2. Open email and inspect link host.
3. Confirm host is the current deployed domain above.
4. Click link and verify user lands in canonical flow (`/onboarding` or `/dashboard` after auth/bootstrap).
