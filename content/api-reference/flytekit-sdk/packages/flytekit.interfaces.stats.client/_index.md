---
title: flytekit.interfaces.stats.client
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interfaces.stats.client

## Directory

### Classes

| Class | Description |
|-|-|
| [`DummyStatsClient`](../flytekit.interfaces.stats.client/dummystatsclient) | A dummy client for statsd. |
| [`ScopeableStatsProxy`](../flytekit.interfaces.stats.client/scopeablestatsproxy) | A Proxy object for an underlying statsd client. |
| [`StatsClientProxy`](../flytekit.interfaces.stats.client/statsclientproxy) |  |

### Methods

| Method | Description |
|-|-|
| [`get_base_stats()`](#get_base_stats) |  |
| [`get_stats()`](#get_stats) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `RESERVED_TAG_WORDS` | `frozenset` |  |

## Methods

#### get_base_stats()

```python
def get_base_stats(
    cfg: flytekit.configuration.StatsConfig,
    prefix: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.StatsConfig` | |
| `prefix` | `str` | |

#### get_stats()

```python
def get_stats(
    cfg: flytekit.configuration.StatsConfig,
    prefix: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.StatsConfig` | |
| `prefix` | `str` | |

