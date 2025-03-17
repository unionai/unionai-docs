---
title: FlyteDirToMultipartBlobTransformer
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# FlyteDirToMultipartBlobTransformer

**Package:** `flytekit.types.directory`

This transformer handles conversion between the Python native FlyteDirectory class defined above, and the Flyte
IDL literal/type of Multipart Blob. Please see the FlyteDirectory comments for additional information.

.. caution:

The transformer will not check if the given path is actually a directory. This is because the path could be
a remote reference.


```python
def FlyteDirToMultipartBlobTransformer()
```
Initialize self.  See help(type(self)) for accurate signature.


No parameters
## Methods

### assert_type()

```python
def assert_type(
    t: typing.Type[FlyteDirectory],
    v: typing.Union[FlyteDirectory, os.PathLike, str],
):
```
| Parameter | Type |
|-|-|
| `t` | `typing.Type[FlyteDirectory]` |
| `v` | `typing.Union[FlyteDirectory, os.PathLike, str]` |
### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: FlyteDirectory,
    python_type: typing.Type[FlyteDirectory],
    expected: LiteralType,
):
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `FlyteDirectory` |
| `python_type` | `typing.Type[FlyteDirectory]` |
| `expected` | `LiteralType` |
### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: typing.Type[FlyteDirectory],
):
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `typing.Type[FlyteDirectory]` |
### dict_to_flyte_directory()

```python
def dict_to_flyte_directory(
    dict_obj: typing.Dict[str, str],
    expected_python_type: typing.Type[FlyteDirectory],
):
```
| Parameter | Type |
|-|-|
| `dict_obj` | `typing.Dict[str, str]` |
| `expected_python_type` | `typing.Type[FlyteDirectory]` |
### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: typing.Type[FlyteDirectory],
):
```
If the input is from flytekit, the Life Cycle will be as follows:

Life Cycle:
binary IDL                 -> resolved binary         -> bytes                   -> expected Python object
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


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `typing.Type[FlyteDirectory]` |
### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: typing.Type[FlyteDirectory],
):
```
If the input is from Flyte Console, the Life Cycle will be as follows:

Life Cycle:
json str            -> protobuf struct         -> resolved protobuf struct   -> expected Python object
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


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `typing.Type[FlyteDirectory]` |
### get_format()

```python
def get_format(
    t: typing.Type[FlyteDirectory],
):
```
| Parameter | Type |
|-|-|
| `t` | `typing.Type[FlyteDirectory]` |
### get_literal_type()

```python
def get_literal_type(
    t: typing.Type[FlyteDirectory],
):
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.Type[FlyteDirectory]` |
### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
):
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |
### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
):
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |
### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
):
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `expected_python_type` | `Type[T]` |
### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
):
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |
### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
):
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |
