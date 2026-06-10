---
title: OpenTelemetry
weight: 1
variants: +flyte +union
---

# OpenTelemetry

[OpenTelemetry](https://opentelemetry.io/) (OTel) tracing in Flyte 2 is user-owned. Flyte exposes a context-propagation primitive — [`custom_context`](../../user-guide/task-programming/custom-context) — that lets you carry the W3C `traceparent` header (and any other tracing metadata) across task boundaries. You bring the rest of the OTel stack: tracer provider, span exporter, and any instrumentation libraries you need.

Unlike the other entries in this section, OpenTelemetry is not a Flyte plugin. It is a usage pattern built on top of `custom_context` plus the standard `opentelemetry-*` packages.

## What Flyte provides

| Capability                                                             | Where it lives                                        |
| ---------------------------------------------------------------------- | ----------------------------------------------------- |
| Trace context propagation across task boundaries                       | `flyte.custom_context` / `flyte.ctx().custom_context` |
| Tracer provider and span exporter                                      | Your code (`opentelemetry-sdk`)                       |
| Auto-instrumentation for libraries (httpx, requests, SQLAlchemy, etc.) | Your code (`opentelemetry-instrumentation-*`)         |
| Span emission for Flyte control-plane API calls                        | Not exposed                                           |
| Span emission for task lifecycle (scheduling, retries)                 | Not exposed                                           |

Flyte does not emit OTel spans into your collector. Every span that shows up in your tracing backend is one you create from inside your own code.

## Installation

Add the OTel libraries to your task image:

```python
image = flyte.Image.from_debian_base().with_pip_packages(
    "opentelemetry-sdk",
    "opentelemetry-instrumentation-httpx",   # one per library you want auto-instrumented
    "httpx",
)
```

The same packages must also be importable in the driver process that calls `flyte.with_runcontext(...).run(...)`.

## Configure the tracer

Initialize a tracer provider and exporter once at module import. The example below uses `ConsoleSpanExporter` for clarity — in production swap in an OTLP, Jaeger, or vendor-specific exporter that points at your collector.

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
HTTPXClientInstrumentor().instrument()
tracer = trace.get_tracer("my.app")
```

## Start a trace and pass it into the run

Open a root span in your driver code, inject the resulting trace context into a carrier dict, and hand it to the run via `with_runcontext(custom_context=...)`:

```python
from opentelemetry.propagate import inject

with tracer.start_as_current_span("workflow_run"):
    carrier = {}
    inject(carrier)   # writes traceparent (and tracestate/baggage if configured) into carrier
    run = flyte.with_runcontext(custom_context=carrier).run(main, url="https://httpbin.org/get")
    print(run.url)
```

The carrier is a regular `Dict[str, str]`, which is exactly what `custom_context` expects.

## Re-parent spans inside a task

Each task pulls the parent context out of `flyte.ctx().custom_context` and uses it to anchor its own spans:

```python
import httpx
from opentelemetry.propagate import extract

@env.task
async def fetch(url: str) -> int:
    parent = extract(flyte.ctx().custom_context)
    with tracer.start_as_current_span("fetch", context=parent):
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
        return resp.status_code
```

Without `extract(...)`, the span you open inside the task would be a new root span in your tracing backend, disconnected from the rest of the workflow.

## Propagate into nested tasks

When a task calls another task, refresh the carrier with the current span and pass it through `flyte.custom_context(...)` so the child task's `flyte.ctx().custom_context` carries the updated parent:

```python
from opentelemetry.propagate import extract, inject

@env.task
async def main(url: str) -> int:
    parent = extract(flyte.ctx().custom_context)
    with tracer.start_as_current_span("main", context=parent):
        carrier = {}
        inject(carrier)
        with flyte.custom_context(**carrier):
            return await fetch(url)
```

The pattern composes — every task that opens a span and calls another task repeats the `inject` + `flyte.custom_context(...)` step.

## Reusable decorator

The `extract` / `start_as_current_span` / `inject` / `flyte.custom_context` sequence is mechanical. Wrap it in a decorator so task bodies stay clean:

```python
import functools
from opentelemetry.propagate import extract, inject

def traced(span_name: str):
    def decorator(fn):
        @functools.wraps(fn)
        async def wrapper(*args, **kwargs):
            parent = extract(flyte.ctx().custom_context)
            with tracer.start_as_current_span(span_name, context=parent):
                carrier = {}
                inject(carrier)
                with flyte.custom_context(**carrier):
                    return await fn(*args, **kwargs)
        return wrapper
    return decorator


@env.task
@traced("fetch")
async def fetch(url: str) -> int:
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
    return resp.status_code
```

## Choosing an exporter

`ConsoleSpanExporter` only prints to stdout. To send spans to a real backend, replace it with the exporter that targets your collector — for example:

- **OTLP** (most collectors, including the OpenTelemetry Collector): `opentelemetry-exporter-otlp`
- **Jaeger**: `opentelemetry-exporter-jaeger`
- **Vendor exporters**: Datadog, Honeycomb, New Relic, Splunk, etc. — each ships its own pip package.

The exporter, endpoint, and credentials are configured entirely in your task code; Flyte does not mediate that connection.
