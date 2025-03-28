---
title: union.errors
version: 0.1.0
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# union.errors


Exceptions raised by Union.

These errors are raised when the underlying task execution fails, either because of a user error, system error or an
unknown error.

## Directory

### Errors

| Exception | Description |
|-|-|
| [`CustomError`](.././union.errors#unionerrorscustomerror) | This error is raised when the user raises a custom error. |
| [`InitializationError`](.././union.errors#unionerrorsinitializationerror) | This error is raised when the Union system is tried to access without being initialized. |
| [`OOMError`](.././union.errors#unionerrorsoomerror) | This error is raised when the underlying task execution fails because of an out-of-memory error. |
| [`RuntimeError`](.././union.errors#unionerrorsruntimeerror) | Base class for all Union runtime errors. |
| [`RuntimeSystemError`](.././union.errors#unionerrorsruntimesystemerror) | This error is raised when the underlying task execution fails because of a system error. |
| [`RuntimeUnknownError`](.././union.errors#unionerrorsruntimeunknownerror) | This error is raised when the underlying task execution fails because of an unknown error. |
| [`RuntimeUserError`](.././union.errors#unionerrorsruntimeusererror) | This error is raised when the underlying task execution fails because of an error in the user's code. |
| [`TaskTimeoutError`](.././union.errors#unionerrorstasktimeouterror) | This error is raised when the underlying task execution runs for longer than the specified timeout. |
| [`UnionRpcError`](.././union.errors#unionerrorsunionrpcerror) | This error is raised when communication with the Union server fails. |

## union.errors.CustomError

This error is raised when the user raises a custom error.


```python
class CustomError(
    code: str,
    message: str,
)
```
| Parameter | Type |
|-|-|
| `code` | `str` |
| `message` | `str` |

### Methods

| Method | Description |
|-|-|
| [`from_exception()`](#from_exception) | Create a CustomError from an exception. |


#### from_exception()

```python
def from_exception(
    e: Exception,
)
```
Create a CustomError from an exception. The exception's class name is used as the error code and the exception
message is used as the error message.


| Parameter | Type |
|-|-|
| `e` | `Exception` |

## union.errors.InitializationError

This error is raised when the Union system is tried to access without being initialized.


```python
class InitializationError(
    code: str,
    kind: typing.Literal['system', 'unknown', 'user'],
    root_cause_message: str,
    worker: str | None,
)
```
| Parameter | Type |
|-|-|
| `code` | `str` |
| `kind` | `typing.Literal['system', 'unknown', 'user']` |
| `root_cause_message` | `str` |
| `worker` | `str \| None` |

## union.errors.OOMError

This error is raised when the underlying task execution fails because of an out-of-memory error.


```python
class OOMError(
    code: str,
    message: str,
    worker: str | None,
)
```
| Parameter | Type |
|-|-|
| `code` | `str` |
| `message` | `str` |
| `worker` | `str \| None` |

## union.errors.RuntimeError

Base class for all Union runtime errors. These errors are raised when the underlying task execution fails, either
because of a user error, system error or an unknown error.


```python
class RuntimeError(
    code: str,
    kind: typing.Literal['system', 'unknown', 'user'],
    root_cause_message: str,
    worker: str | None,
)
```
| Parameter | Type |
|-|-|
| `code` | `str` |
| `kind` | `typing.Literal['system', 'unknown', 'user']` |
| `root_cause_message` | `str` |
| `worker` | `str \| None` |

## union.errors.RuntimeSystemError

This error is raised when the underlying task execution fails because of a system error. This could be a bug in the
Union system or a bug in the user's code.


```python
class RuntimeSystemError(
    code: str,
    message: str,
    worker: str | None,
)
```
| Parameter | Type |
|-|-|
| `code` | `str` |
| `message` | `str` |
| `worker` | `str \| None` |

## union.errors.RuntimeUnknownError

This error is raised when the underlying task execution fails because of an unknown error.


```python
class RuntimeUnknownError(
    code: str,
    message: str,
    worker: str | None,
)
```
| Parameter | Type |
|-|-|
| `code` | `str` |
| `message` | `str` |
| `worker` | `str \| None` |

## union.errors.RuntimeUserError

This error is raised when the underlying task execution fails because of an error in the user's code.


```python
class RuntimeUserError(
    code: str,
    message: str,
    worker: str | None,
)
```
| Parameter | Type |
|-|-|
| `code` | `str` |
| `message` | `str` |
| `worker` | `str \| None` |

## union.errors.TaskTimeoutError

This error is raised when the underlying task execution runs for longer than the specified timeout.


```python
class TaskTimeoutError(
    code: str,
    message: str,
    worker: str | None,
)
```
| Parameter | Type |
|-|-|
| `code` | `str` |
| `message` | `str` |
| `worker` | `str \| None` |

## union.errors.UnionRpcError

This error is raised when communication with the Union server fails.


```python
class UnionRpcError(
    code: str,
    message: str,
    worker: str | None,
)
```
| Parameter | Type |
|-|-|
| `code` | `str` |
| `message` | `str` |
| `worker` | `str \| None` |

