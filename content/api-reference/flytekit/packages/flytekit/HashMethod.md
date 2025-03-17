---
title: HashMethod
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# HashMethod

**Package:** `flytekit`

Flyte-specific object used to wrap the hash function for a specific type


```python
def HashMethod(
    function: typing.Callable[[~T], str],
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `function` | `typing.Callable[[~T], str]` |
## Methods

### calculate()

```python
def calculate(
    obj: ~T,
):
```
Calculate hash for `obj`.


| Parameter | Type |
|-|-|
| `obj` | `~T` |
