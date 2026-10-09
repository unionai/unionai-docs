---
title: RunScopedIdGenerator
description: "Hands back the run's derived trace id when one has been pinned."
icon: braces
version: 2.11.2
variants: +flyte +union
layout: py_api
---

# RunScopedIdGenerator

**Package:** `flyteplugins.otel`

Hands back the run's derived trace id when one has been pinned.

OpenTelemetry gives no way to ask for a specific trace id when starting a span; the
tracer always asks its provider's id generator. Pinning the value around the one call
that needs it is the supported way in.

Everything else is delegated, so wrapping a provider that was configured elsewhere keeps
whatever id generation it already had.


## Parameters

```python
class RunScopedIdGenerator(
    delegate: IdGenerator | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `delegate` | `IdGenerator \| None` | |

## Methods

| Method | Description |
|-|-|
| [`generate_span_id()`](#generate_span_id) | Get a new span ID. |
| [`generate_trace_id()`](#generate_trace_id) | Get a new trace ID. |


### generate_span_id()

```python
def generate_span_id()
```
Get a new span ID.



**Returns:** A 64-bit int for use as a span ID

### generate_trace_id()

```python
def generate_trace_id()
```
Get a new trace ID.

Implementations should at least make the 56 least significant bits
uniformly random. Samplers like the `TraceIdRatioBased` sampler rely on
this randomness to make sampling decisions.

If the implementation does randomly generate the 56 least significant bits,
it should also implement `is_trace_id_random` to return True.

See `the specification on TraceIdRatioBased <https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/sdk.md#traceidratiobased>`_.



**Returns:** A 128-bit int for use as a trace ID

