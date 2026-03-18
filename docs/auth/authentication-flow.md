# Authentication & Organization Onboarding

Owner: Platform Architect  
Last Updated: 2026-03-18  
Version: 1.0  
Status: Approved  

---

## 1. Purpose

Define how users authenticate, how organization context is resolved, and how access to the platform is established.

This document is the **source of truth for all authentication-related behavior**.

---

## 2. Core Principles

1. Authentication is handled by Supabase Auth
2. The platform is **organization-first (multi-tenant)**
3. A user cannot access the workspace without:
   - valid session
   - active organization membership
4. Authorization is NOT handled in auth layer
5. Auth only establishes identity + organization context

---

## 3. Key Concepts

### User Identity
Managed by Supabase Auth

### Profile
Stored in:
- `profiles`

### Organization Membership
Stored in:
- `organization_members`

### Organization Context
The active organization for the session

---

## 4. Tables Involved

### profiles
- id (matches auth.users.id)
- email
- first_name
- last_name

### organizations
- id
- name
- status

### organization_members
- id
- organization_id
- user_id
- role
- status (active / invited / suspended)
- invited_by_user_id
- joined_at

### organization_invitations (REQUIRED)
- id
- organization_id
- email
- role
- token
- status (pending / accepted / expired)
- expires_at
- created_by

---

## 5. Authentication Methods

### 5.1 Email + Password
Handled via Supabase Auth

### 5.2 Google OAuth
Handled via Supabase Auth provider

IMPORTANT:
After OAuth login, onboarding flow must still run.

---

## 6. Authentication Flow

### Step 1: User logs in

- Email/password OR Google
- Supabase returns session

---

### Step 2: Profile resolution

System must ensure:
- profile exists in `profiles`
- if not → create profile

---

### Step 3: Organization resolution

Query:

SELECT * FROM organization_members
WHERE user_id = current_user
AND status = 'active'

---

### Step 4: Routing decision

CASE:

#### No membership
→ redirect to `/onboarding`

#### One membership
→ set current organization
→ go to `/dashboard`

#### Multiple memberships
→ show organization selector

---

## 7. Registration Flows

---

### 7.1 New Organization (Primary Flow)

#### Step 1
User signs up

#### Step 2
Create:
- profile

#### Step 3
Create organization

#### Step 4
Create membership:

role = 'owner'  
status = 'active'

#### Step 5
Enable default modules

#### Step 6
Redirect to dashboard

---

### 7.2 Join Existing Organization (Invitation Only)

Users must NOT self-join organizations.

#### Step 1
User receives invite link:

/invite/{token}

#### Step 2
Validate invitation:
- exists
- status = pending
- not expired

#### Step 3
If user not authenticated:
→ redirect to login/signup

#### Step 4
After auth:
- create membership
- set role from invitation
- mark invitation as accepted

#### Step 5
Redirect to dashboard

---

## 8. Password Recovery Flow

### Step 1
User enters email

### Step 2
Supabase sends reset email

### Step 3
User resets password

### Step 4
User logs in

### Step 5
Normal org resolution runs

---

## 9. Session Handling

- Use Supabase session
- Do NOT store session manually
- Always validate session on page load

---

## 10. Required Backend Checks

Every request must verify:

1. user is authenticated
2. user has active membership
3. organization is active

If any fails → deny access

---

## 11. Security Rules

1. No direct organization joining
2. Invitations required
3. Membership status must be checked
4. Never trust frontend role
5. Always enforce via RLS

---

## 12. Frontend Requirements

Auth pages:

- /login
- /register
- /forgot-password
- /invite/[token]

Workspace access must be blocked until:

- session exists
- org resolved

---

## 13. Failure Cases

| Case | Action |
|------|--------|
| No session | redirect to login |
| No profile | create profile |
| No org | redirect onboarding |
| Invalid invite | show error |
| Expired invite | show expired |
| Suspended membership | block access |

---

## 14. Integration with Feature System

Auth DOES NOT decide:
- modules
- features
- permissions

Auth only provides:
- user_id
- organization_id
- role

Feature system handles the rest.

---

## 15. Non-Negotiable Rules

- No workspace without organization
- No role logic in UI
- No direct DB writes from frontend
- No bypassing invitation system

---

## 16. References

- docs/03-authorization/role-model.md
- docs/05-feature-system/entitlement-resolution.md
- docs/04-database/schema.md
