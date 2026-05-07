# Azure OpenAI Design Only

## Purpose

This document describes a design-only Azure reference architecture for a secure enterprise AI assistant using Azure OpenAI.

This file is intentionally limited to architecture planning. It does not include Azure CLI deployment commands, Terraform deployment, Bicep deployment, or implementation steps that would create billable resources.

The goal is to show how the local-first AI security architecture could be translated into an Azure-native pattern while preserving identity, access control, data protection, logging, monitoring, human review, cost governance, and incident response requirements.

## Design-Only Statement

This is a reference architecture only.

Do not deploy this design unless the following are completed first:

- Azure budget configured
- Cost alert configured
- Cost estimate completed
- Teardown process documented
- Microsoft Entra ID access model reviewed
- Data classification completed
- Provider data handling reviewed
- Logging and monitoring design approved
- Human review workflow defined
- Incident response process documented
- Maximum spend threshold approved

## Business Scenario

A regulated organization wants to provide an internal AI assistant that allows employees to ask questions about approved internal policies, security standards, IAM guidance, compliance mappings, and architecture documents.

The organization wants to use Azure-native services while reducing risks related to:

- Prompt injection
- Unauthorized document retrieval
- Sensitive data exposure
- Overreliance on AI responses
- Weak auditability
- Excessive AI autonomy
- Cloud cost overrun
- Misconfigured identity and access
- Inadequate human review

## Reference Architecture Components

| Component | Azure Service Option | Purpose |
|---|---|---|
| User Authentication | Microsoft Entra ID | Authenticate workforce users |
| Conditional Access | Microsoft Entra Conditional Access | Enforce MFA and access conditions |
| Application Layer | Azure App Service, Azure Functions, or Container Apps | Host AI assistant logic |
| API Layer | Azure API Management or App Service endpoint | Expose controlled application endpoint |
| Document Storage | Azure Blob Storage or SharePoint connector pattern | Store approved internal documents |
| Document Encryption | Azure Storage encryption and Key Vault | Protect documents and secrets |
| Retrieval Layer | Azure AI Search | Retrieve approved document context |
| AI Model | Azure OpenAI | Generate responses from approved context |
| Logging | Azure Monitor and Log Analytics | Capture application and security events |
| SIEM | Microsoft Sentinel | Monitor high-risk activity |
| Secrets Management | Azure Key Vault | Store application secrets |
| Human Review Workflow | Logic Apps, Teams notification, or ticketing integration | Route high-risk output for review |
| Cost Governance | Azure Cost Management | Monitor and control spend |

## High-Level Flow

1. User authenticates through Microsoft Entra ID.
2. Conditional Access enforces MFA and access requirements.
3. User submits a prompt through the AI assistant application.
4. The application validates user identity, role, and group membership.
5. Prompt handling logic checks for prompt injection, sensitive data, or prohibited requests.
6. Retrieval layer searches only documents the user is authorized to access.
7. Retrieved context is minimized and classified before model interaction.
8. Azure OpenAI receives only authorized and minimized context.
9. Azure OpenAI generates a response.
10. Response validation checks for sensitive content, unsupported claims, and high-risk recommendations.
11. Low-risk responses are returned with source references.
12. High-risk responses are routed to human review.
13. Logs are written to Azure Monitor and Log Analytics.
14. Security events may be sent to Microsoft Sentinel.
15. Usage and cost are monitored through Azure Cost Management.

## Identity and Access Control Design

### Workforce Identity

Recommended identity platform:

- Microsoft Entra ID

### Access Control Requirements

- Require Entra ID authentication
- Require MFA through Conditional Access
- Use group-based access
- Enforce least privilege
- Deny access by default
- Separate user, reviewer, administrator, and content owner roles
- Do not allow application administrators to automatically access all restricted documents

### Example Roles

| Role | Purpose |
|---|---|
| General Employee | Access general internal documents |
| Engineer | Access approved technical and cloud standards |
| Security Architect | Access security architecture and approved restricted guidance |
| IAM Analyst | Access IAM standards and access governance documents |
| Compliance Analyst | Access compliance mappings and audit guidance |
| Security Reviewer | Review high-risk AI output |
| AI System Administrator | Manage application configuration |
| Audit Viewer | Review evidence and logs |

## Conditional Access Design

Conditional Access may enforce:

- MFA
- Managed device requirement
- Location-based conditions
- Risk-based sign-in policies
- Privileged access restrictions
- Session controls

High-risk roles such as reviewers, administrators, and audit viewers should have stronger access requirements.

## Document Storage Design

Azure Blob Storage or another approved enterprise document source may be used for approved documents.

### Storage Requirements

- Use dedicated storage for approved AI documents
- Disable public access
- Encrypt data at rest
- Use managed identities where possible
- Apply role-based access
- Require document metadata
- Separate documents by classification if appropriate
- Do not store secrets or regulated data unless formally approved

### Example Document Containers or Paths

| Location | Purpose |
|---|---|
| public/ | Publicly approved reference documents |
| internal/ | General internal documents |
| confidential/ | Role-restricted internal documents |
| restricted/ | Highly controlled documents |
| quarantine/ | Documents pending review and not available for retrieval |

## Document Metadata Requirements

Each document should include metadata such as:

- Document ID
- Owner
- Classification
- Approved roles
- Approved groups
- Source system
- Status
- Review date
- Expiration date
- Version
- Human review requirement

## Retrieval Layer Design

Azure AI Search may be used as the retrieval layer.

This project does not require deploying Azure AI Search during the documentation phase.

### Retrieval Requirements

- Enforce document-level authorization before retrieval
- Filter by role, group, classification, status, and expiration date
- Deny documents with missing metadata
- Preserve source document IDs
- Preserve classification labels
- Log retrieved and denied document references
- Prevent unrestricted search across all repositories

## Azure OpenAI Design

Azure OpenAI may be used as the managed model interface.

### Azure OpenAI Requirements

- Send only authorized and minimized context
- Do not send secrets
- Do not send regulated data unless formally approved
- Do not rely on the model as the access control authority
- Track model deployment, model name, and version
- Log model interaction metadata
- Validate responses before release
- Review provider and service data handling

## Managed Identity and Secrets

Recommended approach:

- Use managed identities where possible
- Store secrets in Azure Key Vault
- Avoid hardcoded API keys
- Do not store credentials in prompts, responses, documents, or logs
- Rotate any exposed secret
- Restrict Key Vault access by role

## Prompt Injection Controls

The Azure design should preserve the same prompt injection controls defined in the project.

Required controls:

- Input filtering
- Injection phrase detection
- System prompt hardening
- Retrieval scope limitation
- Context isolation
- Output validation
- Human review routing
- Security alerting
- Prompt injection testing

Prompt injection attempts should be logged and monitored.

## Response Validation

Before returning AI output to the user, the application should check for:

- Sensitive data
- Credentials or secrets
- Restricted document content
- Unsupported claims
- Missing source citations
- Security exception approval language
- Access approval language
- Production change recommendations
- Legal or compliance conclusions
- Incident response instructions

High-risk responses should be routed to human review.

## Logging and Monitoring Design

### Azure Monitor and Log Analytics

Azure Monitor and Log Analytics may capture:

- Prompt metadata
- Prompt risk score
- Access decisions
- Retrieval events
- Response validation outcomes
- Human review triggers
- Security alerts
- Application errors
- Usage metrics

### Microsoft Sentinel

Microsoft Sentinel may be used to monitor and investigate:

- Prompt injection attempts
- Unauthorized retrieval attempts
- Sensitive data detections
- System prompt extraction attempts
- Excessive usage
- Human review bypass
- Administrative changes
- Cost or operational anomalies

### Recommended Log Fields

- Timestamp
- User ID
- User role
- Prompt ID
- Risk score
- Policy action
- Retrieved document IDs
- Denied document IDs
- Document classification
- Model deployment
- Response status
- Human review decision
- Correlation ID

## Security Monitoring Use Cases

| Use Case | Detection Signal |
|---|---|
| Prompt injection attempt | Prompt contains instruction override language |
| System prompt extraction | User asks for hidden instructions |
| Unauthorized retrieval | User attempts to access denied document category |
| Sensitive data submission | Prompt contains secret, regulated data, or credential pattern |
| Restricted output | Response validation detects restricted content |
| Human review bypass | High-risk response released without review |
| Excessive usage | Prompt or token volume exceeds threshold |
| Cost spike | Daily spend exceeds expected level |
| Logging failure | Expected logs are missing |
| Admin misconfiguration | Guardrail, access, model, or retrieval setting changed unexpectedly |

## Human Review Workflow

High-risk AI responses should be routed to human review.

Possible Azure design options:

- Logic Apps
- Microsoft Teams notification
- ServiceNow or ticketing integration
- Microsoft Sentinel incident workflow
- Manual review queue

Human review should be required for:

- Security exceptions
- Access approval
- Privileged access
- Compliance interpretation
- Legal interpretation
- Incident response recommendations
- Production change guidance
- Restricted data
- Regulated data
- Unsupported AI claims

## Incident Response Design

The Azure design should support investigation of:

- Prompt injection
- System prompt leakage
- Sensitive data exposure
- Unauthorized document retrieval
- Poisoned documents
- Unsafe output
- Excessive usage
- Cost spike
- Human review bypass
- Logging failure

Required evidence:

- User ID
- Prompt metadata
- Retrieved documents
- Response metadata
- Policy decisions
- Human review logs
- Azure Monitor logs
- Microsoft Sentinel incidents
- Entra ID sign-in logs
- Admin change history
- Cost and usage data

## Data Protection Requirements

| Area | Requirement |
|---|---|
| Documents | Encrypt at rest |
| Logs | Restrict access and define retention |
| Prompts | Minimize logging of full text |
| Responses | Avoid full response logging unless justified |
| Embeddings | Classify based on source content |
| Secrets | Store only in Key Vault |
| Network | Use secure transport |
| Access | Enforce least privilege |

## Cost Controls

Before any Azure deployment, configure:

- Azure budget
- Cost alerts
- Maximum spend threshold
- Daily cost review during testing
- Resource tagging
- Teardown checklist
- Usage quotas
- Service limits
- Log retention limits
- No always-on resources unless justified

## Azure Services With Cost Risk

Avoid or carefully review:

- Azure AI Search
- Large Log Analytics ingestion
- Always-on App Service plans
- Container Apps with sustained usage
- Azure Kubernetes Service
- Large storage datasets
- High-volume model calls
- Premium networking features
- Unbounded diagnostics
- Long-running compute

## Required Tags

| Tag | Purpose |
|---|---|
| Project | ai-security-rag-governance-architecture |
| Environment | dev, test, or pilot |
| Owner | Responsible person or team |
| CostCenter | Cost tracking |
| ExpirationDate | Planned teardown date |
| DataClassification | Highest data classification |
| DeploymentType | design-only, local, pilot, or production |

## Azure Deployment Decision Gate

Do not deploy until the following are answered:

| Question | Required Answer |
|---|---|
| Why is Azure deployment needed? |  |
| Can this be demonstrated locally? |  |
| Which Azure services will be used? |  |
| What is the estimated monthly cost? |  |
| What resources bill continuously? |  |
| What is the maximum approved spend? |  |
| Has Azure budget alerting been configured? |  |
| Has data been classified? |  |
| Has Entra ID access design been reviewed? |  |
| Has teardown been documented? |  |
| Who owns the deployment? |  |
| When will resources be destroyed? |  |

## Risks

| Risk | Mitigation |
|---|---|
| Cloud cost overrun | Budgets, quotas, teardown, local-first testing |
| Unauthorized document retrieval | Metadata filtering and document-level authorization |
| Sensitive data exposure | Data classification, prompt filtering, output validation |
| Prompt injection | Defense-in-depth controls |
| Model overreliance | Human review and advisory-only wording |
| Weak auditability | Structured logging and correlation IDs |
| Entra ID misconfiguration | Least privilege and access reviews |
| Vendor or service dependency | Provider review and fallback plan |
| Excessive agency | Read-only initial design |
| Logging sensitive data | Log minimization and access control |

## Security Architect Notes

The Azure design demonstrates how the secure AI assistant architecture could map to Azure-native services.

However, the design should remain reference-only until there is a clear reason to deploy.

The project’s strongest value is the architecture thinking: Entra ID-based access, identity-aware retrieval, data classification, prompt injection controls, logging, human review, incident response, and cost governance.

## Conclusion

Azure OpenAI can support a secure enterprise AI assistant architecture, but only when surrounded by strong governance and security controls.

The recommended path remains:

1. Documentation-first architecture
2. Local mock prototype
3. Optional local LLM prototype
4. Azure reference design only
5. Controlled Azure pilot only after cost, security, and data controls are complete

This document should not be treated as deployment approval.
