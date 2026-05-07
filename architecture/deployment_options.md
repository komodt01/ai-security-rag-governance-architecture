# Deployment Options

## Purpose

This document compares deployment options for the secure enterprise AI assistant architecture.

The goal is to evaluate how the AI assistant could be implemented locally, internally, through cloud-managed AI services, or through third-party AI providers while maintaining security, governance, cost control, and compliance requirements.

This project begins with a local-first approach to avoid cloud cost exposure and reduce data handling risk.

## Scope

This document covers:

- Documentation-only architecture phase
- Local prototype option
- Local LLM option
- Mocked AI response option
- Internal enterprise deployment option
- AWS Bedrock reference design
- Azure OpenAI reference design
- OpenAI API reference design
- Private model hosting reference design
- SaaS AI tool option
- Deployment decision criteria
- Cost and risk considerations
- Recommended phased approach

## Deployment Principle

The recommended deployment principle is:

Architecture first. Local prototype second. Cloud deployment last.

No cloud deployment should occur until cost controls, access controls, logging requirements, data classification, provider review, teardown steps, and human review workflows are documented.

## Deployment Options Summary

| Option | Description | Cost Risk | Data Risk | Recommended For |
|---|---|---|---|---|
| Documentation Only | Architecture, governance, and control documentation only | None | None | Phase 1 portfolio and planning |
| Local Mock Prototype | Local app with mock users, mock documents, and simulated responses | None | Low | Safe hands-on demonstration |
| Local LLM Prototype | Local model using tools such as Ollama | Low | Low to Medium | Demonstrating AI behavior without cloud |
| Internal Enterprise Deployment | Company-hosted application and internal infrastructure | Medium | Medium to High | Controlled enterprise use |
| AWS Bedrock Reference | Managed model service through AWS | Medium to High | Medium to High | AWS architecture comparison only |
| Azure OpenAI Reference | Managed model service through Azure | Medium to High | Medium to High | Microsoft enterprise architecture comparison |
| OpenAI API Reference | External API-based model access | Medium | Medium to High | Vendor API comparison |
| Private Model Hosting | Self-hosted model on private infrastructure | High | Medium | Organizations needing maximum control |
| SaaS AI Tool | Commercial AI assistant or enterprise search product | Medium | Medium to High | Buy-versus-build evaluation |

## Option 1: Documentation-Only Architecture

### Description

This option includes only architecture, governance, security, compliance, and incident response documentation.

No AI model is deployed. No cloud resources are used. No APIs are called.

### Components

- Business case
- Reference architecture
- Data flow
- Trust boundaries
- STRIDE threat model
- OWASP LLM Top 10 mapping
- Prompt injection controls
- Access control model
- Logging and monitoring requirements
- AI risk assessment
- Data classification
- Human review requirements
- Compliance mappings
- Incident response playbook
- Cost controls

### Advantages

- No cloud cost
- No data exposure
- Strong architecture portfolio value
- Easy to publish in GitHub
- Demonstrates security architect thinking
- Supports interviews and resume discussion
- Safe for regulated environment examples

### Disadvantages

- No working prototype
- Does not demonstrate runtime behavior
- Some reviewers may want hands-on validation
- Does not prove prompt filtering or retrieval controls technically

### Cost Risk

None.

### Data Risk

None if only mock scenarios are documented.

### Recommendation

This is the correct starting point for the project.

## Option 2: Local Mock Prototype

### Description

This option creates a lightweight local application that simulates how a secure AI assistant would behave.

The prototype can use mock users, mock roles, mock documents, basic keyword retrieval, prompt injection detection, and local logs without requiring a real AI model.

### Components

- Python application
- Mock user roles
- Mock document set
- Document metadata file
- Local retrieval logic
- Prompt injection detection rules
- Sensitive data pattern detection
- Local JSONL logs
- Simulated AI responses
- Simulated human review triggers

### Example Folder Structure

- local_prototype/
  - README.md
  - app.py
  - requirements.txt
  - sample_users.json
  - sample_docs/
    - ai_usage_policy.md
    - cloud_logging_standard.md
    - iam_role_design_standard.md
    - incident_response_playbook.md
  - metadata/
    - document_metadata.json
  - tests/
    - prompt_injection_tests.md
  - logs/
    - prompt_events.jsonl
    - retrieval_events.jsonl
    - access_decisions.jsonl
    - security_alerts.jsonl

### Advantages

- No cloud cost
- No external AI provider
- Safe to test locally
- Demonstrates access control logic
- Demonstrates prompt injection detection
- Demonstrates logging and monitoring concepts
- Good hands-on extension for GitHub
- Avoids data exposure

### Disadvantages

- Simulated responses are less impressive than real AI output
- Retrieval may be basic
- Does not demonstrate model-specific behavior
- Requires some Python implementation

### Cost Risk

None.

### Data Risk

Low if only mock documents are used.

### Recommendation

This is the best Phase 2 hands-on implementation option.

## Option 3: Local LLM Prototype

### Description

This option uses a local model runtime, such as Ollama, to run a small model locally without sending prompts or documents to a cloud AI provider.

The AI assistant can retrieve mock documents and pass approved context to the local model.

### Possible Tools

- Python
- Streamlit
- Ollama
- ChromaDB or FAISS
- Local markdown documents
- Local JSON logs

### Components

- Local LLM runtime
- Local vector store or keyword retrieval
- Mock user roles
- Mock document classifications
- Prompt injection checks
- Retrieval authorization
- Response validation
- Local logging

### Advantages

- No paid model API
- No AWS or Azure cost
- Keeps data local
- Demonstrates real AI response generation
- Stronger hands-on story than a purely mocked prototype
- Good bridge between architecture and implementation

### Disadvantages

- Requires local setup
- Model quality depends on hardware and selected model
- Local models may be slower
- Still requires careful prompt and output handling
- Some laptops may struggle with larger models

### Cost Risk

Low to none, assuming existing local hardware.

### Data Risk

Low if only mock data is used.

### Recommendation

This is a good optional Phase 3 after the local mock prototype is working.

## Option 4: Internal Enterprise Deployment

### Description

This option deploys the AI assistant within an enterprise-controlled environment using internal infrastructure, enterprise identity, approved document repositories, internal logging, and governance workflows.

This could be hosted on internal Kubernetes, private cloud infrastructure, virtual machines, or enterprise platform services.

### Components

- Enterprise SSO
- Internal application hosting
- Approved document repositories
- Retrieval service
- Vector database or enterprise search
- Internal or approved model endpoint
- SIEM integration
- Human review workflow
- Governance approval process

### Advantages

- Strong enterprise control
- Better data governance
- Integration with internal IAM
- Supports document-level access
- Can integrate with enterprise logging
- Suitable for regulated environments

### Disadvantages

- Higher operational complexity
- Requires platform support
- Requires security review
- Requires data owner approval
- Requires monitoring and support
- May still require cloud or vendor services depending on model

### Cost Risk

Medium.

### Data Risk

Medium to high depending on data used.

### Recommendation

Appropriate only after governance, data classification, logging, and access controls are mature.

## Option 5: AWS Bedrock Reference Design

### Description

This option uses AWS Bedrock as a managed foundation model service. The assistant may retrieve approved documents from AWS storage or search services and send context to Bedrock for response generation.

This project should treat AWS Bedrock as a reference design only unless cost controls are fully implemented.

### Possible AWS Components

- Amazon Bedrock
- Amazon S3 for approved documents
- AWS IAM Identity Center
- IAM roles and policies
- AWS KMS
- AWS CloudTrail
- Amazon CloudWatch
- AWS Lambda
- Amazon OpenSearch Serverless or another retrieval layer
- AWS Budgets
- AWS Cost Explorer

### Advantages

- AWS-native architecture pattern
- Managed model access
- Integrates with IAM and CloudTrail
- Strong fit for AWS-focused portfolio discussions
- Useful for Solutions Architect or Cloud Security Architect positioning

### Disadvantages

- Cloud cost exposure
- Managed AI usage charges
- Possible retrieval or storage cost
- Requires careful IAM design
- Requires provider data handling review
- Requires teardown and budget controls
- Could become expensive if misconfigured

### Cost Risk

Medium to high.

### Data Risk

Medium to high depending on documents and provider configuration.

### Required Controls Before Deployment

- AWS Budget
- Billing alerts
- Service cost estimate
- IAM least privilege review
- KMS encryption design
- CloudTrail logging
- CloudWatch monitoring
- Data classification approval
- Document ingestion approval
- Teardown process
- Maximum spend limit
- Region selection
- Resource tagging
- Human review workflow
- Incident response plan

### Recommendation

Document as a cloud reference architecture only. Do not deploy during early project phases.

## Option 6: Azure OpenAI Reference Design

### Description

This option uses Azure OpenAI with Microsoft Entra ID, Azure Monitor, Azure Key Vault, storage services, and possibly Azure AI Search for retrieval.

This option may be appropriate for Microsoft-heavy enterprise environments.

### Possible Azure Components

- Azure OpenAI
- Microsoft Entra ID
- Azure AI Search
- Azure Blob Storage
- Azure Key Vault
- Azure Monitor
- Log Analytics Workspace
- Microsoft Sentinel
- Azure Policy
- Azure Cost Management

### Advantages

- Strong enterprise identity integration
- Good fit for Microsoft-heavy organizations
- Integrates with Entra ID and Azure monitoring
- Supports enterprise governance patterns
- Useful for regulated enterprise architecture discussions

### Disadvantages

- Cloud cost exposure
- Azure OpenAI access and configuration requirements
- Requires data handling review
- Requires careful logging and retention design
- Requires cost management
- Requires cloud deployment controls

### Cost Risk

Medium to high.

### Data Risk

Medium to high depending on data and configuration.

### Required Controls Before Deployment

- Azure budget alerts
- Cost estimate
- Entra ID access model
- Conditional Access requirements
- Key Vault for secrets
- Log Analytics monitoring
- Data classification review
- Provider data handling review
- Private networking review if applicable
- Teardown process
- Human review workflow
- Incident response process

### Recommendation

Document as a reference design. Do not deploy until cost and governance controls are complete.

## Option 7: OpenAI API Reference Design

### Description

This option uses the OpenAI API or another external AI API provider directly from the application.

The assistant sends approved prompts and context to the API and receives generated responses.

### Components

- Application layer
- API key or service credential
- Prompt handling layer
- Retrieval layer
- Model API call
- Response validation
- Logging
- Cost monitoring

### Advantages

- Easier to prototype than some cloud-native options
- Strong model capability
- Flexible application design
- No need to manage model infrastructure

### Disadvantages

- External provider data handling risk
- API key management required
- Usage-based cost risk
- Requires vendor review
- Requires prompt and response logging decisions
- Requires careful data minimization

### Cost Risk

Medium.

### Data Risk

Medium to high depending on data sent.

### Required Controls Before Deployment

- API usage limits
- Budget threshold
- API key protection
- Provider data retention review
- No sensitive data without approval
- Prompt and response filtering
- Logging minimization
- Human review triggers
- Incident response plan

### Recommendation

Use only as a reference option unless explicitly approved. Local-first remains safer.

## Option 8: Private Model Hosting

### Description

This option hosts a model on private infrastructure controlled by the organization.

The model may run on internal servers, private cloud infrastructure, Kubernetes, GPUs, or dedicated AI platforms.

### Components

- Private compute environment
- Model runtime
- Model artifact repository
- Vector database or retrieval service
- Internal identity integration
- Logging and monitoring
- Model lifecycle management
- Security hardening
- Patch management

### Advantages

- Maximum infrastructure control
- Reduced external data exposure
- Can support strict data residency requirements
- Customizable security controls
- Avoids external model API retention concerns

### Disadvantages

- High complexity
- High infrastructure cost
- Requires AI/ML operations expertise
- Requires GPU or high-performance compute for larger models
- Requires patching, monitoring, scaling, and lifecycle management
- Model performance may lag managed providers

### Cost Risk

High.

### Data Risk

Medium, depending on internal controls.

### Recommendation

Not recommended for this project unless the organization has strong AI platform engineering capability.

## Option 9: SaaS AI Assistant or Enterprise Search Tool

### Description

This option uses a vendor-provided AI assistant, enterprise search tool, or knowledge management product.

Examples may include AI-enabled workplace search, document assistant tools, productivity suite AI features, or vendor-hosted RAG platforms.

### Components

- SaaS provider
- Enterprise SSO integration
- Document connector
- Vendor-managed model
- Vendor logs and admin portal
- Data access permissions
- Governance controls

### Advantages

- Faster deployment
- Vendor-managed infrastructure
- Often integrates with enterprise productivity tools
- May include built-in governance features
- Lower internal engineering burden

### Disadvantages

- Vendor data handling risk
- Connector permission complexity
- Harder to validate retrieval behavior
- Possible overbroad document access
- Limited control over model behavior
- Licensing cost
- Audit evidence may depend on vendor capabilities

### Cost Risk

Medium.

### Data Risk

Medium to high.

### Required Controls Before Deployment

- Vendor risk review
- Contract review
- Data retention review
- Training data opt-out review
- SSO and MFA integration
- Connector permission review
- Least privilege document access
- Logging and audit evidence review
- Admin role review
- User training
- Acceptable use policy

### Recommendation

Useful for buy-versus-build comparison, but not the best starting point for this portfolio project.

## Deployment Decision Matrix

| Criteria | Documentation Only | Local Mock | Local LLM | AWS Bedrock | Azure OpenAI | OpenAI API | Private Hosting | SaaS AI |
|---|---|---|---|---|---|---|---|---|
| No Cloud Cost | Yes | Yes | Yes | No | No | Partial | No | No |
| No External Data Transfer | Yes | Yes | Yes | No | No | No | Yes | No |
| Hands-On Demo Value | Low | Medium | High | High | High | High | High | Medium |
| Security Architecture Value | High | High | High | High | High | High | High | Medium |
| Implementation Complexity | Low | Medium | Medium | High | High | Medium | Very High | Low |
| Cost Risk | None | None | Low | Medium/High | Medium/High | Medium | High | Medium |
| Data Risk | None | Low | Low | Medium/High | Medium/High | Medium/High | Medium | Medium/High |
| Best for Phase 1 | Yes | No | No | No | No | No | No | No |
| Best for Phase 2 | No | Yes | Optional | No | No | No | No | No |
| Best for Reference Design | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

## Recommended Phased Roadmap

### Phase 1: Documentation-First Architecture

Status: Recommended starting point.

Deliverables:

- README
- Business case
- Reference architecture
- Data flow
- Trust boundaries
- STRIDE threat model
- OWASP LLM Top 10 mapping
- Prompt injection controls
- Access control model
- Logging and monitoring requirements
- AI risk assessment
- Data classification
- Human review requirements
- NIST AI RMF mapping
- Incident response playbook
- Cost controls

Cost: $0.

### Phase 2: Local Mock Prototype

Status: Recommended next hands-on step.

Deliverables:

- Mock users
- Mock roles
- Mock documents
- Document metadata
- Prompt injection detection
- Role-based retrieval filtering
- Local logs
- Simulated response validation
- Simulated human review triggers

Cost: $0.

### Phase 3: Local LLM Prototype

Status: Optional after local mock prototype.

Deliverables:

- Local model runtime
- Local RAG pattern
- Local vector store
- Response generation from mock documents
- Prompt and response filtering
- Local logging

Cost: $0 or low depending on local hardware.

### Phase 4: Cloud Reference Architecture Only

Status: Optional documentation expansion.

Deliverables:

- AWS Bedrock design only
- Azure OpenAI design only
- OpenAI API design only
- Cloud cost controls
- IAM design
- Logging design
- Teardown plans
- Cloud risk assessment

Cost: $0 if not deployed.

### Phase 5: Controlled Cloud Pilot

Status: Not recommended until required.

Required before deployment:

- Business reason
- Cost estimate
- Budget alerts
- Teardown process
- Data classification
- Provider review
- IAM review
- Logging and monitoring
- Incident response
- Human review
- Maximum spend threshold

Cost: Variable.

## Cost Decision Gate

Before any cloud deployment, answer the following questions.

| Question | Required Answer |
|---|---|
| What objective requires cloud deployment? |  |
| Can the same objective be demonstrated locally? |  |
| What services will be used? |  |
| What is the hourly cost? |  |
| What is the estimated monthly cost? |  |
| What resources continue billing after testing? |  |
| What is the maximum approved spend? |  |
| Who receives budget alerts? |  |
| What is the teardown process? |  |
| What data will be used? |  |
| Has data been classified? |  |
| Has provider data handling been reviewed? |  |
| Who owns the deployment? |  |
| When will resources be destroyed? |  |

## High-Risk Services to Avoid Early

Avoid the following during early phases:

- Long-running EC2 instances
- NAT Gateway
- Managed Kubernetes clusters
- Managed OpenSearch clusters
- High-throughput vector databases
- SageMaker endpoints
- GPU instances
- Multi-AZ databases
- Large log ingestion
- Large document datasets
- Always-on API services
- Production connectors

## Safer Early Options

Use the following instead:

- Markdown files
- Local Python scripts
- Local mock documents
- Local JSON logs
- Local role simulation
- Local prompt filters
- Documentation-only cloud reference designs
- GitHub repository structure
- Architecture diagrams

## Security Decision Gate

Before moving beyond local prototype, confirm:

| Requirement | Status |
|---|---|
| Data classification complete | Not Started |
| Access control model complete | Not Started |
| Prompt injection controls complete | Not Started |
| Retrieval authorization design complete | Not Started |
| Logging requirements complete | Not Started |
| Human review workflow complete | Not Started |
| Incident response playbook complete | Not Started |
| Cost controls complete | Not Started |
| Vendor review complete if applicable | Not Started |
| Compliance mapping complete | Not Started |

## Deployment Recommendation

For this project, the recommended deployment path is:

1. Documentation-only architecture
2. Local mock prototype
3. Optional local LLM prototype
4. Cloud reference designs only
5. Controlled cloud pilot only if there is a clear business or learning need

The project should not begin with AWS, Azure, OpenAI API, or any paid AI service.

## Security Architect Notes

The deployment decision should be based on risk, business need, and control readiness, not excitement around AI tooling.

For a security architect, the important question is not simply, “Can we deploy an AI assistant?”

The better questions are:

- What data will it access?
- Who can use it?
- What can it influence?
- What happens if it is wrong?
- What happens if it leaks data?
- How is it monitored?
- Who reviews high-risk output?
- What is the cost exposure?
- Can we shut it down quickly?
- Can we prove the controls worked?

## Conclusion

The safest and most practical starting point is a documentation-first and local-first AI security project.

This approach demonstrates architecture, governance, access control, prompt security, data protection, logging, human review, incident response, and compliance alignment without exposing the project owner to unexpected cloud costs.

Cloud deployment should remain optional and should only occur after cost, security, governance, and data handling controls are fully documented.
