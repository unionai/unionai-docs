---
title: flytekit.models.core.errors
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
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
| Parameter | Type |
|-|-|
| `code` | `str` |
| `message` | `str` |
| `kind` | `int` |
| `origin` | `int` |
| `timestamp` | `google.protobuf.timestamp_pb2.Timestamp` |
| `worker` | `str` |

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
    proto,
) -> e: ContainerError
```
| Parameter | Type |
|-|-|
| `proto` |  |

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
:rtype: flyteidl.core.errors_pb2.ContainerError


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
| `is_empty` |  |  |
| `kind` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `message` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `origin` |  | {{< multiline >}}The origin of the error, an enum value from ExecutionError.ErrorKind
{{< /multiline >}} |
| `timestamp` |  | {{< multiline >}}The timestamp of the error, as number of seconds and nanos since Epoch
{{< /multiline >}} |
| `worker` |  | {{< multiline >}}The worker name where the error originated
{{< /multiline >}} |

## flytekit.models.core.errors.ErrorDocument

```python
class ErrorDocument(
    error,
)
```
| Parameter | Type |
|-|-|
| `error` |  |

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
    proto,
) -> e: ErrorDocument
```
| Parameter | Type |
|-|-|
| `proto` |  |

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
:rtype: flyteidl.core.errors_pb2.ErrorDocument


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `error` |  | {{< multiline >}}:rtype: ContainerError
{{< /multiline >}} |
| `is_empty` |  |  |

