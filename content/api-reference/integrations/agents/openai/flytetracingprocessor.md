---
title: FlyteTracingProcessor
version: 2.6.2
variants: +flyte +union
layout: py_api
---

# FlyteTracingProcessor

**Package:** `flyteplugins.agents.openai`

Map OpenAI Agents spans onto the shared `flyteplugins.agents.core.ReportTimeline`.


## Parameters

```python
class FlyteTracingProcessor(
    tab_name: str = 'Agent',
)
```
| Parameter | Type | Description |
|-|-|-|
| `tab_name` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`force_flush()`](#force_flush) | Forces immediate processing of any queued traces/spans. |
| [`on_span_end()`](#on_span_end) | Called when a span completes execution. |
| [`on_span_start()`](#on_span_start) | Called when a new span begins execution. |
| [`on_trace_end()`](#on_trace_end) | Called when a trace completes execution. |
| [`on_trace_start()`](#on_trace_start) | Called when a new trace begins execution. |
| [`shutdown()`](#shutdown) | Called when the application stops to clean up resources. |


### force_flush()

```python
def force_flush()
```
Forces immediate processing of any queued traces/spans.



> [!NOTE]
> - Should process all queued items before returning
> - Useful before shutdown or when immediate processing is needed
> - May block while processing completes

### on_span_end()

```python
def on_span_end(
    span: typing.Any,
)
```
Called when a span completes execution.



| Parameter | Type | Description |
|-|-|-|
| `span` | `typing.Any` | The completed span containing execution results. |

> [!NOTE]
> - Called synchronously when span finishes
> - Should not block or raise exceptions
> - Good time to export/process the individual span

### on_span_start()

```python
def on_span_start(
    span: typing.Any,
)
```
Called when a new span begins execution.



| Parameter | Type | Description |
|-|-|-|
| `span` | `typing.Any` | The span that started. Contains operation details and context. |

> [!NOTE]
> - Called synchronously on span start
> - Should return quickly to avoid blocking execution
> - Spans are automatically nested under current trace/span

### on_trace_end()

```python
def on_trace_end(
    trace: typing.Any,
)
```
Called when a trace completes execution.



| Parameter | Type | Description |
|-|-|-|
| `trace` | `typing.Any` | The completed trace containing all spans and results. |

> [!NOTE]
> - Called synchronously when trace finishes
> - Good time to export/process the complete trace
> - Should handle cleanup of any trace-specific resources

### on_trace_start()

```python
def on_trace_start(
    trace: typing.Any,
)
```
Called when a new trace begins execution.



| Parameter | Type | Description |
|-|-|-|
| `trace` | `typing.Any` | The trace that started. Contains workflow name and metadata. |

> [!NOTE]
> - Called synchronously on trace start
> - Should return quickly to avoid blocking execution
> - Any errors should be caught and handled internally

### shutdown()

```python
def shutdown()
```
Called when the application stops to clean up resources.

Should perform any necessary cleanup like:
- Flushing queued traces/spans
- Closing connections
- Releasing resources


