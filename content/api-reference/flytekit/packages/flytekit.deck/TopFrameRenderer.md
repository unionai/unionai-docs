---
title: TopFrameRenderer
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# TopFrameRenderer

**Package:** `flytekit.deck`

Render a DataFrame as an HTML table.


```python
def TopFrameRenderer(
    max_rows: int,
    max_cols: int,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `max_rows` | `int` |
| `max_cols` | `int` |
## Methods

### to_html()

```python
def to_html(
    df: pandas.DataFrame,
):
```
| Parameter | Type |
|-|-|
| `df` | `pandas.DataFrame` |
