---
title: flytekit.sensor.sensor_engine
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.sensor.sensor_engine

## Directory

### Classes

| Class | Description |
|-|-|
| [`AgentRegistry`](.././flytekit.sensor.sensor_engine#flytekitsensorsensor_engineagentregistry) | This is the registry for all agents. |
| [`AsyncAgentBase`](.././flytekit.sensor.sensor_engine#flytekitsensorsensor_engineasyncagentbase) | This is the base class for all async agents. |
| [`FlyteContextManager`](.././flytekit.sensor.sensor_engine#flytekitsensorsensor_engineflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`LiteralMap`](.././flytekit.sensor.sensor_engine#flytekitsensorsensor_engineliteralmap) | None. |
| [`Resource`](.././flytekit.sensor.sensor_engine#flytekitsensorsensor_engineresource) | This is the output resource of the job. |
| [`SensorEngine`](.././flytekit.sensor.sensor_engine#flytekitsensorsensor_enginesensorengine) | This is the base class for all async agents. |
| [`SensorMetadata`](.././flytekit.sensor.sensor_engine#flytekitsensorsensor_enginesensormetadata) | None. |
| [`TaskExecution`](.././flytekit.sensor.sensor_engine#flytekitsensorsensor_enginetaskexecution) | A ProtocolMessage. |
| [`TaskTemplate`](.././flytekit.sensor.sensor_engine#flytekitsensorsensor_enginetasktemplate) | None. |
| [`TypeEngine`](.././flytekit.sensor.sensor_engine#flytekitsensorsensor_enginetypeengine) | Core Extensible TypeEngine of Flytekit. |

## flytekit.sensor.sensor_engine.AgentRegistry

This is the registry for all agents.
The agent service will look up the agent registry based on the task type.
The agent metadata service will look up the agent metadata based on the agent name.


### Methods

| Method | Description |
|-|-|
| [`get_agent()`](#get_agent) | None |
| [`get_agent_metadata()`](#get_agent_metadata) | None |
| [`list_agents()`](#list_agents) | None |
| [`register()`](#register) | None |


#### get_agent()

```python
def get_agent(
    task_type_name: str,
    task_type_version: int,
):
```
| Parameter | Type |
|-|-|
| `task_type_name` | `str` |
| `task_type_version` | `int` |

#### get_agent_metadata()

```python
def get_agent_metadata(
    name: str,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |

#### list_agents()

```python
def list_agents()
```
#### register()

```python
def register(
    agent: typing.Union[flytekit.extend.backend.base_agent.AsyncAgentBase, flytekit.extend.backend.base_agent.SyncAgentBase],
    override: bool,
):
```
| Parameter | Type |
|-|-|
| `agent` | `typing.Union[flytekit.extend.backend.base_agent.AsyncAgentBase, flytekit.extend.backend.base_agent.SyncAgentBase]` |
| `override` | `bool` |

## flytekit.sensor.sensor_engine.AsyncAgentBase

This is the base class for all async agents. It defines the interface that all agents must implement.
The agent service is responsible for invoking agents. The propeller will communicate with the agent service
to create tasks, get the status of tasks, and delete tasks.

All the agents should be registered in the AgentRegistry. Agent Service
will look up the agent based on the task type. Every task type can only have one agent.


```python
def AsyncAgentBase(
    metadata_type: flytekit.extend.backend.base_agent.ResourceMeta,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `metadata_type` | `flytekit.extend.backend.base_agent.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Return a resource meta that can be used to get the status of the task |
| [`delete()`](#delete) | Delete the task |
| [`get()`](#get) | Return the status of the task, and return the outputs in some cases |


#### create()

```python
def create(
    task_template: flytekit.models.task.TaskTemplate,
    output_prefix: str,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    task_execution_metadata: typing.Optional[flytekit.models.task.TaskExecutionMetadata],
    kwargs,
):
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `output_prefix` | `str` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `task_execution_metadata` | `typing.Optional[flytekit.models.task.TaskExecutionMetadata]` |
| `kwargs` | ``**kwargs`` |

#### delete()

```python
def delete(
    resource_meta: flytekit.extend.backend.base_agent.ResourceMeta,
    kwargs,
):
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_agent.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

#### get()

```python
def get(
    resource_meta: flytekit.extend.backend.base_agent.ResourceMeta,
    kwargs,
):
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_agent.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| metadata_type |  |  |
| task_category |  |  |

## flytekit.sensor.sensor_engine.FlyteContextManager

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

## flytekit.sensor.sensor_engine.LiteralMap

```python
def LiteralMap(
    literals,
):
```
| Parameter | Type |
|-|-|
| `literals` |  |

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
| literals |  |  |

## flytekit.sensor.sensor_engine.Resource

This is the output resource of the job.



```python
def Resource(
    phase: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1060829f0>,
    message: typing.Optional[str],
    log_links: typing.Optional[typing.List[flyteidl.core.execution_pb2.TaskLog]],
    outputs: typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, typing.Any], NoneType],
    custom_info: typing.Optional[typing.Dict[str, typing.Any]],
):
```
| Parameter | Type |
|-|-|
| `phase` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1060829f0>` |
| `message` | `typing.Optional[str]` |
| `log_links` | `typing.Optional[typing.List[flyteidl.core.execution_pb2.TaskLog]]` |
| `outputs` | `typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, typing.Any], NoneType]` |
| `custom_info` | `typing.Optional[typing.Dict[str, typing.Any]]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`to_flyte_idl()`](#to_flyte_idl) | This function is async to call the async type engine functions |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.agent_pb2.Resource,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.admin.agent_pb2.Resource` |

#### to_flyte_idl()

```python
def to_flyte_idl()
```
This function is async to call the async type engine functions. This is okay to do because this is not a
normal model class that inherits from FlyteIdlEntity


## flytekit.sensor.sensor_engine.SensorEngine

This is the base class for all async agents. It defines the interface that all agents must implement.
The agent service is responsible for invoking agents. The propeller will communicate with the agent service
to create tasks, get the status of tasks, and delete tasks.

All the agents should be registered in the AgentRegistry. Agent Service
will look up the agent based on the task type. Every task type can only have one agent.


```python
def SensorEngine()
```
### Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Return a resource meta that can be used to get the status of the task |
| [`delete()`](#delete) | Delete the task |
| [`get()`](#get) | Return the status of the task, and return the outputs in some cases |


#### create()

```python
def create(
    task_template: flytekit.models.task.TaskTemplate,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwarg,
):
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `kwarg` |  |

#### delete()

```python
def delete(
    resource_meta: flytekit.sensor.base_sensor.SensorMetadata,
    kwargs,
):
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.sensor.base_sensor.SensorMetadata` |
| `kwargs` | ``**kwargs`` |

#### get()

```python
def get(
    resource_meta: flytekit.sensor.base_sensor.SensorMetadata,
    kwargs,
):
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.sensor.base_sensor.SensorMetadata` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| metadata_type |  |  |
| task_category |  |  |

## flytekit.sensor.sensor_engine.SensorMetadata

```python
def SensorMetadata(
    sensor_module: str,
    sensor_name: str,
    sensor_config: typing.Optional[dict],
    inputs: typing.Optional[dict],
):
```
| Parameter | Type |
|-|-|
| `sensor_module` | `str` |
| `sensor_name` | `str` |
| `sensor_config` | `typing.Optional[dict]` |
| `inputs` | `typing.Optional[dict]` |

### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | Decode the resource meta from bytes |
| [`encode()`](#encode) | Encode the resource meta to bytes |


#### decode()

```python
def decode(
    data: bytes,
):
```
Decode the resource meta from bytes.


| Parameter | Type |
|-|-|
| `data` | `bytes` |

#### encode()

```python
def encode()
```
Encode the resource meta to bytes.


## flytekit.sensor.sensor_engine.TaskExecution

A ProtocolMessage


## flytekit.sensor.sensor_engine.TaskTemplate

```python
def TaskTemplate(
    id,
    type,
    metadata,
    interface,
    custom,
    container,
    task_type_version,
    security_context,
    config,
    k8s_pod,
    sql,
    extended_resources,
):
```
A task template represents the full set of information necessary to perform a unit of work in the Flyte system.
It contains the metadata about what inputs and outputs are consumed or produced.  It also contains the metadata
necessary for Flyte Propeller to do the appropriate work.



| Parameter | Type |
|-|-|
| `id` |  |
| `type` |  |
| `metadata` |  |
| `interface` |  |
| `custom` |  |
| `container` |  |
| `task_type_version` |  |
| `security_context` |  |
| `config` |  |
| `k8s_pod` |  |
| `sql` |  |
| `extended_resources` |  |

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
| config |  |  |
| container |  |  |
| custom |  |  |
| extended_resources |  |  |
| id |  |  |
| interface |  |  |
| is_empty |  |  |
| k8s_pod |  |  |
| metadata |  |  |
| security_context |  |  |
| sql |  |  |
| task_type_version |  |  |
| type |  |  |

## flytekit.sensor.sensor_engine.TypeEngine

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

