---
title: flytekit.models.core.errors
version: 1.16.16
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# flytekit.models.core.errors

## Directory

### Classes

| Class | Description |
|-|-|
| [`ContainerError`](.././flytekit.models.core.errors#flytekitmodelscoreerrorscontainererror) |  |
| [`ErrorDocument`](.././flytekit.models.core.errors#flytekitmodelscoreerrorserrordocument) |  |

## flytekit.models.core.errors.ContainerError

### Parameters

```python
class ContainerError(
    code: str,
    message: str,
    kind: int,
    origin: int,
    timestamp: google.protobuf.timestamp_pb2.Timestamp,
    worker: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | A succinct code about the error |
| `message` | `str` | Whatever message you want to surface about the error |
| `kind` | `int` | A value from the ContainerError.Kind enum. |
| `origin` | `int` | A value from ExecutionError.ErrorKind. Don't confuse this with error kind, even though both are called kind. |
| `timestamp` | `google.protobuf.timestamp_pb2.Timestamp` | |
| `worker` | `str` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `code` | `None` |  |
| `is_empty` | `None` |  |
| `kind` | `None` |  |
| `message` | `None` |  |
| `origin` | `None` | The origin of the error, an enum value from ExecutionError.ErrorKind |
| `timestamp` | `None` | The timestamp of the error, as number of seconds and nanos since Epoch |
| `worker` | `None` | The worker name where the error originated |

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
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

**Returns:** ContainerError

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
**Returns:** flyteidl.core.errors_pb2.ContainerError

## flytekit.models.core.errors.ErrorDocument

### Parameters

```python
class ErrorDocument(
    error,
)
```
| Parameter | Type | Description |
|-|-|-|
| `error` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `error` | `None` |  |
| `is_empty` | `None` |  |

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
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

**Returns:** ErrorDocument

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
**Returns:** flyteidl.core.errors_pb2.ErrorDocument

