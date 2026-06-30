---
title: VolumeExplore
version: 0.4.3
variants: +flyte +union
layout: py_api
---

# VolumeExplore

**Package:** `flyteplugins.union.remote`

A resolved :class:`Volume` plus the IO to inspect and walk its lineage.

Construct via :meth:`from_action` (resolve off a run/action), :meth:`from_volume_value`
(wrap an in-hand Volume), or :meth:`from_volume_json` (a serialized value on disk).


## Parameters

```python
class VolumeExplore(
    volume: Volume,
    op_label: Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `volume` | `Volume` | |
| `op_label` | `Optional[str]` | |

## Methods

| Method | Description |
|-|-|
| [`download_index()`](#download_index) | Download this Volume's metadata index to ``dest`` (local path). |
| [`from_action()`](#from_action) | Resolve the Volume to explore off ``run/action``. |
| [`from_volume_json()`](#from_volume_json) | Load a serialized Volume value (``. |
| [`from_volume_value()`](#from_volume_value) |  |
| [`lineage()`](#lineage) | Full version chain, newest first, walked via ``parent_produced_by. |
| [`lineage_has_navigable_parent()`](#lineage_has_navigable_parent) | True iff the immediate parent in ``lineage`` can actually be opened —. |
| [`parent()`](#parent) | The immediate parent version as a new :class:`VolumeExplore`, or ``None``. |
| [`provenance()`](#provenance) | Producer + parent-producer action refs (flattened for display). |


### download_index()

```python
def download_index(
    dest: str,
)
```
Download this Volume's metadata index to ``dest`` (local path).


| Parameter | Type | Description |
|-|-|-|
| `dest` | `str` | |

### from_action()

```python
def from_action(
    run_name: str,
    action_name: str,
    op_name: Optional[str],
) -> 'VolumeExplore'
```
Resolve the Volume to explore off ``run/action``.

With ``op_name`` set it's matched against the action's **outputs first,
then inputs**; omitted, the action's Volume-typed values are discovered,
preferring outputs. A unique match wins; multiple raise
:class:`VolumeResolveError`.


| Parameter | Type | Description |
|-|-|-|
| `run_name` | `str` | |
| `action_name` | `str` | |
| `op_name` | `Optional[str]` | |

### from_volume_json()

```python
def from_volume_json(
    path: 'str | Path',
) -> 'VolumeExplore'
```
Load a serialized Volume value (``.json``) from disk.


| Parameter | Type | Description |
|-|-|-|
| `path` | `'str \| Path'` | |

### from_volume_value()

```python
def from_volume_value(
    volume: Volume,
) -> 'VolumeExplore'
```
| Parameter | Type | Description |
|-|-|-|
| `volume` | `Volume` | |

### lineage()

```python
def lineage(
    current_reader: Optional[Any],
) -> List[dict]
```
Full version chain, newest first, walked via ``parent_produced_by.locator``.

``current_reader`` (any object with an async ``summary()``) supplies the
*current* version's live stats; without it, the Volume's stored
``used_bytes`` / ``inode_count`` are used.


| Parameter | Type | Description |
|-|-|-|
| `current_reader` | `Optional[Any]` | |

### lineage_has_navigable_parent()

```python
def lineage_has_navigable_parent(
    lineage: List[dict],
) -> bool
```
True iff the immediate parent in ``lineage`` can actually be opened —
it loaded (no ``error``), has its own index, and is a *distinct* version.


| Parameter | Type | Description |
|-|-|-|
| `lineage` | `List[dict]` | |

### parent()

```python
def parent()
```
The immediate parent version as a new :class:`VolumeExplore`, or ``None``.


### provenance()

```python
def provenance()
```
Producer + parent-producer action refs (flattened for display).


