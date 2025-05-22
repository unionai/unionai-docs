---
title: flytekitplugins.omegaconf.dictconfig_transformer
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.omegaconf.dictconfig_transformer

## Directory

### Classes

| Class | Description |
|-|-|
| [`DictConfigTransformer`](.././flytekitplugins.omegaconf.dictconfig_transformer#flytekitpluginsomegaconfdictconfig_transformerdictconfigtransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |

### Methods

| Method | Description |
|-|-|
| [`check_if_valid_dictconfig()`](#check_if_valid_dictconfig) | Validate the DictConfig to ensure it's serializable. |
| [`create_struct()`](#create_struct) | Create a protobuf Struct object from type and value maps. |
| [`extract_type_and_value_maps()`](#extract_type_and_value_maps) | Extract type and value maps from the DictConfig. |
| [`handle_base_dataclass()`](#handle_base_dataclass) | Handle the base dataclass and create the DictConfig. |
| [`is_flattenable()`](#is_flattenable) | Check if a DictConfig can be properly flattened and unflattened, i. |
| [`parse_node_value()`](#parse_node_value) | Parse the node value from the nested dictionary. |
| [`parse_type_description()`](#parse_type_description) | Parse the type description and return the corresponding type. |


### Variables

| Property | Type | Description |
|-|-|-|
| `T` | `TypeVar` |  |

## Methods

#### check_if_valid_dictconfig()

```python
def check_if_valid_dictconfig(
    python_val: omegaconf.dictconfig.DictConfig,
)
```
Validate the DictConfig to ensure it's serializable.


| Parameter | Type |
|-|-|
| `python_val` | `omegaconf.dictconfig.DictConfig` |

#### create_struct()

```python
def create_struct(
    type_map: typing.Dict[str, str],
    value_map: typing.Dict[str, typing.Any],
    base_config: typing.Type,
) -> google.protobuf.struct_pb2.Struct
```
Create a protobuf Struct object from type and value maps.


| Parameter | Type |
|-|-|
| `type_map` | `typing.Dict[str, str]` |
| `value_map` | `typing.Dict[str, typing.Any]` |
| `base_config` | `typing.Type` |

#### extract_type_and_value_maps()

```python
def extract_type_and_value_maps(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: omegaconf.dictconfig.DictConfig,
) -> (typing.Dict[str, str], typing.Dict[str, typing.Any])
```
Extract type and value maps from the DictConfig.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `python_val` | `omegaconf.dictconfig.DictConfig` |

#### handle_base_dataclass()

```python
def handle_base_dataclass(
    ctx: flytekit.core.context_manager.FlyteContext,
    nested_dict: typing.Dict[str, typing.Any],
    cfg_dict: typing.Dict[str, typing.Any],
) -> omegaconf.dictconfig.DictConfig
```
Handle the base dataclass and create the DictConfig.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `nested_dict` | `typing.Dict[str, typing.Any]` |
| `cfg_dict` | `typing.Dict[str, typing.Any]` |

#### is_flattenable()

```python
def is_flattenable(
    d: omegaconf.dictconfig.DictConfig,
) -> bool
```
Check if a DictConfig can be properly flattened and unflattened, i.e. keys do not contain dots.


| Parameter | Type |
|-|-|
| `d` | `omegaconf.dictconfig.DictConfig` |

#### parse_node_value()

```python
def parse_node_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    key: str,
    type_desc: str,
    nested_dict: typing.Dict[str, typing.Any],
) -> typing.Any
```
Parse the node value from the nested dictionary.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `key` | `str` |
| `type_desc` | `str` |
| `nested_dict` | `typing.Dict[str, typing.Any]` |

#### parse_type_description()

```python
def parse_type_description(
    type_desc: str,
) -> typing.Type
```
Parse the type description and return the corresponding type.


| Parameter | Type |
|-|-|
| `type_desc` | `str` |

## flytekitplugins.omegaconf.dictconfig_transformer.DictConfigTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
def DictConfigTransformer()
```
Construct DictConfigTransformer.


### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Provide type hint for Flytekit type system. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Convert from given python type object ``DictConfig`` to the Literal representation. |
| [`to_python_value()`](#to_python_value) | Re-hydrate the custom object from Flyte Literal value. |


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

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Type[omegaconf.dictconfig.DictConfig],
) -> flytekit.models.types.LiteralType
```
Provide type hint for Flytekit type system.

To support the multivariate typing of nodes in a DictConfig, we encode them as binaries (no introspection)
with multiple files.


| Parameter | Type |
|-|-|
| `t` | `typing.Type[omegaconf.dictconfig.DictConfig]` |

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
    python_val: ~T,
    python_type: typing.Type[~T],
    expected: flytekit.models.types.LiteralType,
) -> flytekit.models.literals.Literal
```
Convert from given python type object ``DictConfig`` to the Literal representation.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `python_val` | `~T` |
| `python_type` | `typing.Type[~T]` |
| `expected` | `flytekit.models.types.LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[omegaconf.dictconfig.DictConfig],
) -> omegaconf.dictconfig.DictConfig
```
Re-hydrate the custom object from Flyte Literal value.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `lv` | `flytekit.models.literals.Literal` |
| `expected_python_type` | `typing.Type[omegaconf.dictconfig.DictConfig]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

