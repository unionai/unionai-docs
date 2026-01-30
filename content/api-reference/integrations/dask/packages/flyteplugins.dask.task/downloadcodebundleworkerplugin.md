---
title: DownloadCodeBundleWorkerPlugin
version: 2.0.0b53
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DownloadCodeBundleWorkerPlugin

**Package:** `flyteplugins.dask.task`

A Dask plugin to download and set up the code bundle on each worker.


```python
class DownloadCodeBundleWorkerPlugin(
    code_bundle: flyte.models.CodeBundle,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code_bundle` | `flyte.models.CodeBundle` | |

## Methods

| Method | Description |
|-|-|
| [`setup()`](#setup) | Runs on each worker as it is initialized. |
| [`teardown()`](#teardown) | Run when the worker to which the plugin is attached is closed, or. |
| [`transition()`](#transition) | Throughout the lifecycle of a task (see :doc:`Worker State. |


### setup()

```python
def setup(
    worker,
)
```
Runs on each worker as it is initialized.


| Parameter | Type | Description |
|-|-|-|
| `worker` |  | |

### teardown()

```python
def teardown(
    worker: Worker,
) -> None | Awaitable[None]
```
Run when the worker to which the plugin is attached is closed, or
when the plugin is removed.


| Parameter | Type | Description |
|-|-|-|
| `worker` | `Worker` | |

### transition()

```python
def transition(
    key: Key,
    start: WorkerTaskStateState,
    finish: WorkerTaskStateState,
    kwargs: **kwargs,
)
```
Throughout the lifecycle of a task (see :doc:`Worker State
&lt;worker-state&gt;`), Workers are instructed by the scheduler to compute
certain tasks, resulting in transitions in the state of each task. The
Worker owning the task is then notified of this state transition.

Whenever a task changes its state, this method will be called.

.. warning::

    This is an advanced feature and the transition mechanism and details
    of task states are subject to change without deprecation cycle.

Parameters
----------
key :
start :
    Start state of the transition.
    One of waiting, ready, executing, long-running, memory, error.
finish :
    Final state of the transition.
kwargs :
    More options passed when transitioning


| Parameter | Type | Description |
|-|-|-|
| `key` | `Key` | |
| `start` | `WorkerTaskStateState` | |
| `finish` | `WorkerTaskStateState` | |
| `kwargs` | `**kwargs` | |

