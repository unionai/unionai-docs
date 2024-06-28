# Example code components

You can find the full example code on [{fab}`github` Github](https://github.com/unionai/examples/blob/main/guides/01_getting_started/ml_workflow/ml_workflow.py)


## `@workflow`

The overall [workflow](https://docs.union.ai/core-concepts/workflows/) is a collection
of tasks that manages the data flow between tasks. Our standard workflow is defined using
a `@workflow` decorator the wraps a Python function:


```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 100-103
```

The workflow's `max_bins` parameter is automatically added to the `unionai run` CLI allowing
us to run `--max_bins 64` to configure the parameter.

-----

The `@workflow` decorator indicates a function that defines a **workflow**:

* A workflow appears to be a Python function but is actually a [DSL](https://en.wikipedia.org/wiki/Domain-specific_language) that only supports a subset of Python syntax and semantics.
* When deployed to Union, the workflow function is "compiled" to construct the directed acyclic graph of tasks, defining the order of execution of task pods and the data flow dependencies between them.

:::{admonition} Details on `@task` and `@workflow` syntax
* The `@task` and `@workflow` decorators are transparent to Python provided that they are used only on _functions at the top-level scope of the module_.
  You can invoke tasks and workflows as regular Python functions and even import and use them in other Python modules or scripts.
* Task and workflow function signatures must be _type-annotated with Python type hints_.
* Task and workflow functions must be _invoked with keyword arguments_.
:::

TK - link to core concepts page(s)

## `@task`

Each task is defined with a Python function that is decorated with a `@task` decorator.
For example, the `train_model` task is defined as follows:

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 55-64
```

We highlight some of features used to define the task:

1. Python typing is required for all inputs and outputs. Union uses the types for serialization
   and to validate workflows.
2. The `Resources(cpu="3", mem="2Gi")` is **declarative infrastructure** that allocates 3 CPUs
   and `2Gi` of memory for the task.
3. The `container_image=image` sets an image that has all the dependencies required by the task.

The task requires custom dependencies, which we specify with an `ImageSpec`:

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 36-38
```

The `requirements.txt` contain the same dependencies we used to configure our local development environment. The Union hosted image builder builds the image based
on the `ImageSpec` specification and uses that image for the machine learning workflow.

The `get_dataset` task uses a cache of the data outputs of the task:

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 41-52
```

`get_dataset` returns the training and test data as pandas DataFrames which gets cached by Union.
With caching, future executions of the workflow will use the cached data instead of running
the task again.

-----

The `@task` decorator indicates functions that define **tasks**:

* A task is a Python function that takes some inputs and produces an output.
* When deployed to a Kubernetes cluster, each task runs in its own Kubernetes pod.
* Tasks are assembled into workflows.

TK - link to core concepts page(s)

## `ImageSpec`

The `ImageSpec` object is used to define the container image that will run the tasks in the workflow.

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 36-38
```

In this example, the `requirements` parameter is set to the location of the requirements file that will be used to build the image. For a full list of parameters, see the [ImageSpec reference documentation](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.image_spec.ImageSpec.html#flytekit.image_spec.ImageSpec).

## Visualizations

The Flyte Deck feature allows you to enable visualizations in Union's user interface by setting `enable_deck=True` in a task's parameters:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 67-96
:emphasize-lines: 69
```

Enabling the deck adds the "Flyte Deck" button in the UI and task's code places the
visualizations into the deck.
