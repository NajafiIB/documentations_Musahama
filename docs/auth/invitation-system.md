# Organization Invitation System

Status: Required for production

---

## Purpose

Allow controlled joining of users into organizations.

---

## Rules

1. Only admins/owners can invite
2. Invitations are email-based
3. Invitations expire
4. Each invite has a unique token
5. Membership is created ONLY after acceptance

---

## Flow

1. Admin creates invite
2. Record stored in `organization_invitations`
3. Email sent with token link
4. User clicks link
5. System validates token
6. User authenticates (if needed)
7. Membership created
8. Invitation marked accepted

---

## SQL Requirements

Unique constraint:
- (organization_id, email, status='pending')

Indexes:
- email
- token

---

## Security

- Token must be random and unguessable
- Expiration must be enforced
- Invitation must not auto-assign admin role unless explicit

---

## API

POST /invitations/create  
POST /invitations/accept  
POST /invitations/revoke  
