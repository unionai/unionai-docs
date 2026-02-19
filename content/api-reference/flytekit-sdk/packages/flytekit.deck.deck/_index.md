---
title: flytekit.deck.deck
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.deck.deck

## Directory

### Classes

| Class | Description |
|-|-|
| [`Deck`](../flytekit.deck.deck/deck) | Deck enable users to get customizable and default visibility into their tasks. |
| [`DeckField`](../flytekit.deck.deck/deckfield) | DeckField is used to specify the fields that will be rendered in the deck. |
| [`TimeLineDeck`](../flytekit.deck.deck/timelinedeck) | The TimeLineDeck class is designed to render the execution time of each part of a task. |

### Methods

| Method | Description |
|-|-|
| [`generate_time_table()`](#generate_time_table) |  |
| [`get_deck_template()`](#get_deck_template) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `DECK_FILE_NAME` | `str` |  |
| `OUTPUT_DIR_JUPYTER_PREFIX` | `str` |  |

## Methods

#### generate_time_table()

```python
def generate_time_table(
    data: dict,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `data` | `dict` | |

#### get_deck_template()

```python
def get_deck_template()
```
