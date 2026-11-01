---
title: SessionAddress
description: "Where a session can be reached, as its worker reported it."
icon: braces
version: 2.12.2
variants: +flyte +union
layout: py_api
---

# SessionAddress

**Package:** `flyte.extend`

Where a session can be reached, as its worker reported it. Use `url` when it is set; otherwise the session is
served at `routing_info`'s `ip`:`port` and `path`.

Warning: Experimental feature: alpha — APIs may change without notice.



## Parameters

```python
class SessionAddress(
    url: Optional[str] = None,
    path: str = '',
    routing_info: Optional[SessionRoutingInfo] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `url` | `Optional[str]` | A URL that reaches the session, when its worker publishes one. |
| `path` | `str` | The path the session is served at, under `url` or on the pod. |
| `routing_info` | `Optional[SessionRoutingInfo]` | Where in the platform the session is served, when its worker reports it. |

