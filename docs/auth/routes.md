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
