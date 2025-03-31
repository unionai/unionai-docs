---
title: flytekit.utils.asyn
version: 0.1.dev2175+gcd6bd01.d20250325
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

### Classes

| Class | Description |
|-|-|
| [`Any`](.././flytekit.utils.asyn#flytekitutilsasynany) | Special type indicating an unconstrained type. |
| [`ParamSpec`](.././flytekit.utils.asyn#flytekitutilsasynparamspec) | Parameter specification variable. |
| [`TypeVar`](.././flytekit.utils.asyn#flytekitutilsasyntypevar) | Type variable. |

### Methods

| Method | Description |
|-|-|
| [`_selector_policy()`](#_selector_policy) |  |
| [`contextmanager()`](#contextmanager) | @contextmanager decorator. |
| [`run_sync()`](#run_sync) | This should be called from synchronous functions to run an async function. |


### Variables

| Property | Type | Description |
|-|-|-|
| `P` | `ParamSpec` |  |
| `T` | `TypeVar` |  |
| `logger` | `Logger` |  |
| `loop_manager` | `_AsyncLoopManager` |  |

## Methods

#### _selector_policy()

```python
def _selector_policy()
```
#### contextmanager()

```python
def contextmanager(
    func,
)
```
@contextmanager decorator.

Typical usage:

@contextmanager
def some_generator({arguments}):
{setup}
try:
yield {value}
finally:
{cleanup}

This makes this:

with some_generator({arguments}) as {variable}:
{body}

equivalent to this:

{setup}
try:
{variable} = {value}
{body}
finally:
{cleanup}


| Parameter | Type |
|-|-|
| `func` |  |

#### run_sync()

```python
def run_sync(
    coro_func: typing.Callable[..., typing.Awaitable[~T]],
    args,
    kwargs,
) -> ~T
```
This should be called from synchronous functions to run an async function.


| Parameter | Type |
|-|-|
| `coro_func` | `typing.Callable[..., typing.Awaitable[~T]]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

## flytekit.utils.asyn.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.utils.asyn.ParamSpec

Parameter specification variable.

The preferred way to construct a parameter specification is via the
dedicated syntax for generic functions, classes, and type aliases,
where the use of '**' creates a parameter specification::

type IntFunc[**P] = Callable[P, int]

The following syntax creates a parameter specification that defaults
to a callable accepting two positional-only arguments of types int
and str:

type IntFuncDefault[**P = (int, str)] = Callable[P, int]

For compatibility with Python 3.11 and earlier, ParamSpec objects
can also be created as follows::

P = ParamSpec('P')
DefaultP = ParamSpec('DefaultP', default=(int, str))

Parameter specification variables exist primarily for the benefit of
static type checkers.  They are used to forward the parameter types of
one callable to another callable, a pattern commonly found in
higher-order functions and decorators.  They are only valid when used
in ``Concatenate``, or as the first argument to ``Callable``, or as
parameters for user-defined Generics. See class Generic for more
information on generic types.

An example for annotating a decorator::

def add_logging[**P, T](f: Callable[P, T]) -> Callable[P, T]:
'''A type-safe decorator to add logging to a function.'''
def inner(*args: P.args, **kwargs: P.kwargs) -> T:
logging.info(f'{f.__name__} was called')
return f(*args, **kwargs)
return inner

@add_logging
def add_two(x: float, y: float) -> float:
'''Add two numbers together.'''
return x + y

Parameter specification variables can be introspected. e.g.::

>>> P = ParamSpec("P")
>>> P.__name__
'P'

Note that only parameter specification variables defined in the global
scope can be pickled.


## flytekit.utils.asyn.TypeVar

Type variable.

The preferred way to construct a type variable is via the dedicated
syntax for generic functions, classes, and type aliases::

class Sequence[T]:  # T is a TypeVar
...

This syntax can also be used to create bound and constrained type
variables::

# S is a TypeVar bound to str
class StrSequence[S: str]:
...

# A is a TypeVar constrained to str or bytes
class StrOrBytesSequence[A: (str, bytes)]:
...

Type variables can also have defaults:

class IntDefault[T = int]:
...

However, if desired, reusable type variables can also be constructed
manually, like so::

T = TypeVar('T')  # Can be anything
S = TypeVar('S', bound=str)  # Can be any subtype of str
A = TypeVar('A', str, bytes)  # Must be exactly str or bytes
D = TypeVar('D', default=int)  # Defaults to int

Type variables exist primarily for the benefit of static type
checkers.  They serve as the parameters for generic types as well
as for generic function and type alias definitions.

The variance of type variables is inferred by type checkers when they
are created through the type parameter syntax and when
``infer_variance=True`` is passed. Manually created type variables may
be explicitly marked covariant or contravariant by passing
``covariant=True`` or ``contravariant=True``. By default, manually
created type variables are invariant. See PEP 484 and PEP 695 for more
details.


