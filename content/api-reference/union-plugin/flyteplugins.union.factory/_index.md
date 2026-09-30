---
title: flyteplugins.union.factory
description: "Factories: a declared graph of partitioned artifacts the platform can materialize on demand."
icon: box-seam
version: 0.15.0
variants: -flyte +union
layout: py_api
---

# flyteplugins.union.factory

Factories: a declared graph of partitioned artifacts the platform can materialize on demand.

A factory is written in its own module, optionally in its own project, and wires
together tasks owned by other teams without those tasks changing. Deploying it produces
an ordinary task of type ``factory``; running that task for a target and a partition
selector is a *materialization*. Backfill is a materialization over a range.

Typical use::

    from flyte.remote import Task
    from flyteplugins.union import factory

    clean = Task.get("ingest.clean", auto_version="latest")
    report = Task.get("analytics.report", auto_version="latest")

    raw = factory.source("raw_events")  # type and partitions come from the registry
    events = factory.build("events").using(clean, raw=raw, min_quality=30)
    daily_report = factory.build("daily_report").using(report, events=events.all("region"))

    analytics = factory.Factory("analytics", daily_report)
    analytics.deploy()
    run = analytics.materialize(daily_report, date="2026-08-01..2026-08-31")

A factory can end in a running app. ``serve`` names the app and binds its parameters to
artifacts; a materialization deploys it with the versions it resolved::

    endpoint = factory.serve("qwen3-chat").using(chat_app, model_path=approved)

``source``, ``build`` and ``serve`` declare; nothing runs until ``materialize``. A build's names line up
with its task's return tuple, and ``"_"`` skips an output that is not an artifact::

    model, metrics = factory.build("_", "model", "metrics").using(train, data=features)

Partitions are identity in the artifact registry: a version is published with its typed
partition values (one time partition with a granularity, any number of string partitions)
and looked up by them. A source needs no ``type=`` or ``partitions=`` when the registry
already knows the artifact; deploy reads them from it::

    raw = factory.source("raw_events")
## Directory

### Classes

| Class | Description |
|-|-|
| [`Factory`](../flyteplugins.union.factory/factory) | A set of builds. |
| [`TimeRange`](../flyteplugins.union.factory/timerange) | A trailing window, relative to the consumer's own time value, ending at that value. |

### Methods

| Method | Description |
|-|-|
| [`build()`](#build) | Name the artifact (or artifacts) one task call makes. |
| [`materialize()`](#materialize) | Start a run of ``<factory>.materialize`` and return the ``flyte.remote.Run``. |
| [`on()`](#on) | Materialize when a source gets a new version, or on a schedule. |
| [`partition()`](#partition) | Pass the instance's value of ``dim`` to a task parameter. |
| [`serve()`](#serve) | Name the app a factory ends in. |
| [`source()`](#source) | An artifact made outside this factory. |


### Variables

| Property | Type | Description |
|-|-|-|
| `Daily` | `_Granularity` |  |
| `Hourly` | `_Granularity` |  |
| `Monthly` | `_Granularity` |  |
| `Weekly` | `_Granularity` |  |

## Methods

#### build()

```python
def build(
    *outputs: str,
    partitions: Optional[Mapping[str, DimensionType]] = None,
    runcontext: Optional[Mapping[str, Any]] = None,
    backfill: str = 'partition',
    project: Optional[str] = None,
    domain: Optional[str] = None,
    kind: Union[None, ArtifactKind, Mapping[str, ArtifactKind]] = None,
    description: str = '',
) -> BuildSpec
```
Name the artifact (or artifacts) one task call makes. Follow with ``.using(task, **args)``.

``outputs`` lines up with the task's return tuple, left to right. Use ``"_"`` for an
output that is not an artifact::

    events = factory.build("events").using(clean, raw=raw_events)
    model, metrics = factory.build("_", "model", "metrics", "_").using(train, data=features)



| Parameter | Type | Description |
|-|-|-|
| `*outputs` | `str` | |
| `partitions` | `Optional[Mapping[str, DimensionType]]` | Only needed when the outputs have a dimension none of the inputs carry. Otherwise the dimensions follow from the inputs. |
| `runcontext` | `Optional[Mapping[str, Any]]` | Settings for this build's task call: ``queue``, ``env_vars``, ``service_account``. Anything that needs a run of its own is rejected at deploy. |
| `backfill` | `str` | ``"partition"`` (one action per partition) or ``"range"``. |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `kind` | `Union[None, ArtifactKind, Mapping[str, ArtifactKind]]` | Artifact kind (``"model"``, ``"data"`` or ``"generic"``), or a mapping of artifact name to kind. |
| `description` | `str` | |

#### materialize()

```python
def materialize(
    factory_name: str,
    target: Union[ArtifactHandle, str],
    partitions: Mapping[str, Any],
    params: Optional[Mapping[str, Mapping[str, Any]]] = None,
    rebuild: Optional[Sequence[Any]] = None,
    rebuild_all: bool = False,
    downstream: bool = False,
    plan_only: bool = False,
    concurrency: int = 0,
    queue: Optional[str] = None,
    versions: Optional[Mapping[str, str]] = None,
    nodes: Optional[Mapping[str, ArtifactHandle]] = None,
    project: Optional[str] = None,
    domain: Optional[str] = None,
    run_name: Optional[str] = None,
)
```
Start a run of ``<factory>.materialize`` and return the ``flyte.remote.Run``.

``queue`` puts the materialization run and every build it makes on that queue. ``versions``
pins artifacts to versions (``{"tracks": "v2"}``): a source is read at that version instead of
its latest, and a built artifact is read at that version instead of being built, which is how an
endpoint is rolled back.


| Parameter | Type | Description |
|-|-|-|
| `factory_name` | `str` | |
| `target` | `Union[ArtifactHandle, str]` | |
| `partitions` | `Mapping[str, Any]` | |
| `params` | `Optional[Mapping[str, Mapping[str, Any]]]` | |
| `rebuild` | `Optional[Sequence[Any]]` | |
| `rebuild_all` | `bool` | |
| `downstream` | `bool` | |
| `plan_only` | `bool` | |
| `concurrency` | `int` | |
| `queue` | `Optional[str]` | |
| `versions` | `Optional[Mapping[str, str]]` | |
| `nodes` | `Optional[Mapping[str, ArtifactHandle]]` | |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `run_name` | `Optional[str]` | |

#### on()

```python
def on(
    event: Event,
    *targets: ArtifactHandle,
    lag: Optional[TimeRange] = None,
    name: Optional[str] = None,
    **filter: str,
) -> On
```
Materialize when a source gets a new version, or on a schedule.

``event`` is a ``factory.source`` handle or a ``flyte.Cron`` / ``flyte.FixedRate``. ``targets``
are the artifacts or endpoints to materialize; by default, everything the factory produces
downstream of the source (for a source event) or everything it produces (for a schedule).
Acting on each new version of something the factory builds needs no trigger: add a build
that reads it::

    beans = factory.Factory("beans", api, predictions, triggers=[
        factory.on(images),                                    # score each new day of images
        factory.on(flyte.Cron("0 3 * * *"), api),              # nightly: retrain if anything changed
        factory.on(flyte.Cron("0 2 * * *"), report, lag=factory.TimeRange(days=1)),  # yesterday
    ])

A source event materializes the partition the new version belongs to; dimensions the event
does not carry are materialized for every value the registry knows. A schedule materializes
the fire time in the schedule's timezone, moved back by ``lag`` and rounded down to each target's
time granularity. Keyword arguments filter a source event by a string partition, e.g.
``factory.on(raw, region="us")``; ``lag`` and ``name`` are this function's own, so a dimension
with either name cannot be filtered on.

When nothing changed, a triggered materialization is all cache hits and finishes in seconds.


| Parameter | Type | Description |
|-|-|-|
| `event` | `Event` | |
| `*targets` | `ArtifactHandle` | |
| `lag` | `Optional[TimeRange]` | |
| `name` | `Optional[str]` | |
| `**filter` | `str` | |

#### partition()

```python
def partition(
    dim: str,
) -> PartitionValue
```
Pass the instance's value of ``dim`` to a task parameter.

``factory.build("events").using(clean, raw=raw_events, day=factory.partition("date"))``
calls ``clean`` with ``day`` set to the date being built. A parameter that is left unset
and has the same name as a dimension receives that dimension's value without this.


| Parameter | Type | Description |
|-|-|-|
| `dim` | `str` | |

#### serve()

```python
def serve(
    name: str,
    description: str = '',
) -> ServeSpec
```
Name the app a factory ends in. Follow with ``.using(app, **params)``.

``name`` is the app's name. Each keyword binds one of the app's parameters to an artifact,
the way ``build(...).using(task, **args)`` binds task arguments::

    chat = VLLMAppEnvironment(name="qwen3-chat", model_path=ArtifactValue("qwen3-approved"), ...)
    endpoint = factory.serve("qwen3-chat").using(chat, model_path=approved)
    qwen = factory.Factory("qwen3", endpoint)

A materialization deploys the app with each parameter set to the artifact version it resolved,
and leaves an app whose spec did not change alone. An endpoint is one app: materializing a range
of partitions deploys the newest one. The app keeps whatever the definition says about its image,
resources and scaling.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `description` | `str` | |

#### source()

```python
def source(
    name: str,
    project: Optional[str] = None,
    domain: Optional[str] = None,
    type: Any = None,
    partitions: Optional[Mapping[str, DimensionType]] = None,
    kind: Optional[ArtifactKind] = None,
    description: str = '',
) -> ArtifactHandle
```
An artifact made outside this factory. The factory resolves it from the registry.

``type`` and ``partitions`` may be left out: at deploy they are read from the registry,
which fixed the partition keys with the artifact's first version (or a declaration).
When ``partitions`` is given and the registry already has a schema for the name, the two
must agree; when it has none, deploy declares it.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Artifact name in the registry. |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `type` | `Any` | The value type the artifact holds (``flyte.io.File``, ``Dir``, or ``DataFrame``). |
| `partitions` | `Optional[Mapping[str, DimensionType]]` | Dimension name to ``str``, ``int``, ``factory.Daily``, ``factory.Hourly``, ``factory.Weekly``, or ``factory.Monthly``. |
| `kind` | `Optional[ArtifactKind]` | Optional artifact kind (``model``, ``data``, ``generic``). |
| `description` | `str` | |

