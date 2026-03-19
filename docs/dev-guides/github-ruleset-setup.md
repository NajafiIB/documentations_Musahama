# GitHub Ruleset Setup

Owner: Platform Architect  
Last Updated: 2026-03-19  
Version: 1.0  
Status: Approved

## Purpose
Define the required GitHub protection settings for the Musahama documentation repository.

## Recommended ruleset
Create one branch ruleset on `main` with:
- pull request required
- conversation resolution required
- required status checks
- linear history
- force pushes blocked
- deletions restricted

## Required checks
- Repo validation
- Policy guard

## Review settings
Solo maintainer phase:
- do not require approvals yet
- do not require code owner review yet

Team phase:
- require 1 approval
- require code owner review
- dismiss stale approvals

## Final rule
Use PRs and required checks for changes to `main`.
