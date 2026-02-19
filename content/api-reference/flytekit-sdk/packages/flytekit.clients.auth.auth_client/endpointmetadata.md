---
title: EndpointMetadata
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# EndpointMetadata

**Package:** `flytekit.clients.auth.auth_client`

This class can be used to control the rendering of the page on login successful or failure



```python
class EndpointMetadata(
    endpoint: str,
    success_html: typing.Optional[bytes],
    failure_html: typing.Optional[bytes],
)
```
| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |
| `success_html` | `typing.Optional[bytes]` | |
| `failure_html` | `typing.Optional[bytes]` | |

