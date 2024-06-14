# Understanding the workflow code

You can find the full example code on [{fab}`github` Github](https://github.com/unionai/examples/blob/main/guides/01_getting_started/ml_workflow/ml_workflow.py)

## Defining a workflow

The overall [workflow](https://docs.union.ai/core-concepts/workflows/) is a collection
of tasks that manages the data flow between tasks. Our standard workflow is defined using
a `@workflow` decorator the wraps a Python function:


```{rli} https://raw.githubusercontent.com/unionai/examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 100-103
```

The workflow's `max_bins` parameter is automatically added to the `unionai run` CLI allowing
us to run `--max_bins 64` to configure the parameter.

## Defining a task

Each task is defined with a Python function that is decorated with a `@task` decorator.
For example, the `train_model` task is defined as follows:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
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

```{rli} https://raw.githubusercontent.com/unionai/examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 36-38
```

The `requirements.txt` contain the same dependencies we used to configure our local development environment. The Union hosted image builder builds the image based
on the `ImageSpec` specification and uses that image for the machine learning workflow.

The `get_dataset` task uses a cache of the data outputs of the task:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 41-52
```

`get_dataset` returns the training and test data as pandas DataFrames which gets cached by Union.
With caching, future executions of the workflow will use the cached data instead of running
the task again.

## Visualizations

The Flyte Deck feature enables us to show custom visualizations in Union's user interface.
The visualizations is enabled with a single `enable_deck=True`:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 67-96
```

Enabling the deck adds the "Flyte Deck" button in the UI and task's code places the
visualizations into the deck.

## Conclusion

You can learn more about Union-specific capabilities by exploring the
[Core Concepts](../core-concepts/index) section.









Now let's look at the actual workflow code.
Take a look at the file `workflows/example.py`:

```{code-block} python
import pandas as pd

from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from flytekit import ImageSpec, task, workflow

image_spec = ImageSpec(
    registry="ghcr.io/<my-github-org>",
    name="wine-classification-image",
    base_image="ghcr.io/flyteorg/flytekit:py3.11-latest",
    requirements="image-requirements.txt"
)

@task(container_image=image_spec)
def get_data() -> pd.DataFrame:
    """Get the wine dataset."""
    return load_wine(as_frame=True).frame

@task(container_image=image_spec)
def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Simplify the task from a 3-class to a binary classification problem."""
    return data.assign(target=lambda x: x["target"].where(x["target"] == 0, 1))

@task(container_image=image_spec)
def train_model(data: pd.DataFrame, hyperparameters: dict) -> LogisticRegression:
    """Train a model on the wine dataset."""
    features = data.drop("target", axis="columns")
    target = data["target"]
    return LogisticRegression(max_iter=3000, **hyperparameters).fit(features, target)

@workflow
def training_workflow(hyperparameters: dict = {"C": 0.1}) -> LogisticRegression:
    """Put all of the steps together into a single workflow."""
    data = get_data()
    processed_data = process_data(data=data)
    return train_model(
        data=processed_data,
        hyperparameters=hyperparameters,
    )
```

This example shows a few key features of Union workflow code:

## @task

The `@task` decorator indicates functions that define **tasks**:

* A task is a Python function that takes some inputs and produces an output.
* When deployed to a Kubernetes cluster, each task runs in its own Kubernetes pod.
* Tasks are assembled into workflows.

## @workflow

The `@workflow` decorator indicates a function that defines a **workflow**:

* A workflow appears to be a Python function but is actually a [DSL](https://en.wikipedia.org/wiki/Domain-specific_language) that only supports a subset of Python syntax and semantics.
* When deployed to Union, the workflow function is "compiled" to construct the directed acyclic graph of tasks, defining the order of execution of task pods and the data flow dependencies between them.

:::{admonition} Details on `@task` and `@workflow` syntax
* The `@task` and `@workflow` decorators are transparent to Python provided that they are used only on _functions at the top-level scope of the module_.
  You can invoke tasks and workflows as regular Python functions and even import and use them in other Python modules or scripts.
* Task and workflow function signatures must be _type-annotated with Python type hints_.
* Task and workflow functions must be _invoked with keyword arguments_.
:::

## ImageSpec

As mentioned in the previous section, the `ImageSpec` object is used to define the container image that will run the tasks in the workflow.

In this example, the following parameters are used:

* `registry="ghcr.io/<my-github-org>"`: The container registry to which your image will be pushed. **Make sure to replace `<my-github-org>` with your GitHub organization name**.
* `name="wine-classification-image"`: The name of the image that will be pushed to the container registry.
* `base_image="ghcr.io/flyteorg/flytekit:py3.11-latest"`: The base image that will be used to build your custom image. It is a good practice to use the latest version of the `flytekit` base image with the same version of Python as you have locally installed. The naming convention of the `flytekit` images is `flytekit:py<python-version>-<flytekit-version>`. **Recall that it is precisely because we are using a base image that includes `flytekit` that we do not need to include it in the `image-requirements.txt` file**.
* `requirements="image-requirements.txt"`: The requirements file that will be used to build the image. It is a good practice to have a separate requirements file for the image, as it will only include the packages needed to run the workflow in the container.
