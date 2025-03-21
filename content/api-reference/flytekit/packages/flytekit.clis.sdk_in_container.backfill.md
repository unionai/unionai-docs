---
title: flytekit.clis.sdk_in_container.backfill
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.backfill

## Directory

### Classes

| Class | Description |
|-|-|
| [`DateTimeType`](.././flytekit.clis.sdk_in_container.backfill#flytekitclissdk_in_containerbackfilldatetimetype) | The DateTime type converts date strings into `datetime` objects. |
| [`DurationParamType`](.././flytekit.clis.sdk_in_container.backfill#flytekitclissdk_in_containerbackfilldurationparamtype) | Represents the type of a parameter. |
| [`WorkflowFailurePolicy`](.././flytekit.clis.sdk_in_container.backfill#flytekitclissdk_in_containerbackfillworkflowfailurepolicy) | Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`datetime`](.././flytekit.clis.sdk_in_container.backfill#flytekitclissdk_in_containerbackfilldatetime) | datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`timedelta`](.././flytekit.clis.sdk_in_container.backfill#flytekitclissdk_in_containerbackfilltimedelta) | Difference between two datetime values. |

## flytekit.clis.sdk_in_container.backfill.DateTimeType

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
| [`convert()`](#convert) | Convert the value to the correct type |
| [`fail()`](#fail) | Helper method to fail with an invalid value message |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing |
| [`shell_complete()`](#shell_complete) | Return a list of |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating |


#### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
):
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
):
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
):
```
Returns the metavar default for this param if it provides one.


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
):
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
):
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
):
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


## flytekit.clis.sdk_in_container.backfill.DurationParamType

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
| [`convert()`](#convert) | Convert the value to the correct type |
| [`fail()`](#fail) | Helper method to fail with an invalid value message |
| [`get_metavar()`](#get_metavar) | Returns the metavar default for this param if it provides one |
| [`get_missing_message()`](#get_missing_message) | Optionally might return extra information about a missing |
| [`shell_complete()`](#shell_complete) | Return a list of |
| [`split_envvar_value()`](#split_envvar_value) | Given a value from an environment variable this splits it up |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating |


#### convert()

```python
def convert(
    value: typing.Any,
    param: typing.Optional[click.core.Parameter],
    ctx: typing.Optional[click.core.Context],
):
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
):
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
):
```
Returns the metavar default for this param if it provides one.


| Parameter | Type |
|-|-|
| `param` | `Parameter` |

#### get_missing_message()

```python
def get_missing_message(
    param: Parameter,
):
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
):
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
):
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


## flytekit.clis.sdk_in_container.backfill.WorkflowFailurePolicy

Defines the behavior for a workflow execution in the case of an observed node execution failure. By default, a
workflow execution will immediately enter a failed state if a component node fails.


## flytekit.clis.sdk_in_container.backfill.datetime

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.


## flytekit.clis.sdk_in_container.backfill.timedelta

Difference between two datetime values.

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.


