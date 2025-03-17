---
title: BatchSize
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# BatchSize

**Package:** `flytekit`

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
def BatchSize(
    val: int,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `val` | `int` |
## Methods

