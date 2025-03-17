---
title: WebhookTask
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# WebhookTask

**Package:** `flytekit.extras.webhook`

The WebhookTask is used to invoke a webhook. The webhook can be invoked with a POST or GET method.

All the parameters can be formatted using python format strings.

Example:
```python
simple_get = WebhookTask(
name="simple-get",
url="http://localhost:8000/",
method=http.HTTPMethod.GET,
headers={"Content-Type": "application/json"},


with_params = WebhookTask(
name="get-with-params",
url="http://localhost:8000/items/{inputs.item_id}",
method=http.HTTPMethod.GET,
headers={"Content-Type": "application/json"},
dynamic_inputs={"s": str, "item_id": int},
show_data=True,
show_url=True,
description="Test Webhook Task",
data={"q": "{inputs.s}"},



workflow
wf(s: str) -> (dict, dict, dict):
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
def WebhookTask(
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
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `name` | `str` |
| `url` | `str` |
| `method` | `str` |
| `headers` | `typing.Optional[typing.Dict[str, str]]` |
| `data` | `typing.Optional[typing.Dict[str, typing.Any]]` |
| `dynamic_inputs` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `show_data` | `bool` |
| `show_url` | `bool` |
| `description` | `typing.Optional[str]` |
| `timeout` | `typing.Union[int, datetime.timedelta]` |
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
### execute()

```python
def execute(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |
### find_lhs()

```python
def find_lhs()
```
No parameters
### get_config()

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
### get_container()

```python
def get_container(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
):
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
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
### pre_execute()

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
