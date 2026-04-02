---
title: DatabricksConnector
version: 2.1.2
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# DatabricksConnector

**Package:** `flyteplugins.databricks`

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Return a resource meta that can be used to get the status of the task. |
| [`delete()`](#delete) | Delete the task. |
| [`get()`](#get) | Return the status of the task, and return the outputs in some cases. |
| [`get_logs()`](#get_logs) | Return the metrics for the task. |
| [`get_metrics()`](#get_metrics) | Return the metrics for the task. |


### create()

```python
def create(
    task_template: flyteidl2.core.tasks_pb2.TaskTemplate,
    inputs: typing.Optional[typing.Dict[str, typing.Any]],
    databricks_token: typing.Optional[str],
    kwargs,
) -> flyteplugins.databricks.connector.DatabricksJobMetadata
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type | Description |
|-|-|-|
| `task_template` | `flyteidl2.core.tasks_pb2.TaskTemplate` | |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | |
| `databricks_token` | `typing.Optional[str]` | |
| `kwargs` | `**kwargs` | |

### delete()

```python
def delete(
    resource_meta: flyteplugins.databricks.connector.DatabricksJobMetadata,
    databricks_token: typing.Optional[str],
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flyteplugins.databricks.connector.DatabricksJobMetadata` | |
| `databricks_token` | `typing.Optional[str]` | |
| `kwargs` | `**kwargs` | |

### get()

```python
def get(
    resource_meta: flyteplugins.databricks.connector.DatabricksJobMetadata,
    databricks_token: typing.Optional[str],
    kwargs,
) -> flyte.connectors._connector.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flyteplugins.databricks.connector.DatabricksJobMetadata` | |
| `databricks_token` | `typing.Optional[str]` | |
| `kwargs` | `**kwargs` | |

### get_logs()

```python
def get_logs(
    resource_meta: flyte.connectors._connector.ResourceMeta,
    kwargs,
) -> flyteidl2.connector.connector_pb2.GetTaskLogsResponse
```
Return the metrics for the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flyte.connectors._connector.ResourceMeta` | |
| `kwargs` | `**kwargs` | |

### get_metrics()

```python
def get_metrics(
    resource_meta: flyte.connectors._connector.ResourceMeta,
    kwargs,
) -> flyteidl2.connector.connector_pb2.GetTaskMetricsResponse
```
Return the metrics for the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flyte.connectors._connector.ResourceMeta` | |
| `kwargs` | `**kwargs` | |

