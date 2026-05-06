# Cost Controls

## Purpose

This project is designed to demonstrate AI security architecture without creating unexpected cloud costs.

The initial phases are documentation-first and local-first. No paid cloud services are required.

## Cost Control Principle

The project follows this rule:

> Architecture first. Local prototype second. Cloud deployment last, and only after cost controls, budgets, alerts, and teardown steps are in place.

## Phase 1: Documentation-Only

Estimated cost: $0

Phase 1 includes:

- Architecture documentation
- Threat modeling
- Governance templates
- Compliance mappings
- Logging and monitoring design
- Incident response playbook
- Cloud reference architecture only

No cloud resources are deployed.

## Phase 2: Local Prototype

Estimated cost: $0, assuming existing local hardware

Possible tools:

- Python
- Streamlit
- ChromaDB or FAISS
- Local markdown documents
- Ollama or another local model runtime

No external AI API is required.

## Phase 3: Cloud Reference Design Only

Estimated cost: $0 unless explicitly deployed

Cloud documents may describe:

- AWS Bedrock design
- Azure OpenAI design
- Identity and access control patterns
- Logging and monitoring patterns
- Cost-control requirements

These are design artifacts only.

## Do Not Deploy Without Controls

No cloud deployment should occur unless the following are completed first:

- Budget alert configured
- Billing alarm configured
- Region selected and documented
- Resource tagging strategy defined
- Teardown process written and tested
- Estimated monthly cost documented
- Maximum spend threshold defined
- Owner identified
- Deployment duration defined
- Services reviewed for minimum charges or always-on costs

## AWS Cost Controls Required Before Any AWS Deployment

Before deploying any AWS resources, the following must be in place:

- AWS Budget with email alert
- CloudWatch billing alarm if supported in the account
- Resource tags:
  - Project
  - Owner
  - Environment
  - CostCenter
  - ExpirationDate
- Terraform destroy instructions
- Manual cleanup checklist
- Service quota review
- Daily cost check during testing

## High-Risk AWS Services to Avoid in Early Phases

Avoid using these services in early project phases unless cost is fully understood:

- Amazon SageMaker
- Amazon OpenSearch Service
- Amazon Kendra
- Long-running EC2 instances
- NAT Gateway
- Multi-AZ databases
- Provisioned throughput resources
- Large-scale logging ingestion
- Large S3 datasets
- Managed Kubernetes clusters
- Always-on endpoints
- GPU-backed services

## Safer Alternatives

Use these instead during early project phases:

| Need | Safer Local Option |
|---|---|
| AI model interaction | Local LLM via Ollama |
| Vector database | ChromaDB or FAISS |
| Web interface | Streamlit |
| Documents | Local markdown files |
| Logging | Local JSON or CSV logs |
| Access control demo | Mock user roles |
| Security testing | Local prompt injection test cases |
| Architecture design | Markdown and diagrams |

## Cloud Deployment Decision Gate

Before any cloud deployment, answer these questions:

1. What business or learning objective requires cloud deployment?
2. Can the same objective be demonstrated locally?
3. What is the estimated hourly and monthly cost?
4. What services can continue billing after testing?
5. What is the teardown process?
6. Who receives budget alerts?
7. What is the maximum acceptable spend?
8. How long will the environment remain active?
9. What data will be used?
10. What compliance or privacy concerns exist?

## Final Cost Statement

This project is intentionally structured to provide portfolio value without exposing the owner to unnecessary cloud costs.

Cloud deployment is optional and should only occur after explicit cost review and approval.
