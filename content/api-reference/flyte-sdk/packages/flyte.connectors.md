---
title: flyte.connectors
version: 2.0.0b31
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.connectors

## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncConnector`](.././flyte.connectors#flyteconnectorsasyncconnector) | This is the base class for all async connectors, and it defines the interface that all connectors must implement. |
| [`AsyncConnectorExecutorMixin`](.././flyte.connectors#flyteconnectorsasyncconnectorexecutormixin) | This mixin class is used to run the connector task locally, and it's only used for local execution. |
| [`ConnectorRegistry`](.././flyte.connectors#flyteconnectorsconnectorregistry) | This is the registry for all connectors. |
| [`ConnectorService`](.././flyte.connectors#flyteconnectorsconnectorservice) |  |
| [`Resource`](.././flyte.connectors#flyteconnectorsresource) | This is the output resource of the job. |
| [`ResourceMeta`](.././flyte.connectors#flyteconnectorsresourcemeta) | This is the metadata for the job. |

## flyte.connectors.AsyncConnector

This is the base class for all async connectors, and it defines the interface that all connectors must implement.
The connector service is responsible for invoking connectors.
The executor will communicate with the connector service to create tasks, get the status of tasks, and delete tasks.

All the connectors should be registered in the ConnectorRegistry.
Connector Service will look up the connector based on the task type and version.


### Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Return a resource meta that can be used to get the status of the task. |
| [`delete()`](#delete) | Delete the task. |
| [`get()`](#get) | Return the status of the task, and return the outputs in some cases. |
| [`get_logs()`](#get_logs) | Return the metrics for the task. |
| [`get_metrics()`](#get_metrics) | Return the metrics for the task. |


#### create()

```python
def create(
    task_template: flyteidl2.core.tasks_pb2.TaskTemplate,
    output_prefix: str,
    inputs: typing.Optional[typing.Dict[str, typing.Any]],
    task_execution_metadata: typing.Optional[flyteidl2.plugins.connector_pb2.TaskExecutionMetadata],
    kwargs,
) -> flyte.connectors._connector.ResourceMeta
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type |
|-|-|
| `task_template` | `flyteidl2.core.tasks_pb2.TaskTemplate` |
| `output_prefix` | `str` |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` |
| `task_execution_metadata` | `typing.Optional[flyteidl2.plugins.connector_pb2.TaskExecutionMetadata]` |
| `kwargs` | `**kwargs` |

#### delete()

```python
def delete(
    resource_meta: flyte.connectors._connector.ResourceMeta,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flyte.connectors._connector.ResourceMeta` |
| `kwargs` | `**kwargs` |

#### get()

```python
def get(
    resource_meta: flyte.connectors._connector.ResourceMeta,
    kwargs,
) -> flyte.connectors._connector.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type |
|-|-|
| `resource_meta` | `flyte.connectors._connector.ResourceMeta` |
| `kwargs` | `**kwargs` |

#### get_logs()

```python
def get_logs(
    resource_meta: flyte.connectors._connector.ResourceMeta,
    kwargs,
) -> flyteidl2.plugins.connector_pb2.GetTaskLogsResponse
```
Return the metrics for the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flyte.connectors._connector.ResourceMeta` |
| `kwargs` | `**kwargs` |

#### get_metrics()

```python
def get_metrics(
    resource_meta: flyte.connectors._connector.ResourceMeta,
    kwargs,
) -> flyteidl2.plugins.connector_pb2.GetTaskMetricsResponse
```
Return the metrics for the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flyte.connectors._connector.ResourceMeta` |
| `kwargs` | `**kwargs` |

## flyte.connectors.AsyncConnectorExecutorMixin

This mixin class is used to run the connector task locally, and it's only used for local execution.
Task should inherit from this class if the task can be run in the connector.


### Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) |  |


#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `kwargs` | `**kwargs` |

## flyte.connectors.ConnectorRegistry

This is the registry for all connectors.
The connector service will look up the connector registry based on the task type and version.


### Methods

| Method | Description |
|-|-|
| [`get_connector()`](#get_connector) |  |
| [`register()`](#register) |  |


#### get_connector()

```python
def get_connector(
    task_type_name: str,
    task_type_version: int,
) -> flyte.connectors._connector.AsyncConnector
```
| Parameter | Type |
|-|-|
| `task_type_name` | `str` |
| `task_type_version` | `int` |

#### register()

```python
def register(
    connector: flyte.connectors._connector.AsyncConnector,
    override: bool,
)
```
| Parameter | Type |
|-|-|
| `connector` | `flyte.connectors._connector.AsyncConnector` |
| `override` | `bool` |

## flyte.connectors.ConnectorService

### Methods

| Method | Description |
|-|-|
| [`run()`](#run) |  |


#### run()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ConnectorService.run.aio()`.
```python
def run(
    cls,
    port: int,
    prometheus_port: int,
    worker: int,
    timeout: int | None,
    modules: typing.Optional[typing.List[str]],
)
```
| Parameter | Type |
|-|-|
| `cls` |  |
| `port` | `int` |
| `prometheus_port` | `int` |
| `worker` | `int` |
| `timeout` | `int \| None` |
| `modules` | `typing.Optional[typing.List[str]]` |

## flyte.connectors.Resource

This is the output resource of the job.

Attributes
----------
    phase : TaskExecution.Phase
        The phase of the job.
    message : Optional[str]
        The return message from the job.
    log_links : Optional[List[TaskLog]]
        The log links of the job. For example, the link to the BigQuery Console.
    outputs : Optional[Union[LiteralMap, typing.Dict[str, Any]]]
        The outputs of the job. If return python native types, the agent will convert them to flyte literals.
    custom_info : Optional[typing.Dict[str, Any]]
        The custom info of the job. For example, the job config.


```python
class Resource(
    phase: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1044a42f0>,
    message: typing.Optional[str],
    log_links: typing.Optional[typing.List[flyteidl2.core.execution_pb2.TaskLog]],
    outputs: typing.Optional[typing.Dict[str, typing.Any]],
    custom_info: typing.Optional[typing.Dict[str, typing.Any]],
)
```
| Parameter | Type |
|-|-|
| `phase` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1044a42f0>` |
| `message` | `typing.Optional[str]` |
| `log_links` | `typing.Optional[typing.List[flyteidl2.core.execution_pb2.TaskLog]]` |
| `outputs` | `typing.Optional[typing.Dict[str, typing.Any]]` |
| `custom_info` | `typing.Optional[typing.Dict[str, typing.Any]]` |

## flyte.connectors.ResourceMeta

This is the metadata for the job. For example, the id of the job.


```python
def ResourceMeta()
```
### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | Decode the resource meta from bytes. |
| [`encode()`](#encode) | Encode the resource meta to bytes. |


#### decode()

```python
def decode(
    data: bytes,
) -> ResourceMeta
```
Decode the resource meta from bytes.


| Parameter | Type |
|-|-|
| `data` | `bytes` |

#### encode()

```python
def encode()
```
Encode the resource meta to bytes.


