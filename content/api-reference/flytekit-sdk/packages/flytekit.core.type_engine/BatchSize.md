---
title: BatchSize
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# BatchSize

**Package:** `flytekit.core.type_engine`

This is used to annotate a FlyteDirectory when we want to download/upload the contents of the directory in batches. For example,

```python
@task
def t1(directory: Annotated[FlyteDirectory, BatchSize(10)]) -> Annotated[FlyteDirectory, BatchSize(100)]:
    ...
    return FlyteDirectory(...)
```

In the above example flytekit will download all files from the input `directory` in chunks of 10, i.e. first it
downloads 10 files, loads them to memory, then writes those 10 to local disk, then it loads the next 10, so on
and so forth. Similarly, for outputs, in this case flytekit is going to upload the resulting directory in chunks of
100.


```python
class BatchSize(
    val: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `val` | `int` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `val` |  |  |

