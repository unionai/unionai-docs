---
title: RunOutput
version: 2.1.2
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# RunOutput

**Package:** `flyte.app`

Use a run's output for app parameters.

This enables the declaration of an app parameter dependency on the output of
a run, given by a specific run name, or a task name and version. If
`task_auto_version == 'latest'`, the latest version of the task will be used.
If `task_auto_version == 'current'`, the version will be derived from the callee
app or task context. To get the latest task run for ephemeral task runs, set
`task_version` and `task_auto_version` should both be set to `None` (which is the default).

Get the output of a specific run:

```python
run_output = RunOutput(type="directory", run_name="my-run-123")
```

Get the latest output of an ephemeral task run:

```python
run_output = RunOutput(type="file", task_name="env.my_task")
```

Get the latest output of a deployed task run:

```python
run_output = RunOutput(type="file", task_name="env.my_task", task_auto_version="latest")
```

Get the output of a specific task run:

```python
run_output = RunOutput(type="file", task_name="env.my_task", task_version="xyz")
```


## Parameters

```python
class RunOutput(
    type: typing.Literal['string', 'file', 'directory', 'app_endpoint'],
    run_name: str | None,
    task_name: str | None,
    task_version: str | None,
    task_auto_version: typing.Optional[typing.Literal['latest', 'current']],
    getter: tuple[typing.Any, ...],
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `type` | `typing.Literal['string', 'file', 'directory', 'app_endpoint']` | |
| `run_name` | `str \| None` | |
| `task_name` | `str \| None` | |
| `task_version` | `str \| None` | |
| `task_auto_version` | `typing.Optional[typing.Literal['latest', 'current']]` | |
| `getter` | `tuple[typing.Any, ...]` | |

## Methods

| Method | Description |
|-|-|
| [`check_type()`](#check_type) |  |
| [`get()`](#get) |  |
| [`materialize()`](#materialize) |  |


### check_type()

```python
def check_type(
    data: typing.Any,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `data` | `typing.Any` | |

### get()

```python
def get()
```
### materialize()

```python
def materialize()
```
