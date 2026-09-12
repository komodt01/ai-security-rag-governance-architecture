# AI Risk Assessment

## Purpose

This document defines the risk-assessment approach for the secure enterprise AI assistant architecture.

The objective is to determine:

- What business problem is being solved
- What information the AI system may access
- Who may use it
- What the AI output may influence
- What could fail
- What controls are required
- Who owns the resulting risk
- What evidence would exist if something goes wrong
- Whether the use case should proceed, be constrained, be redesigned, or be rejected

The assessment is intended for enterprise and regulated environments where AI may interact with internal information, security standards, compliance guidance, operational procedures, identity information, or business workflows.

# Core Principle

> AI risk should be evaluated in terms of business consequence, exposure, control effectiveness, and accountability—not simply whether the model produces a useful answer.

A technically functional AI system can still create unacceptable enterprise risk.

# Relationship to AI Use-Case Intake

The governance intake asks whether the use case makes sense and what must be understood before implementation.

This risk assessment goes further by examining:

- Threats
- Exposure
- Business impact
- Control requirements
- Residual risk
- Ownership
- Decision authority

The two documents are complementary rather than duplicate approval forms.

# Assessment Questions

Before implementation, I would want to understand:

1. What problem is being solved?
2. Why is AI appropriate?
3. What information will the system access?
4. Who will use it?
5. How will identity and authorization work?
6. What can the system retrieve?
7. What can the AI output influence?
8. Can it take actions?
9. What happens when the AI is wrong?
10. What happens when a user is malicious?
11. What happens when retrieved content is malicious?
12. What happens when a dependency fails?
13. What information leaves the enterprise boundary?
14. What evidence is retained?
15. Who owns each significant risk?
16. Who has authority to accept residual risk?

# Decision Outcomes

Possible outcomes include:

| Decision | Meaning |
| --- | --- |
| Proceed | Risk is acceptable with normal controls |
| Proceed with Conditions | Specific controls or restrictions are required |
| Limited Validation | Use synthetic or low-risk information to validate selected behavior |
| Redesign | Architecture must change before proceeding |
| Escalate | Additional accountable stakeholders must review |
| Defer | More information is required |
| Reject | Risk cannot be reduced to an acceptable level |

The appropriate decision depends on the organization and use case.

# Risk Assessment Method

This project uses **qualitative risk judgment** rather than an additive numeric scoring formula.

The assessment considers:

- Likelihood
- Impact
- Exposure
- Business consequence
- Existing controls
- Required controls
- Residual risk
- Risk ownership

Ratings such as Low, Medium, High, or Critical can help communicate relative concern, but they should not replace architectural judgment.

## Why the Ratings Are Not Added Together

Different risk domains are not necessarily equivalent.

For example:

- Regulated-data exposure may independently require privacy and legal review.
- Production action authority may independently require stronger controls.
- A low-cost deployment does not offset weak authorization.
- Local hosting does not eliminate prompt or data risk.
- Strong authentication does not eliminate unsafe model behavior.

Therefore, this assessment does not calculate an overall risk rating by simply adding domain scores.

# Risk Rating Guidance

| Rating | General Meaning |
| --- | --- |
| Low | Limited consequence and exposure; standard controls generally sufficient |
| Medium | Meaningful risk requiring documented controls and ownership |
| High | Significant business or security consequence requiring stronger architecture and governance |
| Critical | Potentially unacceptable consequence or exposure requiring escalation, redesign, or avoidance |

The rating should reflect the specific scenario rather than an automatic classification rule.

# Risk Domains

The architecture evaluates risk across several connected domains:

- Business and Decision Risk
- Data Risk
- Identity and Access Risk
- Prompt and Retrieval Risk
- Model and Output Risk
- Vendor and Supply-Chain Risk
- Operational and Resilience Risk
- Logging and Evidence Risk
- Compliance, Privacy, and Governance Risk
- Agent or Tool-Use Risk where applicable

Not every use case will require the same depth in every domain.

# 1. Business and Decision Risk

The first question is not whether the AI can generate an answer.

The first question is:

> What happens if someone relies on that answer?

## Questions

- Is the system informational or decision-supporting?
- Could output affect security?
- Could output affect customers?
- Could output affect financial activity?
- Could output influence production systems?
- Could output influence access decisions?
- Could output influence legal or compliance conclusions?
- Is the AI being treated as advisory or authoritative?
- Who remains accountable?

## Examples

| Use | Relative Concern |
| --- | --- |
| Finding an approved policy | Lower |
| Summarizing internal guidance | Lower to Moderate |
| Recommending a security architecture decision | Moderate to High |
| Recommending a security exception | High |
| Approving privileged access | Critical |
| Making a customer-impacting decision | High to Critical |
| Making a final legal or regulatory determination | Critical |

The exact rating depends on consequence and control design.

# 2. Data Risk

AI systems may expose information through:

- Prompts
- Retrieval
- Context
- Responses
- Logs
- Embeddings
- External providers
- Administrative access

## Questions

- What classifications are involved?
- Is the information real or synthetic?
- Is regulated information involved?
- Are secrets possible?
- Can users enter protected information?
- Is data sent outside the organization?
- Is data retained?
- Is data used for training?
- Can logs become another sensitive repository?
- Can derived data retain source sensitivity?

## Key Risks

| Risk | Possible Control |
| --- | --- |
| Unauthorized information exposure | Document-level authorization |
| Sensitive prompt entry | Input controls and policy |
| Sensitive response | Response controls |
| Sensitive logs | Minimization and restricted access |
| Unknown document classification | Deny or quarantine |
| Provider retention | Vendor and contractual review |
| Training on enterprise information | Explicit governance decision |
| Secret exposure | Block and incident handling |
| Derived-data exposure | Protect according to source sensitivity |

# 3. Identity and Access Risk

The AI assistant should not create a new path around enterprise authorization.

## Questions

- How is identity established?
- Are roles or groups trusted?
- Are document permissions preserved?
- Can platform administrators see content they do not own?
- Can users request information outside their normal scope?
- What happens when authorization cannot be determined?
- How is stale access removed?
- Can prompt text influence identity?

## Key Risks

| Risk | Possible Control |
| --- | --- |
| Unauthorized user | Trusted enterprise authentication |
| Role impersonation | Ignore prompt identity claims |
| Unauthorized retrieval | Document-level authorization |
| Excess privilege | Least privilege |
| Administrative overreach | Separation of duties |
| Stale entitlement | Identity lifecycle |
| Unknown authorization | Deny by default |

The local prototype validates selected role/group and document-metadata behavior using synthetic identities.

It does not implement enterprise IAM.

# 4. Prompt and Retrieval Risk

Natural-language input creates a control surface that traditional applications may not have.

RAG-style architectures also introduce risk because retrieved content can influence downstream behavior.

## Questions

- Can users attempt prompt injection?
- Can users request restricted information?
- Can retrieved documents contain malicious instructions?
- Does relevance ranking occur before authorization?
- Can unauthorized documents enter context?
- Can users broaden retrieval scope?
- Can the system distinguish user instructions from retrieved content?
- Are retrieval decisions observable?

## Key Risks

| Risk | Possible Control |
| --- | --- |
| Direct prompt injection | Input evaluation and containment |
| Privilege claim in prompt | Trusted identity outside prompt |
| Unauthorized retrieval | Permission-aware retrieval |
| Indirect injection | Treat retrieved content as untrusted |
| Excessive retrieval | Scope and metadata controls |
| Retrieval ambiguity | Source and authorization evidence |

Prompt filtering is defense in depth.

It should not replace authorization.

# 5. Model and Output Risk

A production AI model can generate information that is incorrect, incomplete, unsupported, or misleading.

## Questions

- Can the model hallucinate?
- Does the response reflect approved sources?
- Can it expose system instructions?
- Can it reveal protected information?
- Can users mistake advice for approval?
- Can model output trigger another system?
- Can output be used without human judgment?
- What happens when source documents conflict?

## Key Risks

| Risk | Possible Control |
| --- | --- |
| Unsupported response | Source grounding and validation |
| Hallucination | Source-supported answers and review where consequential |
| Sensitive output | Authorization plus response controls |
| Overreliance | Explicit authority boundaries |
| Unsafe recommendation | Consequence-based human review |
| Downstream misuse | Output handling controls |

The current local prototype does not contain a production LLM.

Therefore, it does not validate production hallucination, model leakage, or model-output safety controls.

# 6. Vendor and Supply-Chain Risk

A production implementation may depend on:

- Model providers
- Cloud platforms
- Open-source libraries
- Embedding models
- Vector databases
- Document-processing tools
- Plugins
- APIs
- SaaS services

## Questions

- What data reaches the provider?
- Is it retained?
- Is it used for training?
- Where is it processed?
- What contractual protections exist?
- What happens if the provider changes model behavior?
- What happens if the service is unavailable?
- What dependencies are introduced?
- How are software dependencies governed?

## Possible Controls

- Vendor security review
- Privacy review
- Contract review
- Data-processing restrictions
- Model/provider approval
- Dependency scanning
- Version management
- Provider contingency planning
- Data minimization

The current prototype is local and does not send information to an external AI provider.

# 7. Operational and Resilience Risk

An AI service becomes part of an operational process once users depend on it.

## Questions

- What happens when the service is unavailable?
- Can users return to the authoritative source?
- What happens when a model or provider changes?
- How are source documents updated?
- How are incorrect answers corrected?
- How is the system disabled?
- Who supports it?
- What are the cost dependencies?
- Does the system have a customer or operational SLO?

## Possible Controls

- Source-document fallback
- Defined ownership
- Change management
- Rollback or disablement
- Usage limits
- Cost controls
- Monitoring
- Dependency management
- Resilience planning

A production design should evaluate failure paths rather than assuming AI availability.

# 8. Logging and Evidence Risk

Logging is both a security control and a potential exposure.

## Questions

- What must be recorded?
- Are prompts stored?
- Are responses stored?
- Are document IDs sufficient?
- Could logs contain restricted information?
- Who can read them?
- How long are they retained?
- Can security events be correlated?
- Can investigators reconstruct an authorization decision?

## Useful Evidence

Depending on the use case:

- User identity
- Correlation ID
- Prompt metadata
- Risk classification
- Retrieved document IDs
- Denied document IDs
- Authorization decision
- Security alerts
- Review events
- Administrative changes

Production logging should minimize unnecessary sensitive content.

# 9. Compliance, Privacy, and Governance Risk

AI does not eliminate existing obligations.

## Questions

- Is regulated information involved?
- Is personal information involved?
- Are contractual restrictions involved?
- Could output influence compliance interpretation?
- Is audit evidence involved?
- Are owners identified?
- Are exceptions documented?
- Can decisions be reconstructed?
- Is there a defined acceptable-use policy?

## Possible Controls

- Data-owner approval
- Privacy review
- Legal review
- Compliance review
- Evidence retention
- Exception governance
- Source traceability
- Human accountability
- Control mapping where useful

Framework mappings in this repository are architecture aids.

They do not constitute certification or formal compliance attestation.

# 10. Agent and Tool-Use Risk

The current project does not implement an autonomous agent or tool-execution capability.

If that capability were added, the risk profile would change materially.

Additional questions would include:

- What tools can the AI invoke?
- Under whose identity?
- What permissions are available?
- Can it modify production systems?
- Can it create or approve access?
- Can it initiate transactions?
- Can it communicate externally?
- What actions require human approval?
- Can one tool output become another tool's instruction?
- How is action evidence recorded?

The move from **answering** to **acting** should trigger a new architecture and risk review.

# Threat-to-Control View

| Threat | Potential Impact | Architectural Response |
| --- | --- | --- |
| Prompt injection | Policy bypass or unsafe behavior | Prompt controls plus external authorization |
| Unauthorized retrieval | Confidentiality breach | Document-level authorization |
| Indirect injection | Retrieved content manipulates behavior | Treat retrieved content as untrusted |
| Hallucination | Incorrect decision support | Grounding and consequence-based review |
| Sensitive prompt | Data exposure | Input controls and user policy |
| Sensitive logs | Secondary data exposure | Minimize and protect logs |
| Admin overreach | Unauthorized content access | Separation of duties |
| Provider retention | External data exposure | Vendor and contractual controls |
| Model outage | Business interruption | Fallback and resilience |
| Stale documents | Incorrect guidance | Content lifecycle |
| Excessive agency | Unauthorized action | Least privilege and approval boundaries |
| AI treated as authority | Governance failure | Explicit human accountability |

# Residual Risk

Implementing a control does not make the associated risk disappear.

For each significant risk, I would want to understand:

- Inherent risk
- Controls
- Control limitations
- Residual risk
- Accountable owner
- Decision

Example:

**Risk:** Unauthorized document retrieval

**Controls:**
- Trusted identity
- Document authorization metadata
- Permission-aware retrieval
- Deny by default
- Access logging

**Residual risk:**
- Incorrect metadata
- Stale identity information
- Retrieval implementation defects
- Administrative misconfiguration

**Owner:**
- Appropriate IAM, data, platform, and security owners

The actual ownership model depends on the organization.

# Risk Ownership

Risk should be owned by the party with authority over the affected business outcome.

Possible ownership includes:

| Risk Area | Possible Owner |
| --- | --- |
| Business outcome | Business Owner |
| Data use | Data Owner |
| Identity | IAM Owner |
| Security architecture | Security Architecture |
| Platform operations | Platform Owner |
| Privacy | Privacy |
| Compliance | Compliance |
| Legal interpretation | Legal |
| Vendor dependency | Vendor Risk / Procurement |
| Production operations | Service Owner |

Security architecture can identify and communicate risk without automatically becoming the owner of every risk.

# Risk Treatment

Possible treatment decisions include:

- Accept
- Mitigate
- Avoid
- Transfer where appropriate
- Defer
- Redesign

Acceptance of significant residual risk should come from an accountable owner with appropriate authority.

# Human Accountability

Human review should be based primarily on consequence.

Examples requiring accountable human authority may include:

- Security exceptions
- Risk acceptance
- Privileged-access decisions
- Compliance conclusions
- Legal conclusions
- Production changes
- Incident-response actions
- Customer-impacting decisions

A prompt injection attempt, by contrast, is primarily a security event.

It may require investigation, but it should not be confused with a normal business approval workflow.

# Risk Review Triggers

Risk should be reassessed when something material changes.

Examples include:

- New data classification
- New user population
- New model
- New provider
- New retrieval source
- New tool or agent capability
- Production deployment
- New external integration
- New regulatory obligation
- Significant architecture change
- Security incident
- Material change in business consequence

This is more useful than assigning arbitrary review frequencies to every AI system.

Periodic review may still be required by enterprise policy.

# Example: Internal AI Policy Assistant

## Business Problem

Employees may spend unnecessary time searching across approved security, architecture, IAM, and governance documents.

A production AI assistant could eventually use RAG-style capabilities to improve discovery and provide source-grounded advisory answers.

## Current Project Implementation

The current project does **not** implement that production RAG system.

Instead, it follows:

```text
Architecture and Governance
        ↓
Local Security-Control Prototype
        ↓
Selected Control Validation
```

The local prototype uses:

- Synthetic users
- Synthetic documents
- Local metadata
- Simple keyword retrieval
- Role/group authorization
- Prompt-risk evaluation
- Local JSONL logging
- Advisory response generation

It does not use:

- Production LLM
- Embeddings
- Vector database
- Enterprise IdP
- Cloud AI service
- External model API
- Real enterprise data

# Example Risk Assessment

## Business / Decision Risk

**Current prototype:** Low

Reason:

The prototype is advisory, synthetic, local, and does not influence real business decisions.

**Production concept:** Potentially Medium to High depending on how users rely on the output.

## Data Risk

**Current prototype:** Low

Reason:

Only synthetic information is used.

Synthetic documents can carry Internal, Confidential, and Restricted labels for testing without containing real sensitive enterprise information.

**Production concept:** Depends on the real document classifications and data handling.

## Identity and Access Risk

**Current prototype:** Medium

Reason:

Authorization behavior is central to the design, but identity is simulated.

The prototype demonstrates role/group and document-metadata decisions but not enterprise IAM.

**Production concept:** Potentially High where confidential or restricted enterprise repositories are involved.

## Prompt and Retrieval Risk

**Current prototype:** Medium

Reason:

The prototype deliberately exercises prompt-risk and retrieval-control behavior.

One prompt-injection scenario has been successfully blocked before retrieval.

The detection is pattern-based and incomplete.

## Model and Output Risk

**Current prototype:** Low for actual implementation.

Reason:

There is no production LLM.

**Production concept:** Potentially Medium to High depending on model use, business consequence, and downstream reliance.

## Vendor Risk

**Current prototype:** Low

Reason:

No external AI provider is used.

**Production concept:** Depends on provider, data handling, contractual terms, and architecture.

## Operational Risk

**Current prototype:** Low

Reason:

It is a local architecture validation project, not a business-critical service.

**Production concept:** Depends on availability requirements and business dependency.

## Compliance / Governance Risk

**Current prototype:** Low to Medium

Reason:

No real regulated information or production decision process is involved, but the project intentionally models governance concerns.

**Production concept:** Could become High where output influences regulated workflows or formal compliance decisions.

# Current Risk Decision

For the current project:

**Decision: Proceed with local security-control validation using synthetic data.**

Rationale:

- No real customer data
- No regulated data
- No production secrets
- No cloud AI services
- No external AI provider
- No production actions
- No real approval authority
- No live enterprise repositories
- No autonomous agent behavior

This decision applies to the **local prototype**, not to a future production AI assistant.

# Controls Demonstrated by the Prototype

The prototype currently demonstrates selected behavior for:

- Mock identity context
- Role/group authorization
- Document metadata
- Document access decisions
- Prompt-risk evaluation
- Blocking before retrieval for the tested injection scenario
- Retrieval evidence
- Authorization evidence
- Security alerts
- Simulated human-review event generation
- Advisory-only local response

These are implementation examples, not claims of production control maturity.

# Initial Validation Evidence

Two initial scenarios are documented as executed.

## Authorized Policy Retrieval

A mock General Employee requested the AI acceptable-use policy.

Result:

**Pass**

The approved synthetic document was retrieved and an advisory response was produced.

## Prompt Injection

A mock General Employee requested that previous instructions be ignored and restricted documents revealed.

Result:

**Pass**

The request was detected and blocked before document retrieval.

Other documented test scenarios remain **Not Yet Tested** until they are actually executed.

# Prototype Control Limitations

The current prototype does not demonstrate:

- Enterprise authentication
- MFA
- Production authorization services
- Semantic retrieval
- Vector authorization
- Production LLM behavior
- Comprehensive prompt-injection resistance
- Indirect injection defense
- Production DLP
- Production secrets detection
- Production human approval
- SIEM integration
- Automated incident response
- Cloud IAM
- Provider security
- Production resilience
- Formal compliance evidence

These are areas a production architecture would need to evaluate.

# Example Risk Register

This table represents architecture risks rather than claims that every risk currently exists in the local prototype.

| Risk ID | Risk | Primary Domain | Architectural Treatment |
| --- | --- | --- | --- |
| AI-RISK-001 | Prompt injection influences system behavior | Prompt / Retrieval | Mitigate |
| AI-RISK-002 | User retrieves unauthorized documents | Identity / Access | Mitigate |
| AI-RISK-003 | Sensitive information enters prompts | Data | Mitigate |
| AI-RISK-004 | AI produces unsupported guidance | Model / Output | Mitigate |
| AI-RISK-005 | Logs expose sensitive information | Logging / Data | Mitigate |
| AI-RISK-006 | External provider mishandles enterprise data | Vendor | Avoid or Mitigate |
| AI-RISK-007 | AI service becomes operational dependency | Operational | Mitigate |
| AI-RISK-008 | AI output is mistaken for approval | Governance | Mitigate |
| AI-RISK-009 | Retrieved content contains malicious instructions | Prompt / Retrieval | Mitigate |
| AI-RISK-010 | Agent or tool gains excessive authority | Agent / Tool Use | Avoid or Mitigate |

Risk owners and residual ratings should be assigned for the actual production environment rather than invented for this portfolio project.

# Cloud Deployment

Cloud deployment does not automatically make an AI system unsafe, nor does local deployment automatically make it safe.

Moving to a cloud AI platform would introduce additional considerations such as:

- Cloud IAM
- Provider data handling
- Network architecture
- Encryption
- Secrets management
- Data residency
- Logging
- Cost
- Service availability
- Model/provider changes
- Vendor dependency

Those risks should be evaluated against the selected production architecture.

The AWS and Azure materials in this repository are reference designs only.

# Evidence for Architecture Review

Depending on the use case, useful evidence may include:

- Business case
- AI use-case intake
- Data classification
- Access-control design
- Trust boundaries
- Threat model
- Prompt-security design
- Logging design
- Human-accountability requirements
- Provider review
- Cost model
- Compliance mappings
- Test evidence
- Risk decisions
- Exception records

Not every artifact must exist independently if the same evidence is captured elsewhere.

The objective is traceability, not paperwork for its own sake.

# Security Architecture Perspective

For an AI system, I would not stop at:

> Does the model work?

I would also ask:

- What can it know?
- Who can ask?
- What can they retrieve?
- What can the output influence?
- What happens when it is wrong?
- What happens when a user is malicious?
- What happens when a source is malicious?
- What happens when a dependency fails?
- Who is accountable?
- What evidence exists?
- What residual risk remains?

Those questions determine whether the AI capability fits safely into the enterprise architecture.

# Conclusion

AI should be evaluated as part of an enterprise risk system rather than treated only as a productivity technology.

The most important risks often exist **around** the model:

**Identity → Data → Retrieval → Context → Model → Response → Decision → Action**

For this project, the production architecture defines the broader risk model while the local prototype validates selected security-control concepts using synthetic information.

The result is not a claim that every AI risk has been solved.

It demonstrates a repeatable architecture approach:

> Understand the business consequence, identify the exposure, design the controls, validate what can be validated safely, document the limitations, and leave residual risk with the appropriate accountable owner.
