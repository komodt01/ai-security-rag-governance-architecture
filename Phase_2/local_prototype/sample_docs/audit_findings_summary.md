# Mock Audit Findings Summary

## Purpose

This mock document provides a synthetic audit findings summary for the local AI security prototype.

This document is not based on a real audit and contains no real organization, customer, or regulated data.

## Classification

Restricted

## Approved Roles

This document may be accessed by:

- Compliance Analyst
- Security Reviewer

## Human Review

Human review is required when this document is used to generate AI assistant responses.

## Mock Findings

## Finding 1: Incomplete Access Review Evidence

Some mock access review records did not include evidence of reviewer approval.

### Risk

Without approval evidence, the organization may not be able to prove that access was reviewed by an accountable owner.

### Recommended Control

Access reviews should include:

- Reviewer identity
- Review date
- Access decision
- Business justification
- Evidence retention
- Escalation for unresolved access

## Finding 2: Missing Data Classification Labels

Some mock documents did not include classification labels.

### Risk

Unclassified documents may be retrieved or exposed incorrectly by AI-enabled search or retrieval systems.

### Recommended Control

Documents should include:

- Classification
- Owner
- Status
- Review date
- Approved roles
- Approved groups

Documents missing required metadata should be denied by default.

## Finding 3: Logging Gaps for High-Risk Requests

Some mock high-risk requests did not include complete correlation IDs.

### Risk

Without correlation IDs, it may be difficult to reconstruct prompt, retrieval, response, and review activity.

### Recommended Control

AI assistant logs should include:

- Prompt ID
- Response ID
- User ID
- Retrieved document IDs
- Policy decision
- Risk score
- Correlation ID

## Finding 4: Human Review Trigger Not Consistently Applied

Some mock restricted-content responses were not flagged for human review.

### Risk

Restricted or compliance-impacting responses may be treated as final without accountable review.

### Recommended Control

Human review should be required for:

- Restricted documents
- Audit findings
- Compliance interpretation
- Security exceptions
- Access approval questions
- Unsupported AI responses

## Security Note

This document is restricted in the prototype to test role-based retrieval and human review logic.

It should not be accessible to general employees, engineers, IAM analysts, or AI system administrators by default.
