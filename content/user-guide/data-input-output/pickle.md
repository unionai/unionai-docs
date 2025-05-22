---
title: Pickle type
weight: 8
variants: +flyte +serverless +byoc +selfmanaged
---

# Pickle type


{{< key product_name >}} enforces type safety by utilizing type information for compiling tasks and workflows,
enabling various features such as static analysis and conditional branching.

However, we also strive to offer flexibility to end-users, so they don't have to invest heavily
in understanding their data structures upfront before experiencing the value {{< key product_name >}} has to offer.

{{< key product_name >}} supports the `FlytePickle` transformer, which converts any unrecognized type hint into `FlytePickle`,
enabling the serialization/deserialization of Python values to/from a pickle file.

> [!NOTE]
> Pickle can only be used to send objects between the exact same Python version.
> For optimal performance, it's advisable to either employ Python types that are supported by {{< key product_name >}}
> or register a custom transformer, as using pickle types can result in lower performance.

This example demonstrates how you can utilize custom objects without registering a transformer.

{{< variant flyte >}}
{{< markdown >}}

<!-- TODO: Remove mention of FLytesnacks repo below -->
> [!NOTE]
> To clone and run the example code on this page, see the [Flytesnacks repo](https://github.com/flyteorg/flytesnacks/tree/master/examples/data_types_and_io/).

{{< /markdown >}}
{{< /variant >}}

```python
import {{< key kit_import >}}
```

`Superhero` represents a user-defined complex type that can be serialized to a pickle file by {{< key kit_name >}}
and transferred between tasks as both input and output data.

> [!NOTE]
> Alternatively, you can [turn this object into a dataclass](./dataclass) for improved performance.
> We have used a simple object here for demonstration purposes.

```python
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power


@{{< key kit_as >}}.task
def welcome_superhero(name: str, power: str) -> Superhero:
    return Superhero(name, power)


@{{< key kit_as >}}.task
def greet_superhero(superhero: Superhero) -> str:
    return f"👋 Hello {superhero.name}! Your superpower is {superhero.power}."


@{{< key kit_as >}}.workflow
def superhero_wf(name: str = "Thor", power: str = "Flight") -> str:
    superhero = welcome_superhero(name=name, power=power)
    return greet_superhero(superhero=superhero)
```