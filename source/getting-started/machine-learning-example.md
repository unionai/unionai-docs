# Machine learning example

In this tutorial, we learn about Union features by reviewing a
machine learning workflow using `flytekit`, `scikit-learn`, and `pandas`.
Before starting this tutorial, onboard to the Union platform by following the [Getting started ](index) section.

## Downloading the material

The material for this tutorial is available by downloading the following files and placing them in the same directory:

* <a href="_static/examples/getting-started/ml_workflow.py" download="ml_workflow.py">ml_workflow.py</a>- Contains the machine learning workflow
* <a href="_static/examples/getting-started/requirements.txt" download="requirements.txt">requirements.txt</a> - Contains the requirements for the workflow

## Setting up the development environment

First, we setup our Python environment and install the dependencies for this tutorial.

::::{tab-set}

:::{tab-item} conda
Install `conda` using [Miniconda](https://docs.anaconda.com/free/miniconda/index.html), then run the following to create
a new Python environment:

```shell
conda create -n ml-workflow python=3.11
conda activate ml-workflow
```
:::

:::{tab-item} venv
Install Python 3.8 or higher from your package manager or from [Python.org](https://www.python.org/downloads/), then run the following to create a virtual environment:

```shell
python -m venv .venv
source .venv/bin/activate
```
:::

::::

After setting up an environment install the requirements for this tutorial:

```{code-block} shell
pip install -r requirements.txt
```

## Executing the workflow

We execute the `ml_workflow.py` workflow on Union by running:

```{code-block} shell
unionai run --remote ml_workflow.py main --max_bins 64
```

Which outputs the following to the console, where the first URL points to the image builder and
the second URL is the workflow execution:

```{code-block} shell
👍 Build submitted!
⏳ Waiting for build to finish at: https://serverless-1.us-east-2.s.union.ai/org/...
✅ Build completed in 0:01:57!

[✔] Go to https://serverless-1.us-east-2.s.union.ai/org/... to see execution in the console.
```

When we run the workflow, it launches a Union hosted image builder that creates a image
with the Python dependencies required for the workflow. Afterwards, the machine learning
workflow executes with the image built from the previous step.

Open the second link to view the execution in Union's user interface and click on the "Graph" tab
to see a visualization of the workflow:

![Graph](/_static/images/getting-started-graph.jpg)

Above the graph, there is metadata that describes the workflow execution, such as the
duration and the workflow version. Next, click on the `evaluate_model` node to open up a
sidebar that contains additional information about the task:

![Sidebar](/_static/images/getting-started-full-sidebar.jpg)

The `Inputs` and `Outputs` tabs contains links to data coming into the task and the
task's output:

![Input-Output](/_static/images/getting-started-input-output.jpg)

Finally, click on the "Flyte Deck" button in the sidebar to open up visualizations generated
by the task:

![Flyte Deck](/_static/images/getting-started-flyte-deck.jpg)

Now that we are familiar with the UI, let's jump into the code and see how to build the
workflow!

## Diving into the code

### Defining a workflow

The overall [workflow](https://docs.union.ai/core-concepts/workflows/) is a collection
of tasks that manages the data flow between tasks. Our standard workflow is defined using
a `@workflow` decorator the wraps a Python function:

```{code-block} python
from flytekit import workflow

@workflow
def main(max_bins: int) -> float:
    train, test = get_dataset()
    model = train_model(dataset=train, max_bins=max_bins)
    return evaluate_model(model=model, dataset=test)
```

The workflow's `max_bins` parameter is automatically added to the `unionai run` CLI allowing
us to run `--max_bins 64` to configure the parameter.

### Defining a task

Each task is defined with a Python function that is decorated with a `@task` decorator.
For example, the `train_model` task is defined as follows:

```{code-block} python
from flytekit import task, Resources

@task(
    container_image=image,
    requests=Resources(cpu="3", mem="2Gi"),
)
def train_model(dataset: pd.DataFrame, max_bins: int) -> HistGradientBoostingClassifier:
    ...
```

We highlight some of features used to define the task:

1. Python typing is required for all inputs and outputs. Union uses the types for serialization
   and to validate workflows.
2. The `Resources(cpu="3", mem="2Gi")` is **declarative infrastructure** that allocates 3 CPUs
   and `2Gi` of memory for the task.
3. The `container_image=image` sets an image that has all the dependencies required by the task.

The task requires custom dependencies, which we specify with an `ImageSpec`:

```{code-block} python
from flytekit import ImageSpec

image = ImageSpec(
    builder="unionai",
    requirements="requirements.txt",
)
```

The `requirements.txt` contain the same dependencies we used to configure our local development
environment. The Union hosted image builder builds the image based
on the `ImageSpec` specification and use that image for the machine learning workflow.

The `get_dataset` task uses a cache the data outputs of the task:

```{code-block} python
@task(
    cache=True, cache_version="3", ...
)
def get_dataset() -> tuple[pd.DataFrame, pd.DataFrame]:
```

`get_dataset` returns the train and test data as pandas DataFrames which gets cached by Union.
With caching, future executions of the workflow will use the cached data instead of running
the task again.

### Visualizations

The Flyte Deck feature enables us to show custom visualizations in Union's user interface.
The visualizations is enabled with a single `enable_deck=True`:

```{code-block} python
@task(
    enable_deck=True, ...
)
def evaluate_model(
    model: HistGradientBoostingClassifier, dataset: pd.DataFrame
) -> float:
    ...
    report = classification_report(y_test, y_pred)
    # Code to place `report` into Flyte Deck
```

Enabling the deck adds the "Flyte Deck" button in the UI and task's code places the
visualizations into the deck.

## Conclusion

You can learn more about Union-specific capabilities by exploring this site or Flyte by
visiting [docs.flyte.org](https://docs.flyte.org/en/latest/).
