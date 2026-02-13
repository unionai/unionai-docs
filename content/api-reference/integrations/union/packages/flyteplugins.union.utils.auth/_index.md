---
title: flyteplugins.union.utils.auth
version: 0.1.1
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyteplugins.union.utils.auth

## Directory

### Classes

| Class | Description |
|-|-|
| [`AppClientCredentials`](../flyteplugins.union.utils.auth/appclientcredentials) | Application client credentials for API key. |

### Methods

| Method | Description |
|-|-|
| [`encode_app_client_credentials()`](#encode_app_client_credentials) | Encode app credentials as a base64 string for use as UNION_API_KEY. |
| [`is_serverless_endpoint()`](#is_serverless_endpoint) | Check if endpoint is a Union serverless endpoint. |


## Methods

#### encode_app_client_credentials()

```python
def encode_app_client_credentials(
    app_credentials: flyteplugins.union.utils.auth.AppClientCredentials,
) -> str
```
Encode app credentials as a base64 string for use as UNION_API_KEY.



| Parameter | Type | Description |
|-|-|-|
| `app_credentials` | `flyteplugins.union.utils.auth.AppClientCredentials` | The application credentials to encode |

#### is_serverless_endpoint()

```python
def is_serverless_endpoint(
    endpoint: str,
) -> bool
```
Check if endpoint is a Union serverless endpoint.


| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |

