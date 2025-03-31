---
title: flytekit.utils.asyn
version: 0.1.dev2184+g1e0cbe7
variants: +flyte +byoc +byok +serverless
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

