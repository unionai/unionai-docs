---
title: SnowflakeConnector
icon: braces
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# SnowflakeConnector

**Package:** `flyteplugins.snowflake`

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Submit a query to Snowflake asynchronously. |
| [`delete()`](#delete) | Cancel a running Snowflake query. |
| [`get()`](#get) | Poll the status of a Snowflake query. |
| [`get_logs()`](#get_logs) | Return the task execution logs. |
| [`get_metrics()`](#get_metrics) | Return the metrics for the task. |


### create()

```python
def create(
    task_template: flyteidl2.core.tasks_pb2.TaskTemplate,
    inputs: typing.Optional[typing.Dict[str, typing.Any]] = None,
    snowflake_private_key: typing.Optional[str] = None,
    snowflake_private_key_passphrase: typing.Optional[str] = None,
    **kwargs,
) -> flyteplugins.snowflake.connector.SnowflakeJobMetadata
```
Submit a query to Snowflake asynchronously.



| Parameter | Type | Description |
|-|-|-|
| `task_template` | `flyteidl2.core.tasks_pb2.TaskTemplate` | The Flyte task template containing the SQL query and configuration. |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | Optional dictionary of input parameters for parameterized queries. |
| `snowflake_private_key` | `typing.Optional[str]` | The private key content set as a Flyte secret. |
| `snowflake_private_key_passphrase` | `typing.Optional[str]` | The passphrase for the private key set as a Flyte secret, if any. |
| `**kwargs` |  | |

**Returns:** A SnowflakeJobMetadata object containing the query ID and link to the query dashboard.

### delete()

```python
def delete(
    resource_meta: flyteplugins.snowflake.connector.SnowflakeJobMetadata,
    snowflake_private_key: typing.Optional[str] = None,
    snowflake_private_key_passphrase: typing.Optional[str] = None,
    **kwargs,
)
```
Cancel a running Snowflake query.



| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flyteplugins.snowflake.connector.SnowflakeJobMetadata` | The SnowflakeJobMetadata containing the query ID. |
| `snowflake_private_key` | `typing.Optional[str]` | The private key content set as a Flyte secret. |
| `snowflake_private_key_passphrase` | `typing.Optional[str]` | The passphrase for the private key set as a Flyte secret, if any. |
| `**kwargs` |  | |

### get()

```python
def get(
    resource_meta: flyteplugins.snowflake.connector.SnowflakeJobMetadata,
    snowflake_private_key: typing.Optional[str] = None,
    snowflake_private_key_passphrase: typing.Optional[str] = None,
    **kwargs,
) -> flyte.connectors._connector.Resource
```
Poll the status of a Snowflake query.



| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flyteplugins.snowflake.connector.SnowflakeJobMetadata` | The SnowflakeJobMetadata containing the query ID. |
| `snowflake_private_key` | `typing.Optional[str]` | The private key content set as a Flyte secret. |
| `snowflake_private_key_passphrase` | `typing.Optional[str]` | The passphrase for the private key set as a Flyte secret, if any. |
| `**kwargs` |  | |

**Returns:** A Resource object containing the query results and a link to the query dashboard.

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
`GetTaskLogsResponse`, or an async generator yielding multiple
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

