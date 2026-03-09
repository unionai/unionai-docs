---
title: BigQueryConfig
version: 2.0.4
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# BigQueryConfig

**Package:** `flyteplugins.bigquery`

BigQueryConfig should be used to configure a BigQuery Task.



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

