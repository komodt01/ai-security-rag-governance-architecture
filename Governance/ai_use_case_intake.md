# AI Use Case Intake

## Purpose

This document provides a structured intake process for evaluating proposed AI use cases before design, pilot, or deployment.

The goal is to ensure that AI initiatives are reviewed for business value, data sensitivity, access control, security risk, compliance impact, operational readiness, human accountability, vendor exposure, and cost risk before implementation.

This intake process supports responsible AI adoption in regulated environments.

## Scope

This intake applies to proposed AI use cases involving:

- Internal AI assistants
- Retrieval-Augmented Generation systems
- AI-enabled document search
- AI summarization
- AI-assisted compliance research
- AI-assisted security guidance
- AI-assisted architecture guidance
- AI-enabled workflow automation
- AI tools that process internal, confidential, restricted, or regulated data
- AI services delivered through third-party providers
- AI systems deployed locally, internally, through SaaS, or in cloud environments

## Intake Principle

No AI use case should move into implementation until the organization understands:

- What business problem the AI system solves
- What data the system will use
- Who will use the system
- What decisions the AI output may influence
- What risks the system introduces
- What controls are required
- Who owns the use case
- Who approves the use case
- How the system will be monitored
- What happens if the AI output is wrong

## Intake Decision Outcomes

| Decision | Description |
|---|---|
| Approved | Use case may proceed with documented controls |
| Approved with Conditions | Use case may proceed only after required controls are implemented |
| Limited Pilot | Use case may proceed in a controlled pilot with mock, public, or approved low-risk data |
| Escalated | Use case requires additional review from security, privacy, legal, compliance, risk, or architecture governance |
| Rejected | Use case should not proceed because risk is unacceptable |
| Deferred | More information is needed before a decision can be made |

## Section 1: Basic Use Case Information

| Field | Response |
|---|---|
| Use Case Name |  |
| Intake Date |  |
| Requestor |  |
| Business Unit |  |
| Business Owner |  |
| Technical Owner |  |
| Security Owner |  |
| Data Owner |  |
| Compliance Owner |  |
| Intended Launch or Pilot Date |  |
| Current Status | Draft / Under Review / Approved / Rejected / Deferred |
| Requested Decision | Pilot / Production / Vendor Review / Architecture Review / Other |

## Section 2: Business Purpose

| Question | Response |
|---|---|
| What business problem does this AI use case solve? |  |
| Why is AI needed instead of a traditional workflow or search tool? |  |
| What is the expected business benefit? |  |
| Who benefits from this use case? |  |
| What process, decision, or workflow will this improve? |  |
| What happens if this use case is not implemented? |  |
| Is this use case advisory, operational, customer-facing, or decision-making? |  |

## Business Value Categories

Select all that apply.

| Category | Selected |
|---|---|
| Productivity improvement |  |
| Faster document discovery |  |
| Improved consistency of guidance |  |
| Reduced manual research |  |
| Security risk reduction |  |
| Compliance support |  |
| Operational efficiency |  |
| Customer experience improvement |  |
| Cost reduction |  |
| Knowledge management |  |
| Incident response support |  |
| Architecture review support |  |
| Other |  |

## Section 3: AI Capability

| Question | Response |
|---|---|
| What type of AI capability is being proposed? |  |
| Is the AI system generative, predictive, classification-based, search-based, or automation-based? |  |
| Will the system use Retrieval-Augmented Generation? |  |
| Will the system summarize documents? |  |
| Will the system generate new content? |  |
| Will the system classify or score information? |  |
| Will the system make recommendations? |  |
| Will the system take actions through tools, APIs, or automation? |  |
| Will the system interact with external users or customers? |  |

## AI Capability Categories

| Capability | Description | Selected |
|---|---|---|
| Document Search | Finds relevant documents or passages |  |
| Summarization | Summarizes approved content |  |
| Question Answering | Answers questions using approved sources |  |
| Classification | Labels or categorizes information |  |
| Risk Scoring | Assigns risk or priority ratings |  |
| Content Generation | Generates new text, reports, or recommendations |  |
| Workflow Automation | Triggers actions or updates systems |  |
| Decision Support | Supports human decisions |  |
| Autonomous Decisioning | Makes decisions without human approval |  |

## Section 4: Intended Users

| Question | Response |
|---|---|
| Who will use the AI system? |  |
| Are users internal, external, contractors, customers, or partners? |  |
| What roles or groups need access? |  |
| Will all users have the same access level? |  |
| Are privileged users involved? |  |
| Will users need training before access? |  |
| Will access require approval? |  |
| Will access be temporary or permanent? |  |

## User Groups

| User Group | Access Needed | Notes |
|---|---|---|
| General Employees |  |  |
| Business Analysts |  |  |
| Engineers |  |  |
| Security Architects |  |  |
| IAM Analysts |  |  |
| Compliance Analysts |  |  |
| Legal |  |  |
| Risk Management |  |  |
| Security Operations |  |  |
| Executives |  |  |
| External Users |  |  |
| Customers |  |  |
| Contractors |  |  |
| Vendors |  |  |

## Section 5: Data and Document Scope

| Question | Response |
|---|---|
| What data or documents will the AI system access? |  |
| Where is the data stored today? |  |
| Who owns the data? |  |
| Has the data been classified? |  |
| Will the system use public data? |  |
| Will the system use internal data? |  |
| Will the system use confidential data? |  |
| Will the system use restricted data? |  |
| Will the system use regulated data? |  |
| Will the system use customer data? |  |
| Will the system use employee data? |  |
| Will the system use production data? |  |
| Will the system use secrets, credentials, or keys? |  |
| Will the system generate logs containing prompt or response content? |  |
| Will data be retained by the AI system or provider? |  |
| Will data be used to train or fine-tune a model? |  |

## Data Classification Checklist

| Data Type | Included? | Notes |
|---|---|---|
| Public data |  |  |
| Internal data |  |  |
| Confidential data |  |  |
| Restricted data |  |  |
| Regulated data |  |  |
| Customer data |  |  |
| Employee data |  |  |
| Payment data |  |  |
| Health data |  |  |
| Authentication data |  |  |
| Production logs |  |  |
| Source code |  |  |
| API keys or secrets |  |  |
| Legal documents |  |  |
| Audit findings |  |  |
| Incident response records |  |  |

## Section 6: Access Control Requirements

| Question | Response |
|---|---|
| Will users authenticate through enterprise SSO? |  |
| Will MFA be required? |  |
| What identity provider will be used? |  |
| What roles or groups will control access? |  |
| Will document-level authorization be required? |  |
| Will access differ by data classification? |  |
| Will privileged access be required? |  |
| Will administrators have separate access from content users? |  |
| Will access be reviewed periodically? |  |
| How will access be removed when users change roles or leave? |  |

## Access Control Checklist

| Control | Required? | Notes |
|---|---|---|
| SSO |  |  |
| MFA |  |  |
| Role-based access control |  |  |
| Attribute-based access control |  |  |
| Document-level authorization |  |  |
| Data classification enforcement |  |  |
| Least privilege |  |  |
| Deny by default |  |  |
| Privileged access review |  |  |
| Separation of duties |  |  |
| Access logging |  |  |

## Section 7: Prompt and Model Risk

| Question | Response |
|---|---|
| Could users attempt prompt injection? |  |
| Could retrieved documents contain malicious instructions? |  |
| Could the model reveal hidden instructions? |  |
| Could the model generate inaccurate or unsupported responses? |  |
| Could the output be misunderstood as final approval? |  |
| Could the system produce legal, compliance, security, or access guidance? |  |
| Could the AI output influence production changes? |  |
| Could the AI output influence customer-impacting decisions? |  |
| Will the model have access to tools, APIs, or automation? |  |
| Will the model be allowed to take actions? |  |

## Prompt Risk Checklist

| Risk | Present? | Required Control |
|---|---|---|
| Prompt injection |  | Prompt filtering and testing |
| System prompt leakage |  | Refusal behavior and output filtering |
| Sensitive prompt data |  | Data loss prevention and redaction |
| Unsupported responses |  | Source citation and validation |
| Overreliance |  | Advisory-only language and human review |
| Excessive agency |  | Read-only design and approval workflow |
| Unsafe recommendations |  | Human review and output validation |
| Indirect prompt injection |  | Approved document ingestion and context isolation |

## Section 8: Model, Vendor, and Supply Chain

| Question | Response |
|---|---|
| What model or AI provider will be used? |  |
| Is the model local, internally hosted, SaaS-hosted, or cloud-hosted? |  |
| Will prompts or responses be sent to a third-party provider? |  |
| Does the provider retain prompts or responses? |  |
| Does the provider use customer data for model training? |  |
| Has vendor risk review been completed? |  |
| Has legal or privacy review been completed? |  |
| Are open-source packages used? |  |
| Are dependencies scanned for vulnerabilities? |  |
| Are model versions tracked? |  |
| Are embeddings or vector databases used? |  |
| Are plugins, extensions, or external tools used? |  |

## Vendor Risk Checklist

| Control | Required? | Notes |
|---|---|---|
| Vendor risk review |  |  |
| Privacy review |  |  |
| Legal review |  |  |
| Contract review |  |  |
| Data retention review |  |  |
| Model training opt-out confirmed |  |  |
| Dependency scanning |  |  |
| Version pinning |  |  |
| Model provenance review |  |  |
| Exit strategy |  |  |

## Section 9: Logging and Monitoring

| Question | Response |
|---|---|
| What activity will be logged? |  |
| Will prompts be logged in full, partially, or as metadata only? |  |
| Will responses be logged in full, partially, or as metadata only? |  |
| Will retrieved document IDs be logged? |  |
| Will access decisions be logged? |  |
| Will prompt injection attempts be logged? |  |
| Will sensitive data detections be logged? |  |
| Who can access logs? |  |
| How long will logs be retained? |  |
| Will logs be sent to a SIEM? |  |
| What alerts are required? |  |
| How will suspicious behavior be investigated? |  |

## Logging Checklist

| Logging Requirement | Required? | Notes |
|---|---|---|
| User ID |  |  |
| Timestamp |  |  |
| Prompt metadata |  |  |
| Prompt risk score |  |  |
| Retrieval metadata |  |  |
| Retrieved document IDs |  |  |
| Access decision |  |  |
| Response metadata |  |  |
| Response risk score |  |  |
| Human review decision |  |  |
| Admin changes |  |  |
| Cost and usage signals |  |  |
| Correlation ID |  |  |

## Section 10: Human Review Requirements

| Question | Response |
|---|---|
| Does the use case require human review? |  |
| What topics require review? |  |
| Who reviews high-risk AI output? |  |
| Who approves security exceptions? |  |
| Who approves access-related recommendations? |  |
| Who reviews compliance or legal interpretations? |  |
| How will review decisions be logged? |  |
| What is the review SLA? |  |
| Can the AI assistant release responses before review? |  |
| Can users appeal or request clarification? |  |

## Human Review Checklist

| Trigger | Review Required? | Reviewer |
|---|---|---|
| Security exception |  |  |
| IAM access approval |  |  |
| Privileged access guidance |  |  |
| Compliance interpretation |  |  |
| Legal interpretation |  |  |
| Incident response guidance |  |  |
| Production change recommendation |  |  |
| Restricted data request |  |  |
| Regulated data request |  |  |
| Unsupported response |  |  |
| Prompt injection attempt |  |  |
| Secret exposure |  |  |

## Section 11: Operational Requirements

| Question | Response |
|---|---|
| Who operates the AI system? |  |
| Who supports users? |  |
| What happens if the AI system is unavailable? |  |
| Is there a fallback process? |  |
| How are documents updated? |  |
| How are incorrect responses reported? |  |
| How are model or configuration changes approved? |  |
| Is there a rollback or disablement process? |  |
| Are service levels required? |  |
| Are users trained before access? |  |

## Operational Checklist

| Requirement | Required? | Notes |
|---|---|---|
| Operational owner |  |  |
| Support process |  |  |
| Feedback process |  |  |
| Fallback process |  |  |
| Change management |  |  |
| Document review cycle |  |  |
| Model version tracking |  |  |
| Incident response process |  |  |
| Disablement or kill switch |  |  |
| User training |  |  |

## Section 12: Cost and Deployment

| Question | Response |
|---|---|
| Is this a local prototype, cloud deployment, SaaS tool, or hybrid system? |  |
| Are paid AI services involved? |  |
| Are cloud resources required? |  |
| What is the estimated monthly cost? |  |
| Are budget alerts configured? |  |
| Are usage quotas configured? |  |
| Is there a teardown procedure? |  |
| Are always-on resources involved? |  |
| Who owns cost monitoring? |  |
| What is the maximum approved spend? |  |

## Cost Control Checklist

| Control | Required? | Notes |
|---|---|---|
| Local-first prototype |  |  |
| Estimated monthly cost |  |  |
| Budget alert |  |  |
| Billing alarm or cost alert |  |  |
| Usage quotas |  |  |
| Rate limiting |  |  |
| Teardown process |  |  |
| Resource tagging |  |  |
| Maximum spend threshold |  |  |
| Cost owner identified |  |  |

## Section 13: Compliance and Regulatory Impact

| Question | Response |
|---|---|
| Does the use case support compliance work? |  |
| Could AI output influence audit evidence? |  |
| Could AI output influence regulatory interpretation? |  |
| Could AI output affect customer-impacting decisions? |  |
| Does the system process data subject to regulatory requirements? |  |
| What frameworks or standards apply? |  |
| Is compliance review required? |  |
| Is legal review required? |  |
| Is privacy review required? |  |
| What evidence must be retained? |  |

## Compliance Checklist

| Area | Applicable? | Notes |
|---|---|---|
| NIST AI RMF |  |  |
| NIST 800-53 |  |  |
| ISO 27001 |  |  |
| PCI DSS |  |  |
| GLBA |  |  |
| HIPAA |  |  |
| GDPR or privacy law |  |  |
| Internal audit |  |  |
| Vendor risk management |  |  |
| Records retention |  |  |

## Section 14: Risk Scoring

Assign a score from 1 to 4 for each domain.

| Score | Rating | Description |
|---|---|---|
| 1 | Low | Limited risk; standard controls are sufficient |
| 2 | Medium | Moderate risk; documented controls required |
| 3 | High | Significant risk; security and governance review required |
| 4 | Critical | Major risk; executive, legal, privacy, or compliance review may be required |

## Risk Scorecard

| Risk Domain | Score | Rating | Rationale |
|---|---|---|---|
| Data Risk |  |  |  |
| Access Risk |  |  |  |
| Prompt and Model Risk |  |  |  |
| Vendor Risk |  |  |  |
| Operational Risk |  |  |  |
| Compliance Risk |  |  |  |

## Overall Risk Rating

| Total Score | Overall Rating | Required Action |
|---|---|---|
| 6 to 8 | Low | May proceed with standard controls |
| 9 to 13 | Medium | May proceed with documented controls and owner approval |
| 14 to 18 | High | Requires security architecture and governance review |
| 19 to 24 | Critical | Requires escalation to security, privacy, legal, compliance, and executive stakeholders |

## Total Score

| Field | Response |
|---|---|
| Total Score |  |
| Overall Risk Rating |  |
| Recommended Decision |  |
| Required Reviewers |  |
| Required Controls |  |

## Section 15: Required Controls

| Control Area | Required Control | Owner | Status |
|---|---|---|---|
| Data Classification |  |  | Not Started |
| Access Control |  |  | Not Started |
| Prompt Injection Controls |  |  | Not Started |
| Retrieval Authorization |  |  | Not Started |
| Response Validation |  |  | Not Started |
| Logging and Monitoring |  |  | Not Started |
| Human Review |  |  | Not Started |
| Vendor Review |  |  | Not Started |
| Cost Controls |  |  | Not Started |
| Incident Response |  |  | Not Started |
| Compliance Mapping |  |  | Not Started |
| User Training |  |  | Not Started |

## Section 16: Approval Decision

| Field | Response |
|---|---|
| Decision | Approved / Approved with Conditions / Limited Pilot / Escalated / Rejected / Deferred |
| Decision Date |  |
| Approver |  |
| Approver Role |  |
| Conditions Required Before Pilot |  |
| Conditions Required Before Production |  |
| Review Date |  |
| Notes |  |

## Example Intake: Internal AI Policy Assistant

| Field | Example Response |
|---|---|
| Use Case Name | Internal AI Policy Assistant |
| Business Owner | Security Architecture |
| Technical Owner | Platform Engineering |
| Security Owner | Cloud Security Architecture |
| Data Owner | Security Governance |
| Intended Users | Security architects, engineers, compliance analysts, business analysts |
| Business Purpose | Help users find approved security and architecture guidance faster |
| AI Capability | Retrieval-Augmented Generation and summarization |
| Data Used | Mock or approved internal security policy documents |
| Deployment Model | Local-first prototype |
| Access Model | Role-based access with document-level filtering |
| Human Review | Required for security exceptions, IAM decisions, compliance interpretation, and restricted data |
| Logging | Prompt metadata, retrieval decisions, response metadata, and blocked attempts |
| Cost Model | No cloud deployment in initial phase |
| Risk Rating | High for pilot because output may influence security and compliance interpretation |
| Decision | Limited pilot approved with required controls |

## Example Required Controls for Pilot

| Control | Requirement |
|---|---|
| Data | Use mock or approved internal documents only |
| Access | Enforce role-based document access |
| Prompt Security | Implement prompt injection detection |
| Retrieval | Filter documents by classification and role |
| Response | Require source references |
| Logging | Log prompt metadata, retrieval decisions, and blocked attempts |
| Human Review | Require review for security exceptions or compliance decisions |
| Cost | Keep local-only for initial phase |
| Governance | Assign business, data, technical, and security owners |

## Prohibited Use Cases

The following use cases should be rejected or escalated unless formally reviewed and approved:

- Using AI to approve access requests
- Using AI to approve privileged access
- Using AI to approve security exceptions
- Using AI to make final legal decisions
- Using AI to make final regulatory decisions
- Using AI to make final audit conclusions
- Using AI to process real customer data without approval
- Using AI to process payment data without approval
- Using AI to process employee records without approval
- Entering credentials, keys, or secrets into AI prompts
- Allowing AI to modify production systems without human approval
- Connecting AI to unrestricted internal document repositories
- Training a model on restricted enterprise data without approval
- Using unapproved vendor AI tools for confidential data

## Intake Review Participants

| Role | Required When |
|---|---|
| Business Owner | All use cases |
| Technical Owner | All implementation use cases |
| Security Architect | All enterprise AI use cases |
| Data Owner | Any use case involving documents or data |
| IAM Owner | Any use case involving user access or identity controls |
| Compliance | Compliance-impacting or regulated use cases |
| Legal | Legal, contractual, regulatory, or high-risk vendor use cases |
| Privacy | Personal, employee, customer, or regulated data use cases |
| Vendor Risk | Third-party AI provider use cases |
| Security Operations | Monitoring, incident response, or abuse detection use cases |
| Architecture Review Board | Production or enterprise architecture use cases |

## Intake Evidence Package

The final intake package should include:

- Completed intake form
- Business case
- Data classification review
- Access control model
- AI risk assessment
- Prompt injection control strategy
- Logging and monitoring requirements
- Human review requirements
- Vendor review if applicable
- Cost control plan if applicable
- Compliance mapping if applicable
- Approval decision record

## Review Cadence

| Review Type | Frequency |
|---|---|
| Initial Use Case Intake | Before design or pilot |
| Pilot Review | Before and after pilot |
| Production Review | Before production deployment |
| Access Review | Quarterly or semi-annually depending on sensitivity |
| Data Review | At least annually or when documents change |
| Vendor Review | Annually or when provider/model changes |
| Security Review | At least annually or after major changes |
| Compliance Review | Before audit or regulatory use |
| Incident Review | After any AI-related incident |

## Security Architect Notes

The intake process ensures that AI adoption starts with governance, not tooling.

For security architects, the most important questions are:

- What problem is being solved?
- What data is being used?
- Who can access it?
- What can the AI influence?
- What happens if the AI is wrong?
- What controls prevent misuse?
- Who is accountable?
- What evidence proves the controls are working?

A strong intake process helps prevent unmanaged AI adoption, shadow AI usage, unnecessary cloud cost, data leakage, weak auditability, and overreliance on AI-generated output.

## Conclusion

AI use case intake is a foundational governance control.

Before an AI assistant, RAG system, or AI-enabled workflow is implemented, the organization should document the business purpose, data scope, access model, prompt and model risks, vendor exposure, logging requirements, human review process, cost controls, compliance impact, and approval decision.

This process helps ensure that AI adoption is intentional, secure, auditable, and aligned with business risk.
