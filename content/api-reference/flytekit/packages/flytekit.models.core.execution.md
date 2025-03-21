---
title: flytekit.models.core.execution
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.core.execution

## Directory

### Classes

| Class | Description |
|-|-|
| [`ExecutionError`](.././flytekit.models.core.execution#flytekitmodelscoreexecutionexecutionerror) | None. |
| [`NodeExecutionPhase`](.././flytekit.models.core.execution#flytekitmodelscoreexecutionnodeexecutionphase) | None. |
| [`TaskExecutionPhase`](.././flytekit.models.core.execution#flytekitmodelscoreexecutiontaskexecutionphase) | None. |
| [`TaskLog`](.././flytekit.models.core.execution#flytekitmodelscoreexecutiontasklog) | None. |
| [`WorkflowExecutionPhase`](.././flytekit.models.core.execution#flytekitmodelscoreexecutionworkflowexecutionphase) | This class holds enum values used for setting notifications. |

## flytekit.models.core.execution.ExecutionError

```python
def ExecutionError(
    code: str,
    message: str,
    error_uri: str,
    kind: int,
):
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
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
):
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
| code |  |  |
| error_uri |  |  |
| is_empty |  |  |
| kind |  |  |
| message |  |  |

## flytekit.models.core.execution.NodeExecutionPhase

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
):
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
):
```
| Parameter | Type |
|-|-|
| `int_value` |  |

## flytekit.models.core.execution.TaskLog

```python
def TaskLog(
    uri: str,
    name: str,
    message_format: typing.Optional[flytekit.models.core.execution.TaskLog.MessageFormat],
    ttl: typing.Optional[datetime.timedelta],
):
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
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
):
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
| is_empty |  |  |
| message_format |  |  |
| name |  |  |
| ttl |  |  |
| uri |  |  |

## flytekit.models.core.execution.WorkflowExecutionPhase

This class holds enum values used for setting notifications. See :py:class:`flytekit.Email`
for sample usage.


### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
):
```
| Parameter | Type |
|-|-|
| `int_value` |  |

