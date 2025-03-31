---
title: flytekit.exceptions.scopes
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.exceptions.scopes

## Directory

### Errors

| Exception | Description |
|-|-|
| [`FlyteScopedException`](.././flytekit.exceptions.scopes#flytekitexceptionsscopesflytescopedexception) | Common base class for all non-exit exceptions. |
| [`FlyteScopedSystemException`](.././flytekit.exceptions.scopes#flytekitexceptionsscopesflytescopedsystemexception) | Common base class for all non-exit exceptions. |
| [`FlyteScopedUserException`](.././flytekit.exceptions.scopes#flytekitexceptionsscopesflytescopeduserexception) | Common base class for all non-exit exceptions. |

### Methods

| Method | Description |
|-|-|
| [`_decorator()`](#_decorator) | Decorate a function with signature func(wrapped, args, kwargs). |
| [`_format_tb()`](#_format_tb) | A shorthand for 'format_list(extract_tb(tb, limit))'. |
| [`_is_base_context()`](#_is_base_context) |  |
| [`_wraps()`](#_wraps) | Decorator factory to apply update_wrapper() to a wrapper function. |
| [`is_rich_logging_enabled()`](#is_rich_logging_enabled) |  |
| [`system_entry_point()`](#system_entry_point) | The reason these two (see the user one below) decorators exist is to categorize non-Flyte exceptions at arbitrary. |
| [`user_entry_point()`](#user_entry_point) | See the comment for the system_entry_point above as well. |


## Methods

#### _decorator()

```python
def _decorator(
    outer_f,
)
```
Decorate a function with signature func(wrapped, args, kwargs).


| Parameter | Type |
|-|-|
| `outer_f` |  |

#### _format_tb()

```python
def _format_tb(
    tb,
    limit,
)
```
A shorthand for 'format_list(extract_tb(tb, limit))'.


| Parameter | Type |
|-|-|
| `tb` |  |
| `limit` |  |

#### _is_base_context()

```python
def _is_base_context()
```
#### _wraps()

```python
def _wraps(
    wrapped,
    assigned,
    updated,
)
```
Decorator factory to apply update_wrapper() to a wrapper function

Returns a decorator that invokes update_wrapper() with the decorated
function as the wrapper argument and the arguments to wraps() as the
remaining arguments. Default arguments are as for update_wrapper().
This is a convenience function to simplify applying partial() to
update_wrapper().


| Parameter | Type |
|-|-|
| `wrapped` |  |
| `assigned` |  |
| `updated` |  |

#### is_rich_logging_enabled()

```python
def is_rich_logging_enabled()
```
#### system_entry_point()

```python
def system_entry_point(
    wrapped,
    args,
    kwargs,
)
```
The reason these two (see the user one below) decorators exist is to categorize non-Flyte exceptions at arbitrary
locations. For example, while there is a separate ecosystem of Flyte-defined user and system exceptions
(see the FlyteException hierarchy), and we can easily understand and categorize those, if flytekit comes upon
a random ``ValueError`` or other non-flytekit defined error, how would we know if it was a bug in flytekit versus an
error with user code or something the user called? The purpose of these decorators is to categorize those (see
the last case in the nested try/catch below.

Decorator for wrapping functions that enter a system context. This should decorate every method that may invoke some
user code later on down the line. This will allow us to add differentiation between what is a user error and
what is a system failure. Furthermore, we will clean the exception trace so as to make more sense to the
user -- allowing them to know if they should take action themselves or pass on to the platform owners.
We will dispatch metrics and such appropriately.


| Parameter | Type |
|-|-|
| `wrapped` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### user_entry_point()

```python
def user_entry_point(
    wrapped,
    args,
    kwargs,
)
```
See the comment for the system_entry_point above as well.

Decorator for wrapping functions that enter into a user context.  This will help us differentiate user-created
failures even when it is re-entrant into system code.

Note: a user_entry_point can ONLY ever be called from within a @system_entry_point wrapped function, therefore,
we can always ensure we will hit a system_entry_point to correctly reformat our exceptions.  Also, any exception
we create here will only be handled within our system code so we don't need to worry about leaking weird exceptions
to the user.


| Parameter | Type |
|-|-|
| `wrapped` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

## flytekit.exceptions.scopes.FlyteScopedException

Common base class for all non-exit exceptions.


```python
class FlyteScopedException(
    context,
    exc_type,
    exc_value,
    exc_tb,
    top_trim,
    bottom_trim,
    kind,
)
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
| `error_code` |  |  |
| `kind` |  |  |
| `traceback` |  |  |
| `type` |  |  |
| `value` |  |  |
| `verbose_message` |  |  |

## flytekit.exceptions.scopes.FlyteScopedSystemException

Common base class for all non-exit exceptions.


```python
class FlyteScopedSystemException(
    exc_type,
    exc_value,
    exc_tb,
    kwargs,
)
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
| `error_code` |  |  |
| `kind` |  |  |
| `traceback` |  |  |
| `type` |  |  |
| `value` |  |  |
| `verbose_message` |  |  |

## flytekit.exceptions.scopes.FlyteScopedUserException

Common base class for all non-exit exceptions.


```python
class FlyteScopedUserException(
    exc_type,
    exc_value,
    exc_tb,
    kwargs,
)
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
| `error_code` |  |  |
| `kind` |  |  |
| `traceback` |  |  |
| `type` |  |  |
| `value` |  |  |
| `verbose_message` |  |  |

