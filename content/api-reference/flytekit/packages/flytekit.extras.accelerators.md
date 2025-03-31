---
title: flytekit.extras.accelerators
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.extras.accelerators


Specifying Accelerators
==========================

.. tags:: MachineLearning, Advanced, Hardware

Flyte allows you to specify `gpu` resources for a given task. However, in some cases, you may want to use a different
accelerator type, such as TPU, specific variations of GPUs, or fractional GPUs. You can configure the Flyte backend to
use your preferred accelerators, and those who write workflow code can import the `flytekit.extras.accelerators` module
to specify an accelerator in the task decorator.


If you want to use a specific GPU device, you can pass the device name directly to the task decorator, e.g.:

.. code-block::

    @task(
        limits=Resources(gpu="1"),
        accelerator=GPUAccelerator("nvidia-tesla-v100"),
    )
    def my_task() -> None:
        ...


Base Classes
------------
These classes can be used to create custom accelerator type constants. For example, you can create a TPU accelerator.



.. currentmodule:: flytekit.extras.accelerators

.. autosummary::
   :template: custom.rst
   :toctree: generated/
   :nosignatures:

   BaseAccelerator
   GPUAccelerator
   MultiInstanceGPUAccelerator

But, often, you may want to use a well known accelerator type, and to simplify this, flytekit provides a set of
predefined accelerator constants, as described in the next section.


Predefined Accelerator Constants
--------------------------------

The `flytekit.extras.accelerators` module provides some constants for known accelerators, listed below, but this is not
a complete list. If you know the name of the accelerator, you can pass the string name to the task decorator directly.

If using the constants, you can import them directly from the module, e.g.:

.. code-block::

    from flytekit.extras.accelerators import T4

    @task(
        limits=Resources(gpu="1"),
        accelerator=T4,
    )
    def my_task() -> None:
        ...

if you want to use a fractional GPU, you can use the ``partitioned`` method on the accelerator constant, e.g.:

.. code-block::

    from flytekit.extras.accelerators import A100

    @task(
        limits=Resources(gpu="1"),
        accelerator=A100.partition_2g_10gb,
    )
    def my_task() -> None:
        ...

.. currentmodule:: flytekit.extras.accelerators

.. autosummary::
   :toctree: generated/
   :nosignatures:

   A10G
   L4
   K80
   M60
   P4
   P100
   T4
   V100
   A100
   A100_80GB


## Directory

### Classes

| Class | Description |
|-|-|
| [`BaseAccelerator`](.././flytekit.extras.accelerators#flytekitextrasacceleratorsbaseaccelerator) | Base class for all accelerator types. |
| [`GPUAccelerator`](.././flytekit.extras.accelerators#flytekitextrasacceleratorsgpuaccelerator) | Class that represents a GPU accelerator. |
| [`Generic`](.././flytekit.extras.accelerators#flytekitextrasacceleratorsgeneric) | Abstract base class for generic types. |
| [`MultiInstanceGPUAccelerator`](.././flytekit.extras.accelerators#flytekitextrasacceleratorsmultiinstancegpuaccelerator) | Base class for all multi-instance GPU accelerator types. |
| [`TypeVar`](.././flytekit.extras.accelerators#flytekitextrasacceleratorstypevar) | Type variable. |

### Variables

| Property | Type | Description |
|-|-|-|
| `A100` | `_A100` |  |
| `A100_80GB` | `_A100_80GB` |  |
| `A10G` | `GPUAccelerator` |  |
| `K80` | `GPUAccelerator` |  |
| `L4` | `GPUAccelerator` |  |
| `L4_VWS` | `GPUAccelerator` |  |
| `M60` | `GPUAccelerator` |  |
| `MIG` | `TypeVar` |  |
| `P100` | `GPUAccelerator` |  |
| `P4` | `GPUAccelerator` |  |
| `T` | `TypeVar` |  |
| `T4` | `GPUAccelerator` |  |
| `V100` | `GPUAccelerator` |  |
| `V5E` | `_V5E` |  |
| `V5P` | `_V5P` |  |
| `V6E` | `_V6E` |  |

## flytekit.extras.accelerators.BaseAccelerator

Base class for all accelerator types. This class is not meant to be instantiated directly.


### Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.extras.accelerators.GPUAccelerator

Class that represents a GPU accelerator. The class can be instantiated with any valid GPU device name, but
it is recommended to use one of the pre-defined constants below, as name has to match the name of the device
configured on the cluster.


```python
class GPUAccelerator(
    device: str,
)
```
| Parameter | Type |
|-|-|
| `device` | `str` |

### Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.extras.accelerators.Generic

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


## flytekit.extras.accelerators.MultiInstanceGPUAccelerator

Base class for all multi-instance GPU accelerator types. It is recommended to use one of the pre-defined constants
below, as name has to match the name of the device configured on the cluster.
For example, to specify a 10GB partition of an A100 GPU, use ``A100.partition_2g_10gb``.


### Methods

| Method | Description |
|-|-|
| [`partitioned()`](#partitioned) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### partitioned()

```python
def partitioned(
    partition_size: str,
) -> ~MIG
```
| Parameter | Type |
|-|-|
| `partition_size` | `str` |

#### to_flyte_idl()

```python
def to_flyte_idl()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `unpartitioned` |  |  |

## flytekit.extras.accelerators.TypeVar

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


