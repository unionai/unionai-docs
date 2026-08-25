---
title: ReportTimeline
version: 2.6.6
variants: +flyte +union
layout: py_api
---

# ReportTimeline

**Package:** `flyteplugins.agents.core`

A `flyte.report.Timeline` that defaults to the `Agent` report tab.


## Parameters

```python
class ReportTimeline(
    tab_name: str = 'Agent',
)
```
| Parameter | Type | Description |
|-|-|-|
| `tab_name` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`heading()`](#heading) |  |
| [`row()`](#row) |  |


### heading()

```python
def heading(
    text: typing.Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `text` | `typing.Any` | |

### row()

```python
def row(
    icon: str = '•',
    label: typing.Any = '',
    meta: str = '',
    detail: str = '',
    error: typing.Any = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `icon` | `str` | |
| `label` | `typing.Any` | |
| `meta` | `str` | |
| `detail` | `str` | |
| `error` | `typing.Any` | |

