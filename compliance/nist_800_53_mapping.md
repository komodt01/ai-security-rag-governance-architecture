# NIST 800-53 Control Mapping

## Purpose

This document maps the secure enterprise AI assistant architecture to selected NIST SP 800-53 security and privacy controls.

The purpose is to show how traditional security controls apply to an internal AI assistant that uses Retrieval-Augmented Generation to answer employee questions from approved internal documents.

This mapping focuses on security architect-level control alignment, not formal certification or authorization.

## Scope

This mapping applies to:

- Internal AI assistant architecture
- Retrieval-Augmented Generation workflows
- Identity and access control
- Data classification
- Prompt injection controls
- Document-level authorization
- Logging and monitoring
- Human review
- Incident response
- Vendor and supply chain risk
- Cost and operational governance
- Local prototype and future cloud reference designs

## Project Context

The AI assistant is designed for a regulated organization that wants to let employees ask questions against approved internal documents while preventing unauthorized access, sensitive data exposure, prompt injection, unsafe output, and weak auditability.

The initial implementation is documentation-first and local-first.

The system should not process real customer data, regulated data, production secrets, or confidential employer documents during the initial phase.

## Mapping Summary

| NIST 800-53 Family | Relevance to AI Assistant |
|---|---|
| AC - Access Control | Controls user access, role enforcement, document-level authorization, least privilege |
| AU - Audit and Accountability | Supports logging, monitoring, traceability, and investigation |
| AT - Awareness and Training | Supports user education for approved and prohibited AI use |
| CA - Assessment, Authorization, and Monitoring | Supports ongoing risk assessment and control validation |
| CM - Configuration Management | Controls changes to prompts, models, indexes, guardrails, and access rules |
| CP - Contingency Planning | Supports fallback procedures when AI service is unavailable |
| IA - Identification and Authentication | Supports SSO, MFA, and verified user identity |
| IR - Incident Response | Supports AI misuse, data exposure, and prompt injection incident handling |
| PL - Planning | Supports documented security architecture and governance planning |
| RA - Risk Assessment | Supports AI risk assessment, threat modeling, and vendor review |
| SA - System and Services Acquisition | Supports vendor, model, and supply chain review |
| SC - System and Communications Protection | Supports data protection, isolation, encryption, and boundary controls |
| SI - System and Information Integrity | Supports prompt filtering, output validation, monitoring, and flaw remediation |
| SR - Supply Chain Risk Management | Supports model, provider, dependency, and vendor risk review |

---

# Access Control Family

## AC-2: Account Management

### Control Relevance

The AI assistant must manage which users are allowed to access the system and what role or group-based permissions apply.

### Project Implementation

- Require enterprise identity integration for production use
- Define user roles such as General Employee, Engineer, Security Architect, IAM Analyst, Compliance Analyst, Reviewer, and Administrator
- Remove access when users change roles or leave the organization
- Review access periodically
- Separate administrator access from document content access

### Supporting Artifacts

- security/access_control_model.md
- governance/ai_use_case_intake.md
- governance/human_review_requirements.md

## AC-3: Access Enforcement

### Control Relevance

The system must enforce approved access authorizations before users retrieve documents or receive AI-generated responses.

### Project Implementation

- Enforce role-based access control
- Enforce document-level authorization
- Apply metadata filtering before retrieval
- Re-check authorization before context is sent to the model
- Deny retrieval when classification or ownership metadata is missing

### Supporting Artifacts

- security/access_control_model.md
- governance/data_classification.md
- architecture/trust_boundaries.md

## AC-5: Separation of Duties

### Control Relevance

Administrative access, document ownership, human review, and ordinary user access should be separated.

### Project Implementation

- AI system administrators do not automatically receive access to all document content
- Content owners approve document ingestion
- Security reviewers review high-risk AI output
- IAM owners review access-related decisions
- Compliance or legal teams review regulatory interpretations

### Supporting Artifacts

- security/access_control_model.md
- governance/human_review_requirements.md

## AC-6: Least Privilege

### Control Relevance

Users and administrators should receive only the access necessary for their role.

### Project Implementation

- Apply least privilege to user roles
- Limit access to confidential and restricted documents
- Restrict administrative functions
- Restrict retrieval scope by classification and user role
- Keep the initial AI assistant read-only

### Supporting Artifacts

- security/access_control_model.md
- architecture/deployment_options.md
- governance/data_classification.md

## AC-16: Security and Privacy Attributes

### Control Relevance

The AI assistant depends on metadata attributes to enforce document-level authorization.

### Project Implementation

- Require document metadata such as classification, owner, source system, approved roles, approved groups, status, review date, and expiration date
- Use metadata filters during retrieval
- Deny ingestion or retrieval when metadata is missing
- Preserve source document IDs and classifications in logs

### Supporting Artifacts

- governance/data_classification.md
- security/access_control_model.md
- security/logging_monitoring.md

## AC-17: Remote Access

### Control Relevance

If the assistant is accessed remotely, remote access must be authenticated and controlled.

### Project Implementation

- Require SSO and MFA
- Apply conditional access where appropriate
- Avoid anonymous access
- Log remote access and session metadata where appropriate
- Use secure enterprise access patterns in any future deployment

### Supporting Artifacts

- security/access_control_model.md
- architecture/deployment_options.md

---

# Audit and Accountability Family

## AU-2: Event Logging

### Control Relevance

The system must define which AI-related security and operational events are logged.

### Project Implementation

- Log prompt metadata
- Log retrieval decisions
- Log access decisions
- Log blocked prompt injection attempts
- Log sensitive data detections
- Log human review events
- Log administrative changes
- Log model interaction metadata where appropriate

### Supporting Artifacts

- security/logging_monitoring.md
- incident_response/ai_incident_response_playbook.md

## AU-3: Content of Audit Records

### Control Relevance

Audit records must contain enough information to support investigation and accountability.

### Project Implementation

Recommended log fields include:

- Event ID
- Timestamp
- User ID
- User role
- Session ID
- Prompt risk score
- Policy decision
- Retrieved document IDs
- Document classification
- Response status
- Reviewer ID
- Correlation ID

### Supporting Artifacts

- security/logging_monitoring.md

## AU-6: Audit Record Review, Analysis, and Reporting

### Control Relevance

AI assistant logs should be reviewed to detect misuse, data exposure, prompt injection attempts, and unauthorized retrieval.

### Project Implementation

- Define security monitoring use cases
- Create alert categories for prompt injection, system prompt extraction, sensitive data submission, unauthorized retrieval, and excessive usage
- Review alerts through security operations or governance workflows
- Track high-risk events and remediation

### Supporting Artifacts

- security/logging_monitoring.md
- incident_response/ai_incident_response_playbook.md

## AU-8: Time Stamps

### Control Relevance

AI activity logs must include timestamps for investigation and event correlation.

### Project Implementation

- Include timestamps in prompt logs, retrieval logs, response logs, review logs, and administrative logs
- Use correlation IDs to connect related workflow events
- Preserve time sequencing for incident response

### Supporting Artifacts

- security/logging_monitoring.md
- incident_response/ai_incident_response_playbook.md

## AU-9: Protection of Audit Information

### Control Relevance

Logs may contain sensitive metadata, user activity, retrieved document IDs, or security events and must be protected.

### Project Implementation

- Restrict access to logs by role
- Avoid full prompt and response logging by default
- Redact sensitive values
- Protect logs from unauthorized modification
- Define retention and disposal rules
- Separate operational logs from sensitive security investigation logs

### Supporting Artifacts

- security/logging_monitoring.md
- governance/data_classification.md

## AU-12: Audit Record Generation

### Control Relevance

The AI assistant should generate audit records for security-relevant activity.

### Project Implementation

- Generate logs for prompt submission, retrieval, response validation, access decisions, human review, and admin changes
- Ensure logs support incident reconstruction
- Include correlation IDs across workflow stages

### Supporting Artifacts

- security/logging_monitoring.md

---

# Awareness and Training Family

## AT-2: Literacy Training and Awareness

### Control Relevance

Users need training on approved AI usage, prohibited data entry, limitations of AI responses, and escalation expectations.

### Project Implementation

Users should be trained not to:

- Enter customer data
- Enter secrets or credentials
- Treat AI output as final approval
- Use AI to bypass policy
- Submit restricted data without approval
- Rely on unsupported answers for audit or compliance decisions

### Supporting Artifacts

- governance/ai_use_case_intake.md
- governance/human_review_requirements.md
- governance/data_classification.md

## AT-3: Role-Based Training

### Control Relevance

Privileged users, reviewers, administrators, and content owners need role-specific training.

### Project Implementation

- Security reviewers understand review triggers and decision criteria
- Content owners understand classification and ingestion approval
- Administrators understand configuration, logging, and guardrail change management
- IAM teams understand role and access review responsibilities
- Compliance teams understand AI-generated evidence limitations

### Supporting Artifacts

- governance/human_review_requirements.md
- governance/data_classification.md
- security/access_control_model.md

---

# Assessment, Authorization, and Monitoring Family

## CA-2: Control Assessments

### Control Relevance

AI assistant controls should be assessed before pilot, before production, and after major changes.

### Project Implementation

Assess:

- Access control
- Prompt injection controls
- Retrieval authorization
- Logging
- Human review workflow
- Data classification
- Incident response
- Cost controls
- Vendor and model risk

### Supporting Artifacts

- governance/ai_risk_assessment.md
- security/threat_model_stride.md
- security/owasp_llm_top10_mapping.md

## CA-7: Continuous Monitoring

### Control Relevance

AI assistant risk must be monitored continuously after deployment.

### Project Implementation

- Monitor prompt injection attempts
- Monitor unauthorized retrieval attempts
- Monitor sensitive data detections
- Monitor usage and cost spikes
- Monitor review queue status
- Monitor logging failures
- Monitor administrative changes

### Supporting Artifacts

- security/logging_monitoring.md
- incident_response/ai_incident_response_playbook.md

---

# Configuration Management Family

## CM-2: Baseline Configuration

### Control Relevance

The AI assistant should have a documented baseline configuration.

### Project Implementation

Document:

- Approved model or local simulation approach
- Approved document sources
- User roles
- Retrieval configuration
- Prompt filtering rules
- Response validation rules
- Logging requirements
- Human review rules
- Cost controls

### Supporting Artifacts

- architecture/reference_architecture.md
- architecture/deployment_options.md
- security/prompt_injection_controls.md

## CM-3: Configuration Change Control

### Control Relevance

Changes to AI configuration can introduce security risk.

### Project Implementation

Require review for changes to:

- System prompts
- Model provider or version
- Retrieval indexes
- Document ingestion rules
- Access policies
- Logging settings
- Human review triggers
- Guardrail rules
- Cloud services

### Supporting Artifacts

- architecture/trust_boundaries.md
- security/logging_monitoring.md
- incident_response/ai_incident_response_playbook.md

## CM-6: Configuration Settings

### Control Relevance

Security-relevant configuration settings must be defined and controlled.

### Project Implementation

- Define deny-by-default retrieval behavior
- Require metadata-based document filtering
- Require source citation for supported responses
- Define blocked prompt categories
- Define restricted data handling
- Define log retention and access rules
- Define budget and cost thresholds before cloud deployment

### Supporting Artifacts

- security/access_control_model.md
- security/prompt_injection_controls.md
- cost_controls.md

## CM-8: System Component Inventory

### Control Relevance

The organization should understand the components that make up the AI assistant.

### Project Implementation

Track:

- Application components
- Identity provider
- Document repositories
- Retrieval layer
- Vector store or search index
- Model provider or local model
- Logging platform
- Human review system
- Dependencies and libraries
- Cloud services if deployed

### Supporting Artifacts

- architecture/reference_architecture.md
- architecture/deployment_options.md

---

# Contingency Planning Family

## CP-2: Contingency Plan

### Control Relevance

The organization should define what happens if the AI assistant is unavailable or unsafe to use.

### Project Implementation

- Provide fallback to source documents
- Disable AI functionality if controls fail
- Define manual review paths
- Define response if logging fails
- Define response if model provider is unavailable
- Define cost or usage shutdown triggers

### Supporting Artifacts

- architecture/deployment_options.md
- incident_response/ai_incident_response_playbook.md

## CP-10: System Recovery and Reconstitution

### Control Relevance

If the assistant is disabled due to incident or misconfiguration, safe recovery steps are required.

### Project Implementation

- Validate access controls before re-enabling
- Validate prompt injection controls
- Validate retrieval filtering
- Validate response validation
- Validate logging
- Reindex approved documents if needed
- Document recovery decision

### Supporting Artifacts

- incident_response/ai_incident_response_playbook.md

---

# Identification and Authentication Family

## IA-2: Identification and Authentication

### Control Relevance

The AI assistant should identify and authenticate all users.

### Project Implementation

- Require enterprise SSO for production deployment
- Require MFA
- Avoid anonymous access
- Use trusted identity attributes
- Log authenticated user ID for activity tracking

### Supporting Artifacts

- security/access_control_model.md
- architecture/trust_boundaries.md

## IA-4: Identifier Management

### Control Relevance

User and service identifiers must be managed consistently.

### Project Implementation

- Use unique user IDs
- Use service identities for application components
- Avoid shared accounts
- Associate logs with verified identities
- Remove or disable accounts when no longer needed

### Supporting Artifacts

- security/access_control_model.md
- security/logging_monitoring.md

## IA-5: Authenticator Management

### Control Relevance

Credentials and secrets must be protected and not exposed to AI prompts, responses, documents, or logs.

### Project Implementation

- Prohibit secrets in prompts
- Detect and block secrets
- Use secrets management tools outside the AI assistant
- Rotate exposed secrets if detected
- Do not store API keys in markdown files or logs
- Protect model provider credentials if future API use occurs

### Supporting Artifacts

- governance/data_classification.md
- security/prompt_injection_controls.md
- incident_response/ai_incident_response_playbook.md

---

# Incident Response Family

## IR-4: Incident Handling

### Control Relevance

AI-related security events require defined handling procedures.

### Project Implementation

Define response steps for:

- Prompt injection
- System prompt leakage
- Sensitive data exposure
- Unauthorized retrieval
- Poisoned documents
- Unsafe output
- Excessive usage
- Human review bypass
- Logging failure

### Supporting Artifacts

- incident_response/ai_incident_response_playbook.md

## IR-5: Incident Monitoring

### Control Relevance

AI incidents should be detected through monitoring and alerting.

### Project Implementation

Monitor:

- Prompt injection attempts
- Sensitive data detections
- Unauthorized retrieval
- System prompt extraction attempts
- Cost spikes
- Logging failures
- High-risk review events
- Administrative changes

### Supporting Artifacts

- security/logging_monitoring.md
- incident_response/ai_incident_response_playbook.md

## IR-6: Incident Reporting

### Control Relevance

AI-related incidents should be reported to appropriate internal teams.

### Project Implementation

Escalate incidents to:

- Security Operations
- Security Architecture
- IAM
- Data Owner
- Privacy
- Legal
- Compliance
- Vendor Risk
- Business Owner

### Supporting Artifacts

- incident_response/ai_incident_response_playbook.md
- governance/human_review_requirements.md

## IR-8: Incident Response Plan

### Control Relevance

The AI assistant should have a documented incident response plan.

### Project Implementation

- Define severity levels
- Define incident categories
- Define triage questions
- Define containment options
- Define evidence collection
- Define recovery and post-incident review
- Define escalation matrix

### Supporting Artifacts

- incident_response/ai_incident_response_playbook.md

---

# Planning Family

## PL-2: System Security and Privacy Plans

### Control Relevance

The AI assistant should have documented security and privacy planning artifacts.

### Project Implementation

- Document business case
- Document architecture
- Document data flows
- Document trust boundaries
- Document access control
- Document logging
- Document human review
- Document incident response
- Document compliance mappings

### Supporting Artifacts

- README.md
- business_case.md
- architecture/reference_architecture.md
- architecture/data_flow.md
- architecture/trust_boundaries.md

## PL-8: Security and Privacy Architectures

### Control Relevance

The AI assistant should be designed with security and privacy as architectural principles.

### Project Implementation

- Use local-first prototype to reduce exposure
- Enforce identity-aware retrieval
- Apply data classification
- Validate outputs
- Protect logs
- Require human review
- Avoid processing real sensitive data during initial phase
- Avoid cloud deployment until cost and governance controls are ready

### Supporting Artifacts

- architecture/reference_architecture.md
- architecture/deployment_options.md
- cost_controls.md

---

# Risk Assessment Family

## RA-3: Risk Assessment

### Control Relevance

AI use cases should be evaluated for data, access, prompt, model, vendor, operational, and compliance risk.

### Project Implementation

- Use AI risk assessment scoring
- Maintain AI risk register
- Identify prohibited and approved pilot use cases
- Assign risk owners
- Define risk treatment options
- Review risk before pilot or production deployment

### Supporting Artifacts

- governance/ai_risk_assessment.md

## RA-5: Vulnerability Monitoring and Scanning

### Control Relevance

The AI assistant may depend on libraries, tools, models, and infrastructure that require vulnerability monitoring.

### Project Implementation

For future implementation:

- Scan dependencies
- Pin package versions
- Review open-source libraries
- Review container images if used
- Monitor model and provider updates
- Track vulnerabilities in supporting components

### Supporting Artifacts

- security/owasp_llm_top10_mapping.md
- architecture/deployment_options.md

## RA-7: Risk Response

### Control Relevance

Identified AI risks require treatment decisions.

### Project Implementation

Risk treatment options include:

- Accept
- Mitigate
- Transfer
- Avoid
- Defer

High risks such as prompt injection, sensitive data exposure, unauthorized retrieval, and excessive agency should be mitigated or avoided.

### Supporting Artifacts

- governance/ai_risk_assessment.md
- incident_response/ai_incident_response_playbook.md

---

# System and Services Acquisition Family

## SA-4: Acquisition Process

### Control Relevance

If an AI provider, SaaS tool, or cloud service is used, security and privacy requirements must be included in evaluation.

### Project Implementation

Evaluate:

- Provider data handling
- Retention of prompts and responses
- Training on enterprise data
- Logging capability
- Region and data residency
- IAM integration
- Contractual obligations
- Exit strategy
- Cost model

### Supporting Artifacts

- governance/ai_use_case_intake.md
- architecture/deployment_options.md

## SA-9: External System Services

### Control Relevance

Third-party AI providers, SaaS tools, and cloud services must be reviewed and governed.

### Project Implementation

- Treat AWS Bedrock, Azure OpenAI, OpenAI API, and SaaS AI tools as reference designs only in early phases
- Require vendor risk review before use
- Prohibit sensitive data transfer without approval
- Confirm data retention and training policies
- Define service monitoring and incident escalation

### Supporting Artifacts

- architecture/deployment_options.md
- cloud_reference_only/aws_bedrock_design_only.md
- cloud_reference_only/azure_openai_design_only.md

## SA-10: Developer Configuration Management

### Control Relevance

If a local prototype or application is created, development artifacts should be controlled.

### Project Implementation

- Track code changes in GitHub
- Document configuration
- Do not commit secrets
- Use `.gitignore` for local logs, virtual environments, and credentials
- Review changes to prompt filters, access logic, and retrieval behavior

### Supporting Artifacts

- local_prototype/README.md
- cost_controls.md

## SA-11: Developer Testing and Evaluation

### Control Relevance

Prompt injection, access control, and retrieval behavior should be tested before any deployment.

### Project Implementation

Test:

- Prompt injection attempts
- System prompt extraction
- Unauthorized document retrieval
- Sensitive data prompts
- Restricted document requests
- Missing source citations
- Human review triggers
- Logging generation

### Supporting Artifacts

- security/prompt_injection_controls.md
- security/logging_monitoring.md
- governance/human_review_requirements.md

---

# System and Communications Protection Family

## SC-7: Boundary Protection

### Control Relevance

The AI assistant has multiple trust boundaries that require protection.

### Project Implementation

- Treat user input as untrusted
- Enforce identity boundary
- Enforce retrieval boundary
- Validate model output
- Protect logging boundary
- Separate administrative boundary
- Review cloud provider boundary before deployment

### Supporting Artifacts

- architecture/trust_boundaries.md

## SC-8: Transmission Confidentiality and Integrity

### Control Relevance

If deployed beyond local prototype, data transmitted between users, application, identity provider, retrieval layer, model, and logging system must be protected.

### Project Implementation

- Use TLS for communications
- Protect model API calls
- Protect log transmission
- Use private networking where appropriate
- Avoid sending sensitive data to unapproved external providers

### Supporting Artifacts

- architecture/deployment_options.md
- cloud_reference_only/aws_bedrock_design_only.md
- cloud_reference_only/azure_openai_design_only.md

## SC-12: Cryptographic Key Establishment and Management

### Control Relevance

Encryption keys and secrets must be protected if cloud or API services are used.

### Project Implementation

- Use approved secrets management tools
- Do not store credentials in prompts, documents, code, or logs
- Use KMS or Key Vault in cloud reference designs
- Rotate secrets if exposed
- Restrict key access

### Supporting Artifacts

- governance/data_classification.md
- incident_response/ai_incident_response_playbook.md

## SC-13: Cryptographic Protection

### Control Relevance

Sensitive documents, logs, embeddings, and configuration should be encrypted when stored or transmitted.

### Project Implementation

- Encrypt stored documents where applicable
- Encrypt logs where applicable
- Encrypt vector stores or embeddings based on source classification
- Encrypt API communications
- Use cloud-native encryption if cloud deployment occurs

### Supporting Artifacts

- governance/data_classification.md
- architecture/deployment_options.md

## SC-28: Protection of Information at Rest

### Control Relevance

Documents, logs, embeddings, and review records may contain sensitive information.

### Project Implementation

- Protect local files during prototype
- Avoid real sensitive data in local prototype
- Classify embeddings based on source data
- Restrict access to logs and review records
- Use encryption for cloud storage if deployed

### Supporting Artifacts

- governance/data_classification.md
- security/logging_monitoring.md

---

# System and Information Integrity Family

## SI-3: Malicious Code Protection

### Control Relevance

AI assistants may depend on libraries, document parsers, plugins, containers, or integrations that could introduce malicious code risk.

### Project Implementation

For future implementation:

- Scan dependencies
- Avoid untrusted plugins
- Review document processing libraries
- Avoid executing AI-generated code
- Treat AI output as untrusted

### Supporting Artifacts

- security/owasp_llm_top10_mapping.md
- architecture/deployment_options.md

## SI-4: System Monitoring

### Control Relevance

The system must be monitored for attacks, misuse, data leakage, unauthorized retrieval, and operational failures.

### Project Implementation

Monitor:

- Prompt injection
- Sensitive data submission
- System prompt extraction
- Unauthorized retrieval
- Excessive usage
- Model failures
- Logging failures
- Human review bypass
- Admin changes

### Supporting Artifacts

- security/logging_monitoring.md

## SI-10: Information Input Validation

### Control Relevance

User prompts and document content must be treated as untrusted input.

### Project Implementation

- Validate prompts
- Detect injection phrases
- Detect secrets and regulated data
- Flag restricted requests
- Scan documents for malicious embedded instructions
- Avoid treating retrieved content as instructions

### Supporting Artifacts

- security/prompt_injection_controls.md
- governance/data_classification.md
- architecture/trust_boundaries.md

## SI-12: Information Management and Retention

### Control Relevance

Prompt logs, response metadata, review records, documents, and embeddings require retention decisions.

### Project Implementation

- Avoid full prompt logging by default
- Define retention by log type
- Remove expired indexed content
- Retain human review records according to governance needs
- Define audit evidence retention

### Supporting Artifacts

- security/logging_monitoring.md
- governance/data_classification.md

---

# Supply Chain Risk Management Family

## SR-3: Supply Chain Controls and Processes

### Control Relevance

AI systems often depend on external models, APIs, open-source libraries, vector databases, and SaaS platforms.

### Project Implementation

- Review vendors before use
- Review provider data handling
- Track dependencies
- Pin versions
- Avoid unapproved plugins
- Maintain model/provider inventory
- Review cloud reference designs before deployment

### Supporting Artifacts

- security/owasp_llm_top10_mapping.md
- architecture/deployment_options.md
- governance/ai_use_case_intake.md

## SR-5: Acquisition Strategies, Tools, and Methods

### Control Relevance

Organizations should choose deployment models and providers based on risk, not convenience alone.

### Project Implementation

- Compare local mock, local LLM, cloud-managed, private hosting, and SaaS options
- Use local-first approach to reduce risk
- Require cloud cost and security decision gates
- Require vendor review before third-party provider use

### Supporting Artifacts

- architecture/deployment_options.md
- cost_controls.md

## SR-6: Supplier Assessments and Reviews

### Control Relevance

External AI providers and SaaS tools must be assessed before use.

### Project Implementation

Assess:

- Prompt and response retention
- Model training use
- Data residency
- Logging availability
- Security certifications
- Incident notification
- Access controls
- Admin capabilities
- Exit strategy

### Supporting Artifacts

- governance/ai_use_case_intake.md
- architecture/deployment_options.md

---

# AI-Specific Risk to NIST 800-53 Mapping

| AI Risk | Related NIST Control Areas | Project Control |
|---|---|---|
| Prompt Injection | SI-10, SI-4, AU-2, RA-3 | Prompt filtering, monitoring, logging, testing |
| Sensitive Data Disclosure | AC-3, AC-6, SC-28, AU-9, SI-12 | Access control, data classification, log minimization |
| Unauthorized Retrieval | AC-3, AC-16, AU-2, SI-4 | Document-level authorization and retrieval logs |
| System Prompt Leakage | SI-10, SI-4, SC-7 | Output validation and prompt hardening |
| Misinformation | CA-2, RA-3, SI-4 | Source citation, response validation, human review |
| Excessive Agency | AC-6, AC-5, CM-6 | Read-only design, least privilege, human approval |
| Poisoned Documents | CM-3, SI-10, RA-3 | Ingestion approval, content review, metadata controls |
| Weak Auditability | AU-2, AU-3, AU-6, AU-12 | Structured logging and correlation IDs |
| Vendor Data Exposure | SA-9, SR-6, SC-8 | Vendor review and data handling controls |
| Cost Spike | CA-7, SI-4, CM-6 | Usage monitoring, quotas, budget alerts |

---

# Minimum Control Baseline for Local Prototype

| Control Area | Requirement |
|---|---|
| Data | Use mock data only |
| Access | Use mock roles and role-based document filtering |
| Prompt Security | Detect and block known prompt injection patterns |
| Retrieval | Restrict retrieval by document classification |
| Logging | Log prompt metadata and access decisions locally |
| Human Review | Simulate review triggers for high-risk prompts |
| Secrets | Block obvious secret patterns |
| Cost | Do not use cloud services |
| Incident Response | Document mock incident scenarios |

## Minimum Control Baseline Before Cloud Deployment

| Control Area | Requirement |
|---|---|
| Identity | SSO and MFA |
| Access | Role and document-level authorization |
| Data | Data classification and owner approval |
| Model | Provider review and model configuration review |
| Logging | Central logging and alerting |
| Incident Response | AI incident response process |
| Human Review | Defined reviewer roles and workflow |
| Cost | Budget alerts, quotas, teardown plan |
| Encryption | Encryption in transit and at rest |
| Vendor Risk | Contract, retention, and training review |
| Compliance | Control mapping and evidence plan |

## Control Ownership

| Control Area | Primary Owner |
|---|---|
| Access Control | IAM Team and Security Architecture |
| Data Classification | Data Owner and Security Governance |
| Prompt Injection Controls | Security Architecture |
| Logging and Monitoring | Security Operations |
| Human Review | Security Governance and Control Owners |
| Incident Response | Security Operations |
| Vendor Risk | Vendor Risk Management |
| Compliance Mapping | Compliance and Security Architecture |
| Cost Controls | Platform Owner or FinOps |
| Configuration Management | AI System Administrator |

## Security Architect Notes

This NIST 800-53 mapping demonstrates that AI security is not separate from enterprise security architecture.

The AI assistant should be governed like an enterprise application, with additional controls for prompt injection, retrieval authorization, output validation, human review, and AI-specific incident response.

The most important architectural principle is that the AI model is not the control authority. Security controls must be enforced through identity, access control, metadata, application logic, logging, monitoring, and accountable human review.

## Conclusion

The secure AI assistant architecture aligns with NIST 800-53 by applying established security control families to AI-specific risks.

This mapping supports a regulated organization by showing how traditional controls such as access enforcement, audit logging, risk assessment, configuration management, incident response, boundary protection, input validation, and supply chain review apply to AI-enabled workflows.

The recommended implementation remains local-first and documentation-first until governance, cost controls, data handling, access control, logging, and human review are ready for any future deployment.
