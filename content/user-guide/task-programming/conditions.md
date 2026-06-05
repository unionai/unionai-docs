---
title: Conditions
weight: 18
variants: +flyte +union
---

# Conditions

A **condition** (surfaced in the UI as an *event*) is a first-class action that pauses a running task
until an external signal arrives — a human approval, a callback from an external service, or a value
supplied at runtime. The paused action stays observable, resumable, and governable like any other
action, so you no longer need polling loops or side processes to wait on something the workflow can't
produce itself.

> Conditions and events are the same thing: `flyte.new_event(...)` creates a condition action, and the
> UI and CLI refer to it as an *event*.

> **Looking for the FastAPI approval-app pattern?** This page covers the core `flyte.new_event` API
> built into the SDK. The separate `flyteplugins-hitl` package offers a different approach that serves
> a web form for submitting input — see [Human-in-the-loop]({{< ref "human-in-the-loop" >}}).

## Minimal example

A typed human approval with a timeout:

```python
from datetime import timedelta
import flyte

env = flyte.TaskEnvironment("approvals")

@env.task
async def etl_pipeline():
    staged = await transform()

    approval = await flyte.new_event(
        "prod_write_approval",
        prompt="Approve writing staged data to production?",
        data_type=bool,
        timeout=timedelta(hours=24),
    )
    if not await approval.wait():
        raise RuntimeError("Pipeline rejected by reviewer")

    await write_to_prod(staged)
```

`flyte.new_event(...)` registers the condition and returns an event handle; `await handle.wait()` blocks
the task until the condition is signaled and returns the typed payload.

## Parameters

`flyte.new_event(name, *, prompt, prompt_type, data_type, description, timeout, webhook)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `name` | `str` | required | Identifier for the condition within the parent action. Address it via the CLI / remote API as `<parent-action>.<name>`. |
| `prompt` | `str` | `"Approve?"` | Human-readable text shown in the UI signal form. |
| `prompt_type` | `"text"` \| `"markdown"` | `"text"` | How the prompt is rendered. |
| `data_type` | `type` | `bool` | Payload type — one of `bool`, `int`, `float`, `str`. Determines what `wait()` returns and what a signal must supply. |
| `description` | `str` | `""` | Longer explanation rendered alongside the prompt. |
| `timeout` | `timedelta` \| `int` \| `float` \| `None` | `None` | Maximum wait. If it elapses with no signal, `wait()` raises `flyte.errors.EventTimedoutError`. |
| `webhook` | `flyte.EventWebhook` \| `None` | `None` | Optional outbound HTTP call fired when the condition is created (see below). |

## Signaling a condition

A condition is satisfied by delivering exactly one typed signal. Signaling is idempotent — re-signaling
an already-satisfied condition raises `flyte.errors.EventAlreadyExistsError`.

### From the CLI

```shell
# List the conditions (events) on a run, optionally scoped to one parent action.
flyte get event <run-name>
flyte get event <run-name> <parent-action>

# Signal a condition. Omit the value for an interactive typed prompt.
flyte signal event <run-name> <parent-action.condition-name> true
```

The value is coerced to the condition's declared `data_type` (`true`/`false` for `bool`, integer
literals for `int`, decimal literals for `float`, any string for `str`).

### From Python (remote)

```python
import flyte.remote

event = flyte.remote.Event.get(
    "prod_write_approval",
    run_name="deploy-run-123",
    action_name="etl_pipeline",
)
event.signal(True)
```

`flyte.remote.Event.listall(run_name=...)` enumerates the conditions on a run.

## Webhook callbacks

Attach a `flyte.EventWebhook` to notify an external system when the condition is created. The signal
endpoint is substituted for the `{callback_uri}` template variable anywhere it appears in the payload,
so an external caller can signal the condition without SDK credentials:

```python
approval = await flyte.new_event(
    "prod_write_approval",
    prompt="Approve in Slack",
    data_type=bool,
    webhook=flyte.EventWebhook(
        url="https://hooks.example.com/approvals",
        payload={"callback_uri": "{callback_uri}", "text": "Approve prod write?"},
    ),
)
```

## Timeout with a fallback

```python
from datetime import timedelta
import flyte
from flyte.errors import EventTimedoutError

@env.task
async def with_default():
    ev = await flyte.new_event("threshold", data_type=float, timeout=timedelta(minutes=30))
    try:
        threshold = await ev.wait()
    except EventTimedoutError:
        threshold = 0.5   # proceed with a default if no one responds
```

## Errors

| Situation | Raised |
|---|---|
| Timeout elapses before a signal | `flyte.errors.EventTimedoutError` |
| Condition signaled more than once | `flyte.errors.EventAlreadyExistsError` |
| Signal value doesn't match `data_type` | `TypeError` (client-side, before any call) |
| `wait()` called outside a task context | `RuntimeError` |
