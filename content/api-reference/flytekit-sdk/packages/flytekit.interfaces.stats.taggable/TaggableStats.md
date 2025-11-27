---
title: TaggableStats
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaggableStats

**Package:** `flytekit.interfaces.stats.taggable`

A Proxy object for an underlying statsd client.
Adds a new call, scope(prefix), which returns a new proxy to the same
client which will prefix all calls to underlying methods with the scoped prefix:
new_client = client.get_stats('a')
new_client.incr('b') # Metric name = a.b
This can be nested:
newer_client = new_client.get_stats('subsystem')
newer_client.incr('bad') # Metric name = a.subsystem.bad


```python
class TaggableStats(
    client,
    full_prefix,
    cfg: flytekit.configuration.StatsConfig,
    prefix,
    tags,
)
```
| Parameter | Type | Description |
|-|-|-|
| `client` |  | |
| `full_prefix` |  | |
| `cfg` | `flytekit.configuration.StatsConfig` | |
| `prefix` |  | |
| `tags` |  | |

## Methods

| Method | Description |
|-|-|
| [`clear_tags()`](#clear_tags) |  |
| [`extend_tags()`](#extend_tags) |  |
| [`get_stats()`](#get_stats) |  |
| [`pipeline()`](#pipeline) |  |


### clear_tags()

```python
def clear_tags()
```
### extend_tags()

```python
def extend_tags(
    tags,
)
```
| Parameter | Type | Description |
|-|-|-|
| `tags` |  | |

### get_stats()

```python
def get_stats(
    name,
    copy_tags,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` |  | |
| `copy_tags` |  | |

### pipeline()

```python
def pipeline()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `full_prefix` |  |  |

