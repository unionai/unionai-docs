---
title: flytekitplugins.whylogs.renderer
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.whylogs.renderer

## Directory

### Classes

| Class | Description |
|-|-|
| [`WhylogsConstraintsRenderer`](.././flytekitplugins.whylogs.renderer#flytekitpluginswhylogsrendererwhylogsconstraintsrenderer) | Creates a whylogs' Constraints report from a `Constraints` object. |
| [`WhylogsSummaryDriftRenderer`](.././flytekitplugins.whylogs.renderer#flytekitpluginswhylogsrendererwhylogssummarydriftrenderer) | Creates a whylogs' Summary Drift report from two pandas DataFrames. |

## flytekitplugins.whylogs.renderer.WhylogsConstraintsRenderer

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

## flytekitplugins.whylogs.renderer.WhylogsSummaryDriftRenderer

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

