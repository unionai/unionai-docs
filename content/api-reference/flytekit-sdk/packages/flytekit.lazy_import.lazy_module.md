---
title: flytekit.lazy_import.lazy_module
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.lazy_import.lazy_module

## Directory

### Methods

| Method | Description |
|-|-|
| [`is_imported()`](#is_imported) | This function is used to check if a module has been imported by the regular import. |
| [`lazy_module()`](#lazy_module) | This function is used to lazily import modules. |


## Methods

#### is_imported()

```python
def is_imported(
    module_name,
)
```
This function is used to check if a module has been imported by the regular import.
Return false if module is lazy imported and not used yet.


| Parameter | Type |
|-|-|
| `module_name` |  |

#### lazy_module()

```python
def lazy_module(
    fullname,
)
```
This function is used to lazily import modules.  It is used in the following way:
```python
from flytekit.lazy_import import lazy_module
sklearn = lazy_module("sklearn")
sklearn.svm.SVC()
```


| Parameter | Type |
|-|-|
| `fullname` |  |

