---
title: flytekit.exceptions.scopes
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.exceptions.scopes

## Directory

### Errors

| Exception | Description |
|-|-|
| [`FlyteScopedException`](../flytekit.exceptions.scopes/flytescopedexception) | Common base class for all non-exit exceptions. |
| [`FlyteScopedSystemException`](../flytekit.exceptions.scopes/flytescopedsystemexception) | Common base class for all non-exit exceptions. |
| [`FlyteScopedUserException`](../flytekit.exceptions.scopes/flytescopeduserexception) | Common base class for all non-exit exceptions. |

### Methods

| Method | Description |
|-|-|
| [`system_entry_point()`](#system_entry_point) | The reason these two (see the user one below) decorators exist is to categorize non-Flyte exceptions at arbitrary. |
| [`user_entry_point()`](#user_entry_point) | See the comment for the system_entry_point above as well. |


## Methods

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


| Parameter | Type | Description |
|-|-|-|
| `wrapped` |  | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

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


| Parameter | Type | Description |
|-|-|-|
| `wrapped` |  | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

