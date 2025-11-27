---
title: ActorEnvironment
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# ActorEnvironment

**Package:** `union`

ActorEnvironment class.



```python
class ActorEnvironment(
    name: str,
    container_image: Optional[Union[str, ImageSpec]],
    replica_count: int,
    ttl_seconds: Optional[int],
    environment: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    accelerator: Optional[BaseAccelerator],
    secret_requests: Optional[List[Secret]],
    pod_template: Optional[PodTemplate],
    interruptible: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `container_image` | `Optional[Union[str, ImageSpec]]` | |
| `replica_count` | `int` | |
| `ttl_seconds` | `Optional[int]` | |
| `environment` | `Optional[Dict[str, str]]` | |
| `requests` | `Optional[Resources]` | |
| `limits` | `Optional[Resources]` | |
| `accelerator` | `Optional[BaseAccelerator]` | |
| `secret_requests` | `Optional[List[Secret]]` | |
| `pod_template` | `Optional[PodTemplate]` | |
| `interruptible` | `bool` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `task` |  |  |
| `version` |  |  |

