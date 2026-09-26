---
title: TimeRange
description: "A trailing window, relative to the consumer's own time value, ending at that value."
icon: braces
version: 0.14.0
variants: -flyte +union
layout: py_api
---

# TimeRange

**Package:** `flyteplugins.union.factory`

A trailing window, relative to the consumer's own time value, ending at that value.


## Parameters

```python
class TimeRange(
    days: int = 0,
    hours: int = 0,
)
```
| Parameter | Type | Description |
|-|-|-|
| `days` | `int` | |
| `hours` | `int` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `delta` | `timedelta` |  |

## Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`to_dict()`](#to_dict) |  |


### from_dict()

```python
def from_dict(
    d: Mapping[str, Any],
) -> 'TimeRange'
```
| Parameter | Type | Description |
|-|-|-|
| `d` | `Mapping[str, Any]` | |

### to_dict()

```python
def to_dict()
```
