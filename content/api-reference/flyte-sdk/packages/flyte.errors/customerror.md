---
title: CustomError
version: 2.1.3.dev1+ge23e739d5
variants: +flyte +union
layout: py_api
---

# CustomError

**Package:** `flyte.errors`

This error is raised when the user raises a custom error.


## Parameters

```python
class CustomError(
    code: str,
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `message` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`from_exception()`](#from_exception) | Create a CustomError from an exception. |


### from_exception()

```python
def from_exception(
    e: Exception,
)
```
Create a CustomError from an exception. The exception's class name is used as the error code and the exception
message is used as the error message.


| Parameter | Type | Description |
|-|-|-|
| `e` | `Exception` | |

