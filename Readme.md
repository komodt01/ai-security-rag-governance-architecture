# AI Security Governance and RAG Risk Architecture for Regulated Environments

## Project Overview

This project demonstrates how a regulated organization can design, govern, and secure an internal AI assistant that uses Retrieval-Augmented Generation (RAG) to answer employee questions from approved internal documents.

The project is intentionally designed as a **local-first, documentation-led security architecture project**. It does not require paid cloud services, AWS Bedrock, Azure OpenAI, SageMaker, OpenSearch, or any long-running infrastructure.

The purpose is to show how a security architect would evaluate and design AI-enabled workflows with proper governance, access control, auditability, data protection, and risk management.

## Business Problem

Organizations are increasingly adopting AI assistants to improve employee productivity, reduce manual research time, and accelerate access to internal knowledge. However, AI systems introduce new risks, including:

- Prompt injection
- Sensitive data disclosure
- Unauthorized access to internal documents
- Overreliance on AI-generated answers
- Inaccurate or hallucinated responses
- Lack of auditability
- Unclear ownership of AI outputs
- Vendor and model supply chain risk
- Weak governance around approved use cases

For regulated environments such as financial services, healthcare, insurance, and government-adjacent organizations, these risks must be addressed before AI tools are broadly adopted.

## Project Objective

The objective of this project is to design a secure, governed AI assistant architecture that allows employees to query approved internal knowledge while enforcing security, privacy, compliance, and operational controls.

This project focuses on architecture and governance rather than model training.

## Scope

This project covers:

- AI assistant reference architecture
- RAG data flow design
- Trust boundary analysis
- Data classification requirements
- Role-based access control model
- Prompt injection control strategy
- Logging and monitoring requirements
- Human review and escalation process
- AI incident response considerations
- Compliance mapping
- Local prototype planning
- Cloud deployment reference designs without actual deployment

## Out of Scope

The following are intentionally out of scope for the initial phase:

- Training a custom machine learning model
- Fine-tuning a large language model
- Deploying AWS Bedrock, SageMaker, OpenSearch, Kendra, or Azure OpenAI
- Storing real company data
- Processing confidential, personal, regulated, or production data
- Building a production AI system

## Architecture Approach

This project uses a layered security architecture:

1. Business Use Case Review
2. Data Classification
3. Identity and Access Control
4. Approved Document Ingestion
5. Retrieval Layer Controls
6. Prompt and Response Filtering
7. Human Review
8. Logging and Monitoring
9. Incident Response
10. Compliance and Governance Mapping

## Key Risks Addressed

| Risk Area | Description | Control Theme |
|---|---|---|
| Prompt Injection | User attempts to override system instructions or extract restricted data | Input filtering, retrieval constraints, system prompt hardening |
| Sensitive Data Disclosure | AI returns confidential, regulated, or unauthorized information | Data classification, access control, response review |
| Unauthorized Access | User retrieves documents they should not access | RBAC, document-level permissions, identity-aware retrieval |
| Hallucination | AI produces unsupported or inaccurate output | Source citation, confidence thresholds, human review |
| Overreliance | Employees treat AI output as final authority | Disclaimers, approval workflow, escalation paths |
| Audit Gaps | Organization cannot reconstruct AI activity | Prompt/response logging, user attribution, monitoring |
| Vendor Risk | AI provider or model introduces third-party risk | Vendor assessment, data handling review, contractual controls |

## Repository Structure

```text
ai-security-rag-governance-architecture/
├── README.md
├── business_case.md
├── cost_controls.md
├── lessonslearned.md
├── architecture/
│   ├── reference_architecture.md
│   ├── data_flow.md
│   ├── trust_boundaries.md
│   └── deployment_options.md
├── governance/
│   ├── ai_use_case_intake.md
│   ├── ai_risk_assessment.md
│   ├── data_classification.md
│   └── human_review_requirements.md
├── security/
│   ├── threat_model_stride.md
│   ├── owasp_llm_top10_mapping.md
│   ├── prompt_injection_controls.md
│   ├── access_control_model.md
│   └── logging_monitoring.md
├── compliance/
│   ├── nist_ai_rmf_mapping.md
│   ├── nist_800_53_mapping.md
│   └── iso_27001_mapping.md
├── incident_response/
│   └── ai_incident_response_playbook.md
├── local_prototype/
│   └── README.md
└── cloud_reference_only/
    ├── aws_bedrock_design_only.md
    └── azure_openai_design_only.md

## Additional Compliance Update

ISO/IEC 42001 was added after the initial documentation phase to strengthen the AI governance and AI management system alignment of this project.

Added file:

- `compliance/iso_42001_mapping.md` — Maps the project to ISO/IEC 42001 AI Management System concepts, including AI governance, risk assessment, human oversight, data governance, monitoring, incident response, supplier review, and continual improvement.
