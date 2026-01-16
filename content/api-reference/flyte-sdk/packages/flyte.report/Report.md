---
title: Report
version: 2.0.0b48
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Report

**Package:** `flyte.report`

```python
class Report(
    name: str,
    tabs: typing.Dict[str, flyte.report._report.Tab],
    template_path: pathlib._local.Path,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `tabs` | `typing.Dict[str, flyte.report._report.Tab]` | |
| `template_path` | `pathlib._local.Path` | |

## Methods

| Method | Description |
|-|-|
| [`get_final_report()`](#get_final_report) | Get the final report as a string. |
| [`get_tab()`](#get_tab) | Get a tab by name. |


### get_final_report()

```python
def get_final_report()
```
Get the final report as a string.

:return: The final report.


### get_tab()

```python
def get_tab(
    name: str,
    create_if_missing: bool,
) -> flyte.report._report.Tab
```
Get a tab by name. If the tab does not exist, create it.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the tab. |
| `create_if_missing` | `bool` | Whether to create the tab if it does not exist. :return: The tab. |

