---
title: FlyteFilePathTransformer
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteFilePathTransformer

**Package:** `flytekit.types.file.file`

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
def FlyteFilePathTransformer()
```
## Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`dict_to_flyte_file()`](#dict_to_flyte_file) |  |
| [`from_binary_idl()`](#from_binary_idl) | If the input is from flytekit, the Life Cycle will be as follows:. |
| [`from_generic_idl()`](#from_generic_idl) | If the input is from Flyte Console, the Life Cycle will be as follows:. |
| [`get_additional_headers()`](#get_additional_headers) |  |
| [`get_format()`](#get_format) |  |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`get_mime_type_from_extension()`](#get_mime_type_from_extension) |  |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |
| [`validate_file_type()`](#validate_file_type) | This method validates the type of the file at source_path against the expected python_type. |


### assert_type()

```python
def assert_type(
    t: typing.Union[typing.Type[FlyteFile], os.PathLike],
    v: typing.Union[FlyteFile, os.PathLike, str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` | |
| `v` | `typing.Union[FlyteFile, os.PathLike, str]` | |

### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: typing.Union[FlyteFile, os.PathLike, str],
    python_type: typing.Type[FlyteFile],
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
| `python_val` | `typing.Union[FlyteFile, os.PathLike, str]` | The actual value to be transformed |
| `python_type` | `typing.Type[FlyteFile]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `LiteralType` | Expected Literal Type |

### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: typing.Union[typing.Type[FlyteFile], os.PathLike],
) -> FlyteFile
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | FlyteContext |
| `lv` | `Literal` | The received literal Value |
| `expected_python_type` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` | Expected native python type that should be returned |

### dict_to_flyte_file()

```python
def dict_to_flyte_file(
    dict_obj: typing.Dict[str, str],
    expected_python_type: typing.Union[typing.Type[FlyteFile], os.PathLike],
) -> FlyteFile
```
| Parameter | Type | Description |
|-|-|-|
| `dict_obj` | `typing.Dict[str, str]` | |
| `expected_python_type` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` | |

### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: typing.Union[typing.Type[FlyteFile], os.PathLike],
) -> FlyteFile
```
If the input is from flytekit, the Life Cycle will be as follows:

Life Cycle:
binary IDL                 -> resolved binary         -> bytes                   -> expected Python object
(flytekit customized          (propeller processing)     (flytekit binary IDL)      (flytekit customized
serialization)                                                                       deserialization)

Example Code:
    @dataclass
    class DC:
        ff: FlyteFile

    @workflow
    def wf(dc: DC):
        t_ff(dc.ff)

Note:
- The deserialization is the same as put a flyte file in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type | Description |
|-|-|-|
| `binary_idl_object` | `Binary` | |
| `expected_python_type` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` | |

### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: typing.Union[typing.Type[FlyteFile], os.PathLike],
) -> FlyteFile
```
If the input is from Flyte Console, the Life Cycle will be as follows:

Life Cycle:
json str            -> protobuf struct         -> resolved protobuf struct   -> expected Python object
(console user input)   (console output)           (propeller)                   (flytekit customized deserialization)

Example Code:
@dataclass
class DC:
    ff: FlyteFile

@workflow
def wf(dc: DC):
    t_ff(dc.ff)

Note:
- The deserialization is the same as put a flyte file in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type | Description |
|-|-|-|
| `generic` | `Struct` | |
| `expected_python_type` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` | |

### get_additional_headers()

```python
def get_additional_headers(
    source_path: str | os.PathLike,
) -> typing.Dict[str, str]
```
| Parameter | Type | Description |
|-|-|-|
| `source_path` | `str \| os.PathLike` | |

### get_format()

```python
def get_format(
    t: typing.Union[typing.Type[FlyteFile], os.PathLike],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` | |

### get_literal_type()

```python
def get_literal_type(
    t: typing.Union[typing.Type[FlyteFile], os.PathLike],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` | |

### get_mime_type_from_extension()

```python
def get_mime_type_from_extension(
    extension: str,
) -> typing.Union[str, typing.Sequence[str]]
```
| Parameter | Type | Description |
|-|-|-|
| `extension` | `str` | |

### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> typing.Type[FlyteFile[typing.Any]]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type | Description |
|-|-|-|
| `literal_type` | `LiteralType` | |

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
    python_val: typing.Any,
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
| `python_val` | `typing.Any` | The actual value to be transformed |
| `python_type` | `Type[T]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `LiteralType` | Expected Literal Type |

### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | FlyteContext |
| `lv` | `Literal` | The received literal Value |
| `expected_python_type` | `Type[T]` | Expected native python type that should be returned |

### validate_file_type()

```python
def validate_file_type(
    python_type: typing.Type[FlyteFile],
    source_path: typing.Union[str, os.PathLike],
)
```
This method validates the type of the file at source_path against the expected python_type.
It uses the magic library to determine the real type of the file. If the magic library is not installed,
it logs a debug message and returns. If the actual file does not exist, it returns without raising an error.



| Parameter | Type | Description |
|-|-|-|
| `python_type` | `typing.Type[FlyteFile]` | The expected type of the file |
| `source_path` | `typing.Union[str, os.PathLike]` | The path to the file to validate :raises ValueError: If the real type of the file is not the same as the expected python_type |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

