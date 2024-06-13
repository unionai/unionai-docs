# Setting up the local environment

Here we will set up your local Python environment and install the required dependencies.

## Create a Python virtual environment

::::{tab-set}

:::{tab-item} conda
Install `conda` using [Miniconda](https://docs.anaconda.com/free/miniconda/index.html), then run the following to create a new Python environment:

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

## Clone the `examples` repository

After setting up an environment, clone the examples repository containing the
workflow

```{code-block} shell
$ git clone https://github.com/unionai/examples
```

## Install the dependencies

Now, install the required dependencies:

```{code-block} shell
$ cd examples
$ pip install -r guides/01_getting_started/ml_workflow/requirements.txt
```

This will install `unionai`, `scikit-learn`, `pandas`, and `matplotlib`.

## Next step

{@@ if serverless @@}

The next step is [Executing the workflow](executing-the-workflow).

{@@ elif byoc @@}

The next step is [Setting up container image handling](setting-up-container-image-handling).

{@@ endif @@}
