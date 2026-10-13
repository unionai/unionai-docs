---
title: Trackio
description: "Flyte Trackio plugin."
icon: book
version: 2.11.1
variants: +flyte +union
layout: py_api
---

# Trackio



Flyte Trackio plugin.

Provides seamless Trackio experiment tracking for Flyte tasks through the
`@trackio_init` decorator.

Basic usage:

    from flyteplugins.trackio import (
        get_trackio_run,
        trackio_init,
    )

    @trackio_init(project="my-project")
    @env.task
    async def train():
        run = get_trackio_run()
        run.log({"loss": 0.123})
        return run.id

Configuration can also be provided via `trackio_config()`:

    r = flyte.with_runcontext(
        custom_context=trackio_config(
            project="my-project",
            group="baseline",
            config={"learning_rate": 1e-3},
        )
    ).run(train)
## Directory

### Classes

| Class | Description |
|-|-|
| [`Trackio`](./trackio) | Generates a Trackio dashboard link for Flyte. |

### Methods

| Method | Description |
|-|-|
| [`get_trackio_context()`](#get_trackio_context) | Return the current Trackio configuration. |
| [`get_trackio_run()`](#get_trackio_run) | Return the active Trackio run. |
| [`trackio_config()`](#trackio_config) | Create Trackio configuration for Flyte. |
| [`trackio_init()`](#trackio_init) | Initialize a Trackio run around a Flyte task. |


## Methods

#### get_trackio_context()

```python
def get_trackio_context()
```
Return the current Trackio configuration.


#### get_trackio_run()

```python
def get_trackio_run()
```
Return the active Trackio run.

If called inside a `@trackio_init` decorated Flyte task, this returns the
Trackio run managed by the plugin. Otherwise it falls back to Trackio's
globally active run (if one exists).



**Returns:** trackio.Run | None: The active Trackio run.

#### trackio_config()

```python
def trackio_config(
    project: str | None = None,
    name: str | None = None,
    group: str | None = None,
    space_id: str | None = None,
    dataset_id: str | None = None,
    bucket_id: str | None = None,
    server_url: str | None = None,
    config: dict[str, Any] | None = None,
    resume: str = 'never',
    auto_log_gpu: bool | None = None,
    gpu_log_interval: float = 10.0,
    auto_log_cpu: bool | None = None,
    cpu_log_interval: float = 10.0,
) -> _TrackioConfig
```
Create Trackio configuration for Flyte.


| Parameter | Type | Description |
|-|-|-|
| `project` | `str \| None` | |
| `name` | `str \| None` | |
| `group` | `str \| None` | |
| `space_id` | `str \| None` | |
| `dataset_id` | `str \| None` | |
| `bucket_id` | `str \| None` | |
| `server_url` | `str \| None` | |
| `config` | `dict[str, Any] \| None` | |
| `resume` | `str` | |
| `auto_log_gpu` | `bool \| None` | |
| `gpu_log_interval` | `float` | |
| `auto_log_cpu` | `bool \| None` | |
| `cpu_log_interval` | `float` | |

#### trackio_init()

```python
def trackio_init(
    **decorator_kwargs: Any,
) -> F
```
Initialize a Trackio run around a Flyte task.

Usage
-----

@trackio_init
@env.task
async def train():
    ...

@trackio_init(
    project="vision",
    space_id="user/demo",
)
@env.task
async def train():
    ...


| Parameter | Type | Description |
|-|-|-|
| `**decorator_kwargs` | `Any` | |

