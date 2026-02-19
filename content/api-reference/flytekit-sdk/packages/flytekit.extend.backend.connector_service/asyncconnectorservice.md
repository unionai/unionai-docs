---
title: AsyncConnectorService
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# AsyncConnectorService

**Package:** `flytekit.extend.backend.connector_service`

## Methods

| Method | Description |
|-|-|
| [`CreateTask()`](#createtask) |  |
| [`DeleteTask()`](#deletetask) |  |
| [`GetTask()`](#gettask) |  |
| [`GetTaskLogs()`](#gettasklogs) | GetTaskLogs returns task execution logs, if available. |
| [`GetTaskMetrics()`](#gettaskmetrics) | GetTaskMetrics returns one or more task execution metrics, if available. |


### CreateTask()

```python
def CreateTask(
    request: typing.Union[flyteidl.admin.agent_pb2.CreateTaskRequest, flyteidl.admin.agent_pb2.GetTaskRequest, flyteidl.admin.agent_pb2.DeleteTaskRequest],
    context: grpc.ServicerContext,
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `request` | `typing.Union[flyteidl.admin.agent_pb2.CreateTaskRequest, flyteidl.admin.agent_pb2.GetTaskRequest, flyteidl.admin.agent_pb2.DeleteTaskRequest]` | |
| `context` | `grpc.ServicerContext` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### DeleteTask()

```python
def DeleteTask(
    request: typing.Union[flyteidl.admin.agent_pb2.CreateTaskRequest, flyteidl.admin.agent_pb2.GetTaskRequest, flyteidl.admin.agent_pb2.DeleteTaskRequest],
    context: grpc.ServicerContext,
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `request` | `typing.Union[flyteidl.admin.agent_pb2.CreateTaskRequest, flyteidl.admin.agent_pb2.GetTaskRequest, flyteidl.admin.agent_pb2.DeleteTaskRequest]` | |
| `context` | `grpc.ServicerContext` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### GetTask()

```python
def GetTask(
    request: typing.Union[flyteidl.admin.agent_pb2.CreateTaskRequest, flyteidl.admin.agent_pb2.GetTaskRequest, flyteidl.admin.agent_pb2.DeleteTaskRequest],
    context: grpc.ServicerContext,
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `request` | `typing.Union[flyteidl.admin.agent_pb2.CreateTaskRequest, flyteidl.admin.agent_pb2.GetTaskRequest, flyteidl.admin.agent_pb2.DeleteTaskRequest]` | |
| `context` | `grpc.ServicerContext` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### GetTaskLogs()

```python
def GetTaskLogs(
    request: flyteidl.admin.agent_pb2.GetTaskLogsRequest,
    context: grpc.ServicerContext,
) -> flyteidl.admin.agent_pb2.GetTaskLogsResponse
```
GetTaskLogs returns task execution logs, if available.
        


| Parameter | Type | Description |
|-|-|-|
| `request` | `flyteidl.admin.agent_pb2.GetTaskLogsRequest` | |
| `context` | `grpc.ServicerContext` | |

### GetTaskMetrics()

```python
def GetTaskMetrics(
    request: flyteidl.admin.agent_pb2.GetTaskMetricsRequest,
    context: grpc.ServicerContext,
) -> flyteidl.admin.agent_pb2.GetTaskMetricsResponse
```
GetTaskMetrics returns one or more task execution metrics, if available.

Errors include
* OutOfRange if metrics are not available for the specified task time range
* various other errors


| Parameter | Type | Description |
|-|-|-|
| `request` | `flyteidl.admin.agent_pb2.GetTaskMetricsRequest` | |
| `context` | `grpc.ServicerContext` | |

