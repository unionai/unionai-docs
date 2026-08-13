---
title: FlyteSession
version: 2.6.0
variants: +flyte +union
layout: py_api
---

# FlyteSession

**Package:** `flyteplugins.agents.openai`

An `agents` `Session` whose items live in a keyed Flyte `MemoryStore`.

The store's `messages` transcript is the session item list; `add_items`
persists durably (an object-store upload) so the next run for the same key
resumes the conversation.


## Parameters

```python
class FlyteSession(
    store: typing.Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `store` | `typing.Any` | |

## Methods

| Method | Description |
|-|-|
| [`add_items()`](#add_items) |  |
| [`clear_session()`](#clear_session) |  |
| [`get_items()`](#get_items) |  |
| [`pop_item()`](#pop_item) |  |


### add_items()

```python
def add_items(
    items: list[dict[str, typing.Any]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `items` | `list[dict[str, typing.Any]]` | |

### clear_session()

```python
def clear_session()
```
### get_items()

```python
def get_items(
    limit: int | None = None,
) -> list[dict[str, typing.Any]]
```
| Parameter | Type | Description |
|-|-|-|
| `limit` | `int \| None` | |

### pop_item()

```python
def pop_item()
```
