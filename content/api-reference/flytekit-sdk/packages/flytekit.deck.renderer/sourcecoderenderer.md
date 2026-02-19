---
title: SourceCodeRenderer
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SourceCodeRenderer

**Package:** `flytekit.deck.renderer`

Convert Python source code to HTML, and return HTML as a unicode string.



```python
class SourceCodeRenderer(
    title: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `title` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) | Convert the provided Python source code into HTML format using Pygments library. |


### to_html()

```python
def to_html(
    source_code: str,
) -> str
```
Convert the provided Python source code into HTML format using Pygments library.

This method applies a colorful style and replaces the color "#fff0f0" with "#ffffff" in CSS.



| Parameter | Type | Description |
|-|-|-|
| `source_code` | `str` | The Python source code to be converted. |

