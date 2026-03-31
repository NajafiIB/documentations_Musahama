#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = ROOT / "cases"

RUNTIME_STATES = {"in_implementation", "ready_for_qa", "qa_failed", "ready_for_closure", "closed"}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_event() -> dict:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        raise RuntimeError("GITHUB_EVENT_PATH is required.")

    with open(event_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:72] or "untitled"


def padded_issue_number(number: int) -> str:
    return str(number).zfill(3)


def trim_issue_title(title: str) -> str:
    return re.sub(r"^\[(feature|cr)\]\s*", "", title, flags=re.IGNORECASE).strip() or title.strip()


def extract_summary(body: str | None, fallback: str) -> str:
    if not body:
        return fallback

    lines = body.splitlines()
    capture = False
    collected: list[str] = []

    for line in lines:
      stripped = line.strip()
      lowered = stripped.lower()

      if lowered in {"# summary", "## summary"}:
          capture = True
          continue

      if capture and stripped.startswith("#"):
          break

      if capture and stripped == "---":
          if collected:
              break
          continue

      if capture and stripped:
          collected.append(stripped)

    if collected:
        return " ".join(collected).strip()

    paragraph: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped == "---":
            if paragraph:
                break
            continue
        paragraph.append(stripped)

    return " ".join(paragraph).strip() or fallback


def normalize_labels(raw_labels: list[str]) -> list[str]:
    mapped: list[str] = []
    normalized = {label.strip().lower() for label in raw_labels if isinstance(label, str)}

    if "feature-request" in normalized:
        mapped.append("feature")

    if "change-request" in normalized or "type/bug" in normalized:
        mapped.append("bug")

    if "type/docs" in normalized:
        mapped.append("docs-clarification")

    if "qa-regression" in normalized:
        mapped.append("qa-regression")

    if "status/blocked" in normalized:
        mapped.append("blocked")

    if "status/approved" in normalized or "review/ready-to-implement" in normalized:
        mapped.append("ready-for-implementation")

    for label in ["feature", "bug", "qa-regression", "docs-clarification", "blocked", "ready-for-implementation", "ready-for-qa"]:
        if label in normalized:
            mapped.append(label)

    deduped: list[str] = []
    for label in mapped:
        if label not in deduped:
            deduped.append(label)

    return deduped or ["bug"]


def derive_case_state(labels: list[str]) -> tuple[str, str | None, str]:
    if "blocked" in labels:
        return "blocked", None, "intake-docs-agent"
    if "ready-for-implementation" in labels:
        return "ready_for_implementation", "TASK", "implementation-agent"
    return "planned", None, "intake-docs-agent"


def default_qa_plan(labels: list[str]) -> dict:
    requires_browser = any(label in labels for label in ["feature", "bug", "qa-regression"])
    return {
        "staticChecks": ["check:delivery-orchestrator", "tsc", "lint", "build"],
        "browserSuites": ["workspace-smoke"] if requires_browser else [],
    }


def next_queue_order() -> int:
    highest = 0
    for case_path in CASES_DIR.glob("CASE-*.yaml"):
        try:
            data = json.loads(case_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        queue_order = data.get("queueOrder")
        if isinstance(queue_order, int):
            highest = max(highest, queue_order)
    return highest + 1


def load_existing_case(case_path: Path) -> dict | None:
    if not case_path.exists():
        return None

    return json.loads(case_path.read_text(encoding="utf-8"))


def ensure_document(relative_path: str, content: str) -> None:
    absolute_path = ROOT / relative_path
    absolute_path.parent.mkdir(parents=True, exist_ok=True)
    if absolute_path.exists():
        return
    absolute_path.write_text(content, encoding="utf-8")


def write_case(case_path: Path, payload: dict) -> None:
    case_path.parent.mkdir(parents=True, exist_ok=True)
    case_path.write_text(f"{json.dumps(payload, indent=2)}\n", encoding="utf-8")


def build_paths(year: int, issue_number: int, slug: str) -> dict[str, str]:
    base = f"{year}-{padded_issue_number(issue_number)}"
    case_id = f"CASE-{base}"
    change_request_id = f"CR-{base}"
    implementation_guide_id = f"IMP-{base}"
    task_id = f"TASK-{base}-01"

    return {
        "case_id": case_id,
        "change_request_id": change_request_id,
        "implementation_guide_id": implementation_guide_id,
        "task_id": task_id,
        "change_request_path": f"change-requests/{change_request_id}-{slug}.md",
        "implementation_guide_path": f"implementation-guides/{implementation_guide_id}-{slug}.md",
        "task_path": f"tasks/{task_id}-{slug}.md",
    }


def build_change_request(title: str, summary: str, repo: str, issue_number: int) -> str:
    return f"""# Change Request: {title}

Source issue: {repo}#{issue_number}

## Summary

{summary}

## Requested Outcome

- normalize the issue into the canonical delivery workflow
- update linked implementation and QA artifacts through the orchestrator loop
"""


def build_implementation_guide(title: str, case_id: str, task_title: str) -> str:
    return f"""# Implementation Guide: {title}

Case: {case_id}

## Delivery Sequence

1. {task_title}

## Closure Gate

- docs updated and validated
- implementation evidence attached
- QA passed
"""


def build_task_document(case_id: str, task_id: str, title: str, qa_scope: list[str], qa_plan: dict) -> str:
    return f"""# Task: {title}

Case: {case_id}

Task ID: {task_id}

State: todo

## Implementation Scope

- implementation repo change

## QA Scope

{chr(10).join(f"- {item}" for item in qa_scope)}

## QA Plan

Static checks:
{chr(10).join(f"- {item}" for item in qa_plan["staticChecks"])}

Browser suites:
{chr(10).join(f"- {item}" for item in qa_plan["browserSuites"]) if qa_plan["browserSuites"] else "- none"}
"""


def write_outputs(values: dict[str, str]) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        return

    with open(output_path, "a", encoding="utf-8") as handle:
        for key, value in values.items():
            handle.write(f"{key}={value}\n")


def build_case_manifest(issue: dict, labels: list[str]) -> dict:
    issue_number = int(issue["number"])
    created_at = issue.get("created_at") or now_iso()
    year = datetime.fromisoformat(created_at.replace("Z", "+00:00")).year
    title = trim_issue_title(issue.get("title", "Untitled issue"))
    slug = slugify(title)
    ids = build_paths(year, issue_number, slug)
    case_path = ROOT / "cases" / f"{ids['case_id']}.yaml"
    existing_case = load_existing_case(case_path)
    qa_plan = default_qa_plan(labels)
    summary = extract_summary(issue.get("body"), title)
    state, active_task_marker, next_owner = derive_case_state(labels)
    active_task_id = ids["task_id"] if active_task_marker else None
    timestamp = now_iso()

    task_payload = {
        "id": ids["task_id"],
        "caseId": ids["case_id"],
        "title": title,
        "sequence": 1,
        "state": "active" if state == "ready_for_implementation" else "todo",
        "dependsOn": [],
        "implementationScope": ["implementation repo change"],
        "qaScope": ["static checks", "targeted smoke"],
        "qaPlan": qa_plan,
        "owner": "implementation-agent" if state == "ready_for_implementation" else "intake-docs-agent",
        "sourceTaskPath": ids["task_path"],
    }

    manifest = {
        "id": ids["case_id"],
        "title": title,
        "summary": summary,
        "sourceIssue": {
            "sourceRepo": "documentations_Musahama",
            "sourceIssueNumber": issue_number,
            "sourceIssueUrl": issue.get("html_url"),
            "title": issue.get("title", title),
            "labels": labels,
            "reportedBy": issue.get("user", {}).get("login", "human"),
            "createdAt": created_at,
        },
        "changeRequestId": ids["change_request_id"],
        "implementationGuideId": ids["implementation_guide_id"],
        "taskIds": [ids["task_id"]],
        "reviewIds": [],
        "state": state,
        "activeTaskId": active_task_id,
        "implementationRef": {
            "repo": "Implementation_Musahama",
            "branch": None,
            "commit": None,
            "pullRequestUrl": None,
            "committedAt": None,
        },
        "qaStatus": "pending" if state == "ready_for_qa" else "not-run",
        "closureEvidence": {
            "docsValidated": True,
            "docsPublishedAt": timestamp,
            "docsPublishRef": "main",
            "implementationMerged": False,
            "implementationCommit": None,
            "implementationBranch": None,
            "implementationRecordedAt": None,
            "qaPassed": False,
            "qaRunId": None,
            "closedAt": None,
        },
        "artifacts": {
            "changeRequestPath": ids["change_request_path"],
            "implementationGuidePath": ids["implementation_guide_path"],
            "taskPaths": [ids["task_path"]],
            "reviewPaths": [],
        },
        "tasks": [task_payload],
        "queueOrder": next_queue_order(),
        "nextOwner": next_owner,
        "updatedAt": timestamp,
    }

    if existing_case:
        manifest["reviewIds"] = existing_case.get("reviewIds", [])
        manifest["implementationRef"] = existing_case.get("implementationRef", manifest["implementationRef"])
        manifest["artifacts"]["reviewPaths"] = existing_case.get("artifacts", {}).get("reviewPaths", [])
        manifest["queueOrder"] = existing_case.get("queueOrder", manifest["queueOrder"])
        manifest["tasks"] = existing_case.get("tasks", manifest["tasks"])
        manifest["taskIds"] = existing_case.get("taskIds", manifest["taskIds"])
        manifest["artifacts"]["taskPaths"] = existing_case.get("artifacts", {}).get("taskPaths", manifest["artifacts"]["taskPaths"])
        manifest["artifacts"]["changeRequestPath"] = existing_case.get("artifacts", {}).get("changeRequestPath", manifest["artifacts"]["changeRequestPath"])
        manifest["artifacts"]["implementationGuidePath"] = existing_case.get("artifacts", {}).get("implementationGuidePath", manifest["artifacts"]["implementationGuidePath"])
        manifest["closureEvidence"] = {
            **existing_case.get("closureEvidence", {}),
            "docsValidated": True,
            "docsPublishedAt": timestamp,
            "docsPublishRef": "main",
        }
        manifest["qaStatus"] = existing_case.get("qaStatus", manifest["qaStatus"])

        existing_state = existing_case.get("state")
        if existing_state in RUNTIME_STATES:
            manifest["state"] = existing_state
            manifest["activeTaskId"] = existing_case.get("activeTaskId")
            manifest["nextOwner"] = existing_case.get("nextOwner", manifest["nextOwner"])
        else:
            manifest["state"] = state
            manifest["activeTaskId"] = active_task_id
            manifest["nextOwner"] = next_owner

    if manifest["tasks"]:
        first_task = manifest["tasks"][0]
        first_task.setdefault("qaPlan", qa_plan)
        if manifest["state"] == "ready_for_implementation":
            first_task["state"] = "active"
            manifest["activeTaskId"] = first_task["id"]
            manifest["nextOwner"] = "implementation-agent"
        elif manifest["state"] in {"planned", "blocked"} and first_task.get("state") not in {"done", "cancelled"}:
            first_task["state"] = "todo"
            manifest["activeTaskId"] = None

    ensure_document(
        manifest["artifacts"]["changeRequestPath"],
        build_change_request(title, summary, "documentations_Musahama", issue_number),
    )
    ensure_document(
        manifest["artifacts"]["implementationGuidePath"],
        build_implementation_guide(title, manifest["id"], task_payload["title"]),
    )
    ensure_document(
        manifest["artifacts"]["taskPaths"][0],
        build_task_document(manifest["id"], task_payload["id"], task_payload["title"], task_payload["qaScope"], qa_plan),
    )

    write_case(case_path, manifest)

    write_outputs(
        {
            "case_id": manifest["id"],
            "case_path": f"cases/{case_path.name}",
            "change_request_path": manifest["artifacts"]["changeRequestPath"],
            "implementation_guide_path": manifest["artifacts"]["implementationGuidePath"],
            "task_path": manifest["artifacts"]["taskPaths"][0],
            "task_id": manifest["taskIds"][0],
        }
    )

    return manifest


def main() -> int:
    event = load_event()
    issue = event.get("issue")
    if not isinstance(issue, dict):
        raise RuntimeError("GitHub issue payload is required.")

    raw_labels = [label.get("name", "") for label in issue.get("labels", []) if isinstance(label, dict)]
    labels = normalize_labels(raw_labels)
    build_case_manifest(issue, labels)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
