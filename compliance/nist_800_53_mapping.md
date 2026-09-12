# NIST SP 800-53 Security Control Mapping

## Purpose

This document maps the enterprise AI security architecture in this repository to selected NIST SP 800-53 security and privacy control families.

The purpose is to show how established enterprise security controls continue to apply when AI and Retrieval-Augmented Generation are introduced into an information-access workflow.

This is a **security architecture mapping**.

> It is not a NIST SP 800-53 assessment, authorization package, control implementation statement, or claim that every referenced control has been satisfied.

The mapping distinguishes between:

1. Architecture requirements.
2. Controls demonstrated by the local prototype.
3. Production controls that would require enterprise implementation.

# Project Context

The production concept is an internal AI assistant that could eventually use Retrieval-Augmented Generation to help employees find and understand approved enterprise information.

The current project has progressed through:

```text
Architecture and Governance
        ↓
Local Security-Control Prototype
        ↓
Selected Control Validation
```

The local prototype uses:

- Synthetic users
- Synthetic documents
- Mock roles and groups
- Document metadata
- Simple keyword retrieval
- Pattern-based prompt-risk evaluation
- Document authorization
- Structured JSONL logging
- Advisory response generation
- Simulated human-review triggers

It does not use:

- Production LLM
- Embeddings
- Vector database
- Enterprise SSO
- MFA
- Production SIEM
- Cloud AI
- External model provider
- Formal approval workflow
- Real enterprise data
- Autonomous tools or agents

# Core Security Principle

> AI should operate inside existing enterprise security boundaries rather than create a new path around them.

The model should not determine:

- User identity
- Data entitlement
- Risk acceptance
- Security policy
- Approval authority
- Logging requirements
- Production authorization

# Selected NIST SP 800-53 Families

| Family | Relevance to the Architecture |
| --- | --- |
| AC — Access Control | User authorization, document entitlement, least privilege |
| AU — Audit and Accountability | Security evidence, traceability, investigation |
| AT — Awareness and Training | Appropriate AI use and limitations |
| CA — Assessment, Authorization, and Monitoring | Control validation and reassessment |
| CM — Configuration Management | Changes to access, prompts, retrieval, model/provider settings |
| CP — Contingency Planning | Safe fallback when AI is unavailable or unsafe |
| IA — Identification and Authentication | Trusted user and service identity |
| IR — Incident Response | Handling AI-related security events |
| PL — Planning | Security architecture, scope, boundaries |
| RA — Risk Assessment | AI risk evaluation and threat modeling |
| SA — System and Services Acquisition | Provider and service evaluation |
| SC — System and Communications Protection | Data protection and trust boundaries |
| SI — System and Information Integrity | Input handling, monitoring, integrity |
| SR — Supply Chain Risk Management | Provider, dependency, and component risk |

The presence of a family in this document does not mean every control in that family applies or has been implemented.

---

# AC — Access Control

## AC-2 — Account Management

### Architecture Relevance

A production AI assistant should use the organization's normal identity lifecycle.

This may include:

- Account provisioning
- Role assignment
- Group membership
- Deactivation
- Access review

### Current Prototype

The local prototype uses static synthetic users.

It does not implement enterprise account lifecycle management.

The architecture nevertheless assumes that production access would come from trusted enterprise identity.

---

## AC-3 — Access Enforcement

### Architecture Relevance

Authorization should be enforced before unauthorized information reaches the AI context.

### Current Prototype Evidence

The prototype implements:

- Role checks
- Group checks
- Document approval status
- Document-level allow/deny behavior

The model or response-generation function does not grant access.

### Limitation

The current retrieval implementation selects top candidates before final authorization checks.

A production design should integrate authorization more closely with retrieval.

---

## AC-5 — Separation of Duties

### Architecture Relevance

Important responsibilities should remain separate.

Examples include:

- Platform administration
- Data ownership
- Access approval
- Security review
- Audit access

### Current Prototype Evidence

The synthetic AI System Administrator role does not automatically receive Restricted document access.

This demonstrates the principle:

> Administrative privilege does not equal data entitlement.

---

## AC-6 — Least Privilege

The production architecture should minimize:

- User permissions
- Administrative permissions
- Service permissions
- Retrieval scope
- Tool permissions

The current prototype is advisory and cannot perform production actions.

This significantly limits agency.

---

## AC-16 — Security and Privacy Attributes

Metadata can contribute to authorization decisions.

The prototype uses attributes including:

- Document owner
- Classification
- Allowed roles
- Allowed groups
- Approval status

Additional fields such as review date and expiration date exist as metadata but are not currently enforced.

---

# AU — Audit and Accountability

## AU-2 — Event Logging

The local prototype generates structured event evidence for:

```text
prompt_events.jsonl
retrieval_events.jsonl
access_decisions.jsonl
security_alerts.jsonl
review_events.jsonl
```

These logs capture selected security decisions.

They are not a production audit platform.

---

## AU-3 — Content of Audit Records

Useful fields include:

- Timestamp
- Correlation identifier
- User identifier
- Role
- Prompt-risk category
- Policy action
- Retrieved document
- Denied document
- Authorization result
- Security alert

The exact event schema should follow enterprise logging standards in production.

---

## AU-6 — Audit Record Review

A production organization may analyze AI events for:

- Repeated denied access
- Prompt-injection attempts
- Sensitive-data activity
- Retrieval anomalies
- Administrative changes
- Logging failures

The local prototype creates evidence but does not implement SOC review or enterprise alerting.

---

## AU-8 — Time Stamps

The prototype records timestamps and correlation identifiers.

Production systems should use enterprise time-synchronization and event-correlation standards.

---

## AU-9 — Protection of Audit Information

Production logs may themselves contain sensitive information.

Controls may include:

- Least-privilege log access
- Integrity protection
- Retention rules
- Minimization
- Redaction

The local JSONL files are prototype evidence only and are not equivalent to protected enterprise audit storage.

---

# AT — Awareness and Training

Users of a production AI system should understand:

- Approved uses
- Prohibited uses
- Data-handling expectations
- AI limitations
- Escalation requirements
- Why AI output is not automatically authoritative

Role-specific training may also be needed for:

- Administrators
- Content owners
- Reviewers
- IAM teams
- Security operations

This repository documents those expectations but does not deliver an organizational training program.

---

# CA — Assessment, Authorization, and Monitoring

## CA-2 — Control Assessments

Controls should be evaluated before production use and after significant change.

Relevant areas include:

- Authorization
- Prompt security
- Retrieval behavior
- Logging
- Data handling
- Human accountability
- Provider risk

### Current Evidence

Two scenarios are documented as executed:

1. Authorized policy retrieval — **Pass**
2. Direct prompt injection blocked before retrieval — **Pass**

Other documented tests remain **Not Yet Tested**.

---

## CA-7 — Continuous Monitoring

A production deployment may require monitoring of:

- Prompt abuse
- Authorization failures
- Sensitive-data attempts
- Usage
- Cost
- Configuration changes
- Provider changes
- Logging failures

The current prototype does not implement continuous enterprise monitoring.

---

# CM — Configuration Management

## CM-2 — Baseline Configuration

Security-relevant configuration may include:

- Approved user roles
- Document metadata rules
- Prompt-risk rules
- Retrieval behavior
- Logging
- Provider/model configuration
- Human-review rules

The current repository documents a local prototype baseline and broader production design.

---

## CM-3 — Configuration Change Control

Changes that could alter risk include:

- Prompt-control logic
- Authorization logic
- Retrieval behavior
- Model/provider
- Data sources
- Logging
- User population
- Tool/agent integration

These changes should trigger appropriate review.

---

## CM-6 — Configuration Settings

Examples of security-relevant settings include:

- Deny behavior
- Metadata requirements
- Prompt-risk categories
- Access rules
- Logging fields
- Provider settings

The current prototype hardcodes several of these behaviors.

A production implementation would need formal configuration management.

---

## CM-8 — Component Inventory

A production AI system may include:

- Application
- Identity provider
- Knowledge repositories
- Retrieval service
- Vector store
- Model provider
- Logging platform
- Monitoring platform
- Workflow systems
- Libraries
- Agents or tools

The current prototype contains only a small local subset of this stack.

---

# CP — Contingency Planning

## CP-2 — Contingency Planning

AI should not become the only path to authoritative business information.

If the AI service is unavailable or unsafe, users should be able to return to approved source systems where appropriate.

Potential failure scenarios include:

- Model outage
- Retrieval failure
- Identity failure
- Logging failure
- Provider outage
- Cost threshold exceeded

---

## CP-10 — Recovery

Before restoring a production AI capability after a security issue, the organization may need to validate:

- Identity
- Authorization
- Retrieval
- Logging
- Data sources
- Provider configuration
- Security controls

The current prototype does not implement production recovery procedures.

---

# IA — Identification and Authentication

## IA-2 — Identification and Authentication

Production access should rely on trusted enterprise identity.

Possible mechanisms include:

- SSO
- MFA
- Conditional access
- Trusted identity claims

The current prototype uses synthetic local users.

It does not implement enterprise authentication.

---

## IA-4 — Identifier Management

Production identities should be unique and traceable.

Shared identities should generally be avoided for security-relevant actions.

The prototype uses unique synthetic user IDs for local testing.

---

## IA-5 — Authenticator Management

Credentials should remain outside:

- Prompts
- Documents
- Logs
- Source code
- Model context

The prototype includes simple patterns for selected secret-like values.

This is not a full secrets-management solution.

---

# IR — Incident Response

## IR-4 — Incident Handling

Potential AI-related security scenarios include:

- Prompt injection
- Unauthorized retrieval
- Sensitive-data exposure
- Knowledge-source poisoning
- System-prompt leakage
- Logging failure
- Administrative misconfiguration
- Provider issue

The repository contains an AI incident-response playbook.

It is an architecture artifact, not evidence of an operating enterprise IR program.

---

## IR-5 — Incident Monitoring

Security events may be detected through:

- Application logs
- Authorization events
- Provider telemetry
- IAM telemetry
- SIEM analytics

Only local application evidence exists in the current prototype.

---

## IR-6 — Incident Reporting

Potential stakeholders may include:

- Security Operations
- Security Architecture
- IAM
- Data Owner
- Privacy
- Legal
- Compliance
- Business Owner
- Vendor Risk

The appropriate escalation depends on consequence.

---

## IR-8 — Incident Response Plan

AI-specific response considerations should integrate into the enterprise incident-response process rather than create an isolated security program.

---

# PL — Planning

## PL-2 — System Security and Privacy Planning

This repository contains planning artifacts for:

- Business context
- Architecture
- Data flow
- Trust boundaries
- Access control
- Logging
- Governance
- Human accountability
- Incident response
- Cloud options

These support architecture planning but are not a formal federal System Security Plan.

---

## PL-8 — Security and Privacy Architectures

The project applies:

- Security by design
- Least privilege
- Deny by default
- Data minimization
- Separation of duties
- Source traceability
- Defense in depth
- Human accountability

The local-first implementation reduces exposure while selected controls are validated.

---

# RA — Risk Assessment

## RA-3 — Risk Assessment

AI risk should be evaluated in business context.

Relevant factors include:

- Data sensitivity
- User population
- System authority
- Exposure
- Threat likelihood
- Control maturity
- Business consequence

The project uses qualitative risk analysis rather than additive numeric scoring.

---

## RA-5 — Vulnerability Monitoring and Scanning

A production system may require vulnerability management for:

- Libraries
- Containers
- Infrastructure
- APIs
- Retrieval systems
- Providers

The current prototype does not provide formal vulnerability-management evidence.

---

## RA-7 — Risk Response

Possible treatment choices include:

- Mitigate
- Avoid
- Accept
- Transfer
- Defer
- Redesign
- Escalate

Formal risk acceptance belongs to the authorized organizational risk owner.

---

# SA — System and Services Acquisition

## SA-4 — Acquisition Process

Before adopting a cloud or model provider, an organization may need to review:

- Data handling
- Retention
- Training use
- Security controls
- Identity integration
- Auditability
- Data residency
- Incident notification
- Exit strategy
- Cost

The current project does not use an external AI provider.

---

## SA-9 — External System Services

AWS Bedrock and Azure OpenAI are represented only as reference architectures.

No cloud AI service is deployed.

Any real provider would require organization-specific review.

---

## SA-10 — Developer Configuration Management

The local prototype is maintained in source control and includes:

- Code
- Configuration
- Metadata
- Test definitions
- Documentation

The repository should avoid committed credentials or sensitive data.

---

## SA-11 — Developer Testing and Evaluation

The project contains test definitions for:

- Prompt injection
- Access control
- Sensitive-data handling

Only two initial scenarios are currently documented as executed.

Defined tests should not be presented as successful until run.

---

# SC — System and Communications Protection

## SC-7 — Boundary Protection

Important production trust boundaries include:

- User → Application
- Application → Identity
- Application → Retrieval
- Retrieval → Knowledge Source
- Application → Model Provider
- Application → Logging
- Administrator → Configuration

The model itself is not treated as a trusted enforcement boundary.

---

## SC-8 — Transmission Confidentiality and Integrity

Future external or cloud deployments should protect information in transit.

This may include:

- TLS
- Private connectivity
- Protected API calls
- Controlled egress

The local prototype does not send data to an external model provider.

---

## SC-12 / SC-13 — Cryptographic Protection

A production environment may use:

- KMS
- Key Vault
- Enterprise secrets management
- Platform encryption

The project documents these as production architecture considerations.

It does not implement cloud key-management controls.

---

## SC-28 — Protection of Information at Rest

Production controls should protect:

- Documents
- Logs
- Configuration
- Retrieval data
- Review records

The current prototype avoids real sensitive data, substantially reducing the consequence of local storage exposure.

---

# SI — System and Information Integrity

## SI-3 — Malicious Code Protection

A production implementation should evaluate:

- Dependencies
- Document parsers
- Plugins
- Containers
- Generated code
- Tool integrations

The current architecture does not permit autonomous execution of AI-generated commands.

---

## SI-4 — System Monitoring

Production monitoring may detect:

- Prompt injection
- Authorization failures
- Sensitive-data activity
- Retrieval anomalies
- Provider issues
- Configuration changes

The current prototype produces local logs only.

---

## SI-10 — Information Input Validation

User prompts and retrieved content should be treated as untrusted input.

The local prototype implements selected pattern-based prompt checks.

It does not implement:

- Semantic injection detection
- Indirect prompt-injection defense
- Production document scanning

Therefore the current evidence is limited.

---

## SI-12 — Information Management and Retention

Production environments should define retention for:

- Logs
- Prompts
- Responses
- Review records
- Provider records
- Knowledge sources

The local prototype does not implement formal retention enforcement.

---

# SR — Supply Chain Risk Management

## SR-3 — Supply Chain Controls

AI architectures may depend on:

- Model providers
- Cloud providers
- Open-source packages
- Retrieval platforms
- Document parsers
- Agent frameworks
- Plugins

A production implementation should identify and assess these dependencies.

---

## SR-5 — Acquisition Strategy

The architecture intentionally compares multiple possible deployment patterns rather than assuming cloud AI is automatically required.

Possible approaches include:

- Local security-control validation
- Local model
- Managed cloud model
- Private deployment
- SaaS AI

The selection should follow business need and risk.

---

## SR-6 — Supplier Assessment

Potential review topics include:

- Data retention
- Training use
- Data residency
- Security certifications
- Logging capability
- Incident notification
- Access control
- Administrative functions
- Exit strategy

These are production supplier-governance requirements.

---

# AI-Specific Risk Mapping

| AI Risk | Relevant NIST Areas | Architecture Response |
| --- | --- | --- |
| Prompt injection | SI, AU, RA | Prompt evaluation plus independent authorization |
| Sensitive information disclosure | AC, SC, AU | Classification, authorization, minimization |
| Unauthorized retrieval | AC, AU | Document-level authorization |
| System-prompt leakage | SI, SC | Keep critical security outside prompt secrecy |
| Misinformation | RA, CA | Source grounding and human authority |
| Excessive agency | AC, CM | Advisory design and explicit action authorization |
| Knowledge poisoning | CM, SI, RA | Approved sources and untrusted-content handling |
| Weak auditability | AU | Structured event evidence |
| Vendor exposure | SA, SR, SC | Provider review |
| Cost growth | CA, CM | Usage and deployment controls |

This table shows conceptual alignment.

It does not claim that every control is implemented.

# Current Prototype Evidence

| Area | Evidence |
| --- | --- |
| Identity context | Synthetic user records |
| Access enforcement | Role/group authorization |
| Data attributes | Document metadata |
| Prompt security | Pattern-based prompt-risk logic |
| Sensitive-data handling | Selected pattern detection |
| Retrieval | Local keyword retrieval |
| Logging | Five JSONL evidence types |
| Security alerts | High-risk event logging |
| Human oversight | Simulated review trigger |
| Data protection | Synthetic data only |
| External provider risk | No external provider used |
| Cloud cost | No cloud AI deployment |

# Validated Scenarios

## Authorized Retrieval

A mock General Employee requested the approved synthetic AI policy.

**Result: Pass**

## Direct Prompt Injection

A mock General Employee attempted to override controls and reveal Restricted documents.

The request was blocked before retrieval.

**Result: Pass**

Other test scenarios remain **Not Yet Tested**.

# Production Controls Not Demonstrated

The project does not currently provide evidence for:

- Enterprise account lifecycle
- SSO
- MFA
- PAM
- Production SIEM
- Continuous monitoring
- Formal access reviews
- Production incident response
- Enterprise change management
- Production backups
- Production resilience
- Supplier assessments
- Production DLP
- Formal retention enforcement
- Cloud encryption controls
- Vector security
- Embedding security
- Production LLM output validation
- Autonomous-agent controls

# Control Ownership

Actual ownership belongs to the organization implementing the system.

Illustrative examples include:

| Area | Possible Owner |
| --- | --- |
| Identity and access | IAM Team |
| Data classification | Data Owner |
| Security architecture | Security Architecture |
| Logging and monitoring | Security Operations |
| Incident response | Incident Response / SOC |
| Provider risk | Vendor Risk |
| Privacy | Privacy / Legal |
| Cloud platform | Platform Team |
| Cost | FinOps / Platform Owner |
| Risk acceptance | Authorized Risk Owner |

These are not formal assignments made by the portfolio project.

# Relationship to Formal NIST 800-53 Assessment

A formal NIST SP 800-53 implementation would require substantially more evidence than this repository provides.

Depending on organizational context, that may include:

- Control selection
- Baseline tailoring
- Control implementation statements
- System boundary definition
- Security/privacy plans
- Control assessments
- Evidence
- POA&M management
- Authorization decisions
- Continuous monitoring
- Organizational policies

Those activities are outside the scope of this portfolio project.

# Security Architect Perspective

The value of this mapping is not that AI requires an entirely new security-control universe.

Many AI risks are new expressions of familiar control failures.

For example:

```text
Prompt Injection
        ↓
Attempts to influence behavior
        ↓
Authorization still applies
```

```text
Semantic Retrieval
        ↓
Finds relevant content
        ↓
Access Control still applies
```

```text
AI Recommendation
        ↓
May influence a decision
        ↓
Human authority still applies
```

That is why traditional security architecture remains central.

AI changes the interface and attack paths.

It does not remove the need for:

- Identity
- Least privilege
- Segregation of duties
- Logging
- Change control
- Incident response
- Risk management
- Supply-chain governance
- Resilience

# Conclusion

This architecture maps naturally to selected NIST SP 800-53 control families because AI is still part of an enterprise information system.

The local prototype provides evidence for only a small subset of those security concepts.

It does not constitute a formal NIST 800-53 control implementation or authorization package.

The current progression is:

```text
Architecture and Governance
        ↓
Local Security-Control Prototype
        ↓
Selected Control Validation
        ↓
Cloud Reference Architectures
```

The key architecture principle remains:

> Apply AI-specific defenses without allowing AI to bypass established enterprise security controls.
