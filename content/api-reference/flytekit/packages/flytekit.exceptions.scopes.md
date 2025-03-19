---
title: flytekit.exceptions.scopes
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.exceptions.scopes

## Directory

### Classes

No classes in this package.

### Errors

* [`FlyteScopedException`](.././flytekit.exceptions.scopes#flytekitexceptionsscopesflytescopedexception)
* [`FlyteScopedSystemException`](.././flytekit.exceptions.scopes#flytekitexceptionsscopesflytescopedsystemexception)
* [`FlyteScopedUserException`](.././flytekit.exceptions.scopes#flytekitexceptionsscopesflytescopeduserexception)

## flytekit.exceptions.scopes.FlyteScopedException

Common base class for all non-exit exceptions.


```python
def FlyteScopedException(
    context,
    exc_type,
    exc_value,
    exc_tb,
    top_trim,
    bottom_trim,
    kind,
):
```
| Parameter | Type |
|-|-|
| `context` |  |
| `exc_type` |  |
| `exc_value` |  |
| `exc_tb` |  |
| `top_trim` |  |
| `bottom_trim` |  |
| `kind` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| error_code |  |  |
| kind |  |  |
| traceback |  |  |
| type |  |  |
| value |  |  |
| verbose_message |  |  |

## flytekit.exceptions.scopes.FlyteScopedSystemException

Common base class for all non-exit exceptions.


```python
def FlyteScopedSystemException(
    exc_type,
    exc_value,
    exc_tb,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `exc_type` |  |
| `exc_value` |  |
| `exc_tb` |  |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| error_code |  |  |
| kind |  |  |
| traceback |  |  |
| type |  |  |
| value |  |  |
| verbose_message |  |  |

## flytekit.exceptions.scopes.FlyteScopedUserException

Common base class for all non-exit exceptions.


```python
def FlyteScopedUserException(
    exc_type,
    exc_value,
    exc_tb,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `exc_type` |  |
| `exc_value` |  |
| `exc_tb` |  |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| error_code |  |  |
| kind |  |  |
| traceback |  |  |
| type |  |  |
| value |  |  |
| verbose_message |  |  |

