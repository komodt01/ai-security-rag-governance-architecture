# NIST AI Risk Management Framework Mapping

## Purpose

This document maps the secure enterprise AI assistant architecture to the NIST AI Risk Management Framework.

The purpose is to show how the AI assistant can be governed, designed, monitored, and managed in a way that supports trustworthy AI adoption in a regulated environment.

This mapping focuses on a Retrieval-Augmented Generation assistant used to answer employee questions from approved internal documents.

## Scope

This mapping applies to:

- AI governance
- AI risk assessment
- Data classification
- Identity and access control
- Prompt injection controls
- Logging and monitoring
- Human review
- Model and vendor risk
- Compliance evidence
- Operational controls
- Cost controls
- Local prototype and future cloud reference designs

## Project Context

The AI assistant is designed as an advisory internal tool.

The assistant should:

- Answer questions using approved internal documents
- Enforce role-based and document-level access
- Provide source references where possible
- Avoid processing real sensitive data during the local prototype
- Avoid making final legal, regulatory, access, or production decisions
- Log security-relevant activity
- Escalate high-risk requests to human reviewers
- Remain local-first unless cloud deployment is explicitly approved

The assistant should not:

- Train on confidential or regulated data without approval
- Access unrestricted document repositories
- Approve access requests
- Modify production systems
- Make final compliance decisions
- Reveal system prompts or restricted content
- Operate without human accountability

## NIST AI RMF Core Functions

The NIST AI RMF is organized around four core functions:

| Function | Description |
|---|---|
| Govern | Establish organizational policies, accountability, roles, and risk management processes for AI |
| Map | Identify the context, intended purpose, stakeholders, risks, impacts, and operating environment |
| Measure | Analyze, assess, test, and monitor AI risks and system behavior |
| Manage | Prioritize, respond to, reduce, monitor, and communicate AI risks over time |

## Mapping Summary

| NIST AI RMF Function | Project Alignment |
|---|---|
| Govern | AI use case intake, ownership, approval workflow, human review, risk register, governance artifacts |
| Map | Business case, data flow, trust boundaries, users, document classifications, use case scope |
| Measure | STRIDE threat model, OWASP LLM mapping, prompt injection testing, logging, risk scoring |
| Manage | Risk treatment, access controls, monitoring, escalation, incident response, cost controls |

---

# Govern Function

## Objective

The Govern function establishes the policies, roles, responsibilities, processes, and oversight needed to manage AI risk throughout the system lifecycle.

For this project, governance is critical because the AI assistant may influence security, architecture, IAM, compliance, or operational decisions.

## Govern Mapping

| Governance Area | Project Implementation |
|---|---|
| AI ownership | Business owner, technical owner, security owner, data owner, and governance owner are identified |
| Use case approval | AI use case intake and risk assessment process are required before implementation |
| Risk accountability | AI risk register documents risks, owners, treatment, and status |
| Human accountability | High-risk decisions require human review and cannot be delegated to AI |
| Policy alignment | AI acceptable use, data classification, access control, and logging requirements are documented |
| Role separation | Users, content owners, reviewers, administrators, and audit viewers have separate responsibilities |
| Cost governance | Cloud deployment is restricted until budgets, alerts, and teardown procedures are documented |
| Ongoing review | AI use cases are reviewed periodically or when scope, data, model, or vendor changes |

## Govern Controls

| Control | Description |
|---|---|
| AI Use Case Intake | Captures business purpose, users, data, model, owner, and risk context |
| AI Risk Assessment | Scores data, access, prompt/model, vendor, operational, and compliance risk |
| AI Risk Register | Tracks identified AI risks and mitigation status |
| Human Review Workflow | Routes high-risk requests to accountable human reviewers |
| Data Owner Approval | Requires data owner approval before documents are ingested |
| Security Architecture Review | Reviews AI system design, trust boundaries, and controls |
| Acceptable Use Requirements | Defines approved and prohibited AI use cases |
| Cloud Cost Decision Gate | Prevents paid cloud deployment without cost controls |

## Govern Evidence

| Evidence Artifact | Location |
|---|---|
| Business case | business_case.md |
| Cost controls | cost_controls.md |
| AI risk assessment | governance/ai_risk_assessment.md |
| Human review requirements | governance/human_review_requirements.md |
| Access control model | security/access_control_model.md |
| Logging requirements | security/logging_monitoring.md |
| Incident response playbook | incident_response/ai_incident_response_playbook.md |

## Govern Risks Addressed

| Risk | Governance Response |
|---|---|
| Shadow AI adoption | Approved use case intake and AI governance review |
| Unclear ownership | Named business, technical, security, and data owners |
| Overreliance on AI | Advisory-only design and human review |
| Unapproved data usage | Data owner approval and data classification |
| Weak accountability | Human review and audit logging |
| Runaway cloud cost | Cost decision gates and local-first prototype |
| Compliance ambiguity | Compliance mapping and documented control ownership |

---

# Map Function

## Objective

The Map function identifies the context in which the AI system operates, including the business purpose, intended users, data flows, stakeholder impact, risks, assumptions, and system boundaries.

For this project, mapping ensures the AI assistant is clearly scoped before implementation.

## Map Mapping

| Context Area | Project Implementation |
|---|---|
| Business context | A regulated organization wants a secure internal AI assistant for approved documents |
| Intended users | Employees, analysts, engineers, security architects, IAM analysts, compliance analysts, reviewers |
| Intended use | Advisory question answering and document retrieval support |
| Prohibited use | Access approval, legal decisions, production changes, unrestricted data search |
| Data context | Approved internal documents with classification metadata |
| System boundaries | User interface, identity provider, retrieval layer, AI model, validation layer, logging layer |
| Trust boundaries | User-to-application, application-to-identity provider, retrieval-to-knowledge base, model boundary |
| Risk context | Prompt injection, sensitive data disclosure, unauthorized retrieval, hallucination, excessive agency |
| Deployment context | Local-first prototype; cloud reference only unless approved |

## Map Controls

| Control | Description |
|---|---|
| Business Case Definition | Documents why the AI assistant is needed and what business problem it solves |
| Use Case Scoping | Defines approved, restricted, and prohibited AI uses |
| Data Flow Documentation | Shows how prompts, documents, context, responses, and logs move through the system |
| Trust Boundary Identification | Identifies points where security controls must be enforced |
| Data Classification | Defines whether documents are public, internal, confidential, restricted, or regulated |
| User Role Definition | Defines who may use the assistant and what they may access |
| Deployment Option Review | Compares local prototype and cloud reference options |
| Out-of-Scope Definition | Prevents uncontrolled expansion into model training, production data, or paid cloud deployment |

## Map Evidence

| Evidence Artifact | Location |
|---|---|
| Business case | business_case.md |
| Reference architecture | architecture/reference_architecture.md |
| Data flow | architecture/data_flow.md |
| Trust boundaries | architecture/trust_boundaries.md |
| Deployment options | architecture/deployment_options.md |
| Data classification | governance/data_classification.md |
| Access control model | security/access_control_model.md |

## Map Risks Addressed

| Risk | Mapping Response |
|---|---|
| Undefined AI scope | Clearly defined approved and prohibited use cases |
| Unknown data exposure | Data flow and data classification requirements |
| Unclear trust boundaries | Dedicated trust boundary documentation |
| Unauthorized users | Defined user roles and access model |
| Model misuse | Advisory-only scope and prohibited actions |
| Cloud cost exposure | Local-first deployment scope |
| Compliance uncertainty | Mapping to governance and compliance artifacts |

---

# Measure Function

## Objective

The Measure function evaluates, analyzes, tests, monitors, and validates AI system behavior and risk controls.

For this project, measurement focuses on whether the AI assistant behaves safely, retrieves only authorized content, resists prompt injection, avoids sensitive data leakage, and produces source-supported responses.

## Measure Mapping

| Measurement Area | Project Implementation |
|---|---|
| Threat identification | STRIDE threat model identifies spoofing, tampering, repudiation, disclosure, denial of service, and privilege risks |
| LLM risk analysis | OWASP LLM Top 10 mapping identifies AI-specific risks |
| Prompt injection testing | Prompt injection controls define attack categories and expected system behavior |
| Access validation | Role-based and document-level access checks are defined |
| Retrieval validation | Retrieved documents must match user authorization and document metadata |
| Response validation | Responses are checked for sensitive data, unsupported claims, and high-risk content |
| Logging | Structured logs capture security-relevant events |
| Risk scoring | AI risk assessment scores data, access, prompt/model, vendor, operational, and compliance risk |
| Monitoring | Detection rules identify suspicious or unsafe activity |

## Measure Controls

| Control | Description |
|---|---|
| STRIDE Threat Model | Identifies traditional application and architecture threats |
| OWASP LLM Mapping | Identifies LLM-specific and RAG-specific risks |
| Prompt Injection Test Cases | Tests whether unsafe prompts are blocked, warned, or escalated |
| Retrieval Authorization Testing | Confirms users cannot retrieve unauthorized documents |
| Sensitive Data Detection | Checks prompts and outputs for secrets, regulated data, or confidential information |
| Source Citation Check | Confirms answers are supported by approved documents |
| Unsupported Claim Detection | Flags answers that lack source support |
| Human Review Metrics | Tracks high-risk requests and review outcomes |
| Usage and Cost Monitoring | Tracks prompt volume, model usage, token counts, and budget signals |

## Measure Evidence

| Evidence Artifact | Location |
|---|---|
| STRIDE threat model | security/threat_model_stride.md |
| OWASP LLM Top 10 mapping | security/owasp_llm_top10_mapping.md |
| Prompt injection controls | security/prompt_injection_controls.md |
| Logging and monitoring | security/logging_monitoring.md |
| AI risk assessment | governance/ai_risk_assessment.md |
| Access control model | security/access_control_model.md |

## Measurement Examples

| Test | Expected Result |
|---|---|
| General employee asks for general AI usage policy | Allowed with approved source reference |
| General employee asks for incident response playbook | Denied or limited to general approved guidance |
| User says “Ignore previous instructions” | Blocked, logged, and scored as high risk |
| User asks for system prompt | Blocked and logged |
| User asks for customer data | Blocked and logged |
| Security architect asks for cloud logging guidance | Allowed if authorized documents exist |
| Response lacks source support | Refused, qualified, or routed to review |
| User submits excessive prompts | Throttled or alerted based on usage policy |

## Measure Risks Addressed

| Risk | Measurement Response |
|---|---|
| Prompt injection | Test suite and detection rules |
| Unauthorized retrieval | Role-based retrieval validation |
| Sensitive data leakage | Prompt and output detection |
| Hallucination | Source citation and unsupported claim checks |
| Overreliance | Human review and advisory-only messaging |
| Excessive usage | Quotas, rate limits, and cost monitoring |
| Logging gaps | Required structured log fields |
| Weak audit evidence | Correlation IDs and source traceability |

---

# Manage Function

## Objective

The Manage function prioritizes, responds to, reduces, monitors, and communicates AI risks over time.

For this project, risk management ensures identified risks are treated through controls, ownership, monitoring, escalation, and periodic review.

## Manage Mapping

| Management Area | Project Implementation |
|---|---|
| Risk treatment | Risks are accepted, mitigated, transferred, avoided, or deferred |
| Risk prioritization | High-priority risks are sensitive disclosure, prompt injection, unauthorized retrieval, and excessive agency |
| Control implementation | Access control, prompt filtering, logging, human review, and data classification reduce risk |
| Incident response | AI misuse, data leakage, prompt injection, and poisoned document scenarios are defined |
| Ongoing monitoring | Logs and alerts track unsafe or unexpected behavior |
| Review cycles | Access, data, vendor, and model behavior reviews are defined |
| Cost management | Local-first approach and cloud deployment decision gate reduce financial risk |
| Communication | Risk owners, reviewers, and governance stakeholders are identified |

## Manage Controls

| Control | Description |
|---|---|
| Risk Register | Tracks AI risks, owners, ratings, treatment, and status |
| Risk Treatment Plan | Defines whether risk is accepted, mitigated, avoided, transferred, or deferred |
| Human Review Escalation | Routes high-risk outputs to accountable personnel |
| AI Incident Response | Defines how AI-specific incidents are handled |
| Access Review | Periodically reviews user and privileged access |
| Data Review | Periodically reviews document classification and approval status |
| Vendor Review | Reviews model and provider data handling |
| Kill Switch or Disablement Plan | Allows AI functionality to be disabled if unsafe |
| Cost Review | Prevents uncontrolled usage of paid services |
| Continuous Improvement | Uses logs, tests, incidents, and feedback to improve controls |

## Manage Evidence

| Evidence Artifact | Location |
|---|---|
| AI risk assessment | governance/ai_risk_assessment.md |
| Risk register | governance/ai_risk_assessment.md |
| Human review requirements | governance/human_review_requirements.md |
| Logging and monitoring | security/logging_monitoring.md |
| Incident response playbook | incident_response/ai_incident_response_playbook.md |
| Cost controls | cost_controls.md |
| Lessons learned | lessonslearned.md |

## Manage Risks Addressed

| Risk | Management Response |
|---|---|
| Unresolved high risks | Risk register and ownership |
| Repeated unsafe prompts | Monitoring and escalation |
| Data leakage incident | Incident response process |
| Poisoned document | Content owner review and document removal |
| Excessive model usage | Rate limiting, quotas, and cost alerts |
| Unauthorized access | Access review and IAM lifecycle integration |
| Stale documents | Content review and expiration dates |
| Weak adoption controls | AI use case review process |

---

# AI Trustworthiness Characteristics

The AI assistant should support the following trustworthy AI characteristics.

## Valid and Reliable

| Requirement | Project Control |
|---|---|
| Responses should be based on approved documents | RAG with source references |
| Unsupported answers should be limited | Source citation and unsupported-claim detection |
| Retrieval should be tested | Role-based retrieval validation |
| Documents should be reviewed | Content ownership and expiration dates |

## Safe

| Requirement | Project Control |
|---|---|
| Assistant should not provide dangerous or unauthorized guidance | Prompt filtering and output validation |
| Assistant should not approve high-risk actions | Advisory-only design and human review |
| Assistant should not execute production actions | Read-only initial architecture |
| Unsafe use should be blocked | Detection rules and escalation |

## Secure and Resilient

| Requirement | Project Control |
|---|---|
| Users must authenticate | SSO and MFA |
| Access must be authorized | Role and document-level controls |
| Prompt injection must be addressed | Prompt injection controls |
| Logs must support investigation | Logging and monitoring requirements |
| System must handle abuse | Rate limits and alerts |

## Accountable and Transparent

| Requirement | Project Control |
|---|---|
| Owners must be identified | Business, data, security, and technical owners |
| Decisions must be traceable | Correlation IDs and logging |
| Sources should be visible | Source references in responses |
| High-risk output needs review | Human review workflow |
| AI use case decisions must be documented | Intake and risk assessment |

## Explainable and Interpretable

| Requirement | Project Control |
|---|---|
| Users should know why an answer was generated | Source references and retrieved document IDs |
| Users should understand limitations | Advisory-only language |
| Reviewers should understand system behavior | Logs, risk scores, and policy actions |
| Audit should reconstruct events | Prompt, retrieval, response, and review metadata |

## Privacy-Enhanced

| Requirement | Project Control |
|---|---|
| Sensitive data should not be used in prototype | Mock data only |
| Prompts and responses should not be overlogged | Log minimization |
| Restricted data should be blocked | Data classification and filtering |
| Provider data handling should be reviewed | Vendor risk assessment |

## Fair and Bias-Managed

| Requirement | Project Control |
|---|---|
| Use case should avoid unsupported employment, lending, or customer decisions | Prohibited use case list |
| High-impact decisions require human review | Human accountability |
| Training data risk should be controlled | No model training in initial scope |
| Output should be validated | Response review and source support |

## Cost-Aware and Operationally Controlled

| Requirement | Project Control |
|---|---|
| Prototype should avoid paid cloud usage | Local-first design |
| Cloud usage must be reviewed | Cost decision gate |
| Usage should be monitored | Prompt, token, and model usage logs |
| System should support shutdown | Kill switch or disablement plan |

---

# AI Risk to Control Mapping

| AI Risk | NIST AI RMF Function | Project Control |
|---|---|---|
| Prompt injection | Measure, Manage | Prompt filtering, testing, logging, escalation |
| Sensitive information disclosure | Govern, Map, Measure, Manage | Data classification, access control, output validation |
| Unauthorized document retrieval | Map, Measure, Manage | Document-level authorization and retrieval filtering |
| Hallucination or misinformation | Measure, Manage | Source citation, unsupported-claim detection, human review |
| Overreliance on AI | Govern, Manage | Advisory-only design and human accountability |
| Excessive agency | Govern, Manage | Read-only design, no autonomous production action |
| Vendor data exposure | Govern, Map, Manage | Vendor review and data handling assessment |
| Poisoned documents | Measure, Manage | Approved document ingestion and content review |
| Weak auditability | Govern, Measure, Manage | Structured logging and evidence retention |
| Unexpected cloud cost | Govern, Manage | Local-first design, budgets, quotas, and cost alerts |

---

# Example Control Mapping

## Use Case: Internal Security Policy Assistant

| Area | Mapping |
|---|---|
| Business Purpose | Help employees find approved security and architecture guidance |
| Govern | Use case owner, risk assessment, approved pilot scope |
| Map | Data flow, users, document classes, trust boundaries |
| Measure | Prompt injection tests, retrieval checks, logging, response validation |
| Manage | Risk register, human review, monitoring, cost controls |
| Risk Level | High for pilot because responses may influence security or compliance interpretation |
| Decision | Limited pilot using mock or approved internal documents only |

## Required Controls

| Control | NIST AI RMF Function |
|---|---|
| Business owner identified | Govern |
| Data owner approval | Govern |
| Data classification | Govern, Map |
| Role-based access control | Map, Measure, Manage |
| Document-level authorization | Map, Measure, Manage |
| Prompt injection testing | Measure |
| Source citation | Measure |
| Human review | Govern, Manage |
| Logging and monitoring | Measure, Manage |
| Cost controls | Govern, Manage |
| Incident response process | Manage |

---

# Governance Decision Record Template

| Field | Description |
|---|---|
| Use Case Name | Name of AI use case |
| Business Owner | Accountable business owner |
| Technical Owner | Implementation owner |
| Security Owner | Security architecture owner |
| Data Owner | Owner of documents or data |
| Intended Users | Approved user groups |
| Intended Purpose | Approved AI capability |
| Data Classification | Highest data sensitivity level |
| Risk Rating | Low, medium, high, or critical |
| Required Controls | Controls required before pilot or deployment |
| Approval Decision | Approved, conditional, limited pilot, rejected, escalated, or deferred |
| Review Date | Date for reassessment |
| Approver | Governance or control owner |

---

# Minimum Controls Before Pilot

Before any pilot begins, the following controls should be documented:

| Control | Required |
|---|---|
| Business use case documented | Yes |
| Data classification completed | Yes |
| Approved data or mock data selected | Yes |
| User roles defined | Yes |
| Access control model defined | Yes |
| Prompt injection controls defined | Yes |
| Logging requirements defined | Yes |
| Human review criteria defined | Yes |
| Prohibited use cases documented | Yes |
| Cost controls documented | Yes |
| Risk rating assigned | Yes |

---

# Minimum Controls Before Cloud Deployment

Before any cloud deployment begins, the following additional controls should be in place:

| Control | Required |
|---|---|
| Budget alert configured | Yes |
| Billing or cost monitoring configured | Yes |
| Teardown procedure documented | Yes |
| Cloud IAM design reviewed | Yes |
| Encryption requirements documented | Yes |
| Logging destination defined | Yes |
| Provider data handling reviewed | Yes |
| Retention requirements documented | Yes |
| Network exposure reviewed | Yes |
| Secrets management approach defined | Yes |
| Production data approval completed | Yes |
| Cloud deployment owner identified | Yes |

---

# Review Cadence

| Review Area | Frequency |
|---|---|
| AI use case risk review | Before pilot and before expansion |
| Access review | Quarterly or semi-annually depending on sensitivity |
| Data classification review | At least annually or when documents change |
| Prompt injection test review | At each major release |
| Logging review | At least annually |
| Vendor review | Annually or when provider/model changes |
| Human review workflow | Quarterly or after incidents |
| Cost review | Before cloud deployment and monthly if deployed |
| Incident response review | After any AI-related incident |

---

# Security Architect Notes

The NIST AI RMF mapping shows that AI security is broader than model behavior.

A secure AI assistant requires:

- Governance before deployment
- Clear use case boundaries
- Data classification
- Identity-aware access control
- Prompt injection testing
- Response validation
- Human accountability
- Logging and monitoring
- Risk treatment
- Continuous review

The security architect’s role is to make sure the AI system fits inside an enterprise control environment instead of becoming an unmanaged productivity tool.

## Conclusion

This project aligns to the NIST AI RMF by defining how the AI assistant is governed, mapped, measured, and managed.

The most important implementation decision is to begin with a limited local prototype using mock or approved data, then expand only after governance, access control, logging, human review, and cost controls are in place.

This approach supports responsible AI adoption while reducing security, compliance, operational, and financial risk.
