---
title: FlytePickle
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# FlytePickle

**Package:** `flytekit.types.pickle`

This type is only used by flytekit internally. User should not use this type.
Any type that flyte can't recognize will become FlytePickle


## Methods

### from_pickle()

```python
def from_pickle(
    uri: str,
):
```
| Parameter | Type |
|-|-|
| `uri` | `str` |
### python_type()

```python
def python_type()
```
No parameters
### to_pickle()

```python
def to_pickle(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `python_val` | `typing.Any` |
