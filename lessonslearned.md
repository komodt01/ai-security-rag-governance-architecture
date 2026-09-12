# Lessons Learned

## Purpose

This document captures the key architecture and implementation lessons from the AI Security Governance and RAG Risk Architecture project.

The project began as a documentation-first security architecture exercise and progressed into a local security-control prototype using synthetic data and no paid cloud services.

The objective was not to build a production chatbot. The objective was to determine how an enterprise AI assistant could improve access to approved organizational knowledge without bypassing existing security, authorization, governance, and accountability requirements.

## 1. AI Security Is an Architecture Problem, Not Just a Model Problem

One of the strongest lessons from this project was that the model is only one component of the system.

Security decisions exist throughout the workflow:

- Identity
- Authorization
- Data classification
- Document governance
- Prompt handling
- Retrieval
- Context assembly
- Model interaction
- Response validation
- Logging and monitoring
- Human review
- Incident response
- Vendor risk
- Cost governance

A secure design cannot rely on the model to protect the surrounding system.

## 2. The Model Is Not the Security Boundary

The model should not determine whether a user is authorized to access enterprise information.

Authorization belongs outside the model.

For this scenario, identity context, document metadata, role or group membership, classification, and access policy determine whether information can be retrieved.

Prompt instructions can influence model behavior, but they are not a substitute for authorization controls.

The local prototype reinforced this principle by making authorization decisions in application logic rather than relying on an AI model.

## 3. RAG Security Starts Before Retrieval

RAG security is not simply a question of finding relevant documents.

Before information is returned, the architecture needs to consider:

- Whether the document is approved
- Who owns it
- Its classification
- Who is authorized to access it
- Whether it is still valid
- Whether additional review is required
- Whether the requesting user should receive it

A technically relevant document is not necessarily an authorized document.

This distinction became especially important when designing the local metadata and authorization logic.

## 4. Document Governance Is Part of the Security Boundary

Source documents can be stale, misclassified, poisoned, overly permissive, or inappropriate for AI use.

Documents therefore need governance such as:

- Classification
- Ownership
- Approval status
- Authorized roles or groups
- Review dates
- Expiration or lifecycle information
- Change management
- Defined onboarding and removal processes

Embeddings and indexes used by a production RAG system would also need to be protected according to the sensitivity of the underlying information.

## 5. Prompt Injection Requires Defense in Depth

Prompt injection cannot be solved by a stronger system prompt.

Controls may be needed at several points:

- Input evaluation
- Identity and role validation
- Document authorization
- Retrieval restrictions
- Context isolation
- Response validation
- Logging and monitoring
- Human review
- Security testing

The local prototype implemented basic pattern-based prompt injection detection and demonstrated that a detected injection attempt could be blocked before document retrieval.

That validation also showed the limitation of simple pattern matching. Production controls would need to account for indirect attacks, obfuscation, context manipulation, and techniques that do not match known patterns.

## 6. Authorization Should Happen Before Sensitive Information Reaches the Model

One architectural decision became especially important:

> Do not retrieve protected information first and expect the model to decide whether the user should see it.

The retrieval and authorization layers should prevent unauthorized information from entering the model context whenever practical.

This reduces the chance of unauthorized information being exposed through responses, logs, debugging data, or unexpected model behavior.

## 7. Data Classification Must Influence System Behavior

Classification should not exist only as a label.

It should influence decisions such as:

- Whether information can be included in the AI knowledge base
- Who can retrieve it
- Whether additional controls are required
- Whether it can be sent to an external provider
- Whether human review is appropriate
- How related logs should be protected

The local prototype uses classification as part of document metadata, although a production implementation would require more mature lifecycle and policy enforcement.

## 8. Human Review Depends on Consequence

Not every AI response needs human approval.

The important question is what happens if the response is wrong or acted upon.

Higher-impact scenarios may include:

- Security exceptions
- Privileged-access decisions
- Legal or regulatory interpretation
- Audit conclusions
- Significant incident-response decisions
- Production changes
- Customer-impacting actions

The prototype includes simulated human-review triggers. It does not implement a production approval workflow or prevent response generation while waiting for approval.

That distinction is important: identifying the need for review is not the same as implementing the review process.

## 9. Logging Must Balance Evidence With Data Minimization

AI systems create new logging questions because prompts, retrieved documents, responses, and review notes can themselves contain sensitive information.

Useful evidence may include:

- User identity
- Timestamp
- Correlation ID
- Prompt-risk classification
- Retrieved document IDs
- Access decisions
- Policy actions
- Security alerts
- Human-review events

The local prototype uses JSONL logs to demonstrate this type of evidence.

A production design would still need decisions around log access, retention, masking, monitoring, and whether full prompt or response content should be retained at all.

## 10. AI Incident Response Requires AI-Specific Evidence

Traditional infrastructure and application logs may not be enough to reconstruct an AI-related incident.

An investigation may need to determine:

- Who submitted the request
- What was requested
- What documents were considered or retrieved
- What authorization decisions occurred
- What context reached the model
- What response was generated
- Whether security controls fired
- Whether human review occurred
- What the user ultimately received

This evidence needs to be considered during architecture design rather than after an incident occurs.

## 11. Local Prototypes Can Validate Architecture Decisions

One of the most useful lessons from Phase 2 was that meaningful architecture validation does not necessarily require a production AI platform.

The local Python prototype was sufficient to exercise selected concepts involving:

- Mock identity and roles
- Document metadata
- Role- and group-based authorization
- Prompt-risk evaluation
- Basic prompt injection detection
- Sensitive-data pattern detection
- Retrieval decisions
- Local logging
- Security alerts
- Simulated human-review triggers
- Advisory responses

The prototype intentionally does not include an LLM, embeddings, vector database, production identity provider, or cloud AI service.

That limitation does not prevent it from validating selected security-control sequencing and architecture decisions.

## 12. Testing Changed the Value of the Project

Writing architecture documentation established the design.

Running the prototype provided a different kind of evidence.

The initial validation demonstrated two behaviors:

1. An authorized General Employee could retrieve the approved mock AI policy.
2. A prompt injection attempt could be detected and blocked before document retrieval.

Those tests do not validate every control in the architecture.

Additional prompt injection, access-control, and sensitive-data scenarios remain defined but untested.

The important lesson was that implementation and execution can expose assumptions that documentation alone does not.

## 13. Cost Governance Is an Architecture Concern

Cloud cost is not separate from architecture.

A prototype can create unnecessary operational and financial exposure if services are deployed before their purpose, billing behavior, ownership, and teardown process are understood.

For this project, I chose a local-first approach because the initial security questions could be explored without paid cloud infrastructure.

Before a future cloud implementation, I would want to establish:

- Why cloud deployment is required
- Expected cost
- Budget thresholds and alerts
- Ownership
- Deployment duration
- Resource tagging
- Teardown procedures
- Data-handling requirements

Cloud should solve a problem the local approach cannot, rather than simply make the project appear more sophisticated.

## 14. AI Governance Starts With the Business Problem

AI architecture should not begin with selecting an LLM, vector database, or cloud service.

For this scenario, the starting problem was:

> A regulated organization wants to improve employee access to approved knowledge without creating a new path around existing authorization, data-governance, security, and accountability boundaries.

That business problem drove the security requirements.

AI use-case intake should therefore establish:

- What problem is being solved
- Who will use the system
- What data is involved
- What decisions the AI may influence
- What happens if the AI is wrong
- Who owns the use case
- What controls are required
- What evidence is required
- Who accepts the remaining risk

## 15. Traditional Security Architecture Still Matters

AI introduces new attack patterns and governance questions, but many foundational controls remain familiar.

The project mapped the architecture against:

- NIST AI RMF
- NIST 800-53
- ISO 27001
- OWASP LLM Top 10
- STRIDE

The exercise reinforced that identity, least privilege, data protection, logging, incident response, supplier risk, configuration management, governance, and secure development remain relevant.

AI changes the system being protected. It does not eliminate established security principles.

## 16. Advisory Language Is Part of the Control Design

Users can place too much confidence in an AI-generated response.

For that reason, response design should avoid implying authority the system does not have.

Examples include:

- “Based on approved source material...”
- “This response is advisory and does not constitute approval.”
- “This should be reviewed by the appropriate control owner.”
- “Please follow the approved exception process.”

Language does not replace technical controls, but it can help establish appropriate expectations and preserve human accountability.

## What Went Well

The strongest part of the project was the progression from business problem to architecture and then to limited implementation evidence.

The project now includes:

- Business case and architecture requirements
- Reference architecture
- Data-flow and trust-boundary analysis
- Threat modeling
- AI governance artifacts
- Access-control design
- Data-classification design
- Prompt injection controls
- Logging and monitoring requirements
- Human-review requirements
- Incident-response planning
- Security and compliance mappings
- Cloud design-only references
- Cost-control strategy
- Working local security-control prototype
- Defined security test scenarios
- Documented initial validation results

## What I Would Improve Next

The current project is sufficient to demonstrate the architecture approach and selected control implementation.

If I continued the prototype, the highest-value improvements would be:

- Execute additional defined security test scenarios
- Add automated tests
- Improve prompt-risk detection beyond simple pattern matching
- Improve retrieval behavior
- Test additional authorization and denial paths
- Exercise sensitive-data scenarios
- Add log-analysis examples
- Evaluate a true human-review approval gate
- Evaluate semantic retrieval only if it adds value to the security testing

A local LLM, vector database, Streamlit interface, or cloud deployment would be optional extensions rather than requirements for demonstrating the current architecture.

## Interview Talking Point

I would describe the project this way:

> I designed a secure AI/RAG architecture for a regulated environment, starting with the business problem and governance requirements rather than the model. I focused on identity, document-level authorization, data classification, prompt injection, retrieval controls, logging, human review, incident response, and compliance. I then built a limited local Python prototype to validate selected controls, including an authorized retrieval path and a prompt injection attempt that was blocked before retrieval. The prototype intentionally uses synthetic data and no paid cloud services.

The main architectural principle is:

> The model is not the security boundary.

## Final Reflection

The most important lesson from this project is that responsible enterprise AI adoption requires architecture around the model.

A secure AI assistant needs identity, authorization, data governance, retrieval controls, monitoring, accountability, and incident-response capability just like other enterprise systems, while also addressing AI-specific risks.

For this scenario, the progression that made the most sense was:

**Business problem → governance → architecture → threat analysis → control design → local validation → additional testing → cloud implementation only when justified.**

The local prototype does not prove the entire production architecture. It does provide evidence that selected architecture decisions can be translated into working control logic and tested before committing to a production AI platform.
