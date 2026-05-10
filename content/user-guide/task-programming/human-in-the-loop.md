---
title: Human-in-the-loop
weight: 17
variants: +flyte +union
---

# Human-in-the-loop

Human-in-the-loop (HITL) workflows pause execution at a defined point, wait for a human to provide input or approval, and then continue based on that response. Common use cases include content moderation gates, model output review, anomaly confirmation, and manual approval steps before costly or irreversible operations.

The `flyteplugins-hitl` package provides an event-based API for this pattern. When an event is created, Flyte automatically serves a small FastAPI web app with a form where a human can submit input. The workflow then resumes with the submitted value.

```bash
pip install flyteplugins-hitl
```

Key characteristics:

- Supports `int`, `float`, `str`, and `bool` input types
- Crash-resilient: uses durable sleep so polling survives task restarts
- Configurable timeout and poll interval
- The web form is accessible from the task's report in the Flyte UI

## Setup

The task environment must declare `hitl.env` as a dependency. This makes the HITL web app available during task execution:

{{< code file="/unionai-examples/v2/user-guide/task-programming/human-in-the-loop/hitl.py" fragment="setup" lang="python" >}}

## Automated task

An automated task runs first and produces a result that requires human review:

{{< code file="/unionai-examples/v2/user-guide/task-programming/human-in-the-loop/hitl.py" fragment="automated-task" lang="python" >}}

## Requesting human input

Use `hitl.new_event()` to pause and wait for a human response. The `prompt` is shown on the web form. The `data_type` controls what type the submitted value is converted to before being returned:

{{< code file="/unionai-examples/v2/user-guide/task-programming/human-in-the-loop/hitl.py" fragment="hitl-event" lang="python" >}}

When this task runs, Flyte:

1. Serves the HITL web app (if not already running)
2. Creates an event and writes a pending request to object storage
3. Displays a link to the web form in the task report
4. Polls for a response using durable sleep
5. Returns the submitted value once input is received

## Wiring it together

The main task orchestrates the automated step and the HITL gate:

{{< code file="/unionai-examples/v2/user-guide/task-programming/human-in-the-loop/hitl.py" fragment="main" lang="python" >}}

## Event options

`hitl.new_event()` accepts the following parameters:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | — | Descriptive name shown in logs and the UI |
| `data_type` | `type` | — | Expected input type: `int`, `float`, `str`, or `bool` |
| `scope` | `str` | `"run"` | Scope of the event. Currently only `"run"` is supported |
| `prompt` | `str` | `"Please provide a value"` | Message shown on the web form |
| `timeout_seconds` | `int` | `3600` | Maximum time to wait before raising `TimeoutError` |
| `poll_interval_seconds` | `int` | `5` | How often to check for a response |

## Submitting input programmatically

In addition to the web form, input can be submitted via the event's JSON API endpoint. This is useful for automated testing or integration with external approval systems:

```bash
curl -X POST https://<hitl-app-endpoint>/submit/json \
  -H "Content-Type: application/json" \
  -d '{
    "request_id": "<request_id>",
    "response_path": "<response_path>",
    "value": "true",
    "data_type": "bool"
  }'
```

The `request_id` and `response_path` are shown in the task report alongside the form URL.
