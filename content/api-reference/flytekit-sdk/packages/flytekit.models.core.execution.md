---
title: flytekit.models.core.execution
version: 1.16.19
variants: +flyte +union
layout: py_api
---

# flytekit.models.core.execution

## Directory

### Classes

| Class | Description |
|-|-|
| [`ExecutionError`](.././flytekit.models.core.execution#flytekitmodelscoreexecutionexecutionerror) |  |
| [`NodeExecutionPhase`](.././flytekit.models.core.execution#flytekitmodelscoreexecutionnodeexecutionphase) |  |
| [`TaskExecutionPhase`](.././flytekit.models.core.execution#flytekitmodelscoreexecutiontaskexecutionphase) |  |
| [`TaskLog`](.././flytekit.models.core.execution#flytekitmodelscoreexecutiontasklog) |  |
| [`WorkflowExecutionPhase`](.././flytekit.models.core.execution#flytekitmodelscoreexecutionworkflowexecutionphase) | This class holds enum values used for setting notifications. |

## flytekit.models.core.execution.ExecutionError

### Parameters

```python
class ExecutionError(
    code: str,
    message: str,
    error_uri: str,
    kind: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `message` | `str` | |
| `error_uri` | `str` | |
| `kind` | `int` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `code` | `None` |  |
| `error_uri` | `None` |  |
| `is_empty` | `None` |  |
| `kind` | `None` | Enum value from ErrorKind |
| `message` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

**Returns:** ExecutionError

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.execution_pb2.ExecutionError

## flytekit.models.core.execution.NodeExecutionPhase

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `int_value` |  | |

**Returns:** Text

## flytekit.models.core.execution.TaskExecutionPhase

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `int_value` |  | |

**Returns:** Text

## flytekit.models.core.execution.TaskLog

### Parameters

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

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `message_format` | `None` | Enum value from TaskLog.MessageFormat |
| `name` | `None` |  |
| `ttl` | `None` |  |
| `uri` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

**Returns:** TaskLog

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.execution_pb2.TaskLog

## flytekit.models.core.execution.WorkflowExecutionPhase

This class holds enum values used for setting notifications. See {{&lt; py_class_ref flytekit.Email &gt;}}
for sample usage.


### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `int_value` |  | |

**Returns:** Text

