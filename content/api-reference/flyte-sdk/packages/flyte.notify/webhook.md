---
title: Webhook
version: 2.0.11
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Webhook

**Package:** `flyte.notify`

Send custom HTTP webhook notifications (most flexible option).

    Example:
        ```python
        Webhook(
            on_phase=ActionPhase.FAILED,
            url="https://api.example.com/alerts",
            method="POST",
            headers={"Content-Type": "application/json", "X-API-Key": "secret"},
            body={
                "event": "task_failed",
                "task": "{task.name}",
                "run": "{run.name}",
                "project": "{project}",
                "domain": "{domain}",
                "error": "{run.error}",
                "url": "{run.url}",
            }
        )
        ```

    Args:
        on_phase:ActionPhase(s) to trigger notification
        url: Webhook URL (supports template variables)
        method: HTTP method (default: "POST")
        headers: Optional HTTP headers (values support template variables)
        body: Optional request body as dict
            (all string values support template variables recursively)
    


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
| `on_phase` | `typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]]` | |
| `url` | `str` | |
| `method` | `typing.Literal['POST', 'PUT', 'PATCH', 'GET', 'DELETE', 'HEAD', 'OPTIONS', 'TRACE', 'CONNECT']` | |
| `headers` | `typing.Optional[typing.Dict[str, str]]` | |
| `body` | `typing.Optional[typing.Dict[str, typing.Any]]` | |

