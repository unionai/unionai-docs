---
title: Enum type
weight: 8
variants: "+flyte +serverless +byoc +byok"
---

# Enum type

At times, you might need to limit the acceptable values for inputs or outputs to a predefined set.
This common requirement is usually met by using Enum types in programming languages.

You can create a Python Enum type and utilize it as an input or output for a task.
{@= Kit =@} will automatically convert it and constrain the inputs and outputs to the predefined set of values.

{{-- note >}}
Currently, only string values are supported as valid enum values.
{@= Product =@} assumes the first value in the list as the default, and Enum types cannot be optional.
Therefore, when defining enums, it's important to design them with the first value as a valid default.
{{-- /note >}}

{{< if-variant flyte >}}
{{-- note >}}
To clone and run the example code on this page, see the [Flytesnacks repo](https://github.com/flyteorg/flytesnacks/tree/master/examples/data_types_and_io/).
{{-- /note >}}
{{< /if-variant >}}

To begin, import the dependencies:

```python
from enum import Enum
from union
```

We define an enum and a simple coffee maker workflow that accepts an order and brews coffee ☕️ accordingly.
The assumption is that the coffee maker only understands enum inputs:

```python
class Coffee(Enum):
    ESPRESSO = "espresso"
    AMERICANO = "americano"
    LATTE = "latte"
    CAPPUCCINO = "cappucccino"


@union.task
def take_order(coffee: str) -> Coffee:
    return Coffee(coffee)


@union.task
def prep_order(coffee_enum: Coffee) -> str:
    return f"Preparing {coffee_enum.value} ..."


@union.workflow
def coffee_maker(coffee: str) -> str:
    coffee_enum = take_order(coffee=coffee)
    return prep_order(coffee_enum=coffee_enum)


# The workflow can also accept an enum value
@union.workflow
def coffee_maker_enum(coffee_enum: Coffee) -> str:
    return prep_order(coffee_enum=coffee_enum)
```

The workflow can also accept an enum value:

```python
@union.workflow
def coffee_maker_enum(coffee_enum: Coffee) -> str:
    return prep_order(coffee_enum=coffee_enum)
```

{{< if-variant flyte >}}

You can send a string to the `coffee_maker_enum` workflow during its execution, like this:
```
pyflyte run \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/69dbe4840031a85d79d9ded25f80397c6834752d/examples/data_types_and_io/data_types_and_io/enum_type.py \
  coffee_maker_enum --coffee_enum="latte"
```

{{< /if-variant >}}
{{< if-variant "byoc byok serverless" >}}

You can send a string to the `coffee_maker_enum` workflow during its execution, like this:
```
union run \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/69dbe4840031a85d79d9ded25f80397c6834752d/examples/data_types_and_io/data_types_and_io/enum_type.py \
  coffee_maker_enum --coffee_enum="latte"
```

{{< /if-variant >}}

You can run the workflows locally:

```python
if __name__ == "__main__":
    print(coffee_maker(coffee="latte"))
    print(coffee_maker_enum(coffee_enum=Coffee.LATTE))
```