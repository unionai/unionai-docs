---
title: flytekit.extras.tensorflow.record
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extras.tensorflow.record

## Directory

### Classes

| Class | Description |
|-|-|
| [`TFRecordDatasetConfig`](.././flytekit.extras.tensorflow.record#flytekitextrastensorflowrecordtfrecorddatasetconfig) | TFRecordDatasetConfig can be used while creating tf. |
| [`TensorFlowRecordFileTransformer`](.././flytekit.extras.tensorflow.record#flytekitextrastensorflowrecordtensorflowrecordfiletransformer) | TypeTransformer that supports serialising and deserialising to and from TFRecord file. |
| [`TensorFlowRecordsDirTransformer`](.././flytekit.extras.tensorflow.record#flytekitextrastensorflowrecordtensorflowrecordsdirtransformer) | TypeTransformer that supports serialising and deserialising to and from TFRecord directory. |

### Methods

| Method | Description |
|-|-|
| [`extract_metadata_and_uri()`](#extract_metadata_and_uri) |  |


## Methods

#### extract_metadata_and_uri()

```python
def extract_metadata_and_uri(
    lv: flytekit.models.literals.Literal,
    t: typing.Type[typing.Union[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass, flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass]],
) -> typing.Tuple[typing.Union[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass, flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass], flytekit.extras.tensorflow.record.TFRecordDatasetConfig]
```
| Parameter | Type | Description |
|-|-|-|
| `lv` | `flytekit.models.literals.Literal` | |
| `t` | `typing.Type[typing.Union[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass, flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass]]` | |

## flytekit.extras.tensorflow.record.TFRecordDatasetConfig

TFRecordDatasetConfig can be used while creating tf.data.TFRecordDataset comprising
record of one or more TFRecord files.



```python
class TFRecordDatasetConfig(
    compression_type: typing.Optional[str],
    buffer_size: typing.Optional[int],
    num_parallel_reads: typing.Optional[int],
    name: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `compression_type` | `typing.Optional[str]` | |
| `buffer_size` | `typing.Optional[int]` | |
| `num_parallel_reads` | `typing.Optional[int]` | |
| `name` | `typing.Optional[str]` | |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`schema()`](#schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` | |
| `infer_missing` |  | |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` | |
| `parse_float` |  | |
| `parse_int` |  | |
| `parse_constant` |  | |
| `infer_missing` |  | |
| `kw` |  | |

#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type | Description |
|-|-|-|
| `infer_missing` | `bool` | |
| `only` |  | |
| `exclude` |  | |
| `many` | `bool` | |
| `context` |  | |
| `load_only` |  | |
| `dump_only` |  | |
| `partial` | `bool` | |
| `unknown` |  | |

#### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type | Description |
|-|-|-|
| `encode_json` |  | |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `skipkeys` | `bool` | |
| `ensure_ascii` | `bool` | |
| `check_circular` | `bool` | |
| `allow_nan` | `bool` | |
| `indent` | `typing.Union[int, str, NoneType]` | |
| `separators` | `typing.Tuple[str, str]` | |
| `default` | `typing.Callable` | |
| `sort_keys` | `bool` | |
| `kw` |  | |

## flytekit.extras.tensorflow.record.TensorFlowRecordFileTransformer

TypeTransformer that supports serialising and deserialising to and from TFRecord file.
https://www.tensorflow.org/tutorials/load_data/tfrecord


```python
def TensorFlowRecordFileTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[T],
    v: T,
)
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[T]` | |
| `v` | `T` | |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
) -> Optional[T]
```
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access.｀

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
    python val -> msgpack bytes -> binary literal scalar -> msgpack bytes -> python val
                  (to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
    python val -> msgpack bytes -> binary literal scalar -> resolved golang value -> binary literal scalar -> msgpack bytes -> python val
                  (to_literal)                            (propeller attribute access)                       (from_binary_idl)


| Parameter | Type | Description |
|-|-|-|
| `binary_idl_object` | `Binary` | |
| `expected_python_type` | `Type[T]` | |

#### from_generic_idl()

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

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Type[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass],
) -> flytekit.models.types.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Type[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass]` | |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: flytekit.models.types.LiteralType,
) -> typing.Type[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type | Description |
|-|-|-|
| `literal_type` | `flytekit.models.types.LiteralType` | |

#### isinstance_generic()

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

#### to_html()

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

#### to_literal()

```python
def to_literal(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass,
    python_type: typing.Type[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass],
    expected: flytekit.models.types.LiteralType,
) -> flytekit.models.literals.Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `python_val` | `flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass` | The actual value to be transformed |
| `python_type` | `typing.Type[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `flytekit.models.types.LiteralType` | Expected Literal Type |

#### to_python_value()

```python
def to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass],
) -> tensorflow.python.data.ops.readers.TFRecordDatasetV2
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | FlyteContext |
| `lv` | `flytekit.models.literals.Literal` | The received literal Value |
| `expected_python_type` | `typing.Type[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass]` | Expected native python type that should be returned |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.extras.tensorflow.record.TensorFlowRecordsDirTransformer

TypeTransformer that supports serialising and deserialising to and from TFRecord directory.
https://www.tensorflow.org/tutorials/load_data/tfrecord


```python
def TensorFlowRecordsDirTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[T],
    v: T,
)
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[T]` | |
| `v` | `T` | |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
) -> Optional[T]
```
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access.｀

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
    python val -> msgpack bytes -> binary literal scalar -> msgpack bytes -> python val
                  (to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
    python val -> msgpack bytes -> binary literal scalar -> resolved golang value -> binary literal scalar -> msgpack bytes -> python val
                  (to_literal)                            (propeller attribute access)                       (from_binary_idl)


| Parameter | Type | Description |
|-|-|-|
| `binary_idl_object` | `Binary` | |
| `expected_python_type` | `Type[T]` | |

#### from_generic_idl()

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

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Type[flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass],
) -> flytekit.models.types.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Type[flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass]` | |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: flytekit.models.types.LiteralType,
) -> typing.Type[flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type | Description |
|-|-|-|
| `literal_type` | `flytekit.models.types.LiteralType` | |

#### isinstance_generic()

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

#### to_html()

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

#### to_literal()

```python
def to_literal(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass,
    python_type: typing.Type[flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass],
    expected: flytekit.models.types.LiteralType,
) -> flytekit.models.literals.Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `python_val` | `flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass` | The actual value to be transformed |
| `python_type` | `typing.Type[flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `flytekit.models.types.LiteralType` | Expected Literal Type |

#### to_python_value()

```python
def to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass],
) -> tensorflow.python.data.ops.readers.TFRecordDatasetV2
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | FlyteContext |
| `lv` | `flytekit.models.literals.Literal` | The received literal Value |
| `expected_python_type` | `typing.Type[flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass]` | Expected native python type that should be returned |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

