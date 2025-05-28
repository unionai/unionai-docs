---
title: flytekit.core.tracked_abc
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.tracked_abc

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteTrackedABC`](.././flytekit.core.tracked_abc#flytekitcoretracked_abcflytetrackedabc) | This class exists because if you try to inherit from abc. |

## flytekit.core.tracked_abc.FlyteTrackedABC

This class exists because if you try to inherit from abc.ABC and TrackedInstance by itself, you'll get the
well-known ``TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass
of the metaclasses of all its bases`` error.


### Methods

| Method | Description |
|-|-|
| [`register()`](#register) | Register a virtual subclass of an ABC. |


#### register()

```python
def register(
    cls,
    subclass,
)
```
Register a virtual subclass of an ABC.

Returns the subclass, to allow usage as a class decorator.


| Parameter | Type |
|-|-|
| `cls` |  |
| `subclass` |  |

