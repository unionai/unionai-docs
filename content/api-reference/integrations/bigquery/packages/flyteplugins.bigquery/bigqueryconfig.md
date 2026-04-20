---
title: BigQueryConfig
version: 2.0.11
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# BigQueryConfig

**Package:** `flyteplugins.bigquery`

Configuration for a BigQuery task.

    Attributes:
        ProjectID: The Google Cloud project ID that owns the BigQuery dataset.
        Location: The geographic location of the dataset, e.g. `"US"` or `"EU"`.
            Defaults to the project's default location if not specified.
        QueryJobConfig: Optional advanced job configuration passed directly to the
            BigQuery client. Use this to set query parameters, destination tables,
            time partitioning, etc.
    


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
| `ProjectID` | `str` | |
| `Location` | `typing.Optional[str]` | |
| `QueryJobConfig` | `typing.Optional[google.cloud.bigquery.job.query.QueryJobConfig]` | |

