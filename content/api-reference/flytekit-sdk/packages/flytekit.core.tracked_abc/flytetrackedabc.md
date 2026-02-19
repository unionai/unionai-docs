---
title: FlyteTrackedABC
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteTrackedABC

**Package:** `flytekit.core.tracked_abc`

This class exists because if you try to inherit from abc.ABC and TrackedInstance by itself, you'll get the
well-known ``TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass
of the metaclasses of all its bases`` error.



## Methods

| Method | Description |
|-|-|
| [`register()`](#register) | Register a virtual subclass of an ABC. |


### register()

```python
def register(
    cls,
    subclass,
)
```
Register a virtual subclass of an ABC.

Returns the subclass, to allow usage as a class decorator.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `subclass` |  | |

