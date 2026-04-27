---
title: flytekit.utils.asyn
version: 1.16.19
variants: +flyte +union
layout: py_api
---

# flytekit.utils.asyn

Manages an async event loop on another thread. Developers should only require to call
sync to use the managed loop:

from flytekit.tools.asyn import run_sync

async def async_add(a: int, b: int) -> int:
    return a + b

result = run_sync(async_add, a=10, b=12)
## Directory

### Variables

| Property | Type | Description |
|-|-|-|
| `P` | `ParamSpec` |  |
| `T` | `TypeVar` |  |
| `loop_manager` | `_AsyncLoopManager` |  |

