---
title: BigQueryConfig
version: 2.1.9
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# BigQueryConfig

**Package:** `flyteplugins.bigquery`

Configuration for a BigQuery task.



## Parameters

```python
class BigQueryConfig(
    ProjectID: str,
    Location: typing.Optional[str],
    QueryJobConfig: typing.Optional[google.cloud.bigquery.job.query.QueryJobConfig],
)
```
| Parameter | Type | Description |
|-|-|-|
| `ProjectID` | `str` | The Google Cloud project ID that owns the BigQuery dataset. |
| `Location` | `typing.Optional[str]` | The geographic location of the dataset, e.g. `"US"` or `"EU"`. Defaults to the project's default location if not specified. |
| `QueryJobConfig` | `typing.Optional[google.cloud.bigquery.job.query.QueryJobConfig]` | Optional advanced job configuration passed directly to the BigQuery client. Use this to set query parameters, destination tables, time partitioning, etc. |

