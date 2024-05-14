# Creating the project

## Wine classification example

To demonstrate the essential elements of a Union project, we will start with a simple model training workflow called `wine-classification`.
It consists of three steps:

1. Get the classic [wine dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-recognition-dataset) using [scikit-learn](https://scikit-learn.org/stable/).
2. Process the data that simplifies the 3-class prediction problem into a binary classification problem by consolidating class labels `1` and `2` into a single class.
3. Train a `LogisticRegression` model to learn a binary classifier.

## Create the project using pyflyte init

We will use the `pyflyte` (the CLI tool that ships with `flytekit`) to quickly initialize the project, from a template.
The `wine-classification` example is among the installable examples published in the GitHub repository [`flyteorg/flytekit-python-template`](https://github.com/flyteorg/flytekit-python-template).

Install the example, and `cd` into it:

```{code-block} shell
[~]:wine-classification
$ pyflyte init --template wine-classification wine-classification

[~]:wine-classification
$ cd wine-classification

[~/wine-classification]:wine-classification
$
```

:::{note}
If you need to use a Dockerfile in your project instead of ImageSpec, you can use the Dockerfile template:

```{code-block} shell
pyflyte init --template basic-template-dockerfile my_project
```
:::

## Project structure

If you examine the `wine-classification` directory you’ll see the following file structure:

```{code-block} shell
[~/wine-classification]:wine-classification
$ tree
.
├── LICENSE
├── README.md
├── local-requirements.txt
├── image-requirements.txt
└── workflows
    ├── __init__.py
    └── example.py
```

:::{note}
You can create your own conventions and file structure for your Union projects.
The `pyflyte init` command just provides a good starting point.
:::

## Install the local dependencies

We will explain the significance of the two requirements files later.
For now, you just need to install the local dependencies.
Make sure that you have activated your `wine-classification` conda environment, then install the dependencies from `local-requirements.txt`:

```{code-block} shell
[~/wine-classification]:wine-classification
$ pip install -r local-requirements.txt
```

