---
title: TaskLog
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskLog

**Package:** `flytekit.models.core.execution`

```python
class TaskLog(
    uri: str,
    name: str,
    message_format: typing.Optional[flytekit.models.core.execution.TaskLog.MessageFormat],
    ttl: typing.Optional[datetime.timedelta],
)
```
| Parameter | Type | Description |
|-|-|-|
| `uri` | `str` | |
| `name` | `str` | |
| `message_format` | `typing.Optional[flytekit.models.core.execution.TaskLog.MessageFormat]` | |
| `ttl` | `typing.Optional[datetime.timedelta]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `message_format` | `None` | Enum value from TaskLog.MessageFormat :rtype: MessageFormat |
| `name` | `None` | :rtype: Text |
| `ttl` | `None` | :rtype: datetime.timedelta |
| `uri` | `None` | :rtype: Text |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.execution_pb2.TaskLog


