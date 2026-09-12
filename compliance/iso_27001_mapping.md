# ISO/IEC 27001 Security Control Mapping

## Purpose

This document maps the enterprise AI security architecture in this repository to selected ISO/IEC 27001 information-security control themes.

The purpose is to show how AI security can fit within an existing enterprise information-security management approach rather than being treated as a separate or model-only security problem.

This document is an **architecture alignment**.

> It is not an ISO/IEC 27001 certification assessment, audit, Statement of Applicability, or claim that the organization has implemented every referenced control.

The mapping distinguishes between:

1. Security and governance requirements defined by the architecture.
2. Controls demonstrated by the local prototype.
3. Controls that would require production implementation.

# Project Context

The production concept is an internal AI assistant that could eventually use Retrieval-Augmented Generation to help employees access approved enterprise information.

The current project has progressed through:

```text
Architecture and Governance
        ↓
Local Security-Control Prototype
        ↓
Selected Control Validation
```

The current prototype uses:

- Synthetic users
- Synthetic documents
- Mock roles and groups
- Document metadata
- Simple keyword retrieval
- Pattern-based prompt-risk evaluation
- Document authorization
- Local JSONL logging
- Advisory response generation
- Simulated human-review triggers

It does not use:

- Production LLM
- Embeddings
- Vector database
- Enterprise identity provider
- Production SIEM
- Cloud AI
- External model API
- Formal approval workflow
- Real enterprise data
- Autonomous agents

# Core Security Principle

> The AI model is not the security authority.

Security decisions should remain anchored in:

- Identity
- Authorization
- Data classification
- Application logic
- Governance
- Logging
- Monitoring
- Change control
- Incident response
- Human accountability

# ISO 27001 Alignment Summary

| Security Theme | Project Alignment |
| --- | --- |
| Information-security governance | AI use-case intake, risk assessment, ownership, architecture decisions |
| Roles and responsibilities | Business, technical, security, data, and operational accountability |
| Asset management | Documents, metadata, prompts, logs, configuration, model/provider context |
| Information classification | Classification and document metadata |
| Access control | Role/group authorization and document-level access |
| Supplier security | Cloud/model/provider evaluation before production use |
| Incident management | AI-specific incident scenarios and evidence requirements |
| Secure development | Security requirements defined before production implementation |
| Logging and monitoring | Structured evidence and production monitoring design |
| Change management | Reassessment when model, data, provider, permissions, or architecture changes |
| Communications security | Protected production data flows and provider boundaries |
| Data protection | Minimization, classification, authorization, and sensitive-data controls |

# Organizational Controls

## Information Security Policies

### Relevance

An enterprise AI capability needs documented expectations for:

- Acceptable use
- Prohibited use
- Data handling
- Access
- Logging
- Human accountability
- Provider use
- Incident response

### Project Alignment

The repository includes architecture artifacts addressing:

- AI use-case intake
- Data classification
- Human-review requirements
- Prompt-injection controls
- Logging and monitoring
- Cost controls
- Risk assessment

These are design artifacts.

They should not be confused with formally approved organizational policies.

# Roles and Responsibilities

## Relevance

Responsibility cannot be delegated to the AI model.

Production ownership may include:

- Business owner
- Technical owner
- Security owner
- Data owner
- IAM owner
- Compliance or privacy owner
- Platform owner
- Incident-response owner

## Architecture Principle

Different responsibilities should remain separated.

For example:

> Operating the AI platform should not automatically grant entitlement to all enterprise content.

# Segregation of Duties

Relevant separations may include:

- Platform administration vs. content access
- Content ownership vs. access approval
- Security design vs. risk acceptance
- AI recommendation vs. business approval
- Operational administration vs. audit review

The local prototype demonstrates one part of this principle by defining an AI System Administrator role that does not automatically receive all document access.

# Information Security in Project Management

The project intentionally follows:

```text
Business Problem
      ↓
Governance
      ↓
Architecture
      ↓
Threat Analysis
      ↓
Control Design
      ↓
Local Validation
```

This supports security-by-design rather than adding security after implementation.

# Asset and Information Management

## Relevant Assets

A production AI architecture may need to protect:

- Enterprise documents
- Document metadata
- User prompts
- Retrieved context
- Model responses
- Logs
- Access policies
- System configuration
- Model/provider configuration
- Retrieval indexes
- Review records

Not all of these exist in the local prototype.

## Information Classification

The project uses classification as one input to security decisions.

The production concept may use classifications such as:

- Public
- Internal
- Confidential
- Restricted
- Regulated
- Secrets

The local prototype uses synthetic documents labeled:

- Internal
- Confidential
- Restricted

These are synthetic labels used to exercise the control model.

No real Restricted enterprise data is included.

## Classification Is Not Authorization

Classification indicates sensitivity.

It does not automatically grant or deny access.

The system should still evaluate:

- User identity
- Role
- Group
- Document entitlement
- Approval status
- Source policy

A relevant document is not necessarily an authorized document.

# Information Labelling

Production metadata may include:

- Document ID
- Owner
- Classification
- Allowed roles
- Allowed groups
- Source
- Status
- Version
- Review date
- Expiration date

The local prototype stores selected metadata.

However:

> A metadata field is not an enforced control unless application logic actually uses it.

For example, review and expiration dates currently exist as metadata but are not enforced by the prototype.

# Acceptable Use

A production policy may prohibit or restrict:

- Customer information
- Employee records
- Payment information
- Secrets
- Credentials
- Private keys
- Unapproved confidential information
- Requests to bypass controls

The local prototype includes basic pattern detection for selected secret and sensitive-data terms.

This is not equivalent to enterprise DLP.

# Information Transfer

The local prototype is local-only and does not send prompts or enterprise information to an external AI provider.

A future cloud or external-model implementation would require review of:

- Data handling
- Encryption
- Retention
- Model-provider behavior
- Data residency
- Logging
- Contractual obligations

# Access Control

## Identity Management

Production access should rely on trusted enterprise identity such as:

- Enterprise SSO
- MFA where required
- Trusted user attributes
- Role/group membership
- Identity lifecycle management

The local prototype does not implement enterprise authentication.

It uses predefined synthetic identities.

## Access Rights

The local prototype implements document-level authorization using:

- Role matching
- Group matching
- Document approval status
- Required metadata

Authorization occurs outside the response-generation logic.

This supports the architecture principle:

> The model cannot grant access.

## Privileged Access

Production administrative access should use:

- Least privilege
- Strong authentication
- Privileged-access governance
- Logging
- Periodic review
- Separation from content entitlement

These are production requirements, not controls currently demonstrated by the local prototype.

## Restriction of Access to Information

The local prototype demonstrates:

- Synthetic classification labels
- Document-level role/group permissions
- Deny behavior for unauthorized content
- Separation of system administration and content entitlement

It does not implement:

- Enterprise repository permissions
- Production IAM lifecycle
- Production response filtering
- Formal Restricted-data approval workflow

# Supplier and Vendor Security

## Relevance

Production AI platforms may introduce dependencies on:

- Cloud providers
- Model providers
- SaaS platforms
- Open-source libraries
- Retrieval platforms
- Embedding models
- Document-processing libraries

## Production Review Areas

A supplier assessment may need to evaluate:

- Prompt retention
- Response retention
- Training use
- Data residency
- Access control
- Incident notification
- Audit support
- Deletion
- Service availability
- Contract terms
- Exit strategy
- Cost

The local prototype intentionally avoids third-party AI providers.

# ICT Supply Chain

The prototype still depends on local software and Python packages, so ordinary software supply-chain risk remains.

A production implementation would need to consider:

- Approved package sources
- Dependency scanning
- Version management
- Vulnerability management
- Model provenance
- Artifact integrity
- SBOM where appropriate
- Provider change management

No broad AI supply-chain control implementation is claimed by this project.

# Incident Management

## AI-Specific Scenarios

A production organization should be prepared to investigate:

- Prompt injection
- Unauthorized retrieval
- Sensitive-data exposure
- Knowledge-source poisoning
- System-prompt leakage
- Administrative misconfiguration
- Logging failure
- Model/provider incident
- Excessive usage
- Agent/tool misuse if later introduced

## Incident Response Process

AI incidents should generally integrate with the existing enterprise incident-response process:

```text
Detection
   ↓
Triage
   ↓
Containment
   ↓
Investigation
   ↓
Recovery
   ↓
Lessons Learned
```

The repository contains an AI-specific incident-response playbook as an architecture artifact.

It is not evidence of a deployed incident-management capability.

# Event Assessment

Not every unusual AI event is automatically a security incident.

For example:

- A blocked injection attempt may simply be a security event.
- Unauthorized retrieval that succeeds may represent an incident.
- Sensitive information reaching an external provider may require escalation.
- A malformed prompt may have no security consequence.

Severity should follow enterprise incident criteria and actual consequence.

# Evidence

Useful evidence may include:

- User identifier
- Timestamp
- Correlation ID
- Prompt metadata
- Risk category
- Retrieval decision
- Document ID
- Authorization result
- Security alert
- Administrative changes
- Model/provider information

The local prototype currently produces five JSONL evidence streams:

```text
prompt_events.jsonl
retrieval_events.jsonl
access_decisions.jsonl
security_alerts.jsonl
review_events.jsonl
```

This is local implementation evidence, not a production SIEM.

# Operational Security

## Logging

The local prototype implements structured local logging for:

- Prompt evaluation
- Retrieval
- Authorization
- Security alerts
- Simulated review triggers

It does not log:

- Enterprise authentication events
- Production model telemetry
- Administrative cloud changes
- Provider telemetry
- Production SIEM events

Those remain production requirements.

# Monitoring

The architecture identifies possible monitoring use cases such as:

- Prompt-injection activity
- Repeated authorization denial
- Sensitive-data submission
- Retrieval anomalies
- Administrative changes
- Logging failures
- Usage anomalies
- Cost anomalies

The local prototype does not implement an enterprise monitoring platform.

# Clock and Event Correlation

The prototype uses timestamps and correlation identifiers for local events.

A production environment should use the organization's standard time synchronization and event-correlation mechanisms.

# Capacity and Availability

AI systems can introduce:

- Request spikes
- Token consumption
- Retrieval load
- Logging volume
- Provider throttling
- Cost growth

The current prototype is local and low-cost.

It does not implement:

- Rate limiting
- Quotas
- Production capacity monitoring
- Production SLOs
- Cloud cost alerts

# Change Management

Changes that may materially alter risk include:

- New model
- New provider
- New user population
- New data source
- New classification
- Retrieval changes
- Authorization changes
- Prompt/control changes
- Logging changes
- Agent/tool introduction
- Production deployment

These changes should trigger appropriate reassessment.

# Secure Development

## Security Requirements

The local prototype was built to exercise selected security-control behavior including:

- Prompt-risk evaluation
- Document authorization
- Sensitive-pattern matching
- Structured logging
- Synthetic data
- Advisory responses
- Simulated review events

## Prototype Limitations

It does not implement:

- Full SDLC security program
- SAST
- DAST
- SCA evidence
- Production secrets management
- Enterprise CI/CD
- Formal code review
- Production release controls

Those are outside the scope of this repository.

## Security Testing

The project contains test cases for:

- Prompt injection
- Access control
- Sensitive-data handling

Two initial scenarios are documented as executed:

1. Authorized policy retrieval — **Pass**
2. Direct prompt injection blocked before retrieval — **Pass**

Other documented cases remain **Not Yet Tested**.

# Secure Architecture Principles

The project consistently applies:

- Security by design
- Least privilege
- Deny by default
- Separation of duties
- Data minimization
- Source traceability
- Defense in depth
- Human accountability
- Local-first validation

Most importantly:

> The model does not become the control authority.

# Communications Security

The local prototype does not involve an external model-provider network path.

A production design should evaluate:

- TLS
- Private connectivity where appropriate
- Public exposure
- Egress control
- API security
- Provider connectivity
- DNS
- Existing enterprise network controls

These are production architecture considerations.

# Data Protection

## Sensitive Data

The project avoids real sensitive information.

The local prototype uses synthetic content only.

It includes pattern-based detection for selected sensitive terms and secret-like values.

This is not equivalent to:

- Enterprise DLP
- Tokenization
- Formal data masking
- Production redaction service

## Data Leakage Risk

A production AI architecture may leak data through:

```text
Prompt
  ↓
Retrieval
  ↓
Context
  ↓
Model / Provider
  ↓
Response
  ↓
Logs
```

Control therefore requires multiple layers:

- Classification
- Authorization
- Minimization
- Provider review
- Logging controls
- Response controls

# Human Accountability

Human authority should be based primarily on the consequence of the decision or action.

Examples may include:

- Access approval
- Security exception
- Production change
- Legal interpretation
- Regulatory decision
- High-impact business decision

Classification alone should not automatically require human approval for every informational request.

The local prototype includes a simulated review trigger.

It does not implement a real approval gate.

# AI-Specific Risk Mapping

| AI Risk | Relevant ISO 27001 Theme | Architecture Response |
| --- | --- | --- |
| Prompt injection | Threat management, secure development, monitoring | Prompt controls plus independent authorization |
| Sensitive information disclosure | Classification, access control, data protection | Classification, authorization, minimization |
| Unauthorized retrieval | Access control | Document-level authorization |
| System-prompt leakage | Secure development, information protection | Keep critical policy outside prompt |
| Knowledge poisoning | Change management, asset management | Approved sources and content governance |
| Misinformation | Governance, review, secure operation | Source support and human authority |
| Excessive agency | Least privilege, segregation of duties | Advisory design and explicit action authority |
| Weak auditability | Logging and evidence | Structured event logging |
| Provider exposure | Supplier security | Provider review |
| Cost growth | Capacity and operations | Usage and cost controls |
| Secrets exposure | Credential protection, data leakage controls | Detection, blocking, secrets management |

# Prototype Evidence

The current local prototype demonstrates selected behaviors relevant to ISO 27001 themes:

| Area | Evidence |
| --- | --- |
| Synthetic identity context | Mock users and roles |
| Access control | Role/group document authorization |
| Data classification | Synthetic document metadata |
| Prompt security | Pattern-based evaluation |
| Secrets protection | Selected sensitive-pattern blocking |
| Logging | Five JSONL event types |
| Security alerts | High-risk events logged |
| Human accountability | Simulated review trigger |
| Data minimization | No real enterprise data |
| Cost control | No cloud AI deployment |

This does **not** establish ISO 27001 compliance.

# Production Controls Not Demonstrated

The project does not currently provide implementation evidence for:

- Enterprise SSO
- MFA
- PAM
- Production IAM lifecycle
- Enterprise DLP
- SIEM
- Centralized immutable logging
- Formal supplier assessment
- Formal compliance audit
- Production incident response
- Production change management
- Production backup/recovery
- Cloud resilience
- Production LLM output controls
- Vector security
- Embedding security
- Agent/tool controls

# Control Ownership

Actual ownership belongs to the organization implementing the architecture.

Typical examples may include:

| Area | Possible Owner |
| --- | --- |
| Business use case | Business Owner |
| Data classification | Data Owner |
| Identity | IAM Team |
| Security architecture | Security Architecture |
| Monitoring | Security Operations |
| Incident response | Incident Response / SOC |
| Supplier review | Vendor Risk |
| Privacy | Privacy / Legal |
| Cloud platform | Platform Team |
| Cost | FinOps / Platform Owner |
| Risk acceptance | Authorized Business / Risk Owner |

These are illustrative rather than assignments made by this portfolio project.

# Relationship to ISO 27001

ISO 27001 operates at the organizational information-security management level.

This project demonstrates how AI security architecture can fit within that environment.

A formal ISO 27001 assessment would require broader evidence including:

- Defined organizational scope
- Information-security policies
- Risk methodology
- Statement of Applicability
- Implemented controls
- Operational evidence
- Internal audits
- Management review
- Corrective actions
- Formal accountability

Those activities are outside this project's scope.

# Security Architect Perspective

The useful lesson from this mapping is that AI does not replace established security disciplines.

It creates new paths through them.

For example:

```text
User
   ↓
Identity
   ↓
AI Interface
   ↓
Retrieval
   ↓
Enterprise Information
   ↓
Model
   ↓
Response
```

At every point, existing security concepts still matter:

- Identity
- Least privilege
- Classification
- Change management
- Supplier risk
- Logging
- Incident response
- Secure development
- Human accountability

The architecture challenge is to make sure AI does not create a shortcut around those controls.

# Conclusion

The enterprise AI security architecture aligns with selected ISO/IEC 27001 information-security themes through:

- Governance
- Ownership
- Data classification
- Access control
- Supplier risk
- Logging
- Incident response
- Secure development
- Change management
- Data protection

The local prototype provides evidence for only a limited subset of those controls.

It does not establish formal ISO 27001 compliance or certification.

The current project progression is:

```text
Architecture and Governance
        ↓
Local Security-Control Prototype
        ↓
Selected Control Validation
```

The broader production architecture shows how additional ISO-aligned enterprise controls would surround a real AI/RAG implementation.

The key design principle remains:

> AI should fit inside the enterprise security management system rather than becoming an exception to it.
