---
title: flyteplugins.connectors.databricks.connector
version: 2.0.0b53
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyteplugins.connectors.databricks.connector

## Directory

### Classes

| Class | Description |
|-|-|
| [`DatabricksConnector`](../flyteplugins.connectors.databricks.connector/databricksconnector) | This is the base class for all async connectors, and it defines the interface that all connectors must implement. |
| [`DatabricksJobMetadata`](../flyteplugins.connectors.databricks.connector/databricksjobmetadata) |  |

### Methods

| Method | Description |
|-|-|
| [`get_header()`](#get_header) |  |
| [`result_state_is_available()`](#result_state_is_available) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `DATABRICKS_API_ENDPOINT` | `str` |  |
| `DEFAULT_DATABRICKS_INSTANCE_ENV_KEY` | `str` |  |

## Methods

#### get_header()

```python
def get_header(
    token: str,
) -> typing.Dict[str, str]
```
| Parameter | Type | Description |
|-|-|-|
| `token` | `str` | |

#### result_state_is_available()

```python
def result_state_is_available(
    life_cycle_state: str,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `life_cycle_state` | `str` | |

