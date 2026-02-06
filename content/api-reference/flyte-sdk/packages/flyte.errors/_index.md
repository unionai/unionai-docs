---
title: flyte.errors
version: 2.0.0b54
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.errors


Exceptions raised by Union.

These errors are raised when the underlying task execution fails, either because of a user error, system error or an
unknown error.

## Directory

### Errors

| Exception | Description |
|-|-|
| [`ActionAbortedError`](../flyte.errors/actionabortederror) | This error is raised when an action was aborted, externally. |
| [`ActionNotFoundError`](../flyte.errors/actionnotfounderror) | This error is raised when the user tries to access an action that does not exist. |
| [`BaseRuntimeError`](../flyte.errors/baseruntimeerror) | Base class for all Union runtime errors. |
| [`CodeBundleError`](../flyte.errors/codebundleerror) | This error is raised when the code bundle cannot be created, for example when no files are found to bundle. |
| [`CustomError`](../flyte.errors/customerror) | This error is raised when the user raises a custom error. |
| [`DeploymentError`](../flyte.errors/deploymenterror) | This error is raised when the deployment of a task fails, or some preconditions for deployment are not met. |
| [`ImageBuildError`](../flyte.errors/imagebuilderror) | This error is raised when the image build fails. |
| [`ImagePullBackOffError`](../flyte.errors/imagepullbackofferror) | This error is raised when the image cannot be pulled. |
| [`InitializationError`](../flyte.errors/initializationerror) | This error is raised when the Union system is tried to access without being initialized. |
| [`InlineIOMaxBytesBreached`](../flyte.errors/inlineiomaxbytesbreached) | This error is raised when the inline IO max bytes limit is breached. |
| [`InvalidImageNameError`](../flyte.errors/invalidimagenameerror) | This error is raised when the image name is invalid. |
| [`LogsNotYetAvailableError`](../flyte.errors/logsnotyetavailableerror) | This error is raised when the logs are not yet available for a task. |
| [`ModuleLoadError`](../flyte.errors/moduleloaderror) | This error is raised when the module cannot be loaded, either because it does not exist or because of a. |
| [`NotInTaskContextError`](../flyte.errors/notintaskcontexterror) | This error is raised when the user tries to access the task context outside of a task. |
| [`OOMError`](../flyte.errors/oomerror) | This error is raised when the underlying task execution fails because of an out-of-memory error. |
| [`OnlyAsyncIOSupportedError`](../flyte.errors/onlyasynciosupportederror) | This error is raised when the user tries to use sync IO in an async task. |
| [`ParameterMaterializationError`](../flyte.errors/parametermaterializationerror) | This error is raised when the user tries to use a Parameter in an App, that has delayed Materialization,. |
| [`PrimaryContainerNotFoundError`](../flyte.errors/primarycontainernotfounderror) | This error is raised when the primary container is not found. |
| [`RemoteTaskNotFoundError`](../flyte.errors/remotetasknotfounderror) | This error is raised when the user tries to access a task that does not exist. |
| [`RemoteTaskUsageError`](../flyte.errors/remotetaskusageerror) | This error is raised when the user tries to access a task that does not exist. |
| [`RestrictedTypeError`](../flyte.errors/restrictedtypeerror) | This error is raised when the user uses a restricted type, for example current a Tuple is not supported for one. |
| [`RetriesExhaustedError`](../flyte.errors/retriesexhaustederror) | This error is raised when the underlying task execution fails after all retries have been exhausted. |
| [`RuntimeDataValidationError`](../flyte.errors/runtimedatavalidationerror) | This error is raised when the user tries to access a resource that does not exist or is invalid. |
| [`RuntimeSystemError`](../flyte.errors/runtimesystemerror) | This error is raised when the underlying task execution fails because of a system error. |
| [`RuntimeUnknownError`](../flyte.errors/runtimeunknownerror) | This error is raised when the underlying task execution fails because of an unknown error. |
| [`RuntimeUserError`](../flyte.errors/runtimeusererror) | This error is raised when the underlying task execution fails because of an error in the user's code. |
| [`SlowDownError`](../flyte.errors/slowdownerror) | This error is raised when the user tries to access a resource that does not exist or is invalid. |
| [`TaskInterruptedError`](../flyte.errors/taskinterruptederror) | This error is raised when the underlying task execution is interrupted. |
| [`TaskTimeoutError`](../flyte.errors/tasktimeouterror) | This error is raised when the underlying task execution runs for longer than the specified timeout. |
| [`UnionRpcError`](../flyte.errors/unionrpcerror) | This error is raised when communication with the Union server fails. |

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


| Parameter | Type | Description |
|-|-|-|
| `loop` |  | |
| `context` |  | |

