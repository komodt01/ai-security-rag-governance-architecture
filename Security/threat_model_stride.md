# STRIDE Threat Model

## Purpose

This document identifies threats to the secure enterprise AI assistant architecture using the STRIDE threat modeling framework.

The purpose is to evaluate how an internal AI assistant using Retrieval-Augmented Generation could be abused, misused, or misconfigured in a regulated environment.

## System Overview

The AI assistant allows authenticated internal users to ask questions against approved organizational documents.

The system includes:

- User interface
- Identity provider
- Access control layer
- Prompt handling layer
- Retrieval layer
- Approved knowledge base
- AI model or LLM interface
- Response validation layer
- Logging and monitoring layer
- Human review process

## Key Assets

| Asset | Description |
|---|---|
| User identity | Authenticated user account, role, group membership, and session data |
| Internal documents | Approved policies, standards, architecture documents, procedures, and compliance guidance |
| Document metadata | Classification labels, ownership, access rules, review dates, and source references |
| Prompts | User-submitted questions or instructions |
| Retrieved context | Document excerpts passed to the AI model |
| AI responses | Generated responses returned to the user |
| Logs | Prompt metadata, response metadata, user activity, policy decisions, and blocked attempts |
| System prompts | Internal instructions that guide AI behavior |
| Access policies | Rules that determine which documents and functions users may access |

## Trust Boundaries

| Trust Boundary | Description |
|---|---|
| User to AI assistant interface | Boundary between employee input and the application |
| AI assistant to identity provider | Boundary where authentication and authorization data is exchanged |
| Prompt handling to retrieval layer | Boundary where user prompts are converted into document search requests |
| Retrieval layer to knowledge base | Boundary where documents are queried and filtered |
| AI assistant to AI model | Boundary where prompts and retrieved context are sent to the model |
| AI assistant to logging layer | Boundary where activity is recorded for audit and investigation |
| AI output to user | Boundary where generated content is presented to the user |

---

# STRIDE Analysis

## 1. Spoofing

### Threat Description

Spoofing occurs when an attacker pretends to be another user, service, or trusted system component.

### Example Threats

| Threat | Example |
|---|---|
| User impersonation | An attacker uses stolen credentials to access the AI assistant |
| Session hijacking | An attacker reuses an active session token |
| Service impersonation | A malicious service pretends to be the approved AI model endpoint |
| Role spoofing | A user manipulates request metadata to appear as a privileged role |

### Potential Impact

- Unauthorized access to restricted documents
- Exposure of confidential information
- Incorrect audit attribution
- Privileged AI functions used by unauthorized users

### Security Controls

| Control | Description |
|---|---|
| Strong authentication | Require SSO and MFA for all users |
| Session management | Enforce session timeout and token protection |
| Role validation | Validate role and group membership server-side |
| Service authentication | Authenticate application-to-model and application-to-logging connections |
| Audit attribution | Log verified user identity for every prompt and response |

### Residual Risk

Spoofing risk remains if user credentials are compromised or if privileged access is not reviewed regularly.

---

## 2. Tampering

### Threat Description

Tampering occurs when data, prompts, documents, model inputs, model outputs, logs, or policies are altered without authorization.

### Example Threats

| Threat | Example |
|---|---|
| Prompt manipulation | User attempts to override system instructions |
| Document tampering | An attacker modifies source documents to influence AI responses |
| Retrieval manipulation | Unauthorized changes to document metadata alter what content is retrieved |
| Response tampering | AI output is modified before being shown to the user |
| Log tampering | An attacker deletes or changes prompt/response logs |

### Potential Impact

- AI returns incorrect or unsafe guidance
- Users rely on manipulated documents
- Audit records become unreliable
- Prompt injection succeeds
- Compliance evidence is weakened

### Security Controls

| Control | Description |
|---|---|
| Change control | Require approval for document updates |
| Document integrity | Track document version, owner, and review date |
| Prompt injection controls | Detect attempts to override system instructions |
| Output validation | Check responses for unsupported or unsafe content |
| Immutable logging | Restrict log modification and retain audit history |
| Admin separation | Separate content administration from system administration |

### Residual Risk

Tampering risk remains if document governance is weak or if logs are not protected from privileged misuse.

---

## 3. Repudiation

### Threat Description

Repudiation occurs when users or administrators deny actions because the system lacks sufficient evidence.

### Example Threats

| Threat | Example |
|---|---|
| User denies prompt submission | A user claims they did not submit a risky prompt |
| Admin denies policy change | An administrator changes access rules without traceability |
| Missing source traceability | AI response cannot be tied back to source documents |
| Incomplete logs | Prompt, response, or policy decision is not recorded |

### Potential Impact

- Weak incident investigation capability
- Poor audit readiness
- Inability to prove misuse
- Inability to reconstruct AI decision flow
- Increased regulatory or legal risk

### Security Controls

| Control | Description |
|---|---|
| User activity logging | Log user ID, timestamp, prompt metadata, and session metadata |
| Admin action logging | Log changes to policies, documents, and configuration |
| Source citation | Record which documents were retrieved for each response |
| Policy decision logging | Log allow, deny, block, and escalation decisions |
| Log retention | Define retention requirements based on compliance needs |

### Residual Risk

Repudiation risk remains if logs contain too little detail or if sensitive prompts must be minimized for privacy reasons.

---

## 4. Information Disclosure

### Threat Description

Information disclosure occurs when sensitive, confidential, restricted, or unauthorized information is exposed.

### Example Threats

| Threat | Example |
|---|---|
| Unauthorized document retrieval | A user receives content from documents outside their role |
| Sensitive prompt submission | User enters customer data, credentials, or confidential records |
| Sensitive response output | AI response exposes restricted information |
| Cross-user leakage | One user's context or prompt appears in another user's response |
| Excessive logging | Logs store sensitive prompt or response content without controls |
| Vendor data exposure | Prompts or retrieved context are sent to an external provider without approval |

### Potential Impact

- Exposure of regulated data
- Loss of customer or employee privacy
- Intellectual property leakage
- Compliance violations
- Legal or reputational harm

### Security Controls

| Control | Description |
|---|---|
| Data classification | Label documents by sensitivity and approved use |
| Document-level authorization | Retrieve only documents the user is permitted to access |
| Prompt filtering | Detect and block sensitive data in prompts |
| Response filtering | Detect sensitive content before output is shown |
| Data minimization | Send only necessary context to the model |
| Log minimization | Avoid storing full sensitive prompts unless justified |
| Provider review | Assess AI provider data handling, retention, and training policies |

### Residual Risk

Information disclosure is one of the highest-risk categories for AI assistants because retrieval, generation, and logging can each expose sensitive data if controls fail.

---

## 5. Denial of Service

### Threat Description

Denial of Service occurs when the AI assistant, retrieval layer, model interface, or supporting systems become unavailable or degraded.

### Example Threats

| Threat | Example |
|---|---|
| Prompt flooding | User or attacker submits excessive prompts |
| Expensive query abuse | Long or complex prompts consume excessive compute or API usage |
| Retrieval overload | Large document searches degrade performance |
| Model dependency outage | AI model provider becomes unavailable |
| Logging failure | Logging pipeline outage prevents audit capture |

### Potential Impact

- AI assistant unavailable to users
- Increased operating costs
- Delayed business workflows
- Reduced trust in AI service
- Loss of monitoring or audit evidence

### Security Controls

| Control | Description |
|---|---|
| Rate limiting | Limit prompt frequency by user or role |
| Quotas | Define usage limits by group or business unit |
| Timeout controls | Stop long-running queries |
| Cost monitoring | Monitor usage and cost patterns |
| Graceful degradation | Provide fallback to source documents if AI service fails |
| Service health monitoring | Alert on retrieval, model, or logging failures |

### Residual Risk

Denial of Service risk remains if the system depends on external model providers or if usage spikes are not monitored.

---

## 6. Elevation of Privilege

### Threat Description

Elevation of Privilege occurs when a user gains capabilities beyond their authorized role.

### Example Threats

| Threat | Example |
|---|---|
| Prompt-based privilege escalation | User instructs AI to ignore role restrictions |
| Retrieval bypass | User manipulates prompts to access restricted documents |
| Admin function abuse | Non-admin user accesses configuration or document ingestion tools |
| Tool misuse | AI assistant performs actions beyond intended read-only behavior |
| Excessive agency | AI system is granted ability to execute changes without human approval |

### Potential Impact

- Unauthorized access to restricted documents
- Unauthorized configuration changes
- Unapproved business or security decisions
- Privileged operations triggered through AI workflow
- Loss of control over AI-enabled actions

### Security Controls

| Control | Description |
|---|---|
| Deny-by-default authorization | Users receive no access unless explicitly granted |
| Server-side access checks | Never rely on user-provided role claims |
| Read-only initial design | Initial AI assistant should not perform autonomous changes |
| Human approval | Require approval for high-risk decisions or actions |
| Least privilege | Restrict admin and ingestion functions |
| Separation of duties | Separate AI users, content owners, reviewers, and administrators |

### Residual Risk

Elevation of Privilege risk remains if the AI assistant is later connected to tools, APIs, ticketing systems, or production workflows without strong approval controls.

---

# Summary Risk Table

| STRIDE Category | Risk Level | Primary Concern |
|---|---|---|
| Spoofing | Medium | Stolen credentials or false role claims |
| Tampering | High | Prompt injection or document manipulation |
| Repudiation | Medium | Incomplete logging or weak audit trails |
| Information Disclosure | High | Sensitive data leakage through prompts, retrieval, output, or logs |
| Denial of Service | Medium | Usage abuse, model outage, or cost spikes |
| Elevation of Privilege | High | Unauthorized access or excessive AI agency |

## Highest Priority Risks

The highest priority risks for this architecture are:

1. Information disclosure
2. Prompt injection and tampering
3. Elevation of privilege
4. Weak logging and auditability
5. Overreliance on AI-generated responses

## Recommended Control Priorities

| Priority | Control Area | Reason |
|---|---|---|
| 1 | Document-level access control | Prevents unauthorized retrieval |
| 2 | Prompt injection controls | Reduces manipulation risk |
| 3 | Sensitive data filtering | Reduces disclosure risk |
| 4 | Source citation and response validation | Reduces hallucination and overreliance |
| 5 | Logging and monitoring | Supports investigation and audit |
| 6 | Human review | Keeps accountability with approved personnel |
| 7 | Cost and rate controls | Prevents misuse and runaway usage |

## Conclusion

The AI assistant introduces new risk patterns beyond traditional application architecture. The most important design concern is not only whether the model generates accurate answers, but whether the surrounding system enforces identity, access, data protection, logging, and human accountability.

The architecture should treat the AI model as one component inside a governed system, not as the control authority.
