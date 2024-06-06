# Looking at the workflow code

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
