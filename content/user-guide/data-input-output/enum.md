---
title: Enum type
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
---

# Enum type

At times, you might need to limit the acceptable values for inputs or outputs to a predefined set.
This common requirement is usually met by using `Enum` types in programming languages.

You can create a Python `Enum` type and utilize it as an input or output for a task.
{{< key kit_name >}} will automatically convert it and constrain the inputs and outputs to the predefined set of values.

> [!NOTE]
> Currently, only string values are supported as valid `Enum` values.
> {{< key product_name >}} assumes the first value in the list as the default, and `Enum` types cannot be optional.
> Therefore, when defining `Enum`s, it's important to design them with the first value as a valid default.

We define an `Enum` and a simple coffee maker workflow that accepts an order and brews coffee ☕️ accordingly.
The assumption is that the coffee maker only understands `Enum` inputs:

```python
# coffee_maker.py

from enum import Enum

import {{< key kit_import >}}

class Coffee(Enum):
    ESPRESSO = "espresso"
    AMERICANO = "americano"
    LATTE = "latte"
    CAPPUCCINO = "cappucccino"


@{{< key kit_as >}}.task
def take_order(coffee: str) -> Coffee:
    return Coffee(coffee)


@{{< key kit_as >}}.task
def prep_order(coffee_enum: Coffee) -> str:
    return f"Preparing {coffee_enum.value} ..."


@{{< key kit_as >}}.workflow
def coffee_maker(coffee: str) -> str:
    coffee_enum = take_order(coffee=coffee)
    return prep_order(coffee_enum=coffee_enum)

# The workflow can also accept an enum value
@{{< key kit_as >}}.workflow
def coffee_maker_enum(coffee_enum: Coffee) -> str:
    return prep_order(coffee_enum=coffee_enum)
```

You can specify value for the parameter `coffee_enum` on run:

```shell
$ {{< key cli >}} run coffee_maker.py coffee_maker_enum --coffee_enum="latte"
```
