# Task types

Task types include:

* **`PythonFunctionTask`**: This Python class represents the standard default task.
It is the type that is created when you use the `@task` decorator.
* **`ContainerTask`**: This Python class represents a raw container.
It allows you to install any image you like, giving you complete control of the task.
* **Map tasks**: The map task functionality enables you to run multiple copies of the same task across multiple containers in parallel.
* **Specialized plugin tasks**: These include both specialized classes and specialized configurations of the `PythonFunctionTask`.
They implement integrations with third-party systems.

## PythonFunctionTask

This is the task type that is created when you add the `@task` decorator to a Python function.
It represents a Python function that will be run within a single container. For example::

```{code-block} python
@task
def get_data() -> pd.DataFrame:
    """Get the wine dataset."""
    return load_wine(as_frame=True).frame

```

See the [Python Function Task example](https://github.com/unionai-oss/union-cloud-docs-examples/tree/main/python_function_task).

This is the most common task variant and the one that, thus far, we have focused on in this documentation.

## ContainerTask

This task variant represents a raw container, with no assumptions made about what is running within it.
Here is an example of declaring a `ContainerTask`:

```{code-block} python
greeting_task = ContainerTask(
    name="echo_and_return_greeting",
    image="alpine:latest",
    input_data_dir="/var/inputs",
    output_data_dir="/var/outputs",
    inputs=kwtypes(name=str),
    outputs=kwtypes(greeting=str),
    command=["/bin/sh", "-c", "echo 'Hello, my name is {{.inputs.name}}.' | tee -a /var/outputs/greeting"],
)

```

The `ContainerTask` enables you to include a task in your workflow that executes arbitrary code in any language, not just Python.

{@# TODO: Besides support for other languages, there are other reasons to use a container task. Mention them here. #@}

See the [Container Task example](https://github.com/unionai-oss/union-cloud-docs-examples/tree/main/container_task).

## Map tasks

A map task allows you to execute many instances of a task within a single workflow node.
This enables you to execute a task across a set of inputs without having to create a node for each input, resulting in significant performance improvements.

Map tasks find application in various scenarios, including:

* When multiple inputs require running through the same code logic.
* Processing multiple data batches concurrently.
* Conducting hyperparameter optimization.

Just like normal tasks, map tasks are automatically parallelized to the extent possible given resources available in the cluster.

```{code-block} python
THRESHOLD = 11

@task
def detect_anomalies(data_point: int) -> bool:
    return data_point > THRESHOLD

@workflow
def map_workflow(data: list[int] = [10, 12, 11, 10, 13, 12, 100, 11, 12, 10]) -> list[bool]:
    # Use the map task to apply the anomaly detection function to each data point
    return map_task(detect_anomalies)(data_point=data)

```

```{note}
Map tasks can also map over launch plans. For more information and example code, see [Mapping over launch plans](../launch-plans/mapping-over-launch-plans).
```

For more details see [Map Task example](https://github.com/unionai-oss/union-cloud-docs-examples/tree/main/map_task) in the `unionai-examples` repository and [Map Tasks](https://docs.flyte.org/en/latest/user_guide/advanced_composition/map_tasks.html#map-task) in the Flyte docs.

## Specialized plugin task classes and configs

Union supports a wide variety of plugin tasks.
Some of these are enabled as specialized task classes, others as specialized configurations of the default `@task` (`PythonFunctionTask`).

They enable things like:

* Querying external databases (AWS Athena, BigQuery, DuckDB, SQL, Snowflake, Hive).
* Executing specialized processing right in Union (Spark in virtual cluster, Dask in Virtual cluster, Sagemaker, Airflow, Modin, Ray, MPI and Horovod).
* Handing off processing to external services(AWS Batch, Spark on Databricks, Ray on external cluster).
* Data transformation(Great Expectations, DBT, Dolt, ONNX, Pandera).
* Data tracking and presentation  (MLFlow, Papermill).

See the [Integration section](https://docs.flyte.org/en/latest/flytesnacks/integrations.html) of the Flyte documentation for examples.


<!-- INCORPORATE THE FOLLOWING ABOVE WHERE NECESSARY

## @task parameters

`task_config`: This argument provides configuration for a specific task types. Please refer to the plugins documentation for the right object to use.
It is impossible to define the unit of execution of a task in the same
way for all tasks. Hence, Flyte allows for different task types in the
system. Flyte has a set of defined, battle-tested task types. It allows
for a flexible model to
`define new types <cookbook:plugins_extend>`{.interpreted-text
role="std:ref"}.
Flyte offers numerous plugins for tasks, including backend plugins like Athena.
Flyte exposes an extensible model to express tasks in an
execution-independent language. It contains first-class task plugins
(for example:
[Papermill](https://github.com/flyteorg/flytekit/blob/master/plugins/flytekit-papermill/flytekitplugins/papermill/task.py),
[Great
Expectations](https://github.com/flyteorg/flytekit/blob/master/plugins/flytekit-greatexpectations/flytekitplugins/great_expectations/task.py),
and `more <integrations>`{.interpreted-text role="ref"}.) that execute
the Flyte tasks. Almost any action can be implemented and introduced
into Flyte as a \"Plugin\", which includes:
- Tasks that run queries on distributed data warehouses like Redshift, Hive, Snowflake, etc.
- Tasks that run executions on compute engines like Spark, Flink, AWS Sagemaker, AWS Batch, Kubernetes pods, jobs, etc.
- Tasks that call web services.
Flyte ships with certain defaults, for example, running a simple Python
function does not need any hosted service. Flyte knows how to execute
these kinds of tasks on Kubernetes. It turns out these are the vast
majority of tasks in machine learning, and Flyte is adept at handling an
enormous scale on Kubernetes. This is achieved by implementing a unique
scheduler on Kubernetes.

-->
