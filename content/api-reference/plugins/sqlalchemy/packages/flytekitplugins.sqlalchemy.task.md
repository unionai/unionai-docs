---
title: flytekitplugins.sqlalchemy.task
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.sqlalchemy.task

## Directory

### Classes

| Class | Description |
|-|-|
| [`SQLAlchemyConfig`](.././flytekitplugins.sqlalchemy.task#flytekitpluginssqlalchemytasksqlalchemyconfig) | Use this configuration to configure task. |
| [`SQLAlchemyDefaultImages`](.././flytekitplugins.sqlalchemy.task#flytekitpluginssqlalchemytasksqlalchemydefaultimages) | Default images for the sqlalchemy flytekit plugin. |
| [`SQLAlchemyTask`](.././flytekitplugins.sqlalchemy.task#flytekitpluginssqlalchemytasksqlalchemytask) | Makes it possible to run client side SQLAlchemy queries that optionally return a FlyteSchema object. |
| [`SQLAlchemyTaskExecutor`](.././flytekitplugins.sqlalchemy.task#flytekitpluginssqlalchemytasksqlalchemytaskexecutor) |  |

## flytekitplugins.sqlalchemy.task.SQLAlchemyConfig

Use this configuration to configure task. String should be standard
sqlalchemy connector format
(https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls).
Database can be found:
- within the container
- or from a publicly accessible source



```python
class SQLAlchemyConfig(
    uri: str,
    connect_args: typing.Optional[typing.Dict[str, typing.Any]],
    secret_connect_args: typing.Optional[typing.Dict[str, flytekit.models.security.Secret]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `uri` | `str` | default sqlalchemy connector |
| `connect_args` | `typing.Optional[typing.Dict[str, typing.Any]]` | |
| `secret_connect_args` | `typing.Optional[typing.Dict[str, flytekit.models.security.Secret]]` | flyte secrets loaded into sqlalchemy connect args -- ex: {"password": flytekit.models.security.Secret(name=SECRET_NAME, group=SECRET_GROUP)} |

### Methods

| Method | Description |
|-|-|
| [`secret_connect_args_to_dicts()`](#secret_connect_args_to_dicts) |  |


#### secret_connect_args_to_dicts()

```python
def secret_connect_args_to_dicts()
```
## flytekitplugins.sqlalchemy.task.SQLAlchemyDefaultImages

Default images for the sqlalchemy flytekit plugin.


### Methods

| Method | Description |
|-|-|
| [`default_image()`](#default_image) |  |
| [`find_image_for()`](#find_image_for) |  |
| [`get_version_suffix()`](#get_version_suffix) |  |


#### default_image()

```python
def default_image()
```
#### find_image_for()

```python
def find_image_for(
    python_version: typing.Optional[flytekit.configuration.default_images.PythonVersion],
    flytekit_version: typing.Optional[str],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `python_version` | `typing.Optional[flytekit.configuration.default_images.PythonVersion]` | |
| `flytekit_version` | `typing.Optional[str]` | |

#### get_version_suffix()

```python
def get_version_suffix()
```
## flytekitplugins.sqlalchemy.task.SQLAlchemyTask

Makes it possible to run client side SQLAlchemy queries that optionally return a FlyteSchema object



```python
class SQLAlchemyTask(
    name: str,
    query_template: str,
    task_config: flytekitplugins.sqlalchemy.task.SQLAlchemyConfig,
    inputs: typing.Optional[typing.Dict[str, typing.Type]],
    output_schema_type: typing.Optional[typing.Type[flytekit.types.schema.types.FlyteSchema]],
    container_image: str,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | unique name for the task, usually the function's module and name. |
| `query_template` | `str` | |
| `task_config` | `flytekitplugins.sqlalchemy.task.SQLAlchemyConfig` | Configuration object for Task. Should be a unique type for that specific Task |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Type]]` | |
| `output_schema_type` | `typing.Optional[typing.Type[flytekit.types.schema.types.FlyteSchema]]` | |
| `container_image` | `str` | This is the external container image the task should run at platform-run-time. |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `container_image` | `None` |  |
| `deck_fields` | `None` | If not empty, this task will output deck html file for the specified decks |
| `disable_deck` | `None` | If true, this task will not output deck html file |
| `docs` | `None` |  |
| `enable_deck` | `None` | If true, this task will output deck html file |
| `environment` | `None` | Any environment variables that supplied during the execution of the task. |
| `executor` | `None` |  |
| `executor_type` | `None` |  |
| `instantiated_in` | `None` |  |
| `interface` | `None` |  |
| `lhs` | `None` |  |
| `location` | `None` |  |
| `metadata` | `None` |  |
| `name` | `None` | Return the name of the underlying task. |
| `output_columns` | `None` |  |
| `python_interface` | `None` | Returns this task's python interface. |
| `query_template` | `None` |  |
| `resources` | `None` |  |
| `security_context` | `None` |  |
| `task_config` | `None` | Returns the user-specified task config which is used for plugin-specific handling of the task. |
| `task_resolver` | `None` |  |
| `task_template` | `None` | Override the base class implementation to serialize on first call. |
| `task_type` | `None` |  |
| `task_type_version` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This function is largely similar to the base PythonTask, with the exception that we have to infer the Python. |
| [`execute()`](#execute) | Rather than running here, send everything to the executor. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_command()`](#get_command) |  |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_image()`](#get_image) |  |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_query()`](#get_query) |  |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`interpolate_query()`](#interpolate_query) | This function will fill in the query template with the provided kwargs and return the interpolated query. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask. |
| [`pre_execute()`](#pre_execute) | This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
| [`serialize_to_model()`](#serialize_to_model) |  |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
Generates a node that encapsulates this task in a workflow definition.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### dispatch_execute()

```python
def dispatch_execute(
    ctx: FlyteContext,
    input_literal_map: _literal_models.LiteralMap,
) -> Union[_literal_models.LiteralMap, _dynamic_job.DynamicJobSpec]
```
This function is largely similar to the base PythonTask, with the exception that we have to infer the Python
interface before executing. Also, we refer to ``self.task_template`` rather than just ``self`` similar to task
classes that derive from the base ``PythonTask``.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `input_literal_map` | `_literal_models.LiteralMap` | |

#### execute()

```python
def execute(
    kwargs,
) -> Any
```
Rather than running here, send everything to the executor.


| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

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
| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

#### get_config()

```python
def get_config(
    settings: SerializationSettings,
) -> Dict[str, str]
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

#### get_container()

```python
def get_container(
    settings: SerializationSettings,
) -> _task_model.Container
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Dict[str, typing.Any]
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_image()

```python
def get_image(
    settings: SerializationSettings,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.K8sPod]
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_query()

```python
def get_query(
    kwargs,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.Sql]
```
Returns the Sql definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_type_for_input_var()

```python
def get_type_for_input_var(
    k: str,
    v: typing.Any,
) -> typing.Type[typing.Any]
```
Returns the python type for an input variable by name.


| Parameter | Type | Description |
|-|-|-|
| `k` | `str` | |
| `v` | `typing.Any` | |

#### get_type_for_output_var()

```python
def get_type_for_output_var(
    k: str,
    v: typing.Any,
) -> typing.Type[typing.Any]
```
Returns the python type for the specified output variable by name.


| Parameter | Type | Description |
|-|-|-|
| `k` | `str` | |
| `v` | `typing.Any` | |

#### interpolate_query()

```python
def interpolate_query(
    query_template,
    kwargs,
) -> typing.Any
```
This function will fill in the query template with the provided kwargs and return the interpolated query.
Please note that when SQL tasks run in Flyte, this step is done by the task executor.


| Parameter | Type | Description |
|-|-|-|
| `query_template` |  | |
| `kwargs` | `**kwargs` | |

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


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `kwargs` | `**kwargs` | |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### post_execute()

```python
def post_execute(
    _: Optional[ExecutionParameters],
    rval: Any,
) -> Any
```
This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask.


| Parameter | Type | Description |
|-|-|-|
| `_` | `Optional[ExecutionParameters]` | |
| `rval` | `Any` | |

#### pre_execute()

```python
def pre_execute(
    user_params: Optional[ExecutionParameters],
) -> Optional[ExecutionParameters]
```
This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask.


| Parameter | Type | Description |
|-|-|-|
| `user_params` | `Optional[ExecutionParameters]` | |

#### sandbox_execute()

```python
def sandbox_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` | |

#### serialize_to_model()

```python
def serialize_to_model(
    settings: SerializationSettings,
) -> _task_model.TaskTemplate
```
| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

## flytekitplugins.sqlalchemy.task.SQLAlchemyTaskExecutor

```python
class SQLAlchemyTaskExecutor(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `instantiated_in` | `None` |  |
| `lhs` | `None` |  |
| `location` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`execute_from_model()`](#execute_from_model) | This function must be overridden and is where all the business logic for running a task should live. |
| [`find_lhs()`](#find_lhs) |  |


#### execute_from_model()

```python
def execute_from_model(
    tt: flytekit.models.task.TaskTemplate,
    kwargs,
) -> typing.Any
```
This function must be overridden and is where all the business logic for running a task should live. Keep in
mind that you're only working with the ``TaskTemplate``. You won't have access to any information in the task
that wasn't serialized into the template.



| Parameter | Type | Description |
|-|-|-|
| `tt` | `flytekit.models.task.TaskTemplate` | This is the template, the serialized form of the task. |
| `kwargs` | `**kwargs` | These are the Python native input values to the task. :return: Python native output values from the task. |

#### find_lhs()

```python
def find_lhs()
```
