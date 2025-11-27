---
title: ScopeableStatsProxy
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ScopeableStatsProxy

**Package:** `flytekit.interfaces.stats.client`

A Proxy object for an underlying statsd client.
Adds a new call, scope(prefix), which returns a new proxy to the same
client which will prefix all calls to underlying methods with the scoped prefix:
new_client = client.get_stats('a')
new_client.incr('b') # Metric name = a.b
This can be nested:
newer_client = new_client.get_stats('subsystem')
newer_client.incr('bad') # Metric name = a.subsystem.bad


```python
class ScopeableStatsProxy(
    client,
    prefix,
)
```
| Parameter | Type | Description |
|-|-|-|
| `client` |  | |
| `prefix` |  | |

## Methods

| Method | Description |
|-|-|
| [`get_stats()`](#get_stats) |  |
| [`pipeline()`](#pipeline) |  |


### get_stats()

```python
def get_stats(
    name,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` |  | |

### pipeline()

```python
def pipeline()
```
