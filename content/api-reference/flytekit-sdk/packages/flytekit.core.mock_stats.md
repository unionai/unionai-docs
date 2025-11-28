---
title: flytekit.core.mock_stats
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.mock_stats

## Directory

### Classes

| Class | Description |
|-|-|
| [`MockStats`](.././flytekit.core.mock_stats#flytekitcoremock_statsmockstats) |  |

## flytekit.core.mock_stats.MockStats

```python
class MockStats(
    scope,
    tags,
)
```
Initializes a new mock stats object


| Parameter | Type | Description |
|-|-|-|
| `scope` |  | |
| `tags` |  | |

### Methods

| Method | Description |
|-|-|
| [`current_tags()`](#current_tags) |  |
| [`current_value()`](#current_value) |  |
| [`decr()`](#decr) |  |
| [`gauge()`](#gauge) |  |
| [`incr()`](#incr) |  |
| [`timer()`](#timer) |  |
| [`timing()`](#timing) |  |


#### current_tags()

```python
def current_tags(
    metric,
)
```
| Parameter | Type | Description |
|-|-|-|
| `metric` |  | |

#### current_value()

```python
def current_value(
    metric,
)
```
| Parameter | Type | Description |
|-|-|-|
| `metric` |  | |

#### decr()

```python
def decr(
    metric,
    count,
    tags,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `metric` |  | |
| `count` |  | |
| `tags` |  | |
| `kwargs` | `**kwargs` | |

#### gauge()

```python
def gauge(
    metric,
    value,
    tags,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `metric` |  | |
| `value` |  | |
| `tags` |  | |
| `kwargs` | `**kwargs` | |

#### incr()

```python
def incr(
    metric,
    count,
    tags,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `metric` |  | |
| `count` |  | |
| `tags` |  | |
| `kwargs` | `**kwargs` | |

#### timer()

```python
def timer(
    metric,
    tags,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `metric` |  | |
| `tags` |  | |
| `kwargs` | `**kwargs` | |

#### timing()

```python
def timing(
    metric,
)
```
| Parameter | Type | Description |
|-|-|-|
| `metric` |  | |

