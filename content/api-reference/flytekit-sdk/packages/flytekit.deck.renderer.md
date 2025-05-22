---
title: flytekit.deck.renderer
version: 0.1.dev2192+g7c539c3.d20250403
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
| [`Renderable`](.././flytekit.deck.renderer#flytekitdeckrendererrenderable) | Base class for protocol classes. |
| [`SourceCodeRenderer`](.././flytekit.deck.renderer#flytekitdeckrenderersourcecoderenderer) | Convert Python source code to HTML, and return HTML as a unicode string. |
| [`TopFrameRenderer`](.././flytekit.deck.renderer#flytekitdeckrenderertopframerenderer) | Render a DataFrame as an HTML table. |

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
| Parameter | Type |
|-|-|
| `df` | `pyarrow.Table` |

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
| Parameter | Type |
|-|-|
| `text` | `str` |

## flytekit.deck.renderer.PythonDependencyRenderer

PythonDependencyDeck is a deck that contains information about packages installed via pip.


```python
class PythonDependencyRenderer(
    title: str,
)
```
| Parameter | Type |
|-|-|
| `title` | `str` |

### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) |  |


#### to_html()

```python
def to_html()
```
## flytekit.deck.renderer.Renderable

Base class for protocol classes.

Protocol classes are defined as::

    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

    class C:
        def meth(self) -> int:
            return 0

    def func(x: Proto) -> int:
        return x.meth()

    func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

    class GenProto[T](Protocol):
        def meth(self) -> T:
            ...


```python
class Renderable(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

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


| Parameter | Type |
|-|-|
| `python_value` | `typing.Any` |

## flytekit.deck.renderer.SourceCodeRenderer

Convert Python source code to HTML, and return HTML as a unicode string.


```python
class SourceCodeRenderer(
    title: str,
)
```
| Parameter | Type |
|-|-|
| `title` | `str` |

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



| Parameter | Type |
|-|-|
| `source_code` | `str` |

## flytekit.deck.renderer.TopFrameRenderer

Render a DataFrame as an HTML table.


```python
class TopFrameRenderer(
    max_rows: int,
    max_cols: int,
)
```
| Parameter | Type |
|-|-|
| `max_rows` | `int` |
| `max_cols` | `int` |

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
| Parameter | Type |
|-|-|
| `df` | `pandas.DataFrame` |

