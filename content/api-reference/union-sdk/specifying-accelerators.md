# Specifying accelerators

Flyte allows you to specify `gpu` resources for a given task. However, in some cases, you may want to use a different accelerator type, such as TPU, specific variations of GPUs, or fractional GPUs. You can configure the Flyte backend to use your preferred accelerators, and those who write workflow code can import the `flytekit.extras.accelerators` module to specify an accelerator in the task decorator.


If you want to use a specific GPU device, you can pass the device name directly to the task decorator, e.g.:

{{< highlight python >}}
@union.task(
    limits=Resources(gpu="1"),
    accelerator=GPUAccelerator("nvidia-tesla-v100"),
)
def my_task() -> None:
    ...
{{< /highlight >}}

## Predefined accelerator constants

The `flytekit.extras.accelerators` module provides some constants for known accelerators, listed below, but this is not a complete list. If you know the name of the accelerator, you can pass the string name to the task decorator directly.

```--note--
If you need to create a custom accelerator constant, see [Base classes for custom accelerators](#base-classes-for-custom-accelerator-constants)
```

You can import constants directly from the module:

{{< highlight python >}}
from flytekit.extras.accelerators import T4

@union.task(
    limits=Resources(gpu="1"),
    accelerator=T4,
)
def my_task() -> None:
    ...
{{< /highlight >}}

To use a fractional GPU, you can use the `partitioned` method on the accelerator constant:

{{< highlight python >}}
from flytekit.extras.accelerators import A100

@union.task(
    limits=Resources(gpu="1"),
    accelerator=A100.partition_2g_10gb,
)
def my_task() -> None:
    ...
{{< /highlight >}}

```--eval-rst--
.. currentmodule:: flytekit.extras.accelerators

.. autosummary::
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
```

## Base classes for custom accelerator constants

These classes can be used to create custom accelerator type constants. For example, you can create a TPU accelerator.

```--eval-rst--

.. currentmodule:: flytekit.extras.accelerators

.. autoclass:: BaseAccelerator
    :members:

.. autoclass:: GPUAccelerator
    :members:

.. autoclass:: MultiInstanceGPUAccelerator
    :members:
```
