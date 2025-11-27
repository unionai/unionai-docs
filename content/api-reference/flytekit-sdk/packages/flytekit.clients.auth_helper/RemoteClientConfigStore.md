---
title: RemoteClientConfigStore
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RemoteClientConfigStore

**Package:** `flytekit.clients.auth_helper`

This class implements the ClientConfigStore that is served by the Flyte Server, that implements AuthMetadataService


```python
class RemoteClientConfigStore(
    secure_channel: grpc.Channel,
)
```
| Parameter | Type | Description |
|-|-|-|
| `secure_channel` | `grpc.Channel` | |

## Methods

| Method | Description |
|-|-|
| [`get_client_config()`](#get_client_config) | Retrieves the ClientConfig from the given grpc. |


### get_client_config()

```python
def get_client_config()
```
Retrieves the ClientConfig from the given grpc.Channel assuming  AuthMetadataService is available


