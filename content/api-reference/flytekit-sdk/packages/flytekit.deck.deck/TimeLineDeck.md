---
title: TimeLineDeck
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TimeLineDeck

**Package:** `flytekit.deck.deck`

The TimeLineDeck class is designed to render the execution time of each part of a task.
Unlike deck class, the conversion of data to HTML is delayed until the html property is accessed.
This approach is taken because rendering a timeline graph with partial data would not provide meaningful insights.
Instead, the complete data set is used to create a comprehensive visualization of the execution time of each part of the task.


```python
class TimeLineDeck(
    name: str,
    html: typing.Optional[str],
    auto_add_to_deck: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `html` | `typing.Optional[str]` | |
| `auto_add_to_deck` | `bool` | |

## Methods

| Method | Description |
|-|-|
| [`append()`](#append) |  |
| [`append_time_info()`](#append_time_info) |  |
| [`publish()`](#publish) |  |


### append()

```python
def append(
    html: str,
) -> Deck
```
| Parameter | Type | Description |
|-|-|-|
| `html` | `str` | |

### append_time_info()

```python
def append_time_info(
    info: dict,
)
```
| Parameter | Type | Description |
|-|-|-|
| `info` | `dict` | |

### publish()

```python
def publish()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `html` |  |  |
| `name` |  |  |

