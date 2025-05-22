---
title: flytekitplugins.pandera.pandas_renderer
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.pandera.pandas_renderer

## Directory

### Classes

| Class | Description |
|-|-|
| [`PandasReport`](.././flytekitplugins.pandera.pandas_renderer#flytekitpluginspanderapandas_rendererpandasreport) |  |
| [`PandasReportRenderer`](.././flytekitplugins.pandera.pandas_renderer#flytekitpluginspanderapandas_rendererpandasreportrenderer) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `DATA_ERROR_COLUMNS` | `list` |  |
| `DATA_ERROR_DISPLAY_ORDER` | `list` |  |
| `DATA_ERROR_KEY` | `str` |  |
| `DATA_PREVIEW_HEAD` | `int` |  |
| `ERROR_COLUMN_MAX_WIDTH` | `int` |  |
| `FAILURE_CASE_LIMIT` | `int` |  |
| `SCHEMA_ERROR_COLUMNS` | `list` |  |
| `SCHEMA_ERROR_KEY` | `str` |  |
| `TYPE_CHECKING` | `bool` |  |

## flytekitplugins.pandera.pandas_renderer.PandasReport

```python
class PandasReport(
    summary: pandas.core.frame.DataFrame,
    data_preview: pandas.core.frame.DataFrame,
    schema_error_df: typing.Optional[pandas.core.frame.DataFrame],
    data_error_df: typing.Optional[pandas.core.frame.DataFrame],
)
```
| Parameter | Type |
|-|-|
| `summary` | `pandas.core.frame.DataFrame` |
| `data_preview` | `pandas.core.frame.DataFrame` |
| `schema_error_df` | `typing.Optional[pandas.core.frame.DataFrame]` |
| `data_error_df` | `typing.Optional[pandas.core.frame.DataFrame]` |

## flytekitplugins.pandera.pandas_renderer.PandasReportRenderer

```python
class PandasReportRenderer(
    title: str,
)
```
| Parameter | Type |
|-|-|
| `title` | `str` |

### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) |  |


#### to_html()

```python
def to_html(
    data: pandas.DataFrame,
    schema: pandera.api.pandas.container.DataFrameSchema,
    error: typing.Optional[pandera.errors.SchemaErrors],
) -> str
```
| Parameter | Type |
|-|-|
| `data` | `pandas.DataFrame` |
| `schema` | `pandera.api.pandas.container.DataFrameSchema` |
| `error` | `typing.Optional[pandera.errors.SchemaErrors]` |

