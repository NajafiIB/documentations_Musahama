# Auth Routes

---

## Public Routes

/login  
/register  
/forgot-password  
/invite/[token]

---

## Protected Routes

/workspace/*

---

## Routing Rules

IF no session → /login  
IF session AND no org → /onboarding  
IF session AND org → /dashboard  


## Deployment Note
For Supabase email confirmation URL configuration and redirect behavior, see `docs/auth/supabase-confirmation-url-setup.md`.
