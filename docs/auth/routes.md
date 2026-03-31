# Auth Routes

---

## Public Routes

/login  
/signup  
/register  
/forgot-password  
/reset-password  
/invite/[token]
/auth/callback
/privacy
/terms
/support

---

## Protected Transitional Routes

/onboarding  
/select-organization  

---

## Protected Workspace Routes

/dashboard and canonical module routes under `app/(workspace)`

---

## Routing Rules

IF no session AND protected route → /login  
IF session AND public auth route → resolve post-login destination  
IF session AND no org → /onboarding  
IF session AND multiple org memberships to resolve → /select-organization  
IF session AND active org → /dashboard or intended protected destination  

## Alias Rules

`/register` redirects to `/signup`.

`/` bootstraps to `/dashboard`, and auth middleware then resolves the final destination.


## Deployment Note
For Supabase email confirmation URL configuration and redirect behavior, see `docs/auth/supabase-confirmation-url-setup.md`.
