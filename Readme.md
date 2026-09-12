# AI Security Governance and RAG Risk Architecture for Regulated Environments

## Project Scope Note

This repository contains an AI security architecture and governance project focused on securing an internal Retrieval-Augmented Generation (RAG) assistant in a regulated enterprise environment.

The project covers architecture, governance, threat modeling, access control, RAG security, compliance mapping, incident response, and an implemented local security-control prototype.

The architecture and cloud deployment materials are **design artifacts** and should not be interpreted as a fully implemented production AI environment.

Phase 2 moves selected controls from the architecture into a local Python prototype using mock users, mock documents, metadata, and local logging. The prototype validates selected security-control concepts but is not a production RAG or LLM implementation.

---

## Project Overview

The scenario is an enterprise deploying an internal AI assistant that allows employees to ask questions against approved internal documents.

The business value is straightforward: employees can find information faster and reduce manual research.

The security problem is more complicated.

Introducing an AI assistant creates new questions around:

- What data the AI can access
- Whether the user is authorized to retrieve that data
- How retrieved documents influence the model
- Whether prompts or retrieved content can manipulate system behavior
- How sensitive information is prevented from appearing in responses
- How AI activity is logged and investigated
- When a human must review or override an AI-assisted response
- How third-party models and AI services are governed

I approached the project from the security architecture perspective rather than starting with model selection or model development.

---

## Business Problem

A RAG assistant creates a new path between employees and enterprise information.

That path can improve access to knowledge, but it can also weaken existing controls if identity, authorization, classification, retrieval, and monitoring are not carried through the AI workflow.

The central architecture question became:

> **What is the AI allowed to know, what is the user allowed to know, and where is that decision actually enforced?**

A useful answer from the model is not enough. The organization also needs to know that the information was authorized, the request was evaluated appropriately, significant decisions were logged, and higher-risk activity can be reviewed or investigated.

---

## Architecture Objective

The objective is to design a governed AI architecture that allows employees to query approved enterprise knowledge while maintaining appropriate controls around:

- Identity
- Authorization
- Data classification
- Retrieval
- Prompt handling
- Model interaction
- Response handling
- Human oversight
- Logging
- Incident response
- Compliance

A central principle of the design is:

> **The AI assistant should not create a new path around existing enterprise authorization and data-governance boundaries.**

If a user cannot access information through the underlying enterprise environment, the RAG architecture should not make that information available simply because the user is interacting through AI.

---

## Scope

This project includes:

- AI assistant reference architecture
- RAG data-flow design
- Trust-boundary analysis
- AI use-case governance
- AI risk assessment
- Data-classification requirements
- Role-based access-control design
- Identity-aware retrieval
- Prompt-injection controls
- AI threat modeling
- OWASP LLM risk mapping
- Logging and monitoring requirements
- Human-review requirements
- AI incident-response planning
- Compliance mapping
- Cost-control considerations
- Local security-control prototype and validation
- AWS and Azure deployment reference designs

---

## Out of Scope

The following are intentionally outside the scope of this project:

- Training a custom machine-learning model
- Fine-tuning a large language model
- Building a production AI platform
- Processing real confidential or regulated enterprise data
- Deploying a production vector database
- Operating a production cloud AI service
- Claiming formal regulatory or framework compliance

Cloud architecture documents in this repository are reference designs rather than evidence of deployed production infrastructure.

The local prototype demonstrates selected control behavior and should not be interpreted as a production RAG, LLM, or semantic-retrieval platform.

---

# Architecture Approach

I approached the problem as a sequence of trust and control decisions rather than treating the LLM as the center of the architecture.

A typical production request would follow a path similar to:

**User → Identity → AI Application → Retrieval → Approved Knowledge → Model → Response Controls → User**

Security decisions exist throughout that path.

---

## 1. Business Use-Case Review

Before selecting a model or AI platform, the organization should determine:

- What problem the AI system is solving
- Who will use it
- What decisions it may influence
- What information it needs
- What information it must not access
- What happens when it produces an incorrect answer

Not every AI use case should automatically proceed to implementation.

The consequence of failure helps determine how much governance, human oversight, testing, and technical control is appropriate.

---

## 2. Data Classification

Documents entering the RAG knowledge base need to be understood before they are indexed or made available for retrieval.

Classification affects:

- Who can retrieve the document
- Whether it should be available to AI at all
- Logging requirements
- Retention
- Response filtering
- Regulatory obligations

RAG does not eliminate existing data-governance requirements.

---

## 3. Identity and Authorization

Authentication identifies the user.

Authorization determines what that user is permitted to retrieve.

For this scenario, I would constrain retrieval using the user's enterprise authorization context before restricted information is supplied to the model.

This prevents the AI application from becoming an alternate route to information the user would otherwise be unable to access.

---

## 4. Approved Document Ingestion

Only approved information sources should enter the retrieval pipeline.

The ingestion process should account for:

- Source ownership
- Classification
- Document permissions
- Integrity
- Versioning
- Retention
- Removal of outdated information

Retrieved content should also be treated as data rather than automatically trusted instructions.

This becomes important when considering indirect prompt injection through documents or other retrieved sources.

---

## 5. Retrieval Controls

RAG changes the security model because additional context is selected dynamically and supplied to the model.

Retrieval therefore needs controls around:

- Document authorization
- Metadata filtering
- User identity
- Classification
- Retrieval scope
- Source attribution

A technically relevant document is not necessarily an authorized document.

For this reason, retrieval quality and retrieval authorization are separate architecture concerns.

---

## 6. Prompt and Context Security

Prompt injection can originate from the user or from retrieved content.

Controls therefore need to consider both:

**Direct prompt injection**  
A user attempts to override or manipulate expected system behavior.

**Indirect prompt injection**  
Malicious or inappropriate instructions are embedded inside content that the AI system retrieves.

For this scenario, I would use layered controls rather than assume that a single prompt filter can solve the problem.

Authorization, retrieval boundaries, trusted-source management, monitoring, response controls, and human oversight all contribute to the overall defense.

---

## 7. Model Interaction

The model should receive only the context required for the authorized request.

In a production environment, I would also need to evaluate:

- Model-provider data handling
- Data retention
- Model access
- API authentication
- Secrets management
- Vendor risk
- Logging
- Failure behavior
- Model and dependency changes

The model is one component inside the architecture. It is not the security boundary itself.

---

## 8. Response Controls

AI output cannot automatically be assumed to be accurate or appropriate.

Depending on the use case and consequence of failure, response controls may include:

- Source citations
- Confidence or retrieval thresholds
- Sensitive-data filtering
- Refusal behavior
- Human review
- Escalation

The required control level should reflect what happens if the AI produces an incorrect, incomplete, or inappropriate response.

---

## 9. Logging and Monitoring

The system should provide enough evidence to reconstruct significant AI activity.

Relevant events may include:

- User identity
- Request
- Retrieved sources
- Model interaction
- Response
- Policy decisions
- Denied requests
- Administrative changes
- Human-review events

Logging also needs its own data-protection considerations.

Capturing every prompt and response without considering sensitivity could turn the monitoring environment into another repository of confidential information.

---

## 10. Incident Response

AI incidents can differ from traditional application incidents.

Examples include:

- Sensitive-data disclosure
- Prompt-injection exploitation
- Unauthorized retrieval
- Malicious document ingestion
- Unexpected model behavior
- Compromised credentials
- Provider or model issues

The repository includes AI incident-response material for considering how these scenarios would be detected, investigated, contained, and escalated.

---

# Key Risks Addressed

| Risk | Example | Primary Control Direction |
|---|---|---|
| Prompt Injection | User or retrieved content attempts to manipulate AI behavior | Prompt/context controls, retrieval boundaries, monitoring |
| Sensitive Data Disclosure | Restricted information appears in a response | Classification, authorization, response controls |
| Unauthorized Retrieval | User retrieves documents outside authorized access | Identity-aware retrieval and document permissions |
| Hallucination | AI generates unsupported information | Source grounding, citations, human review |
| Overreliance | User treats AI output as authoritative | Human oversight and escalation |
| Audit Gaps | Activity cannot be reconstructed | Identity-linked logging and monitoring |
| Malicious Knowledge Content | Retrieved document contains hostile instructions | Ingestion controls and untrusted-content handling |
| Vendor Risk | External AI service introduces data or operational risk | Provider assessment and contractual controls |

---

# Governance Model

AI security starts before a prompt reaches a model.

The governance material in this repository addresses areas including:

- AI use-case intake
- Risk assessment
- Data classification
- Human-review requirements

The intent is to determine the appropriate control level based on the use case, data, users, and potential consequence rather than applying exactly the same architecture to every AI workload.

---

# Security Architecture

The security material covers areas including:

- Threat modeling
- Prompt injection
- Access control
- RAG-specific risks
- Logging and monitoring
- OWASP LLM risks

These documents focus on where trust boundaries exist, where security decisions should occur, and what can fail across the AI request lifecycle.

---

# Phase 2: Local Security-Control Prototype

After documenting the architecture, I built a small local Python prototype to exercise selected security decisions.

The goal was not to build a production RAG platform or deploy an LLM.

I wanted to demonstrate that some of the controls surrounding an AI/RAG workflow could be validated independently of a production model.

The prototype uses:

- Mock users and roles
- Mock documents
- Document metadata
- Python control logic
- Local JSONL security logs
- No real enterprise data
- No cloud AI services
- No paid AI APIs

## Prototype Control Flow

The prototype follows a simplified sequence:

**Mock User → Prompt Risk Evaluation → Policy Decision → Retrieval → Document Authorization → Logging → Advisory Response**

If a prompt is classified for blocking, processing stops before document retrieval.

For requests that proceed, the prototype evaluates document authorization using mock user roles/groups and document metadata.

---

## Controls Demonstrated

The prototype demonstrates:

- Mock identity and role context
- Role- and group-based document authorization
- Document approval and classification checks
- Prompt-injection pattern detection
- Sensitive-data and secret-pattern detection
- Prompt risk scoring
- Blocking high-risk prompts before retrieval
- Authorized and denied retrieval decisions
- Prompt event logging
- Retrieval event logging
- Access-decision logging
- Security-alert logging
- Simulated human-review triggers
- Advisory-only response behavior

These are intentionally simplified controls designed to validate architecture concepts rather than represent production security products.

---

## Initial Prototype Validation

Two initial scenarios were documented and tested.

### Prompt Injection Attempt

A mock General Employee attempted to override previous instructions and reveal restricted documents.

The prototype:

- Detected the prompt-injection pattern
- Assigned a high risk level
- Blocked the request
- Stopped processing before document retrieval
- Generated security logging

**Result: Pass**

### Authorized Policy Request

A mock General Employee requested information from an approved internal AI acceptable-use policy.

The prototype:

- Classified the request as low risk
- Evaluated document authorization
- Retrieved the authorized mock document
- Generated an advisory response
- Recorded prompt, retrieval, and access-decision events

**Result: Pass**

Detailed implementation and test evidence are located under:

`Phase_2/local_prototype/`

---

# Compliance

The project includes illustrative mappings to:

- NIST AI Risk Management Framework
- NIST SP 800-53
- ISO/IEC 27001
- ISO/IEC 42001

These mappings show how architecture and governance controls can contribute to broader control objectives.

They do **not** demonstrate formal compliance.

Compliance requires operating processes, evidence, testing, ownership, monitoring, risk management, and assessment beyond the design artifacts contained in this repository.

---

# Cloud Reference Designs

AWS and Azure materials are included as **reference architecture only**.

They demonstrate how the architecture could map to cloud-native AI, identity, networking, logging, and security services.

They should not be interpreted as evidence that those cloud environments were deployed as part of this project.

This separation was intentional. The security requirements should survive a change in implementation platform rather than depend entirely on one AI or cloud provider.

---

# Repository Structure

The repository is organized around the major parts of the architecture:

```text
ai-security-rag-governance-architecture/
│
├── Readme.md
├── Business_Case.md
├── Reference_Architecture.md
├── Arichitecture_Dataflow.md
├── Cost_Controls.md
├── lessonslearned.md
├── project_status.md
│
├── Governance/
│   └── AI governance and data-governance artifacts
│
├── Security/
│   └── Threat modeling, access control, prompt security,
│       AI risk, and monitoring artifacts
│
├── architecture/
│   └── Supporting architecture documentation
│
├── compliance/
│   └── Framework mappings
│
├── incident_response/
│   └── AI incident-response material
│
├── cloud_reference_only/
│   └── Cloud deployment reference designs
│
└── Phase_2/
    ├── readme.md
    └── local_prototype/
        ├── app.py
        ├── requirements.txt
        ├── sample_users.json
        ├── sample_docs/
        ├── metadata/
        ├── logs/
        ├── tests/
        ├── prototype_results.md
        └── readme_runbook.md
```

> **Repository cleanup note:** The root-level `local_prototype/` directory is intentionally not shown in this structure until its older planning material is reviewed against the implemented `Phase_2/local_prototype/` version.

---

# Architecture Decisions

Several decisions shaped this project.

## Local-First Validation

I chose a local-first prototype so selected security controls could be exercised without requiring paid AI services, creating unnecessary cloud costs, or introducing real enterprise data.

This also separated validation of the security logic from the choice of a particular AI provider.

## RAG Rather Than Model Training

The scenario focuses on retrieving approved enterprise information rather than training or fine-tuning a model.

The primary security problem is therefore not model training. It is controlling the path between the user, enterprise information, retrieval process, and model.

## Authorization Before Access

User authorization should constrain what information can be retrieved before restricted content becomes available to later components in the AI workflow.

The Phase 2 prototype exercises this principle using mock roles, groups, and document metadata.

## Retrieved Content Is Untrusted

Documents can contain malicious or inappropriate instructions.

Retrieved information therefore cannot automatically be treated as trusted instructions simply because it came from an approved knowledge source.

## Human Review Depends on Consequence

Not every AI response requires manual approval.

The need for human review should increase with the sensitivity of the information, the action being taken, and the potential impact of an incorrect answer.

The local prototype includes simulated human-review triggers to demonstrate this design concept.

## Cloud Services Are Implementation Choices

The security architecture should not depend entirely on one AI provider.

AWS, Azure, or another platform can implement the architecture, but the underlying requirements around identity, authorization, retrieval, data protection, monitoring, and governance remain.

---

# Failure Paths Considered

The architecture considers what happens when controls do not behave as expected.

Examples include:

- User authentication succeeds but document authorization fails
- Prompt is determined to be high risk before retrieval
- User requests information outside authorized scope
- Retrieved content contains malicious instructions
- Required document governance metadata is missing
- Sensitive information appears in a prompt
- Human review is required
- Logging or monitoring becomes unavailable
- Model or provider behavior changes
- An approved document becomes outdated or compromised

The appropriate response may be to block, deny, constrain, log, alert, escalate, or require human review depending on the failure.

---

# What I Would Evaluate Before Production

Before moving this architecture into production, I would need to evaluate:

- Actual enterprise identity architecture
- Document repositories and permission models
- Data classifications
- Regulatory scope
- Model-provider contracts and data handling
- Vector database authorization
- Production retrieval architecture
- Network architecture
- Private connectivity
- Secrets management
- Encryption and key management
- Logging and retention
- Security monitoring
- Prompt and response testing
- Red-team testing
- Exception processes
- Model and dependency changes
- Business continuity
- AI incident-response integration
- Human-review responsibilities
- Production availability and failure requirements

Those decisions depend on the organization, the data, the AI use case, and the consequence of failure.

---

# Result

This project demonstrates that securing RAG is not simply a matter of securing an LLM API.

The architecture has to protect the complete path between:

**the user, identity, enterprise data, retrieval system, model, response, and operational controls.**

Phase 2 then takes selected controls from that architecture and demonstrates them locally through code and test evidence.

The central question throughout the project remains:

> **What is the AI allowed to know, what is the user allowed to know, and where is that decision actually enforced?**

That question drives the identity, retrieval, data, monitoring, governance, and human-oversight decisions throughout the architecture.
