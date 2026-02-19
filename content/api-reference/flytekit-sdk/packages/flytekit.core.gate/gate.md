---
title: Gate
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Gate

**Package:** `flytekit.core.gate`

A node type that waits for user input before proceeding with a workflow.
A gate is a type of node that behaves like a task, but instead of running code, it either needs to wait
for user input to proceed or wait for a timer to complete running.



```python
class Gate(
    name: str,
    input_type: typing.Optional[typing.Type],
    upstream_item: typing.Optional[typing.Any],
    sleep_duration: typing.Optional[datetime.timedelta],
    timeout: typing.Optional[datetime.timedelta],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `input_type` | `typing.Optional[typing.Type]` | |
| `upstream_item` | `typing.Optional[typing.Any]` | |
| `sleep_duration` | `typing.Optional[datetime.timedelta]` | |
| `timeout` | `typing.Optional[datetime.timedelta]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `input_type` | `None` |  |
| `literal_type` | `None` |  |
| `name` | `None` |  |
| `python_interface` | `None` | This will not be valid during local execution Part of SupportsNodeCreation interface |
| `sleep_duration` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


### construct_node_metadata()

```python
def construct_node_metadata()
```
### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
) -> Union[Tuple[Promise], Promise, VoidPromise]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `kwargs` | `**kwargs` | |

### local_execution_mode()

```python
def local_execution_mode()
```
