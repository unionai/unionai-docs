---
title: flytekit.exceptions.eager
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.exceptions.eager

## Directory

### Errors

| Exception | Description |
|-|-|
| [`EagerException`](.././flytekit.exceptions.eager#flytekitexceptionseagereagerexception) | Raised when a node in an eager workflow encounters an error. |

## flytekit.exceptions.eager.EagerException

Raised when a node in an eager workflow encounters an error.

This exception should be used in an {{< py_func_ref `@eager <flytekit.core.task.eager>` >}} workflow function to
catch exceptions that are raised by tasks or subworkflows.

```python
from flytekit import task
from flytekit.exceptions.eager import EagerException

@task
def add_one(x: int) -> int:
    if x < 0:
        raise ValueError("x must be positive")
    return x + 1

@task
def double(x: int) -> int:
    return x * 2

@eager
async def eager_workflow(x: int) -> int:
    try:
        out = await add_one(x=x)
    except EagerException:
        # The ValueError error is caught
        # and raised as an EagerException
        raise
    return await double(x=out)
```


