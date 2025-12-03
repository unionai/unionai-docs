---
title: flyte.app
version: 2.0.0b34
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.app

## Directory

### Classes

| Class | Description |
|-|-|
| [`AppEnvironment`](../flyte.app/appenvironment) |  |
| [`Domain`](../flyte.app/domain) | Subdomain to use for the domain. |
| [`Input`](../flyte.app/input) | Input for application. |
| [`Link`](../flyte.app/link) | Custom links to add to the app. |
| [`Port`](../flyte.app/port) |  |
| [`Scaling`](../flyte.app/scaling) |  |

### Methods

| Method | Description |
|-|-|
| [`get_input()`](#get_input) | Get inputs for application or endpoint. |


## Methods

#### get_input()

```python
def get_input(
    name: str,
) -> str
```
Get inputs for application or endpoint.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

