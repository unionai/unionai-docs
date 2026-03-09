---
title: Additional task settings
weight: 11
variants: +flyte +byoc +selfmanaged
---

# Additional task settings

This page covers task configuration parameters that do not have their own dedicated page:
naming and metadata, environment variables, and inline I/O thresholds.

For the full list of all task configuration parameters, see [Configure tasks](./_index).

## Naming and metadata

### `name`

The `name` parameter on `TaskEnvironment` is required.
It is combined with each task function name to form the fully-qualified task name.
For example, if you define a `TaskEnvironment` with `name="my_env"` and a task function `my_task`,
the fully-qualified task name is `my_env.my_task`.

The `name` must use `snake_case` or `kebab-case` and is immutable once set.

### `short_name`

The `short_name` parameter on `@env.task` (and `override()`) overrides the display name of a task in the UI graph view.
By default, the display name is the Python function name.
Overriding `short_name` does not change the fully-qualified task name.

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task(short_name="Train Model")
def train(data: list) -> dict:
    return {"accuracy": 0.95}
```

### `description`

The `description` parameter on `TaskEnvironment` provides a description of the task environment (max 255 characters).
It is used for organizational purposes and can be viewed in the UI.

### `docs`

The `docs` parameter on `@env.task` accepts a `Documentation` object.
If not set explicitly, the documentation is auto-extracted from the task function's docstring.

```python
import flyte
from flyte import Documentation

env = flyte.TaskEnvironment(name="my_env")

@env.task(docs=Documentation(description="Trains a model on the given dataset."))
def train(data: list) -> dict:
    """This docstring is used if docs is not set explicitly."""
    return {"accuracy": 0.95}
```

### `report`

The `report` parameter on `@env.task` controls whether an HTML report is generated for the task.
See [Reports](../task-programming/reports) for details.

### `links`

The `links` parameter on `@env.task` (and `override()`) attaches clickable URLs to tasks in the UI.
Use links to connect tasks to external tools like experiment trackers, monitoring dashboards, or logging systems.

Links are defined by implementing the [`Link`](../../api-reference/flyte-sdk/packages/flyte/link) protocol.
See [Links](../task-programming/links) for full details on creating and using links.

## Environment variables

The `env_vars` parameter on `TaskEnvironment` injects plain-text environment variables into the task container.
It accepts a `Dict[str, str]`.

```python
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    env_vars={
        "LOG_LEVEL": "DEBUG",
        "API_ENDPOINT": "https://api.example.com",
    },
)

@env.task
def my_task() -> str:
    import os
    return os.environ["API_ENDPOINT"]
```

Environment variables can be overridden at the `task.override()` invocation level
(unless `reusable` is in effect).

Use `env_vars` for non-sensitive configuration values.
For sensitive values like API keys and credentials, use [`secrets`](./secrets) instead.

## Inline I/O threshold

The `max_inline_io_bytes` parameter on `@env.task` (and `override()`) controls the maximum
size for data passed directly in the task request and response
(e.g., primitives, strings, dictionaries).

Data exceeding this threshold raises an `InlineIOMaxBytesBreached` error.

The default value is 10 MiB (`10 * 1024 * 1024` bytes).

This setting does **not** affect [`flyte.io.File`, `flyte.io.Dir`](../task-programming/files-and-directories),
or [`flyte.DataFrame`](../task-programming/dataclasses-and-structures),
which are always offloaded to object storage regardless of size.

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

# Allow up to 50 MiB of inline data
@env.task(max_inline_io_bytes=50 * 1024 * 1024)
def process_large_dict(data: dict) -> dict:
    return {k: v * 2 for k, v in data.items()}
```
