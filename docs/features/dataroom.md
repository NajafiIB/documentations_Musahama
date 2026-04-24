# Dataroom

## Summary
Dataroom is a new Musahama solution for securely organizing, sharing, and tracking sensitive documents for investors, partners, advisors, and other external reviewers.

This v1 specification is intentionally lean. It takes the strongest reusable patterns from Papermark-style datarooms—share links, folder hierarchy, invitations, analytics, and audit-style activity—without importing heavier features like granular groups, Q&A, file requests, webhooks, watermarking, screenshot protection, or custom domains in the first phase.

## 1. Feature Name
- **Name:** Dataroom
- **Module:** `dataroom`
- **Type:** New solution
- **Priority:** High
- **Requested by:** Product / Founder
- **Date:** 2026-04-24

## 2. Goal
- **What should be built:** A Musahama-native investor and partner dataroom solution for securely organizing, sharing, and tracking sensitive documents.
- **Why it is needed:** Musahama needs a controlled external-sharing workflow for fundraising, due diligence, partner review, and advisor access.
- **What problem it solves:** Document sharing is otherwise fragmented, weakly tracked, and not standardized. A dataroom gives one controlled place for files, access, and analytics.
- **Who will use it:** Internal workspace teams, founders, investor-relations users, advisors, and invited external viewers.

## 3. Entry Point
- **Route / URL:** `/dataroom`, `/dataroom/:roomId`
- **Where user comes from:** Solutions navigation, company/funding workflow, deal context, admin/workspace tools
- **Where user goes after finishing:** Dataroom detail view, then Analytics or Access tab
- **Is this:** New solution with list page, detail workspace, and external viewer flow

## 4. Scope

### V1 included
- Create dataroom
- Folder and subfolder hierarchy
- Upload documents
- Version documents
- Create secure share links
- Invite viewers by email
- Room-level access rules
- External viewer access gate
- Basic analytics: visits, unique viewers, time spent, document views, downloads
- Audit and event logging
- Archive room and revoke access

### Later, not in first implementation
- Group-based granular file and folder permissions
- Dynamic watermarking
- NDA signing
- Screenshot protection
- Q&A conversations
- File requests
- Webhooks
- Custom domains
- Full resumable bulk-upload pipeline
- Advanced per-page analytics UI

## 5. Views Needed

### View A — Dataroom List
- **Purpose:** Show all datarooms in the workspace
- **Visible to:** Internal authorized users
- **Main components:** Search, filters, status badges, owner, last updated, active links, total visits
- **Actions available:** Create room, open room, archive room, duplicate room

### View B — Create / Edit Dataroom
- **Purpose:** Create room metadata and default settings
- **Visible to:** Workspace owner, admin, solution manager
- **Main components:** Name, description, related company/deal, default visibility, link defaults
- **Actions available:** Save draft, create room, update settings

### View C — Dataroom Overview
- **Purpose:** Operational summary for one room
- **Visible to:** Internal authorized users
- **Main components:** Header, key metrics, recent activity, latest uploads, active links, invite status
- **Actions available:** Upload files, share room, open analytics, open settings

### View D — Contents
- **Purpose:** Manage room structure and assets
- **Visible to:** Internal editors and contributors
- **Main components:** Folder tree, file list, upload area, preview pane, version panel
- **Actions available:** Create folder, upload, rename, move, publish or hide asset, replace version, archive asset

### View E — Access
- **Purpose:** Manage sharing
- **Visible to:** Internal managers and admins
- **Main components:** Links tab, invitations tab
- **Actions available:** Create link, revoke link, expire link, invite viewers, resend invite

### View F — Analytics
- **Purpose:** Measure engagement
- **Visible to:** Internal managers, admins, read-only analytics users
- **Main components:** Visits, viewers, time spent, document views, downloads, latest activity
- **Actions available:** Filter by date, link, document; export CSV later

### View G — Settings
- **Purpose:** Room configuration
- **Visible to:** Admin and solution manager
- **Main components:** Room metadata, default access rules, archive controls
- **Actions available:** Update settings, archive room

### View H — External Viewer
- **Purpose:** Investor and partner-facing dataroom
- **Visible to:** Valid invited or link-authorized external users
- **Main components:** Access gate, room header, folder navigation, file viewer, download button if allowed
- **Actions available:** Open folder, view file, download allowed file

## 6. Data Model

### Entity: dataroom
- **Is it new or existing:** New
- **Main purpose:** Top-level solution record
- **Primary key:** `id`
- **Required fields:** `workspace_id`, `name`, `status`, `owner_user_id`
- **Optional fields:** `description`, `related_company_id`, `related_deal_id`, `archived_at`
- **Status field values:** `draft`, `active`, `archived`
- **Relations:** Has many folders, assets, links, invitations, sessions, events

### Entity: dataroom_folder
- **Is it new or existing:** New
- **Main purpose:** Folder hierarchy
- **Primary key:** `id`
- **Required fields:** `dataroom_id`, `name`
- **Optional fields:** `parent_folder_id`, `sort_order`
- **Relations:** Belongs to dataroom; has many child folders and assets

### Entity: dataroom_asset
- **Is it new or existing:** New
- **Main purpose:** Logical document or file record
- **Primary key:** `id`
- **Required fields:** `dataroom_id`, `folder_id`, `name`, `file_type`, `visibility_status`
- **Optional fields:** `current_version_id`, `description`
- **Status field values:** `hidden`, `published`, `archived`
- **Relations:** Belongs to folder; has many versions

### Entity: dataroom_asset_version
- **Is it new or existing:** New
- **Main purpose:** Versioned file metadata
- **Primary key:** `id`
- **Required fields:** `asset_id`, `storage_key`, `version_no`, `processing_status`, `uploaded_by`
- **Optional fields:** `preview_key`, `size_bytes`, `mime_type`, `checksum`
- **Status field values:** `uploading`, `processing`, `ready`, `failed`, `archived`
- **Relations:** Belongs to asset

### Entity: dataroom_link
- **Is it new or existing:** New
- **Main purpose:** Shareable access link
- **Primary key:** `id`
- **Required fields:** `dataroom_id`, `token`, `status`
- **Optional fields:** `expires_at`, `require_email`, `require_password`, `allow_download`
- **Status field values:** `draft`, `active`, `expired`, `revoked`
- **Relations:** Belongs to dataroom

### Entity: dataroom_invitation
- **Is it new or existing:** New
- **Main purpose:** Email invitation tracking
- **Primary key:** `id`
- **Required fields:** `dataroom_id`, `email`, `invited_by`, `status`
- **Optional fields:** `link_id`, `sent_at`, `viewed_at`
- **Status field values:** `pending`, `sent`, `viewed`, `expired`, `revoked`
- **Relations:** Belongs to room and optionally link

### Entity: dataroom_viewer
- **Is it new or existing:** New
- **Main purpose:** External identity snapshot
- **Primary key:** `id`
- **Required fields:** `normalized_email`
- **Optional fields:** `first_name`, `last_name`, `verification_status`
- **Relations:** Has many sessions

### Entity: dataroom_visit_session
- **Is it new or existing:** New
- **Main purpose:** One access session
- **Primary key:** `id`
- **Required fields:** `dataroom_id`, `link_id`, `started_at`, `access_result`
- **Optional fields:** `viewer_id`, `ended_at`
- **Relations:** Has many events

### Entity: dataroom_event
- **Is it new or existing:** New
- **Main purpose:** Append-only audit and analytics event record
- **Primary key:** `id`
- **Required fields:** `dataroom_id`, `event_type`, `occurred_at`
- **Optional fields:** `asset_id`, `session_id`, `metadata_json`
- **Relations:** Belongs to room, session, and optionally asset

### Entity: dataroom_download
- **Is it new or existing:** New
- **Main purpose:** Download log
- **Primary key:** `id`
- **Required fields:** `dataroom_id`, `asset_id`, `session_id`, `occurred_at`
- **Relations:** Belongs to session and asset

## 7. Main Actions
- Create dataroom
- Edit dataroom metadata
- Create folder
- Upload asset
- Replace asset version
- Publish asset
- Hide asset
- Create share link
- Revoke link
- Invite viewer
- Resend invite
- View analytics
- Archive room

## 8. Permissions

### Internal roles
- **Workspace Owner / Admin:** Full view, create, edit, archive rights; can manage access rules, invitations, analytics, room settings
- **Solution Manager:** Full room operations except workspace-level admin settings
- **Contributor:** Can upload, replace versions, move files, edit content metadata; cannot change room security policy or create/revoke external links unless explicitly granted
- **Internal Viewer:** Can view room and analytics if allowed; no edit or share actions

### External role
- **Invited Viewer / Authorized Link Viewer:** Can access only through valid link, can view only published assets, can download only if link permits

### Blocked conditions
- Link expired
- Link revoked
- Room archived
- Asset not published
- Viewer fails access gate
- Viewer not on allow-list when allow-list is enabled

## 9. Automations
- **Room bootstrap:** On room creation, create root folder, default settings, first audit event
- **Asset processing:** On upload completion, create version row, detect metadata, start preview or processing job, mark `processing`
- **Publish current version:** On publish or replace, update current version pointer and append audit event
- **Link issuance:** On link creation, generate token, persist rules, activate link, append audit event
- **Invitation dispatch:** On invitation create or resend, send email, mark `sent`, append event
- **Access gate enforcement:** On external open, evaluate link status, expiry, email, password, verification, allow/block rules; create session or deny
- **Analytics tracking:** On room open, file open, page event, or download, append event rows and update aggregates
- **Archive room:** On archive, revoke active links, block new external sessions, preserve historical analytics and audit

## 10. Business Rules
- External users never access storage directly; they access through a Musahama-controlled link and session layer.
- Only `published` assets with `ready` current versions are visible externally.
- Room archive is soft-archive, not hard delete.
- Analytics and audit events are append-only.
- Replacing a document version does not break the logical asset reference.
- Internal previews do not count as external analytics.
- Invitation status changes are system-derived, not manually editable.
- Default v1 sharing is room-wide; selective file and folder access is deferred.

## 11. Calculations / Derived Logic
- **Unique viewers:** Distinct verified email or session identity per date range
- **Total visits:** Count of successful sessions
- **Total time spent:** Sum of session durations with cap rules to avoid runaway tabs
- **Top documents:** Highest views, then highest total time
- **Download count:** Count of download events
- **Last viewed:** Latest event timestamp per room, asset, or link

## 12. States To Handle
- **No data yet:** Empty room with CTA to upload first documents
- **Draft:** Room exists but has no active share links
- **Active:** Room has publishable contents and can be shared
- **Processing:** Asset version still being prepared
- **Failed processing:** Asset version failed; internal retry needed
- **Archived:** No new external access
- **Missing dependency:** Storage, email, or preview backend unavailable
- **Revoked access:** Link or invite invalidated

## 13. Acceptance Criteria
- User can create a dataroom, add folders, upload files, publish assets, and create a share link.
- User can invite a viewer by email and see invitation state.
- External viewer can access the room through a valid link and see only published assets.
- External viewer is blocked when link is expired, revoked, or gate requirements fail.
- System records visits, document opens, and downloads in analytics and audit records.
- Replacing a document version preserves the logical asset record.
- Archiving a room disables new external access without deleting historical data.
- Internal users can see room-level analytics: visits, unique viewers, time spent, document views, and downloads.
- Processing failures are visible and do not silently expose broken assets.

## 14. Delivery

### Implement now
- Schema
- Backend services
- UI for list, detail, contents, access, analytics, settings
- External viewer flow
- Docs page / wiki entry
- Core tests

### Leave for later
- Groups and granular file/folder permissions
- Watermarking
- NDA requirement
- Screenshot protection
- Q&A
- File requests
- Webhooks
- Custom domains
- Advanced analytics breakdowns
