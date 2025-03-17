---
title: SourceCodeRenderer
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# SourceCodeRenderer

**Package:** `flytekit.deck`

Convert Python source code to HTML, and return HTML as a unicode string.


```python
def SourceCodeRenderer(
    title: str,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `title` | `str` |
## Methods

### to_html()

```python
def to_html(
    source_code: str,
):
```
Convert the provided Python source code into HTML format using Pygments library.

This method applies a colorful style and replaces the color "#fff0f0" with "#ffffff" in CSS.



| Parameter | Type |
|-|-|
| `source_code` | `str` |
