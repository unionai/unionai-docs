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
| [`TaggableStats`](.././flytekit.interfaces.stats.taggable#flytekitinterfacesstatstaggabletaggablestats) |  |

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

## flytekit.interfaces.stats.taggable.TaggableStats

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

### Properties

| Property | Type | Description |
|-|-|-|
| `full_prefix` | `None` |  |

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
| Parameter | Type | Description |
|-|-|-|
| `tags` |  | |

#### get_stats()

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

#### pipeline()

```python
def pipeline()
```
