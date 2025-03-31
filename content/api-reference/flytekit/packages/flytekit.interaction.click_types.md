---
title: flytekit.interaction.click_types
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.interaction.click_types

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArtifactQuery`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesartifactquery) |  |
| [`BlobType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesblobtype) | This type represents offloaded data and is typically used for things like files. |
| [`DataClassJsonMixin`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesdataclassjsonmixin) | DataClassJsonMixin is an ABC that functions as a Mixin. |
| [`DateTimeType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesdatetimetype) | The DateTime type converts date strings into `datetime` objects. |
| [`DirParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesdirparamtype) | Represents the type of a parameter. |
| [`DurationParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesdurationparamtype) | Represents the type of a parameter. |
| [`EnumParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesenumparamtype) | The choice type allows a value to be checked against a fixed set. |
| [`FileAccessProvider`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesfileaccessprovider) | This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`FileParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesfileparamtype) | Represents the type of a parameter. |
| [`FlyteContext`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteDirectory`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesflytedirectory) |  |
| [`FlyteFile`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesflytefile) |  |
| [`FlyteLiteralConverter`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesflyteliteralconverter) |  |
| [`FlytePathResolver`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesflytepathresolver) |  |
| [`FlytePickleTransformer`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesflytepickletransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`FlyteSchema`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesflyteschema) |  |
| [`JSONIteratorParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesjsoniteratorparamtype) | Represents the type of a parameter. |
| [`JSONIteratorTransformer`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesjsoniteratortransformer) | A JSON iterator that handles conversion between an iterator/generator and a JSONL file. |
| [`JsonParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesjsonparamtype) | Represents the type of a parameter. |
| [`Literal`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesliteral) |  |
| [`LiteralType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesliteraltype) |  |
| [`PickleParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typespickleparamtype) | Represents the type of a parameter. |
| [`SimpleType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typessimpletype) |  |
| [`StructuredDataset`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesstructureddataset) | This is the user facing StructuredDataset class. |
| [`StructuredDatasetParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesstructureddatasetparamtype) | TODO handle column types. |
| [`TypeEngine`](.././flytekit.interaction.click_types#flytekitinteractionclick_typestypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`UnionParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesunionparamtype) | A composite type that allows for multiple types to be specified. |

### Methods

| Method | Description |
|-|-|
| [`cast()`](#cast) | Cast a value to a type. |
| [`dataclass_json()`](#dataclass_json) | Based on the code in the `dataclasses` module to handle optional-parens. |
| [`get_args()`](#get_args) | Get type arguments with all substitutions performed. |
| [`is_pydantic_basemodel()`](#is_pydantic_basemodel) | Checks if the python type is a pydantic BaseModel. |
| [`key_value_callback()`](#key_value_callback) | Callback for click to parse key-value pairs. |
| [`labels_callback()`](#labels_callback) | Callback for click to parse labels. |
| [`literal_type_to_click_type()`](#literal_type_to_click_type) | Converts a Flyte LiteralType given a python_type to a click. |
| [`modify_literal_uris()`](#modify_literal_uris) | Modifies the literal object recursively to replace the URIs with the native paths. |
| [`parse()`](#parse) | Parse a time expression, returning it as a number of seconds. |


### Variables

| Property | Type | Description |
|-|-|-|
| `SIMPLE_TYPE_CONVERTER` | `dict` |  |

## Methods

#### cast()

```python
def cast(
    typ,
    val,
)
```
Cast a value to a type.

This returns the value unchanged.  To the type checker this
signals that the return value has the designated type, but at
runtime we intentionally don't check anything (we want this
to be as fast as possible).


| Parameter | Type |
|-|-|
| `typ` |  |
| `val` |  |

#### dataclass_json()

```python
def dataclass_json(
    _cls,
    letter_case,
    undefined: typing.Union[str, dataclasses_json.undefined.Undefined, NoneType],
)
```
Based on the code in the `dataclasses` module to handle optional-parens
decorators. See example below:

@dataclass_json
@dataclass_json(letter_case=LetterCase.CAMEL)
class Example:
...


| Parameter | Type |
|-|-|
| `_cls` |  |
| `letter_case` |  |
| `undefined` | `typing.Union[str, dataclasses_json.undefined.Undefined, NoneType]` |

#### get_args()

```python
def get_args(
    tp,
)
```
Get type arguments with all substitutions performed.

For unions, basic simplifications used by Union constructor are performed.

Examples::

>>> T = TypeVar('T')
>>> assert get_args(Dict[str, int]) == (str, int)
>>> assert get_args(int) == ()
>>> assert get_args(Union[int, Union[T, int], str][int]) == (int, str)
>>> assert get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
>>> assert get_args(Callable[[], T][int]) == ([], int)


| Parameter | Type |
|-|-|
| `tp` |  |

#### is_pydantic_basemodel()

```python
def is_pydantic_basemodel(
    python_type: typing.Type,
) -> bool
```
Checks if the python type is a pydantic BaseModel


| Parameter | Type |
|-|-|
| `python_type` | `typing.Type` |

#### key_value_callback()

```python
def key_value_callback(
    _: typing.Any,
    param: str,
    values: typing.List[str],
) -> typing.Optional[typing.Dict[str, str]]
```
Callback for click to parse key-value pairs.


| Parameter | Type |
|-|-|
| `_` | `typing.Any` |
| `param` | `str` |
| `values` | `typing.List[str]` |

#### labels_callback()

```python
def labels_callback(
    _: typing.Any,
    param: str,
    values: typing.List[str],
) -> typing.Optional[typing.Dict[str, str]]
```
Callback for click to parse labels.


| Parameter | Type |
|-|-|
| `_` | `typing.Any` |
| `param` | `str` |
| `values` | `typing.List[str]` |

#### literal_type_to_click_type()

```python
def literal_type_to_click_type(
    lt: flytekit.models.types.LiteralType,
    python_type: typing.Type,
) -> click.types.ParamType
```
Converts a Flyte LiteralType given a python_type to a click.ParamType


| Parameter | Type |
|-|-|
| `lt` | `flytekit.models.types.LiteralType` |
| `python_type` | `typing.Type` |

#### modify_literal_uris()

```python
def modify_literal_uris(
    lit: flytekit.models.literals.Literal,
)
```
Modifies the literal object recursively to replace the URIs with the native paths.


| Parameter | Type |
|-|-|
| `lit` | `flytekit.models.literals.Literal` |

#### parse()

```python
def parse(
    sval,
    granularity,
)
```
Parse a time expression, returning it as a number of seconds.  If
possible, the return value will be an `int`; if this is not
possible, the return will be a `float`.  Returns `None` if a time
expression cannot be parsed from the given string.

Arguments:
- `sval`: the string value to parse

>>> timeparse('1:24')
84
>>> timeparse(':22')
22
>>> timeparse('1 minute, 24 secs')
84
>>> timeparse('1m24s')
84
>>> timeparse('1.2 minutes')
72
>>> timeparse('1.2 seconds')
1.2

Time expressions can be signed.

>>> timeparse('- 1 minute')
-60
>>> timeparse('+ 1 minute')
60

If granularity is specified as ``minutes``, then ambiguous digits following
a colon will be interpreted as minutes; otherwise they are considered seconds.

>>> timeparse('1:30')
90
>>> timeparse('1:30', granularity='minutes')
5400


| Parameter | Type |
|-|-|
| `sval` |  |
| `granularity` |  |

## flytekit.interaction.click_types.ArtifactQuery

```python
class ArtifactQuery(
    artifact: Artifact,
    name: str,
    project: Optional[str],
    domain: Optional[str],
    time_partition: Optional[TimePartition],
    partitions: Optional[Partitions],
    tag: Optional[str],
)
```
| Parameter | Type |
|-|-|
| `artifact` | `Artifact` |
| `name` | `str` |
| `project` | `Optional[str]` |
| `domain` | `Optional[str]` |
| `time_partition` | `Optional[TimePartition]` |
| `partitions` | `Optional[Partitions]` |
| `tag` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`get_partition_str()`](#get_partition_str) |  |
| [`get_str()`](#get_str) |  |
| [`get_time_partition_str()`](#get_time_partition_str) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### get_partition_str()

```python
def get_partition_str(
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_str()

```python
def get_str(
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_time_partition_str()

```python
def get_time_partition_str(
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### to_flyte_idl()

```python
def to_flyte_idl(
    kwargs,
) -> art_id.ArtifactQuery
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `bound` |  |  |

## flytekit.interaction.click_types.BlobType

This type represents offloaded data and is typically used for things like files.


```python
class BlobType(
    format,
    dimensionality,
)
```
| Parameter | Type |
|-|-|
| `format` |  |
| `dimensionality` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> BlobType
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `dimensionality` |  | {{< multiline >}}An integer from BlobType.BlobDimensionality enum
{{< /multiline >}} |
| `format` |  | {{< multiline >}}A string describing the format of the underlying blob data.
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.interaction.click_types.DataClassJsonMixin

DataClassJsonMixin is an ABC that functions as a Mixin.

As with other ABCs, it should not be instantiated directly.


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

## flytekit.interaction.click_types.DateTimeType

The DateTime type converts date strings into `datetime` objects.

The format strings which are checked are configurable, but default to some
common (non-timezone aware) ISO 8601 formats.

When specifying *DateTime* formats, you should only pass a list or a tuple.
Other iterables, like generators, may lead to surprising results.

The format strings are processed using ``datetime.strptime``, and this
consequently defines the format strings which are allowed.

Parsing is tried using each format, in order, and the first format which
parses successfully is used.



```python
def DateTimeType()
```
### Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Convert the value to the correct type. |
| [`fail()`](#fail) | Helper method to fail with an invalid value message. |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one. |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing. |
| [`shell_complete()`](#shell_complete) | Return a list of. |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


#### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
) -> typing.Any
```
Convert the value to the correct type. This is not called if
the value is ``None`` (the missing value).

This must accept string values from the command line, as well as
values that are already the correct type. It may also convert
other compatible types.

The ``param`` and ``ctx`` arguments may be ``None`` in certain
situations, such as when converting prompt input.

If the value cannot be converted, call :meth:`fail` with a
descriptive message.



| Parameter | Type |
|-|-|
| `value` | `typing.Any` |
| `param` | `typing.Optional[click.core.Parameter]` |
| `ctx` | `typing.Optional[click.core.Context]` |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type |
|-|-|
| `message` | `str` |
| `param` | `typing.Optional[ForwardRef('Parameter')]` |
| `ctx` | `typing.Optional[ForwardRef('Context')]` |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> str
```
Returns the metavar default for this param if it provides one.


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Return a list of
:class:`~click.shell_completion.CompletionItem` objects for the
incomplete value. Most types do not provide completions, but
some do, and this allows custom types to provide custom
completions as well.



| Parameter | Type |
|-|-|
| `ctx` | `Context` |
| `param` | `Parameter` |
| `incomplete` | `str` |

#### split_envvar_value()

```python
def split_envvar_value(
    rv: str,
) -> typing.Sequence[str]
```
Given a value from an environment variable this splits it up
into small chunks depending on the defined envvar list splitter.

If the splitter is set to `None`, which means that whitespace splits,
then leading and trailing whitespace is ignored.  Otherwise, leading
and trailing splitters usually lead to empty items being included.


| Parameter | Type |
|-|-|
| `rv` | `str` |

#### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

.. versionadded:: 8.0


## flytekit.interaction.click_types.DirParamType

Represents the type of a parameter. Validates and converts values
from the command line or Python into the correct type.

To implement a custom type, subclass and implement at least the
following:

-   The :attr:`name` class attribute must be set.
-   Calling an instance of the type with ``None`` must return
``None``. This is already implemented by default.
-   :meth:`convert` must convert string values to the correct type.
-   :meth:`convert` must accept values that are already the correct
type.
-   It must be able to convert a value if the ``ctx`` and ``param``
arguments are ``None``. This can occur when converting prompt
input.


### Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Convert the value to the correct type. |
| [`fail()`](#fail) | Helper method to fail with an invalid value message. |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one. |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing. |
| [`shell_complete()`](#shell_complete) | Return a list of. |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


#### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
) -> typing.Any
```
Convert the value to the correct type. This is not called if
the value is ``None`` (the missing value).

This must accept string values from the command line, as well as
values that are already the correct type. It may also convert
other compatible types.

The ``param`` and ``ctx`` arguments may be ``None`` in certain
situations, such as when converting prompt input.

If the value cannot be converted, call :meth:`fail` with a
descriptive message.



| Parameter | Type |
|-|-|
| `value` | `typing.Any` |
| `param` | `typing.Optional[click.core.Parameter]` |
| `ctx` | `typing.Optional[click.core.Context]` |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type |
|-|-|
| `message` | `str` |
| `param` | `typing.Optional[ForwardRef('Parameter')]` |
| `ctx` | `typing.Optional[ForwardRef('Context')]` |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Return a list of
:class:`~click.shell_completion.CompletionItem` objects for the
incomplete value. Most types do not provide completions, but
some do, and this allows custom types to provide custom
completions as well.



| Parameter | Type |
|-|-|
| `ctx` | `Context` |
| `param` | `Parameter` |
| `incomplete` | `str` |

#### split_envvar_value()

```python
def split_envvar_value(
    rv: str,
) -> typing.Sequence[str]
```
Given a value from an environment variable this splits it up
into small chunks depending on the defined envvar list splitter.

If the splitter is set to `None`, which means that whitespace splits,
then leading and trailing whitespace is ignored.  Otherwise, leading
and trailing splitters usually lead to empty items being included.


| Parameter | Type |
|-|-|
| `rv` | `str` |

#### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

.. versionadded:: 8.0


## flytekit.interaction.click_types.DurationParamType

Represents the type of a parameter. Validates and converts values
from the command line or Python into the correct type.

To implement a custom type, subclass and implement at least the
following:

-   The :attr:`name` class attribute must be set.
-   Calling an instance of the type with ``None`` must return
``None``. This is already implemented by default.
-   :meth:`convert` must convert string values to the correct type.
-   :meth:`convert` must accept values that are already the correct
type.
-   It must be able to convert a value if the ``ctx`` and ``param``
arguments are ``None``. This can occur when converting prompt
input.


### Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Convert the value to the correct type. |
| [`fail()`](#fail) | Helper method to fail with an invalid value message. |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one. |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing. |
| [`shell_complete()`](#shell_complete) | Return a list of. |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


#### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
) -> typing.Any
```
Convert the value to the correct type. This is not called if
the value is ``None`` (the missing value).

This must accept string values from the command line, as well as
values that are already the correct type. It may also convert
other compatible types.

The ``param`` and ``ctx`` arguments may be ``None`` in certain
situations, such as when converting prompt input.

If the value cannot be converted, call :meth:`fail` with a
descriptive message.



| Parameter | Type |
|-|-|
| `value` | `typing.Any` |
| `param` | `typing.Optional[click.core.Parameter]` |
| `ctx` | `typing.Optional[click.core.Context]` |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type |
|-|-|
| `message` | `str` |
| `param` | `typing.Optional[ForwardRef('Parameter')]` |
| `ctx` | `typing.Optional[ForwardRef('Context')]` |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Return a list of
:class:`~click.shell_completion.CompletionItem` objects for the
incomplete value. Most types do not provide completions, but
some do, and this allows custom types to provide custom
completions as well.



| Parameter | Type |
|-|-|
| `ctx` | `Context` |
| `param` | `Parameter` |
| `incomplete` | `str` |

#### split_envvar_value()

```python
def split_envvar_value(
    rv: str,
) -> typing.Sequence[str]
```
Given a value from an environment variable this splits it up
into small chunks depending on the defined envvar list splitter.

If the splitter is set to `None`, which means that whitespace splits,
then leading and trailing whitespace is ignored.  Otherwise, leading
and trailing splitters usually lead to empty items being included.


| Parameter | Type |
|-|-|
| `rv` | `str` |

#### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

.. versionadded:: 8.0


## flytekit.interaction.click_types.EnumParamType

The choice type allows a value to be checked against a fixed set
of supported values. All of these values have to be strings.

You should only pass a list or tuple of choices. Other iterables
(like generators) may lead to surprising results.

The resulting value will always be one of the originally passed choices
regardless of ``case_sensitive`` or any ``ctx.token_normalize_func``
being specified.

See :ref:`choice-opts` for an example.



```python
class EnumParamType(
    enum_type: typing.Type[enum.Enum],
)
```
| Parameter | Type |
|-|-|
| `enum_type` | `typing.Type[enum.Enum]` |

### Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Convert the value to the correct type. |
| [`fail()`](#fail) | Helper method to fail with an invalid value message. |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one. |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing. |
| [`shell_complete()`](#shell_complete) | Complete choices that start with the incomplete value. |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


#### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
) -> <enum 'Enum'>
```
Convert the value to the correct type. This is not called if
the value is ``None`` (the missing value).

This must accept string values from the command line, as well as
values that are already the correct type. It may also convert
other compatible types.

The ``param`` and ``ctx`` arguments may be ``None`` in certain
situations, such as when converting prompt input.

If the value cannot be converted, call :meth:`fail` with a
descriptive message.



| Parameter | Type |
|-|-|
| `value` | `typing.Any` |
| `param` | `typing.Optional[click.core.Parameter]` |
| `ctx` | `typing.Optional[click.core.Context]` |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type |
|-|-|
| `message` | `str` |
| `param` | `typing.Optional[ForwardRef('Parameter')]` |
| `ctx` | `typing.Optional[ForwardRef('Context')]` |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> str
```
Returns the metavar default for this param if it provides one.


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> str
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Complete choices that start with the incomplete value.



| Parameter | Type |
|-|-|
| `ctx` | `Context` |
| `param` | `Parameter` |
| `incomplete` | `str` |

#### split_envvar_value()

```python
def split_envvar_value(
    rv: str,
) -> typing.Sequence[str]
```
Given a value from an environment variable this splits it up
into small chunks depending on the defined envvar list splitter.

If the splitter is set to `None`, which means that whitespace splits,
then leading and trailing whitespace is ignored.  Otherwise, leading
and trailing splitters usually lead to empty items being included.


| Parameter | Type |
|-|-|
| `rv` | `str` |

#### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

.. versionadded:: 8.0


## flytekit.interaction.click_types.FileAccessProvider

This is the class that is available through the FlyteContext and can be used for persisting data to the remote
durable store.


```python
class FileAccessProvider(
    local_sandbox_dir: typing.Union[str, os.PathLike],
    raw_output_prefix: str,
    data_config: typing.Optional[flytekit.configuration.DataConfig],
    execution_metadata: typing.Optional[dict],
)
```
| Parameter | Type |
|-|-|
| `local_sandbox_dir` | `typing.Union[str, os.PathLike]` |
| `raw_output_prefix` | `str` |
| `data_config` | `typing.Optional[flytekit.configuration.DataConfig]` |
| `execution_metadata` | `typing.Optional[dict]` |

### Methods

| Method | Description |
|-|-|
| [`async_get_data()`](#async_get_data) | . |
| [`async_put_data()`](#async_put_data) | The implication here is that we're always going to put data to the remote location, so we . |
| [`async_put_raw_data()`](#async_put_raw_data) | This is a more flexible version of put that accepts a file-like object or a string path. |
| [`download()`](#download) | Downloads from remote to local. |
| [`download_directory()`](#download_directory) | Downloads directory from given remote to local path. |
| [`exists()`](#exists) |  |
| [`generate_new_custom_path()`](#generate_new_custom_path) | Generates a new path with the raw output prefix and a random string appended to it. |
| [`get()`](#get) |  |
| [`get_async_filesystem_for_path()`](#get_async_filesystem_for_path) |  |
| [`get_data()`](#get_data) | . |
| [`get_file_tail()`](#get_file_tail) |  |
| [`get_filesystem()`](#get_filesystem) |  |
| [`get_filesystem_for_path()`](#get_filesystem_for_path) |  |
| [`get_random_local_directory()`](#get_random_local_directory) |  |
| [`get_random_local_path()`](#get_random_local_path) | Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name. |
| [`get_random_remote_directory()`](#get_random_remote_directory) |  |
| [`get_random_remote_path()`](#get_random_remote_path) |  |
| [`get_random_string()`](#get_random_string) |  |
| [`is_remote()`](#is_remote) | Deprecated. |
| [`join()`](#join) |  |
| [`put_data()`](#put_data) | The implication here is that we're always going to put data to the remote location, so we . |
| [`put_raw_data()`](#put_raw_data) | This is a more flexible version of put that accepts a file-like object or a string path. |
| [`recursive_paths()`](#recursive_paths) |  |
| [`sep()`](#sep) |  |
| [`strip_file_header()`](#strip_file_header) | Drops file:// if it exists from the file. |
| [`upload()`](#upload) | . |
| [`upload_directory()`](#upload_directory) | . |


#### async_get_data()

```python
def async_get_data(
    remote_path: str,
    local_path: str,
    is_multipart: bool,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `remote_path` | `str` |
| `local_path` | `str` |
| `is_multipart` | `bool` |
| `kwargs` | ``**kwargs`` |

#### async_put_data()

```python
def async_put_data(
    local_path: typing.Union[str, os.PathLike],
    remote_path: str,
    is_multipart: bool,
    kwargs,
) -> str
```
The implication here is that we're always going to put data to the remote location, so we .remote to ensure
we don't use the true local proxy if the remote path is a file://



| Parameter | Type |
|-|-|
| `local_path` | `typing.Union[str, os.PathLike]` |
| `remote_path` | `str` |
| `is_multipart` | `bool` |
| `kwargs` | ``**kwargs`` |

#### async_put_raw_data()

```python
def async_put_raw_data(
    lpath: typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO],
    upload_prefix: typing.Optional[str],
    file_name: typing.Optional[str],
    read_chunk_size_bytes: int,
    encoding: str,
    skip_raw_data_prefix: bool,
    kwargs,
) -> str
```
This is a more flexible version of put that accepts a file-like object or a string path.
Writes to the raw output prefix only. If you want to write to another fs use put_data or get the fsspec
file system directly.
FYI: Currently the raw output prefix set by propeller is already unique per retry and looks like
s3://my-s3-bucket/data/o4/feda4e266c748463a97d-n0-0

If lpath is a folder, then recursive will be set.
If lpath is a streamable, then it can only be a single file.

Writes to:
{raw output prefix}/{upload_prefix}/{file_name}



| Parameter | Type |
|-|-|
| `lpath` | `typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO]` |
| `upload_prefix` | `typing.Optional[str]` |
| `file_name` | `typing.Optional[str]` |
| `read_chunk_size_bytes` | `int` |
| `encoding` | `str` |
| `skip_raw_data_prefix` | `bool` |
| `kwargs` | ``**kwargs`` |

#### download()

```python
def download(
    remote_path: str,
    local_path: str,
    kwargs,
)
```
Downloads from remote to local


| Parameter | Type |
|-|-|
| `remote_path` | `str` |
| `local_path` | `str` |
| `kwargs` | ``**kwargs`` |

#### download_directory()

```python
def download_directory(
    remote_path: str,
    local_path: str,
    kwargs,
)
```
Downloads directory from given remote to local path


| Parameter | Type |
|-|-|
| `remote_path` | `str` |
| `local_path` | `str` |
| `kwargs` | ``**kwargs`` |

#### exists()

```python
def exists(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### generate_new_custom_path()

```python
def generate_new_custom_path(
    fs: typing.Optional[fsspec.spec.AbstractFileSystem],
    alt: typing.Optional[str],
    stem: typing.Optional[str],
) -> str
```
Generates a new path with the raw output prefix and a random string appended to it.
Optionally, you can provide an alternate prefix and a stem. If stem is provided, it
will be appended to the path instead of a random string. If alt is provided, it will
replace the first part of the output prefix, e.g. the S3 or GCS bucket.

If wanting to write to a non-random prefix in a non-default S3 bucket, this can be
called with alt="my-alt-bucket" and stem="my-stem" to generate a path like
s3://my-alt-bucket/default-prefix-part/my-stem



| Parameter | Type |
|-|-|
| `fs` | `typing.Optional[fsspec.spec.AbstractFileSystem]` |
| `alt` | `typing.Optional[str]` |
| `stem` | `typing.Optional[str]` |

#### get()

```python
def get(
    from_path: str,
    to_path: str,
    recursive: bool,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `to_path` | `str` |
| `recursive` | `bool` |
| `kwargs` | ``**kwargs`` |

#### get_async_filesystem_for_path()

```python
def get_async_filesystem_for_path(
    path: str,
    anonymous: bool,
    kwargs,
) -> typing.Union[fsspec.asyn.AsyncFileSystem, fsspec.spec.AbstractFileSystem]
```
| Parameter | Type |
|-|-|
| `path` | `str` |
| `anonymous` | `bool` |
| `kwargs` | ``**kwargs`` |

#### get_data()

```python
def get_data(
    remote_path: str,
    local_path: str,
    is_multipart: bool,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `remote_path` | `str` |
| `local_path` | `str` |
| `is_multipart` | `bool` |
| `kwargs` | ``**kwargs`` |

#### get_file_tail()

```python
def get_file_tail(
    file_path_or_file_name: str,
) -> str
```
| Parameter | Type |
|-|-|
| `file_path_or_file_name` | `str` |

#### get_filesystem()

```python
def get_filesystem(
    protocol: typing.Optional[str],
    anonymous: bool,
    path: typing.Optional[str],
    kwargs,
) -> fsspec.spec.AbstractFileSystem
```
| Parameter | Type |
|-|-|
| `protocol` | `typing.Optional[str]` |
| `anonymous` | `bool` |
| `path` | `typing.Optional[str]` |
| `kwargs` | ``**kwargs`` |

#### get_filesystem_for_path()

```python
def get_filesystem_for_path(
    path: str,
    anonymous: bool,
    kwargs,
) -> fsspec.spec.AbstractFileSystem
```
| Parameter | Type |
|-|-|
| `path` | `str` |
| `anonymous` | `bool` |
| `kwargs` | ``**kwargs`` |

#### get_random_local_directory()

```python
def get_random_local_directory()
```
#### get_random_local_path()

```python
def get_random_local_path(
    file_path_or_file_name: typing.Optional[str],
) -> str
```
Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name


| Parameter | Type |
|-|-|
| `file_path_or_file_name` | `typing.Optional[str]` |

#### get_random_remote_directory()

```python
def get_random_remote_directory()
```
#### get_random_remote_path()

```python
def get_random_remote_path(
    file_path_or_file_name: typing.Optional[str],
) -> str
```
| Parameter | Type |
|-|-|
| `file_path_or_file_name` | `typing.Optional[str]` |

#### get_random_string()

```python
def get_random_string()
```
#### is_remote()

```python
def is_remote(
    path: typing.Union[str, os.PathLike],
) -> bool
```
Deprecated. Let's find a replacement


| Parameter | Type |
|-|-|
| `path` | `typing.Union[str, os.PathLike]` |

#### join()

```python
def join(
    args: `*args`,
    unstrip: bool,
    fs: typing.Optional[fsspec.spec.AbstractFileSystem],
) -> str
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `unstrip` | `bool` |
| `fs` | `typing.Optional[fsspec.spec.AbstractFileSystem]` |

#### put_data()

```python
def put_data(
    local_path: typing.Union[str, os.PathLike],
    remote_path: str,
    is_multipart: bool,
    kwargs,
) -> str
```
The implication here is that we're always going to put data to the remote location, so we .remote to ensure
we don't use the true local proxy if the remote path is a file://



| Parameter | Type |
|-|-|
| `local_path` | `typing.Union[str, os.PathLike]` |
| `remote_path` | `str` |
| `is_multipart` | `bool` |
| `kwargs` | ``**kwargs`` |

#### put_raw_data()

```python
def put_raw_data(
    lpath: typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO],
    upload_prefix: typing.Optional[str],
    file_name: typing.Optional[str],
    read_chunk_size_bytes: int,
    encoding: str,
    skip_raw_data_prefix: bool,
    kwargs,
) -> str
```
This is a more flexible version of put that accepts a file-like object or a string path.
Writes to the raw output prefix only. If you want to write to another fs use put_data or get the fsspec
file system directly.
FYI: Currently the raw output prefix set by propeller is already unique per retry and looks like
s3://my-s3-bucket/data/o4/feda4e266c748463a97d-n0-0

If lpath is a folder, then recursive will be set.
If lpath is a streamable, then it can only be a single file.

Writes to:
{raw output prefix}/{upload_prefix}/{file_name}



| Parameter | Type |
|-|-|
| `lpath` | `typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO]` |
| `upload_prefix` | `typing.Optional[str]` |
| `file_name` | `typing.Optional[str]` |
| `read_chunk_size_bytes` | `int` |
| `encoding` | `str` |
| `skip_raw_data_prefix` | `bool` |
| `kwargs` | ``**kwargs`` |

#### recursive_paths()

```python
def recursive_paths(
    f: str,
    t: str,
) -> typing.Tuple[str, str]
```
| Parameter | Type |
|-|-|
| `f` | `str` |
| `t` | `str` |

#### sep()

```python
def sep(
    file_system: typing.Optional[fsspec.spec.AbstractFileSystem],
) -> str
```
| Parameter | Type |
|-|-|
| `file_system` | `typing.Optional[fsspec.spec.AbstractFileSystem]` |

#### strip_file_header()

```python
def strip_file_header(
    path: str,
    trim_trailing_sep: bool,
) -> str
```
Drops file:// if it exists from the file


| Parameter | Type |
|-|-|
| `path` | `str` |
| `trim_trailing_sep` | `bool` |

#### upload()

```python
def upload(
    file_path: str,
    to_path: str,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `file_path` | `str` |
| `to_path` | `str` |
| `kwargs` | ``**kwargs`` |

#### upload_directory()

```python
def upload_directory(
    local_path: str,
    remote_path: str,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `local_path` | `str` |
| `remote_path` | `str` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `data_config` |  |  |
| `local_access` |  |  |
| `local_sandbox_dir` |  | {{< multiline >}}This is a context based temp dir.
{{< /multiline >}} |
| `raw_output_fs` |  | {{< multiline >}}Returns a file system corresponding to the provided raw output prefix
{{< /multiline >}} |
| `raw_output_prefix` |  |  |

## flytekit.interaction.click_types.FileParamType

Represents the type of a parameter. Validates and converts values
from the command line or Python into the correct type.

To implement a custom type, subclass and implement at least the
following:

-   The :attr:`name` class attribute must be set.
-   Calling an instance of the type with ``None`` must return
``None``. This is already implemented by default.
-   :meth:`convert` must convert string values to the correct type.
-   :meth:`convert` must accept values that are already the correct
type.
-   It must be able to convert a value if the ``ctx`` and ``param``
arguments are ``None``. This can occur when converting prompt
input.


### Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Convert the value to the correct type. |
| [`fail()`](#fail) | Helper method to fail with an invalid value message. |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one. |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing. |
| [`shell_complete()`](#shell_complete) | Return a list of. |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


#### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
) -> typing.Any
```
Convert the value to the correct type. This is not called if
the value is ``None`` (the missing value).

This must accept string values from the command line, as well as
values that are already the correct type. It may also convert
other compatible types.

The ``param`` and ``ctx`` arguments may be ``None`` in certain
situations, such as when converting prompt input.

If the value cannot be converted, call :meth:`fail` with a
descriptive message.



| Parameter | Type |
|-|-|
| `value` | `typing.Any` |
| `param` | `typing.Optional[click.core.Parameter]` |
| `ctx` | `typing.Optional[click.core.Context]` |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type |
|-|-|
| `message` | `str` |
| `param` | `typing.Optional[ForwardRef('Parameter')]` |
| `ctx` | `typing.Optional[ForwardRef('Context')]` |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Return a list of
:class:`~click.shell_completion.CompletionItem` objects for the
incomplete value. Most types do not provide completions, but
some do, and this allows custom types to provide custom
completions as well.



| Parameter | Type |
|-|-|
| `ctx` | `Context` |
| `param` | `Parameter` |
| `incomplete` | `str` |

#### split_envvar_value()

```python
def split_envvar_value(
    rv: str,
) -> typing.Sequence[str]
```
Given a value from an environment variable this splits it up
into small chunks depending on the defined envvar list splitter.

If the splitter is set to `None`, which means that whitespace splits,
then leading and trailing whitespace is ignored.  Otherwise, leading
and trailing splitters usually lead to empty items being included.


| Parameter | Type |
|-|-|
| `rv` | `str` |

#### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

.. versionadded:: 8.0


## flytekit.interaction.click_types.FlyteContext

This is an internal-facing context object, that most users will not have to deal with. It's essentially a globally
available grab bag of settings and objects that allows flytekit to do things like convert complex types, run and
compile workflows, serialize Flyte entities, etc.

Even though this object as a ``current_context`` function on it, it should not be called directly. Please use the
:py:class:`flytekit.FlyteContextManager` object instead.

Please do not confuse this object with the :py:class:`flytekit.ExecutionParameters` object.


```python
class FlyteContext(
    file_access: FileAccessProvider,
    level: int,
    flyte_client: Optional['friendly_client.SynchronousFlyteClient'],
    compilation_state: Optional[CompilationState],
    execution_state: Optional[ExecutionState],
    serialization_settings: Optional[SerializationSettings],
    in_a_condition: bool,
    origin_stackframe: Optional[traceback.FrameSummary],
    output_metadata_tracker: Optional[OutputMetadataTracker],
    worker_queue: Optional[Controller],
)
```
| Parameter | Type |
|-|-|
| `file_access` | `FileAccessProvider` |
| `level` | `int` |
| `flyte_client` | `Optional['friendly_client.SynchronousFlyteClient']` |
| `compilation_state` | `Optional[CompilationState]` |
| `execution_state` | `Optional[ExecutionState]` |
| `serialization_settings` | `Optional[SerializationSettings]` |
| `in_a_condition` | `bool` |
| `origin_stackframe` | `Optional[traceback.FrameSummary]` |
| `output_metadata_tracker` | `Optional[OutputMetadataTracker]` |
| `worker_queue` | `Optional[Controller]` |

### Methods

| Method | Description |
|-|-|
| [`current_context()`](#current_context) | This method exists only to maintain backwards compatibility. |
| [`enter_conditional_section()`](#enter_conditional_section) |  |
| [`get_deck()`](#get_deck) | Returns the deck that was created as part of the last execution. |
| [`get_origin_stackframe_repr()`](#get_origin_stackframe_repr) |  |
| [`new_builder()`](#new_builder) |  |
| [`new_compilation_state()`](#new_compilation_state) | Creates and returns a default compilation state. |
| [`new_execution_state()`](#new_execution_state) | Creates and returns a new default execution state. |
| [`set_stackframe()`](#set_stackframe) |  |
| [`with_client()`](#with_client) |  |
| [`with_compilation_state()`](#with_compilation_state) |  |
| [`with_execution_state()`](#with_execution_state) |  |
| [`with_file_access()`](#with_file_access) |  |
| [`with_new_compilation_state()`](#with_new_compilation_state) |  |
| [`with_output_metadata_tracker()`](#with_output_metadata_tracker) |  |
| [`with_serialization_settings()`](#with_serialization_settings) |  |
| [`with_worker_queue()`](#with_worker_queue) |  |


#### current_context()

```python
def current_context()
```
This method exists only to maintain backwards compatibility. Please use
``FlyteContextManager.current_context()`` instead.

Users of flytekit should be wary not to confuse the object returned from this function
with :py:func:`flytekit.current_context`


#### enter_conditional_section()

```python
def enter_conditional_section()
```
#### get_deck()

```python
def get_deck()
```
Returns the deck that was created as part of the last execution.

The return value depends on the execution environment. In a notebook, the return value is compatible with
IPython.display and should be rendered in the notebook.

.. code-block:: python

with flytekit.new_context() as ctx:
my_task(...)
ctx.get_deck()

OR if you wish to explicitly display

.. code-block:: python

from IPython import display
display(ctx.get_deck())


#### get_origin_stackframe_repr()

```python
def get_origin_stackframe_repr()
```
#### new_builder()

```python
def new_builder()
```
#### new_compilation_state()

```python
def new_compilation_state(
    prefix: str,
) -> CompilationState
```
Creates and returns a default compilation state. For most of the code this should be the entrypoint
of compilation, otherwise the code should always uses - with_compilation_state


| Parameter | Type |
|-|-|
| `prefix` | `str` |

#### new_execution_state()

```python
def new_execution_state(
    working_dir: Optional[os.PathLike],
) -> ExecutionState
```
Creates and returns a new default execution state. This should be used at the entrypoint of execution,
in all other cases it is preferable to use with_execution_state


| Parameter | Type |
|-|-|
| `working_dir` | `Optional[os.PathLike]` |

#### set_stackframe()

```python
def set_stackframe(
    s: traceback.FrameSummary,
)
```
| Parameter | Type |
|-|-|
| `s` | `traceback.FrameSummary` |

#### with_client()

```python
def with_client(
    c: SynchronousFlyteClient,
) -> Builder
```
| Parameter | Type |
|-|-|
| `c` | `SynchronousFlyteClient` |

#### with_compilation_state()

```python
def with_compilation_state(
    c: CompilationState,
) -> Builder
```
| Parameter | Type |
|-|-|
| `c` | `CompilationState` |

#### with_execution_state()

```python
def with_execution_state(
    es: ExecutionState,
) -> Builder
```
| Parameter | Type |
|-|-|
| `es` | `ExecutionState` |

#### with_file_access()

```python
def with_file_access(
    fa: FileAccessProvider,
) -> Builder
```
| Parameter | Type |
|-|-|
| `fa` | `FileAccessProvider` |

#### with_new_compilation_state()

```python
def with_new_compilation_state()
```
#### with_output_metadata_tracker()

```python
def with_output_metadata_tracker(
    t: OutputMetadataTracker,
) -> Builder
```
| Parameter | Type |
|-|-|
| `t` | `OutputMetadataTracker` |

#### with_serialization_settings()

```python
def with_serialization_settings(
    ss: SerializationSettings,
) -> Builder
```
| Parameter | Type |
|-|-|
| `ss` | `SerializationSettings` |

#### with_worker_queue()

```python
def with_worker_queue(
    wq: Controller,
) -> Builder
```
| Parameter | Type |
|-|-|
| `wq` | `Controller` |

### Properties

| Property | Type | Description |
|-|-|-|
| `user_space_params` |  |  |

## flytekit.interaction.click_types.FlyteDirectory

```python
class FlyteDirectory(
    path: typing.Union[str, os.PathLike],
    downloader: typing.Optional[typing.Callable],
    remote_directory: typing.Optional[typing.Union[os.PathLike, str, typing.Literal[False]]],
)
```
| Parameter | Type |
|-|-|
| `path` | `typing.Union[str, os.PathLike]` |
| `downloader` | `typing.Optional[typing.Callable]` |
| `remote_directory` | `typing.Optional[typing.Union[os.PathLike, str, typing.Literal[False]]]` |

### Methods

| Method | Description |
|-|-|
| [`crawl()`](#crawl) | Crawl returns a generator of all files prefixed by any sub-folders under the given "FlyteDirectory". |
| [`deserialize_flyte_dir()`](#deserialize_flyte_dir) |  |
| [`download()`](#download) |  |
| [`extension()`](#extension) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_source()`](#from_source) | Create a new FlyteDirectory object with the remote source set to the input. |
| [`listdir()`](#listdir) | This function will list all files and folders in the given directory, but without downloading the contents. |
| [`new()`](#new) | Create a new FlyteDirectory object in current Flyte working directory. |
| [`new_dir()`](#new_dir) | This will create a new folder under the current folder. |
| [`new_file()`](#new_file) | This will create a new file under the current folder. |
| [`new_remote()`](#new_remote) | Create a new FlyteDirectory object using the currently configured default remote in the context (i. |
| [`schema()`](#schema) |  |
| [`serialize_flyte_dir()`](#serialize_flyte_dir) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### crawl()

```python
def crawl(
    maxdepth: typing.Optional[int],
    topdown: bool,
    kwargs,
) -> Generator[Tuple[typing.Union[str, os.PathLike[Any]], typing.Dict[Any, Any]], None, None]
```
Crawl returns a generator of all files prefixed by any sub-folders under the given "FlyteDirectory".
if details=True is passed, then it will return a dictionary as specified by fsspec.

Example:

>>> list(fd.crawl())
[("/base", "file1"), ("/base", "dir1/file1"), ("/base", "dir2/file1"), ("/base", "dir1/dir/file1")]

>>> list(x.crawl(detail=True))
[('/tmp/test', {'my-dir/ab.py': {'name': '/tmp/test/my-dir/ab.py', 'size': 0, 'type': 'file',
'created': 1677720780.2318847, 'islink': False, 'mode': 33188, 'uid': 501, 'gid': 0,
'mtime': 1677720780.2317934, 'ino': 1694329, 'nlink': 1}})]


| Parameter | Type |
|-|-|
| `maxdepth` | `typing.Optional[int]` |
| `topdown` | `bool` |
| `kwargs` | ``**kwargs`` |

#### deserialize_flyte_dir()

```python
def deserialize_flyte_dir(
    info,
) -> FlyteDirectory
```
| Parameter | Type |
|-|-|
| `info` |  |

#### download()

```python
def download()
```
#### extension()

```python
def extension()
```
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

#### from_source()

```python
def from_source(
    source: str | os.PathLike,
) -> FlyteDirectory
```
Create a new FlyteDirectory object with the remote source set to the input


| Parameter | Type |
|-|-|
| `source` | `str \| os.PathLike` |

#### listdir()

```python
def listdir(
    directory: FlyteDirectory,
) -> typing.List[typing.Union[FlyteDirectory, FlyteFile]]
```
This function will list all files and folders in the given directory, but without downloading the contents.
In addition, it will return a list of FlyteFile and FlyteDirectory objects that have ability to lazily download the
contents of the file/folder. For example:

.. code-block:: python

entity = FlyteDirectory.listdir(directory)
for e in entity:
print("s3 object:", e.remote_source)
# s3 object: s3://test-flytedir/file1.txt
# s3 object: s3://test-flytedir/file2.txt
# s3 object: s3://test-flytedir/sub_dir

open(entity[0], "r")  # This will download the file to the local disk.
open(entity[0], "r")  # flytekit will read data from the local disk if you open it again.


| Parameter | Type |
|-|-|
| `directory` | `FlyteDirectory` |

#### new()

```python
def new(
    dirname: str | os.PathLike,
) -> FlyteDirectory
```
Create a new FlyteDirectory object in current Flyte working directory.


| Parameter | Type |
|-|-|
| `dirname` | `str \| os.PathLike` |

#### new_dir()

```python
def new_dir(
    name: typing.Optional[str],
) -> FlyteDirectory
```
This will create a new folder under the current folder.
If given a name, it will use the name given, otherwise it'll pick a random string.
Collisions are not checked.


| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |

#### new_file()

```python
def new_file(
    name: typing.Optional[str],
) -> FlyteFile
```
This will create a new file under the current folder.
If given a name, it will use the name given, otherwise it'll pick a random string.
Collisions are not checked.


| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |

#### new_remote()

```python
def new_remote(
    stem: typing.Optional[str],
    alt: typing.Optional[str],
) -> FlyteDirectory
```
Create a new FlyteDirectory object using the currently configured default remote in the context (i.e.
the raw_output_prefix configured in the current FileAccessProvider object in the context).
This is used if you explicitly have a folder somewhere that you want to create files under.
If you want to write a whole folder, you can let your task return a FlyteDirectory object,
and let flytekit handle the uploading.



| Parameter | Type |
|-|-|
| `stem` | `typing.Optional[str]` |
| `alt` | `typing.Optional[str]` |

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

#### serialize_flyte_dir()

```python
def serialize_flyte_dir()
```
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

### Properties

| Property | Type | Description |
|-|-|-|
| `downloaded` |  |  |
| `remote_directory` |  |  |
| `remote_source` |  | {{< multiline >}}If this is an input to a task, and the original path is s3://something, flytekit will download the
directory for the user. In case the user wants access to the original path, it will be here.
{{< /multiline >}} |
| `sep` |  |  |

## flytekit.interaction.click_types.FlyteFile

```python
class FlyteFile(
    path: typing.Union[str, os.PathLike],
    downloader: typing.Callable,
    remote_path: typing.Optional[typing.Union[os.PathLike, str, bool]],
    metadata: typing.Optional[dict[str, str]],
)
```
FlyteFile's init method.



| Parameter | Type |
|-|-|
| `path` | `typing.Union[str, os.PathLike]` |
| `downloader` | `typing.Callable` |
| `remote_path` | `typing.Optional[typing.Union[os.PathLike, str, bool]]` |
| `metadata` | `typing.Optional[dict[str, str]]` |

### Methods

| Method | Description |
|-|-|
| [`deserialize_flyte_file()`](#deserialize_flyte_file) |  |
| [`download()`](#download) |  |
| [`extension()`](#extension) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_source()`](#from_source) | Create a new FlyteFile object with the remote source set to the input. |
| [`new()`](#new) | Create a new FlyteFile object in the current Flyte working directory. |
| [`new_remote_file()`](#new_remote_file) | Create a new FlyteFile object with a remote path. |
| [`open()`](#open) | Returns a streaming File handle. |
| [`serialize_flyte_file()`](#serialize_flyte_file) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### deserialize_flyte_file()

```python
def deserialize_flyte_file(
    info,
) -> 'FlyteFile'
```
| Parameter | Type |
|-|-|
| `info` |  |

#### download()

```python
def download()
```
#### extension()

```python
def extension()
```
#### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### from_source()

```python
def from_source(
    source: str | os.PathLike,
) -> FlyteFile
```
Create a new FlyteFile object with the remote source set to the input


| Parameter | Type |
|-|-|
| `source` | `str \| os.PathLike` |

#### new()

```python
def new(
    filename: str | os.PathLike,
) -> FlyteFile
```
Create a new FlyteFile object in the current Flyte working directory


| Parameter | Type |
|-|-|
| `filename` | `str \| os.PathLike` |

#### new_remote_file()

```python
def new_remote_file(
    name: typing.Optional[str],
    alt: typing.Optional[str],
) -> FlyteFile
```
Create a new FlyteFile object with a remote path.



| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |
| `alt` | `typing.Optional[str]` |

#### open()

```python
def open(
    mode: str,
    cache_type: typing.Optional[str],
    cache_options: typing.Optional[typing.Dict[str, typing.Any]],
)
```
Returns a streaming File handle

.. code-block:: python

@task
def copy_file(ff: FlyteFile) -> FlyteFile:
new_file = FlyteFile.new_remote_file()
with ff.open("rb", cache_type="readahead") as r:
with new_file.open("wb") as w:
w.write(r.read())
return new_file



| Parameter | Type |
|-|-|
| `mode` | `str` |
| `cache_type` | `typing.Optional[str]` |
| `cache_options` | `typing.Optional[typing.Dict[str, typing.Any]]` |

#### serialize_flyte_file()

```python
def serialize_flyte_file()
```
#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `downloaded` |  |  |
| `remote_path` |  |  |
| `remote_source` |  | {{< multiline >}}If this is an input to a task, and the original path is an ``s3`` bucket, Flytekit downloads the
file for the user. In case the user wants access to the original path, it will be here.
{{< /multiline >}} |

## flytekit.interaction.click_types.FlyteLiteralConverter

```python
class FlyteLiteralConverter(
    flyte_ctx: flytekit.core.context_manager.FlyteContext,
    literal_type: flytekit.models.types.LiteralType,
    python_type: typing.Type,
    is_remote: bool,
)
```
| Parameter | Type |
|-|-|
| `flyte_ctx` | `flytekit.core.context_manager.FlyteContext` |
| `literal_type` | `flytekit.models.types.LiteralType` |
| `python_type` | `typing.Type` |
| `is_remote` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Convert the value to a Flyte Literal or a python native type. |
| [`is_bool()`](#is_bool) |  |


#### convert()

```python
def convert(
    ctx: click.core.Context,
    param: typing.Optional[click.core.Parameter],
    value: typing.Any,
) -> typing.Union[flytekit.models.literals.Literal, typing.Any]
```
Convert the value to a Flyte Literal or a python native type. This is used by click to convert the input.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `param` | `typing.Optional[click.core.Parameter]` |
| `value` | `typing.Any` |

#### is_bool()

```python
def is_bool()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `click_type` |  |  |

## flytekit.interaction.click_types.FlytePathResolver

### Methods

| Method | Description |
|-|-|
| [`add_mapping()`](#add_mapping) | Thread safe method to dd a mapping from a flyte uri to a remote path. |
| [`resolve_remote_path()`](#resolve_remote_path) | Given a flyte uri, return the remote path if it exists or was created in current session, otherwise return None. |


#### add_mapping()

```python
def add_mapping(
    flyte_uri: str,
    remote_path: str,
)
```
Thread safe method to dd a mapping from a flyte uri to a remote path


| Parameter | Type |
|-|-|
| `flyte_uri` | `str` |
| `remote_path` | `str` |

#### resolve_remote_path()

```python
def resolve_remote_path(
    flyte_uri: str,
) -> typing.Optional[str]
```
Given a flyte uri, return the remote path if it exists or was created in current session, otherwise return None


| Parameter | Type |
|-|-|
| `flyte_uri` | `str` |

## flytekit.interaction.click_types.FlytePickleTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
def FlytePickleTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
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
    t: typing.Type[~T],
    v: ~T,
)
```
| Parameter | Type |
|-|-|
| `t` | `typing.Type[~T]` |
| `v` | `~T` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: ~T,
    python_type: typing.Type[~T],
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
| `python_val` | `~T` |
| `python_type` | `typing.Type[~T]` |
| `expected` | `flytekit.models.types.LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[~T],
) -> ~T
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `lv` | `flytekit.models.literals.Literal` |
| `expected_python_type` | `typing.Type[~T]` |

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
    t: typing.Type[~T],
) -> flytekit.models.types.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.Type[~T]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: flytekit.models.types.LiteralType,
) -> typing.Type[flytekit.types.pickle.pickle.FlytePickle.__class_getitem__.<locals>._SpecificFormatClass]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `flytekit.models.types.LiteralType` |

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


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.interaction.click_types.FlyteSchema

```python
class FlyteSchema(
    local_path: typing.Optional[str],
    remote_path: typing.Optional[str],
    supported_mode: SchemaOpenMode,
    downloader: typing.Optional[typing.Callable],
)
```
| Parameter | Type |
|-|-|
| `local_path` | `typing.Optional[str]` |
| `remote_path` | `typing.Optional[str]` |
| `supported_mode` | `SchemaOpenMode` |
| `downloader` | `typing.Optional[typing.Callable]` |

### Methods

| Method | Description |
|-|-|
| [`as_readonly()`](#as_readonly) |  |
| [`column_names()`](#column_names) |  |
| [`columns()`](#columns) |  |
| [`deserialize_flyte_schema()`](#deserialize_flyte_schema) |  |
| [`format()`](#format) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`open()`](#open) | Returns a reader or writer depending on the mode of the object when created. |
| [`serialize_flyte_schema()`](#serialize_flyte_schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### as_readonly()

```python
def as_readonly()
```
#### column_names()

```python
def column_names()
```
#### columns()

```python
def columns()
```
#### deserialize_flyte_schema()

```python
def deserialize_flyte_schema(
    info,
) -> FlyteSchema
```
| Parameter | Type |
|-|-|
| `info` |  |

#### format()

```python
def format()
```
#### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### open()

```python
def open(
    dataframe_fmt: typing.Optional[type],
    override_mode: typing.Optional[SchemaOpenMode],
) -> typing.Union[SchemaReader, SchemaWriter]
```
Returns a reader or writer depending on the mode of the object when created. This mode can be
overridden, but will depend on whether the override can be performed. For example, if the Object was
created in a read-mode a "write mode" override is not allowed.
if the object was created in write-mode, a read is allowed.



| Parameter | Type |
|-|-|
| `dataframe_fmt` | `typing.Optional[type]` |
| `override_mode` | `typing.Optional[SchemaOpenMode]` |

#### serialize_flyte_schema()

```python
def serialize_flyte_schema()
```
#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `local_path` |  |  |
| `supported_mode` |  |  |

## flytekit.interaction.click_types.JSONIteratorParamType

Represents the type of a parameter. Validates and converts values
from the command line or Python into the correct type.

To implement a custom type, subclass and implement at least the
following:

-   The :attr:`name` class attribute must be set.
-   Calling an instance of the type with ``None`` must return
``None``. This is already implemented by default.
-   :meth:`convert` must convert string values to the correct type.
-   :meth:`convert` must accept values that are already the correct
type.
-   It must be able to convert a value if the ``ctx`` and ``param``
arguments are ``None``. This can occur when converting prompt
input.


### Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Convert the value to the correct type. |
| [`fail()`](#fail) | Helper method to fail with an invalid value message. |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one. |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing. |
| [`shell_complete()`](#shell_complete) | Return a list of. |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


#### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
) -> typing.Any
```
Convert the value to the correct type. This is not called if
the value is ``None`` (the missing value).

This must accept string values from the command line, as well as
values that are already the correct type. It may also convert
other compatible types.

The ``param`` and ``ctx`` arguments may be ``None`` in certain
situations, such as when converting prompt input.

If the value cannot be converted, call :meth:`fail` with a
descriptive message.



| Parameter | Type |
|-|-|
| `value` | `typing.Any` |
| `param` | `typing.Optional[click.core.Parameter]` |
| `ctx` | `typing.Optional[click.core.Context]` |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type |
|-|-|
| `message` | `str` |
| `param` | `typing.Optional[ForwardRef('Parameter')]` |
| `ctx` | `typing.Optional[ForwardRef('Context')]` |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Return a list of
:class:`~click.shell_completion.CompletionItem` objects for the
incomplete value. Most types do not provide completions, but
some do, and this allows custom types to provide custom
completions as well.



| Parameter | Type |
|-|-|
| `ctx` | `Context` |
| `param` | `Parameter` |
| `incomplete` | `str` |

#### split_envvar_value()

```python
def split_envvar_value(
    rv: str,
) -> typing.Sequence[str]
```
Given a value from an environment variable this splits it up
into small chunks depending on the defined envvar list splitter.

If the splitter is set to `None`, which means that whitespace splits,
then leading and trailing whitespace is ignored.  Otherwise, leading
and trailing splitters usually lead to empty items being included.


| Parameter | Type |
|-|-|
| `rv` | `str` |

#### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

.. versionadded:: 8.0


## flytekit.interaction.click_types.JSONIteratorTransformer

A JSON iterator that handles conversion between an iterator/generator and a JSONL file.


```python
def JSONIteratorTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
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
| Parameter | Type |
|-|-|
| `t` | `Type[T]` |
| `v` | `T` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: typing.Iterator[typing.Union[typing.Dict[str, typing.Any], typing.List[typing.Any], bool, float, int, str]],
    python_type: typing.Type[typing.Iterator[typing.Union[typing.Dict[str, typing.Any], typing.List[typing.Any], bool, float, int, str]]],
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
| `python_val` | `typing.Iterator[typing.Union[typing.Dict[str, typing.Any], typing.List[typing.Any], bool, float, int, str]]` |
| `python_type` | `typing.Type[typing.Iterator[typing.Union[typing.Dict[str, typing.Any], typing.List[typing.Any], bool, float, int, str]]]` |
| `expected` | `flytekit.models.types.LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[typing.Iterator[typing.Union[typing.Dict[str, typing.Any], typing.List[typing.Any], bool, float, int, str]]],
) -> flytekit.types.iterator.json_iterator.JSONIterator
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `lv` | `flytekit.models.literals.Literal` |
| `expected_python_type` | `typing.Type[typing.Iterator[typing.Union[typing.Dict[str, typing.Any], typing.List[typing.Any], bool, float, int, str]]]` |

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
    t: typing.Type[typing.Iterator[typing.Union[typing.Dict[str, typing.Any], typing.List[typing.Any], bool, float, int, str]]],
) -> flytekit.models.types.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.Type[typing.Iterator[typing.Union[typing.Dict[str, typing.Any], typing.List[typing.Any], bool, float, int, str]]]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: flytekit.models.types.LiteralType,
) -> typing.Type[typing.Iterator[typing.Union[typing.Dict[str, typing.Any], typing.List[typing.Any], bool, float, int, str]]]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `flytekit.models.types.LiteralType` |

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


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.interaction.click_types.JsonParamType

Represents the type of a parameter. Validates and converts values
from the command line or Python into the correct type.

To implement a custom type, subclass and implement at least the
following:

-   The :attr:`name` class attribute must be set.
-   Calling an instance of the type with ``None`` must return
``None``. This is already implemented by default.
-   :meth:`convert` must convert string values to the correct type.
-   :meth:`convert` must accept values that are already the correct
type.
-   It must be able to convert a value if the ``ctx`` and ``param``
arguments are ``None``. This can occur when converting prompt
input.


```python
class JsonParamType(
    python_type: typing.Type,
)
```
| Parameter | Type |
|-|-|
| `python_type` | `typing.Type` |

### Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Convert the value to the correct type. |
| [`fail()`](#fail) | Helper method to fail with an invalid value message. |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one. |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing. |
| [`shell_complete()`](#shell_complete) | Return a list of. |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


#### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
) -> typing.Any
```
Convert the value to the correct type. This is not called if
the value is ``None`` (the missing value).

This must accept string values from the command line, as well as
values that are already the correct type. It may also convert
other compatible types.

The ``param`` and ``ctx`` arguments may be ``None`` in certain
situations, such as when converting prompt input.

If the value cannot be converted, call :meth:`fail` with a
descriptive message.



| Parameter | Type |
|-|-|
| `value` | `typing.Any` |
| `param` | `typing.Optional[click.core.Parameter]` |
| `ctx` | `typing.Optional[click.core.Context]` |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type |
|-|-|
| `message` | `str` |
| `param` | `typing.Optional[ForwardRef('Parameter')]` |
| `ctx` | `typing.Optional[ForwardRef('Context')]` |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Return a list of
:class:`~click.shell_completion.CompletionItem` objects for the
incomplete value. Most types do not provide completions, but
some do, and this allows custom types to provide custom
completions as well.



| Parameter | Type |
|-|-|
| `ctx` | `Context` |
| `param` | `Parameter` |
| `incomplete` | `str` |

#### split_envvar_value()

```python
def split_envvar_value(
    rv: str,
) -> typing.Sequence[str]
```
Given a value from an environment variable this splits it up
into small chunks depending on the defined envvar list splitter.

If the splitter is set to `None`, which means that whitespace splits,
then leading and trailing whitespace is ignored.  Otherwise, leading
and trailing splitters usually lead to empty items being included.


| Parameter | Type |
|-|-|
| `rv` | `str` |

#### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

.. versionadded:: 8.0


## flytekit.interaction.click_types.Literal

```python
class Literal(
    scalar: typing.Optional[flytekit.models.literals.Scalar],
    collection: typing.Optional[flytekit.models.literals.LiteralCollection],
    map: typing.Optional[flytekit.models.literals.LiteralMap],
    hash: typing.Optional[str],
    metadata: typing.Optional[typing.Dict[str, str]],
    offloaded_metadata: typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata],
)
```
This IDL message represents a literal value in the Flyte ecosystem.



| Parameter | Type |
|-|-|
| `scalar` | `typing.Optional[flytekit.models.literals.Scalar]` |
| `collection` | `typing.Optional[flytekit.models.literals.LiteralCollection]` |
| `map` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `hash` | `typing.Optional[str]` |
| `metadata` | `typing.Optional[typing.Dict[str, str]]` |
| `offloaded_metadata` | `typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`set_metadata()`](#set_metadata) | Note: This is a mutation on the literal. |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.Literal,
) -> Literal
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.Literal` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### set_metadata()

```python
def set_metadata(
    metadata: typing.Dict[str, str],
)
```
Note: This is a mutation on the literal


| Parameter | Type |
|-|-|
| `metadata` | `typing.Dict[str, str]` |

#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `collection` |  | {{< multiline >}}If not None, this value holds a collection of Literal values which can be further unpacked.
{{< /multiline >}} |
| `hash` |  | {{< multiline >}}If not None, this value holds a hash that represents the literal for caching purposes.
{{< /multiline >}} |
| `is_empty` |  |  |
| `map` |  | {{< multiline >}}If not None, this value holds a map of Literal values which can be further unpacked.
{{< /multiline >}} |
| `metadata` |  | {{< multiline >}}This value holds metadata about the literal.
{{< /multiline >}} |
| `offloaded_metadata` |  | {{< multiline >}}This value holds metadata about the offloaded literal.
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}If not None, this value holds a scalar value which can be further unpacked.
{{< /multiline >}} |
| `value` |  | {{< multiline >}}Returns one of the scalar, collection, or map properties based on which one is set.
{{< /multiline >}} |

## flytekit.interaction.click_types.LiteralType

```python
class LiteralType(
    simple,
    schema,
    collection_type,
    map_value_type,
    blob,
    enum_type,
    union_type,
    structured_dataset_type,
    metadata,
    structure,
    annotation,
)
```
This is a oneof message, only one of the kwargs may be set, representing one of the Flyte types.



| Parameter | Type |
|-|-|
| `simple` |  |
| `schema` |  |
| `collection_type` |  |
| `map_value_type` |  |
| `blob` |  |
| `enum_type` |  |
| `union_type` |  |
| `structured_dataset_type` |  |
| `metadata` |  |
| `structure` |  |
| `annotation` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> LiteralType
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `annotation` |  |  |
| `blob` |  |  |
| `collection_type` |  | {{< multiline >}}The collection value type
{{< /multiline >}} |
| `enum_type` |  |  |
| `is_empty` |  |  |
| `map_value_type` |  | {{< multiline >}}The Value for a dictionary. Key is always string
{{< /multiline >}} |
| `metadata` |  |  |
| `schema` |  |  |
| `simple` |  |  |
| `structure` |  |  |
| `structured_dataset_type` |  |  |
| `union_type` |  |  |

## flytekit.interaction.click_types.PickleParamType

Represents the type of a parameter. Validates and converts values
from the command line or Python into the correct type.

To implement a custom type, subclass and implement at least the
following:

-   The :attr:`name` class attribute must be set.
-   Calling an instance of the type with ``None`` must return
``None``. This is already implemented by default.
-   :meth:`convert` must convert string values to the correct type.
-   :meth:`convert` must accept values that are already the correct
type.
-   It must be able to convert a value if the ``ctx`` and ``param``
arguments are ``None``. This can occur when converting prompt
input.


### Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Convert the value to the correct type. |
| [`fail()`](#fail) | Helper method to fail with an invalid value message. |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one. |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing. |
| [`shell_complete()`](#shell_complete) | Return a list of. |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


#### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
) -> typing.Any
```
Convert the value to the correct type. This is not called if
the value is ``None`` (the missing value).

This must accept string values from the command line, as well as
values that are already the correct type. It may also convert
other compatible types.

The ``param`` and ``ctx`` arguments may be ``None`` in certain
situations, such as when converting prompt input.

If the value cannot be converted, call :meth:`fail` with a
descriptive message.



| Parameter | Type |
|-|-|
| `value` | `typing.Any` |
| `param` | `typing.Optional[click.core.Parameter]` |
| `ctx` | `typing.Optional[click.core.Context]` |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type |
|-|-|
| `message` | `str` |
| `param` | `typing.Optional[ForwardRef('Parameter')]` |
| `ctx` | `typing.Optional[ForwardRef('Context')]` |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Return a list of
:class:`~click.shell_completion.CompletionItem` objects for the
incomplete value. Most types do not provide completions, but
some do, and this allows custom types to provide custom
completions as well.



| Parameter | Type |
|-|-|
| `ctx` | `Context` |
| `param` | `Parameter` |
| `incomplete` | `str` |

#### split_envvar_value()

```python
def split_envvar_value(
    rv: str,
) -> typing.Sequence[str]
```
Given a value from an environment variable this splits it up
into small chunks depending on the defined envvar list splitter.

If the splitter is set to `None`, which means that whitespace splits,
then leading and trailing whitespace is ignored.  Otherwise, leading
and trailing splitters usually lead to empty items being included.


| Parameter | Type |
|-|-|
| `rv` | `str` |

#### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

.. versionadded:: 8.0


## flytekit.interaction.click_types.SimpleType

## flytekit.interaction.click_types.StructuredDataset

This is the user facing StructuredDataset class. Please don't confuse it with the literals.StructuredDataset
class (that is just a model, a Python class representation of the protobuf).


```python
class StructuredDataset(
    dataframe: typing.Optional[typing.Any],
    uri: typing.Optional[str],
    metadata: typing.Optional[literals.StructuredDatasetMetadata],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `dataframe` | `typing.Optional[typing.Any]` |
| `uri` | `typing.Optional[str]` |
| `metadata` | `typing.Optional[literals.StructuredDatasetMetadata]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`all()`](#all) |  |
| [`column_names()`](#column_names) |  |
| [`columns()`](#columns) |  |
| [`deserialize_structured_dataset()`](#deserialize_structured_dataset) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`iter()`](#iter) |  |
| [`open()`](#open) |  |
| [`serialize_structured_dataset()`](#serialize_structured_dataset) |  |
| [`set_literal()`](#set_literal) | A public wrapper method to set the StructuredDataset Literal. |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### all()

```python
def all()
```
#### column_names()

```python
def column_names()
```
#### columns()

```python
def columns()
```
#### deserialize_structured_dataset()

```python
def deserialize_structured_dataset(
    info,
) -> StructuredDataset
```
| Parameter | Type |
|-|-|
| `info` |  |

#### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### iter()

```python
def iter()
```
#### open()

```python
def open(
    dataframe_type: Type[DF],
)
```
| Parameter | Type |
|-|-|
| `dataframe_type` | `Type[DF]` |

#### serialize_structured_dataset()

```python
def serialize_structured_dataset()
```
#### set_literal()

```python
def set_literal(
    ctx: FlyteContext,
    expected: LiteralType,
)
```
A public wrapper method to set the StructuredDataset Literal.

This method provides external access to the internal _set_literal method.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `expected` | `LiteralType` |

#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `dataframe` |  |  |
| `literal` |  |  |
| `metadata` |  |  |

## flytekit.interaction.click_types.StructuredDatasetParamType

TODO handle column types


### Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Convert the value to the correct type. |
| [`fail()`](#fail) | Helper method to fail with an invalid value message. |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one. |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing. |
| [`shell_complete()`](#shell_complete) | Return a list of. |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


#### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
) -> typing.Any
```
Convert the value to the correct type. This is not called if
the value is ``None`` (the missing value).

This must accept string values from the command line, as well as
values that are already the correct type. It may also convert
other compatible types.

The ``param`` and ``ctx`` arguments may be ``None`` in certain
situations, such as when converting prompt input.

If the value cannot be converted, call :meth:`fail` with a
descriptive message.



| Parameter | Type |
|-|-|
| `value` | `typing.Any` |
| `param` | `typing.Optional[click.core.Parameter]` |
| `ctx` | `typing.Optional[click.core.Context]` |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type |
|-|-|
| `message` | `str` |
| `param` | `typing.Optional[ForwardRef('Parameter')]` |
| `ctx` | `typing.Optional[ForwardRef('Context')]` |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Return a list of
:class:`~click.shell_completion.CompletionItem` objects for the
incomplete value. Most types do not provide completions, but
some do, and this allows custom types to provide custom
completions as well.



| Parameter | Type |
|-|-|
| `ctx` | `Context` |
| `param` | `Parameter` |
| `incomplete` | `str` |

#### split_envvar_value()

```python
def split_envvar_value(
    rv: str,
) -> typing.Sequence[str]
```
Given a value from an environment variable this splits it up
into small chunks depending on the defined envvar list splitter.

If the splitter is set to `None`, which means that whitespace splits,
then leading and trailing whitespace is ignored.  Otherwise, leading
and trailing splitters usually lead to empty items being included.


| Parameter | Type |
|-|-|
| `rv` | `str` |

#### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

.. versionadded:: 8.0


## flytekit.interaction.click_types.TypeEngine

Core Extensible TypeEngine of Flytekit. This should be used to extend the capabilities of FlyteKits type system.
Users can implement their own TypeTransformers and register them with the TypeEngine. This will allow special handling
of user objects


### Methods

| Method | Description |
|-|-|
| [`async_to_literal()`](#async_to_literal) | Converts a python value of a given type and expected ``LiteralType`` into a resolved ``Literal`` value. |
| [`async_to_python_value()`](#async_to_python_value) |  |
| [`calculate_hash()`](#calculate_hash) |  |
| [`dict_to_literal_map()`](#dict_to_literal_map) |  |
| [`dict_to_literal_map_pb()`](#dict_to_literal_map_pb) |  |
| [`get_available_transformers()`](#get_available_transformers) | Returns all python types for which transformers are available. |
| [`get_transformer()`](#get_transformer) | Implements a recursive search for the transformer. |
| [`guess_python_type()`](#guess_python_type) | Transforms a flyte-specific ``LiteralType`` to a regular python value. |
| [`guess_python_types()`](#guess_python_types) | Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values. |
| [`lazy_import_transformers()`](#lazy_import_transformers) | Only load the transformers if needed. |
| [`literal_map_to_kwargs()`](#literal_map_to_kwargs) |  |
| [`named_tuple_to_variable_map()`](#named_tuple_to_variable_map) | Converts a python-native ``NamedTuple`` to a flyte-specific VariableMap of named literals. |
| [`register()`](#register) | This should be used for all types that respond with the right type annotation when you use type(. |
| [`register_additional_type()`](#register_additional_type) |  |
| [`register_restricted_type()`](#register_restricted_type) |  |
| [`to_html()`](#to_html) |  |
| [`to_literal()`](#to_literal) | The current dance is because we are allowing users to call from an async function, this synchronous. |
| [`to_literal_checks()`](#to_literal_checks) |  |
| [`to_literal_type()`](#to_literal_type) | Converts a python type into a flyte specific ``LiteralType``. |
| [`to_python_value()`](#to_python_value) | Converts a Literal value with an expected python type into a python value. |
| [`unwrap_offloaded_literal()`](#unwrap_offloaded_literal) |  |


#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a python value of a given type and expected ``LiteralType`` into a resolved ``Literal`` value.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type` |

#### calculate_hash()

```python
def calculate_hash(
    python_val: typing.Any,
    python_type: Type[T],
) -> Optional[str]
```
| Parameter | Type |
|-|-|
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |

#### dict_to_literal_map()

```python
def dict_to_literal_map(
    ctx: FlyteContext,
    d: typing.Dict[str, typing.Any],
    type_hints: Optional[typing.Dict[str, type]],
) -> LiteralMap
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `d` | `typing.Dict[str, typing.Any]` |
| `type_hints` | `Optional[typing.Dict[str, type]]` |

#### dict_to_literal_map_pb()

```python
def dict_to_literal_map_pb(
    ctx: FlyteContext,
    d: typing.Dict[str, typing.Any],
    type_hints: Optional[typing.Dict[str, type]],
) -> Optional[literals_pb2.LiteralMap]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `d` | `typing.Dict[str, typing.Any]` |
| `type_hints` | `Optional[typing.Dict[str, type]]` |

#### get_available_transformers()

```python
def get_available_transformers()
```
Returns all python types for which transformers are available


#### get_transformer()

```python
def get_transformer(
    python_type: Type,
) -> TypeTransformer[T]
```
Implements a recursive search for the transformer.


| Parameter | Type |
|-|-|
| `python_type` | `Type` |

#### guess_python_type()

```python
def guess_python_type(
    flyte_type: LiteralType,
) -> Type[T]
```
Transforms a flyte-specific ``LiteralType`` to a regular python value.


| Parameter | Type |
|-|-|
| `flyte_type` | `LiteralType` |

#### guess_python_types()

```python
def guess_python_types(
    flyte_variable_dict: typing.Dict[str, _interface_models.Variable],
) -> typing.Dict[str, type]
```
Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values.


| Parameter | Type |
|-|-|
| `flyte_variable_dict` | `typing.Dict[str, _interface_models.Variable]` |

#### lazy_import_transformers()

```python
def lazy_import_transformers()
```
Only load the transformers if needed.


#### literal_map_to_kwargs()

```python
def literal_map_to_kwargs(
    ctx: FlyteContext,
    lm: LiteralMap,
    python_types: typing.Optional[typing.Dict[str, type]],
    literal_types: typing.Optional[typing.Dict[str, _interface_models.Variable]],
) -> typing.Dict[str, typing.Any]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lm` | `LiteralMap` |
| `python_types` | `typing.Optional[typing.Dict[str, type]]` |
| `literal_types` | `typing.Optional[typing.Dict[str, _interface_models.Variable]]` |

#### named_tuple_to_variable_map()

```python
def named_tuple_to_variable_map(
    t: typing.NamedTuple,
) -> _interface_models.VariableMap
```
Converts a python-native ``NamedTuple`` to a flyte-specific VariableMap of named literals.


| Parameter | Type |
|-|-|
| `t` | `typing.NamedTuple` |

#### register()

```python
def register(
    transformer: TypeTransformer,
    additional_types: Optional[typing.List[Type]],
)
```
This should be used for all types that respond with the right type annotation when you use type(...) function


| Parameter | Type |
|-|-|
| `transformer` | `TypeTransformer` |
| `additional_types` | `Optional[typing.List[Type]]` |

#### register_additional_type()

```python
def register_additional_type(
    transformer: TypeTransformer[T],
    additional_type: Type[T],
    override,
)
```
| Parameter | Type |
|-|-|
| `transformer` | `TypeTransformer[T]` |
| `additional_type` | `Type[T]` |
| `override` |  |

#### register_restricted_type()

```python
def register_restricted_type(
    name: str,
    type: Type[T],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `type` | `Type[T]` |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: typing.Any,
    expected_python_type: Type[typing.Any],
) -> str
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `expected_python_type` | `Type[typing.Any]` |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
The current dance is because we are allowing users to call from an async function, this synchronous
to_literal function, and allowing this to_literal function, to then invoke yet another async function,
namely an async transformer.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_literal_checks()

```python
def to_literal_checks(
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
)
```
| Parameter | Type |
|-|-|
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_literal_type()

```python
def to_literal_type(
    python_type: Type[T],
) -> LiteralType
```
Converts a python type into a flyte specific ``LiteralType``


| Parameter | Type |
|-|-|
| `python_type` | `Type[T]` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type,
) -> typing.Any
```
Converts a Literal value with an expected python type into a python value.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type` |

#### unwrap_offloaded_literal()

```python
def unwrap_offloaded_literal(
    ctx: FlyteContext,
    lv: Literal,
) -> Literal
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |

## flytekit.interaction.click_types.UnionParamType

A composite type that allows for multiple types to be specified. This is used for union types.


```python
class UnionParamType(
    types: typing.List[click.types.ParamType],
)
```
| Parameter | Type |
|-|-|
| `types` | `typing.List[click.types.ParamType]` |

### Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Important to implement NoneType / Optional. |
| [`fail()`](#fail) | Helper method to fail with an invalid value message. |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one. |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing. |
| [`shell_complete()`](#shell_complete) | Return a list of. |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


#### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
) -> typing.Any
```
Important to implement NoneType / Optional.
Also could we just determine the click types from the python types


| Parameter | Type |
|-|-|
| `value` | `typing.Any` |
| `param` | `typing.Optional[click.core.Parameter]` |
| `ctx` | `typing.Optional[click.core.Context]` |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type |
|-|-|
| `message` | `str` |
| `param` | `typing.Optional[ForwardRef('Parameter')]` |
| `ctx` | `typing.Optional[ForwardRef('Context')]` |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Return a list of
:class:`~click.shell_completion.CompletionItem` objects for the
incomplete value. Most types do not provide completions, but
some do, and this allows custom types to provide custom
completions as well.



| Parameter | Type |
|-|-|
| `ctx` | `Context` |
| `param` | `Parameter` |
| `incomplete` | `str` |

#### split_envvar_value()

```python
def split_envvar_value(
    rv: str,
) -> typing.Sequence[str]
```
Given a value from an environment variable this splits it up
into small chunks depending on the defined envvar list splitter.

If the splitter is set to `None`, which means that whitespace splits,
then leading and trailing whitespace is ignored.  Otherwise, leading
and trailing splitters usually lead to empty items being included.


| Parameter | Type |
|-|-|
| `rv` | `str` |

#### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

.. versionadded:: 8.0


### Properties

| Property | Type | Description |
|-|-|-|
| `name` |  |  |

