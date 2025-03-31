---
title: flytekit.models.core.errors
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.core.errors

## Directory

### Classes

| Class | Description |
|-|-|
| [`ContainerError`](.././flytekit.models.core.errors#flytekitmodelscoreerrorscontainererror) |  |
| [`ErrorDocument`](.././flytekit.models.core.errors#flytekitmodelscoreerrorserrordocument) |  |
| [`Timestamp`](.././flytekit.models.core.errors#flytekitmodelscoreerrorstimestamp) | A ProtocolMessage. |

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> ContainerError
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
| `is_empty` |  |  |
| `kind` |  |  |
| `message` |  |  |
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> ErrorDocument
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
| `error` |  |  |
| `is_empty` |  |  |

## flytekit.models.core.errors.Timestamp

A ProtocolMessage


### Methods

| Method | Description |
|-|-|
| [`FromDatetime()`](#fromdatetime) | Converts datetime to Timestamp. |
| [`FromJsonString()`](#fromjsonstring) | Parse a RFC 3339 date string format to Timestamp. |
| [`FromMicroseconds()`](#frommicroseconds) | Converts microseconds since epoch to Timestamp. |
| [`FromMilliseconds()`](#frommilliseconds) | Converts milliseconds since epoch to Timestamp. |
| [`FromNanoseconds()`](#fromnanoseconds) | Converts nanoseconds since epoch to Timestamp. |
| [`FromSeconds()`](#fromseconds) | Converts seconds since epoch to Timestamp. |
| [`GetCurrentTime()`](#getcurrenttime) | Get the current UTC into Timestamp. |
| [`ToDatetime()`](#todatetime) | Converts Timestamp to a datetime. |
| [`ToJsonString()`](#tojsonstring) | Converts Timestamp to RFC 3339 date string format. |
| [`ToMicroseconds()`](#tomicroseconds) | Converts Timestamp to microseconds since epoch. |
| [`ToMilliseconds()`](#tomilliseconds) | Converts Timestamp to milliseconds since epoch. |
| [`ToNanoseconds()`](#tonanoseconds) | Converts Timestamp to nanoseconds since epoch. |
| [`ToSeconds()`](#toseconds) | Converts Timestamp to seconds since epoch. |


#### FromDatetime()

```python
def FromDatetime(
    dt,
)
```
Converts datetime to Timestamp.



| Parameter | Type |
|-|-|
| `dt` |  |

#### FromJsonString()

```python
def FromJsonString(
    value,
)
```
Parse a RFC 3339 date string format to Timestamp.



| Parameter | Type |
|-|-|
| `value` |  |

#### FromMicroseconds()

```python
def FromMicroseconds(
    micros,
)
```
Converts microseconds since epoch to Timestamp.


| Parameter | Type |
|-|-|
| `micros` |  |

#### FromMilliseconds()

```python
def FromMilliseconds(
    millis,
)
```
Converts milliseconds since epoch to Timestamp.


| Parameter | Type |
|-|-|
| `millis` |  |

#### FromNanoseconds()

```python
def FromNanoseconds(
    nanos,
)
```
Converts nanoseconds since epoch to Timestamp.


| Parameter | Type |
|-|-|
| `nanos` |  |

#### FromSeconds()

```python
def FromSeconds(
    seconds,
)
```
Converts seconds since epoch to Timestamp.


| Parameter | Type |
|-|-|
| `seconds` |  |

#### GetCurrentTime()

```python
def GetCurrentTime()
```
Get the current UTC into Timestamp.


#### ToDatetime()

```python
def ToDatetime(
    tzinfo,
)
```
Converts Timestamp to a datetime.



| Parameter | Type |
|-|-|
| `tzinfo` |  |

#### ToJsonString()

```python
def ToJsonString()
```
Converts Timestamp to RFC 3339 date string format.

Returns:
A string converted from timestamp. The string is always Z-normalized
and uses 3, 6 or 9 fractional digits as required to represent the
exact time. Example of the return format: '1972-01-01T10:00:20.021Z'


#### ToMicroseconds()

```python
def ToMicroseconds()
```
Converts Timestamp to microseconds since epoch.


#### ToMilliseconds()

```python
def ToMilliseconds()
```
Converts Timestamp to milliseconds since epoch.


#### ToNanoseconds()

```python
def ToNanoseconds()
```
Converts Timestamp to nanoseconds since epoch.


#### ToSeconds()

```python
def ToSeconds()
```
Converts Timestamp to seconds since epoch.


