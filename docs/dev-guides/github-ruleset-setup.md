# GitHub Ruleset Setup

Owner: Platform Architect  
Last Updated: 2026-03-19  
Version: 1.0  
Status: Approved

## Purpose
Define the required GitHub protection settings for the Musahama documentation repository.

## Use a branch ruleset on `main`
Create one branch ruleset named `Protect main` targeting the default branch `main` with enforcement set to Active.

## Enable these rules now
- require a pull request before merging
- require conversation resolution before merging
- require status checks to pass before merging
- require linear history
- block force pushes
- restrict deletions

## Required status checks
- Repo validation
- Policy guard

## Review settings for solo-maintainer phase
If there is only one human maintainer:
- do not require approving reviews yet
- do not require code owner review yet

## Review settings for team phase
When there is at least one second human reviewer:
- require 1 approval
- require code owner review
- dismiss stale approvals

## Final rule
No direct patching into `main`. Use PRs, required checks, and repo governance.