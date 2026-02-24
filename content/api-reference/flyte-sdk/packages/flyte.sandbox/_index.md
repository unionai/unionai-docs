---
title: flyte.sandbox
version: 2.0.1
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.sandbox

Sandboxed tasks powered by Monty (Pydantic's Rust-based sandboxed Python interpreter).

.. warning:: Experimental feature: alpha — APIs may change without notice.

Sandboxed tasks are:
- **Side-effect free**: No filesystem, network, or OS access
- **Super fast**: Microsecond startup for pure Python
- **Multiplexable**: Many tasks run safely on the same Python process

Usage::

    import flyte
    import flyte.sandbox

    # Environment-based approach (preferred for ``flyte run``)
    env = flyte.TaskEnvironment(name="my-env")

    @env.sandbox.orchestrator
    def my_orchestrator(x: int, y: int) -> int:
        return add(x, y)

    # Create a reusable task from a code string
    pipeline = flyte.sandbox.orchestrator_from_str(
        "add(x, y) * 2",
        inputs={"x": int, "y": int},
        output=int,
        tasks=[add],
    )

    # One-shot execution of a code string (local only)
    result = await flyte.sandbox.orchestrate_local(
        "x + y",
        inputs={"x": 1, "y": 2},
    )

## Directory

### Classes

| Class | Description |
|-|-|
| [`CodeTaskTemplate`](../flyte.sandbox/codetasktemplate) | A sandboxed task created from a code string rather than a decorated function. |
| [`SandboxedConfig`](../flyte.sandbox/sandboxedconfig) | Configuration for a sandboxed task executed via Monty. |
| [`SandboxedTaskTemplate`](../flyte.sandbox/sandboxedtasktemplate) | A task template that executes the function body in a Monty sandbox. |

### Methods

| Method | Description |
|-|-|
| [`orchestrate_local()`](#orchestrate_local) | One-shot local execution of a code string in the Monty sandbox. |
| [`orchestrator_from_str()`](#orchestrator_from_str) | Create a reusable sandboxed task from a code string. |


### Variables

| Property | Type | Description |
|-|-|-|
| `ORCHESTRATOR_SYNTAX_PROMPT` | `str` |  |

## Methods

#### orchestrate_local()

```python
def orchestrate_local(
    source: str,
    inputs: Dict[str, Any],
    tasks: Optional[List[Any]],
    timeout_ms: int,
) -> Any
```
One-shot local execution of a code string in the Monty sandbox.

.. warning:: Experimental feature: alpha — APIs may change without notice.

Sends the code + inputs to Monty and returns the result directly,
without creating a ``TaskTemplate`` or going through the controller.

The **last expression** in *source* becomes the return value::

    result = await sandbox.orchestrate_local(
        "add(x, y) * 2",
        inputs={"x": 1, "y": 2},
        tasks=[add],
    )
    # → 6

Parameters
----------
source:
    Python code string to execute in the sandbox.
inputs:
    Mapping of input names to their values.
tasks:
    List of external functions (tasks, durable ops) available inside the
    sandbox. Each item's ``__name__`` is used as the key.
timeout_ms:
    Sandbox execution timeout in milliseconds.


| Parameter | Type | Description |
|-|-|-|
| `source` | `str` | |
| `inputs` | `Dict[str, Any]` | |
| `tasks` | `Optional[List[Any]]` | |
| `timeout_ms` | `int` | |

#### orchestrator_from_str()

```python
def orchestrator_from_str(
    source: str,
    inputs: Dict[str, type],
    output: type,
    tasks: Optional[List[Any]],
    name: str,
    timeout_ms: int,
    cache: CacheRequest,
    retries: int,
    image: Optional[Any],
) -> CodeTaskTemplate
```
Create a reusable sandboxed task from a code string.

.. warning:: Experimental feature: alpha — APIs may change without notice.

The returned ``CodeTaskTemplate`` can be passed to ``flyte.run()``
just like a decorated task.

The **last expression** in *source* becomes the return value::

    pipeline = sandbox.orchestrator_from_str(
        "add(x, y) * 2",
        inputs={"x": int, "y": int},
        output=int,
        tasks=[add],
    )
    result = flyte.run(pipeline, x=1, y=2)  # → 6

Parameters
----------
source:
    Python code string to execute in the sandbox.
inputs:
    Mapping of input names to their types.
output:
    The return type (default ``NoneType``).
tasks:
    List of external functions (tasks, durable ops) available inside the
    sandbox. Each item's ``__name__`` is used as the key.
name:
    Task name (default ``"sandboxed-code"``).
timeout_ms:
    Sandbox execution timeout in milliseconds.
cache:
    Cache policy for the task.
retries:
    Number of retries on failure.
image:
    Docker image to use. If not provided, a default Debian image with
    ``pydantic-monty`` is created automatically.


| Parameter | Type | Description |
|-|-|-|
| `source` | `str` | |
| `inputs` | `Dict[str, type]` | |
| `output` | `type` | |
| `tasks` | `Optional[List[Any]]` | |
| `name` | `str` | |
| `timeout_ms` | `int` | |
| `cache` | `CacheRequest` | |
| `retries` | `int` | |
| `image` | `Optional[Any]` | |

