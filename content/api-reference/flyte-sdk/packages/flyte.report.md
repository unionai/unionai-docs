---
title: flyte.report
version: 2.0.0b33
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
| [`flush()`](#flush) | Flush the report. |
| [`get_tab()`](#get_tab) | Get a tab by name. |
| [`log()`](#log) | Log content to the main tab. |
| [`replace()`](#replace) | Get the report. |


## Methods

#### current_report()

```python
def current_report()
```
Get the current report. This is a dummy report if not in a task context.

:return: The current report.


#### flush()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await flush.aio()`.
```python
def flush()
```
Flush the report.


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
| `name` | {{< multiline >}}`str`
doc: The name of the tab.
{{< /multiline >}} |
| `create_if_missing` | {{< multiline >}}`bool`
doc: Whether to create the tab if it does not exist.
:return: The tab.
{{< /multiline >}} |

#### log()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await log.aio()`.
```python
def log(
    content: str,
    do_flush: bool,
)
```
Log content to the main tab. The content should be a valid HTML string, but not a complete HTML document,
 as it will be inserted into a div.



| Parameter | Type |
|-|-|
| `content` | {{< multiline >}}`str`
doc: The content to log.
{{< /multiline >}} |
| `do_flush` | {{< multiline >}}`bool`
doc: flush the report after logging.
{{< /multiline >}} |

#### replace()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await replace.aio()`.
```python
def replace(
    content: str,
    do_flush: bool,
)
```
Get the report. Replaces the content of the main tab.

:return: The report.


| Parameter | Type |
|-|-|
| `content` | `str` |
| `do_flush` | `bool` |

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
| `name` | {{< multiline >}}`str`
doc: The name of the tab.
{{< /multiline >}} |
| `create_if_missing` | {{< multiline >}}`bool`
doc: Whether to create the tab if it does not exist.
:return: The tab.
{{< /multiline >}} |

