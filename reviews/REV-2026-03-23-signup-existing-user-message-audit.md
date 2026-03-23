# Review — Signup Existing-User Messaging Audit (2026-03-23)

## Scope
Check signup behavior when the email is already registered.

## Finding
Current signup flow redirects to login with "Check your email to confirm your account" on any non-error signup response. This can show a misleading confirmation message for already-registered users.

## Technical Note
Supabase `signUp` may return an obfuscated user-like response for existing confirmed users (instead of a hard error) depending on auth settings. Existing-user detection should handle this response shape before showing success messaging.

## Decision
Add a task to harden signup UX messaging so existing-user outcomes do not display "check your email" confirmation wording.
