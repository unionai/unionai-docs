---
title: Renderable
version: 2.1.2
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Renderable

**Package:** `flyte.types`

```python
protocol Renderable()
```
## Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) | Convert an object(markdown, pandas. |


### to_html()

```python
def to_html(
    python_value: typing.Any,
) -> str
```
Convert an object(markdown, pandas.dataframe) to HTML and return HTML as a unicode string.
Returns: An HTML document as a string.


| Parameter | Type | Description |
|-|-|-|
| `python_value` | `typing.Any` | |

