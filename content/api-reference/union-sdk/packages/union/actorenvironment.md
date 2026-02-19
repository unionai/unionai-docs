---
title: ActorEnvironment
version: 0.1.201
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
| `name` | `str` | The name of the actor. This is used in conjunction with the project, domain, and version to uniquely identify the actor. |
| `container_image` | `Optional[Union[str, ImageSpec]]` | The container image to use for the task. Set to default image if none provided. |
| `replica_count` | `int` | The number of workers to provision that are able to accept tasks. |
| `ttl_seconds` | `Optional[int]` | How long to keep the Actor alive while no tasks are being run. If not provided the default configuration value of 90s will be used. |
| `environment` | `Optional[Dict[str, str]]` | Environment variables as key, value pairs in a Python dictionary. |
| `requests` | `Optional[Resources]` | Compute resource requests per task. |
| `limits` | `Optional[Resources]` | Compute resource limits. |
| `accelerator` | `Optional[BaseAccelerator]` | The accelerator device to use for the task. |
| `secret_requests` | `Optional[List[Secret]]` | Keys (ideally descriptive) that can identify the secrets supplied at runtime. |
| `pod_template` | `Optional[PodTemplate]` | The pod template to use as the base configuration for actor replica pods. |
| `interruptible` | `bool` | Whether the actor replica pods are labelled as interruptible. |

## Properties

| Property | Type | Description |
|-|-|-|
| `task` | `None` |  |
| `version` | `None` |  |

