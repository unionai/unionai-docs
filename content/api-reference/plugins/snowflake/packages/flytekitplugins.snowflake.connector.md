---
title: flytekitplugins.snowflake.connector
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.snowflake.connector

## Directory

### Classes

| Class | Description |
|-|-|
| [`SnowflakeConnector`](.././flytekitplugins.snowflake.connector#flytekitpluginssnowflakeconnectorsnowflakeconnector) |  |
| [`SnowflakeJobMetadata`](.././flytekitplugins.snowflake.connector#flytekitpluginssnowflakeconnectorsnowflakejobmetadata) |  |

### Methods

| Method | Description |
|-|-|
| [`construct_query_link()`](#construct_query_link) |  |
| [`get_connection()`](#get_connection) |  |
| [`get_private_key()`](#get_private_key) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `SNOWFLAKE_PRIVATE_KEY` | `str` |  |
| `TASK_TYPE` | `str` |  |

## Methods

#### construct_query_link()

```python
def construct_query_link(
    resource_meta: flytekitplugins.snowflake.connector.SnowflakeJobMetadata,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekitplugins.snowflake.connector.SnowflakeJobMetadata` | |

#### get_connection()

```python
def get_connection(
    metadata: flytekitplugins.snowflake.connector.SnowflakeJobMetadata,
) -> <module 'snowflake.connector' from '/Users/ppiegaze/repos/unionai/unionai-docs/.venv/lib/python3.12/site-packages/snowflake/connector/__init__.py'>
```
| Parameter | Type | Description |
|-|-|-|
| `metadata` | `flytekitplugins.snowflake.connector.SnowflakeJobMetadata` | |

#### get_private_key()

```python
def get_private_key()
```
## flytekitplugins.snowflake.connector.SnowflakeConnector

```python
def SnowflakeConnector()
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
    kwargs,
) -> flytekitplugins.snowflake.connector.SnowflakeJobMetadata
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type | Description |
|-|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` | |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` | |
| `kwargs` | `**kwargs` | |

#### delete()

```python
def delete(
    resource_meta: flytekitplugins.snowflake.connector.SnowflakeJobMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekitplugins.snowflake.connector.SnowflakeJobMetadata` | |
| `kwargs` | `**kwargs` | |

#### get()

```python
def get(
    resource_meta: flytekitplugins.snowflake.connector.SnowflakeJobMetadata,
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekitplugins.snowflake.connector.SnowflakeJobMetadata` | |
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

## flytekitplugins.snowflake.connector.SnowflakeJobMetadata

```python
class SnowflakeJobMetadata(
    user: str,
    account: str,
    database: str,
    schema: str,
    warehouse: str,
    query_id: str,
    has_output: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `user` | `str` | |
| `account` | `str` | |
| `database` | `str` | |
| `schema` | `str` | |
| `warehouse` | `str` | |
| `query_id` | `str` | |
| `has_output` | `bool` | |

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


