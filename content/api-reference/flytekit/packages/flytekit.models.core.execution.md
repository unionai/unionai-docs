---
title: flytekit.models.core.execution
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> ExecutionError
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `code` |  |  |
| `error_uri` |  |  |
| `is_empty` |  |  |
| `kind` |  | {{< multiline >}}Enum value from ErrorKind
{{< /multiline >}} |
| `message` |  |  |

## flytekit.models.core.execution.NodeExecutionPhase

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) | . |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
) -> Text
```
| Parameter | Type |
|-|-|
| `int_value` |  |

## flytekit.models.core.execution.TaskExecutionPhase

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) | . |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
) -> Text
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> TaskLog
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `message_format` |  | {{< multiline >}}Enum value from TaskLog.MessageFormat
{{< /multiline >}} |
| `name` |  |  |
| `ttl` |  |  |
| `uri` |  |  |

## flytekit.models.core.execution.WorkflowExecutionPhase

This class holds enum values used for setting notifications. See :py:class:`flytekit.Email`
for sample usage.


### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) | . |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
) -> Text
```
| Parameter | Type |
|-|-|
| `int_value` |  |

