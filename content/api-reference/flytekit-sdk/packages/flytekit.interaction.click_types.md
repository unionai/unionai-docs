---
title: flytekit.interaction.click_types
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interaction.click_types

## Directory

### Classes

| Class | Description |
|-|-|
| [`DateTimeType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesdatetimetype) | The DateTime type converts date strings into `datetime` objects. |
| [`DirParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesdirparamtype) | Represents the type of a parameter. |
| [`DurationParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesdurationparamtype) | Represents the type of a parameter. |
| [`EnumParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesenumparamtype) | The choice type allows a value to be checked against a fixed set. |
| [`FileParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesfileparamtype) | Represents the type of a parameter. |
| [`FlyteLiteralConverter`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesflyteliteralconverter) |  |
| [`JSONIteratorParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesjsoniteratorparamtype) | Represents the type of a parameter. |
| [`JsonParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesjsonparamtype) | Represents the type of a parameter. |
| [`PickleParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typespickleparamtype) | Represents the type of a parameter. |
| [`StructuredDatasetParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesstructureddatasetparamtype) | TODO handle column types. |
| [`UnionParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesunionparamtype) | A composite type that allows for multiple types to be specified. |

### Methods

| Method | Description |
|-|-|
| [`is_pydantic_basemodel()`](#is_pydantic_basemodel) | Checks if the python type is a pydantic BaseModel. |
| [`key_value_callback()`](#key_value_callback) | Callback for click to parse key-value pairs. |
| [`labels_callback()`](#labels_callback) | Callback for click to parse labels. |
| [`literal_type_to_click_type()`](#literal_type_to_click_type) | Converts a Flyte LiteralType given a python_type to a click. |
| [`modify_literal_uris()`](#modify_literal_uris) | Modifies the literal object recursively to replace the URIs with the native paths. |


### Variables

| Property | Type | Description |
|-|-|-|
| `SIMPLE_TYPE_CONVERTER` | `dict` |  |

## Methods

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

