# AI Security Governance & RAG Risk Architecture

## Project Overview

This project demonstrates how I would approach the security architecture and governance of an internal enterprise AI assistant in a regulated environment.

The scenario assumes an organization wants employees to use AI to find and understand approved internal information without creating a new path around existing identity, authorization, data-governance, logging, and risk-management controls.

The project combines:

- Business and governance analysis
- AI security architecture
- RAG security design
- Identity and document-level authorization
- Prompt-injection controls
- Threat and risk analysis
- Human accountability
- Logging and incident-response design
- Compliance-framework mapping
- A local security-control prototype
- AWS and Azure reference architectures

The project is intentionally **local-first and architecture-led**.

No production AI platform or paid cloud AI service is required.

---

# Scope Note

This repository contains both **architecture artifacts** and an **implemented local security-control prototype**.

The project progression is:

```text
Architecture and Governance
        ↓
Local Security-Control Prototype
        ↓
Selected Control Validation
        ↓
Cloud Reference Architectures
```

The local prototype validates selected security-control concepts.

It is **not** a production RAG implementation.

The project does not currently use:

- Production LLM
- Embeddings
- Vector database
- Enterprise identity provider
- Production SIEM
- Cloud AI
- External model provider
- Production human-review workflow
- Real enterprise data
- Autonomous agents

AWS Bedrock and Azure OpenAI are included only as **design/reference architectures**.

---

# Business Problem

Enterprise AI assistants can create a deceptively simple user experience:

```text
User
  ↓
Question
  ↓
AI
  ↓
Answer
```

The security architecture underneath that experience is much more complicated.

The system still needs to answer questions such as:

- Who is the user?
- What is the user allowed to access?
- Which documents are approved for AI use?
- What happens when relevant content is not authorized?
- Can retrieved content manipulate the AI?
- What happens when the user attempts to bypass controls?
- What evidence is generated?
- When is accountable human authority required?
- What happens when a control fails?

The central architecture question became:

> What is the AI allowed to know, what is the user allowed to know, and where is that decision actually enforced?

---

# Architecture Principle

The primary design principle for this project is:

> The AI assistant should not create a new path around existing enterprise authorization and data-governance boundaries.

The model should not become the authority for:

- Identity
- Access
- Data entitlement
- Risk acceptance
- Security policy
- Business approval
- Compliance interpretation
- Production action

Those decisions should remain outside the model.

---

# Production Reference Architecture

A production implementation could follow a flow similar to:

```text
User
  ↓
Enterprise Identity
  ↓
Application / API
  ↓
Prompt Risk Evaluation
  ↓
Authorization Context
  ↓
Permission-Aware Retrieval
  ↓
Approved Knowledge Sources
  ↓
Authorized + Minimized Context
  ↓
LLM
  ↓
Response Controls
  ↓
User
```

Security evidence should be generated throughout the flow.

The model receives only the context required to answer the authorized request.

---

# Identity and Authorization

One of the most important decisions in the architecture is that retrieval relevance does not equal authorization.

A document can be highly relevant to a question and still be unavailable to the user.

The intended decision is closer to:

```text
Relevant?
   +
Approved?
   +
User Authorized?
        ↓
Eligible for Context
```

The model should never decide whether the user is entitled to the document.

Another important principle is:

> Platform administration does not automatically grant access to enterprise content.

The prototype reflects this by separating AI system administration from Restricted document entitlement.

---

# Data Governance

Enterprise AI depends heavily on the quality and governance of the information supplied to it.

Possible document attributes include:

- Owner
- Classification
- Approval status
- Allowed roles
- Allowed groups
- Version
- Review date
- Expiration date

The local prototype uses synthetic document metadata to demonstrate selected authorization decisions.

Not every metadata field is currently enforced.

For example, review and expiration dates are represented but are not enforced by the application.

Classification also does not grant access by itself.

---

# Prompt and Context Security

Prompts and retrieved content are treated as untrusted input.

The architecture considers:

- Direct prompt injection
- Attempts to bypass access controls
- Requests for Restricted information
- Sensitive-data patterns
- System-prompt extraction
- Indirect prompt injection
- Poisoned knowledge sources

The current prototype implements simple pattern-based detection for selected direct prompt-injection and sensitive-data scenarios.

It does not implement semantic injection detection or dedicated indirect prompt-injection defense.

A critical design principle is:

> Prompt controls can reduce malicious input, but authorization must still operate independently.

---

# Human Accountability

Human review should be based on the consequence of the decision or action rather than simply the presence of AI or a particular document classification.

Examples that may require accountable human authority include:

- Access approval
- Security exceptions
- Production changes
- Legal decisions
- Regulatory decisions
- Material business decisions

The local prototype can generate a simulated review event for selected document metadata.

It does not implement a human approval gate.

The response continues after the simulated review event.

Therefore:

> The prototype demonstrates a human-review trigger, not a human-review approval workflow.

---

# Local Security-Control Prototype

The implemented prototype is located under:

```text
Phase_2/local_prototype/
```

It uses:

- Python
- Synthetic users
- Synthetic roles and groups
- Synthetic documents
- JSON metadata
- Local keyword retrieval
- Pattern-based prompt-risk evaluation
- Role/group authorization
- JSONL logging
- Advisory response generation

No production LLM is used.

The purpose of the prototype is not to demonstrate AI application development.

It is to validate where selected security decisions occur in the request path.

---

# Prototype Request Flow

The implemented local flow is approximately:

```text
Mock User
    ↓
Prompt Risk Evaluation
    ↓
Block / Evaluate / Allow
    ↓
Local Retrieval
    ↓
Document Authorization
    ↓
Logging
    ↓
Simulated Review Trigger if Applicable
    ↓
Advisory Response
```

For configured blocking conditions, the request stops before retrieval.

---

# Current Control Evidence

The prototype currently demonstrates:

- Mock identity and role context
- Role/group authorization
- Document metadata
- Approved-document checks
- Pattern-based prompt-risk evaluation
- Selected sensitive-pattern detection
- Block-before-retrieval behavior
- Local retrieval
- Access-decision logging
- Retrieval logging
- Security-alert generation
- Simulated human-review events
- Advisory-only responses

The prototype writes:

```text
prompt_events.jsonl
retrieval_events.jsonl
access_decisions.jsonl
security_alerts.jsonl
review_events.jsonl
```

These logs provide local control evidence.

They are not a production SIEM or forensic logging platform.

---

# Validated Scenarios

Two initial scenarios are currently documented as executed.

## 1. Authorized Policy Retrieval

A mock General Employee requested the approved synthetic AI acceptable-use policy.

The request was authorized and processed.

**Result: Pass**

## 2. Direct Prompt Injection

A mock General Employee attempted to override controls and reveal Restricted documents.

The request was detected and blocked before retrieval.

**Result: Pass**

Additional test cases exist for:

- Prompt injection
- Access control
- Sensitive-data handling

Those scenarios should remain **Not Yet Tested** until they are actually executed.

---

# Known Prototype Limitations

The local implementation intentionally remains small.

Current limitations include:

- No production LLM
- No embeddings
- No vector database
- No semantic retrieval
- No enterprise SSO
- No MFA
- No production DLP
- No SIEM integration
- No cloud deployment
- No provider telemetry
- No production human-review workflow
- No autonomous actions
- No production incident-response automation

The current retrieval logic also selects candidate documents before final authorization filtering.

A production implementation should evaluate authorization-aware retrieval more closely so unauthorized candidates do not unnecessarily consume the retrieval window.

---

# Threat Modeling

The project uses STRIDE and AI-specific threat analysis to evaluate risks such as:

- Spoofed identity
- Unauthorized retrieval
- Prompt injection
- Sensitive-data disclosure
- Knowledge-source poisoning
- Logging failure
- Administrative misuse
- Excessive agency
- Provider exposure

The model itself is not treated as a security boundary.

---

# OWASP LLM Security

The project maps the architecture to relevant OWASP LLM risk areas.

The mapping distinguishes between:

- Risks relevant to a future production AI system
- Controls represented in the architecture
- Controls demonstrated by the local prototype
- Risks that cannot yet be validated because no production LLM exists

This prevents design controls from being presented as implemented production controls.

---

# AI Risk Management

AI risk is evaluated qualitatively using factors such as:

- Business consequence
- Data sensitivity
- User population
- System authority
- Exposure
- Threat likelihood
- Control effectiveness
- Residual risk

The project avoids additive numerical scoring that could create false precision.

Possible treatment decisions include:

- Mitigate
- Avoid
- Accept
- Transfer
- Defer
- Redesign
- Escalate

Formal risk acceptance belongs to the authorized organizational risk owner.

---

# Logging and Monitoring

A production AI system may need visibility into:

- Prompt abuse
- Authorization failures
- Retrieval activity
- Sensitive-data attempts
- Provider behavior
- Administrative changes
- Model activity
- Logging failures
- Usage anomalies
- Cost anomalies

The current prototype provides only local application-level evidence.

Production monitoring platforms are architecture considerations rather than deployed components.

---

# Incident Response

The project includes an AI-specific incident-response playbook covering scenarios such as:

- Prompt injection
- Unauthorized retrieval
- Sensitive-data exposure
- Knowledge-source poisoning
- System-prompt exposure
- Unsafe AI output
- Logging failure
- Provider failure
- Excessive agency

A key distinction is made between a security event and an incident.

For example:

> A blocked prompt-injection attempt can demonstrate that a control operated successfully. A successful bypass with meaningful impact may require incident response.

The playbook extends normal enterprise incident response rather than replacing it with a separate AI process.

---

# Governance and Compliance Alignment

The project includes architecture mappings to:

- NIST AI Risk Management Framework
- NIST SP 800-53
- ISO/IEC 27001
- ISO/IEC 42001
- OWASP LLM security risks

These mappings demonstrate architectural alignment.

They do not represent:

- Certification
- Formal compliance
- Authorization
- Audit completion
- An implemented ISMS
- An implemented AIMS

---

# Cloud Reference Architectures

The repository includes design-only reference architectures for:

## AWS Bedrock

The AWS reference explores how the architecture could map to AWS services while keeping authorization and security decisions outside the model.

## Azure OpenAI

The Azure reference explores the same architecture principles using Microsoft Azure services.

Neither environment has been deployed as part of this project.

The cloud references exist to demonstrate that the security architecture can remain consistent even when the implementation platform changes.

---

# Cost Strategy

The current project is intentionally local-first.

Current cloud AI cost:

```text
$0
```

This allows architecture and selected security controls to be evaluated before introducing:

- Managed LLM cost
- Vector database cost
- Search/indexing cost
- Logging cost
- Network cost
- Long-running cloud infrastructure

Cloud deployment should follow a demonstrated technical or business need rather than being required merely to make the architecture credible.

---

# Repository Structure

```text
ai-security-rag-governance-architecture/
│
├── README.md
├── Architecture_Dataflow.md
├── Business_Case.md
├── Cost_Controls.md
├── Reference_Architecture.md
├── lessonslearned.md
├── project_status.md
│
├── Governance/
│   ├── Data_Classification.md
│   ├── ai_use_case_intake.md
│   └── human_review_requirements.md
│
├── Security/
│   ├── access_control_model.md
│   ├── ai_risk_assessment.md
│   ├── logging_monitoring.md
│   ├── nist_ai_rmf_mapping.md
│   ├── owasp_llm_top10_mapping.md
│   ├── prompt_injection_controls.md
│   └── threat_model_stride.md
│
├── architecture/
│   ├── deployment_options.md
│   └── trust_boundaries.md
│
├── cloud_reference_only/
│   ├── aws_bedrock_design_only.md
│   └── azure_openai_design_only.md
│
├── compliance/
│   ├── iso_27001_mapping.md
│   ├── iso_42001.md
│   └── nist_800_53_mapping.md
│
├── incident_response/
│   └── ai_incident_response_playbook.md
│
└── Phase_2/
    ├── README.md
    └── local_prototype/
        ├── app.py
        ├── prototype_results.md
        ├── readme_runbook.md
        ├── requirements.txt
        ├── sample_users.json
        ├── metadata/
        ├── sample_docs/
        ├── logs/
        └── tests/
```

---

# Key Architecture Decisions

Several decisions shaped the project.

## Keep Security Authority Outside the Model

Identity, authorization, approval, and risk decisions should not depend on the LLM following instructions.

## Validate Locally Before Paying for Cloud

The first technical implementation validates security-control placement rather than cloud deployment.

## Treat Retrieved Content as Untrusted

Documents can contain malicious or misleading instructions.

Retrieval does not make content trustworthy.

## Separate Relevance from Authorization

A relevant document is not necessarily an authorized document.

## Keep AI Advisory

The current architecture does not give AI production decision authority.

## Preserve Evidence

Security decisions should generate enough evidence to reconstruct what happened.

---

# What I Would Evaluate Next

If this architecture moved toward production, I would evaluate:

- Enterprise identity integration
- Authorization-aware retrieval
- Production RAG platform
- Embedding and vector security
- Knowledge-source ingestion controls
- Indirect prompt-injection defense
- Production LLM behavior
- Response validation
- Enterprise logging and SIEM integration
- Provider security and data handling
- Human approval workflow where business consequence requires it
- Resilience and fallback
- Cost controls
- Agent and tool authorization if actions are introduced

Those are production design decisions rather than missing requirements for the current portfolio project.

---

# What This Project Demonstrates

This project is intended to demonstrate how I approach an AI security architecture problem:

```text
Business Problem
      ↓
Risk
      ↓
Governance
      ↓
Trust Boundaries
      ↓
Security Decisions
      ↓
Technical Controls
      ↓
Failure Paths
      ↓
Evidence
      ↓
Validation
```

The emphasis is not on showing the largest possible AI technology stack.

It is on showing **where security decisions belong, why they belong there, how selected controls can be validated, and what would still need to be evaluated before production deployment.**

---

# Project Status

**Architecture and governance:** Complete for current project scope

**Local security-control prototype:** Implemented

**Initial selected control validation:** Complete

**AWS reference architecture:** Design only

**Azure reference architecture:** Design only

**Production RAG / LLM deployment:** Not implemented

**Cloud AI deployment:** Not implemented

**Production readiness:** Not claimed

---

# Conclusion

The main lesson from this project is that AI does not eliminate traditional security architecture.

It makes the placement of those controls more important.

Identity still matters.

Authorization still matters.

Data ownership still matters.

Logging still matters.

Human accountability still matters.

Incident response still matters.

The AI model is another component inside that architecture.

It should not become the architecture's security authority.
