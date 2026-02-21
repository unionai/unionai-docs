---
title: flytekitplugins.whylogs
version: 1.16.14
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
                        condition=lambda x: x.min &gt; min_value and x.max &lt; max_value,
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
| Parameter | Type | Description |
|-|-|-|
| `constraints` | `whylogs.core.constraints.metric_constraints.Constraints` | |

## flytekitplugins.whylogs.WhylogsDatasetProfileTransformer

Transforms whylogs Dataset Profile Views to and from a Schema (typed/untyped)



```python
def WhylogsDatasetProfileTransformer()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` | `None` |  |
| `name` | `None` |  |
| `python_type` | `None` | This returns the python type |
| `type_assertions_enabled` | `None` | Indicates if the transformer wants type assertions to be enabled at the core type engine layer |

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
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[T]` | |
| `v` | `T` | |

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
    python val -&gt; msgpack bytes -&gt; binary literal scalar -&gt; msgpack bytes -&gt; python val
                  (to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
    python val -&gt; msgpack bytes -&gt; binary literal scalar -&gt; resolved golang value -&gt; binary literal scalar -&gt; msgpack bytes -&gt; python val
                  (to_literal)                            (propeller attribute access)                       (from_binary_idl)


| Parameter | Type | Description |
|-|-|-|
| `binary_idl_object` | `Binary` | |
| `expected_python_type` | `Type[T]` | |

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


| Parameter | Type | Description |
|-|-|-|
| `generic` | `Struct` | |
| `expected_python_type` | `Type[T]` | |

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView],
) -> flytekit.models.types.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView]` | |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[T]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type | Description |
|-|-|-|
| `literal_type` | `LiteralType` | |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type | Description |
|-|-|-|
| `obj` |  | |
| `generic_alias` |  | |

#### to_html()

```python
def to_html(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: whylogs.core.view.dataset_profile_view.DatasetProfileView,
    expected_python_type: typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `python_val` | `whylogs.core.view.dataset_profile_view.DatasetProfileView` | |
| `expected_python_type` | `typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView]` | |

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


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `python_val` | `whylogs.core.view.dataset_profile_view.DatasetProfileView` | The actual value to be transformed |
| `python_type` | `typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `flytekit.models.types.LiteralType` | Expected Literal Type |

#### to_python_value()

```python
def to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView],
) -> ~T
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | FlyteContext |
| `lv` | `flytekit.models.literals.Literal` | The received literal Value |
| `expected_python_type` | `typing.Type[whylogs.core.view.dataset_profile_view.DatasetProfileView]` | Expected native python type that should be returned |

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
    reference_data: pandas.DataFrame,
    target_data: pandas.DataFrame,
) -> str
```
This static method will profile the input data and then generate an HTML report
with the Summary Drift calculations for all the dataframe's columns



| Parameter | Type | Description |
|-|-|-|
| `reference_data` | `pandas.DataFrame` | The DataFrame that will be the reference for the drift report :type: pandas.DataFrame |
| `target_data` | `pandas.DataFrame` | The data to compare against and create the Summary Drift report :type target_data: pandas.DataFrame |

