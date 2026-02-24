---
title: flytekitplugins.onnxscikitlearn.schema
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.onnxscikitlearn.schema

## Directory

### Classes

| Class | Description |
|-|-|
| [`ScikitLearn2ONNX`](.././flytekitplugins.onnxscikitlearn.schema#flytekitpluginsonnxscikitlearnschemascikitlearn2onnx) |  |
| [`ScikitLearn2ONNXConfig`](.././flytekitplugins.onnxscikitlearn.schema#flytekitpluginsonnxscikitlearnschemascikitlearn2onnxconfig) | ScikitLearn2ONNXConfig is the config used during the scikitlearn to ONNX conversion. |
| [`ScikitLearn2ONNXTransformer`](.././flytekitplugins.onnxscikitlearn.schema#flytekitpluginsonnxscikitlearnschemascikitlearn2onnxtransformer) |  |

### Methods

| Method | Description |
|-|-|
| [`extract_config()`](#extract_config) |  |
| [`to_onnx()`](#to_onnx) |  |


## Methods

#### extract_config()

```python
def extract_config(
    t: Type[ScikitLearn2ONNX],
) -> Tuple[Type[ScikitLearn2ONNX], ScikitLearn2ONNXConfig]
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[ScikitLearn2ONNX]` | |

#### to_onnx()

```python
def to_onnx(
    ctx,
    model,
    config,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` |  | |
| `model` |  | |
| `config` |  | |

## flytekitplugins.onnxscikitlearn.schema.ScikitLearn2ONNX

```python
class ScikitLearn2ONNX(
    model: sklearn.base.BaseEstimator,
)
```
| Parameter | Type | Description |
|-|-|-|
| `model` | `sklearn.base.BaseEstimator` | |

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

## flytekitplugins.onnxscikitlearn.schema.ScikitLearn2ONNXConfig

ScikitLearn2ONNXConfig is the config used during the scikitlearn to ONNX conversion.



```python
class ScikitLearn2ONNXConfig(
    initial_types: List[Tuple[str, Type]],
    name: Optional[str],
    doc_string: str,
    target_opset: Optional[int],
    custom_conversion_functions: Dict[Callable[..., Any], Callable[..., None]],
    custom_shape_calculators: Dict[Callable[..., Any], Callable[..., None]],
    custom_parsers: Dict[Callable[..., Any], Callable[..., None]],
    options: Dict[Any, Any],
    intermediate: bool,
    naming: Optional[Union[str, Callable[..., Any]]],
    white_op: Optional[Set[str]],
    black_op: Optional[Set[str]],
    verbose: int,
    final_types: Optional[List[Tuple[str, Type]]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `initial_types` | `List[Tuple[str, Type]]` | The types of the inputs to the model. |
| `name` | `Optional[str]` | The name of the graph in the produced ONNX model. |
| `doc_string` | `str` | A string attached onto the produced ONNX model. |
| `target_opset` | `Optional[int]` | The ONNX opset number. |
| `custom_conversion_functions` | `Dict[Callable[..., Any], Callable[..., None]]` | A dictionary for specifying the user customized conversion function. |
| `custom_shape_calculators` | `Dict[Callable[..., Any], Callable[..., None]]` | A dictionary for specifying the user customized shape calculator. |
| `custom_parsers` | `Dict[Callable[..., Any], Callable[..., None]]` | Parsers determine which outputs are expected for which particular task. |
| `options` | `Dict[Any, Any]` | Specific options given to converters. |
| `intermediate` | `bool` | If True, the function returns the converted model and the instance of Topology used, else, it returns the converted model. |
| `naming` | `Optional[Union[str, Callable[..., Any]]]` | Change the way intermediates are named. |
| `white_op` | `Optional[Set[str]]` | White list of ONNX nodes allowed while converting a pipeline. |
| `black_op` | `Optional[Set[str]]` | Black list of ONNX nodes disallowed while converting a pipeline. |
| `verbose` | `int` | Display progress while converting a model. |
| `final_types` | `Optional[List[Tuple[str, Type]]]` | Used to overwrite the type (if type is not None) and the name of every output. |

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

## flytekitplugins.onnxscikitlearn.schema.ScikitLearn2ONNXTransformer

```python
def ScikitLearn2ONNXTransformer()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` | `None` |  |
| `name` | `None` |  |
| `python_type` | `None` | This returns the python type |
| `type_assertions_enabled` | `None` | Indicates if the transformer wants type assertions to be enabled at the core type engine layer |

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
    t: Type[ScikitLearn2ONNX],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[ScikitLearn2ONNX]` | |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[ScikitLearn2ONNX]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type | Description |
|-|-|-|
| `literal_type` | `LiteralType` | |

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
    ctx: FlyteContext,
    python_val: ScikitLearn2ONNX,
    python_type: Type[ScikitLearn2ONNX],
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
| `python_val` | `ScikitLearn2ONNX` | The actual value to be transformed |
| `python_type` | `Type[ScikitLearn2ONNX]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `LiteralType` | Expected Literal Type |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[ONNXFile],
) -> ONNXFile
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | FlyteContext |
| `lv` | `Literal` | The received literal Value |
| `expected_python_type` | `Type[ONNXFile]` | Expected native python type that should be returned |

