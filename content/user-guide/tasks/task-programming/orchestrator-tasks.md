---
title: Orchestrator tasks
description: Run driver tasks that only call other tasks without a pod of their own, so they start in milliseconds and hold no compute while they wait.
icon: diagram-2
weight: 12
variants: -flyte +union
---

# Orchestrator tasks

Most pipelines have a driver: a task that calls other tasks, waits for their results, and decides
what to do next. Take a training pipeline written as a regular task:

```python
import flyte

env = flyte.TaskEnvironment(name="training")

@env.task
async def train_pipeline(dataset: str) -> str:
    features = await prepare(dataset)      # 20 minutes
    model = await train(features)          # 4 hours
    return await evaluate(model)           # 10 minutes
```

`train_pipeline` does almost no work itself, but it runs in its own pod for the full four and a half
hours, holding that pod's CPU and memory while it waits for `prepare`, `train`, and `evaluate`. The
same function written as an orchestrator task has no pod at all:

```python
import flyte.orchestrator

@flyte.orchestrator.task
def train_pipeline(dataset: str) -> str:
    features = prepare(dataset)
    model = train(features)
    return evaluate(model)
```

Union runs the body of an orchestrator task in a small sandbox on a shared worker instead of in a
container. When the function calls a task, it is suspended until the result comes back. The tasks
it calls run as ordinary tasks, in their own containers, with their own resources.

> [!NOTE] Union only
> Orchestrator tasks are available in Union only. Install the latest `flyte` SDK to use them:
> `pip install -U flyte`.

## Why use orchestrator tasks

- **No busy waiting.** A regular driver task sits in a pod doing nothing while its children run.
  A suspended orchestrator holds no container, CPU, memory or quota until a result comes back.
- **Fast starts.** There is no pod to schedule and no image to pull, so an orchestrator starts in
  milliseconds rather than seconds. This matters for short control logic and for agent loops that
  take many quick steps, where container start-up would otherwise dominate.
- **Lower cost.** You stop paying for drivers that are only waiting. The saving grows with the
  number of drivers you run at once and how long each one waits.
- **No deadlocks from resource starvation.** When many regular drivers start together, they can
  fill the cluster or the project's quota, leaving no room for the child tasks they are waiting on.
  Nothing finishes. Orchestrators do not take up task pod resources, so they cannot starve their own
  children.

An orchestrator is still a task. Each call it makes is a child action, recorded, retried and shown
in the UI like any other.

## When not to use orchestrator tasks

The function runs in a [Monty](https://github.com/pydantic/monty) sandbox, Pydantic's restricted
Python interpreter, inside a micro sandbox that many orchestrators share. That makes it fast and
cheap, and it also sets clear limits. Use a regular `@env.task` instead when:

- **The driver needs libraries.** An orchestrator cannot import your dependencies, read files or
  make network calls. Only a small part of the standard library, such as `asyncio` and `datetime`,
  is available. If the driver logic depends on packages, or on code whose behavior you need to reason
  about with its dependencies, keep it in a regular task.
- **The driver reads or converts large data.** Every value that passes between the orchestrator
  and its tasks is converted at the sandbox boundary, and each orchestrator has a fixed memory limit
  (256 MiB by default). Pass references such as `flyte.io.File`, `flyte.io.Dir` and dataframes
  through the orchestrator, and do the reading, parsing and transforming inside tasks.

## Write an orchestrator task

Decorate a function with `@flyte.orchestrator.task`. Inside it you can use loops, conditions,
`try`/`except` and plain values, and call tasks without `await`:

```python
import flyte
import flyte.orchestrator
import flyte.remote

add = flyte.remote.Task.get("math.add", auto_version="latest")
multiply = flyte.remote.Task.get("math.multiply", auto_version="latest")

@flyte.orchestrator.task
def sum_of_squares(numbers: list[int]) -> int:
    total = 0
    for n in numbers:
        total = add(total, multiply(n, n))
    return total

if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(sum_of_squares, numbers=[1, 2, 3])
    print(run.url)
```

The orchestrator finds the tasks it calls in the module's globals. They can be:

- **Remote tasks**, fetched with `flyte.remote.Task.get()`. Nothing is built, so the run is
  submitted straight away. See [Remote tasks](./remote-tasks).
- **Local tasks** defined with `@env.task` in your code. Their image and code bundle are built when
  you run the orchestrator, as for any `flyte.run`, and their specs travel with it. Nothing has to be
  deployed first.
- **Other orchestrator tasks.** Each call is a separate child action. Define an orchestrator before
  any orchestrator that calls it.

You can mix the kinds in one function:

```python
import flyte
import flyte.orchestrator
import flyte.remote

env = flyte.TaskEnvironment(name="shapes")

@env.task
def square(x: int) -> int:
    return x * x

@env.task
def describe(label: str, value: int) -> str:
    return f"{label} = {value}"

add = flyte.remote.Task.get("math.add", auto_version="latest")

@flyte.orchestrator.task
def mixed_pipeline(x: int, y: int) -> str:
    total = add(square(x), square(y))
    return describe("sum of squares", total)
```

### Run tasks in parallel

Write the orchestrator as `async def` to run several tasks at once. Task calls then return
awaitables, as in any async task, and `asyncio.gather` waits for all of them:

```python
import asyncio

import flyte.orchestrator
import flyte.remote

summarize = flyte.remote.Task.get("docs.summarize", auto_version="latest")

@flyte.orchestrator.task
async def review(docs: list[str]) -> list[str]:
    return await asyncio.gather(*[summarize(doc=d) for d in docs])
```

### Handle task failures

A task that fails raises an error inside the orchestrator, where you can catch it. The orchestrator
runs without the SDK's exception classes, so catch the built-in exception:

```python
check = flyte.remote.Task.get("math.fail_if_negative", auto_version="latest")

@flyte.orchestrator.task
def tolerant(x: int) -> str:
    try:
        return "ok " + str(check(x))
    except RuntimeError as e:
        return "recovered: " + str(e)
```

### Wait for a person

An orchestrator can pause until someone approves a step or supplies a value from the UI or the
API, using `flyte.new_condition` and the condition's `wait()`, without `await`. While it waits,
nothing runs and no pod is held, whether that is for an hour or a week:

```python
@flyte.orchestrator.task
def deploy(model: str) -> str:
    report = evaluate(model)
    approval = flyte.new_condition(
        "approve",
        prompt=f"Deploy {model}? {report}",
        timeout=24 * 60 * 60,
    )
    if approval.wait():
        return publish(model)
    return "rejected"
```

A condition's `data_type` can be `bool`, `int`, `float` or `str`, and `timeout` is in seconds or a
`timedelta`. Only the function's source is shipped, so import `timedelta` inside the function if you
use it. Webhooks are not supported in orchestrator tasks.

If a condition is not signaled in time, `wait()` raises `TimeoutError`. If it fails or is aborted,
`wait()` raises `RuntimeError`. See [External conditions](./conditions) for how to signal a condition.

## Values inside an orchestrator

Values pass between the orchestrator and its tasks as they do between tasks, but the orchestrator
can only look inside some of them:

| Value | Inside the orchestrator |
|-------|-------------------------|
| `None`, `bool`, `int`, `float`, `str`, and lists and string-keyed dicts of them | Readable and writable |
| `File` and `Dir` | A named tuple of `path`, `name`, `format` and `hash`. The fields are readable, but the contents cannot be opened. |
| Dataframes, dataclasses, Pydantic models (including volumes) | Opaque. The orchestrator can pass them on, return them, or keep them in a list or dict, but cannot read their fields. |

To read the contents of a file or a dataframe, call a task.

## Settings and limits

`@flyte.orchestrator.task` takes these arguments:

| Argument | Default | Description |
|----------|---------|-------------|
| `name` | `<module>.<function>` | Task name. |
| `queue` | The run's queue | Queue to run on. The tasks the orchestrator calls run on the same queue. |
| `timeout_ms` | `30000` | Time the function may spend executing. Time spent waiting for tasks or conditions does not count. |
| `max_stack_depth` | `256` | Maximum recursion depth. |
| `cache` | `"disable"` | Cache policy for the orchestrator itself. The tasks it calls keep their own cache settings. |
| `retries` | `0` | Retries for the orchestrator itself. |

```python
@flyte.orchestrator.task(timeout_ms=5_000, retries=2, queue="critical")
def pipeline(x: int) -> int:
    ...
```

The worker also applies limits that you cannot set on the decorator:

- **Memory:** 256 MiB per orchestrator. Going over it fails the run with `MemoryError`.
- **Task calls:** 10,000 per run. Going over it fails the run with `TooManyTaskCalls`, which the
  function cannot catch.
- **Value nesting:** values passed to tasks can be nested at most 32 levels deep.
- **Error messages:** kept to their first 10 KiB.

Hitting a limit is a user error, so the run is not retried.

## Orchestrators that need a container

`@flyte.orchestrator.task` may call only tasks and conditions. If the driver also needs
[traces](./traces) or durable operations such as `flyte.durable.sleep`, use `env.orchestrator.task`
on a `TaskEnvironment`. It runs the same restricted Python, but inside a container built from the
environment's image, so it starts like a regular task and holds a pod:

```python
env = flyte.TaskEnvironment(name="pipelines")

@env.orchestrator.task
def pipeline(n: int) -> int:
    ...
```

`env.orchestrator.task` also accepts code as a string, for orchestration logic generated at runtime,
for example by an LLM:

```python
pipeline = env.orchestrator.task(
    "add(x, y) * 2",
    tasks=[add],
    inputs={"x": int, "y": int},
    output=int,
)
```

The last expression in the string is the return value. For more on running generated code, see
[Workflow sandboxing](../../agents/sandboxing/workflow-sandboxing-flyte).
