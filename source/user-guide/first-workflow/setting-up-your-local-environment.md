# Setting up your local environment

Here we will set up your local Python environment and install the required dependencies.

## Create a Python virtual environment

::::{tab-set}

:::{tab-item} conda
Install `conda` using [Miniconda](https://docs.anaconda.com/free/miniconda/index.html), then run the following commands to create a new Python environment:

```shell
conda create -n ml-workflow python=3.11
conda activate ml-workflow
```
:::

:::{tab-item} venv
Install Python using your package manager or from [Python.org](https://www.python.org/downloads/), then run the following commands to create a virtual environment:

```shell
python -m venv venvs/ml_workflow_venv
source venvs/ml_workflow_venv/bin/activate
```
:::

::::

## Clone the `unionai/unionai-examples` repository

After setting up a virtual environment, clone the [`unionai/unionai-examples`](https://github.com/unionai/unionai-examples) repository:

```{code-block} shell
$ git clone https://github.com/unionai/unionai-examples
```

## Install the dependencies

Next, install the required dependencies:

```{code-block} shell
$ cd unionai-examples
$ pip install -r guide/first_workflows/ml_workflow/requirements.txt
```

## Next step

{@@ if serverless @@}

The next step is [Running the workflow](running-the-workflow).

{@@ elif byoc @@}

The next step is [Setting up container image handling](setting-up-container-image-handling).

{@@ endif @@}
