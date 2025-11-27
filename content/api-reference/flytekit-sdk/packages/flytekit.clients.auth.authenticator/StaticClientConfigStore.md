---
title: StaticClientConfigStore
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# StaticClientConfigStore

**Package:** `flytekit.clients.auth.authenticator`

Client Config store retrieve client config. this can be done in multiple ways


```python
class StaticClientConfigStore(
    cfg: flytekit.clients.auth.authenticator.ClientConfig,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.clients.auth.authenticator.ClientConfig` | |

## Methods

| Method | Description |
|-|-|
| [`get_client_config()`](#get_client_config) |  |


### get_client_config()

```python
def get_client_config()
```
