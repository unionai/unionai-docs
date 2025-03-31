---
title: flytekit.core.hash
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.hash

## Directory

### Classes

| Class | Description |
|-|-|
| [`Generic`](.././flytekit.core.hash#flytekitcorehashgeneric) | Abstract base class for generic types. |
| [`HashMethod`](.././flytekit.core.hash#flytekitcorehashhashmethod) | Flyte-specific object used to wrap the hash function for a specific type. |
| [`HashOnReferenceMixin`](.././flytekit.core.hash#flytekitcorehashhashonreferencemixin) | None. |
| [`TypeVar`](.././flytekit.core.hash#flytekitcorehashtypevar) | Type variable. |

## flytekit.core.hash.Generic

Abstract base class for generic types.

On Python 3.12 and newer, generic classes implicitly inherit from
Generic when they declare a parameter list after the class's name::

class Mapping[KT, VT]:
def __getitem__(self, key: KT) -> VT:
...
# Etc.

On older versions of Python, however, generic classes have to
explicitly inherit from Generic.

After a class has been declared to be generic, it can then be used as
follows::

def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
try:
return mapping[key]
except KeyError:
return default


## flytekit.core.hash.HashMethod

Flyte-specific object used to wrap the hash function for a specific type


```python
def HashMethod(
    function: typing.Callable[[~T], str],
):
```
| Parameter | Type |
|-|-|
| `function` | `typing.Callable[[~T], str]` |

### Methods

| Method | Description |
|-|-|
| [`calculate()`](#calculate) | Calculate hash for `obj` |


#### calculate()

```python
def calculate(
    obj: ~T,
):
```
Calculate hash for `obj`.


| Parameter | Type |
|-|-|
| `obj` | `~T` |

## flytekit.core.hash.HashOnReferenceMixin

## flytekit.core.hash.TypeVar

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


