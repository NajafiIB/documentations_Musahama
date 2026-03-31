#!/usr/bin/env python3

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = ROOT / "cases"

REQUIRED_FILES = [
    "cases/README.md",
    "cases/CASE-template.yaml",
]

CASE_STATES = {
    "intake",
    "planned",
    "ready_for_implementation",
    "in_implementation",
    "ready_for_qa",
    "qa_failed",
    "ready_for_closure",
    "closed",
    "blocked",
}

TASK_STATES = {"todo", "active", "done", "rework", "blocked", "cancelled"}
QA_STATUSES = {"not-run", "pending", "passed", "failed"}
ACTIVE_CASE_STATES = {"in_implementation", "ready_for_qa", "qa_failed"}

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def ensure(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def parse_iso(value: object, field: str, path: str) -> None:
    if not isinstance(value, str):
        fail(f"{path}: {field} must be a string ISO date")
        return

    candidate = value.replace("Z", "+00:00")
    try:
        dt.datetime.fromisoformat(candidate)
    except Exception:
        fail(f"{path}: {field} must be a valid ISO date")


def load_yaml(path: Path) -> dict | None:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{path.relative_to(ROOT).as_posix()}: invalid YAML → {exc}")
        return None

    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT).as_posix()}: root must be a mapping")
        return None

    return data


def validate_task(case_id: str, task: dict, declared_task_ids: list[str], path: str) -> None:
    for key in ["id", "caseId", "title", "sequence", "state", "implementationScope", "qaScope", "qaPlan"]:
        if key not in task:
            fail(f"{path}: task is missing required field '{key}'")

    task_id = task.get("id")
    if not isinstance(task_id, str) or not task_id:
        fail(f"{path}: task id must be a non-empty string")
    elif task_id not in declared_task_ids:
        fail(f"{path}: task id '{task_id}' must appear in taskIds")

    if task.get("caseId") != case_id:
        fail(f"{path}: task caseId must match parent case id")

    state = task.get("state")
    if state not in TASK_STATES:
        fail(f"{path}: task state '{state}' is not allowed")

    sequence = task.get("sequence")
    if not isinstance(sequence, int) or sequence < 1:
        fail(f"{path}: task sequence must be a positive integer")

    implementation_scope = task.get("implementationScope")
    if not isinstance(implementation_scope, list) or not implementation_scope:
        fail(f"{path}: task implementationScope must be a non-empty list")

    qa_scope = task.get("qaScope")
    if not isinstance(qa_scope, list) or not qa_scope:
        fail(f"{path}: task qaScope must be a non-empty list")

    qa_plan = task.get("qaPlan")
    if not isinstance(qa_plan, dict):
        fail(f"{path}: task qaPlan must be a mapping")
    else:
        static_checks = qa_plan.get("staticChecks")
        if not isinstance(static_checks, list) or not static_checks:
            fail(f"{path}: task qaPlan.staticChecks must be a non-empty list")

        browser_suites = qa_plan.get("browserSuites")
        if not isinstance(browser_suites, list):
            fail(f"{path}: task qaPlan.browserSuites must be a list")

    depends_on = task.get("dependsOn", [])
    if not isinstance(depends_on, list):
        fail(f"{path}: task dependsOn must be a list when present")
    else:
        for dependency in depends_on:
            if dependency not in declared_task_ids:
                fail(f"{path}: task dependency '{dependency}' must appear in taskIds")

    source_task_path = task.get("sourceTaskPath")
    if isinstance(source_task_path, str) and source_task_path:
        ensure(
            (ROOT / source_task_path).exists(),
            f"{path}: task sourceTaskPath does not exist: {source_task_path}",
        )


def validate_case(path: Path) -> None:
    relative_path = path.relative_to(ROOT).as_posix()
    data = load_yaml(path)
    if data is None:
        return

    required_fields = [
        "id",
        "title",
        "summary",
        "sourceIssue",
        "changeRequestId",
        "implementationGuideId",
        "taskIds",
        "reviewIds",
        "state",
        "qaStatus",
        "artifacts",
        "updatedAt",
    ]

    for field in required_fields:
        if field not in data:
            fail(f"{relative_path}: missing required field '{field}'")

    case_id = data.get("id")
    if not isinstance(case_id, str) or not case_id:
        fail(f"{relative_path}: id must be a non-empty string")
        return

    if path.stem != case_id:
        fail(f"{relative_path}: file name must match case id")

    state = data.get("state")
    if state not in CASE_STATES:
        fail(f"{relative_path}: state '{state}' is not allowed")

    qa_status = data.get("qaStatus")
    if qa_status not in QA_STATUSES:
        fail(f"{relative_path}: qaStatus '{qa_status}' is not allowed")

    task_ids = data.get("taskIds")
    if not isinstance(task_ids, list) or not task_ids:
        fail(f"{relative_path}: taskIds must be a non-empty list")
    elif len(set(task_ids)) != len(task_ids):
        fail(f"{relative_path}: taskIds must be unique")

    review_ids = data.get("reviewIds")
    if not isinstance(review_ids, list):
        fail(f"{relative_path}: reviewIds must be a list")

    active_task_id = data.get("activeTaskId")
    if active_task_id is not None and active_task_id not in task_ids:
        fail(f"{relative_path}: activeTaskId must appear in taskIds")

    if state in ACTIVE_CASE_STATES and not active_task_id:
        fail(f"{relative_path}: activeTaskId is required when case is active")

    source_issue = data.get("sourceIssue")
    if not isinstance(source_issue, dict):
        fail(f"{relative_path}: sourceIssue must be a mapping")
    else:
        for field in ["sourceRepo", "sourceIssueNumber", "title", "labels", "reportedBy", "createdAt"]:
            if field not in source_issue:
                fail(f"{relative_path}: sourceIssue missing '{field}'")
        parse_iso(source_issue.get("createdAt"), "createdAt", relative_path)

    parse_iso(data.get("updatedAt"), "updatedAt", relative_path)

    closure_evidence = data.get("closureEvidence", {})
    if isinstance(closure_evidence, dict):
        implementation_recorded_at = closure_evidence.get("implementationRecordedAt")
        if implementation_recorded_at is not None:
            parse_iso(implementation_recorded_at, "implementationRecordedAt", relative_path)

    artifacts = data.get("artifacts")
    if not isinstance(artifacts, dict):
        fail(f"{relative_path}: artifacts must be a mapping")
    else:
        for field in ["changeRequestPath", "implementationGuidePath", "taskPaths"]:
            if field not in artifacts:
                fail(f"{relative_path}: artifacts missing '{field}'")

        change_request_path = artifacts.get("changeRequestPath")
        if isinstance(change_request_path, str):
            ensure(
                (ROOT / change_request_path).exists(),
                f"{relative_path}: missing change request path {change_request_path}",
            )

        implementation_guide_path = artifacts.get("implementationGuidePath")
        if isinstance(implementation_guide_path, str):
            ensure(
                (ROOT / implementation_guide_path).exists(),
                f"{relative_path}: missing implementation guide path {implementation_guide_path}",
            )

        task_paths = artifacts.get("taskPaths")
        if isinstance(task_paths, list):
            if isinstance(task_ids, list) and len(task_paths) != len(task_ids):
                fail(f"{relative_path}: taskPaths must align with taskIds")
            for task_path in task_paths:
                ensure(
                    isinstance(task_path, str) and (ROOT / task_path).exists(),
                    f"{relative_path}: missing task path {task_path}",
                )
        else:
            fail(f"{relative_path}: artifacts.taskPaths must be a list")

        review_paths = artifacts.get("reviewPaths", [])
        if not isinstance(review_paths, list):
            fail(f"{relative_path}: artifacts.reviewPaths must be a list when present")
        else:
            for review_path in review_paths:
                ensure(
                    isinstance(review_path, str) and (ROOT / review_path).exists(),
                    f"{relative_path}: missing review path {review_path}",
                )

    tasks = data.get("tasks", [])
    if tasks:
        if not isinstance(tasks, list):
            fail(f"{relative_path}: tasks must be a list when present")
        else:
            seen_task_ids: set[str] = set()
            active_count = 0
            for index, task in enumerate(tasks):
                if not isinstance(task, dict):
                    fail(f"{relative_path}: tasks[{index}] must be a mapping")
                    continue
                validate_task(case_id, task, task_ids or [], relative_path)
                task_id = task.get("id")
                if isinstance(task_id, str):
                    if task_id in seen_task_ids:
                        fail(f"{relative_path}: embedded tasks must be unique")
                    seen_task_ids.add(task_id)
                if task.get("state") == "active":
                    active_count += 1

            if active_count > 1:
                fail(f"{relative_path}: only one embedded task may be active")

            if active_task_id is not None and active_count != 1:
                fail(f"{relative_path}: activeTaskId requires exactly one embedded active task")


def main() -> int:
    for relative_path in REQUIRED_FILES:
        ensure((ROOT / relative_path).exists(), f"Missing required case file: {relative_path}")

    if not CASES_DIR.exists():
        fail("Missing cases/ directory")
    else:
        active_cases = 0
        for case_path in sorted(CASES_DIR.glob("CASE-*.yaml")):
            if case_path.name == "CASE-template.yaml":
                continue
            validate_case(case_path)
            data = load_yaml(case_path)
            if data and data.get("state") in ACTIVE_CASE_STATES:
                active_cases += 1

        if active_cases > 1:
            fail("Only one case may be in_implementation or ready_for_qa at a time")

    if errors:
        print("CASE VALIDATION FAILED", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        return 1

    print("Case validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
