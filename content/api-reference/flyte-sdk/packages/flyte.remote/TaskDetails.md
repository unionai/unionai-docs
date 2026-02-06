---
title: TaskDetails
version: 2.0.0b54
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskDetails

**Package:** `flyte.remote`

```python
class TaskDetails(
    pb2: task_definition_pb2.TaskDetails,
    max_inline_io_bytes: int,
    overriden_queue: Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `task_definition_pb2.TaskDetails` | |
| `max_inline_io_bytes` | `int` | |
| `overriden_queue` | `Optional[str]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `cache` | `None` | The cache policy of the task. |
| `default_input_args` | `None` | The default input arguments of the task. |
| `interface` | `None` | The interface of the task. |
| `name` | `None` | The name of the task. |
| `queue` | `None` | Get the queue name to use for task execution, if overridden. |
| `required_args` | `None` | The required input arguments of the task. |
| `resources` | `None` | Get the resource requests and limits for the task as a tuple (requests, limits). |
| `secrets` | `None` | Get the list of secret keys required by the task. |
| `task_type` | `None` | The type of the task. |
| `version` | `None` | The version of the task. |

## Methods

| Method | Description |
|-|-|
| [`fetch()`](#fetch) |  |
| [`get()`](#get) | Get a task by its ID or name. |
| [`override()`](#override) | Create a new TaskDetails with overridden properties. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### fetch()

```python
def fetch(
    name: str,
    project: str | None,
    domain: str | None,
    version: str | None,
    auto_version: AutoVersioning | None,
) -> TaskDetails
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |
| `version` | `str \| None` | |
| `auto_version` | `AutoVersioning \| None` | |

### get()

```python
def get(
    name: str,
    project: str | None,
    domain: str | None,
    version: str | None,
    auto_version: AutoVersioning | None,
) -> LazyEntity
```
Get a task by its ID or name. If both are provided, the ID will take precedence.

Either version or auto_version are required parameters.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the task. |
| `project` | `str \| None` | The project of the task. |
| `domain` | `str \| None` | The domain of the task. |
| `version` | `str \| None` | The version of the task. |
| `auto_version` | `AutoVersioning \| None` | If set to "latest", the latest-by-time ordered from now, version of the task will be used. If set to "current", the version will be derived from the callee tasks context. This is useful if you are deploying all environments with the same version. If auto_version is current, you can only access the task from within a task context. |

### override()

```python
def override(
    short_name: Optional[str],
    resources: Optional[flyte.Resources],
    retries: Union[int, flyte.RetryStrategy],
    timeout: Optional[flyte.TimeoutType],
    env_vars: Optional[Dict[str, str]],
    secrets: Optional[flyte.SecretRequest],
    max_inline_io_bytes: Optional[int],
    cache: Optional[flyte.Cache],
    queue: Optional[str],
    kwargs: **kwargs,
) -> TaskDetails
```
Create a new TaskDetails with overridden properties.



| Parameter | Type | Description |
|-|-|-|
| `short_name` | `Optional[str]` | Optional short name for the task. |
| `resources` | `Optional[flyte.Resources]` | Optional resource requirements. |
| `retries` | `Union[int, flyte.RetryStrategy]` | Number of retries or retry strategy. |
| `timeout` | `Optional[flyte.TimeoutType]` | Execution timeout. |
| `env_vars` | `Optional[Dict[str, str]]` | Environment variables to set. |
| `secrets` | `Optional[flyte.SecretRequest]` | Secret requests for the task. |
| `max_inline_io_bytes` | `Optional[int]` | Maximum inline I/O size in bytes. |
| `cache` | `Optional[flyte.Cache]` | Cache configuration. |
| `queue` | `Optional[str]` | Queue name for task execution. :return: A new TaskDetails instance with the overrides applied. |
| `kwargs` | `**kwargs` | |

### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


