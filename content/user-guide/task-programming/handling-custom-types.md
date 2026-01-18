---
title: Custom types
weight: 90
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Custom types

Flyte has a rich type system that handles most Python types automatically. However, there are cases where you may want to pass custom types into a run or between actions. By default, if Flyte doesn't recognize a type, it uses Python pickle to serialize the data. While this works, pickle has several drawbacks:

- **Inefficiency**: Pickle can be very inefficient for certain data types
- **Language compatibility**: Pickle is Python-specific and doesn't work with other languages
- **Version fragility**: Pickled data can break between Python versions
- **Opacity**: Pickled data appears as bytes or file links in the UI, with no automatic form generation

Consider types like Polars DataFrames or PyTorch Tensors. Using pickle for these is extremely inefficient compared to native serialization formats like Parquet or tensor-specific formats.

Flyte SDK addresses this by allowing you to create and share type extensions.

## Types of extensions

Flyte supports two types of type extensions:

1. **Type transformers**: For scalar types (integers, strings, files, directories, custom objects)
2. **DataFrame extensions**: For tabular data types that benefit from DataFrame-specific handling

DataFrame types are special because they have associated metadata (columns, schemas), can be serialized to efficient formats like Parquet, support parallel uploads from engines like Spark, and can be partitioned.

## Creating a type transformer

Type transformers convert between Python types and Flyte's internal representation. Here's how to create one for a custom `PositiveInt` type.

### Step 1: Define your custom type

```python
# custom_type.py
class PositiveInt:
    """A wrapper type that only accepts positive integers."""

    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f"Expected int, got {type(value).__name__}")
        if value <= 0:
            raise ValueError(f"Expected positive integer, got {value}")
        self._value = value

    @property
    def value(self) -> int:
        return self._value

    def __repr__(self) -> str:
        return f"PositiveInt({self._value})"
```

### Step 2: Create the type transformer

```python
# transformer.py
from typing import Type

from flyteidl2.core import literals_pb2, types_pb2

from flyte import logger
from flyte.types import TypeEngine, TypeTransformer, TypeTransformerFailedError
from my_transformer.custom_type import PositiveInt


class PositiveIntTransformer(TypeTransformer[PositiveInt]):
    """
    Type transformer for PositiveInt that validates and transforms positive integers.
    """

    def __init__(self):
        super().__init__(name="PositiveInt", t=PositiveInt)

    def get_literal_type(self, t: Type[PositiveInt]) -> types_pb2.LiteralType:
        """Returns the Flyte literal type for PositiveInt."""
        return types_pb2.LiteralType(
            simple=types_pb2.SimpleType.INTEGER,
            structure=types_pb2.TypeStructure(tag="PositiveInt"),
        )

    async def to_literal(
        self,
        python_val: PositiveInt,
        python_type: Type[PositiveInt],
        expected: types_pb2.LiteralType,
    ) -> literals_pb2.Literal:
        """Converts a PositiveInt instance to a Flyte Literal."""
        if not isinstance(python_val, PositiveInt):
            raise TypeTransformerFailedError(
                f"Expected PositiveInt, got {type(python_val).__name__}"
            )

        return literals_pb2.Literal(
            scalar=literals_pb2.Scalar(
                primitive=literals_pb2.Primitive(integer=python_val.value)
            )
        )

    async def to_python_value(
        self,
        lv: literals_pb2.Literal,
        expected_python_type: Type[PositiveInt]
    ) -> PositiveInt:
        """Converts a Flyte Literal back to a PositiveInt instance."""
        if not lv.scalar or not lv.scalar.primitive:
            raise TypeTransformerFailedError(
                f"Cannot convert literal {lv} to PositiveInt: missing scalar primitive"
            )

        value = lv.scalar.primitive.integer
        try:
            return PositiveInt(value)
        except (TypeError, ValueError) as e:
            raise TypeTransformerFailedError(
                f"Cannot convert value {value} to PositiveInt: {e}"
            )

    def guess_python_type(
        self,
        literal_type: types_pb2.LiteralType
    ) -> Type[PositiveInt]:
        """Guesses the Python type from a Flyte literal type."""
        if (
            literal_type.simple == types_pb2.SimpleType.INTEGER
            and literal_type.structure
            and literal_type.structure.tag == "PositiveInt"
        ):
            return PositiveInt
        raise ValueError(f"Cannot guess PositiveInt from literal type {literal_type}")
```

### Step 3: Register the transformer

Create a registration function that can be called to register your transformer:

```python
def register_positive_int_transformer():
    """Register the PositiveIntTransformer in the TypeEngine."""
    TypeEngine.register(PositiveIntTransformer())
    logger.info("Registered PositiveIntTransformer in TypeEngine")
```

## Distributing type plugins

To share your type transformer as an installable package, configure it as a Flyte plugin using entry points.

### Configure pyproject.toml

Add the entry point to your `pyproject.toml`:

```toml
[project]
name = "my_transformer"
version = "0.1.0"
description = "Custom type transformer"
requires-python = ">=3.10"
dependencies = []

[project.entry-points."flyte.plugins.types"]
my_transformer = "my_transformer.transformer:register_positive_int_transformer"
```

The entry point group `flyte.plugins.types` tells Flyte to automatically load this transformer when the package is installed.

### Automatic loading

When your plugin package is installed, Flyte automatically loads the type transformer at runtime. This happens during `flyte.init()` or `flyte.init_from_config()`.

## Controlling plugin loading

Loading many type plugins can add overhead to initialization. You can disable automatic plugin loading:

```python
import flyte

# Disable automatic loading of type transformer plugins
flyte.init(load_plugin_type_transformers=False)
```

By default, `load_plugin_type_transformers` is `True`.

## Using custom types in tasks

Once registered, use your custom type like any built-in type:

```python
import flyte
from my_transformer.custom_type import PositiveInt

env = flyte.TaskEnvironment(name="custom_types")

@env.task
async def process_positive(value: PositiveInt) -> int:
    """Process a positive integer."""
    return value.value * 2

if __name__ == "__main__":
    flyte.init_from_config()

    # The custom type works seamlessly
    run = flyte.run(process_positive, value=PositiveInt(42))
    run.wait()
    print(run.outputs()[0])  # 84
```

## DataFrame extensions

For tabular data types, Flyte provides a specialized extension mechanism through `flyte.io.DataFrame`. DataFrame extensions support:

- Automatic conversion to/from Parquet format
- Column metadata and schema information
- Parallel uploads from distributed engines
- Partitioning support

DataFrame extensions use encoders and decoders from `flyte.io.extend`. Documentation for creating DataFrame extensions is coming soon.

## Best practices

1. **Use specific types over pickle**: Define type transformers for any custom types used frequently in your workflows
2. **Keep transformers lightweight**: Avoid expensive operations in `to_literal` and `to_python_value`
3. **Add validation**: Validate data in your transformer to catch errors early
4. **Use meaningful tags**: The `TypeStructure.tag` helps identify your type in the Flyte UI
5. **Be judicious with plugins**: Only install the plugins you need to minimize initialization overhead
