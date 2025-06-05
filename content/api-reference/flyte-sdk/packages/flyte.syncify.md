---
title: flyte.syncify
version: 0.2.0b7
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.syncify

## Directory

### Classes

| Class | Description |
|-|-|
| [`Syncify`](.././flyte.syncify#flytesyncifysyncify) | A decorator to convert asynchronous functions or methods into synchronous ones. |

## flyte.syncify.Syncify

A decorator to convert asynchronous functions or methods into synchronous ones.

This is useful for integrating async code into synchronous contexts.

Example::

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


```python
def Syncify()
```
