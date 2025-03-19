# Google BigQuery agent example

This example shows how to use a BigQueryTask to execute a query.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/bigquery_agent/bigquery_agent/bigquery_agent_example_usage.py
:language: python
:lines: 7-10
```

This is the world's simplest query. Note that in order for registration to work properly, you'll need to give your BigQuery task a name that's unique across your project/domain for your Union deployment.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/bigquery_agent/bigquery_agent/bigquery_agent_example_usage.py
:language: python
:lines: 16-26
```

Of course, in real world applications, we are usually more interested in using BigQuery to query a dataset.
In this case we use crypto_dogecoin data, which is a public dataset in BigQuery [here](https://console.cloud.google.com/bigquery?project=bigquery-public-data&page=table&d=crypto_dogecoin&p=bigquery-public-data&t=transactions).

Let's look out how we can parameterize our query to filter results for a specific transaction version, provided as a user input specifying a version.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/bigquery_agent/bigquery_agent/bigquery_agent_example_usage.py
:language: python
:lines: 38-47
```

The `StructuredDataset` transformer can convert query result to a `pandas` dataframe here.
We can also change `pandas.datafram"` to `pyarrow.Table`, and convert the result to an Arrow table.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/bigquery_agent/bigquery_agent/bigquery_agent_example_usage.py
:language: python
:lines: 54-62
```

You can check the query result on the [BigQuery console](https://console.cloud.google.com/bigquery).