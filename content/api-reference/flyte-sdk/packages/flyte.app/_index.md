---
title: flyte.app
version: 2.1.10.dev6+ga8f3f9bfa
variants: +flyte +union
layout: py_api
sidebar_expanded: true
---

# flyte.app

## Directory

### Classes

| Class | Description |
|-|-|
| [`AppEndpoint`](../flyte.app/appendpoint) | Embed an upstream app's endpoint as an app parameter. |
| [`AppEnvironment`](../flyte.app/appenvironment) | Configure a long-running app environment for APIs, dashboards, or model servers. |
| [`ConnectorEnvironment`](../flyte.app/connectorenvironment) | Configure a connector environment for custom Flyte connectors. |
| [`Domain`](../flyte.app/domain) | Subdomain to use for the domain. |
| [`Link`](../flyte.app/link) | Custom links to add to the app. |
| [`Parameter`](../flyte.app/parameter) | Parameter for application. |
| [`Port`](../flyte.app/port) |  |
| [`RunOutput`](../flyte.app/runoutput) | Use a run's output for app parameters. |
| [`Scaling`](../flyte.app/scaling) | Controls replica count and autoscaling behavior for app environments. |
| [`Timeouts`](../flyte.app/timeouts) | Timeout configuration for the application. |

### Methods

| Method | Description |
|-|-|
| [`ctx()`](#ctx) | Returns the current app context. |
| [`get_parameter()`](#get_parameter) | Get parameters for application or endpoint. |


## Methods

#### ctx()

```python
def ctx()
```
Returns the current app context.
Returns: AppContext


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

