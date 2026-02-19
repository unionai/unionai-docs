---
title: UnionParamType
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# UnionParamType

**Package:** `flytekit.interaction.click_types`

A composite type that allows for multiple types to be specified. This is used for union types.



```python
class UnionParamType(
    types: typing.List[click.types.ParamType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `types` | `typing.List[click.types.ParamType]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Important to implement NoneType / Optional. |
| [`fail()`](#fail) | Helper method to fail with an invalid value message. |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one. |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing. |
| [`shell_complete()`](#shell_complete) | Return a list of. |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


### convert()

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

### fail()

```python
def fail(
    message: str,
    param: Parameter | None,
    ctx: Context | None,
) -> t.NoReturn
```
Helper method to fail with an invalid value message.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `param` | `Parameter \| None` | |
| `ctx` | `Context \| None` | |

### get_metavar()

```python
def get_metavar(
    param: Parameter,
    ctx: Context,
) -> str | None
```
Returns the metavar default for this param if it provides one.


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |
| `ctx` | `Context` | |

### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
    ctx: Context | None,
) -> str | None
```
Optionally might return extra information about a missing
parameter.

.. versionadded:: 2.0


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |
| `ctx` | `Context \| None` | |

### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> list[CompletionItem]
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

### split_envvar_value()

```python
def split_envvar_value(
    rv: str,
) -> cabc.Sequence[str]
```
Given a value from an environment variable this splits it up
into small chunks depending on the defined envvar list splitter.

If the splitter is set to `None`, which means that whitespace splits,
then leading and trailing whitespace is ignored.  Otherwise, leading
and trailing splitters usually lead to empty items being included.


| Parameter | Type | Description |
|-|-|-|
| `rv` | `str` | |

### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

.. versionadded:: 8.0


