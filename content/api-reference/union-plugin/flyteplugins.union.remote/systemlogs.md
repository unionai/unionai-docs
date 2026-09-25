---
title: SystemLogs
description: "Logs of the Union system components running on a cluster's dataplane."
icon: braces
version: 0.13.0
variants: -flyte +union
layout: py_api
---

# SystemLogs

**Package:** `flyteplugins.union.remote`

Logs of the Union system components running on a cluster's dataplane.

Selected by Kubernetes label rather than by any Flyte object.


## Parameters

```python
def SystemLogs()
```
## Methods

| Method | Description |
|-|-|
| [`create_viewer()`](#create_viewer) | Stream a cluster's system logs to the console. |
| [`tail()`](#tail) | Stream the system logs of a cluster's dataplane components. |


### create_viewer()

```python
def create_viewer(
    cluster_name: str,
    namespace: str,
    application: Application | None = 1,
    pod_label_selector: str | None = None,
    start_time: datetime | None = None,
    node_name: str | None = None,
    source: logs_pb2.LogsSource = 0,
    max_lines: int = 30,
    show_ts: bool = False,
    raw: bool = True,
)
```
Stream a cluster's system logs to the console.

The remaining arguments select the stream and are passed to `tail`.


| Parameter | Type | Description |
|-|-|-|
| `cluster_name` | `str` | |
| `namespace` | `str` | |
| `application` | `Application \| None` | |
| `pod_label_selector` | `str \| None` | |
| `start_time` | `datetime \| None` | |
| `node_name` | `str \| None` | |
| `source` | `logs_pb2.LogsSource` | |
| `max_lines` | `int` | Lines kept in view, when not raw. |
| `show_ts` | `bool` | Whether to prefix each line with its timestamp. |
| `raw` | `bool` | Print lines as they arrive, scrolling the terminal. When False, they are shown in an auto-scrolling box of ``max_lines`` lines. |

### tail()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await SystemLogs.tail.aio()`.
```python
def tail(
    cls,
    cluster_name: str,
    namespace: str,
    application: Application | None = 1,
    pod_label_selector: str | None = None,
    start_time: datetime | None = None,
    node_name: str | None = None,
    source: logs_pb2.LogsSource = 0,
) -> AsyncGenerator[logs_pb2.LogLine, None]
```
Stream the system logs of a cluster's dataplane components.

Ends when the dataplane closes the stream; there is no reconnect. Lines
are prefixed with their pod once more than one pod is in the stream.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `cluster_name` | `str` | Name of the cluster whose dataplane to read from. |
| `namespace` | `str` | Kubernetes namespace the components run in. |
| `application` | `Application \| None` | Which component to tail. Mutually exclusive with ``pod_label_selector``; pass ``None`` when using one. |
| `pod_label_selector` | `str \| None` | Kubernetes label selector to pick pods with, for components the ``Application`` enum does not name. |
| `start_time` | `datetime \| None` | Earliest time to read logs from. Defaults to the start of the retained logs. |
| `node_name` | `str \| None` | Only stream logs of pods running on this Kubernetes node. |
| `source` | `logs_pb2.LogsSource` | Whether to read live logs, persisted logs, or (the default) live logs falling back to persisted when no live pods match. |

