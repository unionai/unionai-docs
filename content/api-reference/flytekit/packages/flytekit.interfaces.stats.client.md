---
title: flytekit.interfaces.stats.client
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
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
| [`StatsConfig`](.././flytekit.interfaces.stats.client#flytekitinterfacesstatsclientstatsconfig) | Configuration for sending statsd. |

## flytekit.interfaces.stats.client.DummyStatsClient

A dummy client for statsd.


```python
def DummyStatsClient(
    host,
    port,
    prefix,
    maxudpsize,
    ipv6,
):
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
| [`close()`](#close) | Used to close and clean up any underlying resources |
| [`decr()`](#decr) | Decrement a stat by `count` |
| [`gauge()`](#gauge) | Set a gauge value |
| [`incr()`](#incr) | Increment a stat by `count` |
| [`pipeline()`](#pipeline) | None |
| [`set()`](#set) | Set a set value |
| [`timer()`](#timer) | None |
| [`timing()`](#timing) | Send new timing information |


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
):
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
):
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
):
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
):
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
):
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
):
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
def ScopeableStatsProxy(
    client,
    prefix,
):
```
| Parameter | Type |
|-|-|
| `client` |  |
| `prefix` |  |

### Methods

| Method | Description |
|-|-|
| [`get_stats()`](#get_stats) | None |
| [`pipeline()`](#pipeline) | None |


#### get_stats()

```python
def get_stats(
    name,
):
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
def StatsClientProxy(
    client,
    prefix,
):
```
| Parameter | Type |
|-|-|
| `client` |  |
| `prefix` |  |

### Methods

| Method | Description |
|-|-|
| [`get_stats()`](#get_stats) | None |
| [`pipeline()`](#pipeline) | None |


#### get_stats()

```python
def get_stats(
    name,
):
```
| Parameter | Type |
|-|-|
| `name` |  |

#### pipeline()

```python
def pipeline()
```
## flytekit.interfaces.stats.client.StatsConfig

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

