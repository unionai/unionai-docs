---
title: BigQuery
weight: 1
variants: +flyte +union
---

# BigQuery

The BigQuery connector lets you run SQL queries against [Google BigQuery](https://cloud.google.com/bigquery) directly from Flyte tasks. Queries are submitted asynchronously via the BigQuery Jobs API and polled for completion, so they don't block a worker while waiting for results.

The connector supports:

- Parameterized SQL queries with typed inputs
- Google Cloud service account authentication
- Returns query results as DataFrames
- Query cancellation on task abort

## Installation

```bash
pip install flyteplugins-bigquery
```

This installs the Google Cloud BigQuery client libraries.

## Quick start

Here's a minimal example that runs a SQL query on BigQuery:

```python
from flyte.io import DataFrame
from flyteplugins.bigquery import BigQueryConfig, BigQueryTask

config = BigQueryConfig(
    ProjectID="my-gcp-project",
    Location="US",
)

count_users = BigQueryTask(
    name="count_users",
    query_template="SELECT COUNT(*) FROM dataset.users",
    plugin_config=config,
    output_dataframe_type=DataFrame,
)
```

This defines a task called `count_users` that runs the query on the configured BigQuery instance. When executed, the connector:

1. Connects to BigQuery using the provided configuration
2. Submits the query asynchronously via the Jobs API
3. Polls until the query completes or fails

To run the task, create a `TaskEnvironment` from it and execute it locally or remotely:

```python
import flyte

bigquery_env = flyte.TaskEnvironment.from_task("bigquery_env", count_users)

if __name__ == "__main__":
    flyte.init_from_config()

    # Run locally (connector runs in-process, requires credentials locally)
    run = flyte.with_runcontext(mode="local").run(count_users)

    # Run remotely (connector runs on the control plane)
    run = flyte.with_runcontext(mode="remote").run(count_users)

    print(run.url)
```

> [!NOTE]
> The `TaskEnvironment` created by `from_task` does not need an image or pip packages. BigQuery tasks are connector tasks, which means the query executes on the connector service, not in your task container. In `local` mode, the connector runs in-process and requires `flyteplugins-bigquery` and credentials to be available on your machine.

## Configuration

### `BigQueryConfig` parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ProjectID` | `str` | Yes | GCP project ID |
| `Location` | `str` | No | BigQuery region (e.g., `"US"`, `"EU"`) |
| `QueryJobConfig` | `bigquery.QueryJobConfig` | No | Native BigQuery [QueryJobConfig](https://cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJobConfig) object for advanced settings |

### `BigQueryTask` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | `str` | Unique task name |
| `query_template` | `str` | SQL query (whitespace is normalized before execution) |
| `plugin_config` | `BigQueryConfig` | Connection configuration |
| `inputs` | `Dict[str, Type]` | Named typed inputs bound as query parameters |
| `output_dataframe_type` | `Type[DataFrame]` | If set, query results are returned as a `DataFrame` |
| `google_application_credentials` | `str` | Name of the Flyte secret containing the GCP service account JSON key |

## Authentication

Pass the name of a Flyte secret containing your GCP service account JSON key:

```python
query = BigQueryTask(
    name="secure_query",
    query_template="SELECT * FROM dataset.sensitive_data",
    plugin_config=config,
    google_application_credentials="my-gcp-sa-key",
)
```

## Query templating

Use the `inputs` parameter to define typed inputs for your query. Input values are bound as BigQuery `ScalarQueryParameter` values.

### Supported input types

| Python type | BigQuery type |
|-------------|---------------|
| `int` | `INT64` |
| `float` | `FLOAT64` |
| `str` | `STRING` |
| `bool` | `BOOL` |
| `bytes` | `BYTES` |
| `datetime` | `DATETIME` |
| `list` | `ARRAY` |

### Parameterized query example

```python
from flyte.io import DataFrame

events_by_region = BigQueryTask(
    name="events_by_region",
    query_template="SELECT * FROM dataset.events WHERE region = @region AND score > @min_score",
    plugin_config=config,
    inputs={"region": str, "min_score": float},
    output_dataframe_type=DataFrame,
)
```

> [!NOTE]
> The query template is normalized before execution: newlines and tabs are replaced with spaces and consecutive whitespace is collapsed. You can format your queries across multiple lines for readability without affecting execution.

## Retrieving query results

Set `output_dataframe_type` to capture results as a DataFrame:

```python
from flyte.io import DataFrame

top_customers = BigQueryTask(
    name="top_customers",
    query_template="""
        SELECT customer_id, SUM(amount) AS total_spend
        FROM dataset.orders
        GROUP BY customer_id
        ORDER BY total_spend DESC
        LIMIT 100
    """,
    plugin_config=config,
    output_dataframe_type=DataFrame,
)
```

If you don't need query results (for example, DDL statements or INSERT queries), omit `output_dataframe_type`.

## API reference

See the [BigQuery API reference](../../api-reference/integrations/bigquery/_index) for full details.
