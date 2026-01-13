---
title: CachePolicy
version: 2.0.0b47
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# CachePolicy

**Package:** `flyte`

Base class for protocol classes.

Protocol classes are defined as::

    class Proto(Protocol):
        def meth(self) -&gt; int:
            ...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

    class C:
        def meth(self) -&gt; int:
            return 0

    def func(x: Proto) -&gt; int:
        return x.meth()

    func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

    class GenProto[T](Protocol):
        def meth(self) -&gt; T:
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
    params: flyte._cache.cache.VersionParameters,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `salt` | `str` | |
| `params` | `flyte._cache.cache.VersionParameters` | |

