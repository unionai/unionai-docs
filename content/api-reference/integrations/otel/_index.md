---
title: OpenTelemetry
description: "OpenTelemetry tracing for Flyte."
icon: book
version: 2.11.1
variants: +flyte +union
layout: py_api
---

# OpenTelemetry



OpenTelemetry tracing for Flyte.

Every task becomes a span, every `flyte.trace` step becomes a child span inside it, and
spans created by your own code or by any instrumentation library nest underneath without
wiring. Export goes wherever OTLP goes.

Usage:

    import flyte
    from flyteplugins.otel import init

    # At module scope, not inside a task: the task span opens before the task body runs.
    init(service_name="my-service")

    env = flyte.TaskEnvironment(name="my_env")

    @env.task
    async def main(n: int) -> int:
        ...

With no arguments `init` reads OTEL_EXPORTER_OTLP_ENDPOINT and OTEL_EXPORTER_OTLP_HEADERS,
so pointing it at a vendor is a matter of setting those usually from a `flyte.Secret`. If
you already configure OpenTelemetry yourself, pass `tracer_provider` and your setup is
adopted unchanged.

Trace context travels in Flyte's `custom_context` as a W3C carrier in both directions: a
run submitted inside a caller's span joins that trace, and a child task nests under the task
that spawned it even though it runs in another pod.

Two things are specific to Flyte being durable. When no trace context arrives from outside,
the trace id is derived from the run identity, so the several processes that make up a
crashed-and-resumed run all record into one trace with no coordination. And steps that a
resumed run served from its durable log, which never execute and so would otherwise be
missing, are recorded as spans marked `flyte.replayed`.
## Directory

### Classes

| Class | Description |
|-|-|
| [`OtelObserver`](./otelobserver) | A `flyte._observe.Observer` that records spans. |
| [`RunScopedIdGenerator`](./runscopedidgenerator) | Hands back the run's derived trace id when one has been pinned. |

### Methods

| Method | Description |
|-|-|
| [`format_trace_id()`](#format_trace_id) | Render a trace id the way backends display it: 32 lowercase hex characters. |
| [`get_tracer()`](#get_tracer) | The tracer `init` built for handing to another instrumentation library. |
| [`init()`](#init) | Start recording Flyte tasks and trace steps as OpenTelemetry spans. |
| [`shutdown()`](#shutdown) | Unregister the observer and flush pending spans. |
| [`trace_id_for_run()`](#trace_id_for_run) | The trace id shared by every span in this run, across attempts and containers. |


## Methods

#### format_trace_id()

```python
def format_trace_id(
    trace_id: int,
) -> str
```
Render a trace id the way backends display it: 32 lowercase hex characters.


| Parameter | Type | Description |
|-|-|-|
| `trace_id` | `int` | |

#### get_tracer()

```python
def get_tracer()
```
The tracer `init` built for handing to another instrumentation library.

Libraries that create their own provider still nest correctly since parenting comes from
the active context rather than the provider. Sharing the tracer just keeps everything on
one export pipeline.


#### init()

```python
def init(
    service_name: Optional[str] = None,
    endpoint: Optional[str] = None,
    headers: Union[Mapping[str, str], str, None] = None,
    protocol: Optional[str] = None,
    resource_attributes: Optional[Mapping[str, Any]] = None,
    exporter: Union[SpanExporter, Sequence[SpanExporter], None] = None,
    tracer_provider: Optional[trace_api.TracerProvider] = None,
    disable_batch: bool = False,
    set_global: bool = True,
) -> OtelObserver
```
Start recording Flyte tasks and trace steps as OpenTelemetry spans.

Call this once at module scope, not inside a task. The task span opens before the task
body runs, so initializing from within the body means that task's own span has already
been missed. Module scope runs during import, which happens before any task starts.

With no arguments it reads the standard OTEL_EXPORTER_OTLP_ENDPOINT and
OTEL_EXPORTER_OTLP_HEADERS variables, which is the shape most vendors document.

If you already configure OpenTelemetry yourself, pass `tracer_provider` and none of the
exporter arguments. The provider is adopted as it stands, with its sampler, resource, and
exporters untouched; only its id generator is wrapped, so run derived trace ids keep
working without you giving up your own setup.



| Parameter | Type | Description |
|-|-|-|
| `service_name` | `Optional[str]` | Value for service.name. Defaults to OTEL_SERVICE_NAME, then "flyte". Not used when adopting a provider, which carries its own resource. |
| `endpoint` | `Optional[str]` | OTLP endpoint. On http/protobuf a base gateway URL is fine and the traces path is added; on grpc the base endpoint is used as given. |
| `headers` | `Union[Mapping[str, str], str, None]` | Export headers, as a mapping or the "k=v,k2=v2" form. |
| `protocol` | `Optional[str]` | OTLP transport, "http/protobuf" or "grpc". Defaults to OTEL_EXPORTER_OTLP_TRACES_PROTOCOL, then OTEL_EXPORTER_OTLP_PROTOCOL, then http/protobuf. gRPC needs the [grpc] extra. |
| `resource_attributes` | `Optional[Mapping[str, Any]]` | Extra resource attributes to attach to every span. |
| `exporter` | `Union[SpanExporter, Sequence[SpanExporter], None]` | Export through this instead of building an OTLP exporter, or pass several to fan out — a ConsoleSpanExporter alongside a real backend, say. Any `SpanExporter` works; nothing here requires OTLP. |
| `tracer_provider` | `Optional[trace_api.TracerProvider]` | Adopt a provider you configured yourself instead of building one. Cannot be combined with the exporter building arguments. |
| `disable_batch` | `bool` | Export each span as it ends. Slower, but nothing is lost if the process dies, which matters when the thing being demonstrated is a crash. |
| `set_global` | `bool` | Install the provider as the global one, so other instrumentation shares it. Not used when adopting a provider, which is assumed to be installed already. |

**Returns**

The registered observer, which can be passed to `shutdown`.


**Raises**

| Exception | Description |
|-|-|
| `ValueError` | If tracer_provider is combined with the exporter building arguments. |

#### shutdown()

```python
def shutdown()
```
Unregister the observer and flush pending spans.


#### trace_id_for_run()

```python
def trace_id_for_run(
    action: 'ActionID',
) -> int
```
The trace id shared by every span in this run, across attempts and containers.

Derived from the fully qualified run identity rather than the run name alone, so two
runs that happen to share a name in different projects or domains stay distinct.


| Parameter | Type | Description |
|-|-|-|
| `action` | `'ActionID'` | |

