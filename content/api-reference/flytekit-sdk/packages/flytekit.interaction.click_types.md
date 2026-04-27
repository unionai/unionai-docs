---
title: flytekit.interaction.click_types
version: 1.16.19
variants: +flyte +union
layout: py_api
---

# flytekit.interaction.click_types

## Directory

### Classes

| Class | Description |
|-|-|
| [`DateTimeType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesdatetimetype) |  |
| [`DirParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesdirparamtype) |  |
| [`DurationParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesdurationparamtype) |  |
| [`EnumParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesenumparamtype) |  |
| [`FileParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesfileparamtype) |  |
| [`FlyteLiteralConverter`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesflyteliteralconverter) |  |
| [`JSONIteratorParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesjsoniteratorparamtype) |  |
| [`JsonParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typesjsonparamtype) |  |
| [`PickleParamType`](.././flytekit.interaction.click_types#flytekitinteractionclick_typespickleparamtype) |  |
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
| [`resource_callback()`](#resource_callback) | Click callback to parse resource strings like 'cpu=1,mem=2Gi' into a Resources object. |


### Variables

| Property | Type | Description |
|-|-|-|
| `SIMPLE_TYPE_CONVERTER` | `dict` |  |
| `click_version` | `str` |  |

## Methods

#### is_pydantic_basemodel()

```python
def is_pydantic_basemodel(
    python_type: typing.Type,
) -> bool
```
Checks if the python type is a pydantic BaseModel


| Parameter | Type | Description |
|-|-|-|
| `python_type` | `typing.Type` | |

#### key_value_callback()

```python
def key_value_callback(
    _: typing.Any,
    param: str,
    values: typing.List[str],
) -> typing.Optional[typing.Dict[str, str]]
```
Callback for click to parse key-value pairs.


| Parameter | Type | Description |
|-|-|-|
| `_` | `typing.Any` | |
| `param` | `str` | |
| `values` | `typing.List[str]` | |

#### labels_callback()

```python
def labels_callback(
    _: typing.Any,
    param: str,
    values: typing.List[str],
) -> typing.Optional[typing.Dict[str, str]]
```
Callback for click to parse labels.


| Parameter | Type | Description |
|-|-|-|
| `_` | `typing.Any` | |
| `param` | `str` | |
| `values` | `typing.List[str]` | |

#### literal_type_to_click_type()

```python
def literal_type_to_click_type(
    lt: flytekit.models.types.LiteralType,
    python_type: typing.Type,
) -> click.types.ParamType
```
Converts a Flyte LiteralType given a python_type to a click.ParamType


| Parameter | Type | Description |
|-|-|-|
| `lt` | `flytekit.models.types.LiteralType` | |
| `python_type` | `typing.Type` | |

#### modify_literal_uris()

```python
def modify_literal_uris(
    lit: flytekit.models.literals.Literal,
)
```
Modifies the literal object recursively to replace the URIs with the native paths.


| Parameter | Type | Description |
|-|-|-|
| `lit` | `flytekit.models.literals.Literal` | |

#### resource_callback()

```python
def resource_callback(
    _: typing.Any,
    param: str,
    value: typing.Optional[str],
) -> typing.Optional[flytekit.core.resources.Resources]
```
Click callback to parse resource strings like 'cpu=1,mem=2Gi' into a Resources object


| Parameter | Type | Description |
|-|-|-|
| `_` | `typing.Any` | |
| `param` | `str` | |
| `value` | `typing.Optional[str]` | |

## flytekit.interaction.click_types.DateTimeType

### Parameters

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



| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Any` | The value to convert. |
| `param` | `typing.Optional[click.core.Parameter]` | The parameter that is using this type to convert its value. May be ``None``. |
| `ctx` | `typing.Optional[click.core.Context]` | The current context that arrived at this value. May be ``None``. |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `param` | `typing.Optional[ForwardRef('Parameter')]` | |
| `ctx` | `typing.Optional[ForwardRef('Context')]` | |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> str
```
Returns the metavar default for this param if it provides one.


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

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



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `Context` | Invocation context for this command. |
| `param` | `Parameter` | The parameter that is requesting completion. |
| `incomplete` | `str` | Value being completed. May be empty.  .. versionadded:: 8.0 |

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


| Parameter | Type | Description |
|-|-|-|
| `rv` | `str` | |

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



| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Any` | The value to convert. |
| `param` | `typing.Optional[click.core.Parameter]` | The parameter that is using this type to convert its value. May be ``None``. |
| `ctx` | `typing.Optional[click.core.Context]` | The current context that arrived at this value. May be ``None``. |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `param` | `typing.Optional[ForwardRef('Parameter')]` | |
| `ctx` | `typing.Optional[ForwardRef('Context')]` | |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

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



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `Context` | Invocation context for this command. |
| `param` | `Parameter` | The parameter that is requesting completion. |
| `incomplete` | `str` | Value being completed. May be empty.  .. versionadded:: 8.0 |

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


| Parameter | Type | Description |
|-|-|-|
| `rv` | `str` | |

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



| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Any` | The value to convert. |
| `param` | `typing.Optional[click.core.Parameter]` | The parameter that is using this type to convert its value. May be ``None``. |
| `ctx` | `typing.Optional[click.core.Context]` | The current context that arrived at this value. May be ``None``. |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `param` | `typing.Optional[ForwardRef('Parameter')]` | |
| `ctx` | `typing.Optional[ForwardRef('Context')]` | |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

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



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `Context` | Invocation context for this command. |
| `param` | `Parameter` | The parameter that is requesting completion. |
| `incomplete` | `str` | Value being completed. May be empty.  .. versionadded:: 8.0 |

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


| Parameter | Type | Description |
|-|-|-|
| `rv` | `str` | |

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

### Parameters

```python
class EnumParamType(
    enum_type: typing.Type[enum.Enum],
)
```
| Parameter | Type | Description |
|-|-|-|
| `enum_type` | `typing.Type[enum.Enum]` | |

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



| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Any` | The value to convert. |
| `param` | `typing.Optional[click.core.Parameter]` | The parameter that is using this type to convert its value. May be ``None``. |
| `ctx` | `typing.Optional[click.core.Context]` | The current context that arrived at this value. May be ``None``. |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `param` | `typing.Optional[ForwardRef('Parameter')]` | |
| `ctx` | `typing.Optional[ForwardRef('Context')]` | |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> str
```
Returns the metavar default for this param if it provides one.


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> str
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

#### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Complete choices that start with the incomplete value.



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `Context` | Invocation context for this command. |
| `param` | `Parameter` | The parameter that is requesting completion. |
| `incomplete` | `str` | Value being completed. May be empty.  .. versionadded:: 8.0 |

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


| Parameter | Type | Description |
|-|-|-|
| `rv` | `str` | |

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



| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Any` | The value to convert. |
| `param` | `typing.Optional[click.core.Parameter]` | The parameter that is using this type to convert its value. May be ``None``. |
| `ctx` | `typing.Optional[click.core.Context]` | The current context that arrived at this value. May be ``None``. |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `param` | `typing.Optional[ForwardRef('Parameter')]` | |
| `ctx` | `typing.Optional[ForwardRef('Context')]` | |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

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



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `Context` | Invocation context for this command. |
| `param` | `Parameter` | The parameter that is requesting completion. |
| `incomplete` | `str` | Value being completed. May be empty.  .. versionadded:: 8.0 |

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


| Parameter | Type | Description |
|-|-|-|
| `rv` | `str` | |

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

### Parameters

```python
class FlyteLiteralConverter(
    flyte_ctx: flytekit.core.context_manager.FlyteContext,
    literal_type: flytekit.models.types.LiteralType,
    python_type: typing.Type,
    is_remote: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `flyte_ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `literal_type` | `flytekit.models.types.LiteralType` | |
| `python_type` | `typing.Type` | |
| `is_remote` | `bool` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `click_type` | `click.types.ParamType` |  |

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


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |
| `param` | `typing.Optional[click.core.Parameter]` | |
| `value` | `typing.Any` | |

#### is_bool()

```python
def is_bool()
```
## flytekit.interaction.click_types.JSONIteratorParamType

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



| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Any` | The value to convert. |
| `param` | `typing.Optional[click.core.Parameter]` | The parameter that is using this type to convert its value. May be ``None``. |
| `ctx` | `typing.Optional[click.core.Context]` | The current context that arrived at this value. May be ``None``. |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `param` | `typing.Optional[ForwardRef('Parameter')]` | |
| `ctx` | `typing.Optional[ForwardRef('Context')]` | |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

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



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `Context` | Invocation context for this command. |
| `param` | `Parameter` | The parameter that is requesting completion. |
| `incomplete` | `str` | Value being completed. May be empty.  .. versionadded:: 8.0 |

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


| Parameter | Type | Description |
|-|-|-|
| `rv` | `str` | |

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

### Parameters

```python
class JsonParamType(
    python_type: typing.Type,
)
```
| Parameter | Type | Description |
|-|-|-|
| `python_type` | `typing.Type` | |

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



| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Any` | The value to convert. |
| `param` | `typing.Optional[click.core.Parameter]` | The parameter that is using this type to convert its value. May be ``None``. |
| `ctx` | `typing.Optional[click.core.Context]` | The current context that arrived at this value. May be ``None``. |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `param` | `typing.Optional[ForwardRef('Parameter')]` | |
| `ctx` | `typing.Optional[ForwardRef('Context')]` | |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

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



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `Context` | Invocation context for this command. |
| `param` | `Parameter` | The parameter that is requesting completion. |
| `incomplete` | `str` | Value being completed. May be empty.  .. versionadded:: 8.0 |

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


| Parameter | Type | Description |
|-|-|-|
| `rv` | `str` | |

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



| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Any` | The value to convert. |
| `param` | `typing.Optional[click.core.Parameter]` | The parameter that is using this type to convert its value. May be ``None``. |
| `ctx` | `typing.Optional[click.core.Context]` | The current context that arrived at this value. May be ``None``. |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `param` | `typing.Optional[ForwardRef('Parameter')]` | |
| `ctx` | `typing.Optional[ForwardRef('Context')]` | |

#### get_metavar()

```python
def get_metavar(
    param: click.core.Parameter,
    args,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type | Description |
|-|-|-|
| `param` | `click.core.Parameter` | |
| `args` | `*args` | |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

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



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `Context` | Invocation context for this command. |
| `param` | `Parameter` | The parameter that is requesting completion. |
| `incomplete` | `str` | Value being completed. May be empty.  .. versionadded:: 8.0 |

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


| Parameter | Type | Description |
|-|-|-|
| `rv` | `str` | |

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



| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Any` | The value to convert. |
| `param` | `typing.Optional[click.core.Parameter]` | The parameter that is using this type to convert its value. May be ``None``. |
| `ctx` | `typing.Optional[click.core.Context]` | The current context that arrived at this value. May be ``None``. |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `param` | `typing.Optional[ForwardRef('Parameter')]` | |
| `ctx` | `typing.Optional[ForwardRef('Context')]` | |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

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



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `Context` | Invocation context for this command. |
| `param` | `Parameter` | The parameter that is requesting completion. |
| `incomplete` | `str` | Value being completed. May be empty.  .. versionadded:: 8.0 |

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


| Parameter | Type | Description |
|-|-|-|
| `rv` | `str` | |

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


### Parameters

```python
class UnionParamType(
    types: typing.List[click.types.ParamType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `types` | `typing.List[click.types.ParamType]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `name` | `str` |  |

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


| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Any` | |
| `param` | `typing.Optional[click.core.Parameter]` | |
| `ctx` | `typing.Optional[click.core.Context]` | |

#### fail()

```python
def fail(
    message: str,
    param: typing.Optional[ForwardRef('Parameter')],
    ctx: typing.Optional[ForwardRef('Context')],
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `param` | `typing.Optional[ForwardRef('Parameter')]` | |
| `ctx` | `typing.Optional[ForwardRef('Context')]` | |

#### get_metavar()

```python
def get_metavar(
    param: Parameter,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
) -> typing.Optional[str]
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |

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



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `Context` | Invocation context for this command. |
| `param` | `Parameter` | The parameter that is requesting completion. |
| `incomplete` | `str` | Value being completed. May be empty.  .. versionadded:: 8.0 |

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


| Parameter | Type | Description |
|-|-|-|
| `rv` | `str` | |

#### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

.. versionadded:: 8.0


