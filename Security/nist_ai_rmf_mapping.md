# NIST AI Risk Management Framework Mapping

## Purpose

This document maps the enterprise AI security architecture and selected local prototype controls to the NIST AI Risk Management Framework (AI RMF).

The purpose is to show how the project considers AI risk through the NIST AI RMF functions:

- Govern
- Map
- Measure
- Manage

This is an architecture mapping.

> It is not a NIST certification, compliance attestation, or claim that every NIST AI RMF outcome has been implemented.

The mapping distinguishes between:

1. Production architecture and governance requirements.
2. Controls demonstrated by the local security-control prototype.
3. Controls that remain future production considerations.

# Project Context

The production concept is an internal AI assistant that could eventually use Retrieval-Augmented Generation to answer employee questions from approved enterprise information.

The current project has progressed through:

```text
Architecture and Governance
        ↓
Local Security-Control Prototype
        ↓
Selected Control Validation
```

The implemented prototype uses:

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
- Cloud AI
- External model API
- Production SIEM
- Production human-review workflow
- Real enterprise data
- Autonomous tools or agents

# Architecture Principle

> The AI assistant should not create a new path around existing enterprise authorization, data-governance, and accountability boundaries.

The model is treated as one component within the architecture rather than as the control authority.

# NIST AI RMF Functions

| Function | Project Interpretation |
| --- | --- |
| Govern | Establish accountability, policy, oversight, and risk-management expectations |
| Map | Understand the business context, users, data, impacts, assumptions, and system boundaries |
| Measure | Assess, test, observe, and gather evidence about risk and control behavior |
| Manage | Prioritize risk, select treatment, respond to issues, and adapt controls as the system changes |

# Mapping Summary

| Function | Project Alignment |
| --- | --- |
| Govern | Use-case intake, risk assessment, ownership concepts, data governance, human-accountability requirements |
| Map | Business case, data flow, trust boundaries, data classification, user roles, deployment assumptions |
| Measure | STRIDE analysis, OWASP mapping, test scenarios, local control validation, structured security evidence |
| Manage | Risk treatment concepts, authorization, logging, incident-response planning, deployment decision gates |

The amount of implementation evidence differs by function.

---

# GOVERN

## Objective

Governance establishes how AI risk is owned, reviewed, communicated, and controlled.

For this architecture, governance begins before model or cloud technology is selected.

Important questions include:

- What business problem is being solved?
- Who is accountable for the outcome?
- What data is involved?
- Who is allowed to use the capability?
- What decisions may the AI influence?
- What decisions remain human?
- What risks require treatment?
- What evidence is required?
- What changes require reassessment?

# Govern Alignment

| Governance Area | Project Approach |
| --- | --- |
| Business ownership | Intake identifies accountable business ownership |
| Technical ownership | Production implementation requires technical ownership |
| Security architecture | Security requirements and trust boundaries are documented |
| Data ownership | Data owners remain responsible for approved enterprise sources |
| Use-case review | AI use-case intake evaluates business purpose and scope |
| Risk assessment | Qualitative AI risk assessment evaluates exposure and consequence |
| Human accountability | Consequential decisions remain with authorized humans |
| Data governance | Classification and approved-use requirements are documented |
| Role separation | Platform administration does not automatically grant content entitlement |
| Change governance | Material changes should trigger reassessment |

These are architecture and governance requirements.

They should not be interpreted as evidence that a production governance organization or approval workflow has been deployed.

# Govern Artifacts

Relevant repository artifacts include:

```text
Business_Case.md
Cost_Controls.md
Governance/ai_use_case_intake.md
Governance/Data_Classification.md
Governance/human_review_requirements.md
Security/ai_risk_assessment.md
Security/access_control_model.md
incident_response/
```

# Human Accountability

The project does not use a rule that every High-risk prompt or every Restricted document automatically requires human approval.

Instead:

> Human review should be based primarily on the consequence of the decision or action.

Examples that may require accountable human authority include:

- Access approval
- Production change
- Legal interpretation
- Regulatory decision
- Security exception
- Financial decision
- High-impact personnel decision

A prompt-injection attempt is primarily a security event rather than a normal business approval workflow.

# Current Prototype Evidence for Govern

The local prototype provides limited evidence for governance concepts through:

- Synthetic role definitions
- Document classifications
- Document ownership metadata
- Approved-document status
- Separation between AI system administration and content entitlement
- Advisory-only response behavior
- Simulated review metadata

The prototype does not implement:

- Enterprise approval workflow
- Formal risk acceptance
- Real data-owner approval
- Production governance board
- Formal human-review routing
- Production access certification

---

# MAP

## Objective

Map establishes the context in which AI risk exists.

For this project, that means understanding the complete path from business need to information access and eventual business consequence.

# Business Context

The production concept is an internal AI assistant intended to help users locate and understand approved enterprise information.

The system is intended to be advisory.

It should not automatically become an authority for:

- Access approval
- Legal decisions
- Regulatory decisions
- Production changes
- Security exceptions
- Financial transactions

# Map Alignment

| Context Area | Project Approach |
| --- | --- |
| Business purpose | Internal knowledge assistance |
| Intended users | Enterprise users with approved access |
| Data | Approved organizational information |
| Data sensitivity | Classification and metadata influence handling |
| Identity | Production design relies on trusted enterprise identity |
| Authorization | Access should preserve source entitlement |
| Retrieval | Relevance does not equal authorization |
| Model | Model behavior is not trusted as access control |
| Human authority | Consequential decisions remain accountable to people |
| Deployment | Local validation first; cloud designs are reference architectures |
| Agent capability | Not implemented and outside current scope |

# System Boundaries

A conceptual production path is:

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

Security logging and human accountability surround important decision points.

# Trust Boundaries

Important trust boundaries include:

- User → Assistant
- Assistant → Identity Provider
- Prompt → Retrieval
- Retrieval → Knowledge Source
- Knowledge Source → Model Context
- Assistant → Model Provider
- Model → Response Controls
- Assistant → Logging
- Administrator → Configuration
- AI Output → User

These are production architecture boundaries.

The local prototype exercises only selected parts of them.

# Data Context

The local prototype uses only synthetic data.

Synthetic documents may still carry labels such as:

- Internal
- Confidential
- Restricted

Those labels exist to exercise security-control behavior.

They do not represent real Restricted enterprise information.

# Current Prototype Evidence for Map

The prototype demonstrates:

```text
Mock Identity
      ↓
Prompt Risk
      ↓
Local Retrieval
      ↓
Metadata Authorization
      ↓
Logging / Review Trigger
      ↓
Advisory Response
```

This provides practical evidence for selected identity, authorization, retrieval, and logging boundaries without requiring a production AI platform.

---

# MEASURE

## Objective

Measure evaluates whether identified risks and controls behave as expected.

For this project, an important distinction is:

> A documented control is not necessarily an implemented control, and an implemented control is not necessarily a tested control.

# Measure Alignment

| Measurement Area | Current Project Status |
| --- | --- |
| STRIDE threat analysis | Documented |
| OWASP LLM risk mapping | Documented / reviewed separately |
| Prompt-risk logic | Implemented locally |
| Document authorization | Implemented locally |
| Structured security logging | Implemented locally |
| Prompt-injection testing | One direct scenario validated |
| Authorized retrieval testing | One scenario validated |
| Sensitive-data test suite | Defined, not yet executed |
| Broader access-control tests | Defined, not yet executed |
| Human-review trigger | Implemented as simulated event |
| Production LLM behavior | Not implemented |
| Hallucination testing | Not implemented |
| Production output validation | Not implemented |
| Enterprise monitoring | Not implemented |
| Cloud cost monitoring | Not implemented |

# Initial Validation Evidence

Two scenarios are currently documented as executed.

## Authorized Policy Retrieval

A mock General Employee requested the approved synthetic AI acceptable-use policy.

The prototype:

- Evaluated the prompt
- Retrieved the matching document
- Applied role/group authorization
- Logged the decision
- Returned an advisory response

**Result: Pass**

## Direct Prompt Injection

A mock General Employee submitted an instruction attempting to override controls and reveal Restricted documents.

The prototype:

- Detected the configured pattern
- Classified the request as High risk
- Selected Block
- Logged the prompt event
- Generated a security alert
- Stopped before document retrieval

**Result: Pass**

These tests provide evidence for selected control paths.

They do not demonstrate production AI safety generally.

# Measurement Limitations

The current prototype does not validate:

- Enterprise SSO
- MFA
- Session security
- Production RAG
- Semantic retrieval
- Embeddings
- Vector security
- LLM hallucination
- Model leakage
- Indirect prompt injection
- Production output filtering
- Enterprise DLP
- SIEM detections
- Production human approval
- Rate limiting
- Resilience
- Autonomous agent behavior

# Risk Assessment

The project uses qualitative risk reasoning rather than adding unrelated numeric domain scores.

Risk should consider:

- Business consequence
- Data exposure
- User population
- Production authority
- Threat likelihood
- Control effectiveness
- Residual risk

A severe risk in one domain should not be diluted merely because unrelated domains are lower risk.

# Security Evidence

The local prototype writes structured JSONL evidence to:

```text
prompt_events.jsonl
retrieval_events.jsonl
access_decisions.jsonl
security_alerts.jsonl
review_events.jsonl
```

This provides evidence for selected local control decisions.

It is not equivalent to a production SIEM or formal compliance evidence system.

# Testing Principle

Additional test scenarios should remain:

**Not Yet Tested**

until executed.

This prevents architecture documentation from being mistaken for validation evidence.

---

# MANAGE

## Objective

Manage focuses on deciding what to do about identified AI risks.

Possible risk responses include:

- Mitigate
- Avoid
- Accept
- Transfer
- Defer
- Redesign
- Escalate

The appropriate response depends on organizational authority and risk policy.

# Manage Alignment

| Management Area | Project Approach |
| --- | --- |
| Risk treatment | Architecture identifies possible treatment choices |
| Authorization risk | Preserve deterministic access control outside the model |
| Prompt risk | Use layered controls rather than relying on one filter |
| Data exposure | Use classification, authorization, and minimization |
| Human authority | Keep consequential decisions outside AI authority |
| Incident response | Define AI-specific investigation scenarios |
| Deployment risk | Require additional review when moving to production/cloud |
| Cost risk | Avoid unnecessary paid infrastructure during validation |
| Architecture change | Reassess when risk conditions materially change |

# Risk Ownership

Security architecture can identify and explain risk.

It does not automatically own every risk.

Risk ownership should remain with the party that has authority over the affected business outcome.

Examples may include:

- Business owner
- Data owner
- Application owner
- Security owner
- Privacy owner
- Compliance owner
- Platform owner

# Incident Response

The production architecture should be able to support investigation of scenarios such as:

- Unauthorized information exposure
- Successful retrieval bypass
- Prompt-injection activity
- Sensitive-data submission
- Knowledge-source poisoning
- Administrative misconfiguration
- Provider compromise
- Logging failure

The repository contains an AI incident-response playbook as an architecture artifact.

The local prototype does not implement an enterprise incident-management platform.

# Human Review

The production architecture should preserve human authority where consequences justify it.

The local prototype only demonstrates a review trigger.

When an authorized retrieved document is marked:

```text
human_review_required
```

the application can record:

```text
Pending simulated review
```

It does not:

- Hold the response
- Assign a reviewer
- Record approval
- Record rejection
- Enforce an SLA

# Review Triggers

Rather than inventing arbitrary quarterly or annual schedules, reassessment should occur when relevant conditions change.

Examples include:

- New business use case
- New data classification
- New user population
- New model/provider
- New retrieval source
- Production deployment
- Material architecture change
- Security incident
- New tool/agent capability
- New regulatory requirement
- Significant control failure

Organizations may also impose periodic review requirements through existing enterprise policy.

# Cloud Deployment

AWS and Azure materials in this repository are reference architectures.

No cloud AI platform is deployed.

Before production cloud deployment, the organization would need to evaluate areas such as:

- Identity
- Network exposure
- Encryption
- Secrets
- Logging
- Provider data handling
- Retention
- Cost
- Resilience
- Data approval
- Operational ownership

The exact controls depend on the selected platform and use case.

---

# NIST AI RMF Trustworthiness Characteristics

The AI RMF describes characteristics associated with trustworthy AI.

This project uses them as design considerations rather than claiming formal conformance.

# Valid and Reliable

Production considerations include:

- Approved information sources
- Appropriate retrieval quality
- Source traceability
- Testing
- Known limitations
- Controlled document lifecycle

Current prototype evidence is limited to selected local retrieval and authorization behavior.

No production LLM reliability testing has been performed.

# Safe

The architecture limits AI authority and emphasizes:

- Advisory use
- Deterministic authorization
- Prompt controls
- Human authority for consequential decisions
- Controlled expansion into production actions

The current prototype cannot perform production actions.

# Secure and Resilient

Production requirements may include:

- Trusted authentication
- Authorization
- Prompt-injection defenses
- Secure retrieval
- Protected logs
- Monitoring
- Rate controls
- Resilience

The local prototype demonstrates selected authorization, prompt-risk, and logging controls only.

# Accountable and Transparent

The architecture supports:

- Defined ownership
- Traceable security decisions
- Source references
- Documented limitations
- Human accountability

The prototype provides correlation and local security evidence for selected request paths.

# Explainable and Interpretable

For this architecture, useful explainability includes understanding:

- Which source was used
- Which authorization decision occurred
- Why a request was blocked
- Which control triggered
- What limitations apply

This is different from claiming that the internal reasoning of a production LLM can always be explained.

# Privacy-Enhanced

The current prototype uses synthetic data.

Production privacy considerations include:

- Data minimization
- Prompt minimization
- Response minimization
- Log minimization
- Provider data handling
- Retention
- Access control

# Fairness and Harmful Bias

The current prototype is not designed to make employment, lending, healthcare, eligibility, or similar high-impact decisions.

If the system were expanded into such use cases, fairness and harmful-bias analysis would require a separate and deeper evaluation.

The absence of those use cases in the current prototype is not evidence that bias risk has been validated.

---

# AI Risk-to-Architecture Mapping

| AI Risk | Relevant RMF Functions | Architecture Response |
| --- | --- | --- |
| Prompt injection | Map, Measure, Manage | Prompt controls plus independent authorization |
| Information disclosure | Govern, Map, Measure, Manage | Classification, authorization, minimization |
| Unauthorized retrieval | Map, Measure, Manage | Document-level authorization |
| Hallucination | Map, Measure, Manage | Source grounding, limitations, human authority |
| Overreliance | Govern, Manage | Advisory design and consequence-based review |
| Excessive agency | Govern, Map, Manage | No autonomous action in current scope |
| Vendor exposure | Govern, Map, Manage | Provider/data-handling review |
| Knowledge poisoning | Map, Measure, Manage | Content governance and untrusted-context handling |
| Weak auditability | Govern, Measure, Manage | Structured security evidence |
| Operational dependency | Map, Measure, Manage | Resilience and fallback planning |
| Unexpected cost | Govern, Map, Manage | Deployment and usage controls |

Not every listed response is implemented in the local prototype.

# Example Use Case

## Internal AI Policy Assistant

**Business purpose:** Help employees locate approved internal policy and security guidance.

**Production concept:** Could eventually use RAG-style capabilities over approved enterprise sources.

**Current implementation:** Limited local security-control prototype using synthetic users, documents, metadata, simple keyword retrieval, authorization, prompt-risk logic, and JSONL logging.

### Govern

- Business purpose documented
- Governance artifacts defined
- Human-accountability principles documented
- Data-handling requirements documented

### Map

- Users defined
- Synthetic document classes defined
- Trust boundaries documented
- Production and prototype scopes separated

### Measure

- Two initial scenarios executed successfully
- Additional tests defined but not yet executed
- Local structured evidence generated

### Manage

- Architecture identifies treatment choices
- Production risks and limitations documented
- Cloud deployment remains optional/reference-only
- Material changes require reassessment

## Current Decision

Continue local architecture/control validation using synthetic data.

This decision applies only to the current prototype.

It is not an approval for production deployment.

---

# Relationship to Compliance

NIST AI RMF is a risk-management framework.

This repository uses it to organize architecture thinking and identify gaps.

Therefore:

> Mapping project artifacts to NIST AI RMF does not establish compliance, certification, or formal conformance.

A formal organizational assessment would require:

- Defined scope
- Organizational policies
- Responsible owners
- Implemented controls
- Operational evidence
- Risk acceptance
- Appropriate assessment methodology

That work is outside this portfolio project's scope.

# Architecture Evidence

Useful project artifacts include:

```text
Business_Case.md
Architecture_Dataflow.md
Reference_Architecture.md
Cost_Controls.md
lessonslearned.md

Governance/
├── ai_use_case_intake.md
├── Data_Classification.md
└── human_review_requirements.md

architecture/
├── deployment_options.md
└── trust_boundaries.md

Security/
├── access_control_model.md
├── ai_risk_assessment.md
├── logging_monitoring.md
├── prompt_injection_controls.md
├── threat_model_stride.md
├── nist_ai_rmf_mapping.md
└── owasp_llm_top10_mapping.md

Phase_2/local_prototype/
├── app.py
├── metadata/
├── sample_docs/
├── sample_users.json
├── logs/
└── tests/
```

The exact repository filenames should be kept synchronized with the repository as it evolves.

# Security Architect Perspective

The value of NIST AI RMF in this project is not that it produces another checklist.

It helps force several different questions:

**Govern**

> Who is accountable, and what rules apply?

**Map**

> What are we actually building, for whom, using what information, and with what consequence?

**Measure**

> What evidence shows that the controls behave as intended?

**Manage**

> What do we do with the risk that remains?

That sequence fits the architecture approach used throughout this project.

# Conclusion

This project aligns its architecture thinking with the NIST AI Risk Management Framework through the Govern, Map, Measure, and Manage functions.

The project has already progressed beyond documentation-only planning:

```text
Architecture and Governance
        ↓
Local Security-Control Prototype
        ↓
Initial Selected-Control Validation
```

The local prototype provides implementation evidence for selected identity-context, prompt-risk, authorization, retrieval, and logging controls.

The broader production architecture identifies additional controls that would be required before enterprise deployment.

The project does **not** claim NIST AI RMF certification or comprehensive implementation.

Its purpose is to demonstrate how a security architect can use the framework to connect:

```text
Business Context
      ↓
AI Risk
      ↓
Architecture
      ↓
Controls
      ↓
Evidence
      ↓
Residual Risk
      ↓
Accountability
```

That is the useful outcome of the mapping.
