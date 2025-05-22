---
title: flytekitplugins.papermill.task
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.papermill.task

## Directory

### Classes

| Class | Description |
|-|-|
| [`NotebookTask`](.././flytekitplugins.papermill.task#flytekitpluginspapermilltasknotebooktask) | Simple Papermill based input output handling for a Python Jupyter notebook. |

### Methods

| Method | Description |
|-|-|
| [`load_flytedirectory()`](#load_flytedirectory) | Loads a FlyteDirectory from a file. |
| [`load_flytefile()`](#load_flytefile) | Loads a FlyteFile from a file. |
| [`load_python_val_from_file()`](#load_python_val_from_file) | Loads a python value from a Flyte literal saved to a local file. |
| [`load_structureddataset()`](#load_structureddataset) | Loads a StructuredDataset from a file. |
| [`record_outputs()`](#record_outputs) | Use this method to record outputs from a notebook. |
| [`save_python_val_to_file()`](#save_python_val_to_file) | Save a python value to a local file as a Flyte literal. |


### Variables

| Property | Type | Description |
|-|-|-|
| `PAPERMILL_TASK_PREFIX` | `str` |  |
| `SAVE_AS_LITERAL` | `tuple` |  |
| `T` | `TypeVar` |  |

## Methods

#### load_flytedirectory()

```python
def load_flytedirectory(
    path: str,
) -> ~T
```
Loads a FlyteDirectory from a file.



| Parameter | Type |
|-|-|
| `path` | `str` |

#### load_flytefile()

```python
def load_flytefile(
    path: str,
) -> ~T
```
Loads a FlyteFile from a file.



| Parameter | Type |
|-|-|
| `path` | `str` |

#### load_python_val_from_file()

```python
def load_python_val_from_file(
    path: str,
    dtype: ~T,
) -> ~T
```
Loads a python value from a Flyte literal saved to a local file.

If the path matches the type, it is returned as is. This enables
reusing the parameters cell for local development.



| Parameter | Type |
|-|-|
| `path` | `str` |
| `dtype` | `~T` |

#### load_structureddataset()

```python
def load_structureddataset(
    path: str,
) -> ~T
```
Loads a StructuredDataset from a file.



| Parameter | Type |
|-|-|
| `path` | `str` |

#### record_outputs()

```python
def record_outputs(
    kwargs,
) -> str
```
Use this method to record outputs from a notebook.
It will convert all outputs to a Flyte understandable format. For Files, Directories, please use FlyteFile or
FlyteDirectory, or wrap up your paths in these decorators.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### save_python_val_to_file()

```python
def save_python_val_to_file(
    input: typing.Any,
) -> str
```
Save a python value to a local file as a Flyte literal.



| Parameter | Type |
|-|-|
| `input` | `typing.Any` |

## flytekitplugins.papermill.task.NotebookTask

Simple Papermill based input output handling for a Python Jupyter notebook. This task should be used to wrap
a Notebook that has 2 properties

Property 1:
One of the cells (usually the first) should be marked as the parameters cell. This task will inject inputs after this
cell. The task will inject the outputs observed from Flyte

Property 2:
For a notebook that produces outputs, that should be consumed by a subsequent notebook, use the method
:py:func:`record_outputs` in your notebook after the outputs are ready and pass all outputs.

Usage:

.. code-block:: python

    val_x = 10
    val_y = "hello"

    ...
    # cell begin
    from flytekitplugins.papermill import record_outputs

    record_outputs(x=val_x, y=val_y)
    #cell end

Step 2: Wrap in a task
Now point to the notebook and create an instance of :py:class:`NotebookTask` as follows

Usage:

.. code-block:: python

    nb = NotebookTask(
        name="modulename.my_notebook_task", # the name should be unique within all your tasks, usually it is a good
                                           # idea to use the modulename
        notebook_path="../path/to/my_notebook",
        render_deck=True,
        enable_deck=True,
        inputs=kwtypes(v=int),
        outputs=kwtypes(x=int, y=str),
        metadata=TaskMetadata(retries=3, cache=True, cache_version="1.0"),
    )

Step 3: Task can be executed as usual

The Task produces 2 implicit outputs.

#. It captures the executed notebook in its entirety and is available from Flyte with the name ``out_nb``.
#. It also converts the captured notebook into an ``html`` page, which the FlyteConsole will render called -
   ``out_rendered_nb``. If ``render_deck=True`` is passed, this html content will be inserted into a deck.

.. note:

    Users can access these notebooks after execution of the task locally or from remote servers.

.. note:

    By default, print statements in your notebook won't be transmitted to the pod logs/stdout. If you would
    like to have logs forwarded as the notebook executes, pass the stream_logs argument. Note that notebook
    logs can be quite verbose, so ensure you are prepared for any downstream log ingestion costs
    (e.g., cloudwatch)

.. todo:

    Implicit extraction of SparkConfiguration from the notebook is not supported.

.. todo:

    Support for remote notebook execution, we can create a custom metadata field that is read by a propeller plugin
    or just passed down back into the container, so no need to rebuild the container.

.. note:

    Some input types are not permitted by papermill. Types that cannot be passed directly into the cell are not
    supported - Only supported types are
    str, int, float, bool
    Most output types are supported as long as FlyteFile etc is used.


```python
class NotebookTask(
    name: str,
    notebook_path: str,
    render_deck: bool,
    stream_logs: bool,
    task_config: ~T,
    inputs: typing.Optional[typing.Dict[str, typing.Type]],
    outputs: typing.Optional[typing.Dict[str, typing.Type]],
    output_notebooks: typing.Optional[bool],
    kwargs,
)
```
Please see class level documentation.


| Parameter | Type |
|-|-|
| `name` | `str` |
| `notebook_path` | `str` |
| `render_deck` | `bool` |
| `stream_logs` | `bool` |
| `task_config` | `~T` |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `outputs` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `output_notebooks` | `typing.Optional[bool]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
| [`execute()`](#execute) | TODO: Figure out how to share FlyteContext ExecutionParameters with the notebook kernel (as notebook kernel. |
| [`extract_outputs()`](#extract_outputs) | Parse Outputs from Notebook. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_command()`](#get_command) | Returns the command which should be used in the container definition for the serialized version of this task. |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_default_command()`](#get_default_command) | Returns the default pyflyte-execute command used to run this on hosted Flyte platforms. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_image()`](#get_image) | Update image spec based on fast registration usage, and return string representing the image. |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up,. |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs. |
| [`render_nb_html()`](#render_nb_html) | render output notebook to html. |
| [`reset_command_fn()`](#reset_command_fn) | Resets the command which should be used in the container definition of this task to the default arguments. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
| [`set_command_fn()`](#set_command_fn) | By default, the task will run on the Flyte platform using the pyflyte-execute command. |
| [`set_resolver()`](#set_resolver) | By default, flytekit uses the DefaultTaskResolver to resolve the task. |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
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
) -> typing.Union[flytekit.models.literals.LiteralMap, flytekit.models.dynamic_job.DynamicJobSpec, typing.Coroutine]
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
) -> typing.Any
```
TODO: Figure out how to share FlyteContext ExecutionParameters with the notebook kernel (as notebook kernel
     is executed in a separate python process)

For Spark, the notebooks today need to use the new_session or just getOrCreate session and get a handle to the singleton


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### extract_outputs()

```python
def extract_outputs(
    nb: str,
) -> flytekit.models.literals.LiteralMap
```
Parse Outputs from Notebook.
This looks for a cell, with the tag "outputs" to be present.


| Parameter | Type |
|-|-|
| `nb` | `str` |

#### find_lhs()

```python
def find_lhs()
```
#### get_command()

```python
def get_command(
    settings: SerializationSettings,
) -> List[str]
```
Returns the command which should be used in the container definition for the serialized version of this task
registered on a hosted Flyte platform.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_config()

```python
def get_config(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Dict[str, str]
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
) -> flytekit.models.task.Container
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[typing.Dict[str, typing.Any]]
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_default_command()

```python
def get_default_command(
    settings: SerializationSettings,
) -> List[str]
```
Returns the default pyflyte-execute command used to run this on hosted Flyte platforms.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: SerializationSettings,
) -> Optional[tasks_pb2.ExtendedResources]
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_image()

```python
def get_image(
    settings: SerializationSettings,
) -> str
```
Update image spec based on fast registration usage, and return string representing the image


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: flytekit.configuration.SerializationSettings,
) -> flytekit.models.task.K8sPod
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.Sql]
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
) -> typing.Type[typing.Any]
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
) -> typing.Type[typing.Any]
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
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, typing.Coroutine, NoneType]
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
    user_params: flytekit.core.context_manager.ExecutionParameters,
    rval: typing.Any,
) -> typing.Any
```
Post execute is called after the execution has completed, with the user_params and can be used to clean-up,
or alter the outputs to match the intended tasks outputs. If not overridden, then this function is a No-op



| Parameter | Type |
|-|-|
| `user_params` | `flytekit.core.context_manager.ExecutionParameters` |
| `rval` | `typing.Any` |

#### pre_execute()

```python
def pre_execute(
    user_params: flytekit.core.context_manager.ExecutionParameters,
) -> flytekit.core.context_manager.ExecutionParameters
```
This is the method that will be invoked directly before executing the task method and before all the inputs
are converted. One particular case where this is useful is if the context is to be modified for the user process
to get some user space parameters. This also ensures that things like SparkSession are already correctly
setup before the type transformers are called

This should return either the same context of the mutated context


| Parameter | Type |
|-|-|
| `user_params` | `flytekit.core.context_manager.ExecutionParameters` |

#### render_nb_html()

```python
def render_nb_html(
    from_nb: str,
    to: str,
)
```
render output notebook to html
We are using nbconvert htmlexporter and its classic template
later about how to customize the exporter further.


| Parameter | Type |
|-|-|
| `from_nb` | `str` |
| `to` | `str` |

#### reset_command_fn()

```python
def reset_command_fn()
```
Resets the command which should be used in the container definition of this task to the default arguments.
This is useful when the command line is overridden at serialization time.


#### sandbox_execute()

```python
def sandbox_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### set_command_fn()

```python
def set_command_fn(
    get_command_fn: Optional[Callable[[SerializationSettings], List[str]]],
)
```
By default, the task will run on the Flyte platform using the pyflyte-execute command.
However, it can be useful to update the command with which the task is serialized for specific cases like
running map tasks ("pyflyte-map-execute") or for fast-executed tasks.


| Parameter | Type |
|-|-|
| `get_command_fn` | `Optional[Callable[[SerializationSettings], List[str]]]` |

#### set_resolver()

```python
def set_resolver(
    resolver: TaskResolverMixin,
)
```
By default, flytekit uses the DefaultTaskResolver to resolve the task. This method allows the user to set a custom
task resolver. It can be useful to override the task resolver for specific cases like running tasks in the jupyter notebook.


| Parameter | Type |
|-|-|
| `resolver` | `TaskResolverMixin` |

### Properties

| Property | Type | Description |
|-|-|-|
| `container_image` |  |  |
| `deck_fields` |  | {{< multiline >}}If not empty, this task will output deck html file for the specified decks
{{< /multiline >}} |
| `disable_deck` |  | {{< multiline >}}If true, this task will not output deck html file
{{< /multiline >}} |
| `docs` |  |  |
| `enable_deck` |  | {{< multiline >}}If true, this task will output deck html file
{{< /multiline >}} |
| `environment` |  | {{< multiline >}}Any environment variables that supplied during the execution of the task.
{{< /multiline >}} |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `name` |  |  |
| `notebook_path` |  |  |
| `output_notebook_path` |  |  |
| `python_interface` |  | {{< multiline >}}Returns this task's python interface.
{{< /multiline >}} |
| `rendered_output_path` |  |  |
| `resources` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_resolver` |  |  |
| `task_type` |  |  |
| `task_type_version` |  |  |

