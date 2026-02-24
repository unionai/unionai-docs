---
title: flytekitplugins.bigquery.connector
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.bigquery.connector

## Directory

### Classes

| Class | Description |
|-|-|
| [`BigQueryConnector`](.././flytekitplugins.bigquery.connector#flytekitpluginsbigqueryconnectorbigqueryconnector) |  |
| [`BigQueryMetadata`](.././flytekitplugins.bigquery.connector#flytekitpluginsbigqueryconnectorbigquerymetadata) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `pythonTypeToBigQueryType` | `dict` |  |

## flytekitplugins.bigquery.connector.BigQueryConnector

```python
def BigQueryConnector()
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
) -> flytekitplugins.bigquery.connector.BigQueryMetadata
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
    resource_meta: flytekitplugins.bigquery.connector.BigQueryMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekitplugins.bigquery.connector.BigQueryMetadata` | |
| `kwargs` | `**kwargs` | |

#### get()

```python
def get(
    resource_meta: flytekitplugins.bigquery.connector.BigQueryMetadata,
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekitplugins.bigquery.connector.BigQueryMetadata` | |
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

## flytekitplugins.bigquery.connector.BigQueryMetadata

```python
class BigQueryMetadata(
    job_id: str,
    project: str,
    location: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `job_id` | `str` | |
| `project` | `str` | |
| `location` | `str` | |

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


