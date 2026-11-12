---
title: flyte.orchestrator
description: "Tasks that orchestrate other tasks."
icon: box-seam
version: 2.13.2
variants: +flyte +union
layout: py_api
---

# flyte.orchestrator

Tasks that orchestrate other tasks.

`@flyte.orchestrator.task` turns a function that only calls other tasks into a
task that Flyte runs without a pod of its own, so it takes up none of the task
pod resources a regular task does. The tasks it calls run as usual.

```python
import flyte
import flyte.orchestrator
import flyte.remote

add = flyte.remote.Task.get("math.add", auto_version="latest")
multiply = flyte.remote.Task.get("math.multiply", auto_version="latest")


@flyte.orchestrator.task
def pipeline(x: int, y: int) -> int:
    return multiply(add(x, y), 2)


run = flyte.run(pipeline, x=3, y=4)
```

It may only call tasks. For an orchestrator that also calls traces or durable
operations, use `env.orchestrator.task` on a `flyte.TaskEnvironment`, which runs
in the environment's image.
## Directory

### Classes

| Class | Description |
|-|-|
| [`OrchestratorTaskTemplate`](../flyte.orchestrator/orchestratortasktemplate) | An orchestrator task whose source is shipped in the task template. |

### Methods

| Method | Description |
|-|-|
| [`task()`](#task) | Turn a function that only calls other tasks into an orchestrator task. |


## Methods

#### task()

```python
def task(
    name: Optional[str] = None,
    queue: Optional[str] = None,
    timeout_ms: int = 30000,
    max_stack_depth: int = 256,
    cache: CacheRequest = 'disable',
    retries: int = 0,
) -> Union[OrchestratorTaskTemplate, Callable[[Callable], OrchestratorTaskTemplate]]
```
Turn a function that only calls other tasks into an orchestrator task.

The function's source is shipped in the task template and executed by a
sandbox leaseworker, so the orchestrator itself starts without a pod:

```python
add = flyte.remote.Task.get("math.add", auto_version="latest")

@flyte.orchestrator.task
def pipeline(x: int, y: int) -> int:
    return add(add(x, y), 1)

run = flyte.run(pipeline, x=1, y=2)
```

Tasks are discovered from the function's globals; call them without
`await`. They can be:

- remote references (`flyte.remote.Task.get`). Nothing is built, so the run
  is submitted straight away.
- tasks defined locally with `@env.task`. Their image and code bundle are
  built when the orchestrator is run, as for any `flyte.run`, and their
  specs travel in the orchestrator's template.

Values pass between the orchestrator and its tasks as they would between
tasks, but the orchestrator itself can only look into plain data (None,
bool, int, float, str, and lists and str-keyed dicts of them) and files
and directories. A `File` or `Dir` is a named tuple of its `path`, `name`,
`format` and `hash`. A dataframe, Pydantic model or dataclass, such as a
`Volume`, is opaque: the orchestrator can pass it on, return it, or keep it
in a list or dict, but not read its fields. Nothing can be opened or read
from storage inside the orchestrator; call a task for that.

It can also wait for a value someone supplies from the UI or the API, with
`flyte.new_condition` and the condition's `wait()`, again without `await`.
While it waits, nothing runs and no pod is held:

```python
@flyte.orchestrator.task
def deploy(model: str) -> str:
    report = evaluate(model)
    approval = flyte.new_condition("approve", prompt=f"Deploy {model}? {report}", timeout=86_400)
    if approval.wait():
        return publish(model)
    return "rejected"
```

`data_type` is one of bool, int, float and str, and `timeout` is in seconds
or a `timedelta`, imported inside the function since only its source is
shipped. Webhooks are not supported here.

A condition that is not signalled in time raises
`flyte.errors.ConditionTimedoutError` from `wait()`, and one that fails or
is aborted raises `flyte.errors.ConditionFailedError` or
`flyte.errors.ActionAbortedError`. The orchestrator runs without the SDK's
exception classes, so inside it these are the builtins `TimeoutError`,
`RuntimeError` and `RuntimeError`: `except
flyte.errors.ConditionTimedoutError` catches only timeouts, but `except
RuntimeError` does not catch them.

An exception the orchestrator does not catch fails its attempt, and
`retries` applies, as for any task. To fail without retrying, raise
`flyte.errors.NonRecoverableError`, again as in any task:

```python
@flyte.orchestrator.task(retries=3)
def checked(x: int) -> int:
    if x < 0:
        raise flyte.errors.NonRecoverableError(f"{x} is negative")
    return add(x, 1)
```

Inside the orchestrator it is a `RuntimeError`, so `except RuntimeError`
catches it. It takes only a message.



| Parameter | Type | Description |
|-|-|-|
| `name` | `Optional[str]` | Task name. Defaults to `<module>.<function>`. |
| `queue` | `Optional[str]` | Queue to run on, as for any task. Defaults to the run's queue. The scheduler picks a sandbox leaseworker on the queue's clusters by the task type, and the tasks the orchestrator calls run on the same queue. |
| `timeout_ms` | `int` | Time the source may spend executing, and separately the total it may sleep. Time spent waiting for tasks is not counted. |
| `max_stack_depth` | `int` | Maximum recursion depth of the source. |
| `cache` | `CacheRequest` | Cache policy for the orchestrator itself. |
| `retries` | `int` | Number of retries for the orchestrator itself. |

