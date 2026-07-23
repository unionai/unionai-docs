---
title: Timeline
version: 2.5.12
variants: +flyte +union
layout: py_api
---

# Timeline

**Package:** `flyte.report`

Append a best-effort chronological timeline to a tab of the task report.

Writes are skipped silently when there is no active report (running locally, or the
task was not created with ``report=True``), so rendering a timeline never breaks the
work it is observing.


## Parameters

```python
class Timeline(
    tab_name: str,
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
    icon: str,
    label: typing.Any,
    meta: str,
    detail: str,
    error: typing.Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `icon` | `str` | |
| `label` | `typing.Any` | |
| `meta` | `str` | |
| `detail` | `str` | |
| `error` | `typing.Any` | |

