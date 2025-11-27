---
title: DummyStatsClient
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DummyStatsClient

**Package:** `flytekit.interfaces.stats.client`

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


| Parameter | Type | Description |
|-|-|-|
| `host` |  | |
| `port` |  | |
| `prefix` |  | |
| `maxudpsize` |  | |
| `ipv6` |  | |

## Methods

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


### close()

```python
def close()
```
Used to close and clean up any underlying resources.


### decr()

```python
def decr(
    stat,
    count,
    rate,
)
```
Decrement a stat by `count`.


| Parameter | Type | Description |
|-|-|-|
| `stat` |  | |
| `count` |  | |
| `rate` |  | |

### gauge()

```python
def gauge(
    stat,
    value,
    rate,
    delta,
)
```
Set a gauge value.


| Parameter | Type | Description |
|-|-|-|
| `stat` |  | |
| `value` |  | |
| `rate` |  | |
| `delta` |  | |

### incr()

```python
def incr(
    stat,
    count,
    rate,
)
```
Increment a stat by `count`.


| Parameter | Type | Description |
|-|-|-|
| `stat` |  | |
| `count` |  | |
| `rate` |  | |

### pipeline()

```python
def pipeline()
```
### set()

```python
def set(
    stat,
    value,
    rate,
)
```
Set a set value.


| Parameter | Type | Description |
|-|-|-|
| `stat` |  | |
| `value` |  | |
| `rate` |  | |

### timer()

```python
def timer(
    stat,
    rate,
)
```
| Parameter | Type | Description |
|-|-|-|
| `stat` |  | |
| `rate` |  | |

### timing()

```python
def timing(
    stat,
    delta,
    rate,
)
```
Send new timing information.

`delta` can be either a number of milliseconds or a timedelta.


| Parameter | Type | Description |
|-|-|-|
| `stat` |  | |
| `delta` |  | |
| `rate` |  | |

