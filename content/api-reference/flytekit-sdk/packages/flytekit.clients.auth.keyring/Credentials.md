---
title: Credentials
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Credentials

**Package:** `flytekit.clients.auth.keyring`

Stores the credentials together


```python
class Credentials(
    access_token: str,
    refresh_token: typing.Optional[str],
    for_endpoint: str,
    expires_in: typing.Optional[int],
    id_token: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `access_token` | `str` | |
| `refresh_token` | `typing.Optional[str]` | |
| `for_endpoint` | `str` | |
| `expires_in` | `typing.Optional[int]` | |
| `id_token` | `typing.Optional[str]` | |

