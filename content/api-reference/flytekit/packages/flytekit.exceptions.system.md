---
title: flytekit.exceptions.system
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.exceptions.system

## Directory

### Classes

No classes in this package.

### Errors

* [`FlyteAgentNotFound`](.././flytekit.exceptions.system#flytekitexceptionssystemflyteagentnotfound)
* [`FlyteDownloadDataException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytedownloaddataexception)
* [`FlyteEntrypointNotLoadable`](.././flytekit.exceptions.system#flytekitexceptionssystemflyteentrypointnotloadable)
* [`FlyteException`](.././flytekit.exceptions.system#flytekitexceptionssystemflyteexception)
* [`FlyteNonRecoverableSystemException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytenonrecoverablesystemexception)
* [`FlyteNotImplementedException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytenotimplementedexception)
* [`FlyteSystemAssertion`](.././flytekit.exceptions.system#flytekitexceptionssystemflytesystemassertion)
* [`FlyteSystemException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytesystemexception)
* [`FlyteSystemUnavailableException`](.././flytekit.exceptions.system#flytekitexceptionssystemflytesystemunavailableexception)
* [`FlyteUploadDataException`](.././flytekit.exceptions.system#flytekitexceptionssystemflyteuploaddataexception)

## flytekit.exceptions.system.FlyteAgentNotFound

Assertion failed.


```python
def FlyteAgentNotFound(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.system.FlyteDownloadDataException

Common base class for all non-exit exceptions.


```python
def FlyteDownloadDataException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.system.FlyteEntrypointNotLoadable

Common base class for all non-exit exceptions.


```python
def FlyteEntrypointNotLoadable(
    task_module,
    task_name,
    additional_msg,
):
```
| Parameter | Type |
|-|-|
| `task_module` |  |
| `task_name` |  |
| `additional_msg` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.system.FlyteException

Common base class for all non-exit exceptions.


```python
def FlyteException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.system.FlyteNonRecoverableSystemException

Common base class for all non-exit exceptions.


```python
def FlyteNonRecoverableSystemException(
    exc_value: Exception,
):
```
FlyteNonRecoverableSystemException is thrown when a system code raises an exception.



| Parameter | Type |
|-|-|
| `exc_value` | `Exception` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |
| value |  |  |

## flytekit.exceptions.system.FlyteNotImplementedException

Method or function hasn't been implemented yet.


```python
def FlyteNotImplementedException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.system.FlyteSystemAssertion

Assertion failed.


```python
def FlyteSystemAssertion(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.system.FlyteSystemException

Common base class for all non-exit exceptions.


```python
def FlyteSystemException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.system.FlyteSystemUnavailableException

Common base class for all non-exit exceptions.


```python
def FlyteSystemUnavailableException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.system.FlyteUploadDataException

Common base class for all non-exit exceptions.


```python
def FlyteUploadDataException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

