---
title: External conditions
weight: 18
variants: +flyte +union
---

# External conditions

An **external condition** is a first-class action that pauses a running task until an external
signal arrives — a human approval, a callback from an external service, or a value supplied at
runtime. The paused action stays observable, resumable, and governable like any other action, so
you no longer need polling loops or side processes to wait on something the workflow can't produce
itself.

`flyte.new_condition(...)` registers a condition action and returns a handle; `await handle.wait()`
blocks the task until the condition is signaled and returns the typed payload.

## Supported types

A condition declares a `data_type`, which determines what a signal must supply and what `wait()`
returns:

| `data_type` | `wait()` returns | A signal value of |
|---|---|---|
| `bool` (default) | `True` / `False` | `true` / `false` |
| `int` | Python `int` | an integer literal |
| `float` | Python `float` | a decimal literal |
| `str` | Python `str` | any string |

## Example: human approval

A typed approval gate with a timeout — the most common use case:

```python
from datetime import timedelta
import flyte

env = flyte.TaskEnvironment("approvals")

@env.task
async def etl_pipeline():
    staged = await transform()

    approval = await flyte.new_condition(
        "prod_write_approval",
        prompt="Approve writing staged data to production?",
        data_type=bool,
        timeout=timedelta(hours=24),
    )
    if not await approval.wait():
        raise RuntimeError("Pipeline rejected by reviewer")

    await write_to_prod(staged)
```

The task pauses at `await approval.wait()` until someone signals the condition (see
[Signaling a condition](#signaling-a-condition)). If the timeout elapses with no signal, `wait()`
raises `flyte.errors.ConditionTimedoutError`.

## Example: string input at runtime

A condition can collect a typed value — not just a yes/no — and feed it back into the workflow.
Here the task waits for a free-form string before continuing:

```python
import flyte

env = flyte.TaskEnvironment("conditions")

@env.task
async def deploy_with_reason():
    reason = await flyte.new_condition(
        "deploy_reason",
        prompt="Enter a deployment reason to continue:",
        data_type=str,
    )
    note: str = await reason.wait()
    # `note` now holds the string a human supplied — use it downstream.
    await record_audit(note)
```

## Parameters

`flyte.new_condition(name, *, prompt, prompt_type, data_type, description, timeout)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `name` | `str` | required | Identifier for the condition within the parent action. Address it via the CLI / remote API as `<action-name>`. |
| `prompt` | `str` | `"Approve?"` | Human-readable text shown in the UI signal form. |
| `prompt_type` | `"text"` \| `"markdown"` | `"text"` | How the prompt is rendered. |
| `data_type` | `type` | `bool` | Payload type — one of `bool`, `int`, `float`, `str`. Determines what `wait()` returns and what a signal must supply. |
| `description` | `str` | `""` | Longer explanation rendered alongside the prompt. |
| `timeout` | `timedelta` \| `int` \| `float` \| `None` | `None` | Maximum wait. If it elapses with no signal, `wait()` raises `flyte.errors.ConditionTimedoutError`. |

## Signaling a condition

A condition is satisfied by delivering exactly one typed signal. Signaling is idempotent —
re-signaling an already-satisfied condition raises `flyte.errors.ConditionAlreadyExistsError`.

### From the CLI

```shell
# List the conditions on a run, optionally scoped to one parent action.
flyte get condition <run-name>
flyte get condition <run-name> <action-name>

# Signal a condition. Omit the value for an interactive typed prompt.
flyte signal condition <run-name> <action-name> true
```

The value is coerced to the condition's declared `data_type` (`true`/`false` for `bool`, integer
literals for `int`, decimal literals for `float`, any string for `str`).

### From Python (remote)

```python
import flyte.remote

condition = flyte.remote.Condition.get(
    "prod_write_approval",
    run_name="deploy-run-123",
    action_name="etl_pipeline",
)
condition.signal(True)
```

`flyte.remote.Condition.listall(run_name=...)` enumerates the conditions on a run.

## Timeout with a fallback

```python
from datetime import timedelta
import flyte
from flyte.errors import ConditionTimedoutError

@env.task
async def with_default():
    cond = await flyte.new_condition("threshold", data_type=float, timeout=timedelta(minutes=30))
    try:
        threshold = await cond.wait()
    except ConditionTimedoutError:
        threshold = 0.5   # proceed with a default if no one responds
```

## Errors

| Situation | Raised |
|---|---|
| Timeout elapses before a signal | `flyte.errors.ConditionTimedoutError` |
| Condition signaled more than once | `flyte.errors.ConditionAlreadyExistsError` |
| Condition fails during execution | `flyte.errors.ConditionFailedError` |
| Signal value doesn't match `data_type` | `TypeError` (client-side, before any call) |
| `wait()` called outside a task context | `RuntimeError` |
