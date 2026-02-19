---
title: DeviceCodeResponse
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DeviceCodeResponse

**Package:** `flytekit.clients.auth.token_client`

Response from device auth flow endpoint
{'device_code': 'code',
     'user_code': 'BNDJJFXL',
     'verification_uri': 'url',
     'expires_in': 600,
     'interval': 5}



```python
class DeviceCodeResponse(
    device_code: str,
    user_code: str,
    verification_uri: str,
    expires_in: int,
    interval: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `device_code` | `str` | |
| `user_code` | `str` | |
| `verification_uri` | `str` | |
| `expires_in` | `int` | |
| `interval` | `int` | |

## Methods

| Method | Description |
|-|-|
| [`from_json_response()`](#from_json_response) |  |


### from_json_response()

```python
def from_json_response(
    j: typing.Dict,
) -> DeviceCodeResponse
```
| Parameter | Type | Description |
|-|-|-|
| `j` | `typing.Dict` | |

