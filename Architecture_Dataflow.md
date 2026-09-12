# Data Flow

## Purpose

This document describes how data moves through the secure AI assistant architecture.

The goal is to identify security control points, trust boundaries, logging requirements, and areas where sensitive data could be exposed.

## Data Flow Summary

The AI assistant processes the following data types:

- User identity data
- User prompt data
- Document metadata
- Retrieved document excerpts
- AI-generated responses
- Audit logs
- Policy decision records

## Step-by-Step Data Flow

### Step 1: User Authentication

The user authenticates through the enterprise identity provider.

Data involved:

- User ID
- Group membership
- Role assignments
- Authentication status
- Session metadata

Security controls:

- MFA
- Conditional access
- Session expiration
- Identity logging

### Step 2: Prompt Submission

The user submits a question to the AI assistant.

Data involved:

- Prompt text
- User ID
- Timestamp
- Session ID
- Source IP or device metadata, if available

Security controls:

- Input validation
- Prompt injection detection
- Sensitive data detection
- Rate limiting
- Acceptable use policy enforcement

### Step 3: Authorization Check

The system checks whether the user is allowed to use the assistant and which document categories the user may access.

Data involved:

- User role
- Group membership
- Document access policy
- Data classification rules

Security controls:

- Role-based access control
- Attribute-based access control where needed
- Deny-by-default access
- Document-level authorization

### Step 4: Retrieval Query

The system searches the approved knowledge base for relevant content.

Data involved:

- Sanitized user query
- Search terms
- Document embeddings or index references
- Document metadata

Security controls:

- Authorized document filtering
- Data classification enforcement
- Retrieval scope limitation
- Metadata preservation

### Step 5: Context Assembly

The system assembles retrieved content into a controlled prompt context for the AI model.

Data involved:

- Approved document excerpts
- Source references
- System instructions
- User prompt
- Security constraints

Security controls:

- Context size limits
- Restricted document exclusion
- Source validation
- System prompt protection

### Step 6: Model Interaction

The AI model generates a response using the provided context.

Data involved:

- System prompt
- User prompt
- Retrieved context
- Generated response

Security controls:

- No unrestricted tool access
- No autonomous action
- Provider data handling review
- Output constraints
- No use of real sensitive data in local prototype

### Step 7: Response Validation

The system checks the generated answer before displaying it to the user.

Data involved:

- Generated response
- Source references
- Classification labels
- Risk indicators

Security controls:

- Sensitive data scan
- Unsupported claim detection
- Citation requirement
- Restricted topic detection
- Human review routing

### Step 8: User Response

The user receives the AI-generated answer.

Data involved:

- Response text
- Source citations
- Warnings or disclaimers
- Escalation instructions, if needed

Security controls:

- Display only authorized content
- Include limitations
- Provide source references
- Encourage human validation for high-risk topics

### Step 9: Logging and Monitoring

The system records activity for audit and investigation.

Data involved:

- User ID
- Prompt metadata
- Response metadata
- Retrieved document IDs
- Policy decisions
- Blocked prompt attempts
- Escalation events

Security controls:

- Log integrity
- Access restrictions on logs
- Retention policy
- Monitoring alerts
- Privacy review

## Sensitive Data Handling

The architecture should avoid sending the following data to an AI model unless explicitly approved:

- Customer account data
- Payment data
- Authentication secrets
- API keys
- Passwords
- Private keys
- Employee records
- Legal documents
- Unredacted incident data
- Confidential business strategy
- Regulated personal information

## Key Security Control Points

| Data Flow Stage | Main Risk | Control |
|---|---|---|
| Authentication | Unauthorized access | MFA and SSO |
| Prompt submission | Prompt injection or sensitive data entry | Input filtering |
| Authorization | Access to restricted documents | RBAC and document-level permissions |
| Retrieval | Cross-boundary data leakage | Metadata filtering |
| Context assembly | Overexposure of internal content | Context minimization |
| Model interaction | Provider or model data exposure | Data handling review |
| Response validation | Sensitive or inaccurate output | Output filtering and human review |
| Logging | Logs containing sensitive prompts | Log minimization and access control |

## Local Prototype Data Flow

For the local prototype, the data flow is simplified:

1. Mock user role is selected.
2. User submits a prompt.
3. Local sample documents are searched.
4. Only documents available to that role are retrieved.
5. A local or mocked response is generated.
6. Prompt and response metadata are logged locally.
7. Suspicious prompts are flagged.

No real sensitive data should be used.
