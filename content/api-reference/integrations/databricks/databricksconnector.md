---
title: DatabricksConnector
version: 2.5.18
variants: +flyte +union
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
| [`get_logs()`](#get_logs) | Return the task execution logs. |
| [`get_metrics()`](#get_metrics) | Return the metrics for the task. |


### create()

```python
def create(
    task_template: flyteidl2.core.tasks_pb2.TaskTemplate,
    inputs: typing.Optional[typing.Dict[str, typing.Any]] = None,
    databricks_token: typing.Optional[str] = None,
    **kwargs,
) -> flyteplugins.databricks.connector.DatabricksJobMetadata
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type | Description |
|-|-|-|
| `task_template` | `flyteidl2.core.tasks_pb2.TaskTemplate` | |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | |
| `databricks_token` | `typing.Optional[str]` | |
| `**kwargs` |  | |

### delete()

```python
def delete(
    resource_meta: flyteplugins.databricks.connector.DatabricksJobMetadata,
    databricks_token: typing.Optional[str] = None,
    **kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flyteplugins.databricks.connector.DatabricksJobMetadata` | |
| `databricks_token` | `typing.Optional[str]` | |
| `**kwargs` |  | |

### get()

```python
def get(
    resource_meta: flyteplugins.databricks.connector.DatabricksJobMetadata,
    databricks_token: typing.Optional[str] = None,
    **kwargs,
) -> flyte.connectors._connector.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flyteplugins.databricks.connector.DatabricksJobMetadata` | |
| `databricks_token` | `typing.Optional[str]` | |
| `**kwargs` |  | |

### get_logs()

```python
def get_logs(
    resource_meta: ~M,
    **kwargs,
) -> typing.Union[typing.Coroutine[typing.Any, typing.Any, flyteidl2.connector.connector_pb2.GetTaskLogsResponse], typing.AsyncIterator[flyteidl2.connector.connector_pb2.GetTaskLogsResponse]]
```
Return the task execution logs. Populate `body.lines` (structured
LogLine entries with timestamp + originator) in the returned
GetTaskLogsResponse.

Overrides may be a plain async function returning a single
``GetTaskLogsResponse``, or an async generator yielding multiple
responses (preferred for paginated logs — the connector server
handles both shapes).


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `~M` | |
| `**kwargs` |  | |

### get_metrics()

```python
def get_metrics(
    resource_meta: ~M,
    **kwargs,
) -> flyteidl2.connector.connector_pb2.GetTaskMetricsResponse
```
Return the metrics for the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `~M` | |
| `**kwargs` |  | |

