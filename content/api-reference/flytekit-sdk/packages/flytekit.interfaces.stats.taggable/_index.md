---
title: flytekit.interfaces.stats.taggable
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interfaces.stats.taggable

## Directory

### Classes

| Class | Description |
|-|-|
| [`TaggableStats`](../flytekit.interfaces.stats.taggable/taggablestats) |  |

### Methods

| Method | Description |
|-|-|
| [`get_stats()`](#get_stats) | :rtype: TaggableStats. |


## Methods

#### get_stats()

```python
def get_stats(
    cfg: flytekit.configuration.StatsConfig,
    prefix: str,
    tags: typing.Dict[str, str],
) -> flytekit.interfaces.stats.taggable.TaggableStats
```
:rtype: TaggableStats


| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.StatsConfig` | |
| `prefix` | `str` | |
| `tags` | `typing.Dict[str, str]` | |

