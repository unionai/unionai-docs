---
title: RunOutput
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RunOutput

**Package:** `flyte.app`

Use a run's output for app parameters.

This enables the declaration of an app parameter dependency on the output of
a run, given by a specific run name, or a task name and version. If
`task_auto_version == 'latest'`, the latest version of the task will be used.
If `task_auto_version == 'current'`, the version will be derived from the callee
app or task context. To get the latest task run for ephemeral task runs, set
`task_version` and `task_auto_version` should both be set to `None` (which is the default).

Examples:

Get the output of a specific run:

```python
run_output = RunOutput(type="directory", run_name="my-run-123")
```

Get the latest output of an ephemeral task run:

```python
run_output = RunOutput(type="file", task_name="env.my_task")
```

Get the latest output of a deployed task run:

```python
run_output = RunOutput(type="file", task_name="env.my_task", task_auto_version="latest")
```

Get the output of a specific task run:

```python
run_output = RunOutput(type="file", task_name="env.my_task", task_version="xyz")
```


```python
class RunOutput(
    data: Any,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `data` | `Any` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `model_extra` | `None` | Get extra fields set during validation.  Returns:     A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. |
| `model_fields_set` | `None` | Returns the set of fields that have been explicitly set on this model instance.  Returns:     A set of strings representing the fields that have been set,         i.e. that were not filled from defaults. |

## Methods

| Method | Description |
|-|-|
| [`check_type()`](#check_type) |  |
| [`construct()`](#construct) |  |
| [`copy()`](#copy) | Returns a copy of the model. |
| [`dict()`](#dict) |  |
| [`from_orm()`](#from_orm) |  |
| [`get()`](#get) |  |
| [`json()`](#json) |  |
| [`materialize()`](#materialize) |  |
| [`model_construct()`](#model_construct) | Creates a new instance of the `Model` class with validated data. |
| [`model_copy()`](#model_copy) | Returns a copy of the model. |
| [`model_dump()`](#model_dump) | Generate a dictionary representation of the model, optionally specifying which fields to include or exclude. |
| [`model_dump_json()`](#model_dump_json) | Generates a JSON representation of the model using Pydantic's `to_json` method. |
| [`model_json_schema()`](#model_json_schema) | Generates a JSON schema for a model class. |
| [`model_parametrized_name()`](#model_parametrized_name) | Compute the class name for parametrizations of generic classes. |
| [`model_post_init()`](#model_post_init) | Override this method to perform additional initialization after `__init__` and `model_construct`. |
| [`model_rebuild()`](#model_rebuild) | Try to rebuild the pydantic-core schema for the model. |
| [`model_validate()`](#model_validate) | Validate a pydantic model instance. |
| [`model_validate_json()`](#model_validate_json) | Validate the given JSON data against the Pydantic model. |
| [`model_validate_strings()`](#model_validate_strings) | Validate the given object with string data against the Pydantic model. |
| [`parse_file()`](#parse_file) |  |
| [`parse_obj()`](#parse_obj) |  |
| [`parse_raw()`](#parse_raw) |  |
| [`schema()`](#schema) |  |
| [`schema_json()`](#schema_json) |  |
| [`update_forward_refs()`](#update_forward_refs) |  |
| [`validate()`](#validate) |  |


### check_type()

```python
def check_type(
    data: typing.Any,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `data` | `typing.Any` | |

### construct()

```python
def construct(
    _fields_set: set[str] | None,
    values: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `_fields_set` | `set[str] \| None` | |
| `values` | `Any` | |

### copy()

```python
def copy(
    include: AbstractSetIntStr | MappingIntStrAny | None,
    exclude: AbstractSetIntStr | MappingIntStrAny | None,
    update: Dict[str, Any] | None,
    deep: bool,
) -> Self
```
Returns a copy of the model.

> [!WARNING] Deprecated
> This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```python {test="skip" lint="skip"}
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```



| Parameter | Type | Description |
|-|-|-|
| `include` | `AbstractSetIntStr \| MappingIntStrAny \| None` | Optional set or mapping specifying which fields to include in the copied model. |
| `exclude` | `AbstractSetIntStr \| MappingIntStrAny \| None` | Optional set or mapping specifying which fields to exclude in the copied model. |
| `update` | `Dict[str, Any] \| None` | Optional dictionary of field-value pairs to override field values in the copied model. |
| `deep` | `bool` | If True, the values of fields that are Pydantic models will be deep-copied. |

### dict()

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
| Parameter | Type | Description |
|-|-|-|
| `include` | `IncEx \| None` | |
| `exclude` | `IncEx \| None` | |
| `by_alias` | `bool` | |
| `exclude_unset` | `bool` | |
| `exclude_defaults` | `bool` | |
| `exclude_none` | `bool` | |

### from_orm()

```python
def from_orm(
    obj: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | |

### get()

```python
def get()
```
### json()

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
| Parameter | Type | Description |
|-|-|-|
| `include` | `IncEx \| None` | |
| `exclude` | `IncEx \| None` | |
| `by_alias` | `bool` | |
| `exclude_unset` | `bool` | |
| `exclude_defaults` | `bool` | |
| `exclude_none` | `bool` | |
| `encoder` | `Callable[[Any], Any] \| None` | |
| `models_as_dict` | `bool` | |
| `dumps_kwargs` | `Any` | |

### materialize()

```python
def materialize()
```
### model_construct()

```python
def model_construct(
    _fields_set: set[str] | None,
    values: Any,
) -> Self
```
Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

> [!NOTE]
> `model_construct()` generally respects the `model_config.extra` setting on the provided model.
> That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
> and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
> Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
> an error if extra values are passed, but they will be ignored.



| Parameter | Type | Description |
|-|-|-|
| `_fields_set` | `set[str] \| None` | A set of field names that were originally explicitly set during instantiation. If provided, this is directly used for the [`model_fields_set`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_fields_set) attribute. Otherwise, the field names from the `values` argument will be used. |
| `values` | `Any` | Trusted or pre-validated data dictionary. |

### model_copy()

```python
def model_copy(
    update: Mapping[str, Any] | None,
    deep: bool,
) -> Self
```
> [!TIP] Usage Documentation (external docs for inherited method)
> [`model_copy`](https://docs.pydantic.dev/latest/concepts/models/#model-copy)

Returns a copy of the model.

> [!NOTE]
> The underlying instance's [`__dict__`](https://docs.python.org/3/library/stdtypes.html#object.__dict__) attribute is copied. This
> might have unexpected side effects if you store anything in it, on top of the model
> fields (e.g. the value of [cached properties](https://docs.python.org/3/library/functools.html#functools.cached_property)).



| Parameter | Type | Description |
|-|-|-|
| `update` | `Mapping[str, Any] \| None` | |
| `deep` | `bool` | Set to `True` to make a deep copy of the model. |

### model_dump()

```python
def model_dump(
    mode: Literal['json', 'python'] | str,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool | None,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    exclude_computed_fields: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    fallback: Callable[[Any], Any] | None,
    serialize_as_any: bool,
) -> dict[str, Any]
```
> [!TIP] Usage Documentation (external docs for inherited method)
> [`model_dump`](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.



| Parameter | Type | Description |
|-|-|-|
| `mode` | `Literal['json', 'python'] \| str` | The mode in which `to_python` should run. If mode is 'json', the output will only contain JSON serializable types. If mode is 'python', the output may contain non-JSON-serializable Python objects. |
| `include` | `IncEx \| None` | A set of fields to include in the output. |
| `exclude` | `IncEx \| None` | A set of fields to exclude from the output. |
| `context` | `Any \| None` | Additional context to pass to the serializer. |
| `by_alias` | `bool \| None` | Whether to use the field's alias in the dictionary key if defined. |
| `exclude_unset` | `bool` | Whether to exclude fields that have not been explicitly set. |
| `exclude_defaults` | `bool` | Whether to exclude fields that are set to their default value. |
| `exclude_none` | `bool` | Whether to exclude fields that have a value of `None`. |
| `exclude_computed_fields` | `bool` | Whether to exclude computed fields. While this can be useful for round-tripping, it is usually recommended to use the dedicated `round_trip` parameter instead. |
| `round_trip` | `bool` | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError). |
| `fallback` | `Callable[[Any], Any] \| None` | A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |
| `serialize_as_any` | `bool` | Whether to serialize fields with duck-typing serialization behavior. |

### model_dump_json()

```python
def model_dump_json(
    indent: int | None,
    ensure_ascii: bool,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool | None,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    exclude_computed_fields: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    fallback: Callable[[Any], Any] | None,
    serialize_as_any: bool,
) -> str
```
> [!TIP] Usage Documentation (external docs for inherited method)
> [`model_dump_json`](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode)

Generates a JSON representation of the model using Pydantic's `to_json` method.



| Parameter | Type | Description |
|-|-|-|
| `indent` | `int \| None` | Indentation to use in the JSON output. If None is passed, the output will be compact. |
| `ensure_ascii` | `bool` | If `True`, the output is guaranteed to have all incoming non-ASCII characters escaped. If `False` (the default), these characters will be output as-is. |
| `include` | `IncEx \| None` | Field(s) to include in the JSON output. |
| `exclude` | `IncEx \| None` | Field(s) to exclude from the JSON output. |
| `context` | `Any \| None` | Additional context to pass to the serializer. |
| `by_alias` | `bool \| None` | Whether to serialize using field aliases. |
| `exclude_unset` | `bool` | Whether to exclude fields that have not been explicitly set. |
| `exclude_defaults` | `bool` | Whether to exclude fields that are set to their default value. |
| `exclude_none` | `bool` | Whether to exclude fields that have a value of `None`. |
| `exclude_computed_fields` | `bool` | Whether to exclude computed fields. While this can be useful for round-tripping, it is usually recommended to use the dedicated `round_trip` parameter instead. |
| `round_trip` | `bool` | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError). |
| `fallback` | `Callable[[Any], Any] \| None` | A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |
| `serialize_as_any` | `bool` | Whether to serialize fields with duck-typing serialization behavior. |

### model_json_schema()

```python
def model_json_schema(
    by_alias: bool,
    ref_template: str,
    schema_generator: type[GenerateJsonSchema],
    mode: JsonSchemaMode,
    union_format: Literal['any_of', 'primitive_type_array'],
) -> dict[str, Any]
```
Generates a JSON schema for a model class.



| Parameter | Type | Description |
|-|-|-|
| `by_alias` | `bool` | Whether to use attribute aliases or not. |
| `ref_template` | `str` | The reference template. - `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf) keyword to combine schemas (the default). - `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type) keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`. |
| `schema_generator` | `type[GenerateJsonSchema]` | To override the logic used to generate the JSON schema, as a subclass of `GenerateJsonSchema` with your desired modifications |
| `mode` | `JsonSchemaMode` | The mode in which to generate the schema. |
| `union_format` | `Literal['any_of', 'primitive_type_array']` | |

### model_parametrized_name()

```python
def model_parametrized_name(
    params: tuple[type[Any], ...],
) -> str
```
Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.



| Parameter | Type | Description |
|-|-|-|
| `params` | `tuple[type[Any], ...]` | Tuple of types of the class. Given a generic class `Model` with 2 type variables and a concrete model `Model[str, int]`, the value `(str, int)` would be passed to `params`. |

### model_post_init()

```python
def model_post_init(
    context: Any,
)
```
Override this method to perform additional initialization after `__init__` and `model_construct`.
This is useful if you want to do some validation that requires the entire model to be initialized.


| Parameter | Type | Description |
|-|-|-|
| `context` | `Any` | |

### model_rebuild()

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



| Parameter | Type | Description |
|-|-|-|
| `force` | `bool` | Whether to force the rebuilding of the model schema, defaults to `False`. |
| `raise_errors` | `bool` | Whether to raise errors, defaults to `True`. |
| `_parent_namespace_depth` | `int` | The depth level of the parent namespace, defaults to 2. |
| `_types_namespace` | `MappingNamespace \| None` | The types namespace, defaults to `None`. |

### model_validate()

```python
def model_validate(
    obj: Any,
    strict: bool | None,
    extra: ExtraValues | None,
    from_attributes: bool | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
Validate a pydantic model instance.



| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | The object to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value](https://docs.pydantic.dev/latest/api/config/#pydantic.ConfigDict.extra) for details. |
| `from_attributes` | `bool \| None` | Whether to extract data from object attributes. |
| `context` | `Any \| None` | Additional context to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

### model_validate_json()

```python
def model_validate_json(
    json_data: str | bytes | bytearray,
    strict: bool | None,
    extra: ExtraValues | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
> [!TIP] Usage Documentation (external docs for inherited method)
> [JSON Parsing](https://docs.pydantic.dev/latest/concepts/json/#json-parsing)

Validate the given JSON data against the Pydantic model.



| Parameter | Type | Description |
|-|-|-|
| `json_data` | `str \| bytes \| bytearray` | The JSON data to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value](https://docs.pydantic.dev/latest/api/config/#pydantic.ConfigDict.extra) for details. |
| `context` | `Any \| None` | Extra variables to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

### model_validate_strings()

```python
def model_validate_strings(
    obj: Any,
    strict: bool | None,
    extra: ExtraValues | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
Validate the given object with string data against the Pydantic model.



| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | The object containing string data to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value](https://docs.pydantic.dev/latest/api/config/#pydantic.ConfigDict.extra) for details. |
| `context` | `Any \| None` | Extra variables to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

### parse_file()

```python
def parse_file(
    path: str | Path,
    content_type: str | None,
    encoding: str,
    proto: DeprecatedParseProtocol | None,
    allow_pickle: bool,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str \| Path` | |
| `content_type` | `str \| None` | |
| `encoding` | `str` | |
| `proto` | `DeprecatedParseProtocol \| None` | |
| `allow_pickle` | `bool` | |

### parse_obj()

```python
def parse_obj(
    obj: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | |

### parse_raw()

```python
def parse_raw(
    b: str | bytes,
    content_type: str | None,
    encoding: str,
    proto: DeprecatedParseProtocol | None,
    allow_pickle: bool,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `b` | `str \| bytes` | |
| `content_type` | `str \| None` | |
| `encoding` | `str` | |
| `proto` | `DeprecatedParseProtocol \| None` | |
| `allow_pickle` | `bool` | |

### schema()

```python
def schema(
    by_alias: bool,
    ref_template: str,
) -> Dict[str, Any]
```
| Parameter | Type | Description |
|-|-|-|
| `by_alias` | `bool` | |
| `ref_template` | `str` | |

### schema_json()

```python
def schema_json(
    by_alias: bool,
    ref_template: str,
    dumps_kwargs: Any,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `by_alias` | `bool` | |
| `ref_template` | `str` | |
| `dumps_kwargs` | `Any` | |

### update_forward_refs()

```python
def update_forward_refs(
    localns: Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `localns` | `Any` | |

### validate()

```python
def validate(
    value: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `Any` | |

