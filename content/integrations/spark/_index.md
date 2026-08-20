---
title: Spark
weight: 1
variants: +flyte +union
---

# Spark

The Spark plugin lets you run [Apache Spark](https://spark.apache.org/) jobs natively on Kubernetes. Flyte manages the full cluster lifecycle: provisioning a transient Spark cluster for each task execution, running the job, and tearing the cluster down on completion.

Under the hood, the plugin uses the [Spark on Kubernetes Operator](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator) to create and manage Spark applications. No external Spark service or long-running cluster is required.

## When to use this plugin

- Large-scale data processing and ETL pipelines
- Jobs that benefit from Spark's distributed execution engine (Spark SQL, PySpark, Spark MLlib)
- Workloads that need Hadoop-compatible storage access (S3, GCS, HDFS)

## Installation

```bash
pip install flyteplugins-spark
```

## Configuration

Create a `Spark` configuration and pass it as `plugin_config` to a `TaskEnvironment`:

```python
from flyteplugins.spark import Spark

spark_config = Spark(
    spark_conf={
        "spark.driver.memory": "3000M",
        "spark.executor.memory": "1000M",
        "spark.executor.cores": "1",
        "spark.executor.instances": "2",
        "spark.driver.cores": "1",
    },
)

spark_env = flyte.TaskEnvironment(
    name="spark_env",
    plugin_config=spark_config,
    image=image,
)
```

### `Spark` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `spark_conf` | `Dict[str, str]` | Spark configuration key-value pairs (e.g., executor memory, cores, instances) |
| `hadoop_conf` | `Dict[str, str]` | Hadoop configuration key-value pairs (e.g., S3/GCS access settings) |
| `executor_path` | `str` | Path to the Python binary for PySpark executors |
| `applications_path` | `str` | Path to the main Spark application file |
| `driver_pod` | `PodTemplate` | Pod template for the Spark driver pod |
| `executor_pod` | `PodTemplate` | Pod template for the Spark executor pods |

### Pod templates

There are two places to customize the driver and executor pods:

- **`TaskEnvironment(pod_template=...)`**: the task pod spec, used as the base pod template for *both* the driver and the executor pods.
- **`Spark(driver_pod=...)` / `Spark(executor_pod=...)`**: role-specific specs that replace that base pod template for the driver or the executor.

Both use `flyte.PodTemplate`. See [Pod templates](../../user-guide/tasks/task-configuration/pod-templates) for the general rules and for the `kubernetes` package the `V1*` types below come from.

#### On the task environment

Use this when the same customization (security context, tolerations, node selector, volumes) should apply to driver and executor alike. The spec must contain the primary container, the container Flyte injects the task image and command into, whose name defaults to `primary`:

```python
from kubernetes.client import V1Container, V1PodSecurityContext, V1PodSpec

spark_env = flyte.TaskEnvironment(
    name="spark_env",
    plugin_config=spark_config,
    pod_template=flyte.PodTemplate(
        pod_spec=V1PodSpec(
            containers=[V1Container(name="primary")],  # required: the primary container
            security_context=V1PodSecurityContext(run_as_user=1000),
        ),
    ),
    image=image,
)
```

Flyte renames the primary container to `spark-kubernetes-driver` / `spark-kubernetes-executor` before handing the template over, so Spark configures the right container.

#### On the plugin config

Use `driver_pod` / `executor_pod` when the two roles need to differ. These specs are passed through verbatim as the driver or executor pod template; they are *not* merged with the environment's pod template.

Name the container `spark-kubernetes-driver` or `spark-kubernetes-executor`. Spark selects the driver and executor container from the template by that name; if no container matches, it falls back to the first container in the list and configures that one instead, so a template with a sidecar ahead of the real container silently runs the sidecar as the driver. The canonical names are also what the Spark operator and Flyte's log links use to find the container.

```python
from kubernetes.client import V1Container, V1PodSpec, V1ResourceRequirements

spark_config = Spark(
    spark_conf={"spark.executor.instances": "2"},
    executor_pod=flyte.PodTemplate(
        pod_spec=V1PodSpec(
            containers=[
                V1Container(
                    name="spark-kubernetes-executor",
                    resources=V1ResourceRequirements(requests={"ephemeral-storage": "9Gi"}),
                )
            ],
        ),
    ),
)
```

Because a role-specific spec replaces the base template rather than merging into it, anything you still need from the environment's `pod_template`, such as volumes, volume mounts, or sidecars, has to be repeated in the `driver_pod` / `executor_pod` spec. Pod-level scheduling and security settings that Flyte passes to the operator separately (affinity, scheduler name, pod security context, and DNS config) come from the task environment and override the same fields in a role-specific spec. Tolerations, node selectors, and environment variables are combined rather than replaced, so values set in `driver_pod` / `executor_pod` are kept alongside the environment's.

### Accessing the Spark session

Inside a Spark task, the `SparkSession` is available through the task context:

```python
from flyte._context import internal_ctx

@spark_env.task
async def my_spark_task() -> float:
    ctx = internal_ctx()
    spark = ctx.data.task_context.data["spark_session"]
    # Use spark as a normal SparkSession
    df = spark.read.parquet("s3://my-bucket/data.parquet")
    return df.count()
```

### Overriding configuration at runtime

You can override Spark configuration for individual task calls using `.override()`:

```python
from copy import deepcopy

updated_config = deepcopy(spark_config)
updated_config.spark_conf["spark.executor.instances"] = "4"

result = await my_spark_task.override(plugin_config=updated_config)()
```

## Example

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/spark/spark_example.py" lang="python" >}}

## API reference

See the [Spark API reference](../../api-reference/integrations/spark/_index) for full details.
