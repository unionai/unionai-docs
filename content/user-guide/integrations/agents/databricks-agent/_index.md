---
title: Databricks agent
weight: 3
variants: +flyte -serverless +byoc +byok
sidebar_expanded: true
---

# Databricks agent

{{< key product_name >}} can be integrated with the [Databricks](https://www.databricks.com/) service,
enabling you to submit Spark jobs to the Databricks platform.

## Installation

The Databricks agent comes bundled with the Spark plugin. To install the Spark plugin, run the following command:

```
pip install flytekitplugins-spark
```

## Example usage

For a usage example, see [Databricks agent example](./databricks-agent-example).

## Local testing

To test the Databricks agent copy the following code to a file called `databricks_task.py`, modifying as needed.

```python
@{{< key kit_as >}}.task(task_config=Databricks(...))
def hello_spark(partitions: int) -> float:
    print("Starting Spark with Partitions: {}".format(partitions))

    n = 100000 * partitions
    sess = {{< key kit_as >}}.current_context().spark_session
    count = (
        sess.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    )
    pi_val = 4.0 * count / n
    print("Pi val is :{}".format(pi_val))
    return pi_val
```

To execute the Spark task on the agent, you must configure the `raw-output-data-prefix` with a remote path.
This configuration ensures that {{< key product_name >}} transfers the input data to the blob storage and allows the Spark job running on Databricks to access the input data directly from the designated bucket.

> [!NOTE]
> The Spark task will run locally if the `raw-output-data-prefix` is not set.

```shell
$ {{< key cli >}} run --raw-output-data-prefix s3://my-s3-bucket/databricks databricks_task.py hello_spark
```

{{< variant byoc >}}
{{< markdown >}}

## {{< key product_name >}} cluster deployment

After you have finished testing the agent locally, contact the {{< key product_name >}} team to enable it in your cluster.

{{< /markdown >}}
{{< /variant >}}
