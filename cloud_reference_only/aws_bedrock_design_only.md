# AWS Bedrock Design Only

## Purpose

This document describes a design-only AWS reference architecture for a secure enterprise AI assistant using Amazon Bedrock.

This file is intentionally limited to architecture planning. It does not include Terraform deployment, AWS CLI deployment commands, or implementation steps that would create billable resources.

The goal is to show how the local-first AI security architecture could be translated into an AWS-native pattern while preserving access control, data protection, logging, human review, cost governance, and incident response requirements.

## Design-Only Statement

This is a reference architecture only.

Do not deploy this design unless the following are completed first:

- AWS Budget configured
- Billing alerts configured
- Cost estimate completed
- Teardown process documented
- IAM design reviewed
- Data classification completed
- Provider data handling reviewed
- Logging and monitoring design approved
- Human review workflow defined
- Incident response process documented
- Maximum spend threshold approved

## Business Scenario

A regulated organization wants to provide an internal AI assistant that allows employees to ask questions about approved internal policies, security standards, IAM guidance, compliance mappings, and architecture documents.

The organization wants to use AWS-native services while reducing risks related to:

- Prompt injection
- Unauthorized document retrieval
- Sensitive data exposure
- Overreliance on AI responses
- Weak auditability
- Excessive AI autonomy
- Cloud cost overrun
- Misconfigured IAM
- Inadequate human review

## Reference Architecture Components

| Component | AWS Service Option | Purpose |
|---|---|---|
| User Authentication | AWS IAM Identity Center or external IdP federation | Authenticate workforce users |
| Application Layer | AWS Lambda, ECS, or App Runner | Host AI assistant application logic |
| API Layer | Amazon API Gateway or Application Load Balancer | Expose controlled application endpoint |
| Document Storage | Amazon S3 | Store approved internal documents |
| Document Encryption | AWS KMS | Encrypt documents and logs |
| Retrieval Layer | OpenSearch Serverless, Amazon Kendra, or custom vector store | Retrieve approved document context |
| AI Model | Amazon Bedrock | Generate responses from approved context |
| Logging | CloudWatch Logs and CloudTrail | Capture activity and administrative events |
| Monitoring | CloudWatch Metrics, Alarms, and Security Hub integration | Detect misuse and operational issues |
| Notification | Amazon SNS | Notify reviewers or security teams |
| Human Review Workflow | Step Functions, SNS, or ticketing integration | Route high-risk responses for review |
| Cost Governance | AWS Budgets and Cost Explorer | Monitor and control spend |
| Secrets Management | AWS Secrets Manager or Parameter Store | Store application secrets if needed |

## High-Level Flow

1. User authenticates through IAM Identity Center or a federated identity provider.
2. User submits a prompt through the AI assistant application.
3. The application validates user identity, role, and group membership.
4. Prompt handling logic checks for prompt injection, sensitive data, or prohibited requests.
5. Retrieval layer searches only documents the user is authorized to access.
6. Retrieved context is minimized and classified before model interaction.
7. Amazon Bedrock receives only authorized, minimized context.
8. Bedrock generates a response.
9. Response validation checks for sensitive content, unsupported claims, and high-risk recommendations.
10. Low-risk responses are returned with source references.
11. High-risk responses are routed to human review.
12. Logs are written to CloudWatch and administrative events are captured in CloudTrail.
13. Security events, usage trends, and cost signals are monitored.

## Identity and Access Control Design

### Workforce Identity

Recommended options:

- AWS IAM Identity Center
- SAML federation from Microsoft Entra ID, Okta, or another enterprise IdP
- OIDC federation where appropriate

### Access Control Requirements

- Require SSO
- Require MFA
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

## Document Storage Design

Amazon S3 may be used to store approved documents.

### S3 Requirements

- Use dedicated bucket for approved AI documents
- Block public access
- Encrypt with AWS KMS
- Apply bucket policies
- Use object versioning if appropriate
- Require document metadata
- Separate document prefixes by classification if needed
- Do not store secrets or regulated data unless formally approved

### Example Document Prefixes

| Prefix | Purpose |
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

Possible retrieval options include:

- Amazon OpenSearch Serverless
- Amazon Kendra
- Custom vector store
- Simple metadata-aware retrieval service

This project does not require deploying any retrieval service during the documentation phase.

### Retrieval Requirements

- Enforce document-level authorization before retrieval
- Filter by role, group, classification, status, and expiration date
- Deny documents with missing metadata
- Preserve source document IDs
- Preserve classification labels
- Log retrieved and denied document references
- Prevent unrestricted search across all repositories

## Amazon Bedrock Design

Amazon Bedrock may be used as the managed model interface.

### Bedrock Requirements

- Send only authorized and minimized context
- Do not send secrets
- Do not send regulated data unless formally approved
- Do not rely on the model as the access control authority
- Track model ID and configuration
- Log model interaction metadata
- Validate responses before release
- Use guardrails where appropriate
- Review provider and service data handling

## Prompt Injection Controls

The AWS design should preserve the same prompt injection controls defined in the project.

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

### CloudWatch Logs

CloudWatch Logs may capture:

- Prompt metadata
- Prompt risk score
- Access decisions
- Retrieval events
- Response validation outcomes
- Human review triggers
- Security alerts
- Application errors
- Usage metrics

### CloudTrail

CloudTrail should capture:

- IAM changes
- S3 administrative activity
- KMS activity
- Bedrock administrative actions where applicable
- Logging configuration changes
- Security-relevant administrative events

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
- Model ID
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
| Admin misconfiguration | Guardrail, IAM, or retrieval setting changed unexpectedly |

## Human Review Workflow

High-risk AI responses should be routed to human review.

Possible AWS design options:

- Step Functions workflow
- SNS notification
- Integration with ticketing system
- Manual review queue
- Security operations workflow

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

The AWS design should support investigation of:

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
- CloudTrail events
- CloudWatch logs
- Admin change history
- Cost and usage data

## Data Protection Requirements

| Area | Requirement |
|---|---|
| Documents | Encrypt with KMS |
| Logs | Restrict access and define retention |
| Prompts | Minimize logging of full text |
| Responses | Avoid full response logging unless justified |
| Embeddings | Classify based on source content |
| Secrets | Store only in Secrets Manager or Parameter Store |
| Network | Use secure transport |
| Access | Enforce least privilege |

## Cost Controls

Before any AWS deployment, configure:

- AWS Budget
- Budget email alert
- Maximum spend threshold
- Daily cost review during testing
- Resource tagging
- Teardown checklist
- Usage quotas
- Service limits
- Log retention limits
- No always-on resources unless justified

## AWS Services With Cost Risk

Avoid or carefully review:

- NAT Gateway
- OpenSearch
- SageMaker
- Kendra
- Always-on EC2
- Managed Kubernetes
- Large CloudWatch log ingestion
- Large S3 datasets
- Provisioned throughput services
- GPU instances
- Long-running endpoints

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

## AWS Deployment Decision Gate

Do not deploy until the following are answered:

| Question | Required Answer |
|---|---|
| Why is AWS deployment needed? |  |
| Can this be demonstrated locally? |  |
| Which AWS services will be used? |  |
| What is the estimated monthly cost? |  |
| What resources bill continuously? |  |
| What is the maximum approved spend? |  |
| Has AWS Budget been configured? |  |
| Has data been classified? |  |
| Has IAM been reviewed? |  |
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
| IAM misconfiguration | Least privilege and access reviews |
| Vendor or service dependency | Provider review and fallback plan |
| Excessive agency | Read-only initial design |
| Logging sensitive data | Log minimization and access control |

## Security Architect Notes

The AWS design demonstrates how the secure AI assistant architecture could map to AWS-native services.

However, the design should remain reference-only until there is a clear reason to deploy.

The project’s strongest value is the architecture thinking: identity-aware retrieval, data classification, prompt injection controls, logging, human review, incident response, and cost governance.

## Conclusion

Amazon Bedrock can support a secure enterprise AI assistant architecture, but only when surrounded by strong governance and security controls.

The recommended path remains:

1. Documentation-first architecture
2. Local mock prototype
3. Optional local LLM prototype
4. AWS reference design only
5. Controlled AWS pilot only after cost, security, and data controls are complete

This document should not be treated as deployment approval.
