---
title: DataclassTransformer
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DataclassTransformer

**Package:** `flytekit.core.type_engine`

The Dataclass Transformer provides a type transformer for dataclasses.

The dataclass is converted to and from MessagePack Bytes by the mashumaro library
and is transported between tasks using the Binary IDL representation.
Also, the type declaration will try to extract the JSON Schema for the
object, if possible, and pass it with the definition.

The lifecycle of the dataclass in the Flyte type system is as follows:

1. Serialization: The dataclass transformer converts the dataclass to MessagePack Bytes.
    (1) Handle dataclass attributes to make them serializable with mashumaro.
    (2) Use the mashumaro API to serialize the dataclass to MessagePack Bytes.
    (3) Use MessagePack Bytes to create a Flyte Literal.
    (4) Serialize the Flyte Literal to a Binary IDL Object.

2. Deserialization: The dataclass transformer converts the MessagePack Bytes back to a dataclass.
    (1) Convert MessagePack Bytes to a dataclass using mashumaro.
    (2) Handle dataclass attributes to ensure they are of the correct types.

For Json Schema, we use https://github.com/fuhrysteve/marshmallow-jsonschema library.

Example

```python
@dataclass
class Test(DataClassJsonMixin):
    a: int
    b: str

from marshmallow_jsonschema import JSONSchema
t = Test(a=10,b="e")
JSONSchema().dump(t.schema())
```

Output will look like

```python
{'$schema': 'http://json-schema.org/draft-07/schema#',
    'definitions': {'TestSchema': {'properties': {'a': {'title': 'a',
        'type': 'number',
        'format': 'integer'},
    'b': {'title': 'b', 'type': 'string'}},
    'type': 'object',
    'additionalProperties': False}},
    '$ref': '#/definitions/TestSchema'}


&gt; [!NOTE]
&gt; The schema support is experimental and is useful for auto-completing in the UI/CLI




```python
def DataclassTransformer()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `is_async` | `None` |  |
| `name` | `None` |  |
| `python_type` | `None` | This returns the python type |
| `type_assertions_enabled` | `None` | Indicates if the transformer wants type assertions to be enabled at the core type engine layer |

## Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Extracts the Literal type definition for a Dataclass and returns a type Struct. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_generic_literal()`](#to_generic_literal) | Serializes a dataclass or dictionary to a Flyte literal, handling both JSON and MessagePack formats. |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


### assert_type()

```python
def assert_type(
    expected_type: Type[DataClassJsonMixin],
    v: T,
)
```
| Parameter | Type | Description |
|-|-|-|
| `expected_type` | `Type[DataClassJsonMixin]` | |
| `v` | `T` | |

### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
) -> T
```
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access.｀

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
    python val -&gt; msgpack bytes -&gt; binary literal scalar -&gt; msgpack bytes -&gt; python val
                  (to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
    python val -&gt; msgpack bytes -&gt; binary literal scalar -&gt; resolved golang value -&gt; binary literal scalar -&gt; msgpack bytes -&gt; python val
                  (to_literal)                            (propeller attribute access)                       (from_binary_idl)


| Parameter | Type | Description |
|-|-|-|
| `binary_idl_object` | `Binary` | |
| `expected_python_type` | `Type[T]` | |

### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[T],
) -> Optional[T]
```
TODO: Support all Flyte Types.
This is for dataclass attribute access from input created from the Flyte Console.

Note:
- This can be removed in the future when the Flyte Console support generate Binary IDL Scalar as input.


| Parameter | Type | Description |
|-|-|-|
| `generic` | `Struct` | |
| `expected_python_type` | `Type[T]` | |

### get_literal_type()

```python
def get_literal_type(
    t: Type[T],
) -> LiteralType
```
Extracts the Literal type definition for a Dataclass and returns a type Struct.
If possible also extracts the JSONSchema for the dataclass.


| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[T]` | |

### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type | Description |
|-|-|-|
| `obj` |  | |
| `generic_alias` |  | |

### to_generic_literal()

```python
def to_generic_literal(
    ctx: FlyteContext,
    python_val: T,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Serializes a dataclass or dictionary to a Flyte literal, handling both JSON and MessagePack formats.
Set `FLYTE_USE_OLD_DC_FORMAT=true` to use the old JSON-based format.
Note: This is deprecated and will be removed in the future.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `python_val` | `T` | |
| `python_type` | `Type[T]` | |
| `expected` | `LiteralType` | |

### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `python_val` | `T` | |
| `expected_python_type` | `Type[T]` | |

### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: T,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `python_val` | `T` | The actual value to be transformed |
| `python_type` | `Type[T]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `LiteralType` | Expected Literal Type |

### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> T
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | FlyteContext |
| `lv` | `Literal` | The received literal Value |
| `expected_python_type` | `Type[T]` | Expected native python type that should be returned |

