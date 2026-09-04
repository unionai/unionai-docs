---
title: Card
icon: braces
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# Card

**Package:** `flyte.artifacts`

## Parameters

```python
class Card(
    uri: str,
    format: CardFormat = 'html',
    card_type: CardType = 'generic',
)
```
| Parameter | Type | Description |
|-|-|-|
| `uri` | `str` | |
| `format` | `CardFormat` | |
| `card_type` | `CardType` | |

## Methods

| Method | Description |
|-|-|
| [`create_from()`](#create_from) | Upload a card either from raw content or from a local file path. |


### create_from()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Card.create_from.aio()`.
```python
def create_from(
    cls,
    content: str | None = None,
    local_path: pathlib.Path | None = None,
    format: CardFormat = 'html',
    card_type: CardType = 'generic',
) -> Card
```
Upload a card either from raw content or from a local file path.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `content` | `str \| None` | Raw content of the card to be uploaded. |
| `local_path` | `pathlib.Path \| None` | Local file path of the card to be uploaded. |
| `format` | `CardFormat` | Format of the card (e.g., 'html', 'md', 'json', 'yaml', 'csv', 'tsv', 'png', 'jpg', 'jpeg'). |
| `card_type` | `CardType` | Type of the card (e.g., 'model', 'data', 'generic'). |

