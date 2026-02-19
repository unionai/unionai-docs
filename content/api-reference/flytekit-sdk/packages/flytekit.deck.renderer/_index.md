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
| [`ArrowRenderer`](../flytekit.deck.renderer/arrowrenderer) | Render an Arrow dataframe as an HTML table. |
| [`MarkdownRenderer`](../flytekit.deck.renderer/markdownrenderer) | Convert a markdown string to HTML and return HTML as a unicode string. |
| [`PythonDependencyRenderer`](../flytekit.deck.renderer/pythondependencyrenderer) | PythonDependencyDeck is a deck that contains information about packages installed via pip. |
| [`SourceCodeRenderer`](../flytekit.deck.renderer/sourcecoderenderer) | Convert Python source code to HTML, and return HTML as a unicode string. |
| [`TopFrameRenderer`](../flytekit.deck.renderer/topframerenderer) | Render a DataFrame as an HTML table. |

### Protocols

| Protocol | Description |
|-|-|
| [`Renderable`](../flytekit.deck.renderer/renderable) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_MAX_COLS` | `int` |  |
| `DEFAULT_MAX_ROWS` | `int` |  |
| `TYPE_CHECKING` | `bool` |  |

