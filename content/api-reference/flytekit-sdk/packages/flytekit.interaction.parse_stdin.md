---
title: flytekit.interaction.parse_stdin
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.interaction.parse_stdin

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteContext`](.././flytekit.interaction.parse_stdin#flytekitinteractionparse_stdinflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`Literal`](.././flytekit.interaction.parse_stdin#flytekitinteractionparse_stdinliteral) | None. |
| [`LiteralType`](.././flytekit.interaction.parse_stdin#flytekitinteractionparse_stdinliteraltype) | None. |
| [`TypeEngine`](.././flytekit.interaction.parse_stdin#flytekitinteractionparse_stdintypeengine) | Core Extensible TypeEngine of Flytekit. |

## flytekit.interaction.parse_stdin.FlyteContext

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

## flytekit.interaction.parse_stdin.Literal

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

## flytekit.interaction.parse_stdin.LiteralType

```python
def LiteralType(
    simple,
    schema,
    collection_type,
    map_value_type,
    blob,
    enum_type,
    union_type,
    structured_dataset_type,
    metadata,
    structure,
    annotation,
):
```
This is a oneof message, only one of the kwargs may be set, representing one of the Flyte types.



| Parameter | Type |
|-|-|
| `simple` |  |
| `schema` |  |
| `collection_type` |  |
| `map_value_type` |  |
| `blob` |  |
| `enum_type` |  |
| `union_type` |  |
| `structured_dataset_type` |  |
| `metadata` |  |
| `structure` |  |
| `annotation` |  |

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
| annotation |  |  |
| blob |  |  |
| collection_type |  |  |
| enum_type |  |  |
| is_empty |  |  |
| map_value_type |  |  |
| metadata |  |  |
| schema |  |  |
| simple |  |  |
| structure |  |  |
| structured_dataset_type |  |  |
| union_type |  |  |

## flytekit.interaction.parse_stdin.TypeEngine

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

