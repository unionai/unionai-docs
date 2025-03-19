---
title: flytekit.clis.sdk_in_container.run
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.run

## Directory

### Classes

| Class | Description |
|-|-|
| [`Annotations`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunannotations) | None. |
| [`ArtifactQuery`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunartifactquery) | None. |
| [`Context`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerruncontext) | The context is a special internal object that holds state relevant. |
| [`CopyFileDetection`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerruncopyfiledetection) | Create a collection of name/value pairs. |
| [`DefaultImages`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrundefaultimages) | We may want to load the default images from remote - maybe s3 location etc?. |
| [`DynamicEntityLaunchCommand`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrundynamicentitylaunchcommand) | This is a dynamic command that is created for each launch plan. |
| [`Entities`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunentities) | NamedTuple to group all entities in a file. |
| [`FastPackageOptions`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunfastpackageoptions) | FastPackageOptions is used to set configuration options when packaging files. |
| [`FastSerializationSettings`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunfastserializationsettings) | This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`FileAccessProvider`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunfileaccessprovider) | This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`FlyteContext`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteContextManager`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`FlyteLaunchPlan`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunflytelaunchplan) | A class encapsulating a remote Flyte launch plan. |
| [`FlyteLiteralConverter`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunflyteliteralconverter) | None. |
| [`FlyteRemote`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunflyteremote) | Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`FlyteTask`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunflytetask) | A class encapsulating a remote Flyte task. |
| [`FlyteWorkflow`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunflyteworkflow) | A class encapsulating a remote Flyte workflow. |
| [`FlyteWorkflowExecution`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunflyteworkflowexecution) | A class encapsulating a workflow execution being run on a Flyte remote backend. |
| [`ImageConfig`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunimageconfig) | We recommend you to use ImageConfig. |
| [`JSONEncoder`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunjsonencoder) | Abstract base class for generic types. |
| [`Labels`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunlabels) | None. |
| [`LaunchPlan`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunlaunchplan) | Launch Plans are one of the core constructs of Flyte. |
| [`Literal`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunliteral) | None. |
| [`Options`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunoptions) | These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`Parameter`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunparameter) | None. |
| [`Progress`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunprogress) | Renders an auto-updating progress bar(s). |
| [`PyFlyteParams`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunpyflyteparams) | None. |
| [`PythonFunctionWorkflow`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunpythonfunctionworkflow) | Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte. |
| [`PythonTask`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunpythontask) | Base Class for all Tasks with a Python native ``Interface``. |
| [`RawOutputDataConfig`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunrawoutputdataconfig) | None. |
| [`RemoteEntityGroup`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunremoteentitygroup) | click multicommand that retrieves launchplans from a remote flyte instance and executes them. |
| [`RunCommand`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunruncommand) | A click command group for registering and executing flyte workflows & tasks in a file. |
| [`RunLevelComputedParams`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunrunlevelcomputedparams) | This class is used to store the computed parameters that are used to run a workflow / task / launchplan. |
| [`RunLevelParams`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunrunlevelparams) | This class is used to store the parameters that are used to run a workflow / task / launchplan. |
| [`SerializationSettings`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunserializationsettings) | These settings are provided while serializing a workflow and task, before registration. |
| [`SimpleType`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunsimpletype) | None. |
| [`TextColumn`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerruntextcolumn) | A column containing text. |
| [`TimeElapsedColumn`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerruntimeelapsedcolumn) | Renders time elapsed. |
| [`TypeEngine`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerruntypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`Variable`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunvariable) | None. |
| [`WorkflowBase`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunworkflowbase) | None. |
| [`WorkflowCommand`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunworkflowcommand) | click multicommand at the python file layer, subcommands should be all the workflows in the file. |
| [`WorkflowExecutionPhase`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunworkflowexecutionphase) | This class holds enum values used for setting notifications. |
| [`YamlFileReadingCommand`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunyamlfilereadingcommand) | Richly formatted click Command. |

### Errors

* [`FlyteEntityNotFoundException`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunflyteentitynotfoundexception)
* [`FlyteSystemException`](.././flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunflytesystemexception)

## flytekit.clis.sdk_in_container.run.Annotations

```python
def Annotations(
    values,
):
```
Annotation values to be applied to a workflow execution resource.



| Parameter | Type |
|-|-|
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| is_empty |  |  |
| values |  |  |

## flytekit.clis.sdk_in_container.run.ArtifactQuery

```python
def ArtifactQuery(
    artifact: Artifact,
    name: str,
    project: Optional[str],
    domain: Optional[str],
    time_partition: Optional[TimePartition],
    partitions: Optional[Partitions],
    tag: Optional[str],
):
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
| [`get_partition_str()`](#get_partition_str) | None |
| [`get_str()`](#get_str) | None |
| [`get_time_partition_str()`](#get_time_partition_str) | None |
| [`to_flyte_idl()`](#to_flyte_idl) | None |


#### get_partition_str()

```python
def get_partition_str(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_str()

```python
def get_str(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_time_partition_str()

```python
def get_time_partition_str(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### to_flyte_idl()

```python
def to_flyte_idl(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| bound |  |  |

## flytekit.clis.sdk_in_container.run.Context

The context is a special internal object that holds state relevant
for the script execution at every single level.  It's normally invisible
to commands unless they opt-in to getting access to it.

The context is useful as it can pass internal objects around and can
control special execution features such as reading data from
environment variables.

A context can be used as context manager in which case it will call
:meth:`close` on teardown.



```python
def Context(
    command: Command,
    parent: typing.Optional[ForwardRef('Context')],
    info_name: typing.Optional[str],
    obj: typing.Optional[typing.Any],
    auto_envvar_prefix: typing.Optional[str],
    default_map: typing.Optional[typing.MutableMapping[str, typing.Any]],
    terminal_width: typing.Optional[int],
    max_content_width: typing.Optional[int],
    resilient_parsing: bool,
    allow_extra_args: typing.Optional[bool],
    allow_interspersed_args: typing.Optional[bool],
    ignore_unknown_options: typing.Optional[bool],
    help_option_names: typing.Optional[typing.List[str]],
    token_normalize_func: typing.Optional[typing.Callable[[str], str]],
    color: typing.Optional[bool],
    show_default: typing.Optional[bool],
):
```
| Parameter | Type |
|-|-|
| `command` | `Command` |
| `parent` | `typing.Optional[ForwardRef('Context')]` |
| `info_name` | `typing.Optional[str]` |
| `obj` | `typing.Optional[typing.Any]` |
| `auto_envvar_prefix` | `typing.Optional[str]` |
| `default_map` | `typing.Optional[typing.MutableMapping[str, typing.Any]]` |
| `terminal_width` | `typing.Optional[int]` |
| `max_content_width` | `typing.Optional[int]` |
| `resilient_parsing` | `bool` |
| `allow_extra_args` | `typing.Optional[bool]` |
| `allow_interspersed_args` | `typing.Optional[bool]` |
| `ignore_unknown_options` | `typing.Optional[bool]` |
| `help_option_names` | `typing.Optional[typing.List[str]]` |
| `token_normalize_func` | `typing.Optional[typing.Callable[[str], str]]` |
| `color` | `typing.Optional[bool]` |
| `show_default` | `typing.Optional[bool]` |

### Methods

| Method | Description |
|-|-|
| [`abort()`](#abort) | Aborts the script |
| [`call_on_close()`](#call_on_close) | Register a function to be called when the context tears down |
| [`close()`](#close) | Invoke all close callbacks registered with |
| [`ensure_object()`](#ensure_object) | Like :meth:`find_object` but sets the innermost object to a |
| [`exit()`](#exit) | Exits the application with a given exit code |
| [`fail()`](#fail) | Aborts the execution of the program with a specific error |
| [`find_object()`](#find_object) | Finds the closest object of a given type |
| [`find_root()`](#find_root) | Finds the outermost context |
| [`forward()`](#forward) | Similar to :meth:`invoke` but fills in default keyword |
| [`get_help()`](#get_help) | Helper method to get formatted help page for the current |
| [`get_parameter_source()`](#get_parameter_source) | Get the source of a parameter |
| [`get_usage()`](#get_usage) | Helper method to get formatted usage string for the current |
| [`invoke()`](#invoke) | Invokes a command callback in exactly the way it expects |
| [`lookup_default()`](#lookup_default) | Get the default for a parameter from :attr:`default_map` |
| [`make_formatter()`](#make_formatter) | Creates the :class:`~click |
| [`scope()`](#scope) | This helper method can be used with the context object to promote |
| [`set_parameter_source()`](#set_parameter_source) | Set the source of a parameter |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating |
| [`with_resource()`](#with_resource) | Register a resource as if it were used in a ``with`` |


#### abort()

```python
def abort()
```
Aborts the script.


#### call_on_close()

```python
def call_on_close(
    f: typing.Callable[..., typing.Any],
):
```
Register a function to be called when the context tears down.

This can be used to close resources opened during the script
execution. Resources that support Python's context manager
protocol which would be used in a ``with`` statement should be
registered with :meth:`with_resource` instead.



| Parameter | Type |
|-|-|
| `f` | `typing.Callable[..., typing.Any]` |

#### close()

```python
def close()
```
Invoke all close callbacks registered with
:meth:`call_on_close`, and exit all context managers entered
with :meth:`with_resource`.


#### ensure_object()

```python
def ensure_object(
    object_type: typing.Type[~V],
):
```
Like :meth:`find_object` but sets the innermost object to a
new instance of `object_type` if it does not exist.


| Parameter | Type |
|-|-|
| `object_type` | `typing.Type[~V]` |

#### exit()

```python
def exit(
    code: int,
):
```
Exits the application with a given exit code.


| Parameter | Type |
|-|-|
| `code` | `int` |

#### fail()

```python
def fail(
    message: str,
):
```
Aborts the execution of the program with a specific error
message.



| Parameter | Type |
|-|-|
| `message` | `str` |

#### find_object()

```python
def find_object(
    object_type: typing.Type[~V],
):
```
Finds the closest object of a given type.


| Parameter | Type |
|-|-|
| `object_type` | `typing.Type[~V]` |

#### find_root()

```python
def find_root()
```
Finds the outermost context.


#### forward()

```python
def forward(
    _Context__self,
    _Context__cmd: Command,
    args: `*args`,
    kwargs: `**kwargs`,
):
```
Similar to :meth:`invoke` but fills in default keyword
arguments from the current context if the other command expects
it.  This cannot invoke callbacks directly, only other commands.

.. versionchanged:: 8.0
All ``kwargs`` are tracked in :attr:`params` so they will be
passed if ``forward`` is called at multiple levels.


| Parameter | Type |
|-|-|
| `_Context__self` |  |
| `_Context__cmd` | `Command` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### get_help()

```python
def get_help()
```
Helper method to get formatted help page for the current
context and command.


#### get_parameter_source()

```python
def get_parameter_source(
    name: str,
):
```
Get the source of a parameter. This indicates the location
from which the value of the parameter was obtained.

This can be useful for determining when a user specified a value
on the command line that is the same as the default value. It
will be :attr:`~click.core.ParameterSource.DEFAULT` only if the
value was actually taken from the default.



| Parameter | Type |
|-|-|
| `name` | `str` |

#### get_usage()

```python
def get_usage()
```
Helper method to get formatted usage string for the current
context and command.


#### invoke()

```python
def invoke(
    _Context__self,
    _Context__callback: typing.Union[ForwardRef('Command'), ForwardRef('t.Callable[..., V]')],
    args: `*args`,
    kwargs: `**kwargs`,
):
```
Invokes a command callback in exactly the way it expects.  There
are two ways to invoke this method:

1.  the first argument can be a callback and all other arguments and
keyword arguments are forwarded directly to the function.
2.  the first argument is a click command object.  In that case all
arguments are forwarded as well but proper click parameters
(options and click arguments) must be keyword arguments and Click
will fill in defaults.

Note that before Click 3.2 keyword arguments were not properly filled
in against the intention of this code and no context was created.  For
more information about this change and why it was done in a bugfix
release see :ref:`upgrade-to-3.2`.

.. versionchanged:: 8.0
All ``kwargs`` are tracked in :attr:`params` so they will be
passed if :meth:`forward` is called at multiple levels.


| Parameter | Type |
|-|-|
| `_Context__self` |  |
| `_Context__callback` | `typing.Union[ForwardRef('Command'), ForwardRef('t.Callable[..., V]')]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### lookup_default()

```python
def lookup_default(
    name: str,
    call: bool,
):
```
Get the default for a parameter from :attr:`default_map`.



| Parameter | Type |
|-|-|
| `name` | `str` |
| `call` | `bool` |

#### make_formatter()

```python
def make_formatter()
```
Creates the :class:`~click.HelpFormatter` for the help and
usage output.

To quickly customize the formatter class used without overriding
this method, set the :attr:`formatter_class` attribute.

.. versionchanged:: 8.0
Added the :attr:`formatter_class` attribute.


#### scope()

```python
def scope(
    cleanup: bool,
):
```
This helper method can be used with the context object to promote
it to the current thread local (see :func:`get_current_context`).
The default behavior of this is to invoke the cleanup functions which
can be disabled by setting `cleanup` to `False`.  The cleanup
functions are typically used for things such as closing file handles.

If the cleanup is intended the context object can also be directly
used as a context manager.

Example usage::

with ctx.scope():
assert get_current_context() is ctx

This is equivalent::

with ctx:
assert get_current_context() is ctx

.. versionadded:: 5.0



| Parameter | Type |
|-|-|
| `cleanup` | `bool` |

#### set_parameter_source()

```python
def set_parameter_source(
    name: str,
    source: <enum 'ParameterSource'>,
):
```
Set the source of a parameter. This indicates the location
from which the value of the parameter was obtained.



| Parameter | Type |
|-|-|
| `name` | `str` |
| `source` | `<enum 'ParameterSource'>` |

#### to_info_dict()

```python
def to_info_dict()
```
Gather information that could be useful for a tool generating
user-facing documentation. This traverses the entire CLI
structure.

.. code-block:: python

with Context(cli) as ctx:
info = ctx.to_info_dict()

.. versionadded:: 8.0


#### with_resource()

```python
def with_resource(
    context_manager: typing.ContextManager[~V],
):
```
Register a resource as if it were used in a ``with``
statement. The resource will be cleaned up when the context is
popped.

Uses :meth:`contextlib.ExitStack.enter_context`. It calls the
resource's ``__enter__()`` method and returns the result. When
the context is popped, it closes the stack, which calls the
resource's ``__exit__()`` method.

To register a cleanup function for something that isn't a
context manager, use :meth:`call_on_close`. Or use something
from :mod:`contextlib` to turn it into a context manager first.

.. code-block:: python

@click.group()
@click.option("--name")
@click.pass_context
def cli(ctx):
ctx.obj = ctx.with_resource(connect_db(name))



| Parameter | Type |
|-|-|
| `context_manager` | `typing.ContextManager[~V]` |

### Properties

| Property | Type | Description |
|-|-|-|
| command_path |  |  |
| meta |  |  |

## flytekit.clis.sdk_in_container.run.CopyFileDetection

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

>>> Color.RED
<Color.RED: 1>

- value lookup:

>>> Color(1)
<Color.RED: 1>

- name lookup:

>>> Color['RED']
<Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


## flytekit.clis.sdk_in_container.run.DefaultImages

We may want to load the default images from remote - maybe s3 location etc?


### Methods

| Method | Description |
|-|-|
| [`default_image()`](#default_image) | None |
| [`find_image_for()`](#find_image_for) | None |
| [`get_version_suffix()`](#get_version_suffix) | None |


#### default_image()

```python
def default_image()
```
#### find_image_for()

```python
def find_image_for(
    python_version: typing.Optional[flytekit.configuration.default_images.PythonVersion],
    flytekit_version: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `python_version` | `typing.Optional[flytekit.configuration.default_images.PythonVersion]` |
| `flytekit_version` | `typing.Optional[str]` |

#### get_version_suffix()

```python
def get_version_suffix()
```
## flytekit.clis.sdk_in_container.run.DynamicEntityLaunchCommand

This is a dynamic command that is created for each launch plan. This is used to execute a launch plan.
It will fetch the launch plan from remote and create parameters from all the inputs of the launch plan.


```python
def DynamicEntityLaunchCommand(
    name: str,
    h: str,
    entity_name: str,
    launcher: str,
    kwargs,
):
```
Create Rich Command instance.


| Parameter | Type |
|-|-|
| `name` | `str` |
| `h` | `str` |
| `entity_name` | `str` |
| `launcher` | `str` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`collect_usage_pieces()`](#collect_usage_pieces) | Returns all the pieces that go into the usage line and returns |
| [`format_epilog()`](#format_epilog) | Writes the epilog into the formatter if it exists |
| [`format_help()`](#format_help) | Writes the help into the formatter if it exists |
| [`format_help_text()`](#format_help_text) | Writes the help text to the formatter if it exists |
| [`format_options()`](#format_options) | Writes all the options into the formatter if they exist |
| [`format_usage()`](#format_usage) | Writes the usage line into the formatter |
| [`get_help()`](#get_help) | Formats the help into a string and returns it |
| [`get_help_option()`](#get_help_option) | Returns the help option object |
| [`get_help_option_names()`](#get_help_option_names) | Returns the names for the help option |
| [`get_params()`](#get_params) | None |
| [`get_short_help_str()`](#get_short_help_str) | Gets short help for the command or makes it by shortening the |
| [`get_usage()`](#get_usage) | Formats the usage line into a string and returns it |
| [`invoke()`](#invoke) | Default or None values should be ignored |
| [`main()`](#main) | This is the way to invoke a script with all the bells and |
| [`make_context()`](#make_context) | This function when given an info name and arguments will kick |
| [`make_parser()`](#make_parser) | Creates the underlying option parser for this command |
| [`parse_args()`](#parse_args) | Given a context and a list of arguments this creates the parser |
| [`shell_complete()`](#shell_complete) | Return a list of completions for the incomplete value |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating |


#### collect_usage_pieces()

```python
def collect_usage_pieces(
    ctx: click.core.Context,
):
```
Returns all the pieces that go into the usage line and returns
it as a list of strings.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### format_epilog()

```python
def format_epilog(
    ctx: rich_click.rich_context.RichContext,
    formatter: rich_click.rich_help_formatter.RichHelpFormatter,
):
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
):
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
):
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
):
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
):
```
Writes the usage line into the formatter.

This is a low-level method called by :meth:`get_usage`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `formatter` | `click.formatting.HelpFormatter` |

#### get_help()

```python
def get_help(
    ctx: click.core.Context,
):
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
):
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
):
```
Returns the names for the help option.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_params()

```python
def get_params(
    ctx: click.core.Context,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_short_help_str()

```python
def get_short_help_str(
    limit: int,
):
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
):
```
Formats the usage line into a string and returns it.

Calls :meth:`format_usage` internally.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### invoke()

```python
def invoke(
    ctx: click.core.Context,
):
```
Default or None values should be ignored. Only values that are provided by the user should be passed to the
remote execution.


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
):
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
):
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
):
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
):
```
Given a context and a list of arguments this creates the parser
and parses the arguments, then modifies the context as necessary.
This is automatically invoked by :meth:`make_context`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `args` | ``*args`` |

#### shell_complete()

```python
def shell_complete(
    ctx: click.core.Context,
    incomplete: str,
):
```
Return a list of completions for the incomplete value. Looks
at the names of options and chained multi-commands.



| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `incomplete` | `str` |

#### to_info_dict()

```python
def to_info_dict(
    ctx: click.core.Context,
):
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
| console |  |  |
| help_config |  |  |

## flytekit.clis.sdk_in_container.run.Entities

NamedTuple to group all entities in a file


### Methods

| Method | Description |
|-|-|
| [`all()`](#all) | None |
| [`matching_lp()`](#matching_lp) | Returns the variable name of the launch plan in the file |


#### all()

```python
def all()
```
#### matching_lp()

```python
def matching_lp(
    lp_name: str,
):
```
Returns the variable name of the launch plan in the file


| Parameter | Type |
|-|-|
| `lp_name` | `str` |

## flytekit.clis.sdk_in_container.run.FastPackageOptions

FastPackageOptions is used to set configuration options when packaging files.


```python
def FastPackageOptions(
    ignores: list[Ignore],
    keep_default_ignores: bool,
    copy_style: Optional[CopyFileDetection],
    show_files: bool,
):
```
| Parameter | Type |
|-|-|
| `ignores` | `list[Ignore]` |
| `keep_default_ignores` | `bool` |
| `copy_style` | `Optional[CopyFileDetection]` |
| `show_files` | `bool` |

## flytekit.clis.sdk_in_container.run.FastSerializationSettings

This object hold information about settings necessary to serialize an object so that it can be fast-registered.


```python
def FastSerializationSettings(
    enabled: bool,
    destination_dir: Optional[str],
    distribution_location: Optional[str],
):
```
| Parameter | Type |
|-|-|
| `enabled` | `bool` |
| `destination_dir` | `Optional[str]` |
| `distribution_location` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`schema()`](#schema) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
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
):
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
):
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
):
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
):
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

## flytekit.clis.sdk_in_container.run.FileAccessProvider

This is the class that is available through the FlyteContext and can be used for persisting data to the remote
durable store.


```python
def FileAccessProvider(
    local_sandbox_dir: typing.Union[str, os.PathLike],
    raw_output_prefix: str,
    data_config: typing.Optional[flytekit.configuration.DataConfig],
    execution_metadata: typing.Optional[dict],
):
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
| [`async_get_data()`](#async_get_data) |  |
| [`async_put_data()`](#async_put_data) | The implication here is that we're always going to put data to the remote location, so we  |
| [`async_put_raw_data()`](#async_put_raw_data) | This is a more flexible version of put that accepts a file-like object or a string path |
| [`download()`](#download) | Downloads from remote to local |
| [`download_directory()`](#download_directory) | Downloads directory from given remote to local path |
| [`exists()`](#exists) | None |
| [`generate_new_custom_path()`](#generate_new_custom_path) | Generates a new path with the raw output prefix and a random string appended to it |
| [`get()`](#get) | None |
| [`get_async_filesystem_for_path()`](#get_async_filesystem_for_path) | None |
| [`get_data()`](#get_data) |  |
| [`get_file_tail()`](#get_file_tail) | None |
| [`get_filesystem()`](#get_filesystem) | None |
| [`get_filesystem_for_path()`](#get_filesystem_for_path) | None |
| [`get_random_local_directory()`](#get_random_local_directory) | None |
| [`get_random_local_path()`](#get_random_local_path) | Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name |
| [`get_random_remote_directory()`](#get_random_remote_directory) | None |
| [`get_random_remote_path()`](#get_random_remote_path) | None |
| [`get_random_string()`](#get_random_string) | None |
| [`is_remote()`](#is_remote) | Deprecated |
| [`join()`](#join) | None |
| [`put_data()`](#put_data) | The implication here is that we're always going to put data to the remote location, so we  |
| [`put_raw_data()`](#put_raw_data) | This is a more flexible version of put that accepts a file-like object or a string path |
| [`recursive_paths()`](#recursive_paths) | None |
| [`sep()`](#sep) | None |
| [`strip_file_header()`](#strip_file_header) | Drops file:// if it exists from the file |
| [`upload()`](#upload) |  |
| [`upload_directory()`](#upload_directory) |  |


#### async_get_data()

```python
def async_get_data(
    remote_path: str,
    local_path: str,
    is_multipart: bool,
    kwargs,
):
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
):
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
    lpath: typing.Union[str, os.PathLike, pathlib.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO],
    upload_prefix: typing.Optional[str],
    file_name: typing.Optional[str],
    read_chunk_size_bytes: int,
    encoding: str,
    skip_raw_data_prefix: bool,
    kwargs,
):
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
| `lpath` | `typing.Union[str, os.PathLike, pathlib.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO]` |
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
    lpath: typing.Union[str, os.PathLike, pathlib.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO],
    upload_prefix: typing.Optional[str],
    file_name: typing.Optional[str],
    read_chunk_size_bytes: int,
    encoding: str,
    skip_raw_data_prefix: bool,
    kwargs,
):
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
| `lpath` | `typing.Union[str, os.PathLike, pathlib.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO]` |
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
):
```
| Parameter | Type |
|-|-|
| `f` | `str` |
| `t` | `str` |

#### sep()

```python
def sep(
    file_system: typing.Optional[fsspec.spec.AbstractFileSystem],
):
```
| Parameter | Type |
|-|-|
| `file_system` | `typing.Optional[fsspec.spec.AbstractFileSystem]` |

#### strip_file_header()

```python
def strip_file_header(
    path: str,
    trim_trailing_sep: bool,
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `local_path` | `str` |
| `remote_path` | `str` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| data_config |  |  |
| local_access |  |  |
| local_sandbox_dir |  |  |
| raw_output_fs |  |  |
| raw_output_prefix |  |  |

## flytekit.clis.sdk_in_container.run.FlyteContext

This is an internal-facing context object, that most users will not have to deal with. It's essentially a globally
available grab bag of settings and objects that allows flytekit to do things like convert complex types, run and
compile workflows, serialize Flyte entities, etc.

Even though this object as a ``current_context`` function on it, it should not be called directly. Please use the
:py:class:`flytekit.FlyteContextManager` object instead.

Please do not confuse this object with the :py:class:`flytekit.ExecutionParameters` object.


```python
def FlyteContext(
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
):
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
| [`current_context()`](#current_context) | This method exists only to maintain backwards compatibility |
| [`enter_conditional_section()`](#enter_conditional_section) | None |
| [`get_deck()`](#get_deck) | Returns the deck that was created as part of the last execution |
| [`get_origin_stackframe_repr()`](#get_origin_stackframe_repr) | None |
| [`new_builder()`](#new_builder) | None |
| [`new_compilation_state()`](#new_compilation_state) | Creates and returns a default compilation state |
| [`new_execution_state()`](#new_execution_state) | Creates and returns a new default execution state |
| [`set_stackframe()`](#set_stackframe) | None |
| [`with_client()`](#with_client) | None |
| [`with_compilation_state()`](#with_compilation_state) | None |
| [`with_execution_state()`](#with_execution_state) | None |
| [`with_file_access()`](#with_file_access) | None |
| [`with_new_compilation_state()`](#with_new_compilation_state) | None |
| [`with_output_metadata_tracker()`](#with_output_metadata_tracker) | None |
| [`with_serialization_settings()`](#with_serialization_settings) | None |
| [`with_worker_queue()`](#with_worker_queue) | None |


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
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `s` | `traceback.FrameSummary` |

#### with_client()

```python
def with_client(
    c: SynchronousFlyteClient,
):
```
| Parameter | Type |
|-|-|
| `c` | `SynchronousFlyteClient` |

#### with_compilation_state()

```python
def with_compilation_state(
    c: CompilationState,
):
```
| Parameter | Type |
|-|-|
| `c` | `CompilationState` |

#### with_execution_state()

```python
def with_execution_state(
    es: ExecutionState,
):
```
| Parameter | Type |
|-|-|
| `es` | `ExecutionState` |

#### with_file_access()

```python
def with_file_access(
    fa: FileAccessProvider,
):
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
):
```
| Parameter | Type |
|-|-|
| `t` | `OutputMetadataTracker` |

#### with_serialization_settings()

```python
def with_serialization_settings(
    ss: SerializationSettings,
):
```
| Parameter | Type |
|-|-|
| `ss` | `SerializationSettings` |

#### with_worker_queue()

```python
def with_worker_queue(
    wq: Controller,
):
```
| Parameter | Type |
|-|-|
| `wq` | `Controller` |

### Properties

| Property | Type | Description |
|-|-|-|
| user_space_params |  |  |

## flytekit.clis.sdk_in_container.run.FlyteContextManager

FlyteContextManager manages the execution context within Flytekit. It holds global state of either compilation
or Execution. It is not thread-safe and can only be run as a single threaded application currently.
Context's within Flytekit is useful to manage compilation state and execution state. Refer to ``CompilationState``
and ``ExecutionState`` for more information. FlyteContextManager provides a singleton stack to manage these contexts.

Typical usage is

.. code-block:: python

FlyteContextManager.initialize()
with FlyteContextManager.with_context(o) as ctx:
pass

# If required - not recommended you can use
FlyteContextManager.push_context()
# but correspondingly a pop_context should be called
FlyteContextManager.pop_context()


### Methods

| Method | Description |
|-|-|
| [`add_signal_handler()`](#add_signal_handler) | None |
| [`current_context()`](#current_context) | None |
| [`get_origin_stackframe()`](#get_origin_stackframe) | None |
| [`initialize()`](#initialize) | Re-initializes the context and erases the entire context |
| [`pop_context()`](#pop_context) | None |
| [`push_context()`](#push_context) | None |
| [`size()`](#size) | None |
| [`with_context()`](#with_context) | None |


#### add_signal_handler()

```python
def add_signal_handler(
    handler: typing.Callable[[int, FrameType], typing.Any],
):
```
| Parameter | Type |
|-|-|
| `handler` | `typing.Callable[[int, FrameType], typing.Any]` |

#### current_context()

```python
def current_context()
```
#### get_origin_stackframe()

```python
def get_origin_stackframe(
    limit,
):
```
| Parameter | Type |
|-|-|
| `limit` |  |

#### initialize()

```python
def initialize()
```
Re-initializes the context and erases the entire context


#### pop_context()

```python
def pop_context()
```
#### push_context()

```python
def push_context(
    ctx: FlyteContext,
    f: Optional[traceback.FrameSummary],
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `f` | `Optional[traceback.FrameSummary]` |

#### size()

```python
def size()
```
#### with_context()

```python
def with_context(
    b: FlyteContext.Builder,
):
```
| Parameter | Type |
|-|-|
| `b` | `FlyteContext.Builder` |

## flytekit.clis.sdk_in_container.run.FlyteEntityNotFoundException

Inappropriate argument value (of correct type).


```python
def FlyteEntityNotFoundException(
    module_name: str,
    entity_name: str,
):
```
| Parameter | Type |
|-|-|
| `module_name` | `str` |
| `entity_name` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.clis.sdk_in_container.run.FlyteLaunchPlan

A class encapsulating a remote Flyte launch plan.


```python
def FlyteLaunchPlan(
    id,
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `id` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | None |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`execute()`](#execute) | None |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`local_execute()`](#local_execute) | None |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### compile()

```python
def compile(
    ctx: FlyteContext,
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### execute()

```python
def execute(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2,
):
```
| Parameter | Type |
|-|-|
| `pb2` |  |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### promote_from_model()

```python
def promote_from_model(
    id: id_models.Identifier,
    model: _launch_plan_models.LaunchPlanSpec,
):
```
| Parameter | Type |
|-|-|
| `id` | `id_models.Identifier` |
| `model` | `_launch_plan_models.LaunchPlanSpec` |

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
| annotations |  |  |
| auth_role |  |  |
| default_inputs |  |  |
| entity_metadata |  |  |
| entity_type_text |  |  |
| fixed_inputs |  |  |
| flyte_workflow |  |  |
| id |  |  |
| interface |  |  |
| is_empty |  |  |
| is_scheduled |  |  |
| labels |  |  |
| max_parallelism |  |  |
| name |  |  |
| overwrite_cache |  |  |
| python_interface |  |  |
| raw_output_data_config |  |  |
| resource_type |  |  |
| security_context |  |  |
| workflow_id |  |  |

## flytekit.clis.sdk_in_container.run.FlyteLiteralConverter

```python
def FlyteLiteralConverter(
    flyte_ctx: flytekit.core.context_manager.FlyteContext,
    literal_type: flytekit.models.types.LiteralType,
    python_type: typing.Type,
    is_remote: bool,
):
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
| [`convert()`](#convert) | Convert the value to a Flyte Literal or a python native type |
| [`is_bool()`](#is_bool) | None |


#### convert()

```python
def convert(
    ctx: click.core.Context,
    param: typing.Optional[click.core.Parameter],
    value: typing.Any,
):
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
| click_type |  |  |

## flytekit.clis.sdk_in_container.run.FlyteRemote

Main entrypoint for programmatically accessing a Flyte remote backend.

The term 'remote' is synonymous with 'backend' or 'deployment' and refers to a hosted instance of the
Flyte platform, which comes with a Flyte Admin server on some known URI.


```python
def FlyteRemote(
    config: Config,
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: typing.Optional[bool],
    kwargs,
):
```
Initialize a FlyteRemote object.

:type kwargs: All arguments that can be passed to create the SynchronousFlyteClient. These are usually grpc
parameters, if you want to customize credentials, ssl handling etc.


| Parameter | Type |
|-|-|
| `config` | `Config` |
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `typing.Optional[bool]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`activate_launchplan()`](#activate_launchplan) | Given a launchplan, activate it, all previous versions are deactivated |
| [`approve()`](#approve) |  |
| [`auto()`](#auto) | None |
| [`download()`](#download) | Download the data to the specified location |
| [`execute()`](#execute) | Execute a task, workflow, or launchplan, either something that's been declared locally, or a fetched entity |
| [`execute_local_launch_plan()`](#execute_local_launch_plan) | Execute a locally defined `LaunchPlan` |
| [`execute_local_task()`](#execute_local_task) | Execute a @task-decorated function or TaskTemplate task |
| [`execute_local_workflow()`](#execute_local_workflow) | Execute an @workflow decorated function |
| [`execute_reference_launch_plan()`](#execute_reference_launch_plan) | Execute a ReferenceLaunchPlan |
| [`execute_reference_task()`](#execute_reference_task) | Execute a ReferenceTask |
| [`execute_reference_workflow()`](#execute_reference_workflow) | Execute a ReferenceWorkflow |
| [`execute_remote_task_lp()`](#execute_remote_task_lp) | Execute a FlyteTask, or FlyteLaunchplan |
| [`execute_remote_wf()`](#execute_remote_wf) | Execute a FlyteWorkflow |
| [`fast_package()`](#fast_package) | Packages the given paths into an installable zip and returns the md5_bytes and the URL of the uploaded location |
| [`fast_register_workflow()`](#fast_register_workflow) | Use this method to register a workflow with zip mode |
| [`fetch_active_launchplan()`](#fetch_active_launchplan) | Returns the active version of the launch plan if it exists or returns None |
| [`fetch_execution()`](#fetch_execution) | Fetch a workflow execution entity from flyte admin |
| [`fetch_launch_plan()`](#fetch_launch_plan) | Fetch a launchplan entity from flyte admin |
| [`fetch_task()`](#fetch_task) | Fetch a task entity from flyte admin |
| [`fetch_task_lazy()`](#fetch_task_lazy) | Similar to fetch_task, just that it returns a LazyEntity, which will fetch the workflow lazily |
| [`fetch_workflow()`](#fetch_workflow) | Fetch a workflow entity from flyte admin |
| [`fetch_workflow_lazy()`](#fetch_workflow_lazy) | Similar to fetch_workflow, just that it returns a LazyEntity, which will fetch the workflow lazily |
| [`find_launch_plan()`](#find_launch_plan) | None |
| [`find_launch_plan_for_node()`](#find_launch_plan_for_node) | None |
| [`for_endpoint()`](#for_endpoint) | None |
| [`for_sandbox()`](#for_sandbox) | None |
| [`generate_console_http_domain()`](#generate_console_http_domain) | This should generate the domain where console is hosted |
| [`generate_console_url()`](#generate_console_url) | Generate a Flyteconsole URL for the given Flyte remote endpoint |
| [`get()`](#get) | General function that works with flyte tiny urls |
| [`get_domains()`](#get_domains) | Lists registered domains from flyte admin |
| [`get_execution_metrics()`](#get_execution_metrics) | Get the metrics for a given execution |
| [`get_extra_headers_for_protocol()`](#get_extra_headers_for_protocol) | None |
| [`launch_backfill()`](#launch_backfill) | Creates and launches a backfill workflow for the given launchplan |
| [`list_projects()`](#list_projects) | Lists registered projects from flyte admin |
| [`list_signals()`](#list_signals) |  |
| [`list_tasks_by_version()`](#list_tasks_by_version) | None |
| [`raw_register()`](#raw_register) | Raw register method, can be used to register control plane entities |
| [`recent_executions()`](#recent_executions) | None |
| [`register_launch_plan()`](#register_launch_plan) | Register a given launchplan, possibly applying overrides from the provided options |
| [`register_script()`](#register_script) | Use this method to register a workflow via script mode |
| [`register_task()`](#register_task) | Register a qualified task (PythonTask) with Remote |
| [`register_workflow()`](#register_workflow) | Use this method to register a workflow |
| [`reject()`](#reject) |  |
| [`remote_context()`](#remote_context) | Context manager with remote-specific configuration |
| [`set_input()`](#set_input) |  |
| [`set_signal()`](#set_signal) |  |
| [`sync()`](#sync) | This function was previously a singledispatchmethod |
| [`sync_execution()`](#sync_execution) | Sync a FlyteWorkflowExecution object with its corresponding remote state |
| [`sync_node_execution()`](#sync_node_execution) | Get data backing a node execution |
| [`sync_task_execution()`](#sync_task_execution) | Sync a FlyteTaskExecution object with its corresponding remote state |
| [`terminate()`](#terminate) | Terminate a workflow execution |
| [`upload_file()`](#upload_file) | Function will use remote's client to hash and then upload the file using Admin's data proxy service |
| [`wait()`](#wait) | Wait for an execution to finish |


#### activate_launchplan()

```python
def activate_launchplan(
    ident: Identifier,
):
```
Given a launchplan, activate it, all previous versions are deactivated.


| Parameter | Type |
|-|-|
| `ident` | `Identifier` |

#### approve()

```python
def approve(
    signal_id: str,
    execution_name: str,
    project: str,
    domain: str,
):
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `project` | `str` |
| `domain` | `str` |

#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `bool` |
| `kwargs` | ``**kwargs`` |

#### download()

```python
def download(
    data: typing.Union[LiteralsResolver, Literal, LiteralMap],
    download_to: str,
    recursive: bool,
):
```
Download the data to the specified location. If the data is a LiteralsResolver, LiteralMap and if recursive is
specified, then all file like objects will be recursively downloaded (e.g. FlyteFile/Dir (blob),
StructuredDataset etc).

Note: That it will use your sessions credentials to access the remote location. For sandbox, this should be
automatically configured, assuming you are running sandbox locally. For other environments, you will need to
configure your credentials appropriately.



| Parameter | Type |
|-|-|
| `data` | `typing.Union[LiteralsResolver, Literal, LiteralMap]` |
| `download_to` | `str` |
| `recursive` | `bool` |

#### execute()

```python
def execute(
    entity: typing.Union[FlyteTask, FlyteLaunchPlan, FlyteWorkflow, PythonTask, WorkflowBase, LaunchPlan, ReferenceEntity],
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    name: str,
    version: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    image_config: typing.Optional[ImageConfig],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    serialization_settings: typing.Optional[SerializationSettings],
):
```
Execute a task, workflow, or launchplan, either something that's been declared locally, or a fetched entity.

This method supports:
- ``Flyte{Task, Workflow, LaunchPlan}`` remote module objects.
- ``@task``-decorated functions and ``TaskTemplate`` tasks.
- ``@workflow``-decorated functions.
- ``LaunchPlan`` objects.

For local entities, this code will attempt to find the entity first, and if missing, will compile and register
the object.

Not all arguments are relevant in all circumstances. For example, there's no reason to use the serialization
settings for entities that have already been registered on Admin.



| Parameter | Type |
|-|-|
| `entity` | `typing.Union[FlyteTask, FlyteLaunchPlan, FlyteWorkflow, PythonTask, WorkflowBase, LaunchPlan, ReferenceEntity]` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_local_launch_plan()

```python
def execute_local_launch_plan(
    entity: LaunchPlan,
    inputs: typing.Dict[str, typing.Any],
    version: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    name: typing.Optional[str],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    serialization_settings: typing.Optional[SerializationSettings],
):
```
Execute a locally defined `LaunchPlan`.



| Parameter | Type |
|-|-|
| `entity` | `LaunchPlan` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `version` | `str` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `name` | `typing.Optional[str]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_local_task()

```python
def execute_local_task(
    entity: PythonTask,
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    name: str,
    version: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    image_config: typing.Optional[ImageConfig],
    wait: bool,
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    options: typing.Optional[Options],
    serialization_settings: typing.Optional[SerializationSettings],
):
```
Execute a @task-decorated function or TaskTemplate task.



| Parameter | Type |
|-|-|
| `entity` | `PythonTask` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `wait` | `bool` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_local_workflow()

```python
def execute_local_workflow(
    entity: WorkflowBase,
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    name: str,
    version: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    image_config: typing.Optional[ImageConfig],
    options: typing.Optional[Options],
    wait: bool,
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    serialization_settings: typing.Optional[SerializationSettings],
):
```
Execute an @workflow decorated function.



| Parameter | Type |
|-|-|
| `entity` | `WorkflowBase` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_reference_launch_plan()

```python
def execute_reference_launch_plan(
    entity: ReferenceLaunchPlan,
    inputs: typing.Dict[str, typing.Any],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
):
```
Execute a ReferenceLaunchPlan.


| Parameter | Type |
|-|-|
| `entity` | `ReferenceLaunchPlan` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_reference_task()

```python
def execute_reference_task(
    entity: ReferenceTask,
    inputs: typing.Dict[str, typing.Any],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
):
```
Execute a ReferenceTask.


| Parameter | Type |
|-|-|
| `entity` | `ReferenceTask` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_reference_workflow()

```python
def execute_reference_workflow(
    entity: ReferenceWorkflow,
    inputs: typing.Dict[str, typing.Any],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
):
```
Execute a ReferenceWorkflow.


| Parameter | Type |
|-|-|
| `entity` | `ReferenceWorkflow` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_remote_task_lp()

```python
def execute_remote_task_lp(
    entity: typing.Union[FlyteTask, FlyteLaunchPlan],
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
):
```
Execute a FlyteTask, or FlyteLaunchplan.

NOTE: the name and version arguments are currently not used and only there consistency in the function signature


| Parameter | Type |
|-|-|
| `entity` | `typing.Union[FlyteTask, FlyteLaunchPlan]` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_remote_wf()

```python
def execute_remote_wf(
    entity: FlyteWorkflow,
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
):
```
Execute a FlyteWorkflow.

NOTE: the name and version arguments are currently not used and only there consistency in the function signature


| Parameter | Type |
|-|-|
| `entity` | `FlyteWorkflow` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### fast_package()

```python
def fast_package(
    root: os.PathLike,
    deref_symlinks: bool,
    output: str,
    options: typing.Optional[FastPackageOptions],
):
```
Packages the given paths into an installable zip and returns the md5_bytes and the URL of the uploaded location


| Parameter | Type |
|-|-|
| `root` | `os.PathLike` |
| `deref_symlinks` | `bool` |
| `output` | `str` |
| `options` | `typing.Optional[FastPackageOptions]` |

#### fast_register_workflow()

```python
def fast_register_workflow(
    entity: WorkflowBase,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
    default_launch_plan: typing.Optional[bool],
    options: typing.Optional[Options],
    fast_package_options: typing.Optional[FastPackageOptions],
):
```
Use this method to register a workflow with zip mode.


| Parameter | Type |
|-|-|
| `entity` | `WorkflowBase` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |
| `version` | `typing.Optional[str]` |
| `default_launch_plan` | `typing.Optional[bool]` |
| `options` | `typing.Optional[Options]` |
| `fast_package_options` | `typing.Optional[FastPackageOptions]` |

#### fetch_active_launchplan()

```python
def fetch_active_launchplan(
    project: str,
    domain: str,
    name: str,
):
```
Returns the active version of the launch plan if it exists or returns None


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |

#### fetch_execution()

```python
def fetch_execution(
    project: str,
    domain: str,
    name: str,
):
```
Fetch a workflow execution entity from flyte admin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |

#### fetch_launch_plan()

```python
def fetch_launch_plan(
    project: str,
    domain: str,
    name: str,
    version: str,
):
```
Fetch a launchplan entity from flyte admin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_task()

```python
def fetch_task(
    project: str,
    domain: str,
    name: str,
    version: str,
):
```
Fetch a task entity from flyte admin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_task_lazy()

```python
def fetch_task_lazy(
    project: str,
    domain: str,
    name: str,
    version: str,
):
```
Similar to fetch_task, just that it returns a LazyEntity, which will fetch the workflow lazily.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_workflow()

```python
def fetch_workflow(
    project: str,
    domain: str,
    name: str,
    version: str,
):
```
Fetch a workflow entity from flyte admin.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_workflow_lazy()

```python
def fetch_workflow_lazy(
    project: str,
    domain: str,
    name: str,
    version: str,
):
```
Similar to fetch_workflow, just that it returns a LazyEntity, which will fetch the workflow lazily.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### find_launch_plan()

```python
def find_launch_plan(
    lp_ref: id_models,
    node_launch_plans: Dict[id_models, launch_plan_models.LaunchPlanSpec],
):
```
| Parameter | Type |
|-|-|
| `lp_ref` | `id_models` |
| `node_launch_plans` | `Dict[id_models, launch_plan_models.LaunchPlanSpec]` |

#### find_launch_plan_for_node()

```python
def find_launch_plan_for_node(
    node: Node,
    node_launch_plans: Dict[id_models, launch_plan_models.LaunchPlanSpec],
):
```
| Parameter | Type |
|-|-|
| `node` | `Node` |
| `node_launch_plans` | `Dict[id_models, launch_plan_models.LaunchPlanSpec]` |

#### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
    data_config: typing.Optional[DataConfig],
    config_file: typing.Union[str, ConfigFile],
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |
| `data_config` | `typing.Optional[DataConfig]` |
| `config_file` | `typing.Union[str, ConfigFile]` |
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `bool` |
| `kwargs` | ``**kwargs`` |

#### for_sandbox()

```python
def for_sandbox(
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `bool` |
| `kwargs` | ``**kwargs`` |

#### generate_console_http_domain()

```python
def generate_console_http_domain()
```
This should generate the domain where console is hosted.

:return:


#### generate_console_url()

```python
def generate_console_url(
    entity: typing.Union[FlyteWorkflowExecution, FlyteNodeExecution, FlyteTaskExecution, FlyteWorkflow, FlyteTask, WorkflowExecutionIdentifier, Identifier, FlyteLaunchPlan],
):
```
Generate a Flyteconsole URL for the given Flyte remote endpoint.
This will automatically determine if this is an execution or an entity and change the type automatically


| Parameter | Type |
|-|-|
| `entity` | `typing.Union[FlyteWorkflowExecution, FlyteNodeExecution, FlyteTaskExecution, FlyteWorkflow, FlyteTask, WorkflowExecutionIdentifier, Identifier, FlyteLaunchPlan]` |

#### get()

```python
def get(
    flyte_uri: typing.Optional[str],
):
```
General function that works with flyte tiny urls. This can return outputs (in the form of LiteralsResolver, or
individual Literals for singular requests), or HTML if passed a deck link, or bytes containing HTML,
if ipython is not available locally.


| Parameter | Type |
|-|-|
| `flyte_uri` | `typing.Optional[str]` |

#### get_domains()

```python
def get_domains()
```
Lists registered domains from flyte admin.

:returns: typing.List[flytekit.models.domain.Domain]


#### get_execution_metrics()

```python
def get_execution_metrics(
    id: WorkflowExecutionIdentifier,
    depth: int,
):
```
Get the metrics for a given execution.


| Parameter | Type |
|-|-|
| `id` | `WorkflowExecutionIdentifier` |
| `depth` | `int` |

#### get_extra_headers_for_protocol()

```python
def get_extra_headers_for_protocol(
    native_url,
):
```
| Parameter | Type |
|-|-|
| `native_url` |  |

#### launch_backfill()

```python
def launch_backfill(
    project: str,
    domain: str,
    from_date: datetime,
    to_date: datetime,
    launchplan: str,
    launchplan_version: str,
    execution_name: str,
    version: str,
    dry_run: bool,
    execute: bool,
    parallel: bool,
    failure_policy: typing.Optional[WorkflowFailurePolicy],
    overwrite_cache: typing.Optional[bool],
):
```
Creates and launches a backfill workflow for the given launchplan. If launchplan version is not specified,
then the latest launchplan is retrieved.
The from_date is exclusive and end_date is inclusive and backfill run for all instances in between. ::
-> (start_date - exclusive, end_date inclusive)

If dry_run is specified, the workflow is created and returned.
If execute==False is specified then the workflow is created and registered.
In the last case, the workflow is created, registered and executed.

The `parallel` flag can be used to generate a workflow where all launchplans can be run in parallel. Default
is that execute backfill is run sequentially



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `from_date` | `datetime` |
| `to_date` | `datetime` |
| `launchplan` | `str` |
| `launchplan_version` | `str` |
| `execution_name` | `str` |
| `version` | `str` |
| `dry_run` | `bool` |
| `execute` | `bool` |
| `parallel` | `bool` |
| `failure_policy` | `typing.Optional[WorkflowFailurePolicy]` |
| `overwrite_cache` | `typing.Optional[bool]` |

#### list_projects()

```python
def list_projects(
    limit: typing.Optional[int],
    filters: typing.Optional[typing.List[filter_models.Filter]],
    sort_by: typing.Optional[admin_common_models.Sort],
):
```
Lists registered projects from flyte admin.



| Parameter | Type |
|-|-|
| `limit` | `typing.Optional[int]` |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` |
| `sort_by` | `typing.Optional[admin_common_models.Sort]` |

#### list_signals()

```python
def list_signals(
    execution_name: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: int,
    filters: typing.Optional[typing.List[filter_models.Filter]],
):
```
| Parameter | Type |
|-|-|
| `execution_name` | `str` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `limit` | `int` |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` |

#### list_tasks_by_version()

```python
def list_tasks_by_version(
    version: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: typing.Optional[int],
):
```
| Parameter | Type |
|-|-|
| `version` | `str` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `limit` | `typing.Optional[int]` |

#### raw_register()

```python
def raw_register(
    cp_entity: FlyteControlPlaneEntity,
    settings: SerializationSettings,
    version: str,
    create_default_launchplan: bool,
    options: Options,
    og_entity: FlyteLocalEntity,
):
```
Raw register method, can be used to register control plane entities. Usually if you have a Flyte Entity like a
WorkflowBase, Task, LaunchPlan then use other methods. This should be used only if you have already serialized entities



| Parameter | Type |
|-|-|
| `cp_entity` | `FlyteControlPlaneEntity` |
| `settings` | `SerializationSettings` |
| `version` | `str` |
| `create_default_launchplan` | `bool` |
| `options` | `Options` |
| `og_entity` | `FlyteLocalEntity` |

#### recent_executions()

```python
def recent_executions(
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: typing.Optional[int],
    filters: typing.Optional[typing.List[filter_models.Filter]],
):
```
| Parameter | Type |
|-|-|
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `limit` | `typing.Optional[int]` |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` |

#### register_launch_plan()

```python
def register_launch_plan(
    entity: LaunchPlan,
    version: typing.Optional[str],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    options: typing.Optional[Options],
    serialization_settings: typing.Optional[SerializationSettings],
):
```
Register a given launchplan, possibly applying overrides from the provided options. If the underlying workflow
is not already registered, it, along with any underlying entities, will also be registered. If the underlying
workflow does exist (with the given project/domain/version), then only the launchplan will be registered.



| Parameter | Type |
|-|-|
| `entity` | `LaunchPlan` |
| `version` | `typing.Optional[str]` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### register_script()

```python
def register_script(
    entity: typing.Union[WorkflowBase, PythonTask, LaunchPlan],
    image_config: typing.Optional[ImageConfig],
    version: typing.Optional[str],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    destination_dir: str,
    copy_all: bool,
    default_launch_plan: bool,
    options: typing.Optional[Options],
    source_path: typing.Optional[str],
    module_name: typing.Optional[str],
    envs: typing.Optional[typing.Dict[str, str]],
    fast_package_options: typing.Optional[FastPackageOptions],
):
```
Use this method to register a workflow via script mode.


| Parameter | Type |
|-|-|
| `entity` | `typing.Union[WorkflowBase, PythonTask, LaunchPlan]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `version` | `typing.Optional[str]` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `destination_dir` | `str` |
| `copy_all` | `bool` |
| `default_launch_plan` | `bool` |
| `options` | `typing.Optional[Options]` |
| `source_path` | `typing.Optional[str]` |
| `module_name` | `typing.Optional[str]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `fast_package_options` | `typing.Optional[FastPackageOptions]` |

#### register_task()

```python
def register_task(
    entity: PythonTask,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
):
```
Register a qualified task (PythonTask) with Remote
For any conflicting parameters method arguments are regarded as overrides



| Parameter | Type |
|-|-|
| `entity` | `PythonTask` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |
| `version` | `typing.Optional[str]` |

#### register_workflow()

```python
def register_workflow(
    entity: WorkflowBase,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
    default_launch_plan: typing.Optional[bool],
    options: typing.Optional[Options],
):
```
Use this method to register a workflow.


| Parameter | Type |
|-|-|
| `entity` | `WorkflowBase` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |
| `version` | `typing.Optional[str]` |
| `default_launch_plan` | `typing.Optional[bool]` |
| `options` | `typing.Optional[Options]` |

#### reject()

```python
def reject(
    signal_id: str,
    execution_name: str,
    project: str,
    domain: str,
):
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `project` | `str` |
| `domain` | `str` |

#### remote_context()

```python
def remote_context()
```
Context manager with remote-specific configuration.


#### set_input()

```python
def set_input(
    signal_id: str,
    execution_name: str,
    value: typing.Union[literal_models.Literal, typing.Any],
    project,
    domain,
    python_type,
    literal_type,
):
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `value` | `typing.Union[literal_models.Literal, typing.Any]` |
| `project` |  |
| `domain` |  |
| `python_type` |  |
| `literal_type` |  |

#### set_signal()

```python
def set_signal(
    signal_id: str,
    execution_name: str,
    value: typing.Union[literal_models.Literal, typing.Any],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    python_type: typing.Optional[typing.Type],
    literal_type: typing.Optional[type_models.LiteralType],
):
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `value` | `typing.Union[literal_models.Literal, typing.Any]` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `python_type` | `typing.Optional[typing.Type]` |
| `literal_type` | `typing.Optional[type_models.LiteralType]` |

#### sync()

```python
def sync(
    execution: FlyteWorkflowExecution,
    entity_definition: typing.Union[FlyteWorkflow, FlyteTask],
    sync_nodes: bool,
):
```
This function was previously a singledispatchmethod. We've removed that but this function remains
so that we don't break people.



| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `entity_definition` | `typing.Union[FlyteWorkflow, FlyteTask]` |
| `sync_nodes` | `bool` |

#### sync_execution()

```python
def sync_execution(
    execution: FlyteWorkflowExecution,
    entity_definition: typing.Union[FlyteWorkflow, FlyteTask],
    sync_nodes: bool,
):
```
Sync a FlyteWorkflowExecution object with its corresponding remote state.


| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `entity_definition` | `typing.Union[FlyteWorkflow, FlyteTask]` |
| `sync_nodes` | `bool` |

#### sync_node_execution()

```python
def sync_node_execution(
    execution: FlyteNodeExecution,
    node_mapping: typing.Dict[str, FlyteNode],
):
```
Get data backing a node execution. These FlyteNodeExecution objects should've come from Admin with the model
fields already populated correctly. For purposes of the remote experience, we'd like to supplement the object
with some additional fields:
- inputs/outputs
- task/workflow executions, and/or underlying node executions in the case of parent nodes
- TypedInterface (remote wrapper type)

A node can have several different types of executions behind it. That is, the node could've run (perhaps
multiple times because of retries):
- A task
- A static subworkflow
- A dynamic subworkflow (which in turn may have run additional tasks, subwfs, and/or launch plans)
- A launch plan

The data model is complicated, so ascertaining which of these happened is a bit tricky. That logic is
encapsulated in this function.


| Parameter | Type |
|-|-|
| `execution` | `FlyteNodeExecution` |
| `node_mapping` | `typing.Dict[str, FlyteNode]` |

#### sync_task_execution()

```python
def sync_task_execution(
    execution: FlyteTaskExecution,
    entity_interface: typing.Optional[TypedInterface],
):
```
Sync a FlyteTaskExecution object with its corresponding remote state.


| Parameter | Type |
|-|-|
| `execution` | `FlyteTaskExecution` |
| `entity_interface` | `typing.Optional[TypedInterface]` |

#### terminate()

```python
def terminate(
    execution: FlyteWorkflowExecution,
    cause: str,
):
```
Terminate a workflow execution.



| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `cause` | `str` |

#### upload_file()

```python
def upload_file(
    to_upload: pathlib.Path,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    filename_root: typing.Optional[str],
):
```
Function will use remote's client to hash and then upload the file using Admin's data proxy service.



| Parameter | Type |
|-|-|
| `to_upload` | `pathlib.Path` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `filename_root` | `typing.Optional[str]` |

#### wait()

```python
def wait(
    execution: FlyteWorkflowExecution,
    timeout: typing.Optional[typing.Union[timedelta, int]],
    poll_interval: typing.Optional[typing.Union[timedelta, int]],
    sync_nodes: bool,
):
```
Wait for an execution to finish.



| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `timeout` | `typing.Optional[typing.Union[timedelta, int]]` |
| `poll_interval` | `typing.Optional[typing.Union[timedelta, int]]` |
| `sync_nodes` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| client |  |  |
| config |  |  |
| context |  |  |
| default_domain |  |  |
| default_project |  |  |
| file_access |  |  |
| interactive_mode_enabled |  |  |

## flytekit.clis.sdk_in_container.run.FlyteSystemException

Common base class for all non-exit exceptions.


```python
def FlyteSystemException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.clis.sdk_in_container.run.FlyteTask

A class encapsulating a remote Flyte task.


```python
def FlyteTask(
    id,
    type,
    metadata,
    interface,
    custom,
    container,
    task_type_version: int,
    security_context,
    config,
    k8s_pod,
    sql,
    extended_resources,
    should_register: bool,
):
```
| Parameter | Type |
|-|-|
| `id` |  |
| `type` |  |
| `metadata` |  |
| `interface` |  |
| `custom` |  |
| `container` |  |
| `task_type_version` | `int` |
| `security_context` |  |
| `config` |  |
| `k8s_pod` |  |
| `sql` |  |
| `extended_resources` |  |
| `should_register` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | None |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`execute()`](#execute) | None |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`local_execute()`](#local_execute) | None |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### execute()

```python
def execute(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### promote_from_model()

```python
def promote_from_model(
    base_model: _task_model.TaskTemplate,
):
```
| Parameter | Type |
|-|-|
| `base_model` | `_task_model.TaskTemplate` |

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
| config |  |  |
| container |  |  |
| custom |  |  |
| docs |  |  |
| entity_type_text |  |  |
| extended_resources |  |  |
| id |  |  |
| interface |  |  |
| is_empty |  |  |
| k8s_pod |  |  |
| metadata |  |  |
| name |  |  |
| python_interface |  |  |
| resource_type |  |  |
| security_context |  |  |
| should_register |  |  |
| sql |  |  |
| task_type_version |  |  |
| template |  |  |
| type |  |  |

## flytekit.clis.sdk_in_container.run.FlyteWorkflow

A class encapsulating a remote Flyte workflow.


```python
def FlyteWorkflow(
    id: id_models.Identifier,
    nodes: List[FlyteNode],
    interface,
    output_bindings,
    metadata,
    metadata_defaults,
    subworkflows: Optional[List[FlyteWorkflow]],
    tasks: Optional[List[FlyteTask]],
    launch_plans: Optional[Dict[id_models.Identifier, launch_plan_models.LaunchPlanSpec]],
    compiled_closure: Optional[compiler_models.CompiledWorkflowClosure],
    should_register: bool,
):
```
| Parameter | Type |
|-|-|
| `id` | `id_models.Identifier` |
| `nodes` | `List[FlyteNode]` |
| `interface` |  |
| `output_bindings` |  |
| `metadata` |  |
| `metadata_defaults` |  |
| `subworkflows` | `Optional[List[FlyteWorkflow]]` |
| `tasks` | `Optional[List[FlyteTask]]` |
| `launch_plans` | `Optional[Dict[id_models.Identifier, launch_plan_models.LaunchPlanSpec]]` |
| `compiled_closure` | `Optional[compiler_models.CompiledWorkflowClosure]` |
| `should_register` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | None |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`execute()`](#execute) | None |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`get_non_system_nodes()`](#get_non_system_nodes) | None |
| [`local_execute()`](#local_execute) | None |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`promote_from_closure()`](#promote_from_closure) | Extracts out the relevant portions of a FlyteWorkflow from a closure from the control plane |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### execute()

```python
def execute(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### get_non_system_nodes()

```python
def get_non_system_nodes(
    nodes: List[_workflow_models.Node],
):
```
| Parameter | Type |
|-|-|
| `nodes` | `List[_workflow_models.Node]` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### promote_from_closure()

```python
def promote_from_closure(
    closure: compiler_models.CompiledWorkflowClosure,
    node_launch_plans: Optional[Dict[id_models, launch_plan_models.LaunchPlanSpec]],
):
```
Extracts out the relevant portions of a FlyteWorkflow from a closure from the control plane.



| Parameter | Type |
|-|-|
| `closure` | `compiler_models.CompiledWorkflowClosure` |
| `node_launch_plans` | `Optional[Dict[id_models, launch_plan_models.LaunchPlanSpec]]` |

#### promote_from_model()

```python
def promote_from_model(
    base_model: _workflow_models.WorkflowTemplate,
    sub_workflows: Optional[Dict[Identifier, _workflow_models.WorkflowTemplate]],
    tasks: Optional[Dict[Identifier, FlyteTask]],
    node_launch_plans: Optional[Dict[Identifier, launch_plan_models.LaunchPlanSpec]],
):
```
| Parameter | Type |
|-|-|
| `base_model` | `_workflow_models.WorkflowTemplate` |
| `sub_workflows` | `Optional[Dict[Identifier, _workflow_models.WorkflowTemplate]]` |
| `tasks` | `Optional[Dict[Identifier, FlyteTask]]` |
| `node_launch_plans` | `Optional[Dict[Identifier, launch_plan_models.LaunchPlanSpec]]` |

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
| docs |  |  |
| entity_type_text |  |  |
| failure_node |  |  |
| flyte_nodes |  |  |
| flyte_sub_workflows |  |  |
| flyte_tasks |  |  |
| id |  |  |
| interface |  |  |
| is_empty |  |  |
| metadata |  |  |
| metadata_defaults |  |  |
| name |  |  |
| nodes |  |  |
| outputs |  |  |
| python_interface |  |  |
| resource_type |  |  |
| should_register |  |  |
| sub_workflows |  |  |
| template |  |  |

## flytekit.clis.sdk_in_container.run.FlyteWorkflowExecution

A class encapsulating a workflow execution being run on a Flyte remote backend.


```python
def FlyteWorkflowExecution(
    type_hints: Optional[Dict[str, typing.Type]],
    remote: Optional['FlyteRemote'],
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `type_hints` | `Optional[Dict[str, typing.Type]]` |
| `remote` | `Optional['FlyteRemote']` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`sync()`](#sync) | Sync the state of the current execution and returns a new object with the updated state |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |
| [`wait()`](#wait) | Wait for the execution to complete |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
):
```
| Parameter | Type |
|-|-|
| `pb` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model: execution_models.Execution,
    remote: Optional['FlyteRemote'],
    type_hints: Optional[Dict[str, typing.Type]],
):
```
| Parameter | Type |
|-|-|
| `base_model` | `execution_models.Execution` |
| `remote` | `Optional['FlyteRemote']` |
| `type_hints` | `Optional[Dict[str, typing.Type]]` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### sync()

```python
def sync(
    sync_nodes: bool,
):
```
Sync the state of the current execution and returns a new object with the updated state.


| Parameter | Type |
|-|-|
| `sync_nodes` | `bool` |

#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
#### wait()

```python
def wait(
    timeout: Optional[Union[timedelta, int]],
    poll_interval: Optional[Union[timedelta, int]],
    sync_nodes: bool,
):
```
Wait for the execution to complete. This is a blocking call.



| Parameter | Type |
|-|-|
| `timeout` | `Optional[Union[timedelta, int]]` |
| `poll_interval` | `Optional[Union[timedelta, int]]` |
| `sync_nodes` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| closure |  |  |
| error |  |  |
| execution_url |  |  |
| flyte_workflow |  |  |
| id |  |  |
| inputs |  |  |
| is_done |  |  |
| is_empty |  |  |
| is_successful |  |  |
| node_executions |  |  |
| outputs |  |  |
| spec |  |  |

## flytekit.clis.sdk_in_container.run.ImageConfig

We recommend you to use ImageConfig.auto(img_name=None) to create an ImageConfig.
For example, ImageConfig.auto(img_name=""ghcr.io/flyteorg/flytecookbook:v1.0.0"") will create an ImageConfig.

ImageConfig holds available images which can be used at registration time. A default image can be specified
along with optional additional images. Each image in the config must have a unique name.

Attributes:
default_image (Optional[Image]): The default image to be used as a container for task serialization.
images (List[Image]): Optional, additional images which can be used in task container definitions.


```python
def ImageConfig(
    default_image: Optional[Image],
    images: Optional[List[Image]],
):
```
| Parameter | Type |
|-|-|
| `default_image` | `Optional[Image]` |
| `images` | `Optional[List[Image]]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from config file or from img_name |
| [`auto_default_image()`](#auto_default_image) | None |
| [`create_from()`](#create_from) | None |
| [`find_image()`](#find_image) | Return an image, by name, if it exists |
| [`from_dict()`](#from_dict) | None |
| [`from_images()`](#from_images) | Allows you to programmatically create an ImageConfig |
| [`from_json()`](#from_json) | None |
| [`schema()`](#schema) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |
| [`validate_image()`](#validate_image) | Validates the image to match the standard format |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
    img_name: Optional[str],
):
```
Reads from config file or from img_name
Note that this function does not take into account the flytekit default images (see the Dockerfiles at the
base of this repo). To pick those up, see the auto_default_image function..



| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile, None]` |
| `img_name` | `Optional[str]` |

#### auto_default_image()

```python
def auto_default_image()
```
#### create_from()

```python
def create_from(
    default_image: Optional[Image],
    other_images: typing.Optional[typing.List[Image]],
):
```
| Parameter | Type |
|-|-|
| `default_image` | `Optional[Image]` |
| `other_images` | `typing.Optional[typing.List[Image]]` |

#### find_image()

```python
def find_image(
    name,
):
```
Return an image, by name, if it exists.


| Parameter | Type |
|-|-|
| `name` |  |

#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_images()

```python
def from_images(
    default_image: str,
    m: typing.Optional[typing.Dict[str, str]],
):
```
Allows you to programmatically create an ImageConfig. Usually only the default_image is required, unless
your workflow uses multiple images

.. code:: python

ImageConfig.from_dict(
"ghcr.io/flyteorg/flytecookbook:v1.0.0",
{
"spark": "ghcr.io/flyteorg/myspark:...",
"other": "...",
}
)

urn:


| Parameter | Type |
|-|-|
| `default_image` | `str` |
| `m` | `typing.Optional[typing.Dict[str, str]]` |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
):
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
):
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
):
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
):
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

#### validate_image()

```python
def validate_image(
    _: typing.Any,
    param: str,
    values: tuple,
):
```
Validates the image to match the standard format. Also validates that only one default image
is provided. a default image, is one that is specified as ``default=<image_uri>`` or just ``<image_uri>``. All
other images should be provided with a name, in the format ``name=<image_uri>`` This method can be used with the
CLI



| Parameter | Type |
|-|-|
| `_` | `typing.Any` |
| `param` | `str` |
| `values` | `tuple` |

## flytekit.clis.sdk_in_container.run.JSONEncoder

Abstract base class for generic types.

On Python 3.12 and newer, generic classes implicitly inherit from
Generic when they declare a parameter list after the class's name::

class Mapping[KT, VT]:
def __getitem__(self, key: KT) -> VT:
...
# Etc.

On older versions of Python, however, generic classes have to
explicitly inherit from Generic.

After a class has been declared to be generic, it can then be used as
follows::

def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
try:
return mapping[key]
except KeyError:
return default


```python
def JSONEncoder(
    shape_type: typing.Union[typing.Type[~T], typing.Any],
    default_dialect: typing.Optional[typing.Type[mashumaro.dialect.Dialect]],
    post_encoder_func: collections.abc.Callable[[typing.Any], str],
):
```
| Parameter | Type |
|-|-|
| `shape_type` | `typing.Union[typing.Type[~T], typing.Any]` |
| `default_dialect` | `typing.Optional[typing.Type[mashumaro.dialect.Dialect]]` |
| `post_encoder_func` | `collections.abc.Callable[[typing.Any], str]` |

### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | None |


#### encode()

```python
def encode(
    obj: ~T,
):
```
| Parameter | Type |
|-|-|
| `obj` | `~T` |

## flytekit.clis.sdk_in_container.run.Labels

```python
def Labels(
    values,
):
```
Label values to be applied to a workflow execution resource.



| Parameter | Type |
|-|-|
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| is_empty |  |  |
| values |  |  |

## flytekit.clis.sdk_in_container.run.LaunchPlan

Launch Plans are one of the core constructs of Flyte. Please take a look at the discussion in the
:std:ref:`core concepts <flyte:divedeep-launchplans>` if you are unfamiliar with them.

Every workflow is registered with a default launch plan, which is just a launch plan with none of the additional
attributes set - no default values, fixed values, schedules, etc. Assuming you have the following workflow

.. code-block:: python

@workflow
def wf(a: int, c: str) -> str:
...

Create the default launch plan with

.. code-block:: python

LaunchPlan.get_or_create(workflow=my_wf)

If you specify additional parameters, you'll also have to give the launch plan a unique name. Default and
fixed inputs can be expressed as Python native values like so:

.. literalinclude:: ../../../tests/flytekit/unit/core/test_launch_plan.py
:start-after: # fixed_and_default_start
:end-before: # fixed_and_default_end
:language: python
:dedent: 4

Additionally, a launch plan can be configured to run on a schedule and emit notifications.


Please see the relevant Schedule and Notification objects as well.

To configure the remaining parameters, you'll need to import the relevant model objects as well.

.. literalinclude:: ../../../tests/flytekit/unit/core/test_launch_plan.py
:start-after: # schedule_start
:end-before: # schedule_end
:language: python
:dedent: 4

.. code-block:: python

from flytekit.models.common import Annotations, AuthRole, Labels, RawOutputDataConfig

Then use as follows

.. literalinclude:: ../../../tests/flytekit/unit/core/test_launch_plan.py
:start-after: # auth_role_start
:end-before: # auth_role_end
:language: python
:dedent: 4


```python
def LaunchPlan(
    name: str,
    workflow: _annotated_workflow.WorkflowBase,
    parameters: _interface_models.ParameterMap,
    fixed_inputs: _literal_models.LiteralMap,
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `parameters` | `_interface_models.ParameterMap` |
| `fixed_inputs` | `_literal_models.LiteralMap` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`clone_with()`](#clone_with) | None |
| [`construct_node_metadata()`](#construct_node_metadata) | None |
| [`create()`](#create) | None |
| [`get_default_launch_plan()`](#get_default_launch_plan) | Users should probably call the get_or_create function defined below instead |
| [`get_or_create()`](#get_or_create) | This function offers a friendlier interface for creating launch plans |


#### clone_with()

```python
def clone_with(
    name: str,
    parameters: Optional[_interface_models.ParameterMap],
    fixed_inputs: Optional[_literal_models.LiteralMap],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `parameters` | `Optional[_interface_models.ParameterMap]` |
| `fixed_inputs` | `Optional[_literal_models.LiteralMap]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### create()

```python
def create(
    name: str,
    workflow: _annotated_workflow.WorkflowBase,
    default_inputs: Optional[Dict[str, Any]],
    fixed_inputs: Optional[Dict[str, Any]],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    auth_role: Optional[_common_models.AuthRole],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `default_inputs` | `Optional[Dict[str, Any]]` |
| `fixed_inputs` | `Optional[Dict[str, Any]]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `auth_role` | `Optional[_common_models.AuthRole]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

#### get_default_launch_plan()

```python
def get_default_launch_plan(
    ctx: FlyteContext,
    workflow: _annotated_workflow.WorkflowBase,
):
```
Users should probably call the get_or_create function defined below instead. A default launch plan is the one
that will just pick up whatever default values are defined in the workflow function signature (if any) and
use the default auth information supplied during serialization, with no notifications or schedules.



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `workflow` | `_annotated_workflow.WorkflowBase` |

#### get_or_create()

```python
def get_or_create(
    workflow: _annotated_workflow.WorkflowBase,
    name: Optional[str],
    default_inputs: Optional[Dict[str, Any]],
    fixed_inputs: Optional[Dict[str, Any]],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    auth_role: Optional[_common_models.AuthRole],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
):
```
This function offers a friendlier interface for creating launch plans. If the name for the launch plan is not
supplied, this assumes you are looking for the default launch plan for the workflow. If it is specified, it
will be used. If creating the default launch plan, none of the other arguments may be specified.

The resulting launch plan is also cached and if called again with the same name, the
cached version is returned



| Parameter | Type |
|-|-|
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `name` | `Optional[str]` |
| `default_inputs` | `Optional[Dict[str, Any]]` |
| `fixed_inputs` | `Optional[Dict[str, Any]]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `auth_role` | `Optional[_common_models.AuthRole]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| annotations |  |  |
| fixed_inputs |  |  |
| interface |  |  |
| labels |  |  |
| max_parallelism |  |  |
| name |  |  |
| notifications |  |  |
| overwrite_cache |  |  |
| parameters |  |  |
| python_interface |  |  |
| raw_output_data_config |  |  |
| saved_inputs |  |  |
| schedule |  |  |
| security_context |  |  |
| should_auto_activate |  |  |
| trigger |  |  |
| workflow |  |  |

## flytekit.clis.sdk_in_container.run.Literal

```python
def Literal(
    scalar: typing.Optional[flytekit.models.literals.Scalar],
    collection: typing.Optional[flytekit.models.literals.LiteralCollection],
    map: typing.Optional[flytekit.models.literals.LiteralMap],
    hash: typing.Optional[str],
    metadata: typing.Optional[typing.Dict[str, str]],
    offloaded_metadata: typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata],
):
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`set_metadata()`](#set_metadata) | Note: This is a mutation on the literal |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.Literal,
):
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
):
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
| collection |  |  |
| hash |  |  |
| is_empty |  |  |
| map |  |  |
| metadata |  |  |
| offloaded_metadata |  |  |
| scalar |  |  |
| value |  |  |

## flytekit.clis.sdk_in_container.run.Options

These are options that can be configured for a launchplan during registration or overridden during an execution.
For instance two people may want to run the same workflow but have the offloaded data stored in two different
buckets. Or you may want labels or annotations to be different. This object is used when launching an execution
in a Flyte backend, and also when registering launch plans.



```python
def Options(
    labels: typing.Optional[flytekit.models.common.Labels],
    annotations: typing.Optional[flytekit.models.common.Annotations],
    raw_output_data_config: typing.Optional[flytekit.models.common.RawOutputDataConfig],
    security_context: typing.Optional[flytekit.models.security.SecurityContext],
    max_parallelism: typing.Optional[int],
    notifications: typing.Optional[typing.List[flytekit.models.common.Notification]],
    disable_notifications: typing.Optional[bool],
    overwrite_cache: typing.Optional[bool],
):
```
| Parameter | Type |
|-|-|
| `labels` | `typing.Optional[flytekit.models.common.Labels]` |
| `annotations` | `typing.Optional[flytekit.models.common.Annotations]` |
| `raw_output_data_config` | `typing.Optional[flytekit.models.common.RawOutputDataConfig]` |
| `security_context` | `typing.Optional[flytekit.models.security.SecurityContext]` |
| `max_parallelism` | `typing.Optional[int]` |
| `notifications` | `typing.Optional[typing.List[flytekit.models.common.Notification]]` |
| `disable_notifications` | `typing.Optional[bool]` |
| `overwrite_cache` | `typing.Optional[bool]` |

### Methods

| Method | Description |
|-|-|
| [`default_from()`](#default_from) | None |


#### default_from()

```python
def default_from(
    k8s_service_account: typing.Optional[str],
    raw_data_prefix: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `k8s_service_account` | `typing.Optional[str]` |
| `raw_data_prefix` | `typing.Optional[str]` |

## flytekit.clis.sdk_in_container.run.Parameter

```python
def Parameter(
    var,
    default,
    required,
    artifact_query: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactQuery],
    artifact_id: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID],
):
```
Declares an input parameter.  A parameter is used as input to a launch plan and has
the special ability to have a default value or mark itself as required.


| Parameter | Type |
|-|-|
| `var` |  |
| `default` |  |
| `required` |  |
| `artifact_query` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactQuery]` |
| `artifact_id` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| artifact_id |  |  |
| artifact_query |  |  |
| behavior |  |  |
| default |  |  |
| is_empty |  |  |
| required |  |  |
| var |  |  |

## flytekit.clis.sdk_in_container.run.Progress

Renders an auto-updating progress bar(s).



```python
def Progress(
    columns: typing.Union[str, rich.progress.ProgressColumn],
    console: typing.Optional[rich.console.Console],
    auto_refresh: bool,
    refresh_per_second: float,
    speed_estimate_period: float,
    transient: bool,
    redirect_stdout: bool,
    redirect_stderr: bool,
    get_time: typing.Optional[typing.Callable[[], float]],
    disable: bool,
    expand: bool,
):
```
| Parameter | Type |
|-|-|
| `columns` | `typing.Union[str, rich.progress.ProgressColumn]` |
| `console` | `typing.Optional[rich.console.Console]` |
| `auto_refresh` | `bool` |
| `refresh_per_second` | `float` |
| `speed_estimate_period` | `float` |
| `transient` | `bool` |
| `redirect_stdout` | `bool` |
| `redirect_stderr` | `bool` |
| `get_time` | `typing.Optional[typing.Callable[[], float]]` |
| `disable` | `bool` |
| `expand` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`add_task()`](#add_task) | Add a new 'task' to the Progress display |
| [`advance()`](#advance) | Advance task by a number of steps |
| [`get_default_columns()`](#get_default_columns) | Get the default columns used for a new Progress instance: |
| [`get_renderable()`](#get_renderable) | Get a renderable for the progress display |
| [`get_renderables()`](#get_renderables) | Get a number of renderables for the progress display |
| [`make_tasks_table()`](#make_tasks_table) | Get a table to render the Progress display |
| [`open()`](#open) | Track progress while reading from a binary file |
| [`refresh()`](#refresh) | Refresh (render) the progress information |
| [`remove_task()`](#remove_task) | Delete a task if it exists |
| [`reset()`](#reset) | Reset a task so completed is 0 and the clock is reset |
| [`start()`](#start) | Start the progress display |
| [`start_task()`](#start_task) | Start a task |
| [`stop()`](#stop) | Stop the progress display |
| [`stop_task()`](#stop_task) | Stop a task |
| [`track()`](#track) | Track progress by iterating over a sequence |
| [`update()`](#update) | Update information associated with a task |
| [`wrap_file()`](#wrap_file) | Track progress file reading from a binary file |


#### add_task()

```python
def add_task(
    description: str,
    start: bool,
    total: typing.Optional[float],
    completed: int,
    visible: bool,
    fields: typing.Any,
):
```
Add a new 'task' to the Progress display.



| Parameter | Type |
|-|-|
| `description` | `str` |
| `start` | `bool` |
| `total` | `typing.Optional[float]` |
| `completed` | `int` |
| `visible` | `bool` |
| `fields` | `typing.Any` |

#### advance()

```python
def advance(
    task_id: rich.progress.TaskID,
    advance: float,
):
```
Advance task by a number of steps.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |
| `advance` | `float` |

#### get_default_columns()

```python
def get_default_columns()
```
Get the default columns used for a new Progress instance:
- a text column for the description (TextColumn)
- the bar itself (BarColumn)
- a text column showing completion percentage (TextColumn)
- an estimated-time-remaining column (TimeRemainingColumn)
If the Progress instance is created without passing a columns argument,
the default columns defined here will be used.

You can also create a Progress instance using custom columns before
and/or after the defaults, as in this example:

progress = Progress(
SpinnerColumn(),
*Progress.get_default_columns(),
"Elapsed:",
TimeElapsedColumn(),
)

This code shows the creation of a Progress display, containing
a spinner to the left, the default columns, and a labeled elapsed
time column.


#### get_renderable()

```python
def get_renderable()
```
Get a renderable for the progress display.


#### get_renderables()

```python
def get_renderables()
```
Get a number of renderables for the progress display.


#### make_tasks_table()

```python
def make_tasks_table(
    tasks: typing.Iterable[rich.progress.Task],
):
```
Get a table to render the Progress display.



| Parameter | Type |
|-|-|
| `tasks` | `typing.Iterable[rich.progress.Task]` |

#### open()

```python
def open(
    file: typing.Union[str, ForwardRef('PathLike[str]'), bytes],
    mode: typing.Union[typing.Literal['rb'], typing.Literal['rt'], typing.Literal['r']],
    buffering: int,
    encoding: typing.Optional[str],
    errors: typing.Optional[str],
    newline: typing.Optional[str],
    total: typing.Optional[int],
    task_id: typing.Optional[rich.progress.TaskID],
    description: str,
):
```
Track progress while reading from a binary file.



| Parameter | Type |
|-|-|
| `file` | `typing.Union[str, ForwardRef('PathLike[str]'), bytes]` |
| `mode` | `typing.Union[typing.Literal['rb'], typing.Literal['rt'], typing.Literal['r']]` |
| `buffering` | `int` |
| `encoding` | `typing.Optional[str]` |
| `errors` | `typing.Optional[str]` |
| `newline` | `typing.Optional[str]` |
| `total` | `typing.Optional[int]` |
| `task_id` | `typing.Optional[rich.progress.TaskID]` |
| `description` | `str` |

#### refresh()

```python
def refresh()
```
Refresh (render) the progress information.


#### remove_task()

```python
def remove_task(
    task_id: rich.progress.TaskID,
):
```
Delete a task if it exists.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |

#### reset()

```python
def reset(
    task_id: rich.progress.TaskID,
    start: bool,
    total: typing.Optional[float],
    completed: int,
    visible: typing.Optional[bool],
    description: typing.Optional[str],
    fields: typing.Any,
):
```
Reset a task so completed is 0 and the clock is reset.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |
| `start` | `bool` |
| `total` | `typing.Optional[float]` |
| `completed` | `int` |
| `visible` | `typing.Optional[bool]` |
| `description` | `typing.Optional[str]` |
| `fields` | `typing.Any` |

#### start()

```python
def start()
```
Start the progress display.


#### start_task()

```python
def start_task(
    task_id: rich.progress.TaskID,
):
```
Start a task.

Starts a task (used when calculating elapsed time). You may need to call this manually,
if you called ``add_task`` with ``start=False``.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |

#### stop()

```python
def stop()
```
Stop the progress display.


#### stop_task()

```python
def stop_task(
    task_id: rich.progress.TaskID,
):
```
Stop a task.

This will freeze the elapsed time on the task.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |

#### track()

```python
def track(
    sequence: typing.Union[typing.Iterable[~ProgressType], typing.Sequence[~ProgressType]],
    total: typing.Optional[float],
    completed: int,
    task_id: typing.Optional[rich.progress.TaskID],
    description: str,
    update_period: float,
):
```
Track progress by iterating over a sequence.



| Parameter | Type |
|-|-|
| `sequence` | `typing.Union[typing.Iterable[~ProgressType], typing.Sequence[~ProgressType]]` |
| `total` | `typing.Optional[float]` |
| `completed` | `int` |
| `task_id` | `typing.Optional[rich.progress.TaskID]` |
| `description` | `str` |
| `update_period` | `float` |

#### update()

```python
def update(
    task_id: rich.progress.TaskID,
    total: typing.Optional[float],
    completed: typing.Optional[float],
    advance: typing.Optional[float],
    description: typing.Optional[str],
    visible: typing.Optional[bool],
    refresh: bool,
    fields: typing.Any,
):
```
Update information associated with a task.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |
| `total` | `typing.Optional[float]` |
| `completed` | `typing.Optional[float]` |
| `advance` | `typing.Optional[float]` |
| `description` | `typing.Optional[str]` |
| `visible` | `typing.Optional[bool]` |
| `refresh` | `bool` |
| `fields` | `typing.Any` |

#### wrap_file()

```python
def wrap_file(
    file: typing.BinaryIO,
    total: typing.Optional[int],
    task_id: typing.Optional[rich.progress.TaskID],
    description: str,
):
```
Track progress file reading from a binary file.



| Parameter | Type |
|-|-|
| `file` | `typing.BinaryIO` |
| `total` | `typing.Optional[int]` |
| `task_id` | `typing.Optional[rich.progress.TaskID]` |
| `description` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| console |  |  |
| finished |  |  |
| task_ids |  |  |
| tasks |  |  |

## flytekit.clis.sdk_in_container.run.PyFlyteParams

```python
def PyFlyteParams(
    config_file: typing.Optional[str],
    verbose: bool,
    pkgs: typing.List[str],
):
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Optional[str]` |
| `verbose` | `bool` |
| `pkgs` | `typing.List[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) | None |


#### from_dict()

```python
def from_dict(
    d: typing.Dict[str, typing.Any],
):
```
| Parameter | Type |
|-|-|
| `d` | `typing.Dict[str, typing.Any]` |

## flytekit.clis.sdk_in_container.run.PythonFunctionWorkflow

Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte.
This Python object represents a workflow  defined by a function and decorated with the
:py:func:`@workflow <flytekit.workflow>` decorator. Please see notes on that object for additional information.


```python
def PythonFunctionWorkflow(
    workflow_function: Callable,
    metadata: WorkflowMetadata,
    default_metadata: WorkflowMetadataDefaults,
    docstring: Optional[Docstring],
    on_failure: Optional[Union[WorkflowBase, Task]],
    docs: Optional[Documentation],
    pickle_untyped: bool,
    default_options: Optional[Options],
):
```
| Parameter | Type |
|-|-|
| `workflow_function` | `Callable` |
| `metadata` | `WorkflowMetadata` |
| `default_metadata` | `WorkflowMetadataDefaults` |
| `docstring` | `Optional[Docstring]` |
| `on_failure` | `Optional[Union[WorkflowBase, Task]]` |
| `docs` | `Optional[Documentation]` |
| `pickle_untyped` | `bool` |
| `default_options` | `Optional[Options]` |

### Methods

| Method | Description |
|-|-|
| [`add()`](#add) | None |
| [`compile()`](#compile) | Supply static Python native values in the kwargs if you want them to be used in the compilation |
| [`construct_node_metadata()`](#construct_node_metadata) | None |
| [`execute()`](#execute) | This function is here only to try to streamline the pattern between workflows and tasks |
| [`find_lhs()`](#find_lhs) | None |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found |
| [`loader_args()`](#loader_args) | This is responsible for turning an instance of a task into args that the load_task function can reconstitute |
| [`local_execute()`](#local_execute) | None |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task |


#### add()

```python
def add(
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
):
```
| Parameter | Type |
|-|-|
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

#### compile()

```python
def compile(
    kwargs,
):
```
Supply static Python native values in the kwargs if you want them to be used in the compilation. This mimics
a 'closure' in the traditional sense of the word.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### execute()

```python
def execute(
    kwargs,
):
```
This function is here only to try to streamline the pattern between workflows and tasks. Since tasks
call execute from dispatch_execute which is in local_execute, workflows should also call an execute inside
local_execute. This makes mocking cleaner.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### find_lhs()

```python
def find_lhs()
```
#### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


#### load_task()

```python
def load_task(
    loader_args: typing.List[str],
):
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type |
|-|-|
| `loader_args` | `typing.List[str]` |

#### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
):
```
This is responsible for turning an instance of a task into args that the load_task function can reconstitute.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

#### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### task_name()

```python
def task_name(
    t: PythonAutoContainerTask,
):
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `PythonAutoContainerTask` |

### Properties

| Property | Type | Description |
|-|-|-|
| default_options |  |  |
| docs |  |  |
| failure_node |  |  |
| function |  |  |
| instantiated_in |  |  |
| interface |  |  |
| lhs |  |  |
| location |  |  |
| name |  |  |
| nodes |  |  |
| on_failure |  |  |
| output_bindings |  |  |
| python_interface |  |  |
| short_name |  |  |
| workflow_metadata |  |  |
| workflow_metadata_defaults |  |  |

## flytekit.clis.sdk_in_container.run.PythonTask

Base Class for all Tasks with a Python native ``Interface``. This should be directly used for task types, that do
not have a python function to be executed. Otherwise refer to :py:class:`flytekit.PythonFunctionTask`.


```python
def PythonTask(
    task_type: str,
    name: str,
    task_config: typing.Optional[~T],
    interface: typing.Optional[flytekit.core.interface.Interface],
    environment: typing.Optional[typing.Dict[str, str]],
    disable_deck: typing.Optional[bool],
    enable_deck: typing.Optional[bool],
    deck_fields: typing.Optional[typing.Tuple[flytekit.deck.deck.DeckField, ...]],
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `task_type` | `str` |
| `name` | `str` |
| `task_config` | `typing.Optional[~T]` |
| `interface` | `typing.Optional[flytekit.core.interface.Interface]` |
| `environment` | `typing.Optional[typing.Dict[str, str]]` |
| `disable_deck` | `typing.Optional[bool]` |
| `enable_deck` | `typing.Optional[bool]` |
| `deck_fields` | `typing.Optional[typing.Tuple[flytekit.deck.deck.DeckField, ...]]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor |
| [`execute()`](#execute) | This method will be invoked to execute the task |
| [`find_lhs()`](#find_lhs) | None |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up, |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
):
```
Generates a node that encapsulates this task in a workflow definition.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### dispatch_execute()

```python
def dispatch_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
):
```
This method translates Flyte's Type system based input values and invokes the actual call to the executor
This method is also invoked during runtime.

* ``VoidPromise`` is returned in the case when the task itself declares no outputs.
* ``Literal Map`` is returned when the task returns either one more outputs in the declaration. Individual outputs
may be none
* ``DynamicJobSpec`` is returned when a dynamic workflow is executed


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### execute()

```python
def execute(
    kwargs,
):
```
This method will be invoked to execute the task.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### find_lhs()

```python
def find_lhs()
```
#### get_config()

```python
def get_config(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_container()

```python
def get_container(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
):
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the Sql definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_type_for_input_var()

```python
def get_type_for_input_var(
    k: str,
    v: typing.Any,
):
```
Returns the python type for an input variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### get_type_for_output_var()

```python
def get_type_for_output_var(
    k: str,
    v: typing.Any,
):
```
Returns the python type for the specified output variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
```
This function is used only in the local execution path and is responsible for calling dispatch execute.
Use this function when calling a task with native values (or Promises containing Flyte literals derived from
Python native values).


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### post_execute()

```python
def post_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
    rval: typing.Any,
):
```
Post execute is called after the execution has completed, with the user_params and can be used to clean-up,
or alter the outputs to match the intended tasks outputs. If not overridden, then this function is a No-op



| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |
| `rval` | `typing.Any` |

#### pre_execute()

```python
def pre_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
):
```
This is the method that will be invoked directly before executing the task method and before all the inputs
are converted. One particular case where this is useful is if the context is to be modified for the user process
to get some user space parameters. This also ensures that things like SparkSession are already correctly
setup before the type transformers are called

This should return either the same context of the mutated context


| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |

#### sandbox_execute()

```python
def sandbox_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
):
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

### Properties

| Property | Type | Description |
|-|-|-|
| deck_fields |  |  |
| disable_deck |  |  |
| docs |  |  |
| enable_deck |  |  |
| environment |  |  |
| instantiated_in |  |  |
| interface |  |  |
| lhs |  |  |
| location |  |  |
| metadata |  |  |
| name |  |  |
| python_interface |  |  |
| security_context |  |  |
| task_config |  |  |
| task_type |  |  |
| task_type_version |  |  |

## flytekit.clis.sdk_in_container.run.RawOutputDataConfig

```python
def RawOutputDataConfig(
    output_location_prefix,
):
```
| Parameter | Type |
|-|-|
| `output_location_prefix` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2,
):
```
| Parameter | Type |
|-|-|
| `pb2` |  |

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
| is_empty |  |  |
| output_location_prefix |  |  |

## flytekit.clis.sdk_in_container.run.RemoteEntityGroup

click multicommand that retrieves launchplans from a remote flyte instance and executes them.


```python
def RemoteEntityGroup(
    command_name: str,
):
```
Initialize RichGroup class.


| Parameter | Type |
|-|-|
| `command_name` | `str` |

### Methods

| Method | Description |
|-|-|
| [`add_command()`](#add_command) | Registers another :class:`Command` with this group |
| [`collect_usage_pieces()`](#collect_usage_pieces) | Returns all the pieces that go into the usage line and returns |
| [`command()`](#command) | A shortcut decorator for declaring and attaching a command to |
| [`format_commands()`](#format_commands) | Extra format methods for multi methods that adds all the commands |
| [`format_epilog()`](#format_epilog) | Writes the epilog into the formatter if it exists |
| [`format_help()`](#format_help) | Writes the help into the formatter if it exists |
| [`format_help_text()`](#format_help_text) | Writes the help text to the formatter if it exists |
| [`format_options()`](#format_options) | Writes all the options into the formatter if they exist |
| [`format_usage()`](#format_usage) | Writes the usage line into the formatter |
| [`get_command()`](#get_command) | Given a context and a command name, this returns a |
| [`get_help()`](#get_help) | Formats the help into a string and returns it |
| [`get_help_option()`](#get_help_option) | Returns the help option object |
| [`get_help_option_names()`](#get_help_option_names) | Returns the names for the help option |
| [`get_params()`](#get_params) | None |
| [`get_short_help_str()`](#get_short_help_str) | Gets short help for the command or makes it by shortening the |
| [`get_usage()`](#get_usage) | Formats the usage line into a string and returns it |
| [`group()`](#group) | A shortcut decorator for declaring and attaching a group to |
| [`invoke()`](#invoke) | Given a context, this invokes the attached callback (if it exists) |
| [`list_commands()`](#list_commands) | Returns a list of subcommand names in the order they should |
| [`main()`](#main) | This is the way to invoke a script with all the bells and |
| [`make_context()`](#make_context) | This function when given an info name and arguments will kick |
| [`make_parser()`](#make_parser) | Creates the underlying option parser for this command |
| [`parse_args()`](#parse_args) | Given a context and a list of arguments this creates the parser |
| [`resolve_command()`](#resolve_command) | None |
| [`result_callback()`](#result_callback) | Adds a result callback to the command |
| [`shell_complete()`](#shell_complete) | Return a list of completions for the incomplete value |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating |


#### add_command()

```python
def add_command(
    cmd: click.core.Command,
    name: typing.Optional[str],
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
    ctx,
    name,
):
```
Given a context and a command name, this returns a
:class:`Command` object if it exists or returns `None`.


| Parameter | Type |
|-|-|
| `ctx` |  |
| `name` |  |

#### get_help()

```python
def get_help(
    ctx: click.core.Context,
):
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
):
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
):
```
Returns the names for the help option.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_params()

```python
def get_params(
    ctx: click.core.Context,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_short_help_str()

```python
def get_short_help_str(
    limit: int,
):
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
):
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
):
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
):
```
Given a context, this invokes the attached callback (if it exists)
in the right way.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### list_commands()

```python
def list_commands(
    ctx,
):
```
Returns a list of subcommand names in the order they should
appear.


| Parameter | Type |
|-|-|
| `ctx` |  |

#### main()

```python
def main(
    args: `*args`,
    prog_name: typing.Optional[str],
    complete_var: typing.Optional[str],
    standalone_mode: bool,
    windows_expand_args: bool,
    extra: typing.Any,
):
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
):
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
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `args` | ``*args`` |

#### result_callback()

```python
def result_callback(
    replace: bool,
):
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
):
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
):
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
| console |  |  |
| help_config |  |  |

## flytekit.clis.sdk_in_container.run.RunCommand

A click command group for registering and executing flyte workflows & tasks in a file.


```python
def RunCommand(
    args,
    kwargs,
):
```
Initialize RichGroup class.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`add_command()`](#add_command) | Registers another :class:`Command` with this group |
| [`collect_usage_pieces()`](#collect_usage_pieces) | Returns all the pieces that go into the usage line and returns |
| [`command()`](#command) | A shortcut decorator for declaring and attaching a command to |
| [`format_commands()`](#format_commands) | Extra format methods for multi methods that adds all the commands |
| [`format_epilog()`](#format_epilog) | Writes the epilog into the formatter if it exists |
| [`format_help()`](#format_help) | Writes the help into the formatter if it exists |
| [`format_help_text()`](#format_help_text) | Writes the help text to the formatter if it exists |
| [`format_options()`](#format_options) | Writes all the options into the formatter if they exist |
| [`format_usage()`](#format_usage) | Writes the usage line into the formatter |
| [`get_command()`](#get_command) | Given a context and a command name, this returns a |
| [`get_help()`](#get_help) | Formats the help into a string and returns it |
| [`get_help_option()`](#get_help_option) | Returns the help option object |
| [`get_help_option_names()`](#get_help_option_names) | Returns the names for the help option |
| [`get_params()`](#get_params) | None |
| [`get_short_help_str()`](#get_short_help_str) | Gets short help for the command or makes it by shortening the |
| [`get_usage()`](#get_usage) | Formats the usage line into a string and returns it |
| [`group()`](#group) | A shortcut decorator for declaring and attaching a group to |
| [`invoke()`](#invoke) | Given a context, this invokes the attached callback (if it exists) |
| [`list_commands()`](#list_commands) | Returns a list of subcommand names in the order they should |
| [`main()`](#main) | This is the way to invoke a script with all the bells and |
| [`make_context()`](#make_context) | This function when given an info name and arguments will kick |
| [`make_parser()`](#make_parser) | Creates the underlying option parser for this command |
| [`parse_args()`](#parse_args) | Given a context and a list of arguments this creates the parser |
| [`resolve_command()`](#resolve_command) | None |
| [`result_callback()`](#result_callback) | Adds a result callback to the command |
| [`shell_complete()`](#shell_complete) | Return a list of completions for the incomplete value |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating |


#### add_command()

```python
def add_command(
    cmd: click.core.Command,
    name: typing.Optional[str],
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
    ctx,
    filename,
):
```
Given a context and a command name, this returns a
:class:`Command` object if it exists or returns `None`.


| Parameter | Type |
|-|-|
| `ctx` |  |
| `filename` |  |

#### get_help()

```python
def get_help(
    ctx: click.core.Context,
):
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
):
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
):
```
Returns the names for the help option.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_params()

```python
def get_params(
    ctx: click.core.Context,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_short_help_str()

```python
def get_short_help_str(
    limit: int,
):
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
):
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
):
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
):
```
Given a context, this invokes the attached callback (if it exists)
in the right way.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### list_commands()

```python
def list_commands(
    ctx,
    add_remote: bool,
):
```
Returns a list of subcommand names in the order they should
appear.


| Parameter | Type |
|-|-|
| `ctx` |  |
| `add_remote` | `bool` |

#### main()

```python
def main(
    args: `*args`,
    prog_name: typing.Optional[str],
    complete_var: typing.Optional[str],
    standalone_mode: bool,
    windows_expand_args: bool,
    extra: typing.Any,
):
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
):
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
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `args` | ``*args`` |

#### result_callback()

```python
def result_callback(
    replace: bool,
):
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
):
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
):
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
| console |  |  |
| help_config |  |  |

## flytekit.clis.sdk_in_container.run.RunLevelComputedParams

This class is used to store the computed parameters that are used to run a workflow / task / launchplan.
Computed parameters are created during the execution


```python
def RunLevelComputedParams(
    project_root: typing.Optional[str],
    module: typing.Optional[str],
    temp_file_name: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `project_root` | `typing.Optional[str]` |
| `module` | `typing.Optional[str]` |
| `temp_file_name` | `typing.Optional[str]` |

## flytekit.clis.sdk_in_container.run.RunLevelParams

This class is used to store the parameters that are used to run a workflow / task / launchplan.


```python
def RunLevelParams(
    config_file: typing.Optional[str],
    verbose: bool,
    pkgs: typing.List[str],
    project: str,
    domain: str,
    destination_dir: str,
    copy_all: bool,
    copy: typing.Optional[flytekit.constants.CopyFileDetection],
    image_config: flytekit.configuration.ImageConfig,
    service_account: str,
    wait_execution: bool,
    poll_interval: int,
    dump_snippet: bool,
    overwrite_cache: bool,
    envvars: typing.Dict[str, str],
    tags: typing.List[str],
    name: str,
    labels: typing.Dict[str, str],
    annotations: typing.Dict[str, str],
    raw_output_data_prefix: str,
    max_parallelism: int,
    disable_notifications: bool,
    remote: bool,
    limit: int,
    cluster_pool: str,
    execution_cluster_label: str,
    computed_params: flytekit.clis.sdk_in_container.run.RunLevelComputedParams,
    _remote: typing.Optional[flytekit.remote.remote.FlyteRemote],
):
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Optional[str]` |
| `verbose` | `bool` |
| `pkgs` | `typing.List[str]` |
| `project` | `str` |
| `domain` | `str` |
| `destination_dir` | `str` |
| `copy_all` | `bool` |
| `copy` | `typing.Optional[flytekit.constants.CopyFileDetection]` |
| `image_config` | `flytekit.configuration.ImageConfig` |
| `service_account` | `str` |
| `wait_execution` | `bool` |
| `poll_interval` | `int` |
| `dump_snippet` | `bool` |
| `overwrite_cache` | `bool` |
| `envvars` | `typing.Dict[str, str]` |
| `tags` | `typing.List[str]` |
| `name` | `str` |
| `labels` | `typing.Dict[str, str]` |
| `annotations` | `typing.Dict[str, str]` |
| `raw_output_data_prefix` | `str` |
| `max_parallelism` | `int` |
| `disable_notifications` | `bool` |
| `remote` | `bool` |
| `limit` | `int` |
| `cluster_pool` | `str` |
| `execution_cluster_label` | `str` |
| `computed_params` | `flytekit.clis.sdk_in_container.run.RunLevelComputedParams` |
| `_remote` | `typing.Optional[flytekit.remote.remote.FlyteRemote]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) | None |
| [`options()`](#options) | Return the set of base parameters added to every pyflyte run workflow subcommand |
| [`remote_instance()`](#remote_instance) | None |


#### from_dict()

```python
def from_dict(
    d: typing.Dict[str, typing.Any],
):
```
| Parameter | Type |
|-|-|
| `d` | `typing.Dict[str, typing.Any]` |

#### options()

```python
def options()
```
Return the set of base parameters added to every pyflyte run workflow subcommand.


#### remote_instance()

```python
def remote_instance()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_remote |  |  |

## flytekit.clis.sdk_in_container.run.SerializationSettings

These settings are provided while serializing a workflow and task, before registration. This is required to get
runtime information at serialization time, as well as some defaults.

Attributes:
project (str): The project (if any) with which to register entities under.
domain (str): The domain (if any) with which to register entities under.
version (str): The version (if any) with which to register entities under.
image_config (ImageConfig): The image config used to define task container images.
env (Optional[Dict[str, str]]): Environment variables injected into task container definitions.
flytekit_virtualenv_root (Optional[str]):  During out of container serialize the absolute path of the flytekit
virtualenv at serialization time won't match the in-container value at execution time. This optional value
is used to provide the in-container virtualenv path
python_interpreter (Optional[str]): The python executable to use. This is used for spark tasks in out of
container execution.
entrypoint_settings (Optional[EntrypointSettings]): Information about the command, path and version of the
entrypoint program.
fast_serialization_settings (Optional[FastSerializationSettings]): If the code is being serialized so that it
can be fast registered (and thus omit building a Docker image) this object contains additional parameters
for serialization.
source_root (Optional[str]): The root directory of the source code.


```python
def SerializationSettings(
    image_config: ImageConfig,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    version: typing.Optional[str],
    env: Optional[Dict[str, str]],
    git_repo: Optional[str],
    python_interpreter: str,
    flytekit_virtualenv_root: Optional[str],
    fast_serialization_settings: Optional[FastSerializationSettings],
    source_root: Optional[str],
):
```
| Parameter | Type |
|-|-|
| `image_config` | `ImageConfig` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `version` | `typing.Optional[str]` |
| `env` | `Optional[Dict[str, str]]` |
| `git_repo` | `Optional[str]` |
| `python_interpreter` | `str` |
| `flytekit_virtualenv_root` | `Optional[str]` |
| `fast_serialization_settings` | `Optional[FastSerializationSettings]` |
| `source_root` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`default_entrypoint_settings()`](#default_entrypoint_settings) | Assumes the entrypoint is installed in a virtual-environment where the interpreter is |
| [`for_image()`](#for_image) | None |
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`from_transport()`](#from_transport) | None |
| [`new_builder()`](#new_builder) | Creates a ``SerializationSettings |
| [`schema()`](#schema) | None |
| [`should_fast_serialize()`](#should_fast_serialize) | Whether or not the serialization settings specify that entities should be serialized for fast registration |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |
| [`venv_root_from_interpreter()`](#venv_root_from_interpreter) | Computes the path of the virtual environment root, based on the passed in python interpreter path |
| [`with_serialized_context()`](#with_serialized_context) | Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext |


#### default_entrypoint_settings()

```python
def default_entrypoint_settings(
    interpreter_path: str,
):
```
Assumes the entrypoint is installed in a virtual-environment where the interpreter is


| Parameter | Type |
|-|-|
| `interpreter_path` | `str` |

#### for_image()

```python
def for_image(
    image: str,
    version: str,
    project: str,
    domain: str,
    python_interpreter_path: str,
):
```
| Parameter | Type |
|-|-|
| `image` | `str` |
| `version` | `str` |
| `project` | `str` |
| `domain` | `str` |
| `python_interpreter_path` | `str` |

#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
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
):
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### from_transport()

```python
def from_transport(
    s: str,
):
```
| Parameter | Type |
|-|-|
| `s` | `str` |

#### new_builder()

```python
def new_builder()
```
Creates a ``SerializationSettings.Builder`` that copies the existing serialization settings parameters and
allows for customization.


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
):
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

#### should_fast_serialize()

```python
def should_fast_serialize()
```
Whether or not the serialization settings specify that entities should be serialized for fast registration.


#### to_dict()

```python
def to_dict(
    encode_json,
):
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
):
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

#### venv_root_from_interpreter()

```python
def venv_root_from_interpreter(
    interpreter_path: str,
):
```
Computes the path of the virtual environment root, based on the passed in python interpreter path
for example /opt/venv/bin/python3 -> /opt/venv


| Parameter | Type |
|-|-|
| `interpreter_path` | `str` |

#### with_serialized_context()

```python
def with_serialized_context()
```
Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext
This is useful in transporting SerializedContext to serialized and registered tasks.
The setting will be available in the `env` field with the key `SERIALIZED_CONTEXT_ENV_VAR`
:return: A newly constructed SerializationSettings, or self, if it already has the serializationSettings


### Properties

| Property | Type | Description |
|-|-|-|
| entrypoint_settings |  |  |
| serialized_context |  |  |

## flytekit.clis.sdk_in_container.run.SimpleType

## flytekit.clis.sdk_in_container.run.TextColumn

A column containing text.


```python
def TextColumn(
    text_format: str,
    style: typing.Union[str, ForwardRef('Style')],
    justify: typing.Literal['default', 'left', 'center', 'right', 'full'],
    markup: bool,
    highlighter: typing.Optional[rich.highlighter.Highlighter],
    table_column: typing.Optional[rich.table.Column],
):
```
| Parameter | Type |
|-|-|
| `text_format` | `str` |
| `style` | `typing.Union[str, ForwardRef('Style')]` |
| `justify` | `typing.Literal['default', 'left', 'center', 'right', 'full']` |
| `markup` | `bool` |
| `highlighter` | `typing.Optional[rich.highlighter.Highlighter]` |
| `table_column` | `typing.Optional[rich.table.Column]` |

### Methods

| Method | Description |
|-|-|
| [`get_table_column()`](#get_table_column) | Get a table column, used to build tasks table |
| [`render()`](#render) | Should return a renderable object |


#### get_table_column()

```python
def get_table_column()
```
Get a table column, used to build tasks table.


#### render()

```python
def render(
    task: Task,
):
```
Should return a renderable object.


| Parameter | Type |
|-|-|
| `task` | `Task` |

## flytekit.clis.sdk_in_container.run.TimeElapsedColumn

Renders time elapsed.


```python
def TimeElapsedColumn(
    table_column: typing.Optional[rich.table.Column],
):
```
| Parameter | Type |
|-|-|
| `table_column` | `typing.Optional[rich.table.Column]` |

### Methods

| Method | Description |
|-|-|
| [`get_table_column()`](#get_table_column) | Get a table column, used to build tasks table |
| [`render()`](#render) | Show time elapsed |


#### get_table_column()

```python
def get_table_column()
```
Get a table column, used to build tasks table.


#### render()

```python
def render(
    task: Task,
):
```
Show time elapsed.


| Parameter | Type |
|-|-|
| `task` | `Task` |

## flytekit.clis.sdk_in_container.run.TypeEngine

Core Extensible TypeEngine of Flytekit. This should be used to extend the capabilities of FlyteKits type system.
Users can implement their own TypeTransformers and register them with the TypeEngine. This will allow special handling
of user objects


### Methods

| Method | Description |
|-|-|
| [`async_to_literal()`](#async_to_literal) | Converts a python value of a given type and expected ``LiteralType`` into a resolved ``Literal`` value |
| [`async_to_python_value()`](#async_to_python_value) | None |
| [`calculate_hash()`](#calculate_hash) | None |
| [`dict_to_literal_map()`](#dict_to_literal_map) | None |
| [`dict_to_literal_map_pb()`](#dict_to_literal_map_pb) | None |
| [`get_available_transformers()`](#get_available_transformers) | Returns all python types for which transformers are available |
| [`get_transformer()`](#get_transformer) | Implements a recursive search for the transformer |
| [`guess_python_type()`](#guess_python_type) | Transforms a flyte-specific ``LiteralType`` to a regular python value |
| [`guess_python_types()`](#guess_python_types) | Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values |
| [`lazy_import_transformers()`](#lazy_import_transformers) | Only load the transformers if needed |
| [`literal_map_to_kwargs()`](#literal_map_to_kwargs) | None |
| [`named_tuple_to_variable_map()`](#named_tuple_to_variable_map) | Converts a python-native ``NamedTuple`` to a flyte-specific VariableMap of named literals |
| [`register()`](#register) | This should be used for all types that respond with the right type annotation when you use type( |
| [`register_additional_type()`](#register_additional_type) | None |
| [`register_restricted_type()`](#register_restricted_type) | None |
| [`to_html()`](#to_html) | None |
| [`to_literal()`](#to_literal) | The current dance is because we are allowing users to call from an async function, this synchronous |
| [`to_literal_checks()`](#to_literal_checks) | None |
| [`to_literal_type()`](#to_literal_type) | Converts a python type into a flyte specific ``LiteralType`` |
| [`to_python_value()`](#to_python_value) | Converts a Literal value with an expected python type into a python value |
| [`unwrap_offloaded_literal()`](#unwrap_offloaded_literal) | None |


#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
):
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
):
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
):
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
):
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
):
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
):
```
Implements a recursive search for the transformer.


| Parameter | Type |
|-|-|
| `python_type` | `Type` |

#### guess_python_type()

```python
def guess_python_type(
    flyte_type: LiteralType,
):
```
Transforms a flyte-specific ``LiteralType`` to a regular python value.


| Parameter | Type |
|-|-|
| `flyte_type` | `LiteralType` |

#### guess_python_types()

```python
def guess_python_types(
    flyte_variable_dict: typing.Dict[str, _interface_models.Variable],
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |

## flytekit.clis.sdk_in_container.run.Variable

```python
def Variable(
    type,
    description,
    artifact_partial_id: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID],
    artifact_tag: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactTag],
):
```
| Parameter | Type |
|-|-|
| `type` |  |
| `description` |  |
| `artifact_partial_id` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID]` |
| `artifact_tag` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactTag]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`to_flyte_idl_list()`](#to_flyte_idl_list) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    variable_proto,
):
```
| Parameter | Type |
|-|-|
| `variable_proto` |  |

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
#### to_flyte_idl_list()

```python
def to_flyte_idl_list()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| artifact_partial_id |  |  |
| artifact_tag |  |  |
| description |  |  |
| is_empty |  |  |
| type |  |  |

## flytekit.clis.sdk_in_container.run.WorkflowBase

```python
def WorkflowBase(
    name: str,
    workflow_metadata: WorkflowMetadata,
    workflow_metadata_defaults: WorkflowMetadataDefaults,
    python_interface: Interface,
    on_failure: Optional[Union[WorkflowBase, Task]],
    docs: Optional[Documentation],
    default_options: Optional[Options],
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow_metadata` | `WorkflowMetadata` |
| `workflow_metadata_defaults` | `WorkflowMetadataDefaults` |
| `python_interface` | `Interface` |
| `on_failure` | `Optional[Union[WorkflowBase, Task]]` |
| `docs` | `Optional[Documentation]` |
| `default_options` | `Optional[Options]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | None |
| [`construct_node_metadata()`](#construct_node_metadata) | None |
| [`execute()`](#execute) | None |
| [`local_execute()`](#local_execute) | None |
| [`local_execution_mode()`](#local_execution_mode) | None |


#### compile()

```python
def compile(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### execute()

```python
def execute(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
### Properties

| Property | Type | Description |
|-|-|-|
| default_options |  |  |
| docs |  |  |
| failure_node |  |  |
| interface |  |  |
| name |  |  |
| nodes |  |  |
| on_failure |  |  |
| output_bindings |  |  |
| python_interface |  |  |
| short_name |  |  |
| workflow_metadata |  |  |
| workflow_metadata_defaults |  |  |

## flytekit.clis.sdk_in_container.run.WorkflowCommand

click multicommand at the python file layer, subcommands should be all the workflows in the file.


```python
def WorkflowCommand(
    filename: str,
    args,
    kwargs,
):
```
Initialize RichGroup class.


| Parameter | Type |
|-|-|
| `filename` | `str` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`add_command()`](#add_command) | Registers another :class:`Command` with this group |
| [`collect_usage_pieces()`](#collect_usage_pieces) | Returns all the pieces that go into the usage line and returns |
| [`command()`](#command) | A shortcut decorator for declaring and attaching a command to |
| [`format_commands()`](#format_commands) | Extra format methods for multi methods that adds all the commands |
| [`format_epilog()`](#format_epilog) | Writes the epilog into the formatter if it exists |
| [`format_help()`](#format_help) | Writes the help into the formatter if it exists |
| [`format_help_text()`](#format_help_text) | Writes the help text to the formatter if it exists |
| [`format_options()`](#format_options) | Writes all the options into the formatter if they exist |
| [`format_usage()`](#format_usage) | Writes the usage line into the formatter |
| [`get_command()`](#get_command) | This command uses the filename with which this command was created, and the string name of the entity passed |
| [`get_help()`](#get_help) | Formats the help into a string and returns it |
| [`get_help_option()`](#get_help_option) | Returns the help option object |
| [`get_help_option_names()`](#get_help_option_names) | Returns the names for the help option |
| [`get_params()`](#get_params) | None |
| [`get_short_help_str()`](#get_short_help_str) | Gets short help for the command or makes it by shortening the |
| [`get_usage()`](#get_usage) | Formats the usage line into a string and returns it |
| [`group()`](#group) | A shortcut decorator for declaring and attaching a group to |
| [`invoke()`](#invoke) | Given a context, this invokes the attached callback (if it exists) |
| [`list_commands()`](#list_commands) | Returns a list of subcommand names in the order they should |
| [`main()`](#main) | This is the way to invoke a script with all the bells and |
| [`make_context()`](#make_context) | This function when given an info name and arguments will kick |
| [`make_parser()`](#make_parser) | Creates the underlying option parser for this command |
| [`parse_args()`](#parse_args) | Given a context and a list of arguments this creates the parser |
| [`resolve_command()`](#resolve_command) | None |
| [`result_callback()`](#result_callback) | Adds a result callback to the command |
| [`shell_complete()`](#shell_complete) | Return a list of completions for the incomplete value |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating |


#### add_command()

```python
def add_command(
    cmd: click.core.Command,
    name: typing.Optional[str],
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
    ctx,
    exe_entity,
):
```
This command uses the filename with which this command was created, and the string name of the entity passed
after the Python filename on the command line, to load the Python object, and then return the Command that
click should run.


| Parameter | Type |
|-|-|
| `ctx` |  |
| `exe_entity` |  |

#### get_help()

```python
def get_help(
    ctx: click.core.Context,
):
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
):
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
):
```
Returns the names for the help option.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_params()

```python
def get_params(
    ctx: click.core.Context,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_short_help_str()

```python
def get_short_help_str(
    limit: int,
):
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
):
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
):
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
):
```
Given a context, this invokes the attached callback (if it exists)
in the right way.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### list_commands()

```python
def list_commands(
    ctx,
):
```
Returns a list of subcommand names in the order they should
appear.


| Parameter | Type |
|-|-|
| `ctx` |  |

#### main()

```python
def main(
    args: `*args`,
    prog_name: typing.Optional[str],
    complete_var: typing.Optional[str],
    standalone_mode: bool,
    windows_expand_args: bool,
    extra: typing.Any,
):
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
):
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
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `args` | ``*args`` |

#### result_callback()

```python
def result_callback(
    replace: bool,
):
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
):
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
):
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
| console |  |  |
| help_config |  |  |

## flytekit.clis.sdk_in_container.run.WorkflowExecutionPhase

This class holds enum values used for setting notifications. See :py:class:`flytekit.Email`
for sample usage.


### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
):
```
| Parameter | Type |
|-|-|
| `int_value` |  |

## flytekit.clis.sdk_in_container.run.YamlFileReadingCommand

Richly formatted click Command.

Inherits click.Command and overrides help and error methods
to print richly formatted output.

This class can be used as a mixin for other click command objects.


```python
def YamlFileReadingCommand(
    name: str,
    params: typing.List[click.core.Option],
    help: str,
    callback: typing.Callable,
):
```
Create Rich Command instance.


| Parameter | Type |
|-|-|
| `name` | `str` |
| `params` | `typing.List[click.core.Option]` |
| `help` | `str` |
| `callback` | `typing.Callable` |

### Methods

| Method | Description |
|-|-|
| [`collect_usage_pieces()`](#collect_usage_pieces) | Returns all the pieces that go into the usage line and returns |
| [`format_epilog()`](#format_epilog) | Writes the epilog into the formatter if it exists |
| [`format_help()`](#format_help) | Writes the help into the formatter if it exists |
| [`format_help_text()`](#format_help_text) | Writes the help text to the formatter if it exists |
| [`format_options()`](#format_options) | Writes all the options into the formatter if they exist |
| [`format_usage()`](#format_usage) | Writes the usage line into the formatter |
| [`get_help()`](#get_help) | Formats the help into a string and returns it |
| [`get_help_option()`](#get_help_option) | Returns the help option object |
| [`get_help_option_names()`](#get_help_option_names) | Returns the names for the help option |
| [`get_params()`](#get_params) | None |
| [`get_short_help_str()`](#get_short_help_str) | Gets short help for the command or makes it by shortening the |
| [`get_usage()`](#get_usage) | Formats the usage line into a string and returns it |
| [`invoke()`](#invoke) | Given a context, this invokes the attached callback (if it exists) |
| [`main()`](#main) | This is the way to invoke a script with all the bells and |
| [`make_context()`](#make_context) | This function when given an info name and arguments will kick |
| [`make_parser()`](#make_parser) | Creates the underlying option parser for this command |
| [`parse_args()`](#parse_args) | Given a context and a list of arguments this creates the parser |
| [`shell_complete()`](#shell_complete) | Return a list of completions for the incomplete value |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating |


#### collect_usage_pieces()

```python
def collect_usage_pieces(
    ctx: click.core.Context,
):
```
Returns all the pieces that go into the usage line and returns
it as a list of strings.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### format_epilog()

```python
def format_epilog(
    ctx: rich_click.rich_context.RichContext,
    formatter: rich_click.rich_help_formatter.RichHelpFormatter,
):
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
):
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
):
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
):
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
):
```
Writes the usage line into the formatter.

This is a low-level method called by :meth:`get_usage`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `formatter` | `click.formatting.HelpFormatter` |

#### get_help()

```python
def get_help(
    ctx: click.core.Context,
):
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
):
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
):
```
Returns the names for the help option.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_params()

```python
def get_params(
    ctx: click.core.Context,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_short_help_str()

```python
def get_short_help_str(
    limit: int,
):
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
):
```
Formats the usage line into a string and returns it.

Calls :meth:`format_usage` internally.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### invoke()

```python
def invoke(
    ctx: click.core.Context,
):
```
Given a context, this invokes the attached callback (if it exists)
in the right way.


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
):
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
):
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
):
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
):
```
Given a context and a list of arguments this creates the parser
and parses the arguments, then modifies the context as necessary.
This is automatically invoked by :meth:`make_context`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `args` | ``*args`` |

#### shell_complete()

```python
def shell_complete(
    ctx: click.core.Context,
    incomplete: str,
):
```
Return a list of completions for the incomplete value. Looks
at the names of options and chained multi-commands.



| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `incomplete` | `str` |

#### to_info_dict()

```python
def to_info_dict(
    ctx: click.core.Context,
):
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
| console |  |  |
| help_config |  |  |

