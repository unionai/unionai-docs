---
title: flyte.report
version: 0.2.0b9.dev1+g28a3f43
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.report

## Directory

### Classes

| Class | Description |
|-|-|
| [`Report`](.././flyte.report#flytereportreport) |  |

### Methods

| Method | Description |
|-|-|
| [`current_report()`](#current_report) | Get the current report. |
| [`get_tab()`](#get_tab) | Get a tab by name. |


## Methods

#### current_report()

```python
def current_report()
```
Get the current report. This is a dummy report if not in a task context.

:return: The current report.


#### get_tab()

```python
def get_tab(
    name: str,
    create_if_missing: bool,
) -> flyte.report._report.Tab
```
Get a tab by name. If the tab does not exist, create it.



| Parameter | Type |
|-|-|
| `name` | `str` |
| `create_if_missing` | `bool` |

## flyte.report.Report

```python
class Report(
    name: str,
    tabs: typing.Dict[str, flyte.report._report.Tab],
    template_path: pathlib._local.Path,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `tabs` | `typing.Dict[str, flyte.report._report.Tab]` |
| `template_path` | `pathlib._local.Path` |

### Methods

| Method | Description |
|-|-|
| [`get_final_report()`](#get_final_report) | Get the final report as a string. |
| [`get_tab()`](#get_tab) | Get a tab by name. |


#### get_final_report()

```python
def get_final_report()
```
Get the final report as a string.

:return: The final report.


#### get_tab()

```python
def get_tab(
    name: str,
    create_if_missing: bool,
) -> flyte.report._report.Tab
```
Get a tab by name. If the tab does not exist, create it.



| Parameter | Type |
|-|-|
| `name` | `str` |
| `create_if_missing` | `bool` |

