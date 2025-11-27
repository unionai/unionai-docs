---
title: ConnectorRegistry
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ConnectorRegistry

**Package:** `flytekit.extend.backend.base_connector`

This is the registry for all connectors.
The connector service will look up the connector registry based on the task type.
The connector metadata service will look up the connector metadata based on the connector name.


## Methods

| Method | Description |
|-|-|
| [`get_agent()`](#get_agent) |  |
| [`get_connector()`](#get_connector) |  |
| [`get_connector_metadata()`](#get_connector_metadata) |  |
| [`list_connectors()`](#list_connectors) |  |
| [`register()`](#register) |  |


### get_agent()

```python
def get_agent(
    task_type_name: str,
    task_type_version: int,
) -> typing.Union[flytekit.extend.backend.base_connector.SyncConnectorBase, flytekit.extend.backend.base_connector.AsyncConnectorBase]
```
| Parameter | Type | Description |
|-|-|-|
| `task_type_name` | `str` | |
| `task_type_version` | `int` | |

### get_connector()

```python
def get_connector(
    task_type_name: str,
    task_type_version: int,
) -> typing.Union[flytekit.extend.backend.base_connector.SyncConnectorBase, flytekit.extend.backend.base_connector.AsyncConnectorBase]
```
| Parameter | Type | Description |
|-|-|-|
| `task_type_name` | `str` | |
| `task_type_version` | `int` | |

### get_connector_metadata()

```python
def get_connector_metadata(
    name: str,
) -> flyteidl.admin.agent_pb2.Agent
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

### list_connectors()

```python
def list_connectors()
```
### register()

```python
def register(
    connector: typing.Union[flytekit.extend.backend.base_connector.AsyncConnectorBase, flytekit.extend.backend.base_connector.SyncConnectorBase],
    override: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `connector` | `typing.Union[flytekit.extend.backend.base_connector.AsyncConnectorBase, flytekit.extend.backend.base_connector.SyncConnectorBase]` | |
| `override` | `bool` | |

