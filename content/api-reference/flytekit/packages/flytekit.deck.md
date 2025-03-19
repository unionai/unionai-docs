---
title: flytekit.deck
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.deck


==========
Flyte Deck
==========

.. currentmodule:: flytekit.deck

Contains deck renderers provided by flytekit.

.. autosummary::
   :nosignatures:
   :template: custom.rst
   :toctree: generated/

   Deck
   TopFrameRenderer
   MarkdownRenderer
   SourceCodeRenderer

## Directory

### Classes

| Class | Description |
|-|-|
| [`Deck`](.././flytekit.deck#flytekitdeckdeck) | Deck enable users to get customizable and default visibility into their tasks. |
| [`DeckField`](.././flytekit.deck#flytekitdeckdeckfield) | DeckField is used to specify the fields that will be rendered in the deck. |
| [`MarkdownRenderer`](.././flytekit.deck#flytekitdeckmarkdownrenderer) | Convert a markdown string to HTML and return HTML as a unicode string. |
| [`SourceCodeRenderer`](.././flytekit.deck#flytekitdecksourcecoderenderer) | Convert Python source code to HTML, and return HTML as a unicode string. |
| [`TopFrameRenderer`](.././flytekit.deck#flytekitdecktopframerenderer) | Render a DataFrame as an HTML table. |

## flytekit.deck.Deck

Deck enable users to get customizable and default visibility into their tasks.

Deck contains a list of renderers (FrameRenderer, MarkdownRenderer) that can
generate a html file. For example, FrameRenderer can render a DataFrame as an HTML table,
MarkdownRenderer can convert Markdown string to HTML

Flyte context saves a list of deck objects, and we use renderers in those decks to render
the data and create an HTML file when those tasks are executed

Each task has a least three decks (input, output, default). Input/output decks are
used to render tasks' input/output data, and the default deck is used to render line plots,
scatter plots or Markdown text. In addition, users can create new decks to render
their data with custom renderers.

.. code-block:: python

iris_df = px.data.iris()

@task()
def t1() -> str:
md_text = '#Hello Flyte##Hello Flyte###Hello Flyte'
m = MarkdownRenderer()
s = BoxRenderer("sepal_length")
deck = flytekit.Deck("demo", s.to_html(iris_df))
deck.append(m.to_html(md_text))
default_deck = flytekit.current_context().default_deck
default_deck.append(m.to_html(md_text))
return md_text


# Use Annotated to override default renderer
@task()
def t2() -> Annotated[pd.DataFrame, TopFrameRenderer(10)]:
return iris_df


```python
def Deck(
    name: str,
    html: typing.Optional[str],
    auto_add_to_deck: bool,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `html` | `typing.Optional[str]` |
| `auto_add_to_deck` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`append()`](#append) | None |
| [`publish()`](#publish) | None |


#### append()

```python
def append(
    html: str,
):
```
| Parameter | Type |
|-|-|
| `html` | `str` |

#### publish()

```python
def publish()
```
### Properties

| Property | Type | Description |
|-|-|-|
| html |  |  |
| name |  |  |

## flytekit.deck.DeckField

DeckField is used to specify the fields that will be rendered in the deck.


```python
def DeckField(
    args,
    kwds,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwds` |  |

## flytekit.deck.MarkdownRenderer

Convert a markdown string to HTML and return HTML as a unicode string.


### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) | None |


#### to_html()

```python
def to_html(
    text: str,
):
```
| Parameter | Type |
|-|-|
| `text` | `str` |

## flytekit.deck.SourceCodeRenderer

Convert Python source code to HTML, and return HTML as a unicode string.


```python
def SourceCodeRenderer(
    title: str,
):
```
| Parameter | Type |
|-|-|
| `title` | `str` |

### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) | Convert the provided Python source code into HTML format using Pygments library |


#### to_html()

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

## flytekit.deck.TopFrameRenderer

Render a DataFrame as an HTML table.


```python
def TopFrameRenderer(
    max_rows: int,
    max_cols: int,
):
```
| Parameter | Type |
|-|-|
| `max_rows` | `int` |
| `max_cols` | `int` |

### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) | None |


#### to_html()

```python
def to_html(
    df: pandas.DataFrame,
):
```
| Parameter | Type |
|-|-|
| `df` | `pandas.DataFrame` |

