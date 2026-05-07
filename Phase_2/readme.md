## Phase 2: Local Security Prototype

The next phase of this project will add a local, no-cloud-cost prototype to demonstrate selected security controls from the architecture documentation.

The prototype will use mock users, mock roles, mock documents, and local logs to show how a secure AI/RAG assistant could enforce access control, detect prompt injection attempts, and record security-relevant events.

### Phase 2 Goals

- Demonstrate role-based document access
- Use mock document classification labels
- Block basic prompt injection attempts
- Detect secret-like or sensitive-data patterns
- Log prompt events locally
- Log retrieval and access decisions locally
- Simulate human review triggers for high-risk prompts
- Avoid all paid cloud services and external AI APIs

### Planned Phase 2 Components

- `local_prototype/app.py`
- `local_prototype/sample_users.json`
- `local_prototype/sample_docs/`
- `local_prototype/metadata/document_metadata.json`
- `local_prototype/logs/`
- `local_prototype/tests/`

### Phase 2 Cost Statement

Phase 2 will remain local-first and cost-safe.

No AWS, Azure, GCP, OCI, OpenAI API, Bedrock, Azure OpenAI, SageMaker, OpenSearch, Kendra, or paid cloud services are required.

Estimated cost: $0.

### Phase 2 Status

Planned.
