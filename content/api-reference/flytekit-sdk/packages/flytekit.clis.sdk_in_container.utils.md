---
title: flytekit.clis.sdk_in_container.utils
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.utils

## Directory

### Classes

| Class | Description |
|-|-|
| [`ErrorHandlingCommand`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilserrorhandlingcommand) | Helper class that wraps the invoke method of a click command to catch exceptions and print them in a nice way. |
| [`PyFlyteParams`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilspyflyteparams) |  |

### Methods

| Method | Description |
|-|-|
| [`get_option_from_metadata()`](#get_option_from_metadata) |  |
| [`make_click_option_field()`](#make_click_option_field) |  |
| [`pretty_print_exception()`](#pretty_print_exception) | This method will print the exception in a nice way. |
| [`pretty_print_grpc_error()`](#pretty_print_grpc_error) | This method will print the grpc error that us more human readable. |
| [`pretty_print_traceback()`](#pretty_print_traceback) | This method will print the Traceback of an error. |
| [`remove_unwanted_traceback_frames()`](#remove_unwanted_traceback_frames) | Custom function to remove certain frames from the traceback. |
| [`validate_package()`](#validate_package) | This method will validate the packages passed in by the user. |


### Variables

| Property | Type | Description |
|-|-|-|
| `SOURCE_CODE` | `str` |  |

## Methods

#### get_option_from_metadata()

```python
def get_option_from_metadata(
    metadata: mappingproxy,
) -> click.core.Option
```
| Parameter | Type |
|-|-|
| `metadata` | `mappingproxy` |

#### make_click_option_field()

```python
def make_click_option_field(
    o: click.core.Option,
) -> dataclasses.Field
```
| Parameter | Type |
|-|-|
| `o` | `click.core.Option` |

#### pretty_print_exception()

```python
def pretty_print_exception(
    e: Exception,
    verbosity: int,
)
```
This method will print the exception in a nice way. It will also check if the exception is a grpc.RpcError and
print it in a human-readable way.


| Parameter | Type |
|-|-|
| `e` | `Exception` |
| `verbosity` | `int` |

#### pretty_print_grpc_error()

```python
def pretty_print_grpc_error(
    e: grpc.RpcError,
)
```
This method will print the grpc error that us more human readable.


| Parameter | Type |
|-|-|
| `e` | `grpc.RpcError` |

#### pretty_print_traceback()

```python
def pretty_print_traceback(
    e: Exception,
    verbosity: int,
)
```
This method will print the Traceback of an error.
Print the traceback in a nice formatted way if verbose is set to True.


| Parameter | Type |
|-|-|
| `e` | `Exception` |
| `verbosity` | `int` |

#### remove_unwanted_traceback_frames()

```python
def remove_unwanted_traceback_frames(
    tb: traceback,
    unwanted_module_names: typing.List[str],
) -> traceback
```
Custom function to remove certain frames from the traceback.


| Parameter | Type |
|-|-|
| `tb` | `traceback` |
| `unwanted_module_names` | `typing.List[str]` |

#### validate_package()

```python
def validate_package(
    ctx,
    param,
    values,
)
```
This method will validate the packages passed in by the user. It will check that the packages are in the correct
format, and will also split the packages if the user passed in a comma separated list.


| Parameter | Type |
|-|-|
| `ctx` |  |
| `param` |  |
| `values` |  |

## flytekit.clis.sdk_in_container.utils.ErrorHandlingCommand

Helper class that wraps the invoke method of a click command to catch exceptions and print them in a nice way.


```python
class ErrorHandlingCommand(
    args: `*args`,
    kwargs: `**kwargs`,
)
```
Initialize RichGroup class.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`add_command()`](#add_command) | Registers another :class:`Command` with this group. |
| [`collect_usage_pieces()`](#collect_usage_pieces) | Returns all the pieces that go into the usage line and returns. |
| [`command()`](#command) | A shortcut decorator for declaring and attaching a command to. |
| [`format_commands()`](#format_commands) | Extra format methods for multi methods that adds all the commands. |
| [`format_epilog()`](#format_epilog) | Writes the epilog into the formatter if it exists. |
| [`format_help()`](#format_help) | Writes the help into the formatter if it exists. |
| [`format_help_text()`](#format_help_text) | Writes the help text to the formatter if it exists. |
| [`format_options()`](#format_options) | Writes all the options into the formatter if they exist. |
| [`format_usage()`](#format_usage) | Writes the usage line into the formatter. |
| [`get_command()`](#get_command) | Given a context and a command name, this returns a. |
| [`get_help()`](#get_help) | Formats the help into a string and returns it. |
| [`get_help_option()`](#get_help_option) | Returns the help option object. |
| [`get_help_option_names()`](#get_help_option_names) | Returns the names for the help option. |
| [`get_params()`](#get_params) |  |
| [`get_short_help_str()`](#get_short_help_str) | Gets short help for the command or makes it by shortening the. |
| [`get_usage()`](#get_usage) | Formats the usage line into a string and returns it. |
| [`group()`](#group) | A shortcut decorator for declaring and attaching a group to. |
| [`invoke()`](#invoke) | Given a context, this invokes the attached callback (if it exists). |
| [`list_commands()`](#list_commands) | Returns a list of subcommand names in the order they should. |
| [`main()`](#main) | This is the way to invoke a script with all the bells and. |
| [`make_context()`](#make_context) | This function when given an info name and arguments will kick. |
| [`make_parser()`](#make_parser) | Creates the underlying option parser for this command. |
| [`parse_args()`](#parse_args) | Given a context and a list of arguments this creates the parser. |
| [`resolve_command()`](#resolve_command) |  |
| [`result_callback()`](#result_callback) | Adds a result callback to the command. |
| [`shell_complete()`](#shell_complete) | Return a list of completions for the incomplete value. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


#### add_command()

```python
def add_command(
    cmd: click.core.Command,
    name: typing.Optional[str],
)
```
Registers another :class:`Command` with this group.  If the name
is not provided, the name of the command is used.


| Parameter | Type |
|-|-|
| `cmd` | `click.core.Command` |
| `name` | `typing.Optional[str]` |

#### collect_usage_pieces()

```python
def collect_usage_pieces(
    ctx: click.core.Context,
) -> typing.List[str]
```
Returns all the pieces that go into the usage line and returns
it as a list of strings.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### command()

```python
def command(
    args: `*args`,
    kwargs: `**kwargs`,
) -> typing.Union[typing.Callable[[typing.Callable[..., typing.Any]], rich_click.rich_command.RichCommand], rich_click.rich_command.RichCommand]
```
A shortcut decorator for declaring and attaching a command to
the group. This takes the same arguments as :func:`command` and
immediately registers the created command with this group by
calling :meth:`add_command`.

To customize the command class used, set the
:attr:`command_class` attribute.

.. versionchanged:: 8.1
    This decorator can be applied without parentheses.

.. versionchanged:: 8.0
    Added the :attr:`command_class` attribute.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### format_commands()

```python
def format_commands(
    ctx: rich_click.rich_context.RichContext,
    formatter: rich_click.rich_help_formatter.RichHelpFormatter,
)
```
Extra format methods for multi methods that adds all the commands
after the options.


| Parameter | Type |
|-|-|
| `ctx` | `rich_click.rich_context.RichContext` |
| `formatter` | `rich_click.rich_help_formatter.RichHelpFormatter` |

#### format_epilog()

```python
def format_epilog(
    ctx: rich_click.rich_context.RichContext,
    formatter: rich_click.rich_help_formatter.RichHelpFormatter,
)
```
Writes the epilog into the formatter if it exists.


| Parameter | Type |
|-|-|
| `ctx` | `rich_click.rich_context.RichContext` |
| `formatter` | `rich_click.rich_help_formatter.RichHelpFormatter` |

#### format_help()

```python
def format_help(
    ctx: rich_click.rich_context.RichContext,
    formatter: rich_click.rich_help_formatter.RichHelpFormatter,
)
```
Writes the help into the formatter if it exists.

This is a low-level method called by :meth:`get_help`.

This calls the following methods:

-   :meth:`format_usage`
-   :meth:`format_help_text`
-   :meth:`format_options`
-   :meth:`format_epilog`


| Parameter | Type |
|-|-|
| `ctx` | `rich_click.rich_context.RichContext` |
| `formatter` | `rich_click.rich_help_formatter.RichHelpFormatter` |

#### format_help_text()

```python
def format_help_text(
    ctx: rich_click.rich_context.RichContext,
    formatter: rich_click.rich_help_formatter.RichHelpFormatter,
)
```
Writes the help text to the formatter if it exists.


| Parameter | Type |
|-|-|
| `ctx` | `rich_click.rich_context.RichContext` |
| `formatter` | `rich_click.rich_help_formatter.RichHelpFormatter` |

#### format_options()

```python
def format_options(
    ctx: click.core.Context,
    formatter: click.formatting.HelpFormatter,
)
```
Writes all the options into the formatter if they exist.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `formatter` | `click.formatting.HelpFormatter` |

#### format_usage()

```python
def format_usage(
    ctx: click.core.Context,
    formatter: click.formatting.HelpFormatter,
)
```
Writes the usage line into the formatter.

This is a low-level method called by :meth:`get_usage`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `formatter` | `click.formatting.HelpFormatter` |

#### get_command()

```python
def get_command(
    ctx: click.core.Context,
    cmd_name: str,
) -> typing.Optional[click.core.Command]
```
Given a context and a command name, this returns a
:class:`Command` object if it exists or returns `None`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `cmd_name` | `str` |

#### get_help()

```python
def get_help(
    ctx: click.core.Context,
) -> str
```
Formats the help into a string and returns it.

Calls :meth:`format_help` internally.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_help_option()

```python
def get_help_option(
    ctx: click.core.Context,
) -> typing.Optional[ForwardRef('Option')]
```
Returns the help option object.

Unless ``add_help_option`` is ``False``.

.. versionchanged:: 8.1.8
    The help option is now cached to avoid creating it multiple times.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_help_option_names()

```python
def get_help_option_names(
    ctx: click.core.Context,
) -> typing.List[str]
```
Returns the names for the help option.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_params()

```python
def get_params(
    ctx: click.core.Context,
) -> typing.List[ForwardRef('Parameter')]
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_short_help_str()

```python
def get_short_help_str(
    limit: int,
) -> str
```
Gets short help for the command or makes it by shortening the
long help string.


| Parameter | Type |
|-|-|
| `limit` | `int` |

#### get_usage()

```python
def get_usage(
    ctx: click.core.Context,
) -> str
```
Formats the usage line into a string and returns it.

Calls :meth:`format_usage` internally.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### group()

```python
def group(
    args: `*args`,
    kwargs: `**kwargs`,
) -> typing.Union[typing.Callable[[typing.Callable[..., typing.Any]], ForwardRef('RichGroup')], ForwardRef('RichGroup')]
```
A shortcut decorator for declaring and attaching a group to
the group. This takes the same arguments as :func:`group` and
immediately registers the created group with this group by
calling :meth:`add_command`.

To customize the group class used, set the :attr:`group_class`
attribute.

.. versionchanged:: 8.1
    This decorator can be applied without parentheses.

.. versionchanged:: 8.0
    Added the :attr:`group_class` attribute.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### invoke()

```python
def invoke(
    ctx: click.core.Context,
) -> typing.Any
```
Given a context, this invokes the attached callback (if it exists)
in the right way.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### list_commands()

```python
def list_commands(
    ctx: click.core.Context,
) -> typing.List[str]
```
Returns a list of subcommand names in the order they should
appear.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### main()

```python
def main(
    args: `*args`,
    prog_name: typing.Optional[str],
    complete_var: typing.Optional[str],
    standalone_mode: bool,
    windows_expand_args: bool,
    extra: typing.Any,
) -> typing.Any
```
This is the way to invoke a script with all the bells and
whistles as a command line application.  This will always terminate
the application after a call.  If this is not wanted, ``SystemExit``
needs to be caught.

This method is also available by directly calling the instance of
a :class:`Command`.



| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `prog_name` | `typing.Optional[str]` |
| `complete_var` | `typing.Optional[str]` |
| `standalone_mode` | `bool` |
| `windows_expand_args` | `bool` |
| `extra` | `typing.Any` |

#### make_context()

```python
def make_context(
    info_name: typing.Optional[str],
    args: `*args`,
    parent: typing.Optional[click.core.Context],
    extra: typing.Any,
) -> rich_click.rich_context.RichContext
```
This function when given an info name and arguments will kick
off the parsing and create a new :class:`Context`.  It does not
invoke the actual command callback though.

To quickly customize the context class used without overriding
this method, set the :attr:`context_class` attribute.



| Parameter | Type |
|-|-|
| `info_name` | `typing.Optional[str]` |
| `args` | ``*args`` |
| `parent` | `typing.Optional[click.core.Context]` |
| `extra` | `typing.Any` |

#### make_parser()

```python
def make_parser(
    ctx: click.core.Context,
) -> click.parser.OptionParser
```
Creates the underlying option parser for this command.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### parse_args()

```python
def parse_args(
    ctx: click.core.Context,
    args: `*args`,
) -> typing.List[str]
```
Given a context and a list of arguments this creates the parser
and parses the arguments, then modifies the context as necessary.
This is automatically invoked by :meth:`make_context`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `args` | ``*args`` |

#### resolve_command()

```python
def resolve_command(
    ctx: click.core.Context,
    args: `*args`,
) -> typing.Tuple[typing.Optional[str], typing.Optional[click.core.Command], typing.List[str]]
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `args` | ``*args`` |

#### result_callback()

```python
def result_callback(
    replace: bool,
) -> typing.Callable[[~F], ~F]
```
Adds a result callback to the command.  By default if a
result callback is already registered this will chain them but
this can be disabled with the `replace` parameter.  The result
callback is invoked with the return value of the subcommand
(or the list of return values from all subcommands if chaining
is enabled) as well as the parameters as they would be passed
to the main callback.

Example::

    @click.group()
    @click.option('-i', '--input', default=23)
    def cli(input):
        return 42

    @cli.result_callback()
    def process_result(result, input):
        return result + input



| Parameter | Type |
|-|-|
| `replace` | `bool` |

#### shell_complete()

```python
def shell_complete(
    ctx: click.core.Context,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Return a list of completions for the incomplete value. Looks
at the names of options, subcommands, and chained
multi-commands.



| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `incomplete` | `str` |

#### to_info_dict()

```python
def to_info_dict(
    ctx: click.core.Context,
) -> typing.Dict[str, typing.Any]
```
Gather information that could be useful for a tool generating
user-facing documentation. This traverses the entire structure
below this command.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.



| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

### Properties

| Property | Type | Description |
|-|-|-|
| `console` |  | {{< multiline >}}Rich Console.

This is a separate instance from the help formatter that allows full control of the
console configuration.

See `rich_config` decorator for how to apply the settings.
{{< /multiline >}} |
| `help_config` |  | {{< multiline >}}Rich Help Configuration.
{{< /multiline >}} |

## flytekit.clis.sdk_in_container.utils.PyFlyteParams

```python
class PyFlyteParams(
    config_file: typing.Optional[str],
    verbose: bool,
    pkgs: typing.List[str],
)
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Optional[str]` |
| `verbose` | `bool` |
| `pkgs` | `typing.List[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |


#### from_dict()

```python
def from_dict(
    d: typing.Dict[str, typing.Any],
) -> PyFlyteParams
```
| Parameter | Type |
|-|-|
| `d` | `typing.Dict[str, typing.Any]` |

