---
title: Artifact
description: "A published artifact in the Flyte artifact service: a typed value (stored as a Flyte literal) addressed by org/project/domain/name/version."
icon: braces
version: 2.10.0
variants: +flyte +union
layout: py_api
---

# Artifact

**Package:** `flyte.remote`

A published artifact in the Flyte artifact service: a typed value (stored as
a Flyte literal) addressed by org/project/domain/name/version.


## Parameters

```python
class Artifact(
    pb2: artifact_pb2.Artifact,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `artifact_pb2.Artifact` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `artifact_version_id` | `artifact_id_pb2.ArtifactVersionId` | The artifact's typed identity, as stamped onto values (core.Literal.artifact_id). |
| `created_by` | `str` | Best-effort display string for the creating identity (EnrichedIdentity). |
| `kind` | `Kind` | What this artifact is: "model", "data", or "generic".  Read from the reserved `flyte.io/kind` attr. Artifacts published before that key existed fall back to the card's type, which was the closest thing to a discriminator at the time -- so an older model with a card still classifies. Anything with neither marker is "generic": callers get a usable answer rather than None, since "unlabelled" and "not a model" are the same thing here. |
| `name` | `str` |  |
| `partitions` | `dict[str, Any]` | The version's partition values by key: a `date` for a daily (or coarser) time partition, a `datetime` in UTC for an hourly one, strings otherwise. Empty for an unpartitioned artifact. |
| `source` | `str` | Best-effort display string for the artifact's provenance (ArtifactSource). |
| `source_action_url` | `str \| None` | Console URL of the action that produced this artifact, or None if no task produced it. |
| `source_run_url` | `str \| None` | Console URL of the run that produced this artifact, or None if no task produced it. |
| `time_partition` | `artifact_id_pb2.TimePartition \| None` | The stored time partition message (key, floored value, granularity), or None. |
| `tracker` | `str` | The artifact's id as a tracking string: org/project/domain/name@version. |
| `url` | `str` | Get the console URL for viewing this artifact. |
| `version` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`coerce_to_literal()`](#coerce_to_literal) | Coerce the artifact's stored literal to the shape `python_type` expects. |
| [`create()`](#create) | Publish an artifact from the local machine. |
| [`declare()`](#declare) | Fix an artifact name's partition keys ahead of any version. |
| [`delete()`](#delete) | Delete this artifact from the remote system. |
| [`get()`](#get) | Get an artifact by its name and version, or the latest version of one partition. |
| [`get_schema()`](#get_schema) | The partition keys fixed for an artifact name. |
| [`list_names()`](#list_names) | List distinct artifact names, one entry per name carrying the latest version and the total version count, newest activity first. |
| [`listall()`](#listall) | List artifacts, newest first. |
| [`partition_values()`](#partition_values) | The distinct values one partition key has among an artifact's versions, sorted ascending, optionally scoped by the other keys. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`to_python()`](#to_python) | Materialize the artifact's stored literal back into a python value. |


### coerce_to_literal()

```python
def coerce_to_literal(
    python_type: Type | None = None,
) -> literals_pb2.Literal
```
Coerce the artifact's stored literal to the shape `python_type` expects.

Round-trips the stored literal through the type engine — `to_python_value`
against the declared type, then `to_literal` — so every compatibility rule
(Optional/union wrapping, coercions, blob dimensionality) is the engine's, not
re-derived here, and a mismatch fails now with the transformer's error rather
than inside the task. Cheap for offloaded values: File/Dir/DataFrame literals
reconstruct from their uri without downloading. The artifact's identity is
stamped on the result so provenance travels with the coerced literal.



| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type \| None` | Declared type to coerce to. When omitted the stored literal is returned as-is (it already carries the service-stamped identity). |

**Raises**

| Exception | Description |
|-|-|
| `TypeTransformerFailedError` | when the stored value cannot bind to `python_type`. |

### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Artifact.create.aio()`.
```python
def create(
    cls,
    value: Any,
    name: str | None = None,
    version: str | None = None,
    description: str | None = None,
    attrs: Mapping[str, str] | None = None,
    kind: Kind | None = None,
    card: CoreCard | None = None,
    python_type: Type | None = None,
    project: str | None = None,
    domain: str | None = None,
    external_ref: str | None = None,
    partitions: Mapping[str, Any] | None = None,
    parents: Sequence[str | artifact_id_pb2.ArtifactVersionId] | None = None,
) -> Artifact
```
Publish an artifact from the local machine.

The value must be an offloaded asset — a flyte.io File, Dir, or DataFrame.
It is converted with the type engine (local data is uploaded to blob
storage first) and stored in the artifact service as a typed literal.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `value` | `Any` | The File, Dir, or DataFrame to publish. May be wrapped with `flyte.artifacts.new(...)`; wrapper metadata seeds name/version/ description/attrs/card, and explicit keyword arguments override it. |
| `name` | `str \| None` | The artifact name; required when value carries no metadata. |
| `version` | `str \| None` | The version to publish. Defaults to the metadata version or a random one. |
| `description` | `str \| None` | Optional human readable description. |
| `attrs` | `Mapping[str, str] \| None` | Optional free-form key/value metadata. |
| `kind` | `Kind \| None` | What the artifact is ("model", "data", "generic"). Recorded under the reserved `flyte.io/kind` attr and read back via `Artifact.kind`. Distinct from a card's type, which describes how the card renders. |
| `card` | `CoreCard \| None` | Optional `flyte.artifacts.Card` to attach. |
| `python_type` | `Type \| None` | Type used for literal conversion; defaults to `type(value)`. |
| `project` | `str \| None` | Project to publish into; defaults to the init configuration. |
| `domain` | `str \| None` | Domain to publish into; defaults to the init configuration. |
| `external_ref` | `str \| None` | Optional opaque reference into an external system (a URI, model id, dataset id, ...) recorded as the artifact's source. When omitted and called from inside a running task, the producing task action is recorded automatically instead. |
| `partitions` | `Mapping[str, Any] \| None` | Partition values keyed by partition name: a `date` is a daily time partition, a `datetime` an hourly one, `flyte.artifacts.TimePartition` names the granularity, anything else is a string partition. |
| `parents` | `Sequence[str \| artifact_id_pb2.ArtifactVersionId] \| None` | Lineage — the artifact versions this one derives from, ordered with the primary parent first. Each entry is a bare version string (a same-name parent, i.e. an earlier version of this artifact) or an `ArtifactVersionId` when the parent lives under a different name or scope; a fetched `Artifact` offers one as `.artifact_version_id`. Stored as given, never resolved; a not-yet-published parent is legal. |

**Returns:** The published Artifact.

### declare()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Artifact.declare.aio()`.
```python
def declare(
    cls,
    name: str,
    partitions: Mapping[str, Any],
    project: str | None = None,
    domain: str | None = None,
) -> PartitionSchema
```
Fix an artifact name's partition keys ahead of any version.

```python
Artifact.declare("raw_events", partitions={"date": date, "region": str})
Artifact.declare("hourly_events", partitions={"hour": datetime, "region": str})
Artifact.declare("monthly_report", partitions={"date": "month"})
```

Succeeds when the name has no schema yet or an equal one; fails with
FAILED_PRECONDITION when a different schema is already fixed. Changing the
keys is a new artifact name.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The artifact name. |
| `partitions` | `Mapping[str, Any]` | Key to kind: `date` or "day" for a daily time key, `datetime` or "hour" for hourly, "week" / "month" for coarser ones, `str` (or `int`) for a string key. At most one time key. |
| `project` | `str \| None` | Project; defaults to the init configuration. |
| `domain` | `str \| None` | Domain; defaults to the init configuration. |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Artifact instance>.delete.aio()`.
```python
def delete()
```
Delete this artifact from the remote system.


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Artifact.get.aio()`.
```python
def get(
    cls,
    name: str,
    version: str | Literal['latest'] = 'latest',
    project: str | None = None,
    domain: str | None = None,
    partitions: Mapping[str, Any] | None = None,
    **partition_kwargs: Any,
) -> Artifact
```
Get an artifact by its name and version, or the latest version of one partition.

```python
Artifact.get("raw_events")                               # latest version overall
Artifact.get("raw_events", version="1.0")                # a pinned version
Artifact.get("raw_events", date=date(2026, 9, 17), region="us")  # latest of that partition
```



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the artifact. |
| `version` | `str \| Literal['latest']` | The version of the artifact; "latest" returns the most recently created version. |
| `project` | `str \| None` | Project to look in; defaults to the init configuration. |
| `domain` | `str \| None` | Domain to look in; defaults to the init configuration. |
| `partitions` | `Mapping[str, Any] \| None` | Partition values selecting one partition, one per key of the artifact's schema, for keys whose names collide with this method's own parameters (`name`, `version`, `project`, `domain`). |
| `**partition_kwargs` | `Any` | |

**Raises**

| Exception | Description |
|-|-|
| `ValueError` | when both a version and partitions are given, a value selects more than one partition, or no version exists for the partition. |

### get_schema()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Artifact.get_schema.aio()`.
```python
def get_schema(
    cls,
    name: str,
    project: str | None = None,
    domain: str | None = None,
) -> PartitionSchema
```
The partition keys fixed for an artifact name. An unpartitioned artifact
has an empty schema; a name with neither a declaration nor a version is
NOT_FOUND.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |

### list_names()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Artifact.list_names.aio()`.
```python
def list_names(
    cls,
    search: str | None = None,
    limit: int = -1,
    project: str | None = None,
    domain: str | None = None,
) -> AsyncIterator[ArtifactGroup]
```
List distinct artifact names, one entry per name carrying the latest
version and the total version count, newest activity first.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `search` | `str \| None` | Substring match on the artifact name. |
| `limit` | `int` | The maximum number of names to return. -1 for no limit. |
| `project` | `str \| None` | Project to list in; defaults to the init configuration. |
| `domain` | `str \| None` | Domain to list in; defaults to the init configuration. |

**Returns:** An async iterator of artifact groups.

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Artifact.listall.aio()`.
```python
def listall(
    cls,
    name: str | None = None,
    created_after: datetime | None = None,
    limit: int = -1,
    project: str | None = None,
    domain: str | None = None,
    source_run: str | None = None,
    source_action: str | None = None,
    source_external_ref: str | None = None,
    kind: Kind | None = None,
    attrs: Mapping[str, str | Sequence[str]] | None = None,
    latest_per_partition: bool = False,
    partitions: Mapping[str, Any] | None = None,
    **partition_kwargs: Any,
) -> AsyncIterator[Artifact]
```
List artifacts, newest first.

```python
Artifact.listall("raw_events", date=(date(2026, 8, 1), date(2026, 8, 31)), latest_per_partition=True)
Artifact.listall("raw_events", region=["us", "eu"])
```

Filtering happens server-side, so it pages through matches rather than
scanning everything client-side. It requires a control plane that supports
`user_metadata` filters; older ones reject the request rather than silently
returning unfiltered results.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str \| None` | Exact artifact name; when set, all versions of that artifact are listed. |
| `created_after` | `datetime \| None` | Filter artifacts created after this datetime. |
| `limit` | `int` | The maximum number of artifacts to return. -1 for no limit. |
| `project` | `str \| None` | Project to list in; defaults to the init configuration. |
| `domain` | `str \| None` | Domain to list in; defaults to the init configuration. |
| `source_run` | `str \| None` | Only artifacts produced by this run. |
| `source_action` | `str \| None` | Only artifacts produced by this action; usually combined with source_run. |
| `source_external_ref` | `str \| None` | Only artifacts imported from this external reference. |
| `kind` | `Kind \| None` | Only artifacts of this kind, e.g. "model". Shorthand for filtering on the reserved kind attr. |
| `attrs` | `Mapping[str, str \| Sequence[str]] \| None` | Only artifacts whose attrs match. A value may be a single string or a sequence, in which case any of them matches. Separate keys must all match. |
| `latest_per_partition` | `bool` | Return only the newest version of each distinct partition, so a range over the time partition yields one version per partition. Requires a name. |
| `partitions` | `Mapping[str, Any] \| None` | Partition selection by key, the same as the keyword form. A `date`/`datetime` selects one time partition; a 2-tuple `(start, end)` selects an inclusive range of the time partition (dates, datetimes or ISO strings); a list on a string key matches any of the values; any other value matches exactly. |
| `**partition_kwargs` | `Any` | |

**Returns**

An async iterator of artifacts.


### partition_values()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Artifact.partition_values.aio()`.
```python
def partition_values(
    cls,
    name: str,
    key: str,
    project: str | None = None,
    domain: str | None = None,
    limit: int = 1000,
    partitions: Mapping[str, Any] | None = None,
    **fixed: Any,
) -> list[Any]
```
The distinct values one partition key has among an artifact's versions,
sorted ascending, optionally scoped by the other keys.

```python
Artifact.partition_values("raw_events", "region", date=date(2026, 9, 17))  # ["eu", "us"]
Artifact.partition_values("raw_events", "date")                             # [date(...), ...]
```



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The artifact name. |
| `key` | `str` | The partition key to list: a string key, or the time key, whose values come back as `date` (daily or coarser) or `datetime` (hourly). |
| `project` | `str \| None` | Project to look in; defaults to the init configuration. |
| `domain` | `str \| None` | Domain to look in; defaults to the init configuration. |
| `limit` | `int` | Maximum number of values. |
| `partitions` | `Mapping[str, Any] \| None` | Partition selection scoping the versions, for keys whose names collide with this method's own parameters (`name`, `key`, `project`, `domain`, `limit`). |
| `**fixed` | `Any` | |

### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.



**Returns:** dict: A dictionary representation of the object.

### to_json()

```python
def to_json()
```
Convert the object to a JSON string.



**Returns:** str: A JSON string representation of the object.

### to_python()

```python
def to_python(
    python_type: Type | None = None,
) -> Any
```
Materialize the artifact's stored literal back into a python value.



| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type \| None` | Expected python type; guessed from the stored Flyte type when omitted. |

