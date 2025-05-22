---
title: flytekitplugins.great_expectations.schema
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.great_expectations.schema

## Directory

### Classes

| Class | Description |
|-|-|
| [`GreatExpectationsFlyteConfig`](.././flytekitplugins.great_expectations.schema#flytekitpluginsgreat_expectationsschemagreatexpectationsflyteconfig) | Use this configuration to configure GreatExpectations Plugin. |
| [`GreatExpectationsType`](.././flytekitplugins.great_expectations.schema#flytekitpluginsgreat_expectationsschemagreatexpectationstype) | Use this class to send the GreatExpectationsFlyteConfig. |
| [`GreatExpectationsTypeTransformer`](.././flytekitplugins.great_expectations.schema#flytekitpluginsgreat_expectationsschemagreatexpectationstypetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |

## flytekitplugins.great_expectations.schema.GreatExpectationsFlyteConfig

Use this configuration to configure GreatExpectations Plugin.



```python
class GreatExpectationsFlyteConfig(
    datasource_name: str,
    expectation_suite_name: str,
    data_connector_name: str,
    data_asset_name: typing.Optional[str],
    local_file_path: typing.Optional[str],
    checkpoint_params: typing.Optional[typing.Dict[str, typing.Union[str, typing.List[str]]]],
    batch_request_config: typing.Optional[flytekitplugins.great_expectations.task.BatchRequestConfig],
    context_root_dir: str,
)
```
| Parameter | Type |
|-|-|
| `datasource_name` | `str` |
| `expectation_suite_name` | `str` |
| `data_connector_name` | `str` |
| `data_asset_name` | `typing.Optional[str]` |
| `local_file_path` | `typing.Optional[str]` |
| `checkpoint_params` | `typing.Optional[typing.Dict[str, typing.Union[str, typing.List[str]]]]` |
| `batch_request_config` | `typing.Optional[flytekitplugins.great_expectations.task.BatchRequestConfig]` |
| `context_root_dir` | `str` |

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
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

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
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

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
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

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
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

## flytekitplugins.great_expectations.schema.GreatExpectationsType

Use this class to send the GreatExpectationsFlyteConfig.



### Methods

| Method | Description |
|-|-|
| [`config()`](#config) |  |


#### config()

```python
def config()
```
## flytekitplugins.great_expectations.schema.GreatExpectationsTypeTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
def GreatExpectationsTypeTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_config()`](#get_config) |  |
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
| Parameter | Type |
|-|-|
| `t` | `Type[T]` |
| `v` | `T` |

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


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `Type[T]` |

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


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `Type[T]` |

#### get_config()

```python
def get_config(
    t: typing.Type[flytekitplugins.great_expectations.schema.GreatExpectationsType],
) -> typing.Tuple[typing.Type, flytekitplugins.great_expectations.schema.GreatExpectationsFlyteConfig]
```
| Parameter | Type |
|-|-|
| `t` | `typing.Type[flytekitplugins.great_expectations.schema.GreatExpectationsType]` |

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Type[flytekitplugins.great_expectations.schema.GreatExpectationsType],
) -> flytekit.models.types.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.Type[flytekitplugins.great_expectations.schema.GreatExpectationsType]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[T]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `expected_python_type` | `Type[T]` |

#### to_literal()

```python
def to_literal(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: typing.Union[flytekit.types.file.file.FlyteFile, flytekit.types.schema.types.FlyteSchema, str],
    python_type: typing.Type[flytekitplugins.great_expectations.schema.GreatExpectationsType],
    expected: flytekit.models.types.LiteralType,
) -> flytekit.models.literals.Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `python_val` | `typing.Union[flytekit.types.file.file.FlyteFile, flytekit.types.schema.types.FlyteSchema, str]` |
| `python_type` | `typing.Type[flytekitplugins.great_expectations.schema.GreatExpectationsType]` |
| `expected` | `flytekit.models.types.LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[flytekitplugins.great_expectations.schema.GreatExpectationsType],
) -> flytekitplugins.great_expectations.schema.GreatExpectationsType
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `lv` | `flytekit.models.literals.Literal` |
| `expected_python_type` | `typing.Type[flytekitplugins.great_expectations.schema.GreatExpectationsType]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

