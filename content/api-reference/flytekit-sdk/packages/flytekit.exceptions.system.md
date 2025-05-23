---
title: flytekit.exceptions.system
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.exceptions.system

## Directory

### Errors

| Exception | Description |
|-|-|
| [`FlyteAgentNotFound`](.././flytekit.exceptions.system#flytekitexceptionssystemflyteagentnotfound) | Assertion failed. |
| [`FlyteConnectorNotFound`](.././flytekit.exceptions.system#flytekitexceptionssystemflyteconnectornotfound) | Assertion failed. |
| [`FlyteDownloadDataException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytedownloaddataexception) | Common base class for all non-exit exceptions. |
| [`FlyteEntrypointNotLoadable`](.././flytekit.exceptions.system#flytekitexceptionssystemflyteentrypointnotloadable) | Common base class for all non-exit exceptions. |
| [`FlyteNonRecoverableSystemException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytenonrecoverablesystemexception) | Common base class for all non-exit exceptions. |
| [`FlyteNotImplementedException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytenotimplementedexception) | Method or function hasn't been implemented yet. |
| [`FlyteSystemAssertion`](.././flytekit.exceptions.system#flytekitexceptionssystemflytesystemassertion) | Assertion failed. |
| [`FlyteSystemException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytesystemexception) | Common base class for all non-exit exceptions. |
| [`FlyteSystemUnavailableException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytesystemunavailableexception) | Common base class for all non-exit exceptions. |
| [`FlyteUploadDataException`](.././flytekit.exceptions.system#flytekitexceptionssystemflyteuploaddataexception) | Common base class for all non-exit exceptions. |

## flytekit.exceptions.system.FlyteAgentNotFound

Assertion failed.


```python
class FlyteAgentNotFound(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.system.FlyteConnectorNotFound

Assertion failed.


```python
class FlyteConnectorNotFound(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.system.FlyteDownloadDataException

Common base class for all non-exit exceptions.


```python
class FlyteDownloadDataException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.system.FlyteEntrypointNotLoadable

Common base class for all non-exit exceptions.


```python
class FlyteEntrypointNotLoadable(
    task_module,
    task_name,
    additional_msg,
)
```
| Parameter | Type |
|-|-|
| `task_module` |  |
| `task_name` |  |
| `additional_msg` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.system.FlyteNonRecoverableSystemException

Common base class for all non-exit exceptions.


```python
class FlyteNonRecoverableSystemException(
    exc_value: Exception,
)
```
FlyteNonRecoverableSystemException is thrown when a system code raises an exception.



| Parameter | Type |
|-|-|
| `exc_value` | `Exception` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |
| `value` |  |  |

## flytekit.exceptions.system.FlyteNotImplementedException

Method or function hasn't been implemented yet.


```python
class FlyteNotImplementedException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.system.FlyteSystemAssertion

Assertion failed.


```python
class FlyteSystemAssertion(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.system.FlyteSystemException

Common base class for all non-exit exceptions.


```python
class FlyteSystemException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.system.FlyteSystemUnavailableException

Common base class for all non-exit exceptions.


```python
class FlyteSystemUnavailableException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.system.FlyteUploadDataException

Common base class for all non-exit exceptions.


```python
class FlyteUploadDataException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

