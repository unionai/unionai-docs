---
title: BigQueryConfig
version: 2.0.0b53
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# BigQueryConfig

**Package:** `flyteplugins.connectors.bigquery`

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

