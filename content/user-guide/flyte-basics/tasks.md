---
title: Tasks
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Tasks

A task is a Python function that runs remotely in a container. You create tasks by decorating functions with `@env.task`.

## Defining a task

Here's a simple task:

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

The `@env.task` decorator tells Flyte to run this function in a container configured by `env`.

## Type hints are required

Flyte uses type hints to understand your data and serialize it between tasks:

```python
@env.task
def process_numbers(values: list[int]) -> int:
    return sum(values)
```

Supported types include:
- Primitives: `int`, `float`, `str`, `bool`
- Collections: `list`, `dict`, `tuple`
- DataFrames: `pandas.DataFrame`, `polars.DataFrame`
- Files: `flyte.File`, `flyte.Directory`
- Custom: dataclasses, Pydantic models

See [Data classes and structures](../task-programming/dataclasses-and-structures) for complex types.

## Tasks calling tasks

In Flyte 2, tasks can call other tasks directly. The called task runs in its own container:

```python
@env.task
def fetch_data(url: str) -> dict:
    # Runs in container 1
    ...

@env.task
def process_data(url: str) -> str:
    data = fetch_data(url)  # Calls fetch_data, runs in container 2
    return transform(data)
```

This is how you build workflows in Flyte 2. There's no separate `@workflow` decorator - just tasks calling tasks.

## The top-level task

The task you execute directly is the "top-level" or "driver" task. It orchestrates other tasks:

```python
@env.task
def step_one(x: int) -> int:
    return x * 2

@env.task
def step_two(x: int) -> int:
    return x + 10

@env.task
def pipeline(x: int) -> int:
    a = step_one(x)   # Run step_one
    b = step_two(a)   # Run step_two with result
    return b
```

When you run `pipeline`, it becomes the top-level task and orchestrates `step_one` and `step_two`.

## Workflows without the decorator

If you're familiar with Flyte 1, you might remember the `@workflow` decorator. In Flyte 2, workflows are just Python code:

```python
# Flyte 2: Pure Python
@env.task
def my_workflow(input: str) -> str:
    result_a = task_a(input)
    result_b = task_b(result_a)
    return result_b
```

The structure of your workflow is defined by how your tasks call each other, not by a special decorator.

## Running tasks locally

For quick testing, you can call a task like a regular function:

```python
# Direct call - runs locally, not in a container
result = greet("World")
print(result)  # "Hello, World!"
```

This bypasses Flyte entirely and is useful for debugging logic. However, local calls don't track data, use remote resources, or benefit from Flyte's features.

## Running tasks remotely

To run a task on your Flyte backend:

```python
import flyte

flyte.init_from_config()
result = flyte.run(greet, name="World")
print(result)  # "Hello, World!"
```

Or from the command line:

```shell
flyte run my_script.py greet --name World
```

This sends your code to the Flyte backend, runs it in a container, and returns the result.

## Next steps

Now that you can define and run tasks, let's understand how Flyte tracks executions with [runs and actions](./runs-and-actions).
