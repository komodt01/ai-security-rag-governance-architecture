# STRIDE Threat Model

## Purpose

This document applies the STRIDE threat-modeling framework to the enterprise AI assistant architecture.

The objective is to identify how an AI-enabled knowledge assistant could be abused, misused, compromised, or misconfigured and to determine where security controls should exist.

The threat model covers both:

1. The conceptual production AI/RAG architecture.
2. The limited local security-control prototype used to validate selected architecture decisions.

These should not be confused.

The local prototype does not implement a production RAG platform, LLM, enterprise identity provider, cloud AI service, or production monitoring environment.

# Core Principle

> The AI model is one component inside the system. It is not the security authority.

Important controls should exist outside the model, particularly:

- Identity
- Authorization
- Retrieval control
- Data classification
- Logging
- Administrative control
- Human accountability

# Production Architecture in Scope

A production implementation could contain:

```text
User
  ↓
AI Assistant
  ↓
Trusted Identity
  ↓
Prompt / Request Controls
  ↓
Permission-Aware Retrieval
  ↓
Approved Knowledge Sources
  ↓
Authorized Context
  ↓
AI Model
  ↓
Response Controls
  ↓
User
```

Security logging and monitoring should observe important events throughout the flow.

Human authority should remain outside the AI for consequential decisions.

# Current Local Prototype

The implemented prototype is intentionally smaller:

```text
Mock User
   ↓
Prompt Risk Evaluation
   ↓
Local Retrieval
   ↓
Metadata Authorization
   ↓
Logging / Simulated Review Trigger
   ↓
Advisory Response
```

It uses:

- Synthetic users
- Synthetic documents
- Roles and groups
- Document metadata
- Simple keyword retrieval
- Pattern-based prompt evaluation
- Local JSONL logging
- Advisory response generation

It does not use:

- Production LLM
- Embeddings
- Vector database
- Enterprise IdP
- MFA
- Cloud AI
- External model API
- Production SIEM
- Production human-review workflow
- Autonomous tools or agents

# Key Assets

A production architecture may need to protect:

| Asset | Security Concern |
| --- | --- |
| User identity | Prevent impersonation and privilege misuse |
| Internal documents | Prevent unauthorized disclosure or manipulation |
| Document metadata | Preserve classification and authorization integrity |
| Prompts | Prevent misuse and unnecessary sensitive-data exposure |
| Retrieved context | Ensure only authorized information reaches the model |
| AI responses | Prevent unsafe or unauthorized disclosure |
| Logs | Preserve useful evidence without creating another sensitive repository |
| System instructions | Prevent inappropriate exposure or manipulation |
| Access policies | Prevent unauthorized changes to security decisions |
| Model/provider connection | Prevent service impersonation or unauthorized data transfer |
| Administrative configuration | Prevent unauthorized control changes |

Not every asset exists in the local prototype.

# Trust Boundaries

Important production trust boundaries include:

| Boundary | Security Question |
| --- | --- |
| User → Assistant | Can the request or identity be trusted? |
| Assistant → Identity Provider | Is identity authoritative and protected? |
| Prompt Handling → Retrieval | Can prompt content change authorization scope? |
| Retrieval → Knowledge Source | Are only approved and authorized sources accessible? |
| Knowledge Source → Model Context | Can malicious or unauthorized content enter context? |
| Assistant → Model Provider | What information leaves the application boundary? |
| Model → Response Controls | Can unsafe or unsupported output reach the user? |
| Assistant → Logging | Can security evidence be lost or manipulated? |
| Administrator → Configuration | Can privileged changes weaken controls? |
| AI Output → User | Can the response be mistaken for authority? |

The local prototype exercises only selected portions of these boundaries.

---

# STRIDE Analysis

# 1. Spoofing

## Threat

Spoofing occurs when an attacker pretends to be another user, service, role, or trusted system component.

## Example Threats

| Threat | Example |
| --- | --- |
| User impersonation | Attacker uses stolen credentials |
| Session hijacking | Attacker reuses a valid session |
| Role impersonation | User claims to be an administrator in a prompt |
| Service impersonation | Malicious endpoint pretends to be an approved model service |
| Administrative impersonation | Attacker performs configuration changes as another administrator |

## Potential Impact

- Unauthorized document access
- Confidentiality breach
- Incorrect attribution
- Unauthorized administrative activity
- Privileged AI capability misuse

## Production Controls

Possible controls include:

- Enterprise SSO
- MFA
- Trusted identity claims
- Secure session handling
- Server-side authorization
- Service authentication
- Workload identity
- Administrative access controls
- Identity-aware logging

## Local Prototype

The prototype uses synthetic users loaded from local configuration.

It does not validate enterprise authentication or session security.

It does demonstrate one important architecture principle:

> A natural-language claim of privilege should not become trusted identity.

Authorization uses the configured mock role/group context rather than allowing the prompt to grant privilege.

## Residual Risk

In production, spoofing remains possible through:

- Credential compromise
- Session compromise
- Identity-provider compromise
- Excessive privilege
- Weak administrative controls

Identity security therefore remains an external dependency of the AI architecture.

---

# 2. Tampering

## Threat

Tampering occurs when prompts, documents, metadata, configuration, logs, model inputs, model outputs, or security policies are changed without authorization.

## Example Threats

| Threat | Example |
| --- | --- |
| Prompt manipulation | User attempts to override security behavior |
| Document poisoning | Malicious instructions are inserted into a knowledge source |
| Metadata tampering | Authorization metadata is changed |
| Policy tampering | Security configuration is weakened |
| Response tampering | Output is modified before reaching the user |
| Log tampering | Evidence is deleted or altered |

## Potential Impact

- Incorrect guidance
- Unauthorized retrieval
- Indirect prompt injection
- Security-control bypass
- Unreliable audit evidence
- Incorrect business decisions

## Production Controls

Possible controls include:

- Content ownership
- Change management
- Version control
- Document approval
- Metadata integrity
- Administrative separation
- Protected security configuration
- Protected centralized logging
- Prompt-injection controls
- Response controls

## Local Prototype

The prototype demonstrates:

- Local document metadata
- Document approval status
- Prompt-risk evaluation
- Authorization decisions
- Local JSONL evidence

It does not implement:

- Immutable logs
- Production content approval workflow
- Enterprise change management
- Indirect prompt-injection protection
- Production response validation

## Important AI-Specific Concern

A document can be technically authentic while still containing malicious instructions.

Therefore:

> Document integrity and prompt-injection resistance are related but different problems.

A production RAG architecture should treat retrieved content as untrusted input even when the source itself is approved.

---

# 3. Repudiation

## Threat

Repudiation occurs when a user or administrator can deny an action because sufficient evidence does not exist.

## Example Threats

| Threat | Example |
| --- | --- |
| User denies request | User disputes submitting a malicious prompt |
| Admin denies change | Security configuration changed without attribution |
| Missing retrieval evidence | Cannot determine which documents were considered |
| Missing authorization evidence | Cannot determine why content was allowed |
| Missing review evidence | Cannot determine who approved a consequential action |

## Potential Impact

- Weak incident investigation
- Poor accountability
- Incomplete audit evidence
- Difficulty reconstructing security decisions
- Increased legal or compliance exposure

## Production Controls

Useful evidence may include:

- Trusted user identity
- Timestamp
- Correlation ID
- Prompt metadata
- Retrieval decisions
- Authorization decisions
- Security alerts
- Administrative changes
- Review decisions
- Source references

Retention should follow enterprise policy rather than arbitrary periods defined by this project.

## Local Prototype

The prototype writes:

```text
prompt_events.jsonl
retrieval_events.jsonl
access_decisions.jsonl
security_alerts.jsonl
review_events.jsonl
```

This provides evidence for selected local control decisions.

The prototype does not implement:

- Enterprise log immutability
- SIEM integration
- Production identity attribution
- Administrative audit logging
- Formal human approval records

## Architecture Tradeoff

Logging must balance accountability against privacy.

Capturing every prompt and response may improve reconstruction but may also create a sensitive secondary repository.

The production design should collect evidence intentionally.

---

# 4. Information Disclosure

## Threat

Information disclosure occurs when information is exposed to someone or something that should not receive it.

For an enterprise AI assistant, this is one of the most important threat categories because information can leak through several paths.

## Exposure Paths

```text
User Prompt
    ↓
Retrieval
    ↓
Context
    ↓
Model Provider
    ↓
Response
    ↓
Logs
```

Each stage can create a different disclosure risk.

## Example Threats

| Threat | Example |
| --- | --- |
| Unauthorized retrieval | User receives a document outside authorized scope |
| Sensitive prompt | User submits customer data or credentials |
| Sensitive output | AI returns protected information |
| Cross-user leakage | One user's context appears in another response |
| Excessive logging | Sensitive prompts or responses are retained unnecessarily |
| Provider exposure | Enterprise information is sent to an unapproved provider |
| System instruction exposure | Protected instructions are revealed |

## Potential Impact

- Confidentiality breach
- Privacy exposure
- Intellectual-property loss
- Regulatory impact
- Credential compromise
- Security architecture exposure
- Reputational harm

## Production Controls

Possible controls include:

- Data classification
- Trusted identity
- Document-level authorization
- Permission-aware retrieval
- Data minimization
- Prompt controls
- Context minimization
- Provider review
- Response controls
- Log minimization
- Encryption
- Secrets management

## Local Prototype

The prototype uses only synthetic information.

It demonstrates selected controls for:

- Document classification metadata
- Role/group authorization
- Prompt-risk evaluation
- Blocking selected sensitive-data patterns
- Retrieval allow/deny evidence

It does not validate:

- Production DLP
- Provider data handling
- Cross-user model isolation
- LLM response leakage
- Embedding security
- Vector-database security

## Architecture Priority

Information disclosure deserves significant attention in a production AI/RAG architecture because the AI assistant can create a new interface to existing enterprise information.

The architecture should preserve existing authorization boundaries rather than creating a broader AI-specific entitlement.

---

# 5. Denial of Service

## Threat

Denial of Service occurs when the AI assistant or one of its dependencies becomes unavailable, degraded, or excessively expensive to operate.

## Example Threats

| Threat | Example |
| --- | --- |
| Prompt flooding | Excessive requests overwhelm the service |
| Expensive-query abuse | Requests consume excessive model resources |
| Retrieval overload | Broad searches consume excessive resources |
| Provider outage | External model becomes unavailable |
| Identity outage | Users cannot authenticate |
| Logging outage | Security evidence cannot be recorded |
| Cost exhaustion | Usage causes budget limits to be reached |

## Potential Impact

- Service unavailable
- Delayed business workflow
- Increased cost
- Missing evidence
- User reliance on unavailable service
- Reduced trust in the platform

## Production Controls

Possible controls include:

- Rate limits
- Quotas
- Timeouts
- Usage controls
- Cost monitoring
- Dependency monitoring
- Graceful degradation
- Source-document fallback
- Capacity planning
- Provider contingency planning

## Local Prototype

The local prototype is not a production service.

It does not implement:

- Rate limiting
- Production quotas
- Cloud cost controls
- Availability monitoring
- Provider failover
- Production SLOs

Its approximate operating cost is $0.

## Architecture Consideration

The business should still have access to authoritative source information when the AI assistant is unavailable.

The AI layer should not unnecessarily become the only path to enterprise knowledge.

---

# 6. Elevation of Privilege

## Threat

Elevation of Privilege occurs when a user, administrator, service, or AI component gains authority beyond what was intended.

## Example Threats

| Threat | Example |
| --- | --- |
| Prompt-based privilege claim | User tells AI to treat them as an administrator |
| Retrieval bypass | Prompt attempts to obtain Restricted documents |
| Administrative misuse | Platform administrator accesses protected content |
| Configuration abuse | User changes security controls |
| Tool misuse | AI invokes a privileged downstream API |
| Excessive agency | AI takes consequential action without human authority |

## Potential Impact

- Unauthorized information access
- Unauthorized configuration change
- Improper approval
- Production impact
- Fraud or financial consequence
- Loss of governance control

## Production Controls

Possible controls include:

- Deny-by-default authorization
- Trusted identity
- Least privilege
- Document-level authorization
- Administrative separation
- Privileged-access controls
- Tool-specific authorization
- Transaction limits
- Human authority for consequential actions
- Detailed action logging

## Local Prototype

The prototype demonstrates:

- Mock roles and groups
- Document-level allow/deny behavior
- Separation between AI system administration and content entitlement
- Prompt-risk evaluation
- Block-before-retrieval behavior for the validated injection test

The prototype is advisory only.

It cannot:

- Modify production systems
- Approve access
- Execute transactions
- Invoke enterprise tools
- Make production changes

## Agentic AI Consideration

If the architecture later moves from:

```text
AI answers
```

to:

```text
AI acts
```

the Elevation-of-Privilege threat changes substantially.

Each tool would require its own:

- Identity
- Authorization
- Scope
- Transaction boundary
- Logging
- Failure handling
- Human-approval decision

Agent capability should therefore trigger a new threat-model review.

---

# Cross-Cutting AI Threats

Some AI risks do not fit neatly into only one STRIDE category.

# Prompt Injection

Prompt injection may contribute to:

- Tampering
- Information Disclosure
- Elevation of Privilege

The current prototype demonstrates one direct prompt-injection control path.

It does not demonstrate comprehensive prompt-injection resistance.

# Indirect Prompt Injection

Malicious retrieved content can attempt to manipulate the model.

This affects:

- Tampering
- Information Disclosure
- Elevation of Privilege

The production architecture should treat retrieved content as untrusted.

The local prototype does not implement an LLM and therefore does not validate indirect prompt-injection controls.

# Hallucination

Hallucination is not naturally a STRIDE threat by itself.

Its security significance depends on consequence.

Incorrect output could contribute to:

- Unsafe business decisions
- Incorrect security guidance
- Compliance mistakes
- Operational errors

Controls may include:

- Source grounding
- Response validation
- Authority boundaries
- Human review for consequential decisions

The local prototype does not use an LLM and therefore does not validate hallucination controls.

# Excessive Agency

Excessive agency becomes relevant when AI can invoke tools or perform actions.

It can contribute to:

- Elevation of Privilege
- Tampering
- Information Disclosure
- Denial of Service

The current prototype has no autonomous action capability.

---

# Threat Prioritization

This project does not assign fixed numeric or universal Medium/High ratings to each STRIDE category.

The priority depends on:

- Actual data
- User population
- Production authority
- Exposure
- Threat likelihood
- Business consequence
- Control maturity

For the **production concept**, the areas I would pay particular attention to are:

1. Unauthorized information disclosure
2. Authorization bypass
3. Prompt and retrieved-content manipulation
4. Administrative privilege
5. Logging and evidence
6. Overreliance on AI output
7. Operational dependency
8. Agent/tool authority if later introduced

This is a design priority rather than a formal enterprise risk rating.

# Threat-to-Control Summary

| Threat Area | Important Architecture Controls |
| --- | --- |
| Identity spoofing | Trusted identity, MFA, session security |
| Role spoofing | Server-side authorization |
| Prompt manipulation | Prompt controls plus independent authorization |
| Document poisoning | Content governance and untrusted-context handling |
| Metadata tampering | Protected configuration and change control |
| Log tampering | Protected centralized logging |
| Unauthorized retrieval | Permission-aware retrieval |
| Sensitive prompt | Input controls and data policy |
| Sensitive output | Authorized context plus output controls |
| Provider exposure | Data minimization and vendor review |
| Service exhaustion | Rate limits, quotas, monitoring |
| Excess privilege | Least privilege and separation of duties |
| Excessive agency | Tool authorization and human authority |

# Current Prototype Evidence

The prototype currently provides implementation evidence for selected controls:

- Synthetic identity context
- Role/group authorization
- Document metadata
- Prompt-risk evaluation
- Selected sensitive-data patterns
- Simple local retrieval
- Document allow/deny decisions
- Structured JSONL evidence
- Security-alert generation
- Simulated review trigger
- Advisory-only response

# Validated Scenarios

Two initial scenarios are documented as executed.

## Authorized Policy Retrieval

A mock General Employee requested the approved synthetic AI acceptable-use policy.

**Result: Pass**

This provides evidence for selected retrieval and authorization behavior.

## Direct Prompt Injection

A mock General Employee attempted to override instructions and reveal Restricted documents.

**Result: Pass**

The request was blocked before retrieval and a security alert was generated.

Other documented test scenarios remain **Not Yet Tested**.

# Controls Not Validated by the Prototype

The current project should not claim implementation evidence for:

- Enterprise authentication
- MFA
- Session security
- Production SSO
- Immutable logging
- SIEM integration
- Production DLP
- Production LLM output controls
- Indirect prompt-injection defense
- Vector-database security
- Embedding security
- Cloud provider controls
- Provider data handling
- Production human approval
- Rate limiting
- Production resilience
- Autonomous-agent controls

These remain production architecture concerns.

# Failure Paths

A threat model should consider what happens when a control fails.

## Prompt Filter Misses an Attack

Authorization should still prevent unauthorized document access.

## Authorization Cannot Be Determined

Protected content should be denied.

## Logging Fails

A production system should define whether sensitive operations fail closed, degrade safely, or continue with alternate evidence.

The appropriate behavior depends on business consequence.

## Model Provider Fails

Users should retain access to authoritative source systems where possible.

## Retrieved Content Is Malicious

The production architecture should treat retrieved content as untrusted and prevent it from becoming control authority.

## Human Review Is Unavailable

Consequential decisions requiring human authority should not silently become AI-approved decisions.

# Architecture Decisions

## Decision 1 — Keep Authorization Outside the Model

**Reason:** Prompt or model behavior should not redefine access.

## Decision 2 — Preserve Document-Level Access

**Reason:** AI should not create a broader entitlement than the source system.

## Decision 3 — Treat Retrieved Content as Untrusted

**Reason:** Approved documents can still contain malicious or inappropriate instructions.

## Decision 4 — Separate Platform Administration from Data Entitlement

**Reason:** Operating the AI system should not automatically grant access to all content.

## Decision 5 — Keep the Initial System Advisory

**Reason:** Read-only advisory use reduces the consequence of model error and privilege misuse.

## Decision 6 — Log Security Decisions

**Reason:** Investigators need evidence of prompt, retrieval, and authorization behavior.

## Decision 7 — Reassess When the Architecture Changes

A new threat review should occur when introducing:

- Real enterprise data
- Production LLM
- New provider
- New retrieval source
- Enterprise identity
- Cloud deployment
- Agent/tool execution
- Production decision authority
- New user population

# Relationship to the Local Prototype

The STRIDE model intentionally extends beyond what the prototype implements.

That is appropriate.

Threat modeling asks:

> What could go wrong in the intended architecture?

Prototype validation asks:

> Which selected control behaviors have I actually demonstrated?

Keeping those questions separate prevents the portfolio from overstating implementation while still demonstrating production architecture thinking.

# Conclusion

STRIDE provides a useful structure for examining AI security, but the important architectural insight is broader than the six category names.

An AI assistant introduces new paths between:

```text
Identity
   ↓
Prompt
   ↓
Retrieval
   ↓
Enterprise Data
   ↓
Model
   ↓
Response
   ↓
Business Decision
```

The security architecture must preserve trust boundaries across that path.

For this project, the production threat model identifies the broader risks while the local prototype validates selected controls using synthetic data.

The strongest design principle remains:

> The model can assist with information. It does not become the authority for identity, access, data entitlement, or consequential business decisions.
