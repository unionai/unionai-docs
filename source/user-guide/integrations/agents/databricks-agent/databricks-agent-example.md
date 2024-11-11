# Databricks agent example

## Running Spark on Databricks

To begin, import the required dependencies.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/databricks_agent/databricks_agent/databricks_agent_example_usage.py
:language: python
:lines: 8-14
```

To run a Spark job on the Databricks platform, simply include Databricks configuration in the task config.
The Databricks config is the same as the Databricks job request. For more details, please refer to the [Databricks job request](https://docs.databricks.com/dev-tools/api/2.0/jobs.html#request-structure) documentation.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/databricks_agent/databricks_agent/databricks_agent_example_usage.py
:language: python
:lines: 22-56
```

For this particular example, we define a function that executes the map-reduce operation within the Spark cluster.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/databricks_agent/databricks_agent/databricks_agent_example_usage.py
:language: python
:lines: 63-66
```

Additionally, we define a standard Flyte task that won't be executed on the Spark cluster.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/databricks_agent/databricks_agent/databricks_agent_example_usage.py
:language: python
:lines: 72-75
```

Finally, define a workflow that connects your tasks in a sequence. Remember, Spark and non-Spark tasks can be chained together as long as their parameter specifications match.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/databricks_agent/databricks_agent/databricks_agent_example_usage.py
:language: python
:lines: 82-86
```

You can execute the workflow locally.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/databricks_agent/databricks_agent/databricks_agent_example_usage.py
:language: python
:lines: 92-96
```
