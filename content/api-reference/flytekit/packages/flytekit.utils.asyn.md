---
title: flytekit.utils.asyn
version: 1.15.4.dev2+g3e3ce2426
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
| [`ParamSpec`](.././flytekit.utils.asyn#flytekitutilsasynparamspec) | Parameter specification. |
| [`TypeVar`](.././flytekit.utils.asyn#flytekitutilsasyntypevar) | Type variable. |

## flytekit.utils.asyn.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.utils.asyn.ParamSpec

Parameter specification.


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

However, if desired, reusable type variables can also be constructed
manually, like so::

T = TypeVar('T')  # Can be anything
S = TypeVar('S', bound=str)  # Can be any subtype of str
A = TypeVar('A', str, bytes)  # Must be exactly str or bytes

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


