---
title: flytekit.core.mock_stats
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.mock_stats

## Directory

### Classes

| Class | Description |
|-|-|
| [`MockStats`](.././flytekit.core.mock_stats#flytekitcoremock_statsmockstats) | None. |

## flytekit.core.mock_stats.MockStats

```python
def MockStats(
    scope,
    tags,
):
```
Initializes a new mock stats object


| Parameter | Type |
|-|-|
| `scope` |  |
| `tags` |  |

### Methods

| Method | Description |
|-|-|
| [`current_tags()`](#current_tags) | None |
| [`current_value()`](#current_value) | None |
| [`decr()`](#decr) | None |
| [`gauge()`](#gauge) | None |
| [`incr()`](#incr) | None |
| [`timer()`](#timer) | None |
| [`timing()`](#timing) | None |


#### current_tags()

```python
def current_tags(
    metric,
):
```
| Parameter | Type |
|-|-|
| `metric` |  |

#### current_value()

```python
def current_value(
    metric,
):
```
| Parameter | Type |
|-|-|
| `metric` |  |

#### decr()

```python
def decr(
    metric,
    count,
    tags,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `metric` |  |
| `count` |  |
| `tags` |  |
| `kwargs` | ``**kwargs`` |

#### gauge()

```python
def gauge(
    metric,
    value,
    tags,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `metric` |  |
| `value` |  |
| `tags` |  |
| `kwargs` | ``**kwargs`` |

#### incr()

```python
def incr(
    metric,
    count,
    tags,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `metric` |  |
| `count` |  |
| `tags` |  |
| `kwargs` | ``**kwargs`` |

#### timer()

```python
def timer(
    metric,
    tags,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `metric` |  |
| `tags` |  |
| `kwargs` | ``**kwargs`` |

#### timing()

```python
def timing(
    metric,
):
```
| Parameter | Type |
|-|-|
| `metric` |  |

