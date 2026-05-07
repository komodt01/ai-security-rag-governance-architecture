# Mock Cloud Logging Standard

## Purpose

This mock standard defines logging and monitoring expectations for cloud workloads.

This document is synthetic and is used only for the local prototype.

## Classification

Confidential

## Approved Roles

This document may be accessed by:

- Engineer
- Security Architect
- Compliance Analyst
- Security Reviewer

## Logging Objectives

Cloud workloads should produce logs that support:

- Security monitoring
- Incident response
- Audit evidence
- Access review
- Configuration change tracking
- Operational troubleshooting
- Compliance reporting

## Required Log Categories

Cloud workloads should capture:

- Authentication events
- Authorization decisions
- Administrative actions
- Configuration changes
- API activity
- Security alerts
- Network access events
- Data access events where appropriate
- Error and failure events
- High-risk user activity

## AI Assistant Logging Requirements

For AI-enabled workflows, logs should capture:

- User ID
- User role
- Prompt metadata
- Prompt risk score
- Access decision
- Retrieved document IDs
- Denied document IDs
- Response status
- Human review requirement
- Security alert category
- Correlation ID

## Sensitive Logging Guidance

Full prompt and response text should not be logged by default.

Logs should avoid unnecessary storage of:

- Customer data
- Payment data
- Employee records
- Secrets
- Credentials
- Private keys
- Restricted document content

## Monitoring Use Cases

Security monitoring should detect:

- Repeated prompt injection attempts
- Attempts to reveal hidden instructions
- Attempts to access restricted documents
- Sensitive data entered into prompts
- Unauthorized retrieval attempts
- High-risk responses released without review
- Excessive usage or cost spikes
- Logging failures

## Retention Guidance

Log retention should be based on:

- Business requirements
- Audit requirements
- Legal requirements
- Privacy considerations
- Cost constraints

## Security Note

Logs can become sensitive because they may reveal user behavior, document references, access decisions, and security events.

Log access should be restricted to approved roles.
