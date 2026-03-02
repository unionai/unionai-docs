---
title: flytekit.deck.renderer
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.deck.renderer

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArrowRenderer`](.././flytekit.deck.renderer#flytekitdeckrendererarrowrenderer) | Render an Arrow dataframe as an HTML table. |
| [`MarkdownRenderer`](.././flytekit.deck.renderer#flytekitdeckrenderermarkdownrenderer) | Convert a markdown string to HTML and return HTML as a unicode string. |
| [`PythonDependencyRenderer`](.././flytekit.deck.renderer#flytekitdeckrendererpythondependencyrenderer) | PythonDependencyDeck is a deck that contains information about packages installed via pip. |
| [`SourceCodeRenderer`](.././flytekit.deck.renderer#flytekitdeckrenderersourcecoderenderer) | Convert Python source code to HTML, and return HTML as a unicode string. |
| [`TopFrameRenderer`](.././flytekit.deck.renderer#flytekitdeckrenderertopframerenderer) | Render a DataFrame as an HTML table. |

### Protocols

| Protocol | Description |
|-|-|
| [`Renderable`](.././flytekit.deck.renderer#flytekitdeckrendererrenderable) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_MAX_COLS` | `int` |  |
| `DEFAULT_MAX_ROWS` | `int` |  |
| `TYPE_CHECKING` | `bool` |  |

## flytekit.deck.renderer.ArrowRenderer

Render an Arrow dataframe as an HTML table.



### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) |  |


#### to_html()

```python
def to_html(
    df: pyarrow.Table,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `df` | `pyarrow.Table` | |

## flytekit.deck.renderer.MarkdownRenderer

Convert a markdown string to HTML and return HTML as a unicode string.


### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) |  |


#### to_html()

```python
def to_html(
    text: str,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `text` | `str` | |

## flytekit.deck.renderer.PythonDependencyRenderer

PythonDependencyDeck is a deck that contains information about packages installed via pip.



```python
class PythonDependencyRenderer(
    title: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `title` | `str` | |

### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) |  |


#### to_html()

```python
def to_html()
```
## flytekit.deck.renderer.Renderable

```python
protocol Renderable()
```
### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) | Convert an object(markdown, pandas. |


#### to_html()

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

## flytekit.deck.renderer.SourceCodeRenderer

Convert Python source code to HTML, and return HTML as a unicode string.



```python
class SourceCodeRenderer(
    title: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `title` | `str` | |

### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) | Convert the provided Python source code into HTML format using Pygments library. |


#### to_html()

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

## flytekit.deck.renderer.TopFrameRenderer

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

### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) |  |


#### to_html()

```python
def to_html(
    df: pandas.DataFrame,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `df` | `pandas.DataFrame` | |

