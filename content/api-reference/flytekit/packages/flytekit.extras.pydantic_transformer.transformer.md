---
title: flytekit.extras.pydantic_transformer.transformer
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.extras.pydantic_transformer.transformer

## Directory

### Classes

| Class | Description |
|-|-|
| [`BaseModel`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerbasemodel) | Usage docs: https://docs. |
| [`Binary`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerbinary) |  |
| [`FlyteContext`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`Literal`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerliteral) |  |
| [`LiteralType`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerliteraltype) |  |
| [`PydanticTransformer`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerpydantictransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`Scalar`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerscalar) |  |
| [`TypeAnnotationModel`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformertypeannotationmodel) | Python class representation of the flyteidl TypeAnnotation message. |
| [`TypeEngine`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformertypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`TypeStructure`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformertypestructure) | Models _types_pb2. |
| [`TypeTransformer`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformertypetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |

### Errors

| Exception | Description |
|-|-|
| [`TypeTransformerFailedError`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformertypetransformerfailederror) | Inappropriate argument type. |

### Methods

| Method | Description |
|-|-|
| [`str2bool()`](#str2bool) | Convert a string to a boolean. |


### Variables

| Property | Type | Description |
|-|-|-|
| `CACHE_KEY_METADATA` | `str` |  |
| `FLYTE_USE_OLD_DC_FORMAT` | `str` |  |
| `MESSAGEPACK` | `str` |  |
| `SERIALIZATION_FORMAT` | `str` |  |
| `logger` | `Logger` |  |

## Methods

#### str2bool()

```python
def str2bool(
    value: typing.Optional[str],
) -> bool
```
Convert a string to a boolean. This is useful for parsing environment variables.


| Parameter | Type |
|-|-|
| `value` | `typing.Optional[str]` |

## flytekit.extras.pydantic_transformer.transformer.BaseModel

Usage docs: https://docs.pydantic.dev/2.10/concepts/models/

A base class for creating Pydantic models.

Attributes:
__class_vars__: The names of the class variables defined on the model.
__private_attributes__: Metadata about the private attributes of the model.
__signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

__pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
__pydantic_core_schema__: The core schema of the model.
__pydantic_custom_init__: Whether the model has a custom `__init__` function.
__pydantic_decorators__: Metadata containing the decorators defined on the model.
This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
__pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
__args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
__pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
__pydantic_post_init__: The name of the post-init method for the model, if defined.
__pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
__pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
__pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

__pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
__pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

__pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
is set to `'allow'`.
__pydantic_fields_set__: The names of fields explicitly set during instantiation.
__pydantic_private__: Values of private attributes set on the model instance.


```python
class BaseModel(
    data: Any,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type |
|-|-|
| `data` | `Any` |

### Methods

| Method | Description |
|-|-|
| [`construct()`](#construct) |  |
| [`copy()`](#copy) | Returns a copy of the model. |
| [`dict()`](#dict) |  |
| [`from_orm()`](#from_orm) |  |
| [`json()`](#json) |  |
| [`model_construct()`](#model_construct) | Creates a new instance of the `Model` class with validated data. |
| [`model_copy()`](#model_copy) | Usage docs: https://docs. |
| [`model_dump()`](#model_dump) | Usage docs: https://docs. |
| [`model_dump_json()`](#model_dump_json) | Usage docs: https://docs. |
| [`model_json_schema()`](#model_json_schema) | Generates a JSON schema for a model class. |
| [`model_parametrized_name()`](#model_parametrized_name) | Compute the class name for parametrizations of generic classes. |
| [`model_post_init()`](#model_post_init) | Override this method to perform additional initialization after `__init__` and `model_construct`. |
| [`model_rebuild()`](#model_rebuild) | Try to rebuild the pydantic-core schema for the model. |
| [`model_validate()`](#model_validate) | Validate a pydantic model instance. |
| [`model_validate_json()`](#model_validate_json) | Usage docs: https://docs. |
| [`model_validate_strings()`](#model_validate_strings) | Validate the given object with string data against the Pydantic model. |
| [`parse_file()`](#parse_file) |  |
| [`parse_obj()`](#parse_obj) |  |
| [`parse_raw()`](#parse_raw) |  |
| [`schema()`](#schema) |  |
| [`schema_json()`](#schema_json) |  |
| [`update_forward_refs()`](#update_forward_refs) |  |
| [`validate()`](#validate) |  |


#### construct()

```python
def construct(
    _fields_set: set[str] | None,
    values: Any,
) -> Self
```
| Parameter | Type |
|-|-|
| `_fields_set` | `set[str] \| None` |
| `values` | `Any` |

#### copy()

```python
def copy(
    include: AbstractSetIntStr | MappingIntStrAny | None,
    exclude: AbstractSetIntStr | MappingIntStrAny | None,
    update: Dict[str, Any] | None,
    deep: bool,
) -> Self
```
Returns a copy of the model.

!!! warning "Deprecated"
This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```python {test="skip" lint="skip"}
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```



| Parameter | Type |
|-|-|
| `include` | `AbstractSetIntStr \| MappingIntStrAny \| None` |
| `exclude` | `AbstractSetIntStr \| MappingIntStrAny \| None` |
| `update` | `Dict[str, Any] \| None` |
| `deep` | `bool` |

#### dict()

```python
def dict(
    include: IncEx | None,
    exclude: IncEx | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
) -> Dict[str, Any]
```
| Parameter | Type |
|-|-|
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `by_alias` | `bool` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |

#### from_orm()

```python
def from_orm(
    obj: Any,
) -> Self
```
| Parameter | Type |
|-|-|
| `obj` | `Any` |

#### json()

```python
def json(
    include: IncEx | None,
    exclude: IncEx | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    encoder: Callable[[Any], Any] | None,
    models_as_dict: bool,
    dumps_kwargs: Any,
) -> str
```
| Parameter | Type |
|-|-|
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `by_alias` | `bool` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `encoder` | `Callable[[Any], Any] \| None` |
| `models_as_dict` | `bool` |
| `dumps_kwargs` | `Any` |

#### model_construct()

```python
def model_construct(
    _fields_set: set[str] | None,
    values: Any,
) -> Self
```
Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note
`model_construct()` generally respects the `model_config.extra` setting on the provided model.
That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
an error if extra values are passed, but they will be ignored.



| Parameter | Type |
|-|-|
| `_fields_set` | `set[str] \| None` |
| `values` | `Any` |

#### model_copy()

```python
def model_copy(
    update: Mapping[str, Any] | None,
    deep: bool,
) -> Self
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#model_copy

Returns a copy of the model.



| Parameter | Type |
|-|-|
| `update` | `Mapping[str, Any] \| None` |
| `deep` | `bool` |

#### model_dump()

```python
def model_dump(
    mode: Literal['json', 'python'] | str,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    serialize_as_any: bool,
) -> dict[str, Any]
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.



| Parameter | Type |
|-|-|
| `mode` | `Literal['json', 'python'] \| str` |
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `round_trip` | `bool` |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` |
| `serialize_as_any` | `bool` |

#### model_dump_json()

```python
def model_dump_json(
    indent: int | None,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    serialize_as_any: bool,
) -> str
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.



| Parameter | Type |
|-|-|
| `indent` | `int \| None` |
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `round_trip` | `bool` |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` |
| `serialize_as_any` | `bool` |

#### model_json_schema()

```python
def model_json_schema(
    by_alias: bool,
    ref_template: str,
    schema_generator: type[GenerateJsonSchema],
    mode: JsonSchemaMode,
) -> dict[str, Any]
```
Generates a JSON schema for a model class.



| Parameter | Type |
|-|-|
| `by_alias` | `bool` |
| `ref_template` | `str` |
| `schema_generator` | `type[GenerateJsonSchema]` |
| `mode` | `JsonSchemaMode` |

#### model_parametrized_name()

```python
def model_parametrized_name(
    params: tuple[type[Any], ...],
) -> str
```
Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.



| Parameter | Type |
|-|-|
| `params` | `tuple[type[Any], ...]` |

#### model_post_init()

```python
def model_post_init(
    _BaseModel__context: Any,
)
```
Override this method to perform additional initialization after `__init__` and `model_construct`.
This is useful if you want to do some validation that requires the entire model to be initialized.


| Parameter | Type |
|-|-|
| `_BaseModel__context` | `Any` |

#### model_rebuild()

```python
def model_rebuild(
    force: bool,
    raise_errors: bool,
    _parent_namespace_depth: int,
    _types_namespace: MappingNamespace | None,
) -> bool | None
```
Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.



| Parameter | Type |
|-|-|
| `force` | `bool` |
| `raise_errors` | `bool` |
| `_parent_namespace_depth` | `int` |
| `_types_namespace` | `MappingNamespace \| None` |

#### model_validate()

```python
def model_validate(
    obj: Any,
    strict: bool | None,
    from_attributes: bool | None,
    context: Any | None,
) -> Self
```
Validate a pydantic model instance.



| Parameter | Type |
|-|-|
| `obj` | `Any` |
| `strict` | `bool \| None` |
| `from_attributes` | `bool \| None` |
| `context` | `Any \| None` |

#### model_validate_json()

```python
def model_validate_json(
    json_data: str | bytes | bytearray,
    strict: bool | None,
    context: Any | None,
) -> Self
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.



| Parameter | Type |
|-|-|
| `json_data` | `str \| bytes \| bytearray` |
| `strict` | `bool \| None` |
| `context` | `Any \| None` |

#### model_validate_strings()

```python
def model_validate_strings(
    obj: Any,
    strict: bool | None,
    context: Any | None,
) -> Self
```
Validate the given object with string data against the Pydantic model.



| Parameter | Type |
|-|-|
| `obj` | `Any` |
| `strict` | `bool \| None` |
| `context` | `Any \| None` |

#### parse_file()

```python
def parse_file(
    path: str | Path,
    content_type: str | None,
    encoding: str,
    proto: DeprecatedParseProtocol | None,
    allow_pickle: bool,
) -> Self
```
| Parameter | Type |
|-|-|
| `path` | `str \| Path` |
| `content_type` | `str \| None` |
| `encoding` | `str` |
| `proto` | `DeprecatedParseProtocol \| None` |
| `allow_pickle` | `bool` |

#### parse_obj()

```python
def parse_obj(
    obj: Any,
) -> Self
```
| Parameter | Type |
|-|-|
| `obj` | `Any` |

#### parse_raw()

```python
def parse_raw(
    b: str | bytes,
    content_type: str | None,
    encoding: str,
    proto: DeprecatedParseProtocol | None,
    allow_pickle: bool,
) -> Self
```
| Parameter | Type |
|-|-|
| `b` | `str \| bytes` |
| `content_type` | `str \| None` |
| `encoding` | `str` |
| `proto` | `DeprecatedParseProtocol \| None` |
| `allow_pickle` | `bool` |

#### schema()

```python
def schema(
    by_alias: bool,
    ref_template: str,
) -> Dict[str, Any]
```
| Parameter | Type |
|-|-|
| `by_alias` | `bool` |
| `ref_template` | `str` |

#### schema_json()

```python
def schema_json(
    by_alias: bool,
    ref_template: str,
    dumps_kwargs: Any,
) -> str
```
| Parameter | Type |
|-|-|
| `by_alias` | `bool` |
| `ref_template` | `str` |
| `dumps_kwargs` | `Any` |

#### update_forward_refs()

```python
def update_forward_refs(
    localns: Any,
)
```
| Parameter | Type |
|-|-|
| `localns` | `Any` |

#### validate()

```python
def validate(
    value: Any,
) -> Self
```
| Parameter | Type |
|-|-|
| `value` | `Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `model_extra` |  | {{< multiline >}}Get extra fields set during validation.

Returns:
A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`.
{{< /multiline >}} |
| `model_fields_set` |  | {{< multiline >}}Returns the set of fields that have been explicitly set on this model instance.

Returns:
A set of strings representing the fields that have been set,
i.e. that were not filled from defaults.
{{< /multiline >}} |

## flytekit.extras.pydantic_transformer.transformer.Binary

```python
class Binary(
    value,
    tag,
)
```
| Parameter | Type |
|-|-|
| `value` |  |
| `tag` |  |

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
) -> Binary
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
| `is_empty` |  |  |
| `tag` |  |  |
| `value` |  |  |

## flytekit.extras.pydantic_transformer.transformer.FlyteContext

This is an internal-facing context object, that most users will not have to deal with. It's essentially a globally
available grab bag of settings and objects that allows flytekit to do things like convert complex types, run and
compile workflows, serialize Flyte entities, etc.

Even though this object as a ``current_context`` function on it, it should not be called directly. Please use the
:py:class:`flytekit.FlyteContextManager` object instead.

Please do not confuse this object with the :py:class:`flytekit.ExecutionParameters` object.


```python
class FlyteContext(
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
)
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
| [`current_context()`](#current_context) | This method exists only to maintain backwards compatibility. |
| [`enter_conditional_section()`](#enter_conditional_section) |  |
| [`get_deck()`](#get_deck) | Returns the deck that was created as part of the last execution. |
| [`get_origin_stackframe_repr()`](#get_origin_stackframe_repr) |  |
| [`new_builder()`](#new_builder) |  |
| [`new_compilation_state()`](#new_compilation_state) | Creates and returns a default compilation state. |
| [`new_execution_state()`](#new_execution_state) | Creates and returns a new default execution state. |
| [`set_stackframe()`](#set_stackframe) |  |
| [`with_client()`](#with_client) |  |
| [`with_compilation_state()`](#with_compilation_state) |  |
| [`with_execution_state()`](#with_execution_state) |  |
| [`with_file_access()`](#with_file_access) |  |
| [`with_new_compilation_state()`](#with_new_compilation_state) |  |
| [`with_output_metadata_tracker()`](#with_output_metadata_tracker) |  |
| [`with_serialization_settings()`](#with_serialization_settings) |  |
| [`with_worker_queue()`](#with_worker_queue) |  |


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
) -> CompilationState
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
) -> ExecutionState
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
)
```
| Parameter | Type |
|-|-|
| `s` | `traceback.FrameSummary` |

#### with_client()

```python
def with_client(
    c: SynchronousFlyteClient,
) -> Builder
```
| Parameter | Type |
|-|-|
| `c` | `SynchronousFlyteClient` |

#### with_compilation_state()

```python
def with_compilation_state(
    c: CompilationState,
) -> Builder
```
| Parameter | Type |
|-|-|
| `c` | `CompilationState` |

#### with_execution_state()

```python
def with_execution_state(
    es: ExecutionState,
) -> Builder
```
| Parameter | Type |
|-|-|
| `es` | `ExecutionState` |

#### with_file_access()

```python
def with_file_access(
    fa: FileAccessProvider,
) -> Builder
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
) -> Builder
```
| Parameter | Type |
|-|-|
| `t` | `OutputMetadataTracker` |

#### with_serialization_settings()

```python
def with_serialization_settings(
    ss: SerializationSettings,
) -> Builder
```
| Parameter | Type |
|-|-|
| `ss` | `SerializationSettings` |

#### with_worker_queue()

```python
def with_worker_queue(
    wq: Controller,
) -> Builder
```
| Parameter | Type |
|-|-|
| `wq` | `Controller` |

### Properties

| Property | Type | Description |
|-|-|-|
| `user_space_params` |  |  |

## flytekit.extras.pydantic_transformer.transformer.Literal

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

## flytekit.extras.pydantic_transformer.transformer.LiteralType

```python
class LiteralType(
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
)
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> LiteralType
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
| `annotation` |  |  |
| `blob` |  |  |
| `collection_type` |  | {{< multiline >}}The collection value type
{{< /multiline >}} |
| `enum_type` |  |  |
| `is_empty` |  |  |
| `map_value_type` |  | {{< multiline >}}The Value for a dictionary. Key is always string
{{< /multiline >}} |
| `metadata` |  |  |
| `schema` |  |  |
| `simple` |  |  |
| `structure` |  |  |
| `structured_dataset_type` |  |  |
| `union_type` |  |  |

## flytekit.extras.pydantic_transformer.transformer.PydanticTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
def PydanticTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_generic_literal()`](#to_generic_literal) | Note: This is deprecated and will be removed in the future. |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | For pydantic basemodel, we have to go through json first. |
| [`to_python_value()`](#to_python_value) | There will have 2 kinds of literal values:. |


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

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: flytekit.models.literals.Binary,
    expected_python_type: typing.Type[pydantic.main.BaseModel],
) -> pydantic.main.BaseModel
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
| `binary_idl_object` | `flytekit.models.literals.Binary` |
| `expected_python_type` | `typing.Type[pydantic.main.BaseModel]` |

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
    t: typing.Type[pydantic.main.BaseModel],
) -> flytekit.models.types.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.Type[pydantic.main.BaseModel]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[T]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

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

#### to_generic_literal()

```python
def to_generic_literal(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: pydantic.main.BaseModel,
    python_type: typing.Type[pydantic.main.BaseModel],
    expected: flytekit.models.types.LiteralType,
) -> flytekit.models.literals.Literal
```
Note: This is deprecated and will be removed in the future.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `python_val` | `pydantic.main.BaseModel` |
| `python_type` | `typing.Type[pydantic.main.BaseModel]` |
| `expected` | `flytekit.models.types.LiteralType` |

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
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: pydantic.main.BaseModel,
    python_type: typing.Type[pydantic.main.BaseModel],
    expected: flytekit.models.types.LiteralType,
) -> flytekit.models.literals.Literal
```
For pydantic basemodel, we have to go through json first.
This is for handling enum in basemodel.
More details: https://github.com/flyteorg/flytekit/pull/2792


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `python_val` | `pydantic.main.BaseModel` |
| `python_type` | `typing.Type[pydantic.main.BaseModel]` |
| `expected` | `flytekit.models.types.LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[pydantic.main.BaseModel],
) -> pydantic.main.BaseModel
```
There will have 2 kinds of literal values:
1. protobuf Struct (From Flyte Console)
2. binary scalar (Others)
Hence we have to handle 2 kinds of cases.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `lv` | `flytekit.models.literals.Literal` |
| `expected_python_type` | `typing.Type[pydantic.main.BaseModel]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.extras.pydantic_transformer.transformer.Scalar

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

## flytekit.extras.pydantic_transformer.transformer.TypeAnnotationModel

Python class representation of the flyteidl TypeAnnotation message.


```python
class TypeAnnotationModel(
    annotations: typing.Dict[str, typing.Any],
)
```
| Parameter | Type |
|-|-|
| `annotations` | `typing.Dict[str, typing.Any]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`merge_annotations()`](#merge_annotations) | Merges two annotations together. |
| [`to_flyte_idl()`](#to_flyte_idl) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> TypeAnnotation
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### merge_annotations()

```python
def merge_annotations(
    annotation: TypeAnnotation,
    other_annotation: TypeAnnotation,
) -> TypeAnnotation
```
Merges two annotations together. If the same key exists in both annotations, the value in the other annotation
will be used.


| Parameter | Type |
|-|-|
| `annotation` | `TypeAnnotation` |
| `other_annotation` | `TypeAnnotation` |

#### to_flyte_idl()

```python
def to_flyte_idl()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  |  |

## flytekit.extras.pydantic_transformer.transformer.TypeEngine

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

## flytekit.extras.pydantic_transformer.transformer.TypeStructure

Models _types_pb2.TypeStructure


```python
class TypeStructure(
    tag: str,
    dataclass_type: typing.Dict[str, ForwardRef('LiteralType')],
)
```
| Parameter | Type |
|-|-|
| `tag` | `str` |
| `dataclass_type` | `typing.Dict[str, ForwardRef('LiteralType')]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.types_pb2.TypeStructure,
)
```
| Parameter | Type |
|-|-|
| `proto` | `flyteidl.core.types_pb2.TypeStructure` |

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
| `dataclass_type` |  |  |
| `is_empty` |  |  |
| `tag` |  |  |

## flytekit.extras.pydantic_transformer.transformer.TypeTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
class TypeTransformer(
    name: str,
    t: Type[T],
    enable_type_assertions: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `t` | `Type[T]` |
| `enable_type_assertions` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
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
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[T]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

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
    python_val: T,
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
| `python_val` | `T` |
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

## flytekit.extras.pydantic_transformer.transformer.TypeTransformerFailedError

Inappropriate argument type.


