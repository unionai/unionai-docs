---
title: flytekitplugins.whylogs
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.whylogs

## Directory

### Classes

| Class | Description |
|-|-|
| [`WhylogsConstraintsRenderer`](.././flytekitplugins.whylogs#flytekitpluginswhylogswhylogsconstraintsrenderer) | Creates a whylogs' Constraints report from a `Constraints` object. |
| [`WhylogsDatasetProfileTransformer`](.././flytekitplugins.whylogs#flytekitpluginswhylogswhylogsdatasetprofiletransformer) | Transforms whylogs Dataset Profile Views to and from a Schema (typed/untyped). |
| [`WhylogsSummaryDriftRenderer`](.././flytekitplugins.whylogs#flytekitpluginswhylogswhylogssummarydriftrenderer) | Creates a whylogs' Summary Drift report from two pandas DataFrames. |

## flytekitplugins.whylogs.WhylogsConstraintsRenderer

Creates a whylogs' Constraints report from a `Constraints` object. Currently our API
requires the user to have a profiled DataFrame in place to be able to use it. Then the report
will render a nice HTML that will let users check which constraints passed or failed their
logic. An example constraints object definition can be written as follows:

.. code-block:: python

    profile_view = why.log(df).view()
    builder = ConstraintsBuilder(profile_view)
    num_constraint = MetricConstraint(
                        name=f'numbers between {min_value} and {max_value} only',
                        condition=lambda x: x.min > min_value and x.max < max_value,
                        metric_selector=MetricsSelector(
                                                metric_name='distribution',
                                                column_name='sepal_length'
                                                )
                    )

    builder.add_constraint(num_constraint)
    constraints = builder.build()

Each Constraints object (builder.build() in the former example) can have as many constraints as
desired. If you want to learn more, check out our docs and examples at https://whylogs.readthedocs.io/


### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) |  |


#### to_html()

```python
def to_html(
    constraints: whylogs.core.constraints.metric_constraints.Constraints,
) -> str
```
| Parameter | Type |
|-|-|
| `constraints` | `whylogs.core.constraints.metric_constraints.Constraints` |

## flytekitplugins.whylogs.WhylogsDatasetProfileTransformer

Transforms whylogs Dataset Profile Views to and from a Schema (typed/untyped)


```python
def WhylogsDatasetProfileTransformer()
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
    t: typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView],
) -> flytekit.models.types.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView]` |

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
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: whylogs.core.view.dataset_profile_view.DatasetProfileView,
    expected_python_type: typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `python_val` | `whylogs.core.view.dataset_profile_view.DatasetProfileView` |
| `expected_python_type` | `typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView]` |

#### to_literal()

```python
def to_literal(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: whylogs.core.view.dataset_profile_view.DatasetProfileView,
    python_type: typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView],
    expected: flytekit.models.types.LiteralType,
) -> flytekit.models.literals.Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `python_val` | `whylogs.core.view.dataset_profile_view.DatasetProfileView` |
| `python_type` | `typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView]` |
| `expected` | `flytekit.models.types.LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView],
) -> ~T
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `lv` | `flytekit.models.literals.Literal` |
| `expected_python_type` | `typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekitplugins.whylogs.WhylogsSummaryDriftRenderer

Creates a whylogs' Summary Drift report from two pandas DataFrames. One of them
is the reference and the other one is the target data, meaning that this is what
the report will compare it against.


### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) | This static method will profile the input data and then generate an HTML report. |


#### to_html()

```python
def to_html(
    reference_data: pandas.core.frame.DataFrame,
    target_data: pandas.core.frame.DataFrame,
) -> str
```
This static method will profile the input data and then generate an HTML report
with the Summary Drift calculations for all the dataframe's columns



| Parameter | Type |
|-|-|
| `reference_data` | `pandas.core.frame.DataFrame` |
| `target_data` | `pandas.core.frame.DataFrame` |

