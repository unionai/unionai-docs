---
title: ClientConfig
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ClientConfig

**Package:** `flytekit.clients.auth.authenticator`

Client Configuration that is needed by the authenticator



```python
class ClientConfig(
    token_endpoint: str,
    authorization_endpoint: str,
    redirect_uri: str,
    client_id: str,
    device_authorization_endpoint: typing.Optional[str],
    scopes: typing.List[str],
    header_key: str,
    audience: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `token_endpoint` | `str` | |
| `authorization_endpoint` | `str` | |
| `redirect_uri` | `str` | |
| `client_id` | `str` | |
| `device_authorization_endpoint` | `typing.Optional[str]` | |
| `scopes` | `typing.List[str]` | |
| `header_key` | `str` | |
| `audience` | `typing.Optional[str]` | |

