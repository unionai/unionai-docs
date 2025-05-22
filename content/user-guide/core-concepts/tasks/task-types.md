---
title: Task types
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Other task types

Task types include:

* **`PythonFunctionTask`**: This Python class represents the standard default task.
It is the type that is created when you use the `@{{< key kit_as >}}.task` decorator.
* **`ContainerTask`**: This Python class represents a raw container.
It allows you to install any image you like, giving you complete control of the task.
* **Shell tasks**: Use them to execute `bash` scripts within {{< key product_name >}}.
* **Specialized plugin tasks**: These include both specialized classes and specialized configurations of the `PythonFunctionTask`.
They implement integrations with third-party systems.

## PythonFunctionTask

This is the task type that is created when you add the `@{{< key kit_as >}}.task` decorator to a Python function.
It represents a Python function that will be run within a single container. For example::

```python
@{{< key kit_as >}}.task
def get_data() -> pd.DataFrame:
    """Get the wine dataset."""
    return load_wine(as_frame=True).frame

```

See the [Python Function Task example](https://github.com/unionai-oss/union-cloud-docs-examples/tree/main/python_function_task).

This is the most common task variant and the one that, thus far, we have focused on in this documentation.

## ContainerTask

This task variant represents a raw container, with no assumptions made about what is running within it.
Here is an example of declaring a `ContainerTask`:

```python
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

In the following example, the tasks calculate an ellipse area. This name has to be unique in the entire project. Users can specify:

`input_data_dir` -> where inputs will be written to.

`output_data_dir` -> where {{< key product_name >}} will expect the outputs to exist.

The `inputs` and `outputs` specify the interface for the task; thus it should be an ordered dictionary of typed input and output variables.

The image field specifies the container image for the task, either as an image name or an ImageSpec. To access the file that is not included in the image, use ImageSpec to copy files or directories into container `/root`.

Cache can be enabled in a ContainerTask by configuring the cache settings in the `TaskMetadata` in the metadata parameter.

```python
calculate_ellipse_area_haskell = ContainerTask(
    name="ellipse-area-metadata-haskell",
    input_data_dir="/var/inputs",
    output_data_dir="/var/outputs",
    inputs=kwtypes(a=float, b=float),
    outputs=kwtypes(area=float, metadata=str),
    image="ghcr.io/flyteorg/rawcontainers-haskell:v2",
    command=[
        "./calculate-ellipse-area",
        "{{.inputs.a}}",
        "{{.inputs.b}}",
        "/var/outputs",
    ],
    metadata=TaskMetadata(cache=True, cache_version="1.0"),
)

calculate_ellipse_area_julia = ContainerTask(
    name="ellipse-area-metadata-julia",
    input_data_dir="/var/inputs",
    output_data_dir="/var/outputs",
    inputs=kwtypes(a=float, b=float),
    outputs=kwtypes(area=float, metadata=str),
    image="ghcr.io/flyteorg/rawcontainers-julia:v2",
    command=[
        "julia",
        "calculate-ellipse-area.jl",
        "{{.inputs.a}}",
        "{{.inputs.b}}",
        "/var/outputs",
    ],
    metadata=TaskMetadata(cache=True, cache_version="1.0"),
)

@workflow
def wf(a: float, b: float):
    area_haskell, metadata_haskell = calculate_ellipse_area_haskell(a=a, b=b)
    area_julia, metadata_julia = calculate_ellipse_area_julia(a=a, b=b)
```

See the [Container Task example](https://github.com/unionai-oss/union-cloud-docs-examples/tree/main/container_task).

## Shell tasks

Shell tasks enable the execution of shell scripts within {{<key product_name >}}.
To create a shell task, provide a name for it, specify the bash script to be executed, and define inputs and outputs if needed:

### Example
```python
from pathlib import Path
from typing import Tuple

import {{< key kit_import >}}
from flytekit import kwtypes
from flytekit.extras.tasks.shell import OutputLocation, ShellTask

t1 = ShellTask(
    name="task_1",
    debug=True,
    script="""
    set -ex
    echo "Hey there! Let's run some bash scripts using a shell task."
    echo "Showcasing shell tasks." >> {inputs.x}
    if grep "shell" {inputs.x}
    then
        echo "Found it!" >> {inputs.x}
    else
        echo "Not found!"
    fi
    """,
    inputs=kwtypes(x=FlyteFile),
    output_locs=[OutputLocation(var="i", var_type=FlyteFile, location="{inputs.x}")],
)


t2 = ShellTask(
    name="task_2",
    debug=True,
    script="""
    set -ex
    cp {inputs.x} {inputs.y}
    tar -zcvf {outputs.j} {inputs.y}
    """,
    inputs=kwtypes(x=FlyteFile, y=FlyteDirectory),
    output_locs=[OutputLocation(var="j", var_type=FlyteFile, location="{inputs.y}.tar.gz")],
)


t3 = ShellTask(
    name="task_3",
    debug=True,
    script="""
    set -ex
    tar -zxvf {inputs.z}
    cat {inputs.y}/$(basename {inputs.x}) | wc -m > {outputs.k}
    """,
    inputs=kwtypes(x=FlyteFile, y=FlyteDirectory, z=FlyteFile),
    output_locs=[OutputLocation(var="k", var_type=FlyteFile, location="output.txt")],
)
```
Here's a breakdown of the parameters of the `ShellTask`:

- The `inputs` parameter allows you to specify the types of inputs that the task will accept
- The `output_locs` parameter is used to define the output locations, which can be `FlyteFile` or `FlyteDirectory`
- The `script` parameter contains the actual bash script that will be executed
  (`{inputs.x}`, `{outputs.j}`, etc. will be replaced with the actual input and output values).
- The `debug` parameter is helpful for debugging purposes

We define a task to instantiate `FlyteFile` and `FlyteDirectory`.
A `.gitkeep` file is created in the `FlyteDirectory` as a placeholder to ensure the directory exists:

```python
@{{< key kit_as >}}.task
def create_entities() -> Tuple[{{< key kit_as >}}.FlyteFile, {{< key kit_as >}}.FlyteDirectory]:
    working_dir = Path({{< key kit_as >}}.current_context().working_directory)
    flytefile = working_dir / "test.txt"
    flytefile.touch()

    flytedir = working_dir / "testdata"
    flytedir.mkdir(exist_ok=True)

    flytedir_file = flytedir / ".gitkeep"
    flytedir_file.touch()
    return flytefile, flytedir
```
We create a workflow to define the dependencies between the tasks:

```python
@{{< key kit_as >}}.workflow
def shell_task_wf() -> {{< key kit_as >}}.FlyteFile:
    x, y = create_entities()
    t1_out = t1(x=x)
    t2_out = t2(x=t1_out, y=y)
    t3_out = t3(x=x, y=y, z=t2_out)
    return t3_out
```
You can run the workflow locally:
```python
if __name__ == "__main__":
    print(f"Running shell_task_wf() {shell_task_wf()}")
```

## Specialized plugin task classes and configs

{{< key product_name >}} supports a wide variety of plugin tasks.
Some of these are enabled as specialized task classes, others as specialized configurations of the default `@{{< key kit_as >}}.task` (`PythonFunctionTask`).

They enable things like:

* Querying external databases (AWS Athena, BigQuery, DuckDB, SQL, Snowflake, Hive).
* Executing specialized processing right in {{< key product_name >}} (Spark in virtual cluster, Dask in Virtual cluster, Sagemaker, Airflow, Modin, Ray, MPI and Horovod).
* Handing off processing to external services(AWS Batch, Spark on Databricks, Ray on external cluster).
* Data transformation (Great Expectations, DBT, Dolt, ONNX, Pandera).
* Data tracking and presentation  (MLFlow, Papermill).

See the [Integration section]() for examples.
<!-- TODO: Add link to API -->


<!-- TODO: INCORPORATE THE FOLLOWING ABOVE WHERE NECESSARY

## @{{< key kit_as >}}.task parameters

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
