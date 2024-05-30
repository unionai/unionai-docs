# Google BigQuery agent

## Installation

To install the BigQuery agent, run the following command:

```
pip install flytekitplugins-bigquery
```

## Example usage

For an example query, see [BigQuery agent example](bigquery-agent-example).

## Local testing

To test the BigQuery agent locally, create a class for the agent task that inherits from [AsyncAgentExecutorMixin](https://github.com/flyteorg/flytekit/blob/master/flytekit/extend/backend/base_agent.py#L155). This mixin allows flytekit to mimic FlytePropeller's behavior in calling the agent.

To test the BigQuery agent, copy the following code to a file called `bigquery_task.py`, modifying as needed.

:::{note}

When testing the BigQuery integration locally, you will need to set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.

:::

Add `AsyncAgentExecutorMixin` to this class to tell flytekit to use the agent to run the task:
```{code-block} python
class BigQueryTask(AsyncAgentExecutorMixin, SQLTask[BigQueryConfig]):
    def __init__(self, name: str, **kwargs):
        ...
```

Flytekit will automatically use the agent to run the task in the local execution.
```{code-block} python
bigquery_doge_coin = BigQueryTask(
    name=f"bigquery.doge_coin",
    inputs=kwtypes(version=int),
    query_template="SELECT * FROM `bigquery-public-data.crypto_dogecoin.transactions` WHERE version = @version LIMIT 10;",
    output_structured_dataset_type=StructuredDataset,
    task_config=BigQueryConfig(ProjectID="flyte-test-340607")
)
```

You can run the above example task locally and test the agent with the following command:

```{code-block} shell
$ unionai run bigquery_task.py bigquery_doge_coin --version 10
```

## Union cluster deployment

After you have finished testing the agent locally, contact the Union team to enable it in your cluster.
