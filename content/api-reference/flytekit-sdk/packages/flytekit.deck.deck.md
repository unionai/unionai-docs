---
title: flytekit.deck.deck
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.deck.deck

## Directory

### Classes

| Class | Description |
|-|-|
| [`Deck`](.././flytekit.deck.deck#flytekitdeckdeckdeck) | Deck enable users to get customizable and default visibility into their tasks. |
| [`TimeLineDeck`](.././flytekit.deck.deck#flytekitdeckdecktimelinedeck) | The TimeLineDeck class is designed to render the execution time of each part of a task. |

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
| Parameter | Type |
|-|-|
| `data` | `dict` |

#### get_deck_template()

```python
def get_deck_template()
```
## flytekit.deck.deck.Deck

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

```python
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
```


```python
class Deck(
    name: str,
    html: typing.Optional[str],
    auto_add_to_deck: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `html` | `typing.Optional[str]` |
| `auto_add_to_deck` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`append()`](#append) |  |
| [`publish()`](#publish) |  |


#### append()

```python
def append(
    html: str,
) -> Deck
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
| `html` |  |  |
| `name` |  |  |

## flytekit.deck.deck.TimeLineDeck

The TimeLineDeck class is designed to render the execution time of each part of a task.
Unlike deck class, the conversion of data to HTML is delayed until the html property is accessed.
This approach is taken because rendering a timeline graph with partial data would not provide meaningful insights.
Instead, the complete data set is used to create a comprehensive visualization of the execution time of each part of the task.


```python
class TimeLineDeck(
    name: str,
    html: typing.Optional[str],
    auto_add_to_deck: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `html` | `typing.Optional[str]` |
| `auto_add_to_deck` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`append()`](#append) |  |
| [`append_time_info()`](#append_time_info) |  |
| [`publish()`](#publish) |  |


#### append()

```python
def append(
    html: str,
) -> Deck
```
| Parameter | Type |
|-|-|
| `html` | `str` |

#### append_time_info()

```python
def append_time_info(
    info: dict,
)
```
| Parameter | Type |
|-|-|
| `info` | `dict` |

#### publish()

```python
def publish()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `html` |  |  |
| `name` |  |  |

