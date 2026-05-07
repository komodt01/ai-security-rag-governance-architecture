# Mock Incident Response Playbook

## Purpose

This mock playbook defines high-level incident response concepts for the local AI security prototype.

This document is synthetic and is used only for the local prototype.

## Classification

Restricted

## Approved Roles

This document may be accessed by:

- Security Architect
- Security Reviewer

## Human Review

Human review is required when this document is used to generate AI assistant responses.

## Incident Response Objectives

Incident response should:

- Detect suspicious activity
- Confirm whether an incident has occurred
- Contain the impact
- Preserve evidence
- Investigate root cause
- Remove the cause
- Recover safely
- Document lessons learned
- Improve controls

## AI-Related Incident Types

AI-related incidents may include:

- Prompt injection abuse
- System prompt extraction attempts
- Sensitive data entered into prompts
- Restricted data returned in responses
- Unauthorized document retrieval
- Poisoned documents
- Unsafe AI-generated recommendations
- Human review bypass
- Logging failure
- Excessive usage or cost spike

## Initial Triage Questions

Responders should ask:

- Who submitted the prompt?
- What was requested?
- What documents were retrieved?
- Was unauthorized content exposed?
- Was sensitive data included?
- Was the response blocked or returned?
- Was human review required?
- Was human review completed?
- Are logs complete?
- Is the incident ongoing?

## Containment Examples

Possible containment actions include:

- Block the prompt pattern
- Disable the affected user account
- Disable the affected document collection
- Remove a poisoned document
- Rotate exposed credentials
- Disable model access
- Restore logging
- Disable auto-release of high-risk responses

## Evidence to Preserve

Preserve:

- User ID
- Prompt metadata
- Response metadata
- Retrieved document IDs
- Access decisions
- Human review records
- Administrative changes
- Security alerts
- Correlation IDs

## Security Note

The AI assistant should not independently make containment, eradication, legal, regulatory, or customer-impacting decisions.

High-risk incident response recommendations require human review.
