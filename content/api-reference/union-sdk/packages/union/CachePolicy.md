---
title: CachePolicy
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# CachePolicy

**Package:** `union`

Base class for protocol classes.

Protocol classes are defined as::

    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

    class C:
        def meth(self) -> int:
            return 0

    def func(x: Proto) -> int:
        return x.meth()

    func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

    class GenProto(Protocol[T]):
        def meth(self) -> T:
            ...


```python
protocol CachePolicy()
```
## Methods

| Method | Description |
|-|-|
| [`get_version()`](#get_version) |  |


### get_version()

```python
def get_version(
    salt: str,
    params: flytekit.core.cache.VersionParameters,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `salt` | `str` | |
| `params` | `flytekit.core.cache.VersionParameters` | |

