# AI Use Case Intake

## Purpose

This document provides a governance intake framework for evaluating proposed AI use cases before pilot or production implementation.

The purpose is to make sure AI adoption begins with a defined business problem rather than a technology choice.

Before approving an AI initiative, the organization should understand the business value, data involved, intended users, decisions the system may influence, security and privacy risks, human accountability, operational dependencies, provider exposure, and expected cost.

## Intake Principle

> The first question should not be, “Which AI platform should we use?”

The first questions should be:

- What problem are we trying to solve?
- Why is AI appropriate for that problem?
- What information will the system access?
- Who is authorized to access that information?
- What decisions or actions could AI output influence?
- What happens when the AI is wrong?
- Who remains accountable?
- What evidence will show that the controls are working?

The deployment model should be evaluated after those questions are understood.

## Applicability

This intake can be used for AI use cases such as:

- Internal AI assistants
- Retrieval-Augmented Generation
- AI-enabled enterprise search
- Document summarization
- Compliance or security research
- Decision-support systems
- AI-enabled workflow automation
- Agentic or tool-enabled systems
- Customer-facing AI
- AI systems processing internal or regulated information
- SaaS AI products
- Cloud-managed AI services
- Internally hosted AI systems

The depth of review should reflect the risk and consequence of the proposed use case.

# 1. Business Problem

| Question | Response |
| --- | --- |
| What business problem is being solved? | |
| Who experiences the problem today? | |
| How is the problem handled today? | |
| Why is AI being considered? | |
| Could conventional search, rules, automation, or workflow changes solve it? | |
| What business outcome is expected? | |
| How would success be measured? | |
| What happens if the initiative is not implemented? | |

## Architecture Question

AI should provide enough additional value to justify the uncertainty, governance requirements, security controls, operational dependencies, and cost that it introduces.

# 2. Ownership and Accountability

| Role | Owner |
| --- | --- |
| Business Owner | |
| Technical Owner | |
| Security Owner | |
| Data Owner | |
| Operational Owner | |
| Compliance / Risk Owner if applicable | |
| Vendor Owner if applicable | |

Questions to resolve include:

- Who accepts the business risk?
- Who owns the data?
- Who approves access?
- Who operates the service?
- Who investigates security events?
- Who can disable the system?
- Who is accountable when AI output influences a consequential decision?

AI should not create an accountability gap.

# 3. Intended AI Capability

Identify what the proposed system will actually do.

| Capability | Applicable? | Notes |
| --- | --- | --- |
| Search / Retrieval | | |
| Question Answering | | |
| Summarization | | |
| Classification | | |
| Content Generation | | |
| Risk Scoring | | |
| Recommendation | | |
| Decision Support | | |
| Workflow Automation | | |
| Tool / API Use | | |
| Autonomous Action | | |

Additional questions:

- Will the system use RAG?
- Will it generate new content?
- Will it retrieve enterprise documents?
- Will it interact with external systems?
- Can it change data?
- Can it trigger business processes?
- Can it initiate production actions?
- Can it make decisions without human approval?

Increasing system agency generally increases the importance of authorization, monitoring, failure containment, and human accountability.

# 4. Users and Identity

| Question | Response |
| --- | --- |
| Who will use the system? | |
| Internal or external users? | |
| What roles or groups require access? | |
| Will access differ between users? | |
| Are privileged users involved? | |
| How will users authenticate? | |
| Is MFA required? | |
| How is access approved? | |
| How is access removed? | |
| Are periodic access reviews required? | |

## Identity Principle

The AI application should not determine identity or privilege from claims made inside a prompt.

Production identity and authorization context should come from approved enterprise systems.

# 5. Data Scope

Identify the information the AI system may process.

| Data Category | Included? | Owner / Classification | Notes |
| --- | --- | --- | --- |
| Public | | | |
| Internal | | | |
| Confidential | | | |
| Restricted | | | |
| Customer Data | | | |
| Employee Data | | | |
| Payment Data | | | |
| Health Data | | | |
| Authentication Data | | | |
| Production Logs | | | |
| Source Code | | | |
| Secrets / Credentials | | | |
| Legal Information | | | |
| Audit Findings | | | |
| Incident Records | | | |

Questions to resolve include:

- Where does the information reside today?
- Who owns it?
- Has it been classified?
- Is it approved for AI use?
- Will the information leave the organization?
- Will prompts or responses be retained?
- Will data be used for training or model improvement?
- Will embeddings or indexes contain sensitive information?
- How will stale or revoked documents be removed?

# 6. Authorization and Retrieval

Authentication to the AI system does not automatically authorize access to every connected information source.

Evaluate:

- Role-based access
- Group-based access
- Attribute-based access where appropriate
- Document-level authorization
- Data-classification enforcement
- Least privilege
- Deny-by-default behavior
- Separation of administrative and content privileges
- Access lifecycle
- Access-decision logging

For RAG or enterprise-search use cases, answer:

> Where is authorization enforced before protected information enters model context?

The model itself should not be the authorization control.

# 7. Prompt and Input Risk

Evaluate whether users or retrieved content could manipulate system behavior.

Questions include:

- Can users submit unrestricted prompts?
- Could prompts contain secrets or regulated information?
- Could users attempt prompt injection?
- Could retrieved documents contain malicious instructions?
- Could a user attempt to broaden retrieval scope?
- Could a prompt falsely claim privileged identity?
- Could users attempt to suppress logging or security controls?

Possible controls include:

- Prompt-risk evaluation
- Sensitive-data detection
- Retrieval-scope enforcement
- Rate limiting
- Abuse detection
- Context isolation
- Blocking or escalation
- Security-event logging

Prompt filtering should be treated as one layer of defense rather than the primary authorization mechanism.

# 8. Model and Provider Risk

If a model or external AI provider is involved, document:

| Question | Response |
| --- | --- |
| Model / Provider | |
| Deployment Model | Local / Internal / Cloud / SaaS / External API |
| Are prompts sent externally? | |
| Is retrieved context sent externally? | |
| Are prompts or responses retained? | |
| Is enterprise data used for training? | |
| What region processes the data? | |
| Has vendor risk review occurred? | |
| Has privacy review occurred? | |
| Has legal / contract review occurred? | |
| Are model versions tracked? | |
| Is an exit strategy defined? | |

Open-source models and dependencies also require provenance, vulnerability, licensing, and lifecycle consideration.

# 9. Output and Decision Risk

Determine what the AI output can influence.

Questions include:

- Is the output informational or advisory?
- Could it influence access decisions?
- Could it influence security exceptions?
- Could it influence compliance or legal interpretation?
- Could it influence production changes?
- Could it affect customers?
- Could an incorrect response create financial, operational, safety, legal, or regulatory impact?
- Could users mistake the output for formal approval?

Potential controls include:

- Source traceability
- Response validation
- Sensitive-data detection
- Advisory language
- Restricted-action rules
- Human review
- Escalation

# 10. Human Accountability

Human review should be based on consequence rather than applied indiscriminately to every AI interaction.

Determine whether human review is required for:

| Decision / Activity | Review Required? | Reviewer |
| --- | --- | --- |
| Security Exception | | |
| Privileged Access | | |
| Compliance Interpretation | | |
| Legal Interpretation | | |
| Production Change | | |
| Incident Response Decision | | |
| Restricted Data Disclosure | | |
| Customer-Impacting Decision | | |
| High-Risk Automated Action | | |

Also define:

- When review occurs
- Whether output is held pending review
- Who may approve or reject
- What evidence the reviewer receives
- How the decision is recorded
- What escalation path exists

# 11. Logging and Monitoring

Determine what evidence is required to operate, investigate, and govern the system.

Potential events include:

- User identity
- Timestamp
- Correlation ID
- Prompt-risk result
- Retrieval activity
- Retrieved document IDs
- Denied document IDs
- Authorization decisions
- Security alerts
- Response metadata
- Human-review events
- Administrative changes
- Model or configuration changes

Also determine:

- Whether prompt content should be logged
- Whether response content should be logged
- How sensitive information is minimized
- Who can access logs
- Retention requirements
- SIEM integration
- Alert thresholds
- Incident-investigation procedures

Logs should provide evidence without becoming another repository of sensitive information.

# 12. Operational and Resilience Requirements

Questions include:

- Who operates the service?
- Who supports users?
- What happens when the AI model is unavailable?
- What happens when retrieval fails?
- What happens when the identity provider is unavailable?
- Is there a manual fallback process?
- How are documents updated or removed?
- How are incorrect responses reported?
- How are model and configuration changes controlled?
- Is rollback available?
- Can the system be disabled quickly?
- Are service-level objectives required?

The architecture should consider degraded operation and failure behavior, not only the successful request path.

# 13. Security and Incident Response

Determine how AI-specific security events will be identified and handled.

Potential events include:

- Prompt injection attempts
- Sensitive-data exposure
- Unauthorized retrieval
- Excessive denied access
- Malicious source documents
- Model or provider compromise
- Credential exposure
- Unapproved configuration changes
- Unexpected automated actions

Questions include:

- What creates an alert?
- Who investigates?
- What evidence is available?
- Can affected users or documents be identified?
- Can retrieval or model access be disabled?
- Can a compromised source be removed quickly?
- Is the event covered by the organization's existing incident-response process?

# 14. Compliance, Privacy, and Legal Impact

Determine which obligations apply based on the actual use case and data.

Possible considerations include:

- NIST AI RMF
- NIST SP 800-53
- ISO/IEC 27001
- ISO/IEC 42001
- PCI DSS
- GLBA
- HIPAA
- Privacy requirements
- Records retention
- Internal audit requirements
- Vendor risk requirements
- Contractual obligations

Framework mapping should support the risk analysis rather than substitute for it.

# 15. Cost and Deployment

Questions include:

- Is the implementation local, internal, cloud, SaaS, or hybrid?
- What paid services are involved?
- What resources create recurring charges?
- What is the estimated cost?
- What happens at higher usage?
- Are quotas available?
- Are budget alerts configured?
- Who owns cost monitoring?
- What is the maximum acceptable spend?
- What resources continue billing when idle?
- Is a teardown process documented?

Cloud deployment should be justified by a requirement rather than treated as a prerequisite for AI experimentation.

# 16. Risk Assessment

Assess risk across the major domains.

| Risk Domain | Rating | Rationale |
| --- | --- | --- |
| Business / Decision Risk | | |
| Data Risk | | |
| Identity / Access Risk | | |
| Prompt / Retrieval Risk | | |
| Model / Provider Risk | | |
| Operational Risk | | |
| Compliance / Privacy Risk | | |
| Financial / Cost Risk | | |

Suggested qualitative ratings:

- Low
- Medium
- High
- Critical

The rating should reflect both likelihood and consequence in the organization's context.

A simple numeric score may be used if the organization has an approved methodology, but a calculated number should not replace architectural judgment.

# 17. Required Controls

Document the controls required before the proposed use case moves forward.

| Control Area | Requirement | Owner | Status |
| --- | --- | --- | --- |
| Data Governance | | | |
| Identity | | | |
| Authorization | | | |
| Retrieval Security | | | |
| Prompt Security | | | |
| Response Controls | | | |
| Logging / Monitoring | | | |
| Human Review | | | |
| Incident Response | | | |
| Vendor Risk | | | |
| Compliance / Privacy | | | |
| Cost Controls | | | |
| Operational Readiness | | | |

The status column is intentionally left blank because this document is an intake template, not a project-status tracker.

# 18. Intake Decision

Possible outcomes include:

| Decision | Meaning |
| --- | --- |
| Approved | Use case may proceed with documented controls |
| Approved with Conditions | Required controls must be satisfied before proceeding |
| Limited Pilot | Use case may proceed within explicitly restricted scope |
| Escalated | Additional security, privacy, legal, compliance, risk, or architecture review is required |
| Deferred | More information is required |
| Rejected | Risk or business justification does not support proceeding |

## Decision Record

| Field | Response |
| --- | --- |
| Decision | |
| Decision Date | |
| Approver | |
| Conditions | |
| Required Controls | |
| Required Reviewers | |
| Pilot Restrictions | |
| Production Requirements | |
| Reassessment Date | |

# Example: Internal AI Policy Assistant

This project can be used as an example of how the intake questions influence architecture decisions.

## Business Problem

Employees may need to locate approved security, architecture, IAM, and governance guidance spread across multiple internal sources.

The proposed value is faster access to approved information without creating a new path around existing enterprise authorization.

## Architecture Direction

A production system could eventually use RAG or another enterprise-search pattern.

For this project, however, the first implementation step was deliberately smaller:

**Architecture and Governance → Local Security-Control Prototype → Selected Control Validation**

The local prototype uses synthetic documents and mock identities and does not invoke an LLM.

## Data Decision

Only synthetic data is used in the implemented prototype.

No employer documents, customer information, production data, credentials, or regulated personal information are required.

## Access Decision

The prototype uses mock roles and groups plus document metadata to exercise authorization logic.

A production implementation would require integration with trusted enterprise identity and authorization systems.

## Prompt Security Decision

The prototype includes basic pattern-based prompt-risk evaluation.

One documented prompt injection test successfully demonstrated that a high-risk request could be blocked before retrieval.

This does not demonstrate comprehensive prompt-injection protection.

## Retrieval Decision

The prototype uses simplified keyword retrieval.

Candidate documents are evaluated against metadata and mock user authorization before content is used in the advisory response.

This validates selected authorization concepts without claiming production RAG or semantic retrieval.

## Logging Decision

The prototype writes local JSONL events for prompt activity, retrieval, access decisions, and security alerts.

A production implementation would require enterprise decisions around SIEM integration, retention, privacy, access, and monitoring.

## Human Review Decision

The architecture defines consequence-based human review.

The local prototype can generate simulated review events for documents marked as requiring review, but the mechanism is not a production approval gate and does not currently prevent response generation.

## Deployment Decision

No cloud or external AI service was required to validate the selected controls.

AWS and Azure designs remain reference architecture options rather than deployed environments.

## Current Result

The project demonstrates how an AI use case can progress from:

**Business Problem → Governance → Architecture → Threat Analysis → Control Design → Local Validation**

without beginning with a model or cloud service.

# Governance Decision Principle

The purpose of AI governance is not simply to approve or reject AI.

It is to make the conditions for responsible use explicit.

For each use case, the organization should be able to answer:

**Why are we using AI? What information can it access? Who is authorized to access that information? What decisions can it influence? What happens when it fails? Who is accountable? What evidence proves the controls worked?**

If those questions cannot be answered, the use case is not ready for implementation.
