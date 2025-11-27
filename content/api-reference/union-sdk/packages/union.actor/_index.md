---
title: union.actor
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# union.actor

## Directory

### Classes

| Class | Description |
|-|-|
| [`ActorEnvironment`](../union.actor/actorenvironment) | ActorEnvironment class. |
| [`ActorTask`](../union.actor/actortask) | A Python Function task should be used as the base for all extensions that have a python function. |

### Methods

| Method | Description |
|-|-|
| [`actor_cache()`](#actor_cache) | Cache function between actor executions. |


## Methods

#### actor_cache()

```python
def actor_cache(
    f,
)
```
Cache function between actor executions.


| Parameter | Type | Description |
|-|-|-|
| `f` |  | |

