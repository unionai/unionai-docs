---
title: Syncify
description: "A decorator to convert asynchronous functions or methods into synchronous ones."
icon: braces
version: 2.12.2
variants: +flyte +union
layout: py_api
---

# Syncify

**Package:** `flyte.syncify`

A decorator to convert asynchronous functions or methods into synchronous ones.

This is useful for integrating async code into synchronous contexts.

```python
syncer = Syncify()

@syncer
async def async_function(x: str) -> str:
    return f"Hello, Async World {x}!"


# now you can call it synchronously
result = async_function("Async World")
print(result)
# Output: Hello, Async World Async World!

# or call it asynchronously
async def main():
    result = await async_function.aio("World")
    print(result)
```


## Parameters

```python
class Syncify(
    name: str = 'flyte_syncify',
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`awaitable_compat()`](#awaitable_compat) | Like the `Syncify` decorator, for an async method that callers used to `await` directly. |


### awaitable_compat()

```python
def awaitable_compat(
    func: Callable[P, Awaitable[R_co]],
) -> SyncFunction[P, R_co]
```
Like the `Syncify` decorator, for an async method that callers used to `await` directly.

Called with no running event loop in the current thread, it runs synchronously and returns the result, the
same as a syncified method. Called inside a running event loop, it returns the coroutine so that legacy
`await obj.method()` code keeps working, and emits a `DeprecationWarning` once per call site recommending
`await obj.method.aio()`, which is the preferred async form and behaves as it does with `Syncify`.

Only plain async functions and instance methods are supported.


| Parameter | Type | Description |
|-|-|-|
| `func` | `Callable[P, Awaitable[R_co]]` | |

