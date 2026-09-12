# Deployment Options

## Purpose

This document compares deployment approaches for the secure enterprise AI assistant architecture.

The objective is not to select a cloud platform by default. The objective is to determine which deployment model best satisfies the business requirement while balancing security, data handling, governance, operational complexity, and cost.

This project follows a local-first approach. Phase 1 established the architecture and governance model, and Phase 2 implemented a limited local security-control prototype.

AWS, Azure, external AI APIs, private model hosting, and SaaS AI platforms are evaluated as architecture options. They have not been deployed as part of this project.

## Deployment Principle

The guiding principle for this project is:

> Architecture first. Validate controls locally. Introduce model or cloud dependencies only when they provide additional value.

A more sophisticated deployment is not automatically a better architecture.

Before introducing a cloud or external AI service, I would want to understand:

- What business or technical objective requires it
- What data will cross the boundary
- How identity and authorization will work
- What provider or vendor risks are introduced
- What monitoring and incident evidence will exist
- What the operational dependencies are
- What the cost exposure is
- How the service can be disabled or removed

## Current Project State

The project currently includes two implemented phases.

### Phase 1: Architecture and Governance

Completed architecture work includes:

- Business case
- Reference architecture
- Data-flow analysis
- Trust-boundary analysis
- Threat modeling
- Access-control design
- Data-classification design
- Prompt injection control strategy
- Logging and monitoring requirements
- Human-review requirements
- Incident-response planning
- Security and compliance mappings
- Cost-control strategy
- Cloud reference designs

### Phase 2: Local Security-Control Prototype

A local Python prototype was implemented using:

- Mock users and roles
- Mock groups
- Synthetic documents
- Document metadata
- Pattern-based prompt-risk evaluation
- Sensitive-data pattern detection
- Simplified keyword retrieval
- Role- and group-based authorization
- Local JSONL logging
- Security alerts
- Simulated human-review triggers
- Advisory response generation

The prototype does not use an LLM, embeddings, vector database, production identity provider, cloud AI service, or real enterprise data.

Initial documented testing validated an authorized retrieval path and a prompt injection attempt blocked before retrieval.

Additional test scenarios are defined but have not yet been executed.

## Deployment Options Summary

| Option | External Dependency | Relative Complexity | Cost Exposure | Project Status |
| --- | --- | --- | --- | --- |
| Documentation / Architecture | None | Low | None | Completed |
| Local Security-Control Prototype | None | Low–Medium | None | Implemented |
| Local LLM | Local model runtime | Medium | Low | Optional |
| Internal Enterprise Platform | Enterprise infrastructure | High | Medium–High | Architecture option |
| AWS Bedrock | AWS | High | Variable | Reference design only |
| Azure OpenAI | Azure | High | Variable | Reference design only |
| External AI API | External provider | Medium | Variable | Architecture option |
| Private Model Hosting | Internal/private infrastructure | Very High | High | Architecture option |
| SaaS AI Platform | SaaS vendor | Medium | Subscription/usage | Architecture option |

The cost and complexity assessments are illustrative. Actual values would depend on workload, scale, architecture, licensing, and organizational capabilities.

# Option 1: Local Security-Control Prototype

## Description

This is the deployment approach implemented for Phase 2.

The prototype intentionally separates security-control validation from model deployment.

It demonstrates how security decisions can surround an AI/RAG-style workflow without requiring a production AI stack.

## Architecture

The implemented sequence is:

**Mock Identity → Prompt Risk Evaluation → Local Retrieval → Metadata Authorization → Logging / Review Trigger → Advisory Response**

## Advantages

- No cloud cost
- No external AI provider
- No real enterprise data
- Easy to execute and inspect
- Demonstrates authorization logic
- Demonstrates pre-retrieval blocking
- Produces security-event evidence
- Keeps implementation focused on architecture controls

## Limitations

- No actual LLM
- No embeddings
- No semantic retrieval
- No production identity integration
- No enterprise SIEM
- No production human-review workflow
- No model-specific security testing
- Simplified pattern-based detection

## Architecture Decision

For this project, this was sufficient to validate selected security-control concepts without introducing unnecessary cost or infrastructure.

# Option 2: Local LLM

## Description

A future extension could introduce a locally hosted model using a runtime such as Ollama or another local inference platform.

Authorized local content could then be provided to the model after the existing security controls have been applied.

## Possible Components

Examples could include:

- Local model runtime
- Python application
- Existing mock identity and authorization controls
- Local documents
- Keyword or semantic retrieval
- Optional local vector store
- Response validation
- Local logging

## Advantages

- Introduces actual model behavior
- Keeps synthetic information local
- Avoids usage-based cloud model charges
- Allows testing of model-specific behaviors
- Could extend prompt-injection and response-validation testing

## Tradeoffs

- Additional setup and maintenance
- Hardware limitations
- Model quality varies
- Introduces another attack surface
- Requires model lifecycle decisions
- Could distract from the security architecture objective

## Architecture Decision

A local LLM is optional.

I would add it only if I wanted to test a security question that cannot be evaluated with the existing control prototype.

# Option 3: Internal Enterprise Deployment

## Description

An enterprise implementation could host the assistant within organization-controlled infrastructure while integrating enterprise identity, approved repositories, monitoring, governance, and review workflows.

The actual model could be internally hosted or provided through an approved managed service.

## Possible Components

- Enterprise identity provider
- Application platform
- Approved document repositories
- Authorization service
- Retrieval service
- Search or vector platform
- Approved model endpoint
- Enterprise logging or SIEM
- Human-review workflow
- Governance and approval processes

## Advantages

- Strong integration with enterprise IAM
- Greater control over data flows
- Integration with existing monitoring
- Potentially strong fit for regulated environments
- Can preserve existing document authorization

## Tradeoffs

- Greater operational complexity
- Platform support requirements
- Security engineering requirements
- Monitoring and lifecycle responsibilities
- Potential infrastructure cost
- May still introduce third-party model dependencies

## Architecture Decision

This approach becomes appropriate when there is a real enterprise use case, organizational ownership, and sufficient operational maturity.

# Option 4: AWS Bedrock Reference Design

## Description

AWS Bedrock represents one possible managed-model architecture for an AWS-centered enterprise environment.

The project contains AWS material as a **reference design only**. No Bedrock environment was deployed for this project.

## Possible Components

Depending on requirements, an AWS implementation could evaluate:

- Amazon Bedrock
- Amazon S3
- AWS IAM / IAM Identity Center
- AWS KMS
- AWS CloudTrail
- Amazon CloudWatch
- AWS Lambda
- A suitable retrieval or search service
- AWS Budgets and cost monitoring

The exact service selection should follow the architecture requirements rather than treating every possible AWS service as mandatory.

## Security Considerations

An implementation would need decisions around:

- Identity and least privilege
- Document authorization
- Encryption
- Network architecture
- Model/provider data handling
- Logging
- Retrieval security
- Incident response
- Regional requirements
- Cost monitoring
- Teardown

## Architecture Decision

AWS Bedrock is useful as an AWS reference architecture but is not required to demonstrate the current security design.

Cloud deployment should occur only when it provides additional business or technical value.

# Option 5: Azure OpenAI Reference Design

## Description

Azure OpenAI represents a possible architecture for organizations already centered on Microsoft identity, security, and cloud services.

The project treats this as a **reference design only**. Azure OpenAI was not deployed as part of the project.

## Possible Components

Depending on requirements, an Azure implementation could evaluate:

- Azure OpenAI
- Microsoft Entra ID
- Azure AI Search
- Azure Storage
- Azure Key Vault
- Azure Monitor
- Log Analytics
- Microsoft Sentinel
- Azure Policy
- Azure Cost Management

Again, these are possible services rather than a required bill of materials.

## Security Considerations

An implementation would need decisions around:

- Entra ID authorization
- Conditional Access
- Managed identities and secrets
- Private versus public connectivity
- Document authorization
- Provider data handling
- Logging and retention
- Incident response
- Cost management
- Human review

## Architecture Decision

Azure OpenAI could be appropriate for a Microsoft-centered enterprise environment but is not required for the current project.

# Option 6: External AI API

## Description

Another design could call an external AI API directly from the application.

This creates an explicit external trust boundary because approved prompt and context information leave the organization's application environment.

## Security Considerations

Before using an external API, I would evaluate:

- Provider security
- Data retention
- Data usage and training terms
- Authentication method
- Secret management
- Data minimization
- Regional processing requirements
- Contractual requirements
- Logging
- Availability
- Usage limits
- Cost controls
- Incident-response responsibilities

## Advantages

- Lower infrastructure burden
- Rapid access to model capability
- Flexible application integration

## Tradeoffs

- External data transfer
- Vendor dependency
- Usage-based cost
- Secret or credential management
- Contract and provider review
- Reduced infrastructure control

## Architecture Decision

The decision should be based on approved data handling and business need, not simply ease of integration.

# Option 7: Private Model Hosting

## Description

An organization could host its own model on internal or privately controlled infrastructure.

## Possible Components

- Private compute
- Model runtime
- Model artifact repository
- Retrieval platform
- Enterprise IAM
- Logging and monitoring
- Model lifecycle management
- Vulnerability and patch management
- Capacity management

## Advantages

- Greater infrastructure control
- Reduced dependency on external inference APIs
- Potential support for strict data-residency requirements
- Greater customization

## Tradeoffs

- High infrastructure complexity
- Compute expense
- Specialized engineering requirements
- Model lifecycle responsibility
- Patching and vulnerability management
- Capacity and availability engineering

## Architecture Decision

Private hosting should not be selected merely because it appears more secure.

The additional operational responsibility can itself create risk.

It is appropriate only when requirements justify the complexity and the organization has the capability to operate it securely.

# Option 8: SaaS AI or Enterprise Search Platform

## Description

An organization may choose to purchase an AI assistant, enterprise search platform, or AI-enabled knowledge product instead of building one.

## Security Considerations

Important evaluation areas include:

- Enterprise SSO
- MFA
- Connector permissions
- Document-level authorization
- Data retention
- Model/provider data usage
- Administrative roles
- Logging and audit evidence
- Data residency
- Incident response
- Contractual requirements
- Exit strategy

## Advantages

- Faster adoption
- Lower infrastructure burden
- Vendor-managed platform
- Potential integration with existing productivity tools

## Tradeoffs

- Vendor dependency
- Connector permission complexity
- Potentially opaque retrieval behavior
- Licensing cost
- Reduced platform control
- Audit evidence dependent on vendor capabilities

## Architecture Decision

This should be evaluated as a buy-versus-build decision rather than automatically considered less secure or more secure than a custom platform.

# Deployment Decision Criteria

Rather than choosing a platform first, I would evaluate each option against the same architecture questions.

| Decision Area | Question |
| --- | --- |
| Business | What problem requires this deployment? |
| Data | What information will the system access? |
| Identity | How is user identity established? |
| Authorization | Where is document access enforced? |
| Retrieval | How is unauthorized content excluded? |
| Model | What information reaches the model? |
| Provider | What external parties process the information? |
| Monitoring | What evidence is generated? |
| Human Review | Which consequences require human accountability? |
| Resilience | What happens if the model or provider is unavailable? |
| Incident Response | Can an AI-related event be reconstructed? |
| Cost | What creates ongoing charges? |
| Exit | Can the deployment be disabled or removed safely? |

# Cloud Deployment Gate

Before deploying a cloud or external AI implementation, I would expect answers to questions such as:

- What objective cannot be satisfied by the current local approach?
- What services are required?
- What data will leave the current trust boundary?
- Has that data been classified?
- Who owns the deployment?
- How will users authenticate?
- Where will authorization be enforced?
- How will documents be governed?
- How will secrets and encryption keys be protected?
- What will be logged?
- What information must not be logged?
- What security events generate alerts?
- What human-review process is required?
- What provider obligations exist?
- What is the expected cost?
- What is the maximum acceptable spend?
- Who receives cost alerts?
- Which resources continue billing when idle?
- What is the teardown process?
- How quickly can the service be disabled?

# Cost Considerations

The current project deliberately avoids services that would create unnecessary recurring cost.

A production design might legitimately require services such as:

- Managed AI inference
- Search or vector infrastructure
- Long-running compute
- Kubernetes
- NAT or private connectivity
- Databases
- GPU infrastructure
- Large-scale logging
- Multi-region or highly available infrastructure

These services are not inherently bad architecture.

The question is whether their business and technical value justify their security, operational, and financial cost.

For early validation, local files, Python, synthetic data, and local logs were sufficient.

# Future Options

The current project does not require another deployment phase to be considered complete as an architecture case study.

Possible future extensions include:

- Execute additional security test scenarios
- Add automated tests
- Improve retrieval behavior
- Improve prompt-risk evaluation
- Introduce a local LLM for model-specific security testing
- Evaluate semantic retrieval
- Build a true human-review gate
- Expand AWS or Azure reference architectures
- Conduct a controlled cloud pilot if there is a specific reason to do so

These are possible extensions rather than unfinished requirements.

# Deployment Recommendation

For this project, the path taken was:

**Architecture and Governance → Local Security-Control Prototype → Selected Control Validation**

That is currently sufficient for the project's objective.

A future deployment decision should be driven by the next question that needs to be answered.

If model behavior needs to be tested, a local LLM may be appropriate.

If cloud IAM, managed-model controls, private networking, provider integration, or enterprise-scale monitoring needs to be evaluated, a controlled cloud implementation may be appropriate.

If neither adds meaningful evidence, there is no architectural reason to deploy additional infrastructure.

## Final Principle

The deployment platform is an implementation choice.

The security architecture should survive that choice.

Whether the model eventually runs locally, internally, in AWS, in Azure, through an external API, or inside a SaaS platform, the same fundamental questions remain:

**Who is the user? What are they authorized to know? What information may the AI access? Where is that authorization enforced? What happens when something fails? What evidence proves the controls worked?**

Those questions should drive the deployment decision.
