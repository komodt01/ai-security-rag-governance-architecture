# Data Flow

## Purpose

This document describes how data moves through the secure AI assistant reference architecture.

The goal is to identify security control points, trust boundaries, authorization decisions, logging requirements, and areas where sensitive information could be exposed.

The production-oriented reference flow is described first. The implemented local prototype uses a simplified version of this flow to validate selected security controls.

## Data Flow Summary

The reference architecture processes several types of information:

- User identity and authorization context
- User prompt data
- Document metadata
- Retrieved document content
- Model context
- AI-generated responses
- Audit and security events
- Policy and access decisions
- Human-review events

## Step-by-Step Reference Architecture Data Flow

### Step 1: User Authentication

The user authenticates through the enterprise identity provider.

Data involved:

- User ID
- Group membership
- Role assignments
- Authentication status
- Session metadata

Security controls may include:

- MFA
- Conditional access
- Session management
- Identity logging

Authentication establishes who the user is. It does not by itself determine which enterprise information the user may retrieve.

### Step 2: Prompt Submission and Risk Evaluation

The user submits a question through the AI assistant.

Data involved:

- Prompt text
- User identity
- Timestamp
- Session or correlation ID
- Device or network context where appropriate

Security controls may include:

- Input validation
- Prompt injection detection
- Sensitive-data detection
- Abuse-pattern detection
- Rate limiting
- Acceptable-use enforcement

Requests that violate defined policy may be blocked before retrieval.

### Step 3: Authorization Context

The system establishes the authorization context that will govern retrieval.

Data involved:

- User role
- Group membership
- Resource permissions
- Document access policy
- Data-classification rules

Security controls include:

- Role- or attribute-based authorization
- Least privilege
- Deny-by-default behavior
- Document-level authorization

The objective is to preserve existing enterprise authorization boundaries rather than allowing the AI assistant to create a new path around them.

### Step 4: Retrieval

The system searches approved knowledge sources for information relevant to the request.

Data involved:

- User query
- Search terms or semantic representation
- Document or index references
- Document metadata
- Authorization context

Security controls include:

- Approved-source restrictions
- Authorization enforcement
- Data-classification enforcement
- Retrieval-scope limitation
- Metadata preservation

Relevant content should not be treated as authorized content merely because it matches the query.

### Step 5: Context Assembly

Authorized retrieved content is assembled into controlled context for the model.

Data involved:

- Authorized document excerpts
- Source metadata
- System instructions
- User prompt
- Security constraints

Security controls may include:

- Context-size limits
- Restricted-content exclusion
- Source validation
- Context minimization
- System-instruction protection

Retrieved content should itself be treated as untrusted input because documents may contain malicious, outdated, inappropriate, or conflicting instructions.

### Step 6: Model Interaction

The AI model generates a response using the authorized context.

Data involved:

- System instructions
- User prompt
- Retrieved context
- Generated response

Security controls may include:

- Controlled tool access
- Restrictions on autonomous actions
- Provider data-handling requirements
- External connectivity restrictions
- Model and provider approval
- Output constraints

The model is not the authorization authority and should not be relied upon to decide whether protected information may be disclosed.

### Step 7: Response Validation

The generated response is evaluated before release to the user.

Data involved:

- Generated response
- Source references
- Classification context
- Risk indicators

Controls may include:

- Sensitive-data detection
- Source traceability
- Unsupported-claim detection
- Restricted-topic detection
- Policy warnings
- Human-review routing

The level of response validation should reflect the potential consequence of an incorrect or inappropriate answer.

### Step 8: User Response

The authorized response is returned to the user.

Data involved:

- Response text
- Source references
- Warnings or limitations
- Escalation instructions where appropriate

Security controls include:

- Return only authorized information
- Preserve source traceability
- Communicate appropriate limitations
- Require or recommend human validation where consequence warrants it

### Step 9: Logging and Monitoring

Relevant activity is recorded for audit, security monitoring, troubleshooting, and incident investigation.

Data may include:

- User ID
- Timestamp
- Correlation ID
- Prompt-risk metadata
- Retrieved document IDs
- Denied document IDs
- Access decisions
- Response metadata
- Policy decisions
- Blocked requests
- Security alerts
- Human-review events
- Administrative actions

Security controls include:

- Log integrity
- Restricted log access
- Data minimization
- Retention requirements
- Security monitoring
- Privacy review

Full prompts, responses, or retrieved content should not automatically be logged without considering their sensitivity and the organization's evidence requirements.

## Sensitive Data Handling

The architecture should avoid sending sensitive information to an AI model unless there is an approved business requirement and appropriate controls.

Examples include:

- Customer account data
- Payment data
- Authentication secrets
- API keys
- Passwords
- Private keys
- Employee records
- Legal or privileged information
- Unredacted incident data
- Confidential business information
- Regulated personal information

The appropriate handling decision depends on classification, authorization, model/provider architecture, contractual requirements, and the organization's risk tolerance.

## Key Security Control Points

| Data Flow Stage | Main Risk | Primary Control |
| --- | --- | --- |
| Authentication | Unauthorized system access | Enterprise identity, MFA, conditional access |
| Prompt submission | Prompt injection or sensitive-data entry | Prompt-risk evaluation |
| Authorization | Unauthorized information access | Role/group/attribute and document-level authorization |
| Retrieval | Cross-boundary information leakage | Authorization-aware retrieval and metadata filtering |
| Context assembly | Excessive or malicious context | Context minimization and source controls |
| Model interaction | Model/provider data exposure | Provider, data-handling, and connectivity controls |
| Response validation | Sensitive, unsupported, or high-risk output | Response controls and appropriate human review |
| Logging | Sensitive information captured in logs | Data minimization, access control, and retention policy |

## Local Prototype Data Flow

The implemented local Python prototype validates a simplified subset of the production reference flow.

It does not use an LLM, embeddings, vector database, enterprise identity provider, or cloud AI service.

The implemented flow is:

1. A mock user is selected with predefined role and group information.
2. The user submits a prompt.
3. The prompt is evaluated using local pattern-based risk logic.
4. Sensitive-data or prompt-injection patterns can cause the request to be blocked before document retrieval.
5. Requests that are not blocked proceed to local document retrieval.
6. Candidate documents are identified using simplified keyword-based matching.
7. Document metadata is evaluated against the mock user's role and group membership.
8. Documents are separated into authorized retrieved documents and denied documents.
9. Prompt, retrieval, authorization, and security events are written to local JSONL logs.
10. Documents configured for human review can generate a simulated review event.
11. A mock advisory response is generated from authorized local document content.

The human-review mechanism is a simulated trigger and does not currently operate as an approval gate.

## Local Prototype Evidence

Initial documented testing has validated two paths:

### Authorized Retrieval Path

A General Employee requested information from the mock AI acceptable-use policy.

The request was evaluated, the user's authorization was checked, the approved document was retrieved, relevant events were logged, and an advisory response was generated.

**Result: Pass**

### Blocked Prompt Injection Path

A General Employee submitted a prompt attempting to override instructions and reveal restricted documents.

The prompt-risk logic identified the injection pattern and blocked the request before document retrieval.

**Result: Pass**

Additional prompt injection, access-control, and sensitive-data scenarios are defined but have not yet been validated.

## Key Data Flow Principle

The most important security boundary in this architecture is not the AI model itself.

The intended sequence is:

**Identity → Prompt Risk → Authorization-Aware Retrieval → Controlled Context → Model → Response Controls → User**

with security logging and governance surrounding the workflow.

For the local prototype, the sequence stops short of an actual model:

**Mock Identity → Prompt Risk → Local Retrieval → Metadata Authorization → Logging / Review Trigger → Advisory Response**

This allows selected security-control behavior to be validated without implying that the complete production RAG architecture has been implemented.
