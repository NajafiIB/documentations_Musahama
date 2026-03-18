# Authentication Security

---

## Rules

1. Never trust frontend
2. Always validate with Supabase
3. Use RLS for data protection
4. Never expose service role key
5. Validate organization membership on every request

---

## RLS Enforcement

Tables must enforce:

- organization_members
- organizations
- organization_modules

---

## Critical Check

auth.uid() must match user_id
