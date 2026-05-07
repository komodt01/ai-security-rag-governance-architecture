# AI Risk Assessment

## Purpose

This document defines the AI risk assessment process for the secure enterprise AI assistant architecture.

The goal is to evaluate AI use cases before implementation, identify security and governance risks, assign risk ratings, document required controls, and determine whether a proposed AI use case should be approved, rejected, limited, or escalated for additional review.

This assessment is designed for regulated environments where AI systems may interact with internal documents, security standards, compliance guidance, identity data, operational procedures, or business decision workflows.

## Scope

This risk assessment applies to AI use cases involving:

- Internal AI assistants
- Retrieval-Augmented Generation systems
- AI-enabled search over internal documents
- AI summarization of approved policies or standards
- AI-assisted security or architecture guidance
- AI-assisted compliance research
- AI systems that interact with enterprise data
- AI systems that rely on third-party model providers
- AI workflows that may influence business, security, or operational decisions

This assessment does not approve the use of real customer data, regulated data, production secrets, or confidential records unless explicitly reviewed and approved through the appropriate governance process.

## Risk Assessment Objectives

The AI risk assessment process should answer the following questions:

1. What business problem does the AI use case solve?
2. What data will the AI system access, process, retrieve, or generate?
3. Who will use the AI system?
4. What decisions or actions could the AI output influence?
5. What security, privacy, compliance, operational, and cost risks exist?
6. What controls are required before implementation?
7. Who owns the AI use case?
8. Who approves the AI use case?
9. What monitoring and review processes are required?
10. Should the use case be approved, limited, rejected, or escalated?

## Assessment Decision Outcomes

| Decision | Description |
|---|---|
| Approved | Use case may proceed with required controls |
| Approved with Conditions | Use case may proceed only if specific controls are implemented |
| Limited Pilot | Use case may proceed in a controlled pilot with mock or low-risk data |
| Escalated | Use case requires additional review from security, privacy, legal, compliance, or architecture governance |
| Rejected | Use case should not proceed due to unacceptable risk |
| Deferred | Use case requires more information before a decision can be made |

## AI Use Case Intake

Each proposed AI use case should begin with a structured intake.

## Basic Use Case Information

| Field | Description |
|---|---|
| Use Case Name | Name of the proposed AI use case |
| Business Owner | Person or team responsible for the business outcome |
| Technical Owner | Person or team responsible for implementation |
| Security Owner | Person or team responsible for security review |
| Data Owner | Owner of the data or documents used by the AI system |
| Intended Users | User groups expected to use the system |
| Business Purpose | Description of the problem being solved |
| Expected Benefit | Productivity, consistency, cost reduction, risk reduction, or decision support |
| Deployment Model | Local, internal, SaaS, cloud-hosted, vendor-hosted, or hybrid |
| AI Capability | Search, summarization, question answering, classification, generation, automation, or decision support |
| Target Launch Date | Expected implementation or pilot date |
| Review Status | Draft, under review, approved, rejected, or deferred |

## Example Use Case

| Field | Example |
|---|---|
| Use Case Name | Internal Security Policy AI Assistant |
| Business Owner | Security Architecture |
| Technical Owner | Platform Engineering |
| Security Owner | Cloud Security Architecture |
| Data Owner | Security Governance |
| Intended Users | Security architects, engineers, compliance analysts, business analysts |
| Business Purpose | Help employees find approved security and architecture guidance faster |
| Expected Benefit | Reduced manual search time and improved guidance consistency |
| Deployment Model | Local prototype first; cloud reference design only |
| AI Capability | Retrieval-Augmented Generation |
| Review Status | Limited pilot |

## Data Risk Assessment

Data is one of the most important parts of AI risk assessment. The system must identify what data the AI will access, retrieve, process, store, log, or generate.

## Data Categories

| Data Category | Description | Example |
|---|---|---|
| Public Data | Data approved for external release | Public documentation |
| Internal Data | General internal business data | Internal FAQs, general procedures |
| Confidential Data | Sensitive internal information | Architecture diagrams, risk assessments |
| Restricted Data | Highly sensitive data limited to specific roles | Incident response procedures, audit findings |
| Regulated Data | Data subject to legal, regulatory, or contractual rules | Customer data, payment data, personal data |
| Secrets | Credentials or cryptographic material | API keys, passwords, private keys |
| Production Data | Live operational or customer-impacting data | Production logs, transaction records |

## Data Risk Questions

| Question | Risk Consideration |
|---|---|
| Will the AI system access internal documents? | Requires document classification and access control |
| Will the system process confidential data? | Requires stronger controls and approval |
| Will the system process regulated data? | Requires privacy, legal, and compliance review |
| Will prompts or responses be logged? | Requires log minimization and retention rules |
| Will data be sent to a third-party provider? | Requires vendor and contractual review |
| Will data be used for model training? | Requires explicit approval and governance |
| Will data include credentials or secrets? | Should be prohibited |
| Will real production data be used in testing? | Should be avoided unless approved |
| Will data be retained after processing? | Requires retention and deletion rules |

## Data Risk Rating

| Rating | Criteria |
|---|---|
| Low | Uses public or low-risk internal data only |
| Medium | Uses internal business data or approved internal documents |
| High | Uses confidential or restricted documents |
| Critical | Uses regulated data, secrets, customer data, payment data, or production-sensitive data |

## Data Risk Controls

| Risk | Required Control |
|---|---|
| Unauthorized data exposure | Document-level access control |
| Sensitive data in prompts | Prompt filtering and user warnings |
| Sensitive data in responses | Output validation and redaction |
| Sensitive data in logs | Log minimization and restricted log access |
| Vendor data retention | Provider data handling review |
| Data used for training | Explicit opt-in approval and legal review |
| Unclassified documents | Deny ingestion until classified |
| Expired documents | Block or flag retrieval until reviewed |

## Identity and Access Risk Assessment

AI systems must enforce who can use the system, what they can retrieve, and what actions they can request.

## Access Risk Questions

| Question | Risk Consideration |
|---|---|
| Will access require authentication? | Anonymous access should not be allowed |
| Will access use enterprise SSO? | Required for enterprise accountability |
| Will MFA be required? | Recommended for all users |
| Will users have different document access levels? | Requires role and metadata-based controls |
| Can administrators access all content? | Separation of duties should prevent automatic content access |
| Can users request restricted documents through prompts? | Requires prompt filtering and retrieval authorization |
| Can the AI system take actions on behalf of users? | Requires human approval and least privilege |
| Are privileged users reviewed regularly? | Required for governance and audit |

## Access Risk Rating

| Rating | Criteria |
|---|---|
| Low | Read-only access to general internal content |
| Medium | Role-based access to multiple internal document categories |
| High | Access to confidential, IAM, security, or compliance documents |
| Critical | Access to restricted data, privileged workflows, or production-impacting functions |

## Access Risk Controls

| Risk | Required Control |
|---|---|
| Unauthorized user access | SSO, MFA, and session management |
| Role impersonation | Server-side identity validation |
| Unauthorized document retrieval | Document-level authorization |
| Overprivileged users | Least privilege and access reviews |
| Admin overreach | Separation of duties |
| Prompt-based access bypass | Prompt injection controls |
| Stale access | Identity lifecycle integration |
| Privileged actions | Human approval and administrative logging |

## Prompt and Model Behavior Risk Assessment

AI systems introduce risks because natural language input can influence model behavior.

## Prompt and Model Risk Questions

| Question | Risk Consideration |
|---|---|
| Could users attempt prompt injection? | Assume yes for all LLM systems |
| Could retrieved documents contain malicious instructions? | Requires content review and context isolation |
| Could the model reveal hidden instructions? | Requires system prompt leakage controls |
| Could the model generate unsupported answers? | Requires source citation and validation |
| Could users rely on AI output as final authority? | Requires disclaimers and human review |
| Could the model produce unsafe recommendations? | Requires output validation |
| Could the model be connected to tools or APIs? | Requires excessive agency review |
| Could model output be used downstream? | Requires improper output handling controls |

## Prompt and Model Risk Rating

| Rating | Criteria |
|---|---|
| Low | AI provides simple summaries from approved low-risk content |
| Medium | AI answers internal process or policy questions with source references |
| High | AI provides security, IAM, compliance, or operational guidance |
| Critical | AI can influence production actions, access approvals, legal decisions, or customer-impacting activity |

## Prompt and Model Risk Controls

| Risk | Required Control |
|---|---|
| Prompt injection | Input filtering, context isolation, and testing |
| System prompt leakage | Refusal behavior and output filtering |
| Hallucination | Source citation and unsupported-claim detection |
| Unsafe output | Response validation and human review |
| Overreliance | Advisory-only language and escalation guidance |
| Excessive agency | Read-only design and human approval |
| Indirect injection | Approved document ingestion and content scanning |
| Unsupported claims | Require retrieved source support |

## Vendor and Supply Chain Risk Assessment

Many AI systems depend on third-party providers, open-source libraries, models, APIs, embeddings, or document processing tools.

## Vendor Risk Questions

| Question | Risk Consideration |
|---|---|
| Is a third-party AI provider used? | Requires vendor review |
| Are prompts or responses retained by the provider? | Requires data handling review |
| Are prompts or responses used for training? | Should require explicit approval |
| Is the model hosted externally? | Requires privacy, contractual, and security review |
| Are open-source libraries used? | Requires dependency scanning |
| Are embeddings or vector databases used? | Requires data protection review |
| Are browser extensions or plugins involved? | Requires endpoint and data leakage review |
| Is there a service level dependency? | Requires availability and contingency planning |

## Vendor Risk Rating

| Rating | Criteria |
|---|---|
| Low | Local-only tools with no external data transfer |
| Medium | Approved internal tools or low-risk vendor services |
| High | Third-party model provider receives internal data |
| Critical | Third-party provider receives confidential, regulated, or production-sensitive data |

## Vendor Risk Controls

| Risk | Required Control |
|---|---|
| Unapproved provider use | Approved vendor list |
| Provider data retention | Contract and privacy review |
| Training on enterprise data | Explicit prohibition or approval |
| Dependency vulnerabilities | Dependency scanning and version pinning |
| Untrusted model source | Model provenance review |
| Vendor outage | Contingency planning |
| Plugin or extension risk | Restrict unapproved plugins |
| Lack of auditability | Logging and contractual evidence requirements |

## Operational Risk Assessment

Operational risks include availability, performance, cost, support, and change management.

## Operational Risk Questions

| Question | Risk Consideration |
|---|---|
| Is the system business-critical? | Requires availability planning |
| What happens if the model is unavailable? | Requires fallback process |
| Could usage create high cost? | Requires quotas and cost alerts |
| Could logs become too large or expensive? | Requires log filtering and retention |
| Who supports the system? | Requires ownership model |
| How are documents updated? | Requires change control |
| How are incorrect answers corrected? | Requires feedback loop |
| How are users trained? | Requires acceptable use guidance |
| How is the system disabled if needed? | Requires kill switch or rollback plan |

## Operational Risk Rating

| Rating | Criteria |
|---|---|
| Low | Local prototype or non-critical internal pilot |
| Medium | Internal productivity tool with limited user group |
| High | Broad internal deployment or dependency for operational workflows |
| Critical | Production-critical system or system that affects customer, financial, legal, or security outcomes |

## Operational Risk Controls

| Risk | Required Control |
|---|---|
| Service outage | Fallback to source documents |
| High cost | Budget alerts, quotas, and rate limits |
| Usage abuse | Monitoring and throttling |
| Incorrect responses | Feedback loop and human review |
| Stale documents | Content owner review cycle |
| Support gaps | Defined operational owner |
| Change risk | Change management process |
| Emergency shutdown need | Kill switch or disablement process |

## Compliance and Governance Risk Assessment

AI systems in regulated environments must support auditability, control mapping, and accountability.

## Compliance Risk Questions

| Question | Risk Consideration |
|---|---|
| Does the system support audit evidence? | Requires logging and retention |
| Are AI decisions explainable? | Requires source references |
| Are humans accountable for high-risk decisions? | Requires human review |
| Does the system process regulated data? | Requires compliance review |
| Are policies mapped to controls? | Requires control mapping |
| Is there a documented owner? | Required for governance |
| Is there an acceptable use policy? | Required for user guidance |
| Are exceptions tracked? | Required for audit readiness |
| Are risks reviewed periodically? | Required for ongoing governance |

## Compliance Risk Rating

| Rating | Criteria |
|---|---|
| Low | No regulated data and no compliance-impacting decisions |
| Medium | Internal compliance guidance only |
| High | AI output influences control interpretation or audit preparation |
| Critical | AI output affects regulatory reporting, legal conclusions, access approvals, or customer-impacting decisions |

## Compliance Risk Controls

| Risk | Required Control |
|---|---|
| Weak auditability | Structured logging and evidence retention |
| Unsupported compliance claims | Source citation and human review |
| Unclear accountability | Named business, data, and security owners |
| Policy exceptions | Exception workflow and approval tracking |
| Misaligned controls | Compliance mapping |
| Regulatory exposure | Legal and compliance review |
| Shadow AI usage | Approved AI use case registry |
| Inconsistent decisions | Standardized review process |

## Risk Scoring Method

This project uses a simple qualitative scoring model.

Each risk domain is scored from 1 to 4.

| Score | Rating | Description |
|---|---|---|
| 1 | Low | Limited risk, standard controls sufficient |
| 2 | Medium | Some risk, documented controls required |
| 3 | High | Significant risk, security/governance review required |
| 4 | Critical | Major risk, executive, legal, privacy, or compliance review may be required |

## Risk Domains

| Domain | Score |
|---|---|
| Data Risk | 1 to 4 |
| Access Risk | 1 to 4 |
| Prompt and Model Risk | 1 to 4 |
| Vendor Risk | 1 to 4 |
| Operational Risk | 1 to 4 |
| Compliance Risk | 1 to 4 |

## Overall Risk Rating

| Total Score | Overall Rating | Required Action |
|---|---|---|
| 6 to 8 | Low | May proceed with standard controls |
| 9 to 13 | Medium | May proceed with documented controls and owner approval |
| 14 to 18 | High | Requires security architecture and governance review |
| 19 to 24 | Critical | Requires escalation to security, privacy, legal, compliance, and executive stakeholders |

## Example Risk Assessment: Internal AI Policy Assistant

| Domain | Score | Rating | Rationale |
|---|---|---|---|
| Data Risk | 2 | Medium | Uses approved internal documents |
| Access Risk | 3 | High | Different users may access different document categories |
| Prompt and Model Risk | 3 | High | Prompt injection and hallucination are likely risks |
| Vendor Risk | 1 | Low | Initial prototype is local-only |
| Operational Risk | 2 | Medium | Internal pilot with limited users |
| Compliance Risk | 3 | High | May influence compliance or security interpretation |

Total Score: 14

Overall Rating: High

Decision: Limited pilot approved with required controls.

## Required Controls for Example Use Case

| Control Area | Required Control |
|---|---|
| Data | Use mock or approved internal documents only |
| Access | Enforce role-based document access |
| Prompt Security | Implement prompt injection detection |
| Retrieval | Filter documents by classification and role |
| Response | Require source references |
| Logging | Log prompt metadata, retrieval decisions, and blocked attempts |
| Human Review | Require review for security exceptions or compliance decisions |
| Cost | Keep local-only for initial phase |
| Governance | Assign business, data, and security owners |

## AI Use Case Approval Checklist

| Checklist Item | Status |
|---|---|
| Business owner identified | Not Started |
| Technical owner identified | Not Started |
| Security owner identified | Not Started |
| Data owner identified | Not Started |
| Business purpose documented | Not Started |
| Data categories identified | Not Started |
| Data classification completed | Not Started |
| User roles identified | Not Started |
| Access model defined | Not Started |
| Prompt injection risks reviewed | Not Started |
| Logging requirements defined | Not Started |
| Human review requirements defined | Not Started |
| Vendor review completed if applicable | Not Started |
| Cost controls defined if applicable | Not Started |
| Compliance mapping completed | Not Started |
| Risk rating assigned | Not Started |
| Approval decision documented | Not Started |

## Approval Roles

| Role | Responsibility |
|---|---|
| Business Owner | Confirms business need and expected value |
| Data Owner | Approves use of data or documents |
| Security Architect | Reviews security design and control requirements |
| IAM Owner | Reviews identity and access requirements |
| Privacy or Legal | Reviews regulated, personal, or contractual data concerns |
| Compliance Owner | Reviews control mapping and audit implications |
| Platform Owner | Reviews operational and technical implementation |
| AI Governance Review Group | Approves, rejects, or escalates AI use case |

## Risk Treatment Options

| Treatment | Description |
|---|---|
| Accept | Risk is understood and accepted by accountable owner |
| Mitigate | Controls are implemented to reduce risk |
| Transfer | Risk is managed through vendor, contract, or insurance |
| Avoid | Use case is rejected or redesigned |
| Defer | Decision delayed until more information is available |

## Risk Register

| Risk ID | Risk Description | Domain | Rating | Owner | Treatment | Status |
|---|---|---|---|---|---|---|
| AI-RISK-001 | Prompt injection may cause unsafe or unauthorized output | Prompt and Model | High | Security Architecture | Mitigate | Open |
| AI-RISK-002 | User may retrieve documents outside authorized scope | Access | High | IAM and Security Architecture | Mitigate | Open |
| AI-RISK-003 | Sensitive data may be entered into prompts | Data | High | Data Owner and Security | Mitigate | Open |
| AI-RISK-004 | AI-generated response may be inaccurate or unsupported | Prompt and Model | High | Business Owner | Mitigate | Open |
| AI-RISK-005 | Logs may capture sensitive prompt or response data | Data | Medium | Security Operations | Mitigate | Open |
| AI-RISK-006 | External provider may retain enterprise data | Vendor | High | Vendor Risk Management | Avoid or Mitigate | Open |
| AI-RISK-007 | Usage may create unexpected cloud or API costs | Operational | Medium | Platform Owner | Mitigate | Open |
| AI-RISK-008 | AI output may be treated as final approval | Compliance | High | Governance Owner | Mitigate | Open |

## Human Review Triggers

Human review should be required when a prompt or response involves:

- Security exceptions
- IAM access approval
- Privileged access decisions
- Legal interpretation
- Regulatory interpretation
- Audit evidence conclusions
- Customer-impacting decisions
- Production change recommendations
- Incident response recommendations
- Restricted or regulated data
- Unsupported or low-confidence AI output
- Prompt injection attempts
- Policy conflict or ambiguity

## Prohibited Use Cases

The following use cases should not be approved without significant additional governance and executive review:

- Processing real customer account data in an unapproved AI system
- Entering production secrets or credentials into prompts
- Allowing AI to approve access requests
- Allowing AI to modify production systems
- Allowing AI to make final legal or regulatory decisions
- Using unapproved AI tools for confidential data
- Training a model on restricted enterprise data without approval
- Connecting the assistant to unrestricted document repositories
- Using AI output as the sole basis for audit conclusions
- Allowing anonymous access to the AI assistant

## Approved Pilot Use Cases

The following use cases are appropriate for a controlled pilot:

- Answering questions from mock security policies
- Summarizing approved internal architecture standards
- Helping users find cloud logging guidance
- Explaining documented AI acceptable use rules
- Mapping sample AI risks to governance controls
- Demonstrating role-based retrieval using sample documents
- Testing prompt injection controls with mock data
- Generating advisory-only responses with source references

## Risk Review Frequency

AI use cases should be reviewed periodically.

| Review Type | Frequency |
|---|---|
| Pilot Review | Before and after pilot |
| Access Review | Quarterly or semi-annually depending on sensitivity |
| Data Review | At least annually or when documents change |
| Vendor Review | Annually or upon contract/model change |
| Security Review | At least annually or upon architecture change |
| Compliance Review | At least annually or before audit use |
| Model Behavior Review | Periodically based on usage and risk |
| Incident Review | After any AI-related incident |

## Evidence Required for Approval

Before approving an AI use case, the following evidence should be available:

- Business case
- Use case intake form
- Data classification review
- Access control model
- Threat model
- Prompt injection control strategy
- Logging and monitoring requirements
- Human review process
- Vendor review if applicable
- Cost control plan if paid services are used
- Compliance mapping if used in regulated workflow
- Risk rating and decision record

## Local Prototype Risk Posture

The initial local prototype for this project should be considered lower risk because it:

- Uses mock data
- Uses local files
- Does not use paid cloud services
- Does not process customer data
- Does not process regulated data
- Does not approve real business decisions
- Does not modify production systems
- Does not connect to live enterprise repositories

However, the local prototype should still demonstrate strong governance concepts, including role-based access, prompt injection testing, logging, and human review simulation.

## Cloud Deployment Risk Posture

Any future cloud deployment increases risk and requires additional review.

Additional risks include:

- Cloud cost exposure
- External model provider data handling
- Cloud IAM misconfiguration
- Logging and retention cost
- Network exposure
- Vendor dependency
- Region and data residency considerations
- API key or credential management
- Production data exposure

Cloud deployment should not occur until budgets, alerts, teardown steps, access controls, and data handling requirements are documented.

## Security Architect Notes

The AI risk assessment should be completed before implementation, not after deployment.

For AI systems, the most important governance question is not simply whether the model works. The more important questions are:

- What data can it access?
- Who can use it?
- What can it influence?
- What can go wrong?
- Who is accountable?
- What evidence exists if something fails?
- What controls prevent misuse?
- What happens when the AI is wrong?

## Conclusion

AI systems should be evaluated as enterprise risk systems, not just productivity tools.

A secure AI assistant requires documented ownership, data classification, access control, prompt security, logging, human review, compliance mapping, vendor review, and cost governance.

The recommended starting point is a limited local pilot using mock data, followed by controlled expansion only after risks and controls are reviewed.
