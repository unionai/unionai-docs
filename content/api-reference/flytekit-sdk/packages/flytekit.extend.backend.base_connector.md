---
title: flytekit.extend.backend.base_connector
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extend.backend.base_connector

## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncConnectorBase`](.././flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorasyncconnectorbase) | This is the base class for all async connectors. |
| [`AsyncConnectorExecutorMixin`](.././flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorasyncconnectorexecutormixin) | This mixin class is used to run the async task locally, and it's only used for local execution. |
| [`ConnectorBase`](.././flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorconnectorbase) | Helper class that provides a standard way to create an ABC using. |
| [`ConnectorRegistry`](.././flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorconnectorregistry) | This is the registry for all connectors. |
| [`Resource`](.././flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorresource) | This is the output resource of the job. |
| [`ResourceMeta`](.././flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorresourcemeta) | This is the metadata for the job. |
| [`SyncConnectorBase`](.././flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorsyncconnectorbase) | This is the base class for all sync connectors. |
| [`SyncConnectorExecutorMixin`](.././flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorsyncconnectorexecutormixin) | This mixin class is used to run the sync task locally, and it's only used for local execution. |
| [`TaskCategory`](.././flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectortaskcategory) |  |

## flytekit.extend.backend.base_connector.AsyncConnectorBase

This is the base class for all async connectors.
It defines the interface that all connectors must implement.
The connector service is responsible for invoking connectors. The propeller will communicate with the connector service
to create tasks, get the status of tasks, and delete tasks.

All the connectors should be registered in the ConnectorRegistry.
Connector Service
will look up the connector based on the task type. Every task type can only have one connector.


```python
class AsyncConnectorBase(
    metadata_type: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `metadata_type` | `flytekit.extend.backend.base_connector.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

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
    task_template: flytekit.models.task.TaskTemplate,
    output_prefix: str,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    task_execution_metadata: typing.Optional[flytekit.models.task.TaskExecutionMetadata],
    kwargs,
) -> flytekit.extend.backend.base_connector.ResourceMeta
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `output_prefix` | `str` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `task_execution_metadata` | `typing.Optional[flytekit.models.task.TaskExecutionMetadata]` |
| `kwargs` | ``**kwargs`` |

#### delete()

```python
def delete(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

#### get()

```python
def get(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

#### get_logs()

```python
def get_logs(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
) -> flyteidl.admin.agent_pb2.GetTaskLogsResponse
```
Return the metrics for the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

#### get_metrics()

```python
def get_metrics(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
) -> flyteidl.admin.agent_pb2.GetTaskMetricsResponse
```
Return the metrics for the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `metadata_type` |  |  |
| `task_category` |  | {{< multiline >}}task category that the connector supports
{{< /multiline >}} |

## flytekit.extend.backend.base_connector.AsyncConnectorExecutorMixin

This mixin class is used to run the async task locally, and it's only used for local execution.
Task should inherit from this class if the task can be run in the connector.

Asynchronous tasks are tasks that take a long time to complete, such as running a query.


### Methods

| Method | Description |
|-|-|
| [`connector_signal_handler()`](#connector_signal_handler) |  |
| [`execute()`](#execute) |  |


#### connector_signal_handler()

```python
def connector_signal_handler(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    signum: int,
    frame: frame,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` |
| `signum` | `int` |
| `frame` | `frame` |

#### execute()

```python
def execute(
    kwargs,
) -> flytekit.models.literals.LiteralMap
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

## flytekit.extend.backend.base_connector.ConnectorBase

Helper class that provides a standard way to create an ABC using
inheritance.


```python
class ConnectorBase(
    task_type_name: str,
    task_type_version: int,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `task_type_name` | `str` |
| `task_type_version` | `int` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `task_category` |  | {{< multiline >}}task category that the connector supports
{{< /multiline >}} |

## flytekit.extend.backend.base_connector.ConnectorRegistry

This is the registry for all connectors.
The connector service will look up the connector registry based on the task type.
The connector metadata service will look up the connector metadata based on the connector name.


### Methods

| Method | Description |
|-|-|
| [`get_agent()`](#get_agent) |  |
| [`get_connector()`](#get_connector) |  |
| [`get_connector_metadata()`](#get_connector_metadata) |  |
| [`list_connectors()`](#list_connectors) |  |
| [`register()`](#register) |  |


#### get_agent()

```python
def get_agent(
    task_type_name: str,
    task_type_version: int,
) -> typing.Union[flytekit.extend.backend.base_connector.SyncConnectorBase, flytekit.extend.backend.base_connector.AsyncConnectorBase]
```
| Parameter | Type |
|-|-|
| `task_type_name` | `str` |
| `task_type_version` | `int` |

#### get_connector()

```python
def get_connector(
    task_type_name: str,
    task_type_version: int,
) -> typing.Union[flytekit.extend.backend.base_connector.SyncConnectorBase, flytekit.extend.backend.base_connector.AsyncConnectorBase]
```
| Parameter | Type |
|-|-|
| `task_type_name` | `str` |
| `task_type_version` | `int` |

#### get_connector_metadata()

```python
def get_connector_metadata(
    name: str,
) -> flyteidl.admin.agent_pb2.Agent
```
| Parameter | Type |
|-|-|
| `name` | `str` |

#### list_connectors()

```python
def list_connectors()
```
#### register()

```python
def register(
    connector: typing.Union[flytekit.extend.backend.base_connector.AsyncConnectorBase, flytekit.extend.backend.base_connector.SyncConnectorBase],
    override: bool,
)
```
| Parameter | Type |
|-|-|
| `connector` | `typing.Union[flytekit.extend.backend.base_connector.AsyncConnectorBase, flytekit.extend.backend.base_connector.SyncConnectorBase]` |
| `override` | `bool` |

## flytekit.extend.backend.base_connector.Resource

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
    phase: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x107beec80>,
    message: typing.Optional[str],
    log_links: typing.Optional[typing.List[flyteidl.core.execution_pb2.TaskLog]],
    outputs: typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, typing.Any], NoneType],
    custom_info: typing.Optional[typing.Dict[str, typing.Any]],
)
```
| Parameter | Type |
|-|-|
| `phase` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x107beec80>` |
| `message` | `typing.Optional[str]` |
| `log_links` | `typing.Optional[typing.List[flyteidl.core.execution_pb2.TaskLog]]` |
| `outputs` | `typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, typing.Any], NoneType]` |
| `custom_info` | `typing.Optional[typing.Dict[str, typing.Any]]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | This function is async to call the async type engine functions. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.agent_pb2.Resource,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.admin.agent_pb2.Resource` |

#### to_flyte_idl()

```python
def to_flyte_idl()
```
This function is async to call the async type engine functions. This is okay to do because this is not a
normal model class that inherits from FlyteIdlEntity


## flytekit.extend.backend.base_connector.ResourceMeta

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


## flytekit.extend.backend.base_connector.SyncConnectorBase

This is the base class for all sync connectors.
It defines the interface that all connectors must implement.
The connector service is responsible for invoking connectors.
Propeller sends a request to connector service, and gets a response in the same call.

All the connectors should be registered in the ConnectorRegistry.
Connector Service
will look up the connector based on the task type. Every task type can only have one connector.


```python
class SyncConnectorBase(
    task_type_name: str,
    task_type_version: int,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `task_type_name` | `str` |
| `task_type_version` | `int` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`do()`](#do) | This is the method that the connector will run. |


#### do()

```python
def do(
    task_template: flytekit.models.task.TaskTemplate,
    output_prefix: str,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
This is the method that the connector will run.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `output_prefix` | `str` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `task_category` |  | {{< multiline >}}task category that the connector supports
{{< /multiline >}} |

## flytekit.extend.backend.base_connector.SyncConnectorExecutorMixin

This mixin class is used to run the sync task locally, and it's only used for local execution.
Task should inherit from this class if the task can be run in the connector.

Synchronous tasks run quickly and can return their results instantly.
Sending a prompt to ChatGPT and getting a response, or retrieving some metadata from a backend system.


### Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) |  |


#### execute()

```python
def execute(
    kwargs,
) -> flytekit.models.literals.LiteralMap
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

## flytekit.extend.backend.base_connector.TaskCategory

```python
class TaskCategory(
    name: str,
    version: int,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `version` | `int` |

### Properties

| Property | Type | Description |
|-|-|-|
| `name` |  |  |
| `version` |  |  |

