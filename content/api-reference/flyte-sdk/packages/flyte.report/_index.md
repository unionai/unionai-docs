---
title: flyte.report
version: 2.5.11
variants: +flyte +union
layout: py_api
---

# flyte.report

## Directory

### Classes

| Class | Description |
|-|-|
| [`Report`](../flyte.report/report) |  |
| [`Timeline`](../flyte.report/timeline) | Append a best-effort chronological timeline to a tab of the task report. |

### Methods

| Method | Description |
|-|-|
| [`abbreviate()`](#abbreviate) | HTML-escape ``value`` for a report row. |
| [`current_report()`](#current_report) | Get the current report. |
| [`duration_ms()`](#duration_ms) | Format the gap between two ISO-8601 timestamps as ``"<n> ms"`` (best-effort). |
| [`flush()`](#flush) | Flush the report. |
| [`get_tab()`](#get_tab) | Get a tab by name. |
| [`log()`](#log) | Log content to the main tab. |
| [`replace()`](#replace) | Get the report. |


## Methods

#### abbreviate()

```python
def abbreviate(
    value: typing.Any,
    limit: int,
) -> str
```
HTML-escape ``value`` for a report row.

Short values render inline. Longer ones collapse into an expandable ``&lt;details&gt;``:
the row shows a ``limit``-character preview with a ``+N`` overflow marker, and
clicking it reveals the full content (up to a hard cap). Nothing is dropped on the
floor, so a value that trails off in the report can always be opened in place.


| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Any` | |
| `limit` | `int` | |

#### current_report()

```python
def current_report()
```
Get the current report. This is a dummy report if not in a task context.



**Returns:** The current report.

#### duration_ms()

```python
def duration_ms(
    start_iso: typing.Any,
    end_iso: typing.Any,
) -> str
```
Format the gap between two ISO-8601 timestamps as ``"&lt;n&gt; ms"`` (best-effort).


| Parameter | Type | Description |
|-|-|-|
| `start_iso` | `typing.Any` | |
| `end_iso` | `typing.Any` | |

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



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the tab. |
| `create_if_missing` | `bool` | Whether to create the tab if it does not exist. |

**Returns:** The tab.

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



| Parameter | Type | Description |
|-|-|-|
| `content` | `str` | The content to log. |
| `do_flush` | `bool` | flush the report after logging. |

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



| Parameter | Type | Description |
|-|-|-|
| `content` | `str` | |
| `do_flush` | `bool` | |

**Returns:** The report.

