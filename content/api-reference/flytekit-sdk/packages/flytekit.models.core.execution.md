---
title: flytekit.models.core.execution
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
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

```python
class ExecutionError(
    code: str,
    message: str,
    error_uri: str,
    kind: int,
)
```
| Parameter | Type |
|-|-|
| `code` | `str` |
| `message` | `str` |
| `error_uri` | `str` |
| `kind` | `int` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> e: ExecutionError
```
| Parameter | Type |
|-|-|
| `p` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.execution_pb2.ExecutionError


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `code` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `error_uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `kind` |  | {{< multiline >}}Enum value from ErrorKind
{{< /multiline >}} |
| `message` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

## flytekit.models.core.execution.NodeExecutionPhase

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
) -> e: Text
```
| Parameter | Type |
|-|-|
| `int_value` |  |

## flytekit.models.core.execution.TaskExecutionPhase

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
) -> e: Text
```
| Parameter | Type |
|-|-|
| `int_value` |  |

## flytekit.models.core.execution.TaskLog

```python
class TaskLog(
    uri: str,
    name: str,
    message_format: typing.Optional[flytekit.models.core.execution.TaskLog.MessageFormat],
    ttl: typing.Optional[datetime.timedelta],
)
```
| Parameter | Type |
|-|-|
| `uri` | `str` |
| `name` | `str` |
| `message_format` | `typing.Optional[flytekit.models.core.execution.TaskLog.MessageFormat]` |
| `ttl` | `typing.Optional[datetime.timedelta]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> e: TaskLog
```
| Parameter | Type |
|-|-|
| `p` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.execution_pb2.TaskLog


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `message_format` |  | {{< multiline >}}Enum value from TaskLog.MessageFormat
:rtype: MessageFormat
{{< /multiline >}} |
| `name` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `ttl` |  | {{< multiline >}}:rtype: datetime.timedelta
{{< /multiline >}} |
| `uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

## flytekit.models.core.execution.WorkflowExecutionPhase

This class holds enum values used for setting notifications. See {{< py_class_ref flytekit.Email >}}
for sample usage.


### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
) -> e: Text
```
| Parameter | Type |
|-|-|
| `int_value` |  |

