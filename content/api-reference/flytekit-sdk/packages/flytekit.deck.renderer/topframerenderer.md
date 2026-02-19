---
title: TopFrameRenderer
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TopFrameRenderer

**Package:** `flytekit.deck.renderer`

Render a DataFrame as an HTML table.



```python
class TopFrameRenderer(
    max_rows: int,
    max_cols: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `max_rows` | `int` | |
| `max_cols` | `int` | |

## Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) |  |


### to_html()

```python
def to_html(
    df: pandas.DataFrame,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `df` | `pandas.DataFrame` | |

