---
title: flyte.errors
version: 2.0.0b33
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
| [`DeploymentError`](.././flyte.errors#flyteerrorsdeploymenterror) | This error is raised when the deployment of a task fails, or some preconditions for deployment are not met. |
| [`ImageBuildError`](.././flyte.errors#flyteerrorsimagebuilderror) | This error is raised when the image build fails. |
| [`ImagePullBackOffError`](.././flyte.errors#flyteerrorsimagepullbackofferror) | This error is raised when the image cannot be pulled. |
| [`InitializationError`](.././flyte.errors#flyteerrorsinitializationerror) | This error is raised when the Union system is tried to access without being initialized. |
| [`InlineIOMaxBytesBreached`](.././flyte.errors#flyteerrorsinlineiomaxbytesbreached) | This error is raised when the inline IO max bytes limit is breached. |
| [`InvalidImageNameError`](.././flyte.errors#flyteerrorsinvalidimagenameerror) | This error is raised when the image name is invalid. |
| [`LogsNotYetAvailableError`](.././flyte.errors#flyteerrorslogsnotyetavailableerror) | This error is raised when the logs are not yet available for a task. |
| [`ModuleLoadError`](.././flyte.errors#flyteerrorsmoduleloaderror) | This error is raised when the module cannot be loaded, either because it does not exist or because of a. |
| [`NotInTaskContextError`](.././flyte.errors#flyteerrorsnotintaskcontexterror) | This error is raised when the user tries to access the task context outside of a task. |
| [`OOMError`](.././flyte.errors#flyteerrorsoomerror) | This error is raised when the underlying task execution fails because of an out-of-memory error. |
| [`OnlyAsyncIOSupportedError`](.././flyte.errors#flyteerrorsonlyasynciosupportederror) | This error is raised when the user tries to use sync IO in an async task. |
| [`PrimaryContainerNotFoundError`](.././flyte.errors#flyteerrorsprimarycontainernotfounderror) | This error is raised when the primary container is not found. |
| [`ReferenceTaskError`](.././flyte.errors#flyteerrorsreferencetaskerror) | This error is raised when the user tries to access a task that does not exist. |
| [`RetriesExhaustedError`](.././flyte.errors#flyteerrorsretriesexhaustederror) | This error is raised when the underlying task execution fails after all retries have been exhausted. |
| [`RunAbortedError`](.././flyte.errors#flyteerrorsrunabortederror) | This error is raised when the run is aborted by the user. |
| [`RuntimeDataValidationError`](.././flyte.errors#flyteerrorsruntimedatavalidationerror) | This error is raised when the user tries to access a resource that does not exist or is invalid. |
| [`RuntimeSystemError`](.././flyte.errors#flyteerrorsruntimesystemerror) | This error is raised when the underlying task execution fails because of a system error. |
| [`RuntimeUnknownError`](.././flyte.errors#flyteerrorsruntimeunknownerror) | This error is raised when the underlying task execution fails because of an unknown error. |
| [`RuntimeUserError`](.././flyte.errors#flyteerrorsruntimeusererror) | This error is raised when the underlying task execution fails because of an error in the user's code. |
| [`SlowDownError`](.././flyte.errors#flyteerrorsslowdownerror) | This error is raised when the user tries to access a resource that does not exist or is invalid. |
| [`TaskInterruptedError`](.././flyte.errors#flyteerrorstaskinterruptederror) | This error is raised when the underlying task execution is interrupted. |
| [`TaskTimeoutError`](.././flyte.errors#flyteerrorstasktimeouterror) | This error is raised when the underlying task execution runs for longer than the specified timeout. |
| [`UnionRpcError`](.././flyte.errors#flyteerrorsunionrpcerror) | This error is raised when communication with the Union server fails. |

### Methods

| Method | Description |
|-|-|
| [`silence_grpc_polling_error()`](#silence_grpc_polling_error) | Suppress specific gRPC polling errors in the event loop. |


## Methods

#### silence_grpc_polling_error()

```python
def silence_grpc_polling_error(
    loop,
    context,
)
```
Suppress specific gRPC polling errors in the event loop.


| Parameter | Type |
|-|-|
| `loop` |  |
| `context` |  |

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

## flyte.errors.DeploymentError

This error is raised when the deployment of a task fails, or some preconditions for deployment are not met.


```python
class DeploymentError(
    message: str,
)
```
| Parameter | Type |
|-|-|
| `message` | `str` |

## flyte.errors.ImageBuildError

This error is raised when the image build fails.


```python
class ImageBuildError(
    message: str,
)
```
| Parameter | Type |
|-|-|
| `message` | `str` |

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

## flyte.errors.InlineIOMaxBytesBreached

This error is raised when the inline IO max bytes limit is breached.
This can be adjusted per task by setting max_inline_io_bytes in the task definition.


```python
class InlineIOMaxBytesBreached(
    message: str,
)
```
| Parameter | Type |
|-|-|
| `message` | `str` |

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

## flyte.errors.ModuleLoadError

This error is raised when the module cannot be loaded, either because it does not exist or because of a
 syntax error.


```python
class ModuleLoadError(
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

## flyte.errors.OnlyAsyncIOSupportedError

This error is raised when the user tries to use sync IO in an async task.


```python
class OnlyAsyncIOSupportedError(
    message: str,
)
```
| Parameter | Type |
|-|-|
| `message` | `str` |

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

## flyte.errors.RunAbortedError

This error is raised when the run is aborted by the user.


```python
class RunAbortedError(
    message: str,
)
```
| Parameter | Type |
|-|-|
| `message` | `str` |

## flyte.errors.RuntimeDataValidationError

This error is raised when the user tries to access a resource that does not exist or is invalid.


```python
class RuntimeDataValidationError(
    var: str,
    e: Exception | str,
    task_name: str,
)
```
| Parameter | Type |
|-|-|
| `var` | `str` |
| `e` | `Exception \| str` |
| `task_name` | `str` |

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

## flyte.errors.SlowDownError

This error is raised when the user tries to access a resource that does not exist or is invalid.


```python
class SlowDownError(
    message: str,
)
```
| Parameter | Type |
|-|-|
| `message` | `str` |

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
    message: str,
)
```
| Parameter | Type |
|-|-|
| `message` | `str` |

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

