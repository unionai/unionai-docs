---
title: PythonCustomizedContainerTask
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# PythonCustomizedContainerTask

**Package:** `flytekit.extend`

Please take a look at the comments for :py:class`flytekit.extend.ExecutableTemplateShimTask` as well. This class
should be subclassed and a custom Executor provided as a default to this parent class constructor
when building a new external-container flytekit-only plugin.

This class provides authors of new task types the basic scaffolding to create task-template based tasks. In order
to write such a task, authors need to

* subclass the ``ShimTaskExecutor`` class  and override the ``execute_from_model`` function. This function is
where all the business logic should go. Keep in mind though that you, the plugin author, will not have access
to anything that's not serialized within the ``TaskTemplate`` which is why you'll also need to
* subclass this class, and override the ``get_custom`` function to include all the information the executor
will need to run.
* Also pass the executor you created as the ``executor_type`` argument of this class's constructor.

Keep in mind that the total size of the ``TaskTemplate`` still needs to be small, since these will be accessed
frequently by the Flyte engine.


```python
def PythonCustomizedContainerTask(
    name: str,
    task_config: TC,
    container_image: str,
    executor_type: Type[ShimTaskExecutor],
    task_resolver: Optional[TaskTemplateResolver],
    task_type,
    requests: Optional[Resources],
    limits: Optional[Resources],
    environment: Optional[Dict[str, str]],
    secret_requests: Optional[List[Secret]],
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `task_config` | `TC` |
| `container_image` | `str` |
| `executor_type` | `Type[ShimTaskExecutor]` |
| `task_resolver` | `Optional[TaskTemplateResolver]` |
| `task_type` |  |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `environment` | `Optional[Dict[str, str]]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `kwargs` | ``**kwargs`` |
## Methods

### compile()

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
### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


No parameters
### dispatch_execute()

```python
def dispatch_execute(
    ctx: FlyteContext,
    input_literal_map: _literal_models.LiteralMap,
):
```
This function is largely similar to the base PythonTask, with the exception that we have to infer the Python
interface before executing. Also, we refer to ``self.task_template`` rather than just ``self`` similar to task
classes that derive from the base ``PythonTask``.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `input_literal_map` | `_literal_models.LiteralMap` |
### execute()

```python
def execute(
    kwargs,
):
```
Rather than running here, send everything to the executor.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |
### find_lhs()

```python
def find_lhs()
```
No parameters
### get_command()

```python
def get_command(
    settings: SerializationSettings,
):
```
| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |
### get_config()

```python
def get_config(
    settings: SerializationSettings,
):
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |
### get_container()

```python
def get_container(
    settings: SerializationSettings,
):
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |
### get_custom()

```python
def get_custom(
    settings: SerializationSettings,
):
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |
### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
### get_image()

```python
def get_image(
    settings: SerializationSettings,
):
```
| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |
### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


No parameters
### get_k8s_pod()

```python
def get_k8s_pod(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the Sql definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
### get_type_for_input_var()

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
### get_type_for_output_var()

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
### local_execute()

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
### local_execution_mode()

```python
def local_execution_mode()
```
No parameters
### post_execute()

```python
def post_execute(
    _: Optional[ExecutionParameters],
    rval: Any,
):
```
This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask.


| Parameter | Type |
|-|-|
| `_` | `Optional[ExecutionParameters]` |
| `rval` | `Any` |
### pre_execute()

```python
def pre_execute(
    user_params: Optional[ExecutionParameters],
):
```
This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask.


| Parameter | Type |
|-|-|
| `user_params` | `Optional[ExecutionParameters]` |
### sandbox_execute()

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
### serialize_to_model()

```python
def serialize_to_model(
    settings: SerializationSettings,
):
```
| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |
