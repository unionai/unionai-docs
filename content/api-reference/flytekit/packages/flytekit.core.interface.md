---
title: flytekit.core.interface
version: 0.1.dev2175+gcd6bd01.d20250325
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
| [`ArtifactQuery`](.././flytekit.core.interface#flytekitcoreinterfaceartifactquery) |  |
| [`Docstring`](.././flytekit.core.interface#flytekitcoreinterfacedocstring) |  |
| [`FlyteContextManager`](.././flytekit.core.interface#flytekitcoreinterfaceflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`Interface`](.././flytekit.core.interface#flytekitcoreinterfaceinterface) | A Python native interface object, like inspect. |
| [`Literal`](.././flytekit.core.interface#flytekitcoreinterfaceliteral) |  |
| [`OrderedDict`](.././flytekit.core.interface#flytekitcoreinterfaceordereddict) | Dictionary that remembers insertion order. |
| [`Scalar`](.././flytekit.core.interface#flytekitcoreinterfacescalar) |  |
| [`TypeEngine`](.././flytekit.core.interface#flytekitcoreinterfacetypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`TypeVar`](.././flytekit.core.interface#flytekitcoreinterfacetypevar) | Type variable. |
| [`UnionTransformer`](.././flytekit.core.interface#flytekitcoreinterfaceuniontransformer) | Transformer that handles a typing. |
| [`Void`](.././flytekit.core.interface#flytekitcoreinterfacevoid) |  |

### Errors

| Exception | Description |
|-|-|
| [`FlyteMissingReturnValueException`](.././flytekit.core.interface#flytekitcoreinterfaceflytemissingreturnvalueexception) | Common base class for all non-exit exceptions. |
| [`FlyteMissingTypeException`](.././flytekit.core.interface#flytekitcoreinterfaceflytemissingtypeexception) | Common base class for all non-exit exceptions. |
| [`FlyteValidationException`](.././flytekit.core.interface#flytekitcoreinterfaceflytevalidationexception) | Assertion failed. |

### Methods

| Method | Description |
|-|-|
| [`cast()`](#cast) | Cast a value to a type. |
| [`default_output_name()`](#default_output_name) |  |
| [`detect_artifact()`](#detect_artifact) | If the user wishes to control how Artifacts are created (i. |
| [`extract_return_annotation()`](#extract_return_annotation) | The purpose of this function is to sort out whether a function is returning one thing, or multiple things, and to. |
| [`get_args()`](#get_args) | Get type arguments with all substitutions performed. |
| [`get_type_hints()`](#get_type_hints) | Return type hints for an object. |
| [`has_return_statement()`](#has_return_statement) |  |
| [`output_name_generator()`](#output_name_generator) |  |
| [`remap_shared_output_descriptions()`](#remap_shared_output_descriptions) | Deals with mixed styles of return value descriptions used in docstrings. |
| [`repr_kv()`](#repr_kv) |  |
| [`repr_type_signature()`](#repr_type_signature) | Converts an inputs and outputs to a type signature. |
| [`transform_function_to_interface()`](#transform_function_to_interface) | From the annotations on a task function that the user should have provided, and the output names they want to use. |
| [`transform_inputs_to_parameters()`](#transform_inputs_to_parameters) | Transforms the given interface (with inputs) to a Parameter Map with defaults set. |
| [`transform_interface_to_list_interface()`](#transform_interface_to_list_interface) | Takes a single task interface and interpolates it to an array interface - to allow performing distributed python map. |
| [`transform_interface_to_typed_interface()`](#transform_interface_to_typed_interface) | Transform the given simple python native interface to FlyteIDL's interface. |
| [`transform_type()`](#transform_type) |  |
| [`transform_types_to_list_of_type()`](#transform_types_to_list_of_type) | Converts unbound inputs into the equivalent (optional) collections. |
| [`transform_variable_map()`](#transform_variable_map) | Given a map of str (names of inputs for instance) to their Python native types, return a map of the name to a. |
| [`verify_outputs_artifact_bindings()`](#verify_outputs_artifact_bindings) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `DYNAMIC_INPUT_BINDING` | `LabelValue` |  |
| `T` | `TypeVar` |  |
| `annotations` | `_Feature` |  |
| `developer_logger` | `Logger` |  |
| `logger` | `Logger` |  |

## Methods

#### cast()

```python
def cast(
    typ,
    val,
)
```
Cast a value to a type.

This returns the value unchanged.  To the type checker this
signals that the return value has the designated type, but at
runtime we intentionally don't check anything (we want this
to be as fast as possible).


| Parameter | Type |
|-|-|
| `typ` |  |
| `val` |  |

#### default_output_name()

```python
def default_output_name(
    index: int,
) -> str
```
| Parameter | Type |
|-|-|
| `index` | `int` |

#### detect_artifact()

```python
def detect_artifact(
    ts: typing.Tuple[typing.Any, ...],
) -> Optional[art_id.ArtifactID]
```
If the user wishes to control how Artifacts are created (i.e. naming them, etc.) this is where we pick it up and
store it in the interface.


| Parameter | Type |
|-|-|
| `ts` | `typing.Tuple[typing.Any, ...]` |

#### extract_return_annotation()

```python
def extract_return_annotation(
    return_annotation: Union[Type, Tuple, None],
) -> Dict[str, Type]
```
The purpose of this function is to sort out whether a function is returning one thing, or multiple things, and to
name the outputs accordingly, either by using our default name function, or from a typing.NamedTuple.

# Option 1
nt1 = typing.NamedTuple("NT1", x_str=str, y_int=int)
def t(a: int, b: str) -> nt1: ...

# Option 2
def t(a: int, b: str) -> typing.NamedTuple("NT1", x_str=str, y_int=int): ...

# Option 3
def t(a: int, b: str) -> typing.Tuple[int, str]: ...

# Option 4
def t(a: int, b: str) -> (int, str): ...

# Option 5
def t(a: int, b: str) -> str: ...

# Option 6
def t(a: int, b: str) -> None: ...

# Options 7/8
def t(a: int, b: str) -> List[int]: ...
def t(a: int, b: str) -> Dict[str, int]: ...

Note that Options 1 and 2 are identical, just syntactic sugar. In the NamedTuple case, we'll use the names in the
definition. In all other cases, we'll automatically generate output names, indexed starting at 0.


| Parameter | Type |
|-|-|
| `return_annotation` | `Union[Type, Tuple, None]` |

#### get_args()

```python
def get_args(
    tp,
)
```
Get type arguments with all substitutions performed.

For unions, basic simplifications used by Union constructor are performed.

Examples::

>>> T = TypeVar('T')
>>> assert get_args(Dict[str, int]) == (str, int)
>>> assert get_args(int) == ()
>>> assert get_args(Union[int, Union[T, int], str][int]) == (int, str)
>>> assert get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
>>> assert get_args(Callable[[], T][int]) == ([], int)


| Parameter | Type |
|-|-|
| `tp` |  |

#### get_type_hints()

```python
def get_type_hints(
    obj,
    globalns,
    localns,
    include_extras,
)
```
Return type hints for an object.

This is often the same as obj.__annotations__, but it handles
forward references encoded as string literals and recursively replaces all
'Annotated[T, ...]' with 'T' (unless 'include_extras=True').

The argument may be a module, class, method, or function. The annotations
are returned as a dictionary. For classes, annotations include also
inherited members.

TypeError is raised if the argument is not of a type that can contain
annotations, and an empty dictionary is returned if no annotations are
present.

BEWARE -- the behavior of globalns and localns is counterintuitive
(unless you are familiar with how eval() and exec() work).  The
search order is locals first, then globals.

- If no dict arguments are passed, an attempt is made to use the
globals from obj (or the respective module's globals for classes),
and these are also used as the locals.  If the object does not appear
to have globals, an empty dictionary is used.  For classes, the search
order is globals first then locals.

- If one dict argument is passed, it is used for both globals and
locals.

- If two dict arguments are passed, they specify globals and
locals, respectively.


| Parameter | Type |
|-|-|
| `obj` |  |
| `globalns` |  |
| `localns` |  |
| `include_extras` |  |

#### has_return_statement()

```python
def has_return_statement(
    func: typing.Callable,
) -> bool
```
| Parameter | Type |
|-|-|
| `func` | `typing.Callable` |

#### output_name_generator()

```python
def output_name_generator(
    length: int,
) -> Generator[str, None, None]
```
| Parameter | Type |
|-|-|
| `length` | `int` |

#### remap_shared_output_descriptions()

```python
def remap_shared_output_descriptions(
    output_descriptions: Dict[str, str],
    outputs: Dict[str, Type],
) -> Dict[str, str]
```
Deals with mixed styles of return value descriptions used in docstrings. If the docstring contains a single entry of return value description, that output description is shared by each output variable.


| Parameter | Type |
|-|-|
| `output_descriptions` | `Dict[str, str]` |
| `outputs` | `Dict[str, Type]` |

#### repr_kv()

```python
def repr_kv(
    k: str,
    v: Union[Type, Tuple[Type, Any]],
) -> str
```
| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `Union[Type, Tuple[Type, Any]]` |

#### repr_type_signature()

```python
def repr_type_signature(
    io: Union[Dict[str, Tuple[Type, Any]], Dict[str, Type]],
) -> str
```
Converts an inputs and outputs to a type signature


| Parameter | Type |
|-|-|
| `io` | `Union[Dict[str, Tuple[Type, Any]], Dict[str, Type]]` |

#### transform_function_to_interface()

```python
def transform_function_to_interface(
    fn: typing.Callable,
    docstring: Optional[Docstring],
    is_reference_entity: bool,
    pickle_untyped: bool,
) -> Interface
```
From the annotations on a task function that the user should have provided, and the output names they want to use
for each output parameter, construct the TypedInterface object

For now the fancy object, maybe in the future a dumb object.


| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `docstring` | `Optional[Docstring]` |
| `is_reference_entity` | `bool` |
| `pickle_untyped` | `bool` |

#### transform_inputs_to_parameters()

```python
def transform_inputs_to_parameters(
    ctx: context_manager.FlyteContext,
    interface: Interface,
) -> _interface_models.ParameterMap
```
Transforms the given interface (with inputs) to a Parameter Map with defaults set


| Parameter | Type |
|-|-|
| `ctx` | `context_manager.FlyteContext` |
| `interface` | `Interface` |

#### transform_interface_to_list_interface()

```python
def transform_interface_to_list_interface(
    interface: Interface,
    bound_inputs: typing.Set[str],
    excluded_inputs: typing.Set[str],
    optional_outputs: bool,
) -> Interface
```
Takes a single task interface and interpolates it to an array interface - to allow performing distributed python map
like functions


| Parameter | Type |
|-|-|
| `interface` | `Interface` |
| `bound_inputs` | `typing.Set[str]` |
| `excluded_inputs` | `typing.Set[str]` |
| `optional_outputs` | `bool` |

#### transform_interface_to_typed_interface()

```python
def transform_interface_to_typed_interface(
    interface: typing.Optional[Interface],
    allow_partial_artifact_id_binding: bool,
) -> typing.Optional[_interface_models.TypedInterface]
```
Transform the given simple python native interface to FlyteIDL's interface


| Parameter | Type |
|-|-|
| `interface` | `typing.Optional[Interface]` |
| `allow_partial_artifact_id_binding` | `bool` |

#### transform_type()

```python
def transform_type(
    x: type,
    description: Optional[str],
) -> _interface_models.Variable
```
| Parameter | Type |
|-|-|
| `x` | `type` |
| `description` | `Optional[str]` |

#### transform_types_to_list_of_type()

```python
def transform_types_to_list_of_type(
    m: Dict[str, type],
    bound_inputs: typing.Set[str],
    list_as_optional: bool,
) -> Dict[str, type]
```
Converts unbound inputs into the equivalent (optional) collections. This is useful for array jobs / map style code.
It will create a collection of types even if any one these types is not a collection type.


| Parameter | Type |
|-|-|
| `m` | `Dict[str, type]` |
| `bound_inputs` | `typing.Set[str]` |
| `list_as_optional` | `bool` |

#### transform_variable_map()

```python
def transform_variable_map(
    variable_map: Dict[str, type],
    descriptions: Optional[Dict[str, str]],
) -> Dict[str, _interface_models.Variable]
```
Given a map of str (names of inputs for instance) to their Python native types, return a map of the name to a
Flyte Variable object with that type.


| Parameter | Type |
|-|-|
| `variable_map` | `Dict[str, type]` |
| `descriptions` | `Optional[Dict[str, str]]` |

#### verify_outputs_artifact_bindings()

```python
def verify_outputs_artifact_bindings(
    inputs: Dict[str, type],
    outputs: Dict[str, _interface_models.Variable],
    allow_partial_artifact_id_binding: bool,
)
```
| Parameter | Type |
|-|-|
| `inputs` | `Dict[str, type]` |
| `outputs` | `Dict[str, _interface_models.Variable]` |
| `allow_partial_artifact_id_binding` | `bool` |

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
class Artifact(
    project: Optional[str],
    domain: Optional[str],
    name: Optional[str],
    version: Optional[str],
    time_partitioned: bool,
    time_partition: Optional[TimePartition],
    time_partition_granularity: Optional[Granularity],
    partition_keys: Optional[typing.List[str]],
    partitions: Optional[Union[Partitions, typing.Dict[str, str]]],
)
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
| [`create_from()`](#create_from) | This function allows users to declare partition values dynamically from the body of a task. |
| [`embed_as_query()`](#embed_as_query) | This should only be called in the context of a Trigger. |
| [`query()`](#query) |  |
| [`to_id_idl()`](#to_id_idl) | Converts this object to the IDL representation. |


#### create_from()

```python
def create_from(
    o: O,
    card: Optional[SerializableToString],
    args: `*args`,
    kwargs,
) -> O
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
) -> art_id.ArtifactQuery
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
) -> ArtifactQuery
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
| `concrete_artifact_id` |  |  |
| `partitions` |  |  |
| `time_partition` |  |  |

## flytekit.core.interface.ArtifactIDSpecification

This is a special object that helps specify how Artifacts are to be created. See the comment in the
call function of the main Artifact class. Also see the handling code in transform_variable_map for more
information. There's a limited set of information that we ultimately need in a TypedInterface, so it
doesn't make sense to carry the full Artifact object around. This object should be sufficient, despite
having a pointer to the main artifact.


```python
class ArtifactIDSpecification(
    a: Artifact,
)
```
| Parameter | Type |
|-|-|
| `a` | `Artifact` |

### Methods

| Method | Description |
|-|-|
| [`bind_partitions()`](#bind_partitions) |  |
| [`to_partial_artifact_id()`](#to_partial_artifact_id) |  |


#### bind_partitions()

```python
def bind_partitions(
    args,
    kwargs,
) -> ArtifactIDSpecification
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
class ArtifactQuery(
    artifact: Artifact,
    name: str,
    project: Optional[str],
    domain: Optional[str],
    time_partition: Optional[TimePartition],
    partitions: Optional[Partitions],
    tag: Optional[str],
)
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
| [`get_partition_str()`](#get_partition_str) |  |
| [`get_str()`](#get_str) |  |
| [`get_time_partition_str()`](#get_time_partition_str) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### get_partition_str()

```python
def get_partition_str(
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_str()

```python
def get_str(
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_time_partition_str()

```python
def get_time_partition_str(
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### to_flyte_idl()

```python
def to_flyte_idl(
    kwargs,
) -> art_id.ArtifactQuery
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `bound` |  |  |

## flytekit.core.interface.Docstring

```python
class Docstring(
    docstring: typing.Optional[str],
    callable_: typing.Optional[typing.Callable],
)
```
| Parameter | Type |
|-|-|
| `docstring` | `typing.Optional[str]` |
| `callable_` | `typing.Optional[typing.Callable]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `input_descriptions` |  |  |
| `long_description` |  |  |
| `output_descriptions` |  |  |
| `short_description` |  |  |

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
| [`add_signal_handler()`](#add_signal_handler) |  |
| [`current_context()`](#current_context) |  |
| [`get_origin_stackframe()`](#get_origin_stackframe) |  |
| [`initialize()`](#initialize) | Re-initializes the context and erases the entire context. |
| [`pop_context()`](#pop_context) |  |
| [`push_context()`](#push_context) |  |
| [`size()`](#size) |  |
| [`with_context()`](#with_context) |  |


#### add_signal_handler()

```python
def add_signal_handler(
    handler: typing.Callable[[int, FrameType], typing.Any],
)
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
) -> traceback.FrameSummary
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
) -> FlyteContext
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
) -> Generator[FlyteContext, None, None]
```
| Parameter | Type |
|-|-|
| `b` | `FlyteContext.Builder` |

## flytekit.core.interface.FlyteMissingReturnValueException

Common base class for all non-exit exceptions.


```python
class FlyteMissingReturnValueException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.core.interface.FlyteMissingTypeException

Common base class for all non-exit exceptions.


```python
class FlyteMissingTypeException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.core.interface.FlyteValidationException

Assertion failed.


```python
class FlyteValidationException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.core.interface.Interface

A Python native interface object, like inspect.signature but simpler.


```python
class Interface(
    inputs: Union[Optional[Dict[str, Type]], Optional[Dict[str, Tuple[Type, Any]]]],
    outputs: Union[Optional[Dict[str, Type]], Optional[Dict[str, Optional[Type]]]],
    output_tuple_name: Optional[str],
    docstring: Optional[Docstring],
)
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
| [`remove_inputs()`](#remove_inputs) | This method is useful in removing some variables from the Flyte backend inputs specification, as these are. |
| [`with_inputs()`](#with_inputs) | Use this to add additional inputs to the interface. |
| [`with_outputs()`](#with_outputs) | This method allows addition of extra outputs are expected from a task specification. |


#### remove_inputs()

```python
def remove_inputs(
    vars: Optional[List[str]],
) -> Interface
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
) -> Interface
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
) -> Interface
```
This method allows addition of extra outputs are expected from a task specification


| Parameter | Type |
|-|-|
| `extra_outputs` | `Dict[str, Type]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `default_inputs_as_kwargs` |  |  |
| `docstring` |  |  |
| `inputs` |  |  |
| `inputs_with_defaults` |  |  |
| `output_names` |  |  |
| `output_tuple` |  |  |
| `output_tuple_name` |  |  |
| `outputs` |  |  |

## flytekit.core.interface.Literal

```python
class Literal(
    scalar: typing.Optional[flytekit.models.literals.Scalar],
    collection: typing.Optional[flytekit.models.literals.LiteralCollection],
    map: typing.Optional[flytekit.models.literals.LiteralMap],
    hash: typing.Optional[str],
    metadata: typing.Optional[typing.Dict[str, str]],
    offloaded_metadata: typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata],
)
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`set_metadata()`](#set_metadata) | Note: This is a mutation on the literal. |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.Literal,
) -> Literal
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
)
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
| `collection` |  | {{< multiline >}}If not None, this value holds a collection of Literal values which can be further unpacked.
{{< /multiline >}} |
| `hash` |  | {{< multiline >}}If not None, this value holds a hash that represents the literal for caching purposes.
{{< /multiline >}} |
| `is_empty` |  |  |
| `map` |  | {{< multiline >}}If not None, this value holds a map of Literal values which can be further unpacked.
{{< /multiline >}} |
| `metadata` |  | {{< multiline >}}This value holds metadata about the literal.
{{< /multiline >}} |
| `offloaded_metadata` |  | {{< multiline >}}This value holds metadata about the offloaded literal.
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}If not None, this value holds a scalar value which can be further unpacked.
{{< /multiline >}} |
| `value` |  | {{< multiline >}}Returns one of the scalar, collection, or map properties based on which one is set.
{{< /multiline >}} |

## flytekit.core.interface.OrderedDict

Dictionary that remembers insertion order


## flytekit.core.interface.Scalar

```python
class Scalar(
    primitive: typing.Optional[flytekit.models.literals.Primitive],
    blob: typing.Optional[flytekit.models.literals.Blob],
    binary: typing.Optional[flytekit.models.literals.Binary],
    schema: typing.Optional[flytekit.models.literals.Schema],
    union: typing.Optional[flytekit.models.literals.Union],
    none_type: typing.Optional[flytekit.models.literals.Void],
    error: typing.Optional[flytekit.models.types.Error],
    generic: typing.Optional[google.protobuf.struct_pb2.Struct],
    structured_dataset: typing.Optional[flytekit.models.literals.StructuredDataset],
)
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> flytekit.models.literals.Scalar
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
| `binary` |  |  |
| `blob` |  |  |
| `error` |  |  |
| `generic` |  |  |
| `is_empty` |  |  |
| `none_type` |  |  |
| `primitive` |  |  |
| `schema` |  |  |
| `structured_dataset` |  |  |
| `union` |  |  |
| `value` |  | {{< multiline >}}Returns whichever value is set
{{< /multiline >}} |

## flytekit.core.interface.TypeEngine

Core Extensible TypeEngine of Flytekit. This should be used to extend the capabilities of FlyteKits type system.
Users can implement their own TypeTransformers and register them with the TypeEngine. This will allow special handling
of user objects


### Methods

| Method | Description |
|-|-|
| [`async_to_literal()`](#async_to_literal) | Converts a python value of a given type and expected ``LiteralType`` into a resolved ``Literal`` value. |
| [`async_to_python_value()`](#async_to_python_value) |  |
| [`calculate_hash()`](#calculate_hash) |  |
| [`dict_to_literal_map()`](#dict_to_literal_map) |  |
| [`dict_to_literal_map_pb()`](#dict_to_literal_map_pb) |  |
| [`get_available_transformers()`](#get_available_transformers) | Returns all python types for which transformers are available. |
| [`get_transformer()`](#get_transformer) | Implements a recursive search for the transformer. |
| [`guess_python_type()`](#guess_python_type) | Transforms a flyte-specific ``LiteralType`` to a regular python value. |
| [`guess_python_types()`](#guess_python_types) | Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values. |
| [`lazy_import_transformers()`](#lazy_import_transformers) | Only load the transformers if needed. |
| [`literal_map_to_kwargs()`](#literal_map_to_kwargs) |  |
| [`named_tuple_to_variable_map()`](#named_tuple_to_variable_map) | Converts a python-native ``NamedTuple`` to a flyte-specific VariableMap of named literals. |
| [`register()`](#register) | This should be used for all types that respond with the right type annotation when you use type(. |
| [`register_additional_type()`](#register_additional_type) |  |
| [`register_restricted_type()`](#register_restricted_type) |  |
| [`to_html()`](#to_html) |  |
| [`to_literal()`](#to_literal) | The current dance is because we are allowing users to call from an async function, this synchronous. |
| [`to_literal_checks()`](#to_literal_checks) |  |
| [`to_literal_type()`](#to_literal_type) | Converts a python type into a flyte specific ``LiteralType``. |
| [`to_python_value()`](#to_python_value) | Converts a Literal value with an expected python type into a python value. |
| [`unwrap_offloaded_literal()`](#unwrap_offloaded_literal) |  |


#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
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
) -> typing.Any
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
) -> Optional[str]
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
) -> LiteralMap
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
) -> Optional[literals_pb2.LiteralMap]
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
) -> TypeTransformer[T]
```
Implements a recursive search for the transformer.


| Parameter | Type |
|-|-|
| `python_type` | `Type` |

#### guess_python_type()

```python
def guess_python_type(
    flyte_type: LiteralType,
) -> Type[T]
```
Transforms a flyte-specific ``LiteralType`` to a regular python value.


| Parameter | Type |
|-|-|
| `flyte_type` | `LiteralType` |

#### guess_python_types()

```python
def guess_python_types(
    flyte_variable_dict: typing.Dict[str, _interface_models.Variable],
) -> typing.Dict[str, type]
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
) -> typing.Dict[str, typing.Any]
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
) -> _interface_models.VariableMap
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
)
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
)
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
)
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
) -> str
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
) -> Literal
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
)
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
) -> LiteralType
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
) -> typing.Any
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
) -> Literal
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

Type variables can also have defaults:

class IntDefault[T = int]:
...

However, if desired, reusable type variables can also be constructed
manually, like so::

T = TypeVar('T')  # Can be anything
S = TypeVar('S', bound=str)  # Can be any subtype of str
A = TypeVar('A', str, bytes)  # Must be exactly str or bytes
D = TypeVar('D', default=int)  # Defaults to int

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
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`get_sub_type_in_optional()`](#get_sub_type_in_optional) | Return the generic Type T of the Optional type. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`is_optional_type()`](#is_optional_type) |  |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[T],
    v: T,
)
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
) -> typing.Union[Literal, asyncio.Future]
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
) -> Optional[typing.Any]
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
) -> Optional[T]
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
) -> Optional[T]
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
) -> Optional[LiteralType]
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### get_sub_type_in_optional()

```python
def get_sub_type_in_optional(
    t: Type[T],
) -> Type[T]
```
Return the generic Type T of the Optional type


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> type
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### is_optional_type()

```python
def is_optional_type(
    t: Type,
) -> bool
```
| Parameter | Type |
|-|-|
| `t` | `Type` |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
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
) -> str
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
) -> Literal
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
) -> Optional[T]
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
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.core.interface.Void

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> Void
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
| `is_empty` |  |  |

