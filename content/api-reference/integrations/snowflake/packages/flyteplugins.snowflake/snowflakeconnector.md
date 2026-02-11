---
title: SnowflakeConnector
version: 2.0.0b56
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SnowflakeConnector

**Package:** `flyteplugins.snowflake`

This is the base class for all async connectors, and it defines the interface that all connectors must implement.
The connector service is responsible for invoking connectors.
The executor will communicate with the connector service to create tasks, get the status of tasks, and delete tasks.

All the connectors should be registered in the ConnectorRegistry.
Connector Service will look up the connector based on the task type and version.


## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Submit a query to Snowflake asynchronously. |
| [`delete()`](#delete) | Cancel a running Snowflake query. |
| [`get()`](#get) | Poll the status of a Snowflake query. |
| [`get_logs()`](#get_logs) | Return the metrics for the task. |
| [`get_metrics()`](#get_metrics) | Return the metrics for the task. |


### create()

```python
def create(
    task_template: flyteidl2.core.tasks_pb2.TaskTemplate,
    inputs: typing.Optional[typing.Dict[str, typing.Any]],
    snowflake_private_key: typing.Optional[str],
    snowflake_private_key_passphrase: typing.Optional[str],
    kwargs,
) -> flyteplugins.snowflake.connector.SnowflakeJobMetadata
```
Submit a query to Snowflake asynchronously.



| Parameter | Type | Description |
|-|-|-|
| `task_template` | `flyteidl2.core.tasks_pb2.TaskTemplate` | The Flyte task template containing the SQL query and configuration. |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | Optional dictionary of input parameters for parameterized queries. |
| `snowflake_private_key` | `typing.Optional[str]` | The private key content set as a Flyte secret. |
| `snowflake_private_key_passphrase` | `typing.Optional[str]` | The passphrase for the private key set as a Flyte secret, if any. |
| `kwargs` | `**kwargs` | |

### delete()

```python
def delete(
    resource_meta: flyteplugins.snowflake.connector.SnowflakeJobMetadata,
    snowflake_private_key: typing.Optional[str],
    snowflake_private_key_passphrase: typing.Optional[str],
    kwargs,
)
```
Cancel a running Snowflake query.



| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flyteplugins.snowflake.connector.SnowflakeJobMetadata` | The SnowflakeJobMetadata containing the query ID. |
| `snowflake_private_key` | `typing.Optional[str]` | The private key content set as a Flyte secret. |
| `snowflake_private_key_passphrase` | `typing.Optional[str]` | The passphrase for the private key set as a Flyte secret, if any. |
| `kwargs` | `**kwargs` | |

### get()

```python
def get(
    resource_meta: flyteplugins.snowflake.connector.SnowflakeJobMetadata,
    snowflake_private_key: typing.Optional[str],
    snowflake_private_key_passphrase: typing.Optional[str],
    kwargs,
) -> flyte.connectors._connector.Resource
```
Poll the status of a Snowflake query.



| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flyteplugins.snowflake.connector.SnowflakeJobMetadata` | The SnowflakeJobMetadata containing the query ID. |
| `snowflake_private_key` | `typing.Optional[str]` | The private key content set as a Flyte secret. |
| `snowflake_private_key_passphrase` | `typing.Optional[str]` | The passphrase for the private key set as a Flyte secret, if any. |
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

