---
title: flytekit.core.interface
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.interface

## Directory

### Classes

| Class | Description |
|-|-|
| [`Any`](.././flytekit.core.interface#flytekitcoreinterfaceany) | Special type indicating an unconstrained type. |
| [`Artifact`](.././flytekit.core.interface#flytekitcoreinterfaceartifact) | An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`ArtifactIDSpecification`](.././flytekit.core.interface#flytekitcoreinterfaceartifactidspecification) | This is a special object that helps specify how Artifacts are to be created. |
| [`ArtifactQuery`](.././flytekit.core.interface#flytekitcoreinterfaceartifactquery) | None. |
| [`Docstring`](.././flytekit.core.interface#flytekitcoreinterfacedocstring) | None. |
| [`FlyteContextManager`](.././flytekit.core.interface#flytekitcoreinterfaceflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`Interface`](.././flytekit.core.interface#flytekitcoreinterfaceinterface) | A Python native interface object, like inspect. |
| [`Literal`](.././flytekit.core.interface#flytekitcoreinterfaceliteral) | None. |
| [`OrderedDict`](.././flytekit.core.interface#flytekitcoreinterfaceordereddict) | Dictionary that remembers insertion order. |
| [`Scalar`](.././flytekit.core.interface#flytekitcoreinterfacescalar) | None. |
| [`TypeEngine`](.././flytekit.core.interface#flytekitcoreinterfacetypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`TypeVar`](.././flytekit.core.interface#flytekitcoreinterfacetypevar) | Type variable. |
| [`UnionTransformer`](.././flytekit.core.interface#flytekitcoreinterfaceuniontransformer) | Transformer that handles a typing. |
| [`Void`](.././flytekit.core.interface#flytekitcoreinterfacevoid) | None. |

### Errors

* [`FlyteMissingReturnValueException`](.././flytekit.core.interface#flytekitcoreinterfaceflytemissingreturnvalueexception)
* [`FlyteMissingTypeException`](.././flytekit.core.interface#flytekitcoreinterfaceflytemissingtypeexception)
* [`FlyteValidationException`](.././flytekit.core.interface#flytekitcoreinterfaceflytevalidationexception)

## flytekit.core.interface.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.core.interface.Artifact

An Artifact is effectively just a metadata layer on top of data that exists in Flyte. Most data of interest
will be the output of tasks and workflows. The other category is user uploads.

This Python class has limited purpose, as a way for users to specify that tasks/workflows create Artifacts
and the manner (i.e. name, partitions) in which they are created.

Control creation parameters at task/workflow execution time ::

@task
def t1() -> Annotated[nn.Module, Artifact(name="my.artifact.name")]:
...


```python
def Artifact(
    project: Optional[str],
    domain: Optional[str],
    name: Optional[str],
    version: Optional[str],
    time_partitioned: bool,
    time_partition: Optional[TimePartition],
    time_partition_granularity: Optional[Granularity],
    partition_keys: Optional[typing.List[str]],
    partitions: Optional[Union[Partitions, typing.Dict[str, str]]],
):
```
| Parameter | Type |
|-|-|
| `project` | `Optional[str]` |
| `domain` | `Optional[str]` |
| `name` | `Optional[str]` |
| `version` | `Optional[str]` |
| `time_partitioned` | `bool` |
| `time_partition` | `Optional[TimePartition]` |
| `time_partition_granularity` | `Optional[Granularity]` |
| `partition_keys` | `Optional[typing.List[str]]` |
| `partitions` | `Optional[Union[Partitions, typing.Dict[str, str]]]` |

### Methods

| Method | Description |
|-|-|
| [`create_from()`](#create_from) | This function allows users to declare partition values dynamically from the body of a task |
| [`embed_as_query()`](#embed_as_query) | This should only be called in the context of a Trigger |
| [`query()`](#query) | None |
| [`to_id_idl()`](#to_id_idl) | Converts this object to the IDL representation |


#### create_from()

```python
def create_from(
    o: O,
    card: Optional[SerializableToString],
    args: `*args`,
    kwargs,
):
```
This function allows users to declare partition values dynamically from the body of a task. Note that you'll
still need to annotate your task function output with the relevant Artifact object. Below, one of the partition
values is bound to an input, and the other is set at runtime. Note that since tasks are not run at compile
time, flytekit cannot check that you've bound all the partition values. It's up to you to ensure that you've
done so.

Pricing = Artifact(name="pricing", partition_keys=["region"])
EstError = Artifact(name="estimation_error", partition_keys=["dataset"], time_partitioned=True)

@task
def t1() -> Annotated[pd.DataFrame, Pricing], Annotated[float, EstError]:
df = get_pricing_results()
dt = get_time()
return Pricing.create_from(df, region="dubai"),             EstError.create_from(msq_error, dataset="train", time_partition=dt)

You can mix and match with the input syntax as well.

@task
def my_task() -> Annotated[pd.DataFrame, RideCountData(region=Inputs.region)]:
...
return RideCountData.create_from(df, time_partition=datetime.datetime.now())


| Parameter | Type |
|-|-|
| `o` | `O` |
| `card` | `Optional[SerializableToString]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### embed_as_query()

```python
def embed_as_query(
    partition: Optional[str],
    bind_to_time_partition: Optional[bool],
    expr: Optional[str],
    op: Optional[Op],
):
```
This should only be called in the context of a Trigger. The type of query this returns is different from the
query() function. This type of query is used to reference the triggering artifact, rather than running a query.


| Parameter | Type |
|-|-|
| `partition` | `Optional[str]` |
| `bind_to_time_partition` | `Optional[bool]` |
| `expr` | `Optional[str]` |
| `op` | `Optional[Op]` |

#### query()

```python
def query(
    project: Optional[str],
    domain: Optional[str],
    time_partition: Optional[Union[datetime.datetime, TimePartition, art_id.InputBindingData]],
    partitions: Optional[Union[typing.Dict[str, str], Partitions]],
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `project` | `Optional[str]` |
| `domain` | `Optional[str]` |
| `time_partition` | `Optional[Union[datetime.datetime, TimePartition, art_id.InputBindingData]]` |
| `partitions` | `Optional[Union[typing.Dict[str, str], Partitions]]` |
| `kwargs` | ``**kwargs`` |

#### to_id_idl()

```python
def to_id_idl()
```
Converts this object to the IDL representation.
This is here instead of translator because it's in the interface, a relatively simple proto object
that's exposed to the user.


### Properties

| Property | Type | Description |
|-|-|-|
| concrete_artifact_id |  |  |
| partitions |  |  |
| time_partition |  |  |

## flytekit.core.interface.ArtifactIDSpecification

This is a special object that helps specify how Artifacts are to be created. See the comment in the
call function of the main Artifact class. Also see the handling code in transform_variable_map for more
information. There's a limited set of information that we ultimately need in a TypedInterface, so it
doesn't make sense to carry the full Artifact object around. This object should be sufficient, despite
having a pointer to the main artifact.


```python
def ArtifactIDSpecification(
    a: Artifact,
):
```
| Parameter | Type |
|-|-|
| `a` | `Artifact` |

### Methods

| Method | Description |
|-|-|
| [`bind_partitions()`](#bind_partitions) | None |
| [`to_partial_artifact_id()`](#to_partial_artifact_id) | None |


#### bind_partitions()

```python
def bind_partitions(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### to_partial_artifact_id()

```python
def to_partial_artifact_id()
```
## flytekit.core.interface.ArtifactQuery

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

## flytekit.core.interface.Docstring

```python
def Docstring(
    docstring: typing.Optional[str],
    callable_: typing.Optional[typing.Callable],
):
```
| Parameter | Type |
|-|-|
| `docstring` | `typing.Optional[str]` |
| `callable_` | `typing.Optional[typing.Callable]` |

### Properties

| Property | Type | Description |
|-|-|-|
| input_descriptions |  |  |
| long_description |  |  |
| output_descriptions |  |  |
| short_description |  |  |

## flytekit.core.interface.FlyteContextManager

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

## flytekit.core.interface.FlyteMissingReturnValueException

Common base class for all non-exit exceptions.


```python
def FlyteMissingReturnValueException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.core.interface.FlyteMissingTypeException

Common base class for all non-exit exceptions.


```python
def FlyteMissingTypeException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.core.interface.FlyteValidationException

Assertion failed.


```python
def FlyteValidationException(
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

## flytekit.core.interface.Interface

A Python native interface object, like inspect.signature but simpler.


```python
def Interface(
    inputs: Union[Optional[Dict[str, Type]], Optional[Dict[str, Tuple[Type, Any]]]],
    outputs: Union[Optional[Dict[str, Type]], Optional[Dict[str, Optional[Type]]]],
    output_tuple_name: Optional[str],
    docstring: Optional[Docstring],
):
```
| Parameter | Type |
|-|-|
| `inputs` | `Union[Optional[Dict[str, Type]], Optional[Dict[str, Tuple[Type, Any]]]]` |
| `outputs` | `Union[Optional[Dict[str, Type]], Optional[Dict[str, Optional[Type]]]]` |
| `output_tuple_name` | `Optional[str]` |
| `docstring` | `Optional[Docstring]` |

### Methods

| Method | Description |
|-|-|
| [`remove_inputs()`](#remove_inputs) | This method is useful in removing some variables from the Flyte backend inputs specification, as these are |
| [`with_inputs()`](#with_inputs) | Use this to add additional inputs to the interface |
| [`with_outputs()`](#with_outputs) | This method allows addition of extra outputs are expected from a task specification |


#### remove_inputs()

```python
def remove_inputs(
    vars: Optional[List[str]],
):
```
This method is useful in removing some variables from the Flyte backend inputs specification, as these are
implicit local only inputs or will be supplied by the library at runtime. For example, spark-session etc
It creates a new instance of interface with the requested variables removed


| Parameter | Type |
|-|-|
| `vars` | `Optional[List[str]]` |

#### with_inputs()

```python
def with_inputs(
    extra_inputs: Dict[str, Type],
):
```
Use this to add additional inputs to the interface. This is useful for adding additional implicit inputs that
are added without the user requesting for them


| Parameter | Type |
|-|-|
| `extra_inputs` | `Dict[str, Type]` |

#### with_outputs()

```python
def with_outputs(
    extra_outputs: Dict[str, Type],
):
```
This method allows addition of extra outputs are expected from a task specification


| Parameter | Type |
|-|-|
| `extra_outputs` | `Dict[str, Type]` |

### Properties

| Property | Type | Description |
|-|-|-|
| default_inputs_as_kwargs |  |  |
| docstring |  |  |
| inputs |  |  |
| inputs_with_defaults |  |  |
| output_names |  |  |
| output_tuple |  |  |
| output_tuple_name |  |  |
| outputs |  |  |

## flytekit.core.interface.Literal

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

## flytekit.core.interface.OrderedDict

Dictionary that remembers insertion order


## flytekit.core.interface.Scalar

```python
def Scalar(
    primitive: typing.Optional[flytekit.models.literals.Primitive],
    blob: typing.Optional[flytekit.models.literals.Blob],
    binary: typing.Optional[flytekit.models.literals.Binary],
    schema: typing.Optional[flytekit.models.literals.Schema],
    union: typing.Optional[flytekit.models.literals.Union],
    none_type: typing.Optional[flytekit.models.literals.Void],
    error: typing.Optional[flytekit.models.types.Error],
    generic: typing.Optional[google.protobuf.struct_pb2.Struct],
    structured_dataset: typing.Optional[flytekit.models.literals.StructuredDataset],
):
```
Scalar wrapper around Flyte types.  Only one can be specified.



| Parameter | Type |
|-|-|
| `primitive` | `typing.Optional[flytekit.models.literals.Primitive]` |
| `blob` | `typing.Optional[flytekit.models.literals.Blob]` |
| `binary` | `typing.Optional[flytekit.models.literals.Binary]` |
| `schema` | `typing.Optional[flytekit.models.literals.Schema]` |
| `union` | `typing.Optional[flytekit.models.literals.Union]` |
| `none_type` | `typing.Optional[flytekit.models.literals.Void]` |
| `error` | `typing.Optional[flytekit.models.types.Error]` |
| `generic` | `typing.Optional[google.protobuf.struct_pb2.Struct]` |
| `structured_dataset` | `typing.Optional[flytekit.models.literals.StructuredDataset]` |

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
| binary |  |  |
| blob |  |  |
| error |  |  |
| generic |  |  |
| is_empty |  |  |
| none_type |  |  |
| primitive |  |  |
| schema |  |  |
| structured_dataset |  |  |
| union |  |  |
| value |  |  |

## flytekit.core.interface.TypeEngine

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

## flytekit.core.interface.TypeVar

Type variable.

The preferred way to construct a type variable is via the dedicated
syntax for generic functions, classes, and type aliases::

class Sequence[T]:  # T is a TypeVar
...

This syntax can also be used to create bound and constrained type
variables::

# S is a TypeVar bound to str
class StrSequence[S: str]:
...

# A is a TypeVar constrained to str or bytes
class StrOrBytesSequence[A: (str, bytes)]:
...

However, if desired, reusable type variables can also be constructed
manually, like so::

T = TypeVar('T')  # Can be anything
S = TypeVar('S', bound=str)  # Can be any subtype of str
A = TypeVar('A', str, bytes)  # Must be exactly str or bytes

Type variables exist primarily for the benefit of static type
checkers.  They serve as the parameters for generic types as well
as for generic function and type alias definitions.

The variance of type variables is inferred by type checkers when they
are created through the type parameter syntax and when
``infer_variance=True`` is passed. Manually created type variables may
be explicitly marked covariant or contravariant by passing
``covariant=True`` or ``contravariant=True``. By default, manually
created type variables are invariant. See PEP 484 and PEP 695 for more
details.


## flytekit.core.interface.UnionTransformer

Transformer that handles a typing.Union[T1, T2, ...]


```python
def UnionTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) | None |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType |
| [`get_sub_type_in_optional()`](#get_sub_type_in_optional) | Return the generic Type T of the Optional type |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type |
| [`is_optional_type()`](#is_optional_type) | None |
| [`isinstance_generic()`](#isinstance_generic) | None |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type |


#### assert_type()

```python
def assert_type(
    t: Type[T],
    v: T,
):
```
| Parameter | Type |
|-|-|
| `t` | `Type[T]` |
| `v` | `T` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: T,
    python_type: Type[T],
    expected: LiteralType,
):
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
):
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
):
```
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access.｀

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
python val -> msgpack bytes -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
python val -> msgpack bytes -> binary literal scalar -> resolved golang value -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                            (propeller attribute access)                       (from_binary_idl)


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `Type[T]` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[T],
):
```
TODO: Support all Flyte Types.
This is for dataclass attribute access from input created from the Flyte Console.

Note:
- This can be removed in the future when the Flyte Console support generate Binary IDL Scalar as input.


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `Type[T]` |

#### get_literal_type()

```python
def get_literal_type(
    t: Type[T],
):
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### get_sub_type_in_optional()

```python
def get_sub_type_in_optional(
    t: Type[T],
):
```
Return the generic Type T of the Optional type


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
):
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### is_optional_type()

```python
def is_optional_type(
    t: Type,
):
```
| Parameter | Type |
|-|-|
| `t` | `Type` |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
):
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
):
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `expected_python_type` | `Type[T]` |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
):
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
):
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| is_async |  |  |
| name |  |  |
| python_type |  |  |
| type_assertions_enabled |  |  |

## flytekit.core.interface.Void

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
    proto,
):
```
| Parameter | Type |
|-|-|
| `proto` |  |

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

