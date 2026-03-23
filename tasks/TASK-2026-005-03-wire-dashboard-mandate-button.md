# TASK-2026-005-03

Title: Wire dashboard mandate button to implemented mandates flow  
Status: queued  
Parent Change Request: CR-2026-005  
Parent Implementation Guide: IMP-2026-005  
Owner: Platform Architect  
Assigned To: AI Studio  
Target Repo: NajafiIB/Implementation_Musahama  
Target Branch: feature/missing-pages-404-closure  
Layer: frontend | workflow  
Module: mandates  
Last Updated: 2026-03-23

## Objective
Ensure the dashboard mandate CTA navigates to a valid mandates route and never 404s.

## Acceptance Criteria
1. Dashboard mandate button target route exists.
2. Route loads for authorized users without 404.
3. Unauthorized/disabled state uses proper runtime gating reason.
4. Route-check evidence included.
