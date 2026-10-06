---
title: DbtTaskResolver
description: "Reconstructs a DbtTask in the remote task container."
icon: braces
version: 2.11.0
variants: +flyte +union
layout: py_api
---

# DbtTaskResolver

**Package:** `flyteplugins.dbt`

Reconstructs a DbtTask in the remote task container.


## Properties

| Property | Type | Description |
|-|-|-|
| `import_path` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`load_task()`](#load_task) |  |
| [`loader_args()`](#loader_args) |  |


### load_task()

```python
def load_task(
    loader_args: list[str],
) -> TaskTemplate
```
| Parameter | Type | Description |
|-|-|-|
| `loader_args` | `list[str]` | |

### loader_args()

```python
def loader_args(
    task: TaskTemplate,
    root_dir: pathlib.Path | None = None,
) -> list[str]
```
| Parameter | Type | Description |
|-|-|-|
| `task` | `TaskTemplate` | |
| `root_dir` | `pathlib.Path \| None` | |

