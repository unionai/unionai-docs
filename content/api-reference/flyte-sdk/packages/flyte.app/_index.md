---
title: flyte.app
version: 2.0.0b50
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.app

## Directory

### Classes

| Class | Description |
|-|-|
| [`AppEndpoint`](../flyte.app/appendpoint) | Embed an upstream app's endpoint as an app parameter. |
| [`AppEnvironment`](../flyte.app/appenvironment) |  |
| [`ConnectorEnvironment`](../flyte.app/connectorenvironment) |  |
| [`Domain`](../flyte.app/domain) | Subdomain to use for the domain. |
| [`Link`](../flyte.app/link) | Custom links to add to the app. |
| [`Parameter`](../flyte.app/parameter) | Parameter for application. |
| [`Port`](../flyte.app/port) |  |
| [`RunOutput`](../flyte.app/runoutput) | Use a run's output for app parameters. |
| [`Scaling`](../flyte.app/scaling) |  |

### Methods

| Method | Description |
|-|-|
| [`get_parameter()`](#get_parameter) | Get parameters for application or endpoint. |


## Methods

#### get_parameter()

```python
def get_parameter(
    name: str,
) -> str
```
Get parameters for application or endpoint.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

