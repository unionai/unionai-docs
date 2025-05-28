---
title: flytekit.interfaces.stats.taggable
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interfaces.stats.taggable

## Directory

### Classes

| Class | Description |
|-|-|
| [`TaggableStats`](.././flytekit.interfaces.stats.taggable#flytekitinterfacesstatstaggabletaggablestats) | A Proxy object for an underlying statsd client. |

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
) -> e: TaggableStats
```
:rtype: TaggableStats


| Parameter | Type |
|-|-|
| `cfg` | `flytekit.configuration.StatsConfig` |
| `prefix` | `str` |
| `tags` | `typing.Dict[str, str]` |

## flytekit.interfaces.stats.taggable.TaggableStats

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
| Parameter | Type |
|-|-|
| `client` |  |
| `full_prefix` |  |
| `cfg` | `flytekit.configuration.StatsConfig` |
| `prefix` |  |
| `tags` |  |

### Methods

| Method | Description |
|-|-|
| [`clear_tags()`](#clear_tags) |  |
| [`extend_tags()`](#extend_tags) |  |
| [`get_stats()`](#get_stats) |  |
| [`pipeline()`](#pipeline) |  |


#### clear_tags()

```python
def clear_tags()
```
#### extend_tags()

```python
def extend_tags(
    tags,
)
```
| Parameter | Type |
|-|-|
| `tags` |  |

#### get_stats()

```python
def get_stats(
    name,
    copy_tags,
)
```
| Parameter | Type |
|-|-|
| `name` |  |
| `copy_tags` |  |

#### pipeline()

```python
def pipeline()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `full_prefix` |  |  |

