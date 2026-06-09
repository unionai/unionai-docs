---
title: RetryStrategy
version: 2.4.4
variants: +flyte +union
layout: py_api
---

# RetryStrategy

**Package:** `flyte`

Retry strategy for a task.



## Parameters

```python
class RetryStrategy(
    count: int,
    backoff: typing.Optional[flyte._retry.Backoff],
)
```
| Parameter | Type | Description |
|-|-|-|
| `count` | `int` | Number of user retries. ``count=0`` disables retries. |
| `backoff` | `typing.Optional[flyte._retry.Backoff]` | Optional When unset, retries fire immediately back-to-back. |

