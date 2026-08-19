---
title: flytekit.interfaces.stats.client
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekit.interfaces.stats.client

## Directory

### Classes

| Class | Description |
|-|-|
| [`DummyStatsClient`](.././flytekit.interfaces.stats.client#flytekitinterfacesstatsclientdummystatsclient) | A dummy client for statsd. |
| [`ScopeableStatsProxy`](.././flytekit.interfaces.stats.client#flytekitinterfacesstatsclientscopeablestatsproxy) | A Proxy object for an underlying statsd client. |
| [`StatsClientProxy`](.././flytekit.interfaces.stats.client#flytekitinterfacesstatsclientstatsclientproxy) |  |

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

## flytekit.interfaces.stats.client.DummyStatsClient

A dummy client for statsd.


### Parameters

```python
class DummyStatsClient(
    host = 'localhost',
    port = 8125,
    prefix = None,
    maxudpsize = 512,
    ipv6 = False,
)
```
Create a new client.


| Parameter | Type | Description |
|-|-|-|
| `host` |  | |
| `port` |  | |
| `prefix` |  | |
| `maxudpsize` |  | |
| `ipv6` |  | |

## flytekit.interfaces.stats.client.ScopeableStatsProxy

A Proxy object for an underlying statsd client.
Adds a new call, scope(prefix), which returns a new proxy to the same
client which will prefix all calls to underlying methods with the scoped prefix:
new_client = client.get_stats('a')
new_client.incr('b') # Metric name = a.b
This can be nested:
newer_client = new_client.get_stats('subsystem')
newer_client.incr('bad') # Metric name = a.subsystem.bad


### Parameters

```python
class ScopeableStatsProxy(
    client,
    prefix = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `client` |  | |
| `prefix` |  | |

### Methods

| Method | Description |
|-|-|
| [`get_stats()`](#get_stats) |  |
| [`pipeline()`](#pipeline) |  |


#### get_stats()

```python
def get_stats(
    name,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` |  | |

#### pipeline()

```python
def pipeline()
```
## flytekit.interfaces.stats.client.StatsClientProxy

### Parameters

```python
class StatsClientProxy(
    client,
    prefix = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `client` |  | |
| `prefix` |  | |

### Methods

| Method | Description |
|-|-|
| [`get_stats()`](#get_stats) |  |
| [`pipeline()`](#pipeline) |  |


#### get_stats()

```python
def get_stats(
    name,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` |  | |

#### pipeline()

```python
def pipeline()
```
