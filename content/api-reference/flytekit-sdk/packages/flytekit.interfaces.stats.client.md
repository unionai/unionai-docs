---
title: flytekit.interfaces.stats.client
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interfaces.stats.client

## Directory

### Classes

| Class | Description |
|-|-|
| [`DummyStatsClient`](.././flytekit.interfaces.stats.client#flytekitinterfacesstatsclientdummystatsclient) | A dummy client for statsd. |
| [`ScopeableStatsProxy`](.././flytekit.interfaces.stats.client#flytekitinterfacesstatsclientscopeablestatsproxy) | A Proxy object for an underlying statsd client. |
| [`StatsClientProxy`](.././flytekit.interfaces.stats.client#flytekitinterfacesstatsclientstatsclientproxy) | A Proxy object for an underlying statsd client. |

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
| Parameter | Type |
|-|-|
| `cfg` | `flytekit.configuration.StatsConfig` |
| `prefix` | `str` |

#### get_stats()

```python
def get_stats(
    cfg: flytekit.configuration.StatsConfig,
    prefix: str,
)
```
| Parameter | Type |
|-|-|
| `cfg` | `flytekit.configuration.StatsConfig` |
| `prefix` | `str` |

## flytekit.interfaces.stats.client.DummyStatsClient

A dummy client for statsd.


```python
class DummyStatsClient(
    host,
    port,
    prefix,
    maxudpsize,
    ipv6,
)
```
Create a new client.


| Parameter | Type |
|-|-|
| `host` |  |
| `port` |  |
| `prefix` |  |
| `maxudpsize` |  |
| `ipv6` |  |

### Methods

| Method | Description |
|-|-|
| [`close()`](#close) | Used to close and clean up any underlying resources. |
| [`decr()`](#decr) | Decrement a stat by `count`. |
| [`gauge()`](#gauge) | Set a gauge value. |
| [`incr()`](#incr) | Increment a stat by `count`. |
| [`pipeline()`](#pipeline) |  |
| [`set()`](#set) | Set a set value. |
| [`timer()`](#timer) |  |
| [`timing()`](#timing) | Send new timing information. |


#### close()

```python
def close()
```
Used to close and clean up any underlying resources.


#### decr()

```python
def decr(
    stat,
    count,
    rate,
)
```
Decrement a stat by `count`.


| Parameter | Type |
|-|-|
| `stat` |  |
| `count` |  |
| `rate` |  |

#### gauge()

```python
def gauge(
    stat,
    value,
    rate,
    delta,
)
```
Set a gauge value.


| Parameter | Type |
|-|-|
| `stat` |  |
| `value` |  |
| `rate` |  |
| `delta` |  |

#### incr()

```python
def incr(
    stat,
    count,
    rate,
)
```
Increment a stat by `count`.


| Parameter | Type |
|-|-|
| `stat` |  |
| `count` |  |
| `rate` |  |

#### pipeline()

```python
def pipeline()
```
#### set()

```python
def set(
    stat,
    value,
    rate,
)
```
Set a set value.


| Parameter | Type |
|-|-|
| `stat` |  |
| `value` |  |
| `rate` |  |

#### timer()

```python
def timer(
    stat,
    rate,
)
```
| Parameter | Type |
|-|-|
| `stat` |  |
| `rate` |  |

#### timing()

```python
def timing(
    stat,
    delta,
    rate,
)
```
Send new timing information.

`delta` can be either a number of milliseconds or a timedelta.


| Parameter | Type |
|-|-|
| `stat` |  |
| `delta` |  |
| `rate` |  |

## flytekit.interfaces.stats.client.ScopeableStatsProxy

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
| Parameter | Type |
|-|-|
| `client` |  |
| `prefix` |  |

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
| Parameter | Type |
|-|-|
| `name` |  |

#### pipeline()

```python
def pipeline()
```
## flytekit.interfaces.stats.client.StatsClientProxy

A Proxy object for an underlying statsd client.
Adds a new call, scope(prefix), which returns a new proxy to the same
client which will prefix all calls to underlying methods with the scoped prefix:
new_client = client.get_stats('a')
new_client.incr('b') # Metric name = a.b
This can be nested:
newer_client = new_client.get_stats('subsystem')
newer_client.incr('bad') # Metric name = a.subsystem.bad


```python
class StatsClientProxy(
    client,
    prefix,
)
```
| Parameter | Type |
|-|-|
| `client` |  |
| `prefix` |  |

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
| Parameter | Type |
|-|-|
| `name` |  |

#### pipeline()

```python
def pipeline()
```
