---
title: flytekit.extend.backend.connector_service
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extend.backend.connector_service

## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncConnectorService`](.././flytekit.extend.backend.connector_service#flytekitextendbackendconnector_serviceasyncconnectorservice) | AsyncAgentService defines an RPC Service that allows propeller to send the request to the agent server asynchronously. |
| [`ConnectorMetadataService`](.././flytekit.extend.backend.connector_service#flytekitextendbackendconnector_serviceconnectormetadataservice) | AgentMetadataService defines an RPC service that is also served over HTTP via grpc-gateway. |
| [`SyncConnectorService`](.././flytekit.extend.backend.connector_service#flytekitextendbackendconnector_servicesyncconnectorservice) | SyncAgentService defines an RPC Service that allows propeller to send the request to the agent server synchronously. |

### Methods

| Method | Description |
|-|-|
| [`record_connector_metrics()`](#record_connector_metrics) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `create_operation` | `str` |  |
| `delete_operation` | `str` |  |
| `do_operation` | `str` |  |
| `get_operation` | `str` |  |
| `metric_prefix` | `str` |  |

## Methods

#### record_connector_metrics()

```python
def record_connector_metrics(
    func: typing.Callable,
)
```
| Parameter | Type | Description |
|-|-|-|
| `func` | `typing.Callable` | |

## flytekit.extend.backend.connector_service.AsyncConnectorService

AsyncAgentService defines an RPC Service that allows propeller to send the request to the agent server asynchronously.
    


### Methods

| Method | Description |
|-|-|
| [`CreateTask()`](#createtask) |  |
| [`DeleteTask()`](#deletetask) |  |
| [`GetTask()`](#gettask) |  |
| [`GetTaskLogs()`](#gettasklogs) | GetTaskLogs returns task execution logs, if available. |
| [`GetTaskMetrics()`](#gettaskmetrics) | GetTaskMetrics returns one or more task execution metrics, if available. |


#### CreateTask()

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

#### DeleteTask()

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

#### GetTask()

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

#### GetTaskLogs()

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

#### GetTaskMetrics()

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

## flytekit.extend.backend.connector_service.ConnectorMetadataService

AgentMetadataService defines an RPC service that is also served over HTTP via grpc-gateway.
This service allows propeller or users to get the metadata of agents.


### Methods

| Method | Description |
|-|-|
| [`GetAgent()`](#getagent) | Fetch a :ref:`ref_flyteidl. |
| [`ListAgents()`](#listagents) | Fetch a list of :ref:`ref_flyteidl. |


#### GetAgent()

```python
def GetAgent(
    request: flyteidl.admin.agent_pb2.GetAgentRequest,
    context: grpc.ServicerContext,
) -> flyteidl.admin.agent_pb2.GetAgentResponse
```
Fetch a :ref:`ref_flyteidl.admin.Agent` definition.
        


| Parameter | Type | Description |
|-|-|-|
| `request` | `flyteidl.admin.agent_pb2.GetAgentRequest` | |
| `context` | `grpc.ServicerContext` | |

#### ListAgents()

```python
def ListAgents(
    request: flyteidl.admin.agent_pb2.ListAgentsRequest,
    context: grpc.ServicerContext,
) -> flyteidl.admin.agent_pb2.ListAgentsResponse
```
Fetch a list of :ref:`ref_flyteidl.admin.Agent` definitions.
        


| Parameter | Type | Description |
|-|-|-|
| `request` | `flyteidl.admin.agent_pb2.ListAgentsRequest` | |
| `context` | `grpc.ServicerContext` | |

## flytekit.extend.backend.connector_service.SyncConnectorService

SyncAgentService defines an RPC Service that allows propeller to send the request to the agent server synchronously.
    


### Methods

| Method | Description |
|-|-|
| [`ExecuteTaskSync()`](#executetasksync) | ExecuteTaskSync streams the create request and inputs to the agent service and streams the outputs back. |


#### ExecuteTaskSync()

```python
def ExecuteTaskSync(
    request_iterator: typing.AsyncIterator[flyteidl.admin.agent_pb2.ExecuteTaskSyncRequest],
    context: grpc.ServicerContext,
) -> typing.AsyncIterator[flyteidl.admin.agent_pb2.ExecuteTaskSyncResponse]
```
ExecuteTaskSync streams the create request and inputs to the agent service and streams the outputs back.
        


| Parameter | Type | Description |
|-|-|-|
| `request_iterator` | `typing.AsyncIterator[flyteidl.admin.agent_pb2.ExecuteTaskSyncRequest]` | |
| `context` | `grpc.ServicerContext` | |

