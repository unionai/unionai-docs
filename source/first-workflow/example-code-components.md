# Example code components

The ML workflow example code contains a `@workflow`-decorated function made up of several tasks decorated with the `@task` decorator. The code also contains an `ImageSpec` block, and tasks with the `enable_deck=True` parameter set, which enables visualizations in the Union UI.

```{note}
You can find the full ML workflow example code on [{fab}`github` Github](https://github.com/unionai/examples/blob/main/guides/01_getting_started/ml_workflow/ml_workflow.py)
```

## Workflow

The `@workflow` decorator indicates a function that defines a [workflow](../core-concepts/workflows/index). This function contains references to the tasks defined earlier in the code.

A workflow appears to be a Python function but is actually a [DSL](https://en.wikipedia.org/wiki/Domain-specific_language) that only supports a subset of Python syntax and semantics.

When deployed to Union, the workflow function is "compiled" to construct the directed acyclic graph (DAG) of tasks, defining the order of execution of task pods and the data flow dependencies between them.

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:pyobject: main
```

Workflow parameters are available for configuration on the command line. In this example, the `main` workflow's `max_bins` parameter can be set to a different value from the default:

```{code-block} shell
$ union run --remote guides/01_getting_started/ml_workflow/ml_workflow.py main --max_bins 128
```

:::{admonition} `@task` and `@workflow` syntax
* The `@task` and `@workflow` decorators will only work on functions at the top-level scope of the module.
* You can invoke tasks and workflows as regular Python functions and even import and use them in other Python modules or scripts.
* Task and workflow function signatures must be type-annotated with Python type hints.
* Task and workflow functions must be invoked with keyword arguments.
:::

## Tasks

The `@task` decorator indicates a Python function that defines a [**task**](../core-concepts/tasks/index). A task tasks some input and produces an output. When deployed to a Kubernetes cluster, each task runs in its own Kubernetes pod.

### `train_model`

The `train_model` task has the parameter `requests` set to `Resources(cpu="3", mem="2Gi")`, which is declarative infrastructure that allocates 3 CPUs and `2Gi` of memory for the task. This task also has the `container_image` parameter set, which specifies the image (defined in an `ImageSpec` block) to use for the task.

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:pyobject: train_model
```

### `get_dataset`

`get_dataset` returns the training and test data as pandas DataFrames. `cache=True` means that the task output is cached by Union. With caching, future executions of the workflow will use the cached data instead of running
the task again.

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:pyobject: get_dataset
```

```{note}
For a full list of task parameters, see [Task parameters](../core-concepts/tasks/task-parameters).
```

## ImageSpec

The `ImageSpec` object is used to define the container image that will run the tasks in the workflow. The tasks require custom dependencies, which are included in the `ImageSpec`:

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 36-38
```

The `requirements` parameter is set to the location of the requirements file that will be used to build the image. In this case, the `requirements` file is the same one that is used to configure the local development environment.

{@@ if serverless @@}

The Union-hosted image builder will build the image based on the `ImageSpec` definition and use it for designated tasks.

{@@ elif byoc @@}

You build the image on your local machine based on the `ImageSpec` definition and push it to the specified registry. When Union executes the workflow, it will pull the image from the registry and use it for the designated task.

{@@ endif @@}

## Visualizations

The Flyte Deck feature allows you to enable visualizations in Union's user interface by setting `enable_deck=True` in a task's parameters:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 67-96
:emphasize-lines: 3
```
