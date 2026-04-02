---
title: Webhook
version: 2.1.3.dev1+ge23e739d5
variants: +flyte +union
layout: py_api
---

# Webhook

**Package:** `flyte.notify`

Send custom HTTP webhook notifications (most flexible option).



## Parameters

```python
class Webhook(
    on_phase: typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]],
    url: str,
    method: typing.Literal['POST', 'PUT', 'PATCH', 'GET', 'DELETE', 'HEAD', 'OPTIONS', 'TRACE', 'CONNECT'],
    headers: typing.Optional[typing.Dict[str, str]],
    body: typing.Optional[typing.Dict[str, typing.Any]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `on_phase` | `typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]]` | ActionPhase(s) to trigger notification |
| `url` | `str` | Webhook URL (supports template variables) |
| `method` | `typing.Literal['POST', 'PUT', 'PATCH', 'GET', 'DELETE', 'HEAD', 'OPTIONS', 'TRACE', 'CONNECT']` | HTTP method (default: "POST") |
| `headers` | `typing.Optional[typing.Dict[str, str]]` | Optional HTTP headers (values support template variables) |
| `body` | `typing.Optional[typing.Dict[str, typing.Any]]` | Optional request body as dict (all string values support template variables recursively) |

