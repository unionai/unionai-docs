---
title: flyteplugins.hitl
version: 2.0.7
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# flyteplugins.hitl

Human-in-the-Loop (HITL) plugin for Flyte.

This plugin provides an event-based API for pausing workflows and waiting for human input.

## Basic usage:

```python
import flyte
import flyteplugins.hitl as hitl

task_env = flyte.TaskEnvironment(
    name="my-hitl-workflow",
    image=flyte.Image.from_debian_base(python_version=(3, 12)),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    depends_on=[hitl.env],
)


@task_env.task(report=True)
async def main() -> int:
    # Create an event (this serves the app if not already running)
    event = await hitl.new_event.aio(
        "integer_input_event",
        data_type=int,
        scope="run",
        prompt="What should I add to x?",
    )
    y = await event.wait.aio()
    return y
```

## Features:

- Event-based API for human-in-the-loop workflows
- Web form for human input
- Programmatic API for automated input
- Support for int, float, str, and bool data types
- Crash-resilient polling with object storage

## Directory

### Classes

| Class | Description |
|-|-|
| [`Event`](../flyteplugins.hitl/event) | An event that waits for human input via an embedded FastAPI app. |

### Methods

| Method | Description |
|-|-|
| [`new_event()`](#new_event) | Create a new human-in-the-loop event. |


### Variables

| Property | Type | Description |
|-|-|-|
| `env` | `TaskEnvironment` |  |

## Methods

#### new_event()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await new_event.aio()`.
```python
def new_event(
    name: str,
    data_type: Type[T],
    scope: EventScope,
    prompt: str,
    timeout_seconds: int,
    poll_interval_seconds: int,
) -> Event[T]
```
Create a new human-in-the-loop event.

This is a convenience function that wraps Event.create().



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | A descriptive name for the event (used in logs and UI) |
| `data_type` | `Type[T]` | The expected type of the input (int, float, str, bool) |
| `scope` | `EventScope` | The scope of the event. Currently only "run" is supported. |
| `prompt` | `str` | The prompt to display to the human |
| `timeout_seconds` | `int` | |
| `poll_interval_seconds` | `int` | |

