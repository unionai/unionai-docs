---
title: flytekitplugins.spark.connector
version: 1.16.16
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# flytekitplugins.spark.connector

## Directory

### Classes

| Class | Description |
|-|-|
| [`DatabricksConnector`](.././flytekitplugins.spark.connector#flytekitpluginssparkconnectordatabricksconnector) |  |
| [`DatabricksConnectorV2`](.././flytekitplugins.spark.connector#flytekitpluginssparkconnectordatabricksconnectorv2) | Add DatabricksConnectorV2 to support running the k8s spark and databricks spark together in the same workflow. |
| [`DatabricksJobMetadata`](.././flytekitplugins.spark.connector#flytekitpluginssparkconnectordatabricksjobmetadata) |  |

### Methods

| Method | Description |
|-|-|
| [`get_databricks_token()`](#get_databricks_token) | Get the Databricks access token with multi-tenant support. |
| [`get_header()`](#get_header) | Get the authorization header for Databricks API calls. |
| [`get_secret_from_k8s()`](#get_secret_from_k8s) | Read a secret from Kubernetes using the Kubernetes Python client. |
| [`result_state_is_available()`](#result_state_is_available) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `DATABRICKS_API_ENDPOINT` | `str` |  |
| `DEFAULT_DATABRICKS_INSTANCE_ENV_KEY` | `str` |  |
| `DEFAULT_DATABRICKS_SERVICE_CREDENTIAL_PROVIDER_ENV_KEY` | `str` |  |
| `FLYTE_FAIL_ON_ERROR` | `str` |  |

## Methods

#### get_databricks_token()

```python
def get_databricks_token(
    namespace: typing.Optional[str],
    task_template: typing.Optional[flytekit.models.task.TaskTemplate],
    secret_name: typing.Optional[str],
) -> str
```
Get the Databricks access token with multi-tenant support.

Token resolution: namespace K8s secret -&gt; FLYTE_DATABRICKS_ACCESS_TOKEN env var.



| Parameter | Type | Description |
|-|-|-|
| `namespace` | `typing.Optional[str]` | Kubernetes namespace for workflow-specific token lookup. |
| `task_template` | `typing.Optional[flytekit.models.task.TaskTemplate]` | Optional TaskTemplate (kept for API compatibility). |
| `secret_name` | `typing.Optional[str]` | Custom secret name. Defaults to 'databricks-token'. |

**Returns**

str: The Databricks access token.


**Raises**

| Exception | Description |
|-|-|
| `ValueError` | If no token is found from any source. |

#### get_header()

```python
def get_header(
    task_template: typing.Optional[flytekit.models.task.TaskTemplate],
    auth_token: typing.Optional[str],
) -> typing.Dict[str, str]
```
Get the authorization header for Databricks API calls.



| Parameter | Type | Description |
|-|-|-|
| `task_template` | `typing.Optional[flytekit.models.task.TaskTemplate]` | TaskTemplate with workflow-specific secret requests. |
| `auth_token` | `typing.Optional[str]` | Pre-fetched auth token to use directly. |

**Returns:** typing.Dict[str, str]: Authorization and content-type headers.

#### get_secret_from_k8s()

```python
def get_secret_from_k8s(
    secret_name: str,
    secret_key: str,
    namespace: str,
) -> typing.Optional[str]
```
Read a secret from Kubernetes using the Kubernetes Python client.



| Parameter | Type | Description |
|-|-|-|
| `secret_name` | `str` | Name of the Kubernetes secret (e.g., "databricks-token"). |
| `secret_key` | `str` | Key within the secret (e.g., "token"). |
| `namespace` | `str` | Kubernetes namespace where the secret is stored. |

**Returns:** Optional[str]: The secret value as a string, or None if not found.

#### result_state_is_available()

```python
def result_state_is_available(
    life_cycle_state: str,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `life_cycle_state` | `str` | |

## flytekitplugins.spark.connector.DatabricksConnector

### Parameters

```python
def DatabricksConnector()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `metadata_type` | `None` |  |
| `task_category` | `None` | task category that the connector supports |

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
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    task_execution_metadata: typing.Optional[flytekit.models.task.TaskExecutionMetadata],
    kwargs,
) -> flytekitplugins.spark.connector.DatabricksJobMetadata
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type | Description |
|-|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` | |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` | |
| `task_execution_metadata` | `typing.Optional[flytekit.models.task.TaskExecutionMetadata]` | |
| `kwargs` | `**kwargs` | |

#### delete()

```python
def delete(
    resource_meta: flytekitplugins.spark.connector.DatabricksJobMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekitplugins.spark.connector.DatabricksJobMetadata` | |
| `kwargs` | `**kwargs` | |

#### get()

```python
def get(
    resource_meta: flytekitplugins.spark.connector.DatabricksJobMetadata,
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekitplugins.spark.connector.DatabricksJobMetadata` | |
| `kwargs` | `**kwargs` | |

#### get_logs()

```python
def get_logs(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
) -> flyteidl.admin.agent_pb2.GetTaskLogsResponse
```
Return the metrics for the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` | |
| `kwargs` | `**kwargs` | |

#### get_metrics()

```python
def get_metrics(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
) -> flyteidl.admin.agent_pb2.GetTaskMetricsResponse
```
Return the metrics for the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` | |
| `kwargs` | `**kwargs` | |

## flytekitplugins.spark.connector.DatabricksConnectorV2

Add DatabricksConnectorV2 to support running the k8s spark and databricks spark together in the same workflow.
This is necessary because one task type can only be handled by a single backend plugin.

spark -&gt; k8s spark plugin
databricks -&gt; databricks connector


### Parameters

```python
def DatabricksConnectorV2()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `metadata_type` | `None` |  |
| `task_category` | `None` | task category that the connector supports |

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
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    task_execution_metadata: typing.Optional[flytekit.models.task.TaskExecutionMetadata],
    kwargs,
) -> flytekitplugins.spark.connector.DatabricksJobMetadata
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type | Description |
|-|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` | |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` | |
| `task_execution_metadata` | `typing.Optional[flytekit.models.task.TaskExecutionMetadata]` | |
| `kwargs` | `**kwargs` | |

#### delete()

```python
def delete(
    resource_meta: flytekitplugins.spark.connector.DatabricksJobMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekitplugins.spark.connector.DatabricksJobMetadata` | |
| `kwargs` | `**kwargs` | |

#### get()

```python
def get(
    resource_meta: flytekitplugins.spark.connector.DatabricksJobMetadata,
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekitplugins.spark.connector.DatabricksJobMetadata` | |
| `kwargs` | `**kwargs` | |

#### get_logs()

```python
def get_logs(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
) -> flyteidl.admin.agent_pb2.GetTaskLogsResponse
```
Return the metrics for the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` | |
| `kwargs` | `**kwargs` | |

#### get_metrics()

```python
def get_metrics(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
) -> flyteidl.admin.agent_pb2.GetTaskMetricsResponse
```
Return the metrics for the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` | |
| `kwargs` | `**kwargs` | |

## flytekitplugins.spark.connector.DatabricksJobMetadata

### Parameters

```python
class DatabricksJobMetadata(
    databricks_instance: str,
    run_id: str,
    auth_token: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `databricks_instance` | `str` | |
| `run_id` | `str` | |
| `auth_token` | `typing.Optional[str]` | |

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


| Parameter | Type | Description |
|-|-|-|
| `data` | `bytes` | |

#### encode()

```python
def encode()
```
Encode the resource meta to bytes.


