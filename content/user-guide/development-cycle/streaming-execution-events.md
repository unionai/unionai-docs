---
title: Streaming execution events
weight: 21
variants: -flyte +union
---

# Streaming execution events

{{< key product_name >}} exposes a streaming API so you can receive workflow, task, and node execution phase events in real time and implement your own alerting, dashboards, or automation. This page describes the interface and shows how to consume events and react to them (for example, sending Slack alerts when a node fails or is queued too long).

## Overview

Using the Union SDK, you connect to the event stream with a `UnionRemote` instance and iterate over execution events as they occur. You choose which event types to subscribe to (workflow, task, or node executions), and you process each event (e.g., check phase, update state, call a webhook). Events are acknowledged after processing so the service can stop retransmitting them.

## Interface: `stream_execution_events`

The `UnionRemote` class provides the **`stream_execution_events`** async generator.

**Delivery and acknowledgment**

- You may receive the same event more than once, or events out of order. Your code should tolerate duplicates and reordering (for example by treating updates as idempotent or by tracking the latest phase per execution).
- The server keeps sending an event until your side has “acknowledged” it. The SDK acknowledges an event automatically when your loop moves on to the next one (when you pull the next item from the generator).
- If you raise an exception while handling an event, that event is never acknowledged. The server will send it again later. Finish handling without raising if you want that event to be considered done; or raise on purpose to force redelivery.

**Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `event_count` | `Optional[int]` | Number of events to receive before closing the stream. `None` means unlimited. |
| `include_workflow_executions` | `bool` | If `True`, include workflow execution events. |
| `include_task_executions` | `bool` | If `True`, include task execution events. |
| `include_node_executions` | `bool` | If `True`, include node execution events. |


## Event contents

The yielded values are protobuf messages from `flyteidl.event.cloudevents_pb2`: `CloudEventWorkflowExecution`, `CloudEventNodeExecution`, or `CloudEventTaskExecution`. Each has a similar shape:

**Common fields (all event types)**

| Field | Type | Description |
|-------|------|-------------|
| `phase` | enum | Execution phase (e.g. UNDEFINED, QUEUED, RUNNING, SUCCEEDED, FAILED, ABORTED, TIMED_OUT). Use `WorkflowExecutionPhase.enum_to_string(phase)` in Python for a string. |

**Identity**

Identity (which execution and, for node/task, which node or task) can appear as a top-level `execution_id` or under an `id` submessage, depending on event type. Typical attributes:

| Attribute | Description |
|-----------|-------------|
| `execution_id.name` | Execution name (unique per run). |
| `execution_id.project` | Project. |
| `execution_id.domain` | Domain. |
| `node_id` | Present on node (and often task) events. Either a string node id or an object with a `node_id` field. Identifies the node within the workflow. |
| `task_id` | On task events; identifies the task execution. |

**By event type**

- **CloudEventWorkflowExecution** — One of `id` or `execution_id` carries workflow execution identity (project, domain, name). No `node_id`; scope is the whole workflow.
- **CloudEventNodeExecution** — Carries workflow execution identity plus `node_id` (the node that changed phase). Use this for node-level alerting and “which node failed or is queued.”
- **CloudEventTaskExecution** — Carries workflow execution identity plus task-level identifiers (e.g. `task_id`, node association) for task-level phase changes.

In Python, use `getattr(event, "execution_id", None)` or `getattr(getattr(event, "id", None), "execution_id", None)` to resolve the execution id, and `getattr(event, "node_id", None)` or the same from `event.id` when handling node or task events. The example in this page shows this pattern.

## Phases

Execution phases follow the Flyte model (e.g., `UNDEFINED`, `QUEUED`, `RUNNING`, `SUCCEEDED`, `FAILED`, `ABORTED`, `TIMED_OUT`). In Python you can use `flytekit.models.core.execution.WorkflowExecutionPhase.enum_to_string(phase)` to get a string like `"QUEUED"` or `"FAILED"` from the raw phase field on the event.

## How this differs from LaunchPlan notifications

**LaunchPlan notifications** are a separate feature: you attach a webhook URL to a launch plan (or schedule), and the platform calls that URL when a *workflow* run reaches a **terminal** phase (e.g. `SUCCEEDED`, `FAILED`, `ABORTED`, `TIMED_OUT`). You get one HTTP request per workflow completion, with no visibility into intermediate states or into individual nodes/tasks.

| | LaunchPlan notifications | Streaming execution events |
|--|---------------------------|----------------------------|
| **Trigger** | One webhook call when the workflow finishes (terminal phase only). | Continuous stream; you receive every phase change as it happens. |
| **Phases** | Terminal only (SUCCEEDED, FAILED, etc.). No QUEUED or RUNNING. | All phases (QUEUED, RUNNING, SUCCEEDED, FAILED, etc.). |
| **Granularity** | Workflow-level only. | Workflow, task, or node level (you choose via `include_*` flags). |
| **Who runs** | Platform pushes to your URL; no long-lived process on your side. | You run a process that connects and consumes the stream; you implement alerting logic. |
| **Use case** | “Notify me when this workflow run is done.” | “Notify me when a node fails,” “alert if queued too long,” dashboards, custom automation. |

In summary, use **LaunchPlan notifications** for simpler notifications on terminal state. Use the **streaming API** when you need visibility into intermediate phases (e.g. QUEUED) or custom alerting logic, detached from task execution.

## Example: Node-level alerts (Slack)

The following example streams **node execution** events and:

1. Logs every node phase change.
2. Sends a Slack alert when a node enters **FAILED**.
3. Tracks how long nodes stay **QUEUED** and alerts when they exceed a threshold (e.g., 5 minutes).

It uses environment variables for the Union endpoint, Slack webhook, and queue threshold. The stream runs in a loop with reconnection on error.

> This pattern works best with `union >= v0.1.202`

```python
"""
Stream Flyte node execution events and alert to Slack when:
 - A node enters FAILED status
 - A node has been QUEUED longer than QUEUED_THRESHOLD_SEC (default 300s)

Usage:
  python get_node_events.py

  export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."
  export QUEUED_THRESHOLD_SEC=600  # Alert if queued > 10 min
  python get_node_events.py
"""

import asyncio
import json
import os
import sys
import time
import urllib.request

from union.remote import UnionRemote
from flytekit.configuration import Config
from flytekit.models.core.execution import WorkflowExecutionPhase

# Slack webhook (override via SLACK_WEBHOOK_URL or ALERT_WEBHOOK_URL env)
SLACK_WEBHOOK_URL = ""
QUEUED_THRESHOLD_SEC = int(os.getenv("QUEUED_THRESHOLD_SEC", "300"))
QUEUED_CHECK_INTERVAL_SEC = 60

# (execution_name, node_id) -> (first_seen_timestamp, project, domain)
queued_since = {}


def _post_webhook_sync(url: str, payload: dict) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        resp.read()


def _get_webhook_url():
    return os.getenv("SLACK_WEBHOOK_URL") or os.getenv("ALERT_WEBHOOK_URL") or SLACK_WEBHOOK_URL


async def alert_on_failed(*, event_line: str, execution_name: str, node_id: str | None = None):
    if "FAILED" not in event_line:
        return
    node_info = f" Node: `{node_id}`" if node_id else ""
    print(f"[ALERT] Node FAILED: execution={execution_name}{node_info} - {event_line}", file=sys.stderr)
    webhook_url = _get_webhook_url()
    if not webhook_url:
        return
    payload = {
        "text": f"Flyte node execution *FAILED*{node_info}\nExecution: `{execution_name}`\n{event_line}",
    }
    await asyncio.to_thread(_post_webhook_sync, webhook_url, payload)


async def alert_on_queued_threshold(*, execution_name: str, node_id: str | None, project: str, domain: str, queued_sec: float):
    webhook_url = _get_webhook_url()
    if not webhook_url:
        return
    node_info = f" Node: `{node_id}`" if node_id else ""
    project_domain = f"{project}/{domain}" if project or domain else "-"
    payload = {
        "text": (
            f"Flyte node *queued too long*{node_info}\n"
            f"Execution: `{execution_name}`\nProject/Domain: `{project_domain}`\n"
            f"Queued for: {queued_sec:.0f}s (threshold: {QUEUED_THRESHOLD_SEC}s)"
        ),
    }
    await asyncio.to_thread(_post_webhook_sync, webhook_url, payload)


async def _check_queued_threshold():
    while True:
        await asyncio.sleep(QUEUED_CHECK_INTERVAL_SEC)
        now = time.time()
        to_alert = []
        for key, (first_seen, project, domain) in list(queued_since.items()):
            elapsed = now - first_seen
            if elapsed >= QUEUED_THRESHOLD_SEC:
                to_alert.append((key, project, domain, elapsed))
                del queued_since[key]
        for (execution_name, node_id), project, domain, queued_sec in to_alert:
            print(
                f"[ALERT] Node queued {queued_sec:.0f}s (threshold {QUEUED_THRESHOLD_SEC}s): "
                f"{project}/{domain} execution={execution_name} node={node_id}",
                file=sys.stderr,
            )
            await alert_on_queued_threshold(
                execution_name=execution_name, node_id=node_id,
                project=project, domain=domain, queued_sec=queued_sec,
            )


async def _process_event(raw_event):
    """Process a single streamed event (node execution)."""
    event_id = getattr(raw_event, "id", None)
    exec_id = getattr(event_id, "execution_id", None) if event_id else None
    if exec_id is None:
        exec_id = getattr(raw_event, "execution_id", None)

    execution_name = getattr(exec_id, "name", None) if exec_id else "unknown"
    project = getattr(exec_id, "project", "") if exec_id else ""
    domain = getattr(exec_id, "domain", "") if exec_id else ""

    phase_str = WorkflowExecutionPhase.enum_to_string(raw_event.phase)

    node_id_raw = getattr(event_id, "node_id", None) if event_id else getattr(raw_event, "node_id", None)
    node_id_str = None
    if node_id_raw is not None:
        node_id_str = (
            node_id_raw.node_id if hasattr(node_id_raw, "node_id") else
            node_id_raw if isinstance(node_id_raw, str) else str(node_id_raw)
        )

    key = (execution_name, node_id_str)

    if phase_str == "QUEUED":
        if key not in queued_since:
            queued_since[key] = (time.time(), project, domain)
    else:
        queued_since.pop(key, None)

    event_line = f"Node execution {execution_name} in {project}-{domain} is {phase_str}"
    if node_id_str:
        event_line = f"{event_line} (node={node_id_str})"
    print(event_line)
    await alert_on_failed(event_line=event_line, execution_name=execution_name, node_id=node_id_str)

async def main():
    union_remote = UnionRemote(
        config=Config.for_endpoint(endpoint="YOUR_UNION_ENDPOINT"),
        default_project="flytesnacks",
        default_domain="development",
    )

    asyncio.create_task(_check_queued_threshold())

    while True:
        try:
            async for response in union_remote.stream_execution_events(
                event_count=None,
                include_workflow_executions=False,
                include_task_executions=False,
                include_node_executions=True,
            ):
                # response is CloudEventNodeExecution (or workflow/task depending on filters)
                await _process_event(response)

if __name__ == "__main__":
    asyncio.run(main())
```

### What the example does

- **Stream subscription**: Calls `stream_execution_events(..., include_node_executions=True)` so only node execution events are received.
- **Phase handling**: Uses `WorkflowExecutionPhase.enum_to_string(raw_event.phase)` to get phases like `QUEUED`, `RUNNING`, `FAILED`.
- **Identity**: Reads execution name, project, domain, and node id from the event (or its `id` submessage) to log and alert with context.
- **FAILED alerts**: When the phase is FAILED, it prints to stderr and POSTs a Slack-compatible payload to `SLACK_WEBHOOK_URL` or `ALERT_WEBHOOK_URL`.
- **Queued-too-long alerts**: Maintains a map of `(execution_name, node_id)` to the time they first entered QUEUED. A background task periodically checks this map and alerts (and removes the entry) when queued time exceeds `QUEUED_THRESHOLD_SEC`.


You can adapt the same pattern to workflow or task events by setting `include_workflow_executions` or `include_task_executions`, and by adjusting how you read identity and phase from the corresponding CloudEvent type.

## Summary

| Capability | Description |
|------------|-------------|
| **Stream** | `union_remote.stream_execution_events(...)` — async generator over workflow/task/node events. |
| **Filter** | `include_workflow_executions`, `include_task_executions`, `include_node_executions` control which event types you receive. |
| **Phases** | Use `WorkflowExecutionPhase.enum_to_string(phase)` for human-readable phase strings. |
| **Delivery** | At-least-once; handle duplicates and out-of-order events. Events are acknowledged when you consume the next item; raise to avoid ack and get redelivery. |
| **Alerting** | Implement your own logic (e.g., webhooks, Slack) in the async loop that processes each event. |

Using this interface, you can build custom alerting, dashboards, and automation on top of {{< key product_name >}} execution events.
