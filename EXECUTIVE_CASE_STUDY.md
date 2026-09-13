# Executive Case Study — AI Security Governance & RAG Risk Architecture

## Executive Summary

An internal AI assistant can make enterprise information easier to access, but it can also create a new route around controls the organization already depends on.

For this scenario, I approached the problem from a security architecture perspective rather than starting with the AI platform.

The question I wanted to answer was:

> What is the AI allowed to know, what is the user allowed to know, and where is that decision actually enforced?

I designed an architecture in which identity, authorization, data governance, risk ownership, and business approval remain outside the AI model. I then built a small local prototype to validate selected security decisions before introducing a production LLM, vector database, or cloud AI platform.

The result was an architecture that treats AI as another component within enterprise security boundaries rather than as a new security authority.

---

## Business Problem

A regulated organization wants employees to use an internal AI assistant to find and understand approved company information.

The business benefit is straightforward:

- Faster access to internal knowledge
- Less time searching across documents
- More consistent access to approved guidance
- Better employee productivity

The risk is that the AI assistant could unintentionally create a new information-access path.

A user might ask a question they are allowed to ask while the retrieval system finds a document they are not allowed to see.

A malicious prompt might attempt to override instructions.

A retrieved document itself could contain malicious instructions.

Sensitive information could be exposed to a model provider.

An AI-generated recommendation could also be mistaken for an approved business or security decision.

The architecture therefore had to preserve existing enterprise accountability while still allowing AI to provide useful assistance.

---

## My Approach

I separated the problem into four questions:

### 1. Who is making the request?

Identity must come from a trusted enterprise identity source rather than from anything the user tells the AI.

### 2. What information is the user entitled to access?

Retrieval relevance and authorization are different decisions.

A document can be highly relevant and still be unavailable to the user.

### 3. What information should reach the AI?

Only approved, authorized, and appropriately minimized information should become model context.

### 4. What authority should the AI have?

The AI can assist with information and recommendations, but accountable decisions remain with people and existing enterprise processes.

That produced the core design principle:

> The AI assistant should not create a new path around existing enterprise authorization and data-governance boundaries.

---

## Key Architecture Decisions

### Keep Security Authority Outside the Model

I did not treat the model as the enforcement point for identity, access, business approval, or risk acceptance.

Those controls belong in the surrounding architecture.

If the model ignores an instruction, authorization should still hold.

### Separate Retrieval from Authorization

A traditional search problem asks:

> Which documents best match the question?

A secure enterprise RAG problem also has to ask:

> Which of those documents is this user actually allowed to access?

That distinction became one of the central architecture decisions in the project.

### Treat Retrieved Content as Untrusted

Prompt injection is not limited to what the user types.

Documents entering the AI context can also contain instructions intended to manipulate model behavior.

For that reason, retrieval does not make content trustworthy.

### Separate Administration from Data Entitlement

Someone responsible for operating an AI platform should not automatically gain access to all information available through it.

Platform administration and enterprise data authorization are separate privileges.

### Keep Human Authority Based on Consequence

I did not design human review around a simple rule such as "Restricted information requires approval."

The better question is whether the AI output could cause a consequential decision or action.

Access approvals, security exceptions, production changes, legal decisions, and similar activities may require accountable human authority regardless of how the source document was classified.

---

## Validating the Architecture

I did not want the project to remain entirely conceptual.

Instead of immediately deploying a cloud AI stack, I built a small local Python prototype using synthetic users, roles, groups, documents, metadata, and logs.

The purpose was not to build a production chatbot.

It was to test selected security-control placement.

The simplified flow was:

```text
Mock User
    ↓
Prompt Risk Evaluation
    ↓
Block / Evaluate / Allow
    ↓
Document Retrieval
    ↓
Authorization
    ↓
Security Logging
    ↓
Advisory Response
```

This allowed me to examine whether security decisions happened in the intended sequence without paying for or operating unnecessary cloud infrastructure.

---

## What I Validated

Two initial scenarios were executed and documented.

### Authorized Business Request

A mock General Employee requested an approved synthetic AI acceptable-use policy.

The user was authorized and the request completed.

**Result: Pass**

### Prompt-Injection Attempt

A mock user attempted to override instructions and obtain Restricted documents.

The configured prompt-risk control detected the attempt and blocked the request before retrieval occurred.

**Result: Pass**

Additional security scenarios were documented but intentionally remain marked **Not Yet Tested** until they are actually executed.

That distinction was important to me because architecture documentation should not be presented as implementation evidence.

---

## Failure Paths I Considered

The architecture also considers what happens when controls do not work as expected.

Examples include:

- Unauthorized information is retrieved
- Prompt injection bypasses detection
- Document metadata is incorrect
- A knowledge source contains malicious instructions
- Logging fails
- Sensitive information reaches a provider
- An AI recommendation is treated as an approved decision
- Future agents or tools receive excessive authority

These scenarios influenced where I placed authorization, logging, review, and incident-response responsibilities.

---

## Governance and Compliance

I mapped the architecture to relevant concepts from:

- NIST AI Risk Management Framework
- NIST SP 800-53
- ISO/IEC 27001
- ISO/IEC 42001
- OWASP LLM security risks

The purpose was not to claim certification or compliance.

The mappings were used to test whether the architecture addressed familiar governance and security responsibilities as AI was introduced into the environment.

One of the conclusions was that many AI risks are new expressions of familiar architecture problems.

Unauthorized RAG retrieval is still an access-control problem.

Sensitive model context is still a data-protection problem.

AI provider exposure is still third-party risk.

AI-generated production recommendations still require change control and accountable authority.

---

## Cloud Strategy

I also created AWS Bedrock and Azure OpenAI reference architectures.

Neither environment was deployed.

The purpose was to determine whether the security architecture remained valid when implementation technology changed.

That reinforced an important design principle:

> Standardize the security outcome, not necessarily the cloud implementation.

Identity, authorization, information governance, logging, and human accountability should survive a change in AI provider.

---

## Incident Response

I extended the architecture into AI-specific incident-response scenarios.

One distinction became particularly important:

> A security event is not automatically an incident.

A prompt-injection attempt that is detected and blocked may demonstrate that the control worked.

A successful bypass that exposes Restricted information is fundamentally different.

The architecture therefore considers actual consequence, control failure, exposure, and business impact when determining escalation.

---

## Tradeoffs

### Local Prototype vs. Cloud Deployment

I chose local validation first.

**Benefit:**  
No cloud cost, simpler testing, and clearer focus on security decisions.

**Tradeoff:**  
The prototype cannot validate production LLM behavior, provider controls, semantic retrieval, enterprise identity, or cloud telemetry.

### Simple Retrieval vs. Production RAG

The prototype uses simple keyword retrieval.

**Benefit:**  
It made authorization behavior easy to observe.

**Tradeoff:**  
It does not demonstrate semantic search, embeddings, or vector-database security.

### Pattern Detection vs. Advanced Prompt Defense

The prototype uses basic pattern matching.

**Benefit:**  
It demonstrates where prompt-risk decisions can occur.

**Tradeoff:**  
It is not sufficient protection against sophisticated or indirect prompt injection.

These limitations are documented rather than hidden.

---

## Business Value

The architecture provides a way to evaluate AI adoption without treating AI security as an entirely separate discipline.

It gives business, security, architecture, IAM, data, compliance, and platform teams a common set of questions:

```text
Who is asking?
What are they allowed to access?
What information reaches the model?
What can the model do?
What evidence is created?
Who remains accountable?
What happens when a control fails?
```

Those questions can be applied before committing to a particular AI platform.

---

## Outcome

The project produced:

- Enterprise AI security architecture
- RAG authorization model
- Data-governance model
- Prompt-injection control design
- Threat model
- AI risk assessment
- Logging and monitoring architecture
- Human-accountability model
- Incident-response playbook
- NIST, ISO, and OWASP mappings
- AWS Bedrock reference architecture
- Azure OpenAI reference architecture
- Local security-control prototype
- Initial control-validation evidence

The project does not claim production readiness.

Its value is demonstrating how I would move from:

```text
Business Need
      ↓
Risk
      ↓
Architecture
      ↓
Controls
      ↓
Failure Paths
      ↓
Evidence
      ↓
Validation
```

before making a production technology decision.

---

## Key Takeaway

The biggest architecture lesson from this project was not about a particular AI service.

It was that AI does not remove existing enterprise security responsibilities.

It changes where those responsibilities have to be enforced.

The model can help generate an answer.

It should not decide who is allowed to know it.
