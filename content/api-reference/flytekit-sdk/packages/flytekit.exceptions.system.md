---
title: flytekit.exceptions.system
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
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

