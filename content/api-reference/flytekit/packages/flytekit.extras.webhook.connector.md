---
title: flytekit.extras.webhook.connector
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.extras.webhook.connector

## Directory

### Classes

| Class | Description |
|-|-|
| [`ConnectorRegistry`](.././flytekit.extras.webhook.connector#flytekitextraswebhookconnectorconnectorregistry) | This is the registry for all connectors. |
| [`LiteralMap`](.././flytekit.extras.webhook.connector#flytekitextraswebhookconnectorliteralmap) |  |
| [`Resource`](.././flytekit.extras.webhook.connector#flytekitextraswebhookconnectorresource) | This is the output resource of the job. |
| [`SyncConnectorBase`](.././flytekit.extras.webhook.connector#flytekitextraswebhookconnectorsyncconnectorbase) | This is the base class for all sync connectors. |
| [`TaskExecution`](.././flytekit.extras.webhook.connector#flytekitextraswebhookconnectortaskexecution) | A ProtocolMessage. |
| [`TaskTemplate`](.././flytekit.extras.webhook.connector#flytekitextraswebhookconnectortasktemplate) |  |
| [`WebhookConnector`](.././flytekit.extras.webhook.connector#flytekitextraswebhookconnectorwebhookconnector) | WebhookConnector is responsible for handling webhook tasks. |

### Methods

| Method | Description |
|-|-|
| [`format_dict()`](#format_dict) | Recursively update a dictionary with format strings with values from another dictionary where the keys match. |
| [`literal_map_string_repr()`](#literal_map_string_repr) | This method is used to convert a literal map to a string representation. |


### Variables

| Property | Type | Description |
|-|-|-|
| `DATA_KEY` | `str` |  |
| `HEADERS_KEY` | `str` |  |
| `METHOD_KEY` | `str` |  |
| `SHOW_DATA_KEY` | `str` |  |
| `SHOW_URL_KEY` | `str` |  |
| `TASK_TYPE` | `str` |  |
| `TIMEOUT_SEC` | `str` |  |
| `URL_KEY` | `str` |  |

## Methods

#### format_dict()

```python
def format_dict(
    service: str,
    original_dict: typing.Any,
    update_dict: typing.Dict[str, typing.Any],
    idempotence_token: typing.Optional[str],
) -> typing.Any
```
Recursively update a dictionary with format strings with values from another dictionary where the keys match
the format string. This goes a little beyond regular python string formatting and uses `.` to denote nested keys.

For example, if original_dict is {"EndpointConfigName": "{endpoint_config_name}"},
and update_dict is {"endpoint_config_name": "my-endpoint-config"},
then the result will be {"EndpointConfigName": "my-endpoint-config"}.

For nested keys if the original_dict is {"EndpointConfigName": "{inputs.endpoint_config_name}"},
and update_dict is {"inputs": {"endpoint_config_name": "my-endpoint-config"}},
then the result will be {"EndpointConfigName": "my-endpoint-config"}.



| Parameter | Type |
|-|-|
| `service` | `str` |
| `original_dict` | `typing.Any` |
| `update_dict` | `typing.Dict[str, typing.Any]` |
| `idempotence_token` | `typing.Optional[str]` |

#### literal_map_string_repr()

```python
def literal_map_string_repr(
    lm: typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, flytekit.models.literals.Literal]],
) -> typing.Dict[str, typing.Any]
```
This method is used to convert a literal map to a string representation.


| Parameter | Type |
|-|-|
| `lm` | `typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, flytekit.models.literals.Literal]]` |

## flytekit.extras.webhook.connector.ConnectorRegistry

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

## flytekit.extras.webhook.connector.LiteralMap

```python
class LiteralMap(
    literals,
)
```
| Parameter | Type |
|-|-|
| `literals` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> LiteralMap
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `literals` |  | {{< multiline >}}A dictionary mapping Text key names to Literal objects.
{{< /multiline >}} |

## flytekit.extras.webhook.connector.Resource

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
    phase: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1033f4440>,
    message: typing.Optional[str],
    log_links: typing.Optional[typing.List[flyteidl.core.execution_pb2.TaskLog]],
    outputs: typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, typing.Any], NoneType],
    custom_info: typing.Optional[typing.Dict[str, typing.Any]],
)
```
| Parameter | Type |
|-|-|
| `phase` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1033f4440>` |
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


## flytekit.extras.webhook.connector.SyncConnectorBase

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

## flytekit.extras.webhook.connector.TaskExecution

A ProtocolMessage


## flytekit.extras.webhook.connector.TaskTemplate

```python
class TaskTemplate(
    id,
    type,
    metadata,
    interface,
    custom,
    container,
    task_type_version,
    security_context,
    config,
    k8s_pod,
    sql,
    extended_resources,
)
```
A task template represents the full set of information necessary to perform a unit of work in the Flyte system.
It contains the metadata about what inputs and outputs are consumed or produced.  It also contains the metadata
necessary for Flyte Propeller to do the appropriate work.



| Parameter | Type |
|-|-|
| `id` |  |
| `type` |  |
| `metadata` |  |
| `interface` |  |
| `custom` |  |
| `container` |  |
| `task_type_version` |  |
| `security_context` |  |
| `config` |  |
| `k8s_pod` |  |
| `sql` |  |
| `extended_resources` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> TaskTemplate
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `config` |  | {{< multiline >}}Arbitrary dictionary containing metadata for parsing and handling custom plugins.
{{< /multiline >}} |
| `container` |  | {{< multiline >}}If not None, the target of execution should be a container.
{{< /multiline >}} |
| `custom` |  | {{< multiline >}}Arbitrary dictionary containing metadata for custom plugins.
{{< /multiline >}} |
| `extended_resources` |  | {{< multiline >}}If not None, the extended resources to allocate to the task.
{{< /multiline >}} |
| `id` |  | {{< multiline >}}This is generated by the system and uniquely identifies the task.
{{< /multiline >}} |
| `interface` |  | {{< multiline >}}The interface definition for this task.
{{< /multiline >}} |
| `is_empty` |  |  |
| `k8s_pod` |  |  |
| `metadata` |  | {{< multiline >}}This contains information needed at runtime to determine behavior such as whether or not outputs are
discoverable, timeouts, and retries.
{{< /multiline >}} |
| `security_context` |  |  |
| `sql` |  |  |
| `task_type_version` |  |  |
| `type` |  | {{< multiline >}}This is used to identify additional extensions for use by Propeller or SDK.
{{< /multiline >}} |

## flytekit.extras.webhook.connector.WebhookConnector

WebhookConnector is responsible for handling webhook tasks.

This connector sends HTTP requests based on the task template and inputs provided,
and processes the responses to determine the success or failure of the task.



```python
class WebhookConnector(
    client: typing.Optional[httpx.AsyncClient],
)
```
| Parameter | Type |
|-|-|
| `client` | `typing.Optional[httpx.AsyncClient]` |

### Methods

| Method | Description |
|-|-|
| [`do()`](#do) | This method processes the webhook task and sends an HTTP request. |


#### do()

```python
def do(
    task_template: flytekit.models.task.TaskTemplate,
    output_prefix: str,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
This method processes the webhook task and sends an HTTP request.

It uses asyncio to send the request and process the response using the httpx library.


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

