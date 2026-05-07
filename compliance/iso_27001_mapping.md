# ISO 27001 Control Mapping

## Purpose

This document maps the secure enterprise AI assistant architecture to selected ISO/IEC 27001 control themes.

The purpose is to show how an internal AI assistant using Retrieval-Augmented Generation can be governed through information security management practices, access control, logging, supplier review, incident response, data protection, secure configuration, and operational monitoring.

This mapping is intended as a practical security architecture alignment, not a formal certification assessment.

## Scope

This mapping applies to:

- Internal AI assistant architecture
- Retrieval-Augmented Generation workflows
- AI governance
- Data classification
- Identity and access control
- Prompt injection controls
- Document-level authorization
- Logging and monitoring
- Human review
- Incident response
- Supplier and vendor risk
- Secure development considerations
- Local prototype and future cloud reference designs

## Project Context

The AI assistant is designed for a regulated organization that wants to help employees query approved internal documents while reducing the risk of:

- Unauthorized access
- Sensitive data disclosure
- Prompt injection
- Unsafe AI-generated output
- Overreliance on AI
- Weak auditability
- Unapproved vendor exposure
- Cloud cost overruns
- Uncontrolled document ingestion

The initial phase is documentation-first and local-first. No real customer data, production data, secrets, regulated data, or confidential employer documents should be used.

## ISO 27001 Alignment Summary

| ISO 27001 Theme | Project Alignment |
|---|---|
| Information Security Policies | AI usage, data handling, access control, logging, and review requirements are documented |
| Roles and Responsibilities | Business, data, technical, security, reviewer, and governance owners are defined |
| Asset Management | Documents, prompts, responses, logs, models, and indexes are treated as information assets |
| Access Control | Role-based and document-level authorization restricts access to AI-retrieved content |
| Supplier Relationships | AI providers, SaaS tools, APIs, and model vendors require review before use |
| Incident Management | AI-specific incident scenarios and response steps are documented |
| Secure Development | Prompt filtering, retrieval authorization, logging, and output validation are designed before implementation |
| Operations Security | Monitoring, logging, cost controls, and review workflows support safe operation |
| Communications Security | Future deployments must protect data in transit and review provider boundaries |
| Compliance | AI usage is mapped to governance, control evidence, and audit-readiness requirements |

---

# Organizational Controls

## Information Security Policies

### Relevance

The AI assistant requires documented policies and standards defining acceptable use, prohibited data, approved use cases, access expectations, and governance requirements.

### Project Implementation

- AI use case intake process
- Data classification policy
- Human review requirements
- Prompt injection control expectations
- Logging and monitoring requirements
- Cost-control requirements
- Prohibited use cases

### Supporting Artifacts

- governance/ai_use_case_intake.md
- governance/data_classification.md
- governance/human_review_requirements.md
- security/prompt_injection_controls.md
- cost_controls.md

## Information Security Roles and Responsibilities

### Relevance

AI systems require clearly defined ownership because responsibility cannot be delegated to the model.

### Project Implementation

Defined roles include:

- Business Owner
- Technical Owner
- Security Owner
- Data Owner
- Content Owner
- AI System Administrator
- Security Reviewer
- IAM Owner
- Compliance Owner
- Legal or Privacy Reviewer
- Incident Response Owner

### Supporting Artifacts

- governance/ai_use_case_intake.md
- governance/ai_risk_assessment.md
- governance/human_review_requirements.md
- incident_response/ai_incident_response_playbook.md

## Segregation of Duties

### Relevance

AI system administration, content ownership, access approval, human review, and audit viewing should be separated.

### Project Implementation

- AI administrators do not automatically receive access to all restricted content
- Content owners approve document ingestion
- IAM owners review access-related questions
- Security reviewers evaluate high-risk output
- Compliance or legal reviewers validate regulatory interpretations
- Audit viewers receive evidence access, not unrestricted system control

### Supporting Artifacts

- security/access_control_model.md
- governance/human_review_requirements.md

## Contact with Authorities and Special Interest Groups

### Relevance

For regulated environments, AI-related incidents or compliance concerns may require escalation to legal, privacy, compliance, regulators, or industry groups depending on severity and jurisdiction.

### Project Implementation

- Incident response escalation matrix
- Privacy, legal, compliance, and data owner involvement for regulated data exposure
- Vendor escalation for provider-related incidents
- Internal reporting paths for sensitive data exposure or unauthorized retrieval

### Supporting Artifacts

- incident_response/ai_incident_response_playbook.md
- governance/human_review_requirements.md

## Threat Intelligence

### Relevance

AI systems face evolving threats such as prompt injection, data poisoning, model abuse, excessive agency, and supply chain compromise.

### Project Implementation

- OWASP LLM Top 10 mapping
- STRIDE threat model
- Prompt injection test cases
- Monitoring rules for suspicious prompts
- Incident scenarios for poisoned documents and unauthorized retrieval

### Supporting Artifacts

- security/owasp_llm_top10_mapping.md
- security/threat_model_stride.md
- security/prompt_injection_controls.md
- security/logging_monitoring.md

## Information Security in Project Management

### Relevance

Security requirements should be built into the AI project before implementation.

### Project Implementation

- Architecture-first approach
- Risk assessment before pilot
- Data classification before document ingestion
- Access model before retrieval design
- Logging requirements before deployment
- Cost controls before any cloud use
- Human review workflow before high-risk use

### Supporting Artifacts

- README.md
- business_case.md
- governance/ai_risk_assessment.md
- architecture/deployment_options.md

---

# Asset and Information Management

## Inventory of Information and Other Associated Assets

### Relevance

The AI assistant depends on documents, metadata, prompts, responses, logs, model settings, indexes, and review records.

### Project Implementation

The project identifies key assets:

- Approved internal documents
- Document metadata
- User prompts
- Retrieved context
- AI-generated responses
- System prompts
- Access policies
- Vector indexes or search indexes
- Prompt and response logs
- Human review records
- Model or provider configuration

### Supporting Artifacts

- security/threat_model_stride.md
- governance/data_classification.md
- architecture/reference_architecture.md

## Acceptable Use of Information and Associated Assets

### Relevance

Users need clear rules for what they may and may not submit to the AI assistant.

### Project Implementation

Users should not submit:

- Customer data
- Employee records
- Payment data
- Production secrets
- API keys
- Private keys
- Restricted incident data
- Confidential employer documents unless approved
- Requests to bypass security controls
- Requests to approve access or exceptions

### Supporting Artifacts

- governance/data_classification.md
- governance/ai_use_case_intake.md
- security/prompt_injection_controls.md

## Classification of Information

### Relevance

The AI assistant must classify documents and outputs so retrieval and response handling can be controlled.

### Project Implementation

Classification levels:

- Public
- Internal
- Confidential
- Restricted
- Regulated
- Secrets

Each document requires:

- Owner
- Classification
- Approved roles
- Approved groups
- Status
- Review date
- Source system
- Ingestion approval

### Supporting Artifacts

- governance/data_classification.md
- security/access_control_model.md

## Labelling of Information

### Relevance

Classification labels must be attached to documents and preserved through retrieval and logging.

### Project Implementation

- Document metadata includes classification labels
- Retrieved document IDs and classifications are logged
- Responses inherit the highest classification of source content
- Unknown or unlabeled data is denied by default
- Embeddings inherit the classification of source content

### Supporting Artifacts

- governance/data_classification.md
- security/logging_monitoring.md

## Information Transfer

### Relevance

If prompts, documents, or retrieved context are sent to a cloud model or third-party provider, information transfer risks increase.

### Project Implementation

- Local-first prototype avoids external data transfer
- Cloud reference designs require provider data handling review
- Sensitive data cannot be sent to external providers without approval
- Future deployments require encrypted transmission
- Model/provider boundaries are documented

### Supporting Artifacts

- architecture/deployment_options.md
- architecture/trust_boundaries.md
- cloud_reference_only/aws_bedrock_design_only.md
- cloud_reference_only/azure_openai_design_only.md

---

# Access Control

## Identity Management

### Relevance

The AI assistant must know who the user is before allowing access.

### Project Implementation

- Require enterprise SSO for production deployment
- Use trusted identity provider attributes
- Use user ID, role, group membership, and session context for authorization
- Avoid anonymous access
- Remove access when users change roles or leave

### Supporting Artifacts

- security/access_control_model.md
- architecture/trust_boundaries.md

## Authentication Information

### Relevance

Authentication credentials and secrets must not be exposed to the AI assistant.

### Project Implementation

- Prohibit passwords, API keys, tokens, private keys, and certificates in prompts
- Detect and block secret patterns
- Do not store credentials in documents, code, logs, or system prompts
- Rotate any exposed secret
- Use secrets management tools for future deployments

### Supporting Artifacts

- governance/data_classification.md
- security/prompt_injection_controls.md
- incident_response/ai_incident_response_playbook.md

## Access Rights

### Relevance

Users should only retrieve documents and receive responses appropriate to their role.

### Project Implementation

- Role-based access model
- Document-level authorization
- Metadata-based retrieval filtering
- Deny-by-default for missing metadata
- Separate administrator access from document content access
- Access review requirements for privileged and restricted roles

### Supporting Artifacts

- security/access_control_model.md
- governance/data_classification.md

## Privileged Access Rights

### Relevance

Privileged roles such as AI administrators, reviewers, content owners, IAM owners, and audit viewers require additional oversight.

### Project Implementation

- MFA for privileged access
- Privileged access reviews
- No shared admin accounts
- Privileged actions logged
- Separation between system administration and content access
- Emergency or break-glass access documented if used

### Supporting Artifacts

- security/access_control_model.md
- security/logging_monitoring.md

## Restriction of Access to Information

### Relevance

Confidential, restricted, regulated, and secret data must be protected from unauthorized retrieval or output.

### Project Implementation

- Data classification drives access
- Restricted content requires explicit role approval
- Regulated data is prohibited in local prototype
- Secrets are prohibited
- Response validation blocks unauthorized sensitive output
- Human review required for restricted or regulated content

### Supporting Artifacts

- governance/data_classification.md
- security/access_control_model.md
- governance/human_review_requirements.md

---

# Supplier and Vendor Management

## Information Security in Supplier Relationships

### Relevance

AI services may involve third-party providers, cloud platforms, SaaS tools, APIs, models, vector databases, or open-source components.

### Project Implementation

Supplier review should include:

- Data retention
- Prompt and response handling
- Training on customer data
- Security controls
- Logging and audit support
- Data residency
- Incident notification
- Exit strategy
- Contractual obligations
- Cost model

### Supporting Artifacts

- governance/ai_use_case_intake.md
- architecture/deployment_options.md
- security/owasp_llm_top10_mapping.md

## Addressing Information Security Within Supplier Agreements

### Relevance

If a third-party AI provider is used, agreements must address data handling, security, privacy, and audit needs.

### Project Implementation

Before vendor use, review:

- Whether prompts are retained
- Whether responses are retained
- Whether data is used for training
- Where data is processed
- How incidents are reported
- What logs are available
- Whether data can be deleted
- How access is controlled
- What service levels apply

### Supporting Artifacts

- governance/ai_use_case_intake.md
- architecture/deployment_options.md

## Monitoring, Review, and Change Management of Supplier Services

### Relevance

AI vendors and model providers may change features, terms, models, logging, retention, or pricing.

### Project Implementation

- Periodic vendor review
- Review on provider or model change
- Monitor cost and usage
- Review data handling changes
- Reassess risk if deployment scope changes
- Maintain exit strategy

### Supporting Artifacts

- governance/ai_risk_assessment.md
- architecture/deployment_options.md
- cost_controls.md

## ICT Supply Chain

### Relevance

AI applications may depend on open-source packages, model artifacts, embedding tools, document parsers, containers, and hosted providers.

### Project Implementation

- Dependency scanning for future prototype
- Version pinning
- Approved package sources
- Model provenance review
- Avoid untrusted plugins
- Review document parsing libraries
- Maintain component inventory if implemented

### Supporting Artifacts

- security/owasp_llm_top10_mapping.md
- architecture/deployment_options.md

---

# Incident Management

## Responsibilities and Procedures

### Relevance

AI incidents require defined responsibilities and response procedures.

### Project Implementation

The AI incident response playbook defines:

- Incident categories
- Severity levels
- Triage questions
- Roles and responsibilities
- Escalation matrix
- Containment options
- Investigation evidence
- Recovery and lessons learned

### Supporting Artifacts

- incident_response/ai_incident_response_playbook.md

## Reporting Information Security Events

### Relevance

Users, reviewers, administrators, and monitoring systems should report AI-related security events.

### Project Implementation

Reportable events include:

- Prompt injection attempts
- Sensitive data entered into prompts
- Unauthorized retrieval
- Restricted content exposure
- Secret exposure
- Poisoned documents
- Unsafe recommendations
- Human review bypass
- Logging failure
- Cost spike

### Supporting Artifacts

- security/logging_monitoring.md
- incident_response/ai_incident_response_playbook.md

## Assessment and Decision on Information Security Events

### Relevance

AI events must be assessed to determine whether they are incidents and what severity applies.

### Project Implementation

- Severity model: Low, Medium, High, Critical
- Triage questions
- Data classification review
- User and document impact review
- Vendor involvement review
- Human review bypass assessment

### Supporting Artifacts

- incident_response/ai_incident_response_playbook.md
- governance/data_classification.md

## Response to Information Security Incidents

### Relevance

The organization must respond to AI incidents in a structured way.

### Project Implementation

Response steps include:

- Detection
- Triage
- Containment
- Investigation
- Eradication
- Recovery
- Post-incident review
- Control improvement

### Supporting Artifacts

- incident_response/ai_incident_response_playbook.md

## Learning from Information Security Incidents

### Relevance

AI incidents should improve controls, monitoring, documentation, and training.

### Project Implementation

Post-incident improvements may include:

- Updating prompt filters
- Correcting metadata
- Improving retrieval controls
- Updating human review triggers
- Improving logging
- Updating incident response procedures
- Adding user training
- Revising data classification

### Supporting Artifacts

- incident_response/ai_incident_response_playbook.md
- lessonslearned.md

## Collection of Evidence

### Relevance

AI incidents require evidence that connects user prompt, retrieved documents, model context, response, validation, and review decision.

### Project Implementation

Evidence may include:

- User ID
- Prompt metadata
- Prompt text if retained
- Retrieved document IDs
- Document classification
- Response metadata
- Human review records
- Admin changes
- Model configuration
- Vendor logs
- Correlation ID

### Supporting Artifacts

- security/logging_monitoring.md
- incident_response/ai_incident_response_playbook.md

---

# Operational Controls

## Operating Procedures

### Relevance

The AI assistant requires documented procedures for safe operation.

### Project Implementation

Operational procedures include:

- Document ingestion approval
- Data classification
- Access review
- Prompt injection testing
- Logging review
- Human review
- Incident response
- Cost monitoring
- Cloud deployment decision gates

### Supporting Artifacts

- governance/data_classification.md
- security/logging_monitoring.md
- architecture/deployment_options.md

## Change Management

### Relevance

Changes to AI configuration can affect security and compliance.

### Project Implementation

Changes requiring review include:

- System prompts
- Prompt filters
- Model provider
- Model version
- Retrieval index
- Document ingestion rules
- Access policies
- Logging configuration
- Human review triggers
- Cloud services

### Supporting Artifacts

- architecture/trust_boundaries.md
- security/logging_monitoring.md
- incident_response/ai_incident_response_playbook.md

## Capacity Management

### Relevance

AI systems can create usage spikes, token growth, API usage, logging volume, and cost risk.

### Project Implementation

- Rate limiting
- Usage quotas
- Prompt size limits
- Cost monitoring
- Budget alerts before cloud deployment
- Local-first testing
- Alerting on excessive usage

### Supporting Artifacts

- cost_controls.md
- security/logging_monitoring.md
- architecture/deployment_options.md

## Protection Against Malware

### Relevance

AI projects may use third-party packages, document parsers, plugins, or generated code that could introduce malicious content.

### Project Implementation

For future implementation:

- Scan dependencies
- Avoid untrusted plugins
- Review document processing tools
- Do not execute AI-generated code without review
- Treat uploaded or ingested documents as untrusted until reviewed

### Supporting Artifacts

- security/owasp_llm_top10_mapping.md
- architecture/deployment_options.md

## Logging

### Relevance

Logging supports accountability, monitoring, audit readiness, and incident response.

### Project Implementation

Log categories include:

- Authentication events
- Prompt metadata
- Retrieval events
- Access decisions
- Model interaction metadata
- Response validation events
- Human review decisions
- Administrative changes
- Security alerts
- Usage and cost signals

### Supporting Artifacts

- security/logging_monitoring.md

## Monitoring Activities

### Relevance

The assistant must be monitored for misuse, failures, security events, and operational risk.

### Project Implementation

Monitoring use cases include:

- Prompt injection attempts
- System prompt extraction
- Sensitive data submission
- Unauthorized retrieval
- Excessive usage
- Missing source support
- Human review bypass
- Logging failure
- Cost spike

### Supporting Artifacts

- security/logging_monitoring.md

## Clock Synchronization

### Relevance

Logs must have accurate timestamps for investigation and event correlation.

### Project Implementation

- Include timestamps in logs
- Use correlation IDs
- Preserve event order across prompt, retrieval, response, review, and incident logs
- Use consistent time formats in future implementations

### Supporting Artifacts

- security/logging_monitoring.md
- incident_response/ai_incident_response_playbook.md

## Use of Privileged Utility Programs

### Relevance

AI systems should not be allowed to run privileged commands or administrative tools without strict control.

### Project Implementation

- Initial assistant is read-only
- AI cannot execute production changes
- AI cannot approve access
- AI cannot modify infrastructure
- Any future tool use requires allowlisting, approval, and logging

### Supporting Artifacts

- governance/human_review_requirements.md
- security/access_control_model.md
- architecture/deployment_options.md

---

# Communications Security

## Network Security

### Relevance

If deployed beyond the local prototype, communications between users, application components, identity provider, retrieval layer, model provider, and logging systems must be protected.

### Project Implementation

Future deployment should consider:

- TLS encryption
- Private endpoints where appropriate
- No unrestricted public exposure
- Controlled API access
- Secure provider integration
- Logging of network-relevant events
- Network boundary review

### Supporting Artifacts

- architecture/trust_boundaries.md
- architecture/deployment_options.md

## Security of Information in Transit

### Relevance

Prompts, retrieved context, metadata, and responses may contain sensitive information.

### Project Implementation

- Local-first prototype avoids external transmission
- Future cloud deployment requires encrypted communications
- Provider data handling must be reviewed
- Sensitive data should not be sent to unapproved external models

### Supporting Artifacts

- architecture/deployment_options.md
- governance/data_classification.md

---

# System Acquisition, Development, and Maintenance

## Secure Development Lifecycle

### Relevance

If a local prototype or application is created, security requirements should be built into development from the start.

### Project Implementation

Security requirements include:

- Prompt injection detection
- Role-based retrieval
- Document metadata filtering
- Sensitive data detection
- Local logging
- No hardcoded secrets
- No real sensitive data
- Safe error handling
- Human review simulation
- Cost-safe local design

### Supporting Artifacts

- local_prototype/README.md
- security/prompt_injection_controls.md
- security/access_control_model.md

## Application Security Requirements

### Relevance

The assistant should have application-level security requirements before implementation.

### Project Implementation

Requirements include:

- Authentication
- Authorization
- Input filtering
- Retrieval authorization
- Output validation
- Logging
- Human review
- Admin change logging
- Data classification enforcement

### Supporting Artifacts

- architecture/reference_architecture.md
- architecture/trust_boundaries.md
- security/access_control_model.md

## Secure System Architecture and Engineering Principles

### Relevance

AI security must be designed into the system architecture.

### Project Implementation

Architecture principles include:

- Security by design
- Least privilege
- Deny by default
- Human accountability
- Data minimization
- Source traceability
- Local-first experimentation
- Defense in depth
- Model is not the control authority

### Supporting Artifacts

- architecture/reference_architecture.md
- architecture/trust_boundaries.md

## Secure Coding

### Relevance

If code is added later, the prototype should avoid common security weaknesses.

### Project Implementation

Future prototype should:

- Avoid hardcoded credentials
- Use environment variables for configuration if needed
- Validate inputs
- Avoid unsafe command execution
- Sanitize logs
- Restrict file access
- Use safe dependency management
- Avoid real sensitive data

### Supporting Artifacts

- local_prototype/README.md
- architecture/deployment_options.md

## Security Testing in Development and Acceptance

### Relevance

Prompt injection, retrieval authorization, and sensitive data blocking should be tested before use.

### Project Implementation

Test cases should include:

- Instruction override
- System prompt extraction
- Role impersonation
- Unauthorized document retrieval
- Sensitive data prompt
- Secret pattern detection
- Restricted content request
- Missing source support
- Human review trigger
- Logging output

### Supporting Artifacts

- security/prompt_injection_controls.md
- security/logging_monitoring.md
- governance/human_review_requirements.md

## Outsourced Development

### Relevance

If third parties assist with AI development, they may gain access to code, documents, prompts, logs, or architecture details.

### Project Implementation

- Limit third-party access
- Use mock data for development
- Prohibit real credentials
- Review contracts and access rights
- Require secure coding and data handling expectations
- Review outputs before adoption

### Supporting Artifacts

- governance/ai_use_case_intake.md
- governance/data_classification.md

---

# Data Protection and Privacy

## Data Masking

### Relevance

Sensitive data in prompts, responses, documents, or logs should be masked or redacted where appropriate.

### Project Implementation

- Detect sensitive values in prompts
- Redact sensitive values in logs
- Block secrets and regulated data
- Avoid full prompt/response logging by default
- Use mock data in prototype

### Supporting Artifacts

- governance/data_classification.md
- security/logging_monitoring.md

## Data Leakage Prevention

### Relevance

AI assistants can leak data through retrieval, model context, generated responses, logs, or provider transfer.

### Project Implementation

- Data classification
- Prompt filtering
- Retrieval authorization
- Output validation
- Log minimization
- Vendor data handling review
- Human review for restricted or regulated content

### Supporting Artifacts

- governance/data_classification.md
- security/prompt_injection_controls.md
- security/access_control_model.md

## Monitoring Activities for Data Leakage

### Relevance

The system should detect attempts to expose sensitive data.

### Project Implementation

Monitor:

- Secrets in prompts
- Customer or regulated data in prompts
- Restricted document requests
- Sensitive response output
- Unauthorized retrieval attempts
- Prompt injection attempts
- Repeated suspicious activity

### Supporting Artifacts

- security/logging_monitoring.md
- incident_response/ai_incident_response_playbook.md

---

# AI-Specific Risk to ISO 27001 Mapping

| AI Risk | ISO 27001 Control Theme | Project Control |
|---|---|---|
| Prompt Injection | Threat intelligence, input validation, monitoring, secure development | Prompt injection controls and testing |
| Sensitive Data Disclosure | Classification, access control, data leakage prevention, logging | Data classification, retrieval filtering, output validation |
| Unauthorized Retrieval | Access control, restriction of access, asset management | Document-level authorization |
| System Prompt Leakage | Secure development, monitoring, information transfer | Prompt hardening and output validation |
| Poisoned Documents | Asset management, change management, secure development | Ingestion approval and content review |
| Misinformation | Human review, governance, monitoring | Source citation and review workflow |
| Excessive Agency | Access control, segregation of duties, secure architecture | Read-only design and human approval |
| Weak Auditability | Logging, monitoring, collection of evidence | Structured logging and correlation IDs |
| Vendor Data Exposure | Supplier relationships, supplier agreements, ICT supply chain | Vendor review and deployment decision gates |
| Cost Spike | Capacity management, operational monitoring | Usage monitoring, quotas, and cost controls |
| Human Review Bypass | Roles and responsibilities, incident management, monitoring | Human review requirements and logs |
| Secrets Exposure | Authentication information, data leakage prevention, incident response | Secret detection, blocking, and rotation process |

---

# Minimum ISO-Aligned Baseline for Local Prototype

| Control Area | Requirement |
|---|---|
| Data Handling | Use mock data only |
| Classification | Label sample documents |
| Access Control | Simulate role-based document access |
| Prompt Security | Detect and block prompt injection patterns |
| Secrets Protection | Block obvious secret patterns |
| Logging | Create local structured logs |
| Monitoring | Create mock alerts for high-risk events |
| Human Review | Simulate review triggers |
| Incident Response | Document sample incident scenarios |
| Supplier Risk | Avoid third-party AI providers in initial phase |
| Cost Control | No cloud services used |

## Minimum ISO-Aligned Baseline Before Cloud Deployment

| Control Area | Requirement |
|---|---|
| Identity | Enterprise SSO and MFA |
| Access Control | Role and document-level access enforcement |
| Data Protection | Classification and owner approval |
| Supplier Review | Provider data handling and contract review |
| Logging | Centralized logs and alerting |
| Monitoring | Detection rules for AI misuse |
| Incident Response | AI incident response playbook |
| Human Review | Defined reviewer roles and escalation paths |
| Change Management | Controlled changes to prompts, models, indexes, and policies |
| Encryption | Protection of data in transit and at rest |
| Cost Control | Budgets, alerts, quotas, and teardown plan |
| Evidence | Retention of audit and review records |

## Control Ownership

| Control Area | Primary Owner |
|---|---|
| AI Governance | Security Governance |
| Business Use Case | Business Owner |
| Data Classification | Data Owner |
| Access Control | IAM Team |
| Prompt Injection Controls | Security Architecture |
| Logging and Monitoring | Security Operations |
| Incident Response | Security Operations |
| Human Review | Security Governance and Control Owners |
| Supplier Review | Vendor Risk Management |
| Compliance Mapping | Compliance and Security Architecture |
| Cloud Cost Controls | Platform Owner or FinOps |
| Secure Development | Technical Owner or Application Team |

## Security Architect Notes

ISO 27001 alignment reinforces that AI security is part of the broader information security management system.

The AI assistant should not be treated as an isolated chatbot. It should be governed like an enterprise information system, with defined ownership, access control, data classification, supplier review, incident response, monitoring, secure development, and continuous improvement.

The most important design principle is that the AI model is not the security authority. Security must be enforced by policy, process, application logic, identity systems, data classification, logging, monitoring, and accountable human review.

## Conclusion

The secure AI assistant architecture aligns with ISO 27001 control themes by documenting governance, roles, asset handling, classification, access control, supplier review, logging, monitoring, incident response, secure development, and data protection requirements.

This mapping supports responsible AI adoption in regulated environments by showing how AI systems can be integrated into an enterprise security management approach.

The recommended implementation remains documentation-first and local-first until access control, data handling, logging, vendor review, human review, incident response, and cost controls are ready for any future deployment.
