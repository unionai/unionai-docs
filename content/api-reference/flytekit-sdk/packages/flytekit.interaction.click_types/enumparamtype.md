---
title: EnumParamType
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# EnumParamType

**Package:** `flytekit.interaction.click_types`

```python
class EnumParamType(
    enum_type: typing.Type[enum.Enum],
)
```
| Parameter | Type | Description |
|-|-|-|
| `enum_type` | `typing.Type[enum.Enum]` | |

## Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | For a given value from the parser, normalize it and find its. |
| [`fail()`](#fail) | Helper method to fail with an invalid value message. |
| [`get_invalid_choice_message()`](#get_invalid_choice_message) | Get the error message when the given choice is invalid. |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one. |
| [`get_missing_message()`](#get_missing_message) | Message shown when no choice is passed. |
| [`normalize_choice()`](#normalize_choice) | Normalize a choice value, used to map a passed string to a choice. |
| [`shell_complete()`](#shell_complete) | Complete choices that start with the incomplete value. |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
) -> <enum 'Enum'>
```
For a given value from the parser, normalize it and find its
matching normalized value in the list of choices. Then return the
matched "original" choice.


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

### get_invalid_choice_message()

```python
def get_invalid_choice_message(
    value: t.Any,
    ctx: Context | None,
) -> str
```
Get the error message when the given choice is invalid.



| Parameter | Type | Description |
|-|-|-|
| `value` | `t.Any` | The invalid value.  .. versionadded:: 8.2 |
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
) -> str
```
Message shown when no choice is passed.

.. versionchanged:: 8.2.0 Added ``ctx`` argument.


| Parameter | Type | Description |
|-|-|-|
| `param` | `Parameter` | |
| `ctx` | `Context \| None` | |

### normalize_choice()

```python
def normalize_choice(
    choice: ParamTypeValue,
    ctx: Context | None,
) -> str
```
Normalize a choice value, used to map a passed string to a choice.
Each choice must have a unique normalized value.

By default uses :meth:`Context.token_normalize_func` and if not case
sensitive, convert it to a casefolded value.

.. versionadded:: 8.2.0


| Parameter | Type | Description |
|-|-|-|
| `choice` | `ParamTypeValue` | |
| `ctx` | `Context \| None` | |

### shell_complete()

```python
def shell_complete(
    ctx: Context,
    param: Parameter,
    incomplete: str,
) -> list[CompletionItem]
```
Complete choices that start with the incomplete value.



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


