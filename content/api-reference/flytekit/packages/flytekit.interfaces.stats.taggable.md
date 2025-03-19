---
title: flytekit.interfaces.stats.taggable
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.interfaces.stats.taggable

## Directory

### Classes

| Class | Description |
|-|-|
| [`StatsConfig`](.././flytekit.interfaces.stats.taggable#flytekitinterfacesstatstaggablestatsconfig) | Configuration for sending statsd. |
| [`TaggableStats`](.././flytekit.interfaces.stats.taggable#flytekitinterfacesstatstaggabletaggablestats) | A Proxy object for an underlying statsd client. |

## flytekit.interfaces.stats.taggable.StatsConfig

Configuration for sending statsd.



```python
def StatsConfig(
    host: str,
    port: int,
    disabled: bool,
    disabled_tags: bool,
):
```
| Parameter | Type |
|-|-|
| `host` | `str` |
| `port` | `int` |
| `disabled` | `bool` |
| `disabled_tags` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from environment variable, followed by ConfigFile provided |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
```
Reads from environment variable, followed by ConfigFile provided


| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

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
def TaggableStats(
    client,
    full_prefix,
    cfg: flytekit.configuration.StatsConfig,
    prefix,
    tags,
):
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
| [`clear_tags()`](#clear_tags) | None |
| [`extend_tags()`](#extend_tags) | None |
| [`get_stats()`](#get_stats) | None |
| [`pipeline()`](#pipeline) | None |


#### clear_tags()

```python
def clear_tags()
```
#### extend_tags()

```python
def extend_tags(
    tags,
):
```
| Parameter | Type |
|-|-|
| `tags` |  |

#### get_stats()

```python
def get_stats(
    name,
    copy_tags,
):
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
| full_prefix |  |  |

