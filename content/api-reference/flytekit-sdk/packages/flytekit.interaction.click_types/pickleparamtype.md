---
title: PickleParamType
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PickleParamType

**Package:** `flytekit.interaction.click_types`

## Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Convert the value to the correct type. |
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
    param: click.core.Parameter,
    ctx: click.core.Context,
) -> typing.Optional[str]
```
Returns the metavar default for this param if it provides one.


| Parameter | Type | Description |
|-|-|-|
| `param` | `click.core.Parameter` | |
| `ctx` | `click.core.Context` | |

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


