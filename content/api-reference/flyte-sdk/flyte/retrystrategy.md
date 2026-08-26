---
title: RetryStrategy
version: 2.6.9
variants: +flyte +union
layout: py_api
---

# RetryStrategy

**Package:** `flyte`

Retry strategy for a task.

```python
# Plain count, no pacing.
@env.task(retries=5)
async def call_api(): ...

# Exponential backoff: 10s, 20s, 40s, 80s, capped at 5m.
@env.task(
    retries=flyte.RetryStrategy(
        count=5,
        backoff=flyte.Backoff(
            base=timedelta(seconds=10),
            factor=2.0,
            cap=timedelta(minutes=5),
        ),
    ),
)
async def call_api_with_backoff(): ...
```


## Parameters

```python
class RetryStrategy(
    count: int,
    backoff: typing.Optional[flyte._retry.Backoff] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `count` | `int` | Number of user retries. `count=0` disables retries. |
| `backoff` | `typing.Optional[flyte._retry.Backoff]` | Optional `flyte.Backoff` policy applied between retries. When unset, retries fire immediately back-to-back. |

