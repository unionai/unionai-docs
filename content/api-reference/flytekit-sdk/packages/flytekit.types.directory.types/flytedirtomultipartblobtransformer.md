---
title: FlyteDirToMultipartBlobTransformer
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteDirToMultipartBlobTransformer

**Package:** `flytekit.types.directory.types`

This transformer handles conversion between the Python native FlyteDirectory class defined above, and the Flyte
IDL literal/type of Multipart Blob. Please see the FlyteDirectory comments for additional information.

&gt; [!CAUTION] caution:
&gt; The transformer will not check if the given path is actually a directory. This is because the path could be
   a remote reference.




```python
def FlyteDirToMultipartBlobTransformer()
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
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`dict_to_flyte_directory()`](#dict_to_flyte_directory) |  |
| [`from_binary_idl()`](#from_binary_idl) | If the input is from flytekit, the Life Cycle will be as follows:. |
| [`from_generic_idl()`](#from_generic_idl) | If the input is from Flyte Console, the Life Cycle will be as follows:. |
| [`get_format()`](#get_format) |  |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


### assert_type()

```python
def assert_type(
    t: typing.Type[FlyteDirectory],
    v: typing.Union[FlyteDirectory, os.PathLike, str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Type[FlyteDirectory]` | |
| `v` | `typing.Union[FlyteDirectory, os.PathLike, str]` | |

### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: FlyteDirectory,
    python_type: typing.Type[FlyteDirectory],
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
| `python_val` | `FlyteDirectory` | The actual value to be transformed |
| `python_type` | `typing.Type[FlyteDirectory]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `LiteralType` | Expected Literal Type |

### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: typing.Type[FlyteDirectory],
) -> FlyteDirectory
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | FlyteContext |
| `lv` | `Literal` | The received literal Value |
| `expected_python_type` | `typing.Type[FlyteDirectory]` | Expected native python type that should be returned |

### dict_to_flyte_directory()

```python
def dict_to_flyte_directory(
    dict_obj: typing.Dict[str, str],
    expected_python_type: typing.Type[FlyteDirectory],
) -> FlyteDirectory
```
| Parameter | Type | Description |
|-|-|-|
| `dict_obj` | `typing.Dict[str, str]` | |
| `expected_python_type` | `typing.Type[FlyteDirectory]` | |

### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: typing.Type[FlyteDirectory],
) -> FlyteDirectory
```
If the input is from flytekit, the Life Cycle will be as follows:

Life Cycle:
binary IDL                 -&gt; resolved binary         -&gt; bytes                   -&gt; expected Python object
(flytekit customized          (propeller processing)     (flytekit binary IDL)      (flytekit customized
serialization)                                                                       deserialization)

Example Code:
@dataclass
class DC:
    fd: FlyteDirectory

@workflow
def wf(dc: DC):
    t_fd(dc.fd)

Note:
- The deserialization is the same as put a flyte directory in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type | Description |
|-|-|-|
| `binary_idl_object` | `Binary` | |
| `expected_python_type` | `typing.Type[FlyteDirectory]` | |

### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: typing.Type[FlyteDirectory],
) -> FlyteDirectory
```
If the input is from Flyte Console, the Life Cycle will be as follows:

Life Cycle:
json str            -&gt; protobuf struct         -&gt; resolved protobuf struct   -&gt; expected Python object
(console user input)   (console output)           (propeller)                   (flytekit customized deserialization)

Example Code:
@dataclass
class DC:
    fd: FlyteDirectory

@workflow
def wf(dc: DC):
    t_fd(dc.fd)

Note:
- The deserialization is the same as put a flyte directory in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type | Description |
|-|-|-|
| `generic` | `Struct` | |
| `expected_python_type` | `typing.Type[FlyteDirectory]` | |

### get_format()

```python
def get_format(
    t: typing.Type[FlyteDirectory],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Type[FlyteDirectory]` | |

### get_literal_type()

```python
def get_literal_type(
    t: typing.Type[FlyteDirectory],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Type[FlyteDirectory]` | |

### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> typing.Type[FlyteDirectory[typing.Any]]
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

