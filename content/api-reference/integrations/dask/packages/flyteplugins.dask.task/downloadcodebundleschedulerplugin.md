---
title: DownloadCodeBundleSchedulerPlugin
version: 2.0.0b53
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DownloadCodeBundleSchedulerPlugin

**Package:** `flyteplugins.dask.task`

A Dask plugin to download and set up the code bundle on the scheduler.


```python
class DownloadCodeBundleSchedulerPlugin(
    code_bundle: flyte.models.CodeBundle,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code_bundle` | `flyte.models.CodeBundle` | |

## Methods

| Method | Description |
|-|-|
| [`add_client()`](#add_client) | Run when a new client connects. |
| [`add_worker()`](#add_worker) | Run when a new worker enters the cluster. |
| [`before_close()`](#before_close) | Runs prior to any Scheduler shutdown logic. |
| [`close()`](#close) | Run when the scheduler closes down. |
| [`log_event()`](#log_event) | Run when an event is logged. |
| [`remove_client()`](#remove_client) | Run when a client disconnects. |
| [`remove_worker()`](#remove_worker) | Run when a worker leaves the cluster. |
| [`restart()`](#restart) | Run when the scheduler restarts itself. |
| [`start()`](#start) | Run when the scheduler starts up. |
| [`transition()`](#transition) | Run whenever a task changes state. |
| [`update_graph()`](#update_graph) | Run when a new graph / tasks enter the scheduler. |
| [`valid_workers_downscaling()`](#valid_workers_downscaling) | Determine which workers can be removed from the cluster. |


### add_client()

```python
def add_client(
    scheduler: Scheduler,
    client: str,
)
```
Run when a new client connects


| Parameter | Type | Description |
|-|-|-|
| `scheduler` | `Scheduler` | |
| `client` | `str` | |

### add_worker()

```python
def add_worker(
    scheduler: Scheduler,
    worker: str,
) -> None | Awaitable[None]
```
Run when a new worker enters the cluster

If this method is synchronous, it is immediately and synchronously executed
without ``Scheduler.add_worker`` ever yielding to the event loop.
If it is asynchronous, it will be awaited after all synchronous
``SchedulerPlugin.add_worker`` hooks have executed.

.. warning::

    There are no guarantees about the execution order between individual
    ``SchedulerPlugin.add_worker`` hooks and the ordering may be subject
    to change without deprecation cycle.


| Parameter | Type | Description |
|-|-|-|
| `scheduler` | `Scheduler` | |
| `worker` | `str` | |

### before_close()

```python
def before_close()
```
Runs prior to any Scheduler shutdown logic


### close()

```python
def close()
```
Run when the scheduler closes down

This runs at the beginning of the Scheduler shutdown process, but after
workers have been asked to shut down gracefully


### log_event()

```python
def log_event(
    topic: str,
    msg: Any,
)
```
Run when an event is logged


| Parameter | Type | Description |
|-|-|-|
| `topic` | `str` | |
| `msg` | `Any` | |

### remove_client()

```python
def remove_client(
    scheduler: Scheduler,
    client: str,
)
```
Run when a client disconnects


| Parameter | Type | Description |
|-|-|-|
| `scheduler` | `Scheduler` | |
| `client` | `str` | |

### remove_worker()

```python
def remove_worker(
    scheduler: Scheduler,
    worker: str,
    stimulus_id: str,
    kwargs: **kwargs,
) -> None | Awaitable[None]
```
Run when a worker leaves the cluster

If this method is synchronous, it is immediately and synchronously executed
without ``Scheduler.remove_worker`` ever yielding to the event loop.
If it is asynchronous, it will be awaited after all synchronous
``SchedulerPlugin.remove_worker`` hooks have executed.

.. warning::

    There are no guarantees about the execution order between individual
    ``SchedulerPlugin.remove_worker`` hooks and the ordering may be subject
    to change without deprecation cycle.


| Parameter | Type | Description |
|-|-|-|
| `scheduler` | `Scheduler` | |
| `worker` | `str` | |
| `stimulus_id` | `str` | |
| `kwargs` | `**kwargs` | |

### restart()

```python
def restart(
    scheduler: Scheduler,
)
```
Run when the scheduler restarts itself


| Parameter | Type | Description |
|-|-|-|
| `scheduler` | `Scheduler` | |

### start()

```python
def start(
    scheduler,
)
```
Run when the scheduler starts up

This runs at the end of the Scheduler startup process


| Parameter | Type | Description |
|-|-|-|
| `scheduler` |  | |

### transition()

```python
def transition(
    key: Key,
    start: SchedulerTaskStateState,
    finish: SchedulerTaskStateState,
    args: *args,
    stimulus_id: str,
    kwargs: **kwargs,
)
```
Run whenever a task changes state

For a description of the transition mechanism and the available states,
see :ref:`Scheduler task states &lt;scheduler-task-state&gt;`.

.. warning::

    This is an advanced feature and the transition mechanism and details
    of task states are subject to change without deprecation cycle.

Parameters
----------
key :
start :
    Start state of the transition.
    One of released, waiting, processing, memory, error.
finish :
    Final state of the transition.
stimulus_id :
    ID of stimulus causing the transition.
*args, **kwargs :
    More options passed when transitioning
    This may include worker ID, compute time, etc.


| Parameter | Type | Description |
|-|-|-|
| `key` | `Key` | |
| `start` | `SchedulerTaskStateState` | |
| `finish` | `SchedulerTaskStateState` | |
| `args` | `*args` | |
| `stimulus_id` | `str` | |
| `kwargs` | `**kwargs` | |

### update_graph()

```python
def update_graph(
    scheduler: Scheduler,
    client: str,
    keys: set[Key],
    tasks: list[Key],
    annotations: dict[str, dict[Key, Any]],
    priority: dict[Key, tuple[int | float, ...]],
    stimulus_id: str,
    kwargs: **kwargs,
)
```
Run when a new graph / tasks enter the scheduler

Parameters
----------
    scheduler:
        The `Scheduler` instance.
    client:
        The unique Client id.
    keys:
        The keys the Client is interested in when calling `update_graph`.
    tasks:
        The
    annotations:
        Fully resolved annotations as applied to the tasks in the format::

            {
                "annotation": {
                    "key": "value,
                    ...
                },
                ...
            }
    priority:
        Task calculated priorities as assigned to the tasks.
    stimulus_id:
        ID of the stimulus causing the graph update
    **kwargs:
        It is recommended to allow plugins to accept more parameters to
        ensure future compatibility.


| Parameter | Type | Description |
|-|-|-|
| `scheduler` | `Scheduler` | |
| `client` | `str` | |
| `keys` | `set[Key]` | |
| `tasks` | `list[Key]` | |
| `annotations` | `dict[str, dict[Key, Any]]` | |
| `priority` | `dict[Key, tuple[int \| float, ...]]` | |
| `stimulus_id` | `str` | |
| `kwargs` | `**kwargs` | |

### valid_workers_downscaling()

```python
def valid_workers_downscaling(
    scheduler: Scheduler,
    workers: list[scheduler_module.WorkerState],
) -> list[scheduler_module.WorkerState]
```
Determine which workers can be removed from the cluster

This method is called when the scheduler is about to downscale the cluster
by removing workers. The method should return a set of worker states that
can be removed from the cluster.

Parameters
----------
workers : list
    The list of worker states that are candidates for removal.
stimulus_id : str
    ID of stimulus causing the downscaling.

Returns
-------
list
    The list of worker states that can be removed from the cluster.


| Parameter | Type | Description |
|-|-|-|
| `scheduler` | `Scheduler` | |
| `workers` | `list[scheduler_module.WorkerState]` | |

