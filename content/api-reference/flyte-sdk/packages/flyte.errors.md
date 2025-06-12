---
title: flyte.errors
version: 0.2.0b10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.errors


Exceptions raised by Union.

These errors are raised when the underlying task execution fails, either because of a user error, system error or an
unknown error.

## Directory

### Errors

| Exception | Description |
|-|-|
| [`ActionNotFoundError`](.././flyte.errors#flyteerrorsactionnotfounderror) | This error is raised when the user tries to access an action that does not exist. |
| [`BaseRuntimeError`](.././flyte.errors#flyteerrorsbaseruntimeerror) | Base class for all Union runtime errors. |
| [`CustomError`](.././flyte.errors#flyteerrorscustomerror) | This error is raised when the user raises a custom error. |
| [`ImagePullBackOffError`](.././flyte.errors#flyteerrorsimagepullbackofferror) | This error is raised when the image cannot be pulled. |
| [`InitializationError`](.././flyte.errors#flyteerrorsinitializationerror) | This error is raised when the Union system is tried to access without being initialized. |
| [`InvalidImageNameError`](.././flyte.errors#flyteerrorsinvalidimagenameerror) | This error is raised when the image name is invalid. |
| [`LogsNotYetAvailableError`](.././flyte.errors#flyteerrorslogsnotyetavailableerror) | This error is raised when the logs are not yet available for a task. |
| [`NotInTaskContextError`](.././flyte.errors#flyteerrorsnotintaskcontexterror) | This error is raised when the user tries to access the task context outside of a task. |
| [`OOMError`](.././flyte.errors#flyteerrorsoomerror) | This error is raised when the underlying task execution fails because of an out-of-memory error. |
| [`PrimaryContainerNotFoundError`](.././flyte.errors#flyteerrorsprimarycontainernotfounderror) | This error is raised when the primary container is not found. |
| [`ReferenceTaskError`](.././flyte.errors#flyteerrorsreferencetaskerror) | This error is raised when the user tries to access a task that does not exist. |
| [`RetriesExhaustedError`](.././flyte.errors#flyteerrorsretriesexhaustederror) | This error is raised when the underlying task execution fails after all retries have been exhausted. |
| [`RuntimeSystemError`](.././flyte.errors#flyteerrorsruntimesystemerror) | This error is raised when the underlying task execution fails because of a system error. |
| [`RuntimeUnknownError`](.././flyte.errors#flyteerrorsruntimeunknownerror) | This error is raised when the underlying task execution fails because of an unknown error. |
| [`RuntimeUserError`](.././flyte.errors#flyteerrorsruntimeusererror) | This error is raised when the underlying task execution fails because of an error in the user's code. |
| [`TaskInterruptedError`](.././flyte.errors#flyteerrorstaskinterruptederror) | This error is raised when the underlying task execution is interrupted. |
| [`TaskTimeoutError`](.././flyte.errors#flyteerrorstasktimeouterror) | This error is raised when the underlying task execution runs for longer than the specified timeout. |
| [`UnionRpcError`](.././flyte.errors#flyteerrorsunionrpcerror) | This error is raised when communication with the Union server fails. |

## flyte.errors.ActionNotFoundError

This error is raised when the user tries to access an action that does not exist.


## flyte.errors.BaseRuntimeError

Base class for all Union runtime errors. These errors are raised when the underlying task execution fails, either
because of a user error, system error or an unknown error.


```python
class BaseRuntimeError(
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

## flyte.errors.CustomError

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

## flyte.errors.ImagePullBackOffError

This error is raised when the image cannot be pulled.


```python
class ImagePullBackOffError(
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

## flyte.errors.InitializationError

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

## flyte.errors.InvalidImageNameError

This error is raised when the image name is invalid.


```python
class InvalidImageNameError(
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

## flyte.errors.LogsNotYetAvailableError

This error is raised when the logs are not yet available for a task.


```python
class LogsNotYetAvailableError(
    message: str,
)
```
| Parameter | Type |
|-|-|
| `message` | `str` |

## flyte.errors.NotInTaskContextError

This error is raised when the user tries to access the task context outside of a task.


```python
class NotInTaskContextError(
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

## flyte.errors.OOMError

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

## flyte.errors.PrimaryContainerNotFoundError

This error is raised when the primary container is not found.


```python
class PrimaryContainerNotFoundError(
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

## flyte.errors.ReferenceTaskError

This error is raised when the user tries to access a task that does not exist.


```python
class ReferenceTaskError(
    message: str,
)
```
| Parameter | Type |
|-|-|
| `message` | `str` |

## flyte.errors.RetriesExhaustedError

This error is raised when the underlying task execution fails after all retries have been exhausted.


```python
class RetriesExhaustedError(
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

## flyte.errors.RuntimeSystemError

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

## flyte.errors.RuntimeUnknownError

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

## flyte.errors.RuntimeUserError

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

## flyte.errors.TaskInterruptedError

This error is raised when the underlying task execution is interrupted.


```python
class TaskInterruptedError(
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

## flyte.errors.TaskTimeoutError

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

## flyte.errors.UnionRpcError

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

