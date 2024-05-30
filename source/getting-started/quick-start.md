# Quick start

In this section, we give a quick introduction to writing and running workflows on Union Serverless.
Let's get started!

## Signing up for a Union Serverless account

* Sign up for Union Serverless at: [signup.union.ai](https://signup.union.ai).
* Once you've received confirmation that you're off the waitlist:
    * Navigate to [serverless-1.us-east-2.s.union.ai](https://serverless-1.us-east-2.s.union.ai) to see the dashboard:

![Dashboard](/_static/images/dashboard.png)

## Setting up your local environment

First, we need to setup our local Python environment and install `unionai`:

::::{tab-set}

:::{tab-item} conda
Install `conda` using [Miniconda](https://docs.anaconda.com/free/miniconda/index.html), then run the following to create
a new Python environment:

```{code-block} shell
conda create -n quick-start python=3.11
conda activate quick-start
```
:::

:::{tab-item} venv
Install Python from your package manager or from [Python.org](https://www.python.org/downloads/), then run the following to create a virtual environment:

```{code-block} shell
python -m venv .venv
source .venv/bin/activate
```
:::

::::

After configuring your environment, install the UnionAI SDK:

```{code-block} shell
pip install unionai
```

## Creating a simple workflow

Copy the following into a file called `hello.py`:

```{code-block} python
from flytekit import task, workflow

@task
def welcome(name: str) -> str:
    return f"Welcome to Serverless! {name}"

@workflow
def main(name: str) -> str:
    return welcome(name=name)
```

## Running the workflow

Workflows can be run on your machine in your local Python environment or pushed up to the cloud to run on Union Serverless.

To run the workflow locally:

```{code-block} shell
unionai run hello.py main --name "Union"
```

To run the workflow remotely on Union Serverless:

```{code-block} shell
unionai run --remote hello.py main --name "Union"
```

This command prints an URL that links to the execution on Union's UI:

```{code-block} shell
[✔] Go to https://serverless-1.us-east-2.s.union.ai/org/... to see execution in the console.
```

Now that you are logged into Union, you can learn more about the platform by reading the
[Getting started with a ML workflow tutorial](getting-started).
