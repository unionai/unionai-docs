---
title: flytekit.exceptions.system
version: 1.16.16
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# flytekit.exceptions.system

## Directory

### Errors

| Exception | Description |
|-|-|
| [`FlyteAgentNotFound`](.././flytekit.exceptions.system#flytekitexceptionssystemflyteagentnotfound) |  |
| [`FlyteConnectorNotFound`](.././flytekit.exceptions.system#flytekitexceptionssystemflyteconnectornotfound) |  |
| [`FlyteDownloadDataException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytedownloaddataexception) |  |
| [`FlyteEntrypointNotLoadable`](.././flytekit.exceptions.system#flytekitexceptionssystemflyteentrypointnotloadable) |  |
| [`FlyteNonRecoverableSystemException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytenonrecoverablesystemexception) |  |
| [`FlyteNotImplementedException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytenotimplementedexception) |  |
| [`FlyteSystemAssertion`](.././flytekit.exceptions.system#flytekitexceptionssystemflytesystemassertion) |  |
| [`FlyteSystemException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytesystemexception) |  |
| [`FlyteSystemUnavailableException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytesystemunavailableexception) |  |
| [`FlyteUploadDataException`](.././flytekit.exceptions.system#flytekitexceptionssystemflyteuploaddataexception) |  |

## flytekit.exceptions.system.FlyteAgentNotFound

### Parameters

```python
class FlyteAgentNotFound(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.system.FlyteConnectorNotFound

### Parameters

```python
class FlyteConnectorNotFound(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.system.FlyteDownloadDataException

### Parameters

```python
class FlyteDownloadDataException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.system.FlyteEntrypointNotLoadable

### Parameters

```python
class FlyteEntrypointNotLoadable(
    task_module,
    task_name,
    additional_msg,
)
```
| Parameter | Type | Description |
|-|-|-|
| `task_module` |  | |
| `task_name` |  | |
| `additional_msg` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.system.FlyteNonRecoverableSystemException

### Parameters

```python
class FlyteNonRecoverableSystemException(
    exc_value: Exception,
)
```
FlyteNonRecoverableSystemException is thrown when a system code raises an exception.



| Parameter | Type | Description |
|-|-|-|
| `exc_value` | `Exception` | The exception that was raised from system code. |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |
| `value` | `None` |  |

## flytekit.exceptions.system.FlyteNotImplementedException

### Parameters

```python
class FlyteNotImplementedException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.system.FlyteSystemAssertion

### Parameters

```python
class FlyteSystemAssertion(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.system.FlyteSystemException

### Parameters

```python
class FlyteSystemException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.system.FlyteSystemUnavailableException

### Parameters

```python
class FlyteSystemUnavailableException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.system.FlyteUploadDataException

### Parameters

```python
class FlyteUploadDataException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |

