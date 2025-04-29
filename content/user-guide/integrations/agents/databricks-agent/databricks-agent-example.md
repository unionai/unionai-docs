---
title: Databricks connector example
weight: 1
variants: +flyte -serverless +byoc +byok
---

# Databricks connector example

```python
# Running Spark on Databricks
#
# To begin, import the required dependencies.
import datetime
import random
from operator import add

import {{< key kit_import >}}
from flytekitplugins.spark import DatabricksV2 as Databricks


# To run a Spark job on the Databricks platform, simply include Databricks configuration in the task config.
# The Databricks config is the same as the Databricks job request. For more details, please refer to the
# [Databricks job request](https://docs.databricks.com/dev-tools/api/2.0/jobs.html#request-structure) documentation.
@{{< key kit_as >}}.task(
    task_config=Databricks(
        spark_conf={
            "spark.driver.memory": "1000M",
            "spark.executor.memory": "1000M",
            "spark.executor.cores": "1",
            "spark.executor.instances": "2",
            "spark.driver.cores": "1",
        },
        databricks_conf={
            "run_name": "databricks plugin example",
            "new_cluster": {
                "spark_version": "11.0.x-scala2.12",
                "node_type_id": "r3.xlarge",
                "aws_attributes": {
                    "availability": "ON_DEMAND",
                    "instance_profile_arn": "arn:aws:iam::<AWS_ACCOUNT_ID_DATABRICKS>:instance-profile/databricks-flyte-integration",
                },
                "num_workers": 4,
            },
            "timeout_seconds": 3600,
            "max_retries": 1,
        },
    ),
    limits=Resources(mem="2000M"),
    cache_version="1",
)
def hello_spark(partitions: int) -> float:
    print(f"Starting Spark with {partitions} partitions.")
    n = 100000 * partitions
    sess = {{< key kit_as >}}.current_context().spark_session
    count = sess.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    pi_val = 4.0 * count / n
    print("Pi val is :{}".format(pi_val))
    return pi_val


# For this particular example,
# we define a function that executes the map-reduce operation within the Spark cluster.
def f(_):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    return 1 if x**2 + y**2 <= 1 else 0


# Additionally, we define a standard Flyte task that won't be executed on the Spark cluster.
@{{< key kit_as >}}.task(cache_version="1")
def print_every_time(value_to_print: float, date_triggered: datetime.datetime) -> int:
    print("My printed value: {} @ {}".format(value_to_print, date_triggered))
    return 1



# Finally, define a workflow that connects your tasks in a sequence.
# Remember, Spark and non-Spark tasks can be chained together as long as their parameter specifications match.
@{{< key kit_as >}}.workflow
def my_databricks_job(triggered_date: datetime.datetime = datetime.datetime.now()) -> float:
    pi = hello_spark(partitions=1)
    print_every_time(value_to_print=pi, date_triggered=triggered_date)
    return pi
```
