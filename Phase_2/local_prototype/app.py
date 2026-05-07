app.py

import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

USERS_FILE = BASE_DIR / "sample_users.json"
METADATA_FILE = BASE_DIR / "metadata" / "document_metadata.json"
DOCS_DIR = BASE_DIR / "sample_docs"
LOGS_DIR = BASE_DIR / "logs"

PROMPT_LOG = LOGS_DIR / "prompt_events.jsonl"
RETRIEVAL_LOG = LOGS_DIR / "retrieval_events.jsonl"
ACCESS_LOG = LOGS_DIR / "access_decisions.jsonl"
ALERT_LOG = LOGS_DIR / "security_alerts.jsonl"
REVIEW_LOG = LOGS_DIR / "review_events.jsonl"


PROMPT_INJECTION_PATTERNS = [
    r"ignore (all )?(previous|prior) instructions",
    r"disregard (the )?(system|developer) prompt",
    r"show me (the )?(system prompt|hidden instructions)",
    r"reveal (the )?(system prompt|hidden instructions|restricted documents)",
    r"do not log",
    r"bypass (security|access|controls|compliance)",
    r"disable (security|access|logging|controls)",
    r"pretend (you are|i am)",
    r"act as (an|a) (administrator|admin|ciso|security reviewer)",
    r"search all (restricted|confidential|documents)",
]

SENSITIVE_DATA_PATTERNS = [
    r"AKIA[0-9A-Z]{12,20}",
    r"-----BEGIN PRIVATE KEY-----",
    r"password\s*[:=]?\s*\S+",
    r"\b\d{3}-\d{2}-\d{4}\b",
    r"\b(?:\d[ -]*?){13,16}\b",
    r"api[_ -]?key",
    r"secret",
    r"customer account",
    r"employee record",
    r"production log",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_jsonl(path: Path, event: dict) -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(event) + "\n")


def detect_patterns(prompt: str, patterns: list[str]) -> list[str]:
    matches = []
    for pattern in patterns:
        if re.search(pattern, prompt, re.IGNORECASE):
            matches.append(pattern)
    return matches


def score_prompt(prompt: str) -> dict:
    injection_matches = detect_patterns(prompt, PROMPT_INJECTION_PATTERNS)
    sensitive_matches = detect_patterns(prompt, SENSITIVE_DATA_PATTERNS)

    if sensitive_matches:
        return {
            "risk_score": "Critical",
            "category": "Sensitive Data or Secret Exposure",
            "action": "Block",
            "injection_matches": injection_matches,
            "sensitive_matches": sensitive_matches,
        }

    if injection_matches:
        return {
            "risk_score": "High",
            "category": "Prompt Injection Attempt",
            "action": "Block",
            "injection_matches": injection_matches,
            "sensitive_matches": sensitive_matches,
        }

    broad_terms = ["all documents", "everything", "restricted", "confidential"]
    if any(term in prompt.lower() for term in broad_terms):
        return {
            "risk_score": "Medium",
            "category": "Broad or Sensitive Scope",
            "action": "Evaluate",
            "injection_matches": injection_matches,
            "sensitive_matches": sensitive_matches,
        }

    return {
        "risk_score": "Low",
        "category": "Normal Business Prompt",
        "action": "Allow",
        "injection_matches": injection_matches,
        "sensitive_matches": sensitive_matches,
    }


def find_user(users: dict, user_id: str) -> dict:
    for user in users.get("users", []):
        if user["user_id"] == user_id:
            return user
    raise ValueError(f"Unknown user_id: {user_id}")


def user_can_access_document(user: dict, document: dict) -> bool:
    user_role = user.get("role")
    user_groups = set(user.get("groups", []))

    allowed_roles = set(document.get("allowed_roles", []))
    allowed_groups = set(document.get("allowed_groups", []))

    if document.get("status") != "approved":
        return False

    if not document.get("classification"):
        return False

    if not document.get("owner"):
        return False

    role_match = user_role in allowed_roles
    group_match = bool(user_groups.intersection(allowed_groups))

    return role_match or group_match


def keyword_match(prompt: str, document: dict) -> int:
    prompt_text = prompt.lower()
    score = 0

    for tag in document.get("tags", []):
        if tag.lower() in prompt_text:
            score += 3

    title_words = re.findall(r"\w+", document.get("title", "").lower())
    for word in title_words:
        if len(word) > 3 and word in prompt_text:
            score += 1

    return score


def retrieve_documents(prompt: str, user: dict, metadata: dict) -> tuple[list[dict], list[dict]]:
    scored_documents = []

    for document in metadata.get("documents", []):
        score = keyword_match(prompt, document)
        if score > 0:
            scored_documents.append((score, document))

    if not scored_documents:
        scored_documents = [(1, document) for document in metadata.get("documents", [])]

    scored_documents.sort(key=lambda item: item[0], reverse=True)

    retrieved = []
    denied = []

    for _, document in scored_documents[:3]:
        if user_can_access_document(user, document):
            retrieved.append(document)
        else:
            denied.append(document)

    return retrieved, denied


def read_document(document: dict) -> str:
    doc_path = DOCS_DIR / Path(document["file_path"]).name
    if not doc_path.exists():
        return "[Document file missing from local prototype.]"
    return doc_path.read_text(encoding="utf-8")


def build_mock_response(prompt: str, retrieved_documents: list[dict]) -> str:
    if not retrieved_documents:
        return (
            "No authorized documents were available for this request. "
            "Please contact the appropriate document owner or submit a formal review request."
        )

    response_parts = [
        "Prototype advisory response:",
        "",
        "Based on the mock documents you are authorized to access, the following source material may be relevant:",
        "",
    ]

    for document in retrieved_documents:
        content = read_document(document)
        preview = " ".join(content.split()[:55])
        response_parts.append(f"- {document['document_id']} - {document['title']}: {preview}...")

    response_parts.extend(
        [
            "",
            "This prototype response is advisory only. It is not an approval, exception, legal interpretation, or production decision.",
        ]
    )

    return "\n".join(response_parts)


def run_prompt(user_id: str, prompt: str) -> None:
    users = load_json(USERS_FILE)
    metadata = load_json(METADATA_FILE)

    user = find_user(users, user_id)
    correlation_id = f"corr_{uuid.uuid4().hex[:10]}"
    prompt_id = f"prompt_{uuid.uuid4().hex[:10]}"

    prompt_score = score_prompt(prompt)

    prompt_event = {
        "timestamp": utc_now(),
        "correlation_id": correlation_id,
        "prompt_id": prompt_id,
        "user_id": user["user_id"],
        "user_role": user["role"],
        "prompt_category": prompt_score["category"],
        "risk_score": prompt_score["risk_score"],
        "policy_action": prompt_score["action"],
        "injection_pattern_detected": bool(prompt_score["injection_matches"]),
        "sensitive_data_detected": bool(prompt_score["sensitive_matches"]),
    }
    write_jsonl(PROMPT_LOG, prompt_event)

    if prompt_score["action"] == "Block":
        alert_event = {
            "timestamp": utc_now(),
            "correlation_id": correlation_id,
            "prompt_id": prompt_id,
            "user_id": user["user_id"],
            "user_role": user["role"],
            "alert_type": prompt_score["category"],
            "severity": prompt_score["risk_score"],
            "action": "Blocked before retrieval",
        }
        write_jsonl(ALERT_LOG, alert_event)

        print("\nREQUEST BLOCKED")
        print("Reason:", prompt_score["category"])
        print("The request was blocked before document retrieval.")
        return

    retrieved, denied = retrieve_documents(prompt, user, metadata)

    retrieval_event = {
        "timestamp": utc_now(),
        "correlation_id": correlation_id,
        "prompt_id": prompt_id,
        "user_id": user["user_id"],
        "user_role": user["role"],
        "retrieved_document_ids": [doc["document_id"] for doc in retrieved],
        "denied_document_ids": [doc["document_id"] for doc in denied],
    }
    write_jsonl(RETRIEVAL_LOG, retrieval_event)

    for document in retrieved:
        access_event = {
            "timestamp": utc_now(),
            "correlation_id": correlation_id,
            "prompt_id": prompt_id,
            "user_id": user["user_id"],
            "user_role": user["role"],
            "document_id": document["document_id"],
            "document_classification": document["classification"],
            "decision": "Allow",
            "reason": "User role or group is authorized.",
        }
        write_jsonl(ACCESS_LOG, access_event)

        if document.get("human_review_required"):
            review_event = {
                "timestamp": utc_now(),
                "correlation_id": correlation_id,
                "prompt_id": prompt_id,
                "user_id": user["user_id"],
                "user_role": user["role"],
                "document_id": document["document_id"],
                "review_trigger": "Document requires human review.",
                "review_status": "Pending simulated review",
            }
            write_jsonl(REVIEW_LOG, review_event)

    for document in denied:
        access_event = {
            "timestamp": utc_now(),
            "correlation_id": correlation_id,
            "prompt_id": prompt_id,
            "user_id": user["user_id"],
            "user_role": user["role"],
            "document_id": document["document_id"],
            "document_classification": document["classification"],
            "decision": "Deny",
            "reason": "User role or group is not authorized.",
        }
        write_jsonl(ACCESS_LOG, access_event)

    if denied:
        alert_event = {
            "timestamp": utc_now(),
            "correlation_id": correlation_id,
            "prompt_id": prompt_id,
            "user_id": user["user_id"],
            "user_role": user["role"],
            "alert_type": "Denied Document Retrieval",
            "severity": "Medium",
            "denied_document_ids": [doc["document_id"] for doc in denied],
        }
        write_jsonl(ALERT_LOG, alert_event)

    print("\nREQUEST PROCESSED")
    print("User:", user["display_name"], f"({user['role']})")
    print("Risk Score:", prompt_score["risk_score"])
    print("Retrieved Documents:", [doc["document_id"] for doc in retrieved])
    print("Denied Documents:", [doc["document_id"] for doc in denied])
    print()
    print(build_mock_response(prompt, retrieved))


def main() -> None:
    print("Local AI Security Prototype")
    print("---------------------------")
    print("This prototype uses mock users, mock documents, local logs, and no cloud services.")
    print()

    users = load_json(USERS_FILE)

    print("Available mock users:")
    for user in users.get("users", []):
        print(f"- {user['user_id']}: {user['display_name']} ({user['role']})")

    print()
    user_id = input("Enter mock user_id: ").strip()
    prompt = input("Enter prompt: ").strip()

    run_prompt(user_id, prompt)


if __name__ == "__main__":
    main()
