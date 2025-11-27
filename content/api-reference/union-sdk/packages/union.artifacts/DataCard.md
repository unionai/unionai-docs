---
title: DataCard
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# DataCard

**Package:** `union.artifacts`

```python
class DataCard(
    text: str,
    card_type: CardType,
)
```
| Parameter | Type | Description |
|-|-|-|
| `text` | `str` | |
| `card_type` | `CardType` | |

## Methods

| Method | Description |
|-|-|
| [`from_obj()`](#from_obj) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |


### from_obj()

```python
def from_obj(
    card_obj: typing.Any,
) -> Card
```
| Parameter | Type | Description |
|-|-|-|
| `card_obj` | `typing.Any` | |

### serialize_to_string()

```python
def serialize_to_string(
    ctx: FlyteContext,
    variable_name: str,
) -> typing.Tuple[str, str]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `variable_name` | `str` | |

