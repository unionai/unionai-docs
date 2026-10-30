---
title: SessionRoutingInfo
description: "Where in the platform a session is served: the pod its worker serves it from, and the cluster."
icon: braces
version: 2.12.2
variants: +flyte +union
layout: py_api
---

# SessionRoutingInfo

**Package:** `flyte.extend`

Where in the platform a session is served: the pod its worker serves it from, and the cluster.

Warning: Experimental feature: alpha — APIs may change without notice.



## Parameters

```python
class SessionRoutingInfo(
    ip: Optional[str] = None,
    port: Optional[int] = None,
    name: Optional[str] = None,
    namespace: Optional[str] = None,
    cluster: Optional[str] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ip` | `Optional[str]` | IP of the pod serving the session. |
| `port` | `Optional[int]` | Port on that pod. |
| `name` | `Optional[str]` | Name of that pod. |
| `namespace` | `Optional[str]` | Namespace of that pod. |
| `cluster` | `Optional[str]` | The cluster the session runs in. |

