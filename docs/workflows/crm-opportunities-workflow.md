# CRM Opportunities Workflow

## Status

Legacy compatibility workflow.

## Current Role

The older CRM opportunities concept is retained only as legacy compatibility context for earlier CRM sync and opportunity intake behavior.

It is no longer one of the official primary top-level module areas in the current platform model, and it is not currently exposed as an active workspace route.

## Rule

New architecture should not be built around `crm_opportunities` as the product root.

If CRM-linked intake continues, document it as an input path into `Origination Match` or another future solution workflow, not as the platform's defining navigation model.
