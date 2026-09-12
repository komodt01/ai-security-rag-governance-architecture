# Phase 2: Local AI Security Prototype

## Purpose

Phase 2 moves selected controls from the AI security architecture into a small local prototype.

The goal was not to build a production RAG platform or deploy an LLM. I wanted to validate whether several of the security decisions from the architecture could be demonstrated in code before introducing cloud services, external AI APIs, or real enterprise data.

The prototype uses Python, mock users, mock documents, document metadata, and local JSONL logs.

## Security Controls Demonstrated

The prototype demonstrates:

- Mock user identity and role context
- Role- and group-based document authorization
- Document status and classification checks
- Prompt injection detection
- Sensitive-data and secret-pattern detection
- Prompt risk scoring
- Blocking high-risk requests before document retrieval
- Authorized and denied document retrieval decisions
- Prompt event logging
- Retrieval event logging
- Access decision logging
- Security alert logging
- Simulated human-review triggers
- Advisory-only response behavior

## Request Flow

A request follows this simplified control path:

**Mock User → Prompt Risk Evaluation → Policy Decision → Document Retrieval → Authorization Check → Logging → Advisory Response**

A high-risk prompt can be stopped before retrieval occurs.

For requests that proceed to retrieval, document access is evaluated using the user's role and groups together with document metadata.

This was important to the larger architecture because the AI interaction should not become a way around existing authorization boundaries.

## Prototype Components

```text
Phase_2/
└── local_prototype/
    ├── app.py
    ├── requirements.txt
    ├── sample_users.json
    ├── sample_docs/
    ├── metadata/
    │   └── document_metadata.json
    ├── logs/
    ├── tests/
    ├── prototype_results.md
    └── readme_runbook.md
