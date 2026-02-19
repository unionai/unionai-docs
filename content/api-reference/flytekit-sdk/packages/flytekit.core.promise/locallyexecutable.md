---
title: LocallyExecutable
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LocallyExecutable

**Package:** `flytekit.core.promise`

```python
protocol LocallyExecutable()
```
## Methods

| Method | Description |
|-|-|
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
) -> Union[Tuple[Promise], Promise, VoidPromise, None]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `kwargs` | `**kwargs` | |

### local_execution_mode()

```python
def local_execution_mode()
```
