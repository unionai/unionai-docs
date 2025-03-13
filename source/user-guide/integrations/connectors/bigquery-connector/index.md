# Google BigQuery connector

## Installation

To install the BigQuery connector, run the following command:

```
pip install flytekitplugins-bigquery
```

## Example usage

For an example query, see [BigQuery connector example](./bigquery-connector-example.md).

## Local testing

To test the BigQuery connector locally, create a class for the connector task that inherits from [`AsyncConnectorExecutorMixin`](https://github.com/flyteorg/flytekit/blob/03d23011fcf955838669bd5058c8ced17c6de3ee/flytekit/extend/backend/base_connector.py#L278-382). This mixin allows flytekit to mimic FlytePropeller's behavior in calling the connector.

To test the BigQuery connector, copy the following code to a file called `bigquery_task.py`, modifying as needed.

:::{note}
When testing the BigQuery integration locally, you will need to set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
:::

Add `AsyncConnectorExecutorMixin` to this class to tell flytekit to use the connector to run the task:
```{code-block} python
class BigQueryTask(AsyncConnectorExecutorMixin, SQLTask[BigQueryConfig]):
    def __init__(self, name: str, **kwargs):
        ...
```

Flytekit will automatically use the connector to run the task in the local execution.
```{code-block} python
bigquery_doge_coin = BigQueryTask(
    name=f"bigquery.doge_coin",
    inputs=kwtypes(version=int),
    query_template="SELECT * FROM `bigquery-public-data.crypto_dogecoin.transactions` WHERE version = @version LIMIT 10;",
    output_structured_dataset_type=StructuredDataset,
    task_config=BigQueryConfig(ProjectID="flyte-test-340607")
)
```

You can run the above example task locally and test the connector with the following command:

```{code-block} shell
$ union run bigquery_task.py bigquery_doge_coin --version 10
```

{@@ if byoc @@}
## Union cluster deployment

After you have finished testing the connector locally, contact the Union team to enable it in your cluster.
{@@ endif @@}