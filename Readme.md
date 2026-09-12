# AI Security Governance and RAG Risk Architecture for Regulated Environments

## Project Scope Note

This repository contains an AI security architecture and governance project focused on securing an internal Retrieval-Augmented Generation (RAG) assistant in a regulated enterprise environment.

The project covers architecture, governance, threat modeling, access control, RAG security, compliance mapping, incident response, and local prototype planning.

The architecture and cloud deployment materials are **design artifacts** and should not be interpreted as a fully implemented production AI environment.

A separate healthcare AI security case study builds on these concepts by applying them to patient services and physician decision support.

---

## Project Overview

The scenario is an enterprise deploying an internal AI assistant that allows employees to ask questions against approved internal documents.

The business value is straightforward: employees can find information faster and reduce manual research.

The security problem is more complicated.

Introducing an AI assistant creates new questions around:

* What data the AI can access
* Whether the user is authorized to retrieve that data
* How retrieved documents influence the model
* Whether prompts or retrieved content can manipulate system behavior
* How sensitive information is prevented from appearing in responses
* How AI activity is logged and investigated
* When a human must review or override an AI-generated answer
* How third-party models and AI services are governed

The project examines those questions from a security architecture perspective rather than focusing on model development.

---

## Architecture Objective

The objective is to design a governed AI architecture that allows employees to query approved enterprise knowledge while maintaining appropriate controls around:

* Identity
* Authorization
* Data classification
* Retrieval
* Prompt handling
* Model interaction
* Response handling
* Human oversight
* Logging
* Incident response
* Compliance

A central principle of the design is:

> **The AI assistant should not create a new path around existing enterprise authorization and data-governance boundaries.**

If a user cannot access information through the underlying enterprise system, the RAG architecture should not make that information available through AI.

---

## Scope

This project includes:

* AI assistant reference architecture
* RAG data-flow design
* Trust-boundary analysis
* AI use-case governance
* AI risk assessment
* Data-classification requirements
* Role-based access-control design
* Identity-aware retrieval
* Prompt-injection controls
* AI threat modeling
* OWASP LLM risk mapping
* Logging and monitoring requirements
* Human-review requirements
* AI incident-response planning
* Compliance mapping
* Cost-control considerations
* Local prototype planning
* AWS and Azure deployment reference designs

---

## Out of Scope

The following are intentionally outside the scope of this project:

* Training a custom machine-learning model
* Fine-tuning a large language model
* Building a production AI platform
* Processing real confidential or regulated enterprise data
* Deploying a production vector database
* Operating a production cloud AI service
* Claiming formal regulatory or framework compliance

Cloud architecture documents in this repository are reference designs rather than evidence of deployed production infrastructure.

---

# Architecture Approach

I approached the problem as a sequence of trust and control decisions rather than treating the LLM as the center of the architecture.

A typical request follows this path:

**User → Identity → AI Application → Retrieval → Approved Knowledge → Model → Response Controls → User**

Security controls apply throughout that path.

---

## 1. Business Use-Case Review

Before selecting a model or AI platform, the organization should determine:

* What problem the AI system is solving
* Who will use it
* What decisions it may influence
* What information it needs
* What information it must not access
* What happens when it produces an incorrect answer

Not every AI use case should automatically proceed to implementation.

---

## 2. Data Classification

Documents entering the RAG knowledge base must be understood before they are indexed.

Classification affects:

* Who can retrieve the document
* Whether it should be available to AI at all
* Logging requirements
* Retention
* Response filtering
* Regulatory obligations

RAG does not eliminate existing data-governance requirements.

---

## 3. Identity and Authorization

Authentication identifies the user.

Authorization determines what that user is permitted to retrieve.

The retrieval layer should enforce enterprise authorization before context is sent to the model.

This prevents the AI application from becoming an alternate route to restricted information.

---

## 4. Approved Document Ingestion

Only approved information sources should enter the retrieval pipeline.

The ingestion process should account for:

* Source ownership
* Classification
* Document permissions
* Integrity
* Versioning
* Retention
* Removal of outdated information

Retrieved content should be treated as data, not automatically trusted instructions.

---

## 5. Retrieval Controls

RAG changes the security model because the model receives additional context dynamically.

Retrieval therefore needs controls around:

* Document authorization
* Metadata filtering
* User identity
* Classification
* Retrieval scope
* Source attribution

A technically relevant document is not necessarily an authorized document.

---

## 6. Prompt and Context Security

Prompt injection can originate from the user or from retrieved content.

Controls therefore need to consider both:

**Direct prompt injection**
A user attempts to override system behavior.

**Indirect prompt injection**
Malicious or untrusted instructions are embedded inside retrieved content.

The architecture uses layered controls rather than assuming prompt filtering alone solves the problem.

---

## 7. Model Interaction

The model should receive only the context required for the authorized request.

The architecture should also evaluate:

* Model-provider data handling
* Retention
* Model access
* API authentication
* Secrets
* Vendor risk
* Logging
* Failure behavior

The model is one component inside the security boundary, not the security boundary itself.

---

## 8. Response Controls

AI output cannot automatically be assumed to be accurate or appropriate.

Depending on the use case, response controls may include:

* Source citations
* Confidence or retrieval thresholds
* Sensitive-data filtering
* Refusal behavior
* Human review
* Escalation

The required controls depend on the consequence of an incorrect response.

---

## 9. Logging and Monitoring

The system should provide enough evidence to reconstruct significant AI activity.

Relevant events may include:

* User identity
* Request
* Retrieved sources
* Model interaction
* Response
* Policy decisions
* Denied requests
* Administrative changes

Logging must also be designed carefully so that the monitoring system itself does not become a repository for sensitive prompts or data.

---

## 10. Incident Response

AI incidents can differ from traditional application incidents.

Examples include:

* Sensitive-data disclosure
* Prompt-injection exploitation
* Unauthorized retrieval
* Malicious document ingestion
* Unexpected model behavior
* Compromised credentials
* Provider or model issues

The repository includes an AI incident-response playbook for evaluating these scenarios.

---

# Key Risks Addressed

| Risk                        | Example                                                 | Primary Control Direction                                 |
| --------------------------- | ------------------------------------------------------- | --------------------------------------------------------- |
| Prompt Injection            | User or document attempts to manipulate AI behavior     | Prompt/context controls, retrieval boundaries, validation |
| Sensitive Data Disclosure   | Restricted information appears in a response            | Classification, authorization, response controls          |
| Unauthorized Retrieval      | User retrieves documents outside their access           | Identity-aware retrieval and document permissions         |
| Hallucination               | AI generates unsupported information                    | Source grounding, citations, human review                 |
| Overreliance                | User treats AI output as authoritative                  | Human oversight and escalation                            |
| Audit Gaps                  | Activity cannot be reconstructed                        | Identity-linked logging and monitoring                    |
| Malicious Knowledge Content | Retrieved document contains hostile instructions        | Ingestion controls and untrusted-content handling         |
| Vendor Risk                 | External AI service introduces data or operational risk | Provider assessment and contractual controls              |

---

# Governance Model

AI security starts before a prompt reaches a model.

The governance material in this repository addresses:

* AI use-case intake
* Risk assessment
* Data classification
* Human-review requirements

This allows the organization to determine the required control level based on the use case rather than applying the same architecture to every AI workload.

---

# Security Architecture

The security material covers areas including:

* Threat modeling
* Prompt injection
* Access control
* RAG-specific risks
* Logging and monitoring
* OWASP LLM risks

These documents focus on where trust boundaries exist and what can fail across the AI request lifecycle.

---

# Compliance

The project includes illustrative mappings to:

* NIST AI Risk Management Framework
* NIST SP 800-53
* ISO/IEC 27001
* ISO/IEC 42001

These mappings show how architecture and governance controls can contribute to broader control objectives.

They do **not** demonstrate formal compliance.

Compliance requires operating processes, evidence, testing, ownership, monitoring, risk management, and independent assessment beyond the design artifacts contained here.

---

# Local Prototype

The repository includes planning for a local RAG prototype.

The purpose of the prototype is not to build a production AI system.

It provides a low-cost way to explore parts of the architecture such as:

* Document ingestion
* Retrieval
* Embeddings
* Similarity search
* Prompt construction
* Source grounding
* Basic control behavior

No real enterprise or regulated data is required.

---

# Cloud Reference Designs

AWS and Azure materials are included as **reference architecture only**.

They demonstrate how the architecture could map to cloud-native AI, identity, networking, logging, and security services.

They should not be interpreted as evidence that those cloud environments were deployed as part of this project.

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
│   └── Threat modeling, access control, RAG security,
│       prompt-injection, and monitoring artifacts
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
├── local_prototype/
│   └── Local RAG prototype planning
│
├── cloud_reference_only/
│   └── Cloud deployment reference designs
│
└── Phase_2/
    └── Additional project/prototype material
```

The directory names above reflect the current repository organization. Individual documents provide the detailed design within each area.

---

# Architecture Decisions

Several decisions shaped this project.

### Local-first approach

I chose a local-first approach so the architecture could be explored without requiring paid AI services or creating unnecessary cloud costs.

### RAG rather than model training

The scenario focuses on retrieving approved enterprise information rather than training or fine-tuning a model.

### Authorization before retrieval

User authorization should constrain retrieval before information is sent to the model.

### Retrieved content is untrusted

Documents can contain malicious or inappropriate instructions, so retrieved content cannot automatically be treated as trusted input.

### Human review depends on consequence

Not every AI response requires manual approval.

The need for human review should increase with the potential impact of an incorrect answer.

### Cloud services are implementation choices

The security architecture should not depend entirely on one AI provider.

AWS, Azure, or another platform can implement the architecture, but the underlying security requirements remain.

---

# What I Would Evaluate Before Production

Before moving this architecture into production, I would need to evaluate:

* Actual enterprise identity architecture
* Document repositories and permission models
* Data classifications
* Regulatory scope
* Model-provider contracts and data handling
* Vector database authorization
* Network architecture
* Private connectivity
* Secrets management
* Encryption and key management
* Logging and retention
* Security monitoring
* Prompt and response testing
* Red-team testing
* Exception processes
* Model and dependency changes
* Business continuity
* AI incident-response integration
* Human-review responsibilities

Those decisions depend on the organization, the data, the AI use case, and the consequence of failure.

---

# Result

This project demonstrates that securing RAG is not simply a matter of securing an LLM API.

The architecture has to protect the complete path between:

**the user, identity, enterprise data, retrieval system, model, response, and operational controls.**

The central question throughout the project is:

> **What is the AI allowed to know, what is the user allowed to know, and where is that decision actually enforced?**

That question drives the identity, retrieval, data, monitoring, governance, and human-oversight decisions throughout the architecture.
