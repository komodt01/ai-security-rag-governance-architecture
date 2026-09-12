# Cost Controls

## Purpose

This project demonstrates AI security architecture while avoiding unnecessary cloud cost.

The architecture work is documentation-first, and the implemented security-control prototype is local-first. No paid cloud services are required for the current project.

## Cost Control Principle

The project follows this rule:

> Architecture first. Local validation second. Cloud deployment only when it provides additional value and appropriate cost controls are in place.

The purpose of a cloud deployment should be established before resources are provisioned. If the same architecture or security objective can be demonstrated locally, cloud deployment is not required.

## Phase 1: Documentation and Architecture

**Estimated cost: $0**

Phase 1 includes:

- Business case
- Reference architecture
- Data flow and trust boundaries
- Threat modeling
- Governance artifacts
- Compliance mappings
- Access-control design
- Logging and monitoring design
- Incident-response planning
- AWS and Azure design-only reference architectures

No cloud resources are required for this phase.

## Phase 2: Local Security Prototype

**Estimated cost: $0, assuming existing local hardware**

The implemented prototype uses:

- Python
- Synthetic markdown documents
- Mock users and roles
- Local JSON metadata
- Local JSONL logs
- Pattern-based prompt-risk detection
- Metadata-based authorization
- Keyword-based document retrieval

The prototype does not require:

- External AI APIs
- Cloud services
- Vector databases
- Production identity systems
- Local or hosted LLMs

The prototype is intentionally limited to validating selected security-control concepts rather than reproducing a production AI/RAG platform.

## Cloud Reference Designs

**Estimated cost: $0 unless explicitly deployed**

The project includes design-only cloud reference material that may describe:

- AWS Bedrock
- Azure OpenAI
- Cloud identity and access patterns
- Logging and monitoring patterns
- Network and data-protection controls
- Cost-control requirements

These are architecture artifacts only. They do not represent deployed cloud environments.

## Cloud Deployment Decision Gate

Before deploying any cloud resources, answer:

1. What business, architecture, or learning objective requires cloud deployment?
2. Can the same objective be demonstrated locally?
3. What services will be provisioned?
4. What is the estimated hourly and monthly cost?
5. Which resources can continue billing after testing ends?
6. What is the teardown process?
7. Who owns the environment?
8. Who receives budget or billing alerts?
9. What is the maximum acceptable spend?
10. How long will the environment remain active?
11. What data will be used?
12. What security, privacy, or compliance requirements apply?

If those questions cannot be answered, deployment should not proceed.

## Cost Controls Required Before Cloud Deployment

Before a cloud environment is created, the project should define:

- Budget and billing alerts
- Maximum spend threshold
- Resource ownership
- Approved deployment region
- Resource tagging or labeling strategy
- Expected deployment duration
- Estimated cost
- Teardown procedure
- Manual cleanup checklist
- Services that may continue billing after use
- Data-handling restrictions

The exact implementation will depend on the selected cloud provider.

## AWS Cost Controls

If an AWS implementation is later created, appropriate controls should include:

- AWS Budget with notification thresholds
- CloudWatch billing alarm where applicable and supported
- Resource tags such as:
  - Project
  - Owner
  - Environment
  - CostCenter
  - ExpirationDate
- Service quota review
- Cost monitoring during testing
- Infrastructure teardown instructions
- Manual verification that billable resources have been removed

## Higher-Cost Services and Patterns

Some cloud services and architecture patterns deserve additional cost review before being used in a portfolio or prototype environment.

Examples include:

- Amazon SageMaker
- Amazon OpenSearch Service
- Amazon Kendra
- Long-running compute instances
- NAT gateways
- Managed Kubernetes clusters
- Multi-AZ databases
- Provisioned-throughput resources
- Always-on endpoints
- GPU-backed services
- Large-scale logging ingestion
- Large datasets or high-volume storage

The concern is not that these services should never be used. The architecture should justify why they are necessary and understand their billing behavior before deployment.

## Local Alternatives

For early architecture validation, lower-cost local approaches may be sufficient.

| Need | Local Approach |
| --- | --- |
| Security-control logic | Python |
| Documents | Local synthetic markdown files |
| Identity demonstration | Mock users, roles, and groups |
| Authorization | Local metadata and policy logic |
| Prompt-risk testing | Local pattern-based detection |
| Logging | Local JSONL files |
| Security testing | Defined local test scenarios |
| Architecture documentation | Markdown and diagrams |
| Optional AI model interaction | Local LLM such as Ollama |
| Optional vector search | ChromaDB or FAISS |
| Optional web interface | Streamlit |

The optional components are not part of the current implemented prototype.

## Current Project Cost

The documentation and implemented local prototype require no paid cloud services or external AI APIs.

**Estimated current project cost: $0, assuming existing local hardware.**

## Final Cost Principle

Cost is an architecture constraint, not an afterthought.

A cloud implementation should only be introduced when it provides capabilities or validation that cannot reasonably be achieved through the current local approach. Any future deployment should have defined ownership, cost visibility, spending limits, and teardown procedures before resources are created.
