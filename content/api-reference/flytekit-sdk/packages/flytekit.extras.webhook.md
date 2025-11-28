---
title: flytekit.extras.webhook
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extras.webhook

## Directory

### Classes

| Class | Description |
|-|-|
| [`WebhookConnector`](.././flytekit.extras.webhook#flytekitextraswebhookwebhookconnector) | WebhookConnector is responsible for handling webhook tasks. |
| [`WebhookTask`](.././flytekit.extras.webhook#flytekitextraswebhookwebhooktask) | The WebhookTask is used to invoke a webhook. |

## flytekit.extras.webhook.WebhookConnector

WebhookConnector is responsible for handling webhook tasks.

This connector sends HTTP requests based on the task template and inputs provided,
and processes the responses to determine the success or failure of the task.



```python
class WebhookConnector(
    client: typing.Optional[httpx.AsyncClient],
)
```
| Parameter | Type | Description |
|-|-|-|
| `client` | `typing.Optional[httpx.AsyncClient]` | |

### Methods

| Method | Description |
|-|-|
| [`do()`](#do) | This method processes the webhook task and sends an HTTP request. |


#### do()

```python
def do(
    task_template: flytekit.models.task.TaskTemplate,
    output_prefix: str,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
This method processes the webhook task and sends an HTTP request.

It uses asyncio to send the request and process the response using the httpx library.


| Parameter | Type | Description |
|-|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` | |
| `output_prefix` | `str` | |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` | |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `task_category` |  | {{< multiline >}}task category that the connector supports
{{< /multiline >}} |

## flytekit.extras.webhook.WebhookTask

The WebhookTask is used to invoke a webhook. The webhook can be invoked with a POST or GET method.

All the parameters can be formatted using python format strings.

Example:
```python
simple_get = WebhookTask(
name="simple-get",
url="http://localhost:8000/",
method=http.HTTPMethod.GET,
headers={"Content-Type": "application/json"},
)

get_with_params = WebhookTask(
    name="get-with-params",
    url="http://localhost:8000/items/{inputs.item_id}",
    method=http.HTTPMethod.GET,
    headers={"Content-Type": "application/json"},
    dynamic_inputs={"s": str, "item_id": int},
    show_data=True,
    show_url=True,
    description="Test Webhook Task",
    data={"q": "{inputs.s}"},
)


@fk.workflow
def wf(s: str) -> (dict, dict, dict):
    v = hello(s=s)
    w = WebhookTask(
        name="invoke-slack",
        url="https://hooks.slack.com/services/xyz/zaa/aaa",
        headers={"Content-Type": "application/json"},
        data={"text": "{inputs.s}"},
        show_data=True,
        show_url=True,
        description="Test Webhook Task",
        dynamic_inputs={"s": str},
    )
    return simple_get(), get_with_params(s=v, item_id=10), w(s=v)
```

 All the parameters can be formatted using python format strings. The following parameters are available for
formatting:
- dynamic_inputs: These are the dynamic inputs to the task. The keys are the names of the inputs and the values
    are the values of the inputs. All inputs are available under the prefix `inputs.`.
    For example, if the inputs are {"input1": 10, "input2": "hello"}, then you can
    use {inputs.input1} and {inputs.input2} in the URL and the body. Define the dynamic_inputs argument in the
    constructor to use these inputs. The dynamic inputs should not be actual values, but the types of the inputs.

TODO Coming soon secrets support
- secrets: These are the secrets that are requested by the task. The keys are the names of the secrets and the
    values are the values of the secrets. All secrets are available under the prefix `secrets.`.
    For example, if the secret requested are Secret(name="secret1") and Secret(name="secret), then you can use
    {secrets.secret1} and {secrets.secret2} in the URL and the body. Define the secret_requests argument in the
    constructor to use these secrets. The secrets should not be actual values, but the types of the secrets.



```python
class WebhookTask(
    name: str,
    url: str,
    method: str,
    headers: typing.Optional[typing.Dict[str, str]],
    data: typing.Optional[typing.Dict[str, typing.Any]],
    dynamic_inputs: typing.Optional[typing.Dict[str, typing.Type]],
    show_data: bool,
    show_url: bool,
    description: typing.Optional[str],
    timeout: typing.Union[int, datetime.timedelta],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `url` | `str` | |
| `method` | `str` | |
| `headers` | `typing.Optional[typing.Dict[str, str]]` | |
| `data` | `typing.Optional[typing.Dict[str, typing.Any]]` | |
| `dynamic_inputs` | `typing.Optional[typing.Dict[str, typing.Type]]` | |
| `show_data` | `bool` | |
| `show_url` | `bool` | |
| `description` | `typing.Optional[str]` | |
| `timeout` | `typing.Union[int, datetime.timedelta]` | |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
| [`execute()`](#execute) |  |
| [`find_lhs()`](#find_lhs) |  |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up,. |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |


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


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` | |

#### execute()

```python
def execute(
    kwargs,
) -> flytekit.models.literals.LiteralMap
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

#### find_lhs()

```python
def find_lhs()
```
#### get_config()

```python
def get_config(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[typing.Dict[str, str]]
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_container()

```python
def get_container(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.Container]
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

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
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
    rval: typing.Any,
) -> typing.Any
```
Post execute is called after the execution has completed, with the user_params and can be used to clean-up,
or alter the outputs to match the intended tasks outputs. If not overridden, then this function is a No-op



| Parameter | Type | Description |
|-|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` | are the modified user params as created during the pre_execute step |
| `rval` | `typing.Any` | |

#### pre_execute()

```python
def pre_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
) -> typing.Optional[flytekit.core.context_manager.ExecutionParameters]
```
This is the method that will be invoked directly before executing the task method and before all the inputs
are converted. One particular case where this is useful is if the context is to be modified for the user process
to get some user space parameters. This also ensures that things like SparkSession are already correctly
setup before the type transformers are called

This should return either the same context of the mutated context


| Parameter | Type | Description |
|-|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` | |

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

### Properties

| Property | Type | Description |
|-|-|-|
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
| `python_interface` |  | {{< multiline >}}Returns this task's python interface.
{{< /multiline >}} |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

